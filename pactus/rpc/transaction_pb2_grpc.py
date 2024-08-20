# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc

from . import transaction_pb2 as transaction__pb2


class TransactionStub(object):
    """Transaction service defines various RPC methods for interacting with
    transactions.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetTransaction = channel.unary_unary(
            "/pactus.Transaction/GetTransaction",
            request_serializer=transaction__pb2.GetTransactionRequest.SerializeToString,
            response_deserializer=transaction__pb2.GetTransactionResponse.FromString,
        )
        self.CalculateFee = channel.unary_unary(
            "/pactus.Transaction/CalculateFee",
            request_serializer=transaction__pb2.CalculateFeeRequest.SerializeToString,
            response_deserializer=transaction__pb2.CalculateFeeResponse.FromString,
        )
        self.BroadcastTransaction = channel.unary_unary(
            "/pactus.Transaction/BroadcastTransaction",
            request_serializer=transaction__pb2.BroadcastTransactionRequest.SerializeToString,
            response_deserializer=transaction__pb2.BroadcastTransactionResponse.FromString,
        )
        self.GetRawTransferTransaction = channel.unary_unary(
            "/pactus.Transaction/GetRawTransferTransaction",
            request_serializer=transaction__pb2.GetRawTransferTransactionRequest.SerializeToString,
            response_deserializer=transaction__pb2.GetRawTransactionResponse.FromString,
        )
        self.GetRawBondTransaction = channel.unary_unary(
            "/pactus.Transaction/GetRawBondTransaction",
            request_serializer=transaction__pb2.GetRawBondTransactionRequest.SerializeToString,
            response_deserializer=transaction__pb2.GetRawTransactionResponse.FromString,
        )
        self.GetRawUnbondTransaction = channel.unary_unary(
            "/pactus.Transaction/GetRawUnbondTransaction",
            request_serializer=transaction__pb2.GetRawUnbondTransactionRequest.SerializeToString,
            response_deserializer=transaction__pb2.GetRawTransactionResponse.FromString,
        )
        self.GetRawWithdrawTransaction = channel.unary_unary(
            "/pactus.Transaction/GetRawWithdrawTransaction",
            request_serializer=transaction__pb2.GetRawWithdrawTransactionRequest.SerializeToString,
            response_deserializer=transaction__pb2.GetRawTransactionResponse.FromString,
        )


class TransactionServicer(object):
    """Transaction service defines various RPC methods for interacting with
    transactions.
    """

    def GetTransaction(self, request, context):
        """GetTransaction retrieves transaction details based on the provided request
        parameters.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CalculateFee(self, request, context):
        """CalculateFee calculates the transaction fee based on the specified amount
        and payload type.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def BroadcastTransaction(self, request, context):
        """BroadcastTransaction broadcasts a signed transaction to the network."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetRawTransferTransaction(self, request, context):
        """GetRawTransferTransaction retrieves raw details of a transfer transaction."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetRawBondTransaction(self, request, context):
        """GetRawBondTransaction retrieves raw details of a bond transaction."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetRawUnbondTransaction(self, request, context):
        """GetRawUnbondTransaction retrieves raw details of an unbond transaction."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetRawWithdrawTransaction(self, request, context):
        """GetRawWithdrawTransaction retrieves raw details of a withdraw transaction."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_TransactionServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "GetTransaction": grpc.unary_unary_rpc_method_handler(
            servicer.GetTransaction,
            request_deserializer=transaction__pb2.GetTransactionRequest.FromString,
            response_serializer=transaction__pb2.GetTransactionResponse.SerializeToString,
        ),
        "CalculateFee": grpc.unary_unary_rpc_method_handler(
            servicer.CalculateFee,
            request_deserializer=transaction__pb2.CalculateFeeRequest.FromString,
            response_serializer=transaction__pb2.CalculateFeeResponse.SerializeToString,
        ),
        "BroadcastTransaction": grpc.unary_unary_rpc_method_handler(
            servicer.BroadcastTransaction,
            request_deserializer=transaction__pb2.BroadcastTransactionRequest.FromString,
            response_serializer=transaction__pb2.BroadcastTransactionResponse.SerializeToString,
        ),
        "GetRawTransferTransaction": grpc.unary_unary_rpc_method_handler(
            servicer.GetRawTransferTransaction,
            request_deserializer=transaction__pb2.GetRawTransferTransactionRequest.FromString,
            response_serializer=transaction__pb2.GetRawTransactionResponse.SerializeToString,
        ),
        "GetRawBondTransaction": grpc.unary_unary_rpc_method_handler(
            servicer.GetRawBondTransaction,
            request_deserializer=transaction__pb2.GetRawBondTransactionRequest.FromString,
            response_serializer=transaction__pb2.GetRawTransactionResponse.SerializeToString,
        ),
        "GetRawUnbondTransaction": grpc.unary_unary_rpc_method_handler(
            servicer.GetRawUnbondTransaction,
            request_deserializer=transaction__pb2.GetRawUnbondTransactionRequest.FromString,
            response_serializer=transaction__pb2.GetRawTransactionResponse.SerializeToString,
        ),
        "GetRawWithdrawTransaction": grpc.unary_unary_rpc_method_handler(
            servicer.GetRawWithdrawTransaction,
            request_deserializer=transaction__pb2.GetRawWithdrawTransactionRequest.FromString,
            response_serializer=transaction__pb2.GetRawTransactionResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "pactus.Transaction", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Transaction(object):
    """Transaction service defines various RPC methods for interacting with
    transactions.
    """

    @staticmethod
    def GetTransaction(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/pactus.Transaction/GetTransaction",
            transaction__pb2.GetTransactionRequest.SerializeToString,
            transaction__pb2.GetTransactionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def CalculateFee(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/pactus.Transaction/CalculateFee",
            transaction__pb2.CalculateFeeRequest.SerializeToString,
            transaction__pb2.CalculateFeeResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def BroadcastTransaction(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/pactus.Transaction/BroadcastTransaction",
            transaction__pb2.BroadcastTransactionRequest.SerializeToString,
            transaction__pb2.BroadcastTransactionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetRawTransferTransaction(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/pactus.Transaction/GetRawTransferTransaction",
            transaction__pb2.GetRawTransferTransactionRequest.SerializeToString,
            transaction__pb2.GetRawTransactionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetRawBondTransaction(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/pactus.Transaction/GetRawBondTransaction",
            transaction__pb2.GetRawBondTransactionRequest.SerializeToString,
            transaction__pb2.GetRawTransactionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetRawUnbondTransaction(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/pactus.Transaction/GetRawUnbondTransaction",
            transaction__pb2.GetRawUnbondTransactionRequest.SerializeToString,
            transaction__pb2.GetRawTransactionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetRawWithdrawTransaction(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/pactus.Transaction/GetRawWithdrawTransaction",
            transaction__pb2.GetRawWithdrawTransactionRequest.SerializeToString,
            transaction__pb2.GetRawTransactionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
