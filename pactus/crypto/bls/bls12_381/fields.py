#!/usr/bin/python
#
# implementation of Fp and Fp^2 operations
#
# This file is derived from `fields.py` in the Chia BLS signatures Python implementation,
#     https://github.com/Chia-Network/bls-signatures/
# which is (C) 2018 Chia Network Inc. and licensed under the Apache 2.0 license.
# See copyright notice at the end of this file.
#
# Changes from the original version:
# * Some unneeded functionality was removed and some pylint errors were fixed.
# * added trivial __reversed__ method to Fq to support generic sgn0 impl
# * q -> p in frob_coeffs for consistency with the rest of this library
# * moved sgn0 and sqrt_F2 into this file

from copy import deepcopy

from .consts import p


# "sign" of x: returns -1 if x is the lexically larger of x and -1 * x, else returns 1
def sgn0_be(x):
    thresh = (p - 1) // 2
    sign = 0
    for xi in reversed(x):
        if xi > thresh:
            sign = -1 if sign == 0 else sign
        elif xi > 0:
            sign = 1 if sign == 0 else sign
    sign = 1 if sign == 0 else sign
    return sign


# "sign" of x: returns -1 if x is "negative", else returns 1
# this is a "little-endian" signedness test
def sgn0(x):
    sign = 0
    zero = 1
    for xi in x:
        sign_i = xi % 2
        zero_i = xi == 0
        sign = sign | (zero & sign_i)
        zero = zero & zero_i
    return 1 - 2 * sign


class Fq(int):
    """
    Represents an element of a finite field mod a prime q.
    """

    Q = None
    extension = 1

    def __new__(cls, Q, x):
        ret = super().__new__(cls, x % Q)
        ret.Q = Q
        return ret

    def __neg__(self):
        return Fq(self.Q, super().__neg__())

    def __add__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        return Fq(self.Q, super().__add__(other))

    def __radd__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        return self.__add__(other)

    def __sub__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        return Fq(self.Q, super().__sub__(other))

    def __rsub__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        return Fq(self.Q, super().__rsub__(other))

    def __mul__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        return Fq(self.Q, super().__mul__(other))

    def __rmul__(self, other):
        return self.__mul__(other)

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return super().__eq__(other)
        return super().__eq__(other) and self.Q == other.Q

    def __str__(self):
        s = hex(int(self))
        s2 = s[0:7] + ".." + s[-5:] if len(s) > 10 else s
        return "Fq(" + s2 + ")"

    def __repr__(self):
        return "Fq(" + hex(int(self)) + ")"

    def __pow__(self, other):
        if other == 0:
            return Fq(self.Q, 1)
        if other == 1:
            return self
        if other % 2 == 0:
            return (self * self) ** (other // 2)
        return (self * self) ** (other // 2) * self

    def qi_power(self, _):
        return self

    def __invert__(self):
        """
        Extended euclidian algorithm for inversion.
        """
        x0, x1, y0, y1 = 1, 0, 0, 1
        a = int(self.Q)
        b = int(self)
        while a != 0:
            q, b, a = b // a, a, b % a
            x0, x1 = x1, x0 - q * x1
            y0, y1 = y1, y0 - q * y1
        return Fq(self.Q, x0)

    def __floordiv__(self, other):
        if isinstance(other, int) and not isinstance(other, type(self)):
            other = Fq(self.Q, other)
        return self * ~other

    __truediv__ = __floordiv__

    def __iter__(self):
        yield self

    def __reversed__(self):
        yield self

    def __deepcopy__(self, memo):
        return Fq(self.Q, int(self))

    @classmethod
    def zero(cls, Q):
        return Fq(Q, 0)

    @classmethod
    def one(cls, Q):
        return Fq(Q, 1)

    @classmethod
    def from_fq(cls, _, fq):
        return fq


class FieldExtBase(tuple):
    """
    Represents an extension of a field (or extension of an extension).
    The elements of the tuple can be other FieldExtBase or they can be
    Fq elements. For example, Fq2 = (Fq, Fq). Fq12 = (Fq6, Fq6), etc.
    """

    extension = None
    basefield = None
    embedding = None
    root = None
    Q = None

    def __new__(cls, Q, *args):
        new_args = args[:]
        try:
            arg_extension = args[0].extension
            args[1].extension  # pylint: disable=pointless-statement
        except AttributeError:
            if len(args) != 2:
                raise Exception("Invalid number of arguments")
            arg_extension = 1
            new_args = [Fq(Q, a) for a in args]
        if arg_extension != 1:
            if len(args) != cls.embedding:
                raise Exception("Invalid number of arguments")
            for arg in new_args:
                assert arg.extension == arg_extension
        assert all(
            isinstance(arg, cls.basefield if cls.basefield is not Fq else int)
            for arg in new_args
        )
        ret = super().__new__(cls, new_args)
        ret.Q = Q
        return ret

    def __neg__(self):
        cls = type(self)
        ret = super().__new__(cls, (-x for x in self))
        ret.Q = self.Q
        ret.root = self.root
        return ret

    def __add__(self, other):
        cls = type(self)
        if not isinstance(other, cls):
            if type(other) != int and other.extension > self.extension:  # pylint: disable=unidiomatic-typecheck
                return NotImplemented
            other_new = [cls.basefield.zero(self.Q) for _ in self]
            other_new[0] = other_new[0] + other
        else:
            other_new = other

        ret = super().__new__(cls, (a + b for a, b in zip(self, other_new)))
        ret.Q = self.Q
        ret.root = self.root
        return ret

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return self + (-other)

    def __rsub__(self, other):
        return (-self) + other

    def __mul__(self, other):
        cls = type(self)
        if isinstance(other, int):
            ret = super().__new__(cls, (a * other for a in self))
            ret.Q = self.Q
            ret.root = self.root
            return ret
        if cls.extension < other.extension:
            return NotImplemented

        buf = [cls.basefield.zero(self.Q) for _ in self]

        for i, x in enumerate(self):
            if cls.extension == other.extension:
                for j, y in enumerate(other):
                    if x and y:
                        if i + j >= self.embedding:
                            buf[(i + j) % self.embedding] += x * y * self.root
                        else:
                            buf[(i + j) % self.embedding] += x * y
            else:
                if x:
                    buf[i] = x * other
        ret = super().__new__(cls, buf)
        ret.Q = self.Q
        ret.root = self.root
        return ret

    def __rmul__(self, other):
        return self.__mul__(other)

    def __floordiv__(self, other):
        return self * ~other

    __truediv__ = __floordiv__

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            if isinstance(other, (FieldExtBase, int)):
                if (
                    not isinstance(other, FieldExtBase)
                    or self.extension > other.extension
                ):
                    for i in range(1, self.embedding):
                        if self[i] != (type(self.root).zero(self.Q)):
                            return False
                    return self[0] == other
                return NotImplemented
            return NotImplemented
        return super().__eq__(other) and self.Q == other.Q

    def __lt__(self, other):
        # Reverse the order for comparison (3i + 1 > 2i + 7)
        return self[::-1].__lt__(other[::-1])

    def __neq__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return (
            "Fq"
            + str(self.extension)
            + "("
            + ", ".join([a.__str__() for a in self])
            + ")"
        )

    def __repr__(self):
        return (
            "Fq"
            + str(self.extension)
            + "("
            + ", ".join([a.__repr__() for a in self])
            + ")"
        )

    def __pow__(self, e):
        assert isinstance(e, int) and e >= 0
        ans = type(self).one(self.Q)
        base = self
        ans.root = self.root

        while e:
            if e & 1:
                ans *= base

            base *= base
            e >>= 1

        return ans

    def __bool__(self):
        return any(x for x in self)

    def set_root(self, _root):
        self.root = _root

    @classmethod
    def zero(cls, Q):
        return cls.from_fq(Q, Fq(Q, 0))

    @classmethod
    def one(cls, Q):
        return cls.from_fq(Q, Fq(Q, 1))

    @classmethod
    def from_fq(cls, Q, fq):
        y = cls.basefield.from_fq(Q, fq)
        z = cls.basefield.zero(Q)
        ret = super().__new__(cls, (z if i else y for i in range(cls.embedding)))
        ret.Q = Q
        if cls == Fq2:
            ret.set_root(Fq(Q, -1))
        elif cls == Fq6:
            ret.set_root(Fq2(Q, Fq.one(Q), Fq.one(Q)))
        elif cls == Fq12:
            r = Fq6(Q, Fq2.zero(Q), Fq2.one(Q), Fq2.zero(Q))
            ret.set_root(r)
        return ret

    def __deepcopy__(self, memo):
        cls = type(self)
        ret = super().__new__(cls, (deepcopy(a, memo) for a in self))
        ret.Q = self.Q
        ret.root = self.root
        return ret

    def qi_power(self, i):
        cls = type(self)
        i %= cls.extension
        if i == 0:
            return self
        ret = super().__new__(
            cls,
            (
                a.qi_power(i) * frob_coeffs[cls.extension, i, j] if j else a.qi_power(i)
                for j, a in enumerate(self)
            ),
        )
        ret.Q = self.Q
        ret.root = self.root
        return ret


class Fq2(FieldExtBase):
    # Fq2 is constructed as Fq(u) / (u^2 - i) where i = -1
    extension = 2
    embedding = 2
    basefield = Fq

    def __init__(self, Q, *_):
        # pylint: disable=super-init-not-called
        super().set_root(Fq(Q, -1))

    def __invert__(self):
        a, b = self
        factor = ~(a * a + b * b)
        ret = Fq2(self.Q, a * factor, -b * factor)
        return ret

    def mul_by_nonresidue(self):
        # multiply by u + 1
        a, b = self
        return Fq2(self.Q, a - b, a + b)


# roots of unity, used for computing square roots in Fq2
rv1 = 0x6AF0E0437FF400B6831E36D6BD17FFE48395DABC2D3435E77F76E17009241C5EE67992F72EC05F4C81084FBEDE3CC09
roots_of_unity = (Fq2(p, 1, 0), Fq2(p, 0, 1), Fq2(p, rv1, rv1), Fq2(p, rv1, p - rv1))
del rv1


# sqrt function -- returns None when input is nonsquare
def sqrt_F2(val):
    sqrt_cand = pow(val, (p**2 + 7) // 16)
    ret = None
    for root in roots_of_unity:
        tmp = sqrt_cand * root
        ret = tmp if pow(tmp, 2) == val else ret
    return ret


class Fq6(FieldExtBase):
    # Fq6 is constructed as Fq2(v) / (v^3 - j) where j = u + 1
    extension = 6
    embedding = 3
    basefield = Fq2

    def __init__(self, Q, *_):
        # pylint: disable=super-init-not-called
        super().set_root(Fq2(Q, Fq.one(Q), Fq.one(Q)))

    def __invert__(self):
        a, b, c = self
        g0 = a * a - b * c.mul_by_nonresidue()
        g1 = (c * c).mul_by_nonresidue() - a * b
        g2 = b * b - a * c
        factor = ~(g0 * a + (g1 * c + g2 * b).mul_by_nonresidue())
        # TODO(mariano54): no inverse  pylint: disable=fixme
        return Fq6(self.Q, g0 * factor, g1 * factor, g2 * factor)

    def mul_by_nonresidue(self):
        # multiply by v
        a, b, c = self
        return Fq6(self.Q, c * self.root, a, b)


class Fq12(FieldExtBase):
    # Fq12 is constructed as Fq6(w) / (w^2 - k) where k = v
    extension = 12
    embedding = 2
    basefield = Fq6

    def __init__(self, Q, *_):
        # pylint: disable=super-init-not-called
        super().set_root(Fq6(Q, Fq2.zero(Q), Fq2.one(Q), Fq2.zero(Q)))

    def __invert__(self):
        a, b = self
        factor = ~(a * a - (b * b).mul_by_nonresidue())
        return Fq12(self.Q, a * factor, -b * factor)


# Frobenius coefficients for raising elements to q**i -th powers
# These are specific to this given q
frob_coeffs = {
    (2, 1, 1): Fq(p, -1),
    (6, 1, 1): Fq2(
        p,
        Fq(p, 0x0),
        Fq(
            p,
            0x1A0111EA397FE699EC02408663D4DE85AA0D857D89759AD4897D29650FB85F9B409427EB4F49FFFD8BFD00000000AAAC,
        ),
    ),
    (6, 1, 2): Fq2(
        p,
        Fq(
            p,
            0x1A0111EA397FE699EC02408663D4DE85AA0D857D89759AD4897D29650FB85F9B409427EB4F49FFFD8BFD00000000AAAD,
        ),
        Fq(p, 0x0),
    ),
    (6, 2, 1): Fq2(
        p,
        Fq(
            p,
            0x5F19672FDF76CE51BA69C6076A0F77EADDB3A93BE6F89688DE17D813620A00022E01FFFFFFFEFFFE,
        ),
        Fq(p, 0x0),
    ),
    (6, 2, 2): Fq2(
        p,
        Fq(
            p,
            0x1A0111EA397FE699EC02408663D4DE85AA0D857D89759AD4897D29650FB85F9B409427EB4F49FFFD8BFD00000000AAAC,
        ),
        Fq(p, 0x0),
    ),
    (6, 3, 1): Fq2(p, Fq(p, 0x0), Fq(p, 0x1)),
    (6, 3, 2): Fq2(
        p,
        Fq(
            p,
            0x1A0111EA397FE69A4B1BA7B6434BACD764774B84F38512BF6730D2A0F6B0F6241EABFFFEB153FFFFB9FEFFFFFFFFAAAA,
        ),
        Fq(p, 0x0),
    ),
    (6, 4, 1): Fq2(
        p,
        Fq(
            p,
            0x1A0111EA397FE699EC02408663D4DE85AA0D857D89759AD4897D29650FB85F9B409427EB4F49FFFD8BFD00000000AAAC,
        ),
        Fq(p, 0x0),
    ),
    (6, 4, 2): Fq2(
        p,
        Fq(
            p,
            0x5F19672FDF76CE51BA69C6076A0F77EADDB3A93BE6F89688DE17D813620A00022E01FFFFFFFEFFFE,
        ),
        Fq(p, 0x0),
    ),
    (6, 5, 1): Fq2(
        p,
        Fq(p, 0x0),
        Fq(
            p,
            0x5F19672FDF76CE51BA69C6076A0F77EADDB3A93BE6F89688DE17D813620A00022E01FFFFFFFEFFFE,
        ),
    ),
    (6, 5, 2): Fq2(
        p,
        Fq(
            p,
            0x5F19672FDF76CE51BA69C6076A0F77EADDB3A93BE6F89688DE17D813620A00022E01FFFFFFFEFFFF,
        ),
        Fq(p, 0x0),
    ),
    (12, 1, 1): Fq6(
        p,
        Fq2(
            p,
            Fq(
                p,
                0x1904D3BF02BB0667C231BEB4202C0D1F0FD603FD3CBD5F4F7B2443D784BAB9C4F67EA53D63E7813D8D0775ED92235FB8,
            ),
            Fq(
                p,
                0xFC3E2B36C4E03288E9E902231F9FB854A14787B6C7B36FEC0C8EC971F63C5F282D5AC14D6C7EC22CF78A126DDC4AF3,
            ),
        ),
        Fq2(p, Fq(p, 0x0), Fq(p, 0x0)),
        Fq2(p, Fq(p, 0x0), Fq(p, 0x0)),
    ),
    (12, 2, 1): Fq6(
        p,
        Fq2(
            p,
            Fq(
                p,
                0x5F19672FDF76CE51BA69C6076A0F77EADDB3A93BE6F89688DE17D813620A00022E01FFFFFFFEFFFF,
            ),
            Fq(p, 0x0),
        ),
        Fq2(p, Fq(p, 0x0), Fq(p, 0x0)),
        Fq2(p, Fq(p, 0x0), Fq(p, 0x0)),
    ),
    (12, 3, 1): Fq6(
        p,
        Fq2(
            p,
            Fq(
                p,
                0x135203E60180A68EE2E9C448D77A2CD91C3DEDD930B1CF60EF396489F61EB45E304466CF3E67FA0AF1EE7B04121BDEA2,
            ),
            Fq(
                p,
                0x6AF0E0437FF400B6831E36D6BD17FFE48395DABC2D3435E77F76E17009241C5EE67992F72EC05F4C81084FBEDE3CC09,
            ),
        ),
        Fq2(p, Fq(p, 0x0), Fq(p, 0x0)),
        Fq2(p, Fq(p, 0x0), Fq(p, 0x0)),
    ),
    (12, 4, 1): Fq6(
        p,
        Fq2(
            p,
            Fq(
                p,
                0x5F19672FDF76CE51BA69C6076A0F77EADDB3A93BE6F89688DE17D813620A00022E01FFFFFFFEFFFE,
            ),
            Fq(p, 0x0),
        ),
        Fq2(p, Fq(p, 0x0), Fq(p, 0x0)),
        Fq2(p, Fq(p, 0x0), Fq(p, 0x0)),
    ),
    (12, 5, 1): Fq6(
        p,
        Fq2(
            p,
            Fq(
                p,
                0x144E4211384586C16BD3AD4AFA99CC9170DF3560E77982D0DB45F3536814F0BD5871C1908BD478CD1EE605167FF82995,
            ),
            Fq(
                p,
                0x5B2CFD9013A5FD8DF47FA6B48B1E045F39816240C0B8FEE8BEADF4D8E9C0566C63A3E6E257F87329B18FAE980078116,
            ),
        ),
        Fq2(p, Fq(p, 0x0), Fq(p, 0x0)),
        Fq2(p, Fq(p, 0x0), Fq(p, 0x0)),
    ),
    (12, 6, 1): Fq6(
        p,
        Fq2(
            p,
            Fq(
                p,
                0x1A0111EA397FE69A4B1BA7B6434BACD764774B84F38512BF6730D2A0F6B0F6241EABFFFEB153FFFFB9FEFFFFFFFFAAAA,
            ),
            Fq(p, 0x0),
        ),
        Fq2(p, Fq(p, 0x0), Fq(p, 0x0)),
        Fq2(p, Fq(p, 0x0), Fq(p, 0x0)),
    ),
    (12, 7, 1): Fq6(
        p,
        Fq2(
            p,
            Fq(
                p,
                0xFC3E2B36C4E03288E9E902231F9FB854A14787B6C7B36FEC0C8EC971F63C5F282D5AC14D6C7EC22CF78A126DDC4AF3,
            ),
            Fq(
                p,
                0x1904D3BF02BB0667C231BEB4202C0D1F0FD603FD3CBD5F4F7B2443D784BAB9C4F67EA53D63E7813D8D0775ED92235FB8,
            ),
        ),
        Fq2(p, Fq(p, 0x0), Fq(p, 0x0)),
        Fq2(p, Fq(p, 0x0), Fq(p, 0x0)),
    ),
    (12, 8, 1): Fq6(
        p,
        Fq2(
            p,
            Fq(
                p,
                0x1A0111EA397FE699EC02408663D4DE85AA0D857D89759AD4897D29650FB85F9B409427EB4F49FFFD8BFD00000000AAAC,
            ),
            Fq(p, 0x0),
        ),
        Fq2(p, Fq(p, 0x0), Fq(p, 0x0)),
        Fq2(p, Fq(p, 0x0), Fq(p, 0x0)),
    ),
    (12, 9, 1): Fq6(
        p,
        Fq2(
            p,
            Fq(
                p,
                0x6AF0E0437FF400B6831E36D6BD17FFE48395DABC2D3435E77F76E17009241C5EE67992F72EC05F4C81084FBEDE3CC09,
            ),
            Fq(
                p,
                0x135203E60180A68EE2E9C448D77A2CD91C3DEDD930B1CF60EF396489F61EB45E304466CF3E67FA0AF1EE7B04121BDEA2,
            ),
        ),
        Fq2(p, Fq(p, 0x0), Fq(p, 0x0)),
        Fq2(p, Fq(p, 0x0), Fq(p, 0x0)),
    ),
    (12, 10, 1): Fq6(
        p,
        Fq2(
            p,
            Fq(
                p,
                0x1A0111EA397FE699EC02408663D4DE85AA0D857D89759AD4897D29650FB85F9B409427EB4F49FFFD8BFD00000000AAAD,
            ),
            Fq(p, 0x0),
        ),
        Fq2(p, Fq(p, 0x0), Fq(p, 0x0)),
        Fq2(p, Fq(p, 0x0), Fq(p, 0x0)),
    ),
    (12, 11, 1): Fq6(
        p,
        Fq2(
            p,
            Fq(
                p,
                0x5B2CFD9013A5FD8DF47FA6B48B1E045F39816240C0B8FEE8BEADF4D8E9C0566C63A3E6E257F87329B18FAE980078116,
            ),
            Fq(
                p,
                0x144E4211384586C16BD3AD4AFA99CC9170DF3560E77982D0DB45F3536814F0BD5871C1908BD478CD1EE605167FF82995,
            ),
        ),
        Fq2(p, Fq(p, 0x0), Fq(p, 0x0)),
        Fq2(p, Fq(p, 0x0), Fq(p, 0x0)),
    ),
}

# Copyright 2018 Chia Network Inc
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
