# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wallet.proto
"""Generated protocol buffer code."""

from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import transaction_pb2 as transaction__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x0cwallet.proto\x12\x06pactus\x1a\x11transaction.proto"p\n\x0b\x41\x64\x64ressInfo\x12\x18\n\x07\x61\x64\x64ress\x18\x01 \x01(\tR\x07\x61\x64\x64ress\x12\x1d\n\npublic_key\x18\x02 \x01(\tR\tpublicKey\x12\x14\n\x05label\x18\x03 \x01(\tR\x05label\x12\x12\n\x04path\x18\x04 \x01(\tR\x04path"\xa5\x01\n\x0bHistoryInfo\x12%\n\x0etransaction_id\x18\x01 \x01(\tR\rtransactionId\x12\x12\n\x04time\x18\x02 \x01(\rR\x04time\x12!\n\x0cpayload_type\x18\x03 \x01(\tR\x0bpayloadType\x12 \n\x0b\x64\x65scription\x18\x04 \x01(\tR\x0b\x64\x65scription\x12\x16\n\x06\x61mount\x18\x05 \x01(\x03R\x06\x61mount"U\n\x18GetAddressHistoryRequest\x12\x1f\n\x0bwallet_name\x18\x01 \x01(\tR\nwalletName\x12\x18\n\x07\x61\x64\x64ress\x18\x02 \x01(\tR\x07\x61\x64\x64ress"S\n\x19GetAddressHistoryResponse\x12\x36\n\x0chistory_info\x18\x01 \x03(\x0b\x32\x13.pactus.HistoryInfoR\x0bhistoryInfo"\x85\x01\n\x14GetNewAddressRequest\x12\x1f\n\x0bwallet_name\x18\x01 \x01(\tR\nwalletName\x12\x36\n\x0c\x61\x64\x64ress_type\x18\x02 \x01(\x0e\x32\x13.pactus.AddressTypeR\x0b\x61\x64\x64ressType\x12\x14\n\x05label\x18\x03 \x01(\tR\x05label"p\n\x15GetNewAddressResponse\x12\x1f\n\x0bwallet_name\x18\x01 \x01(\tR\nwalletName\x12\x36\n\x0c\x61\x64\x64ress_info\x18\x02 \x01(\x0b\x32\x13.pactus.AddressInfoR\x0b\x61\x64\x64ressInfo"o\n\x14RestoreWalletRequest\x12\x1f\n\x0bwallet_name\x18\x01 \x01(\tR\nwalletName\x12\x1a\n\x08mnemonic\x18\x02 \x01(\tR\x08mnemonic\x12\x1a\n\x08password\x18\x03 \x01(\tR\x08password"8\n\x15RestoreWalletResponse\x12\x1f\n\x0bwallet_name\x18\x01 \x01(\tR\nwalletName"R\n\x13\x43reateWalletRequest\x12\x1f\n\x0bwallet_name\x18\x01 \x01(\tR\nwalletName\x12\x1a\n\x08password\x18\x04 \x01(\tR\x08password"2\n\x14\x43reateWalletResponse\x12\x1a\n\x08mnemonic\x18\x02 \x01(\tR\x08mnemonic"4\n\x11LoadWalletRequest\x12\x1f\n\x0bwallet_name\x18\x01 \x01(\tR\nwalletName"5\n\x12LoadWalletResponse\x12\x1f\n\x0bwallet_name\x18\x01 \x01(\tR\nwalletName"6\n\x13UnloadWalletRequest\x12\x1f\n\x0bwallet_name\x18\x01 \x01(\tR\nwalletName"7\n\x14UnloadWalletResponse\x12\x1f\n\x0bwallet_name\x18\x01 \x01(\tR\nwalletName";\n\x1aGetValidatorAddressRequest\x12\x1d\n\npublic_key\x18\x01 \x01(\tR\tpublicKey"7\n\x1bGetValidatorAddressResponse\x12\x18\n\x07\x61\x64\x64ress\x18\x01 \x01(\tR\x07\x61\x64\x64ress"\x81\x01\n\x19SignRawTransactionRequest\x12\x1f\n\x0bwallet_name\x18\x01 \x01(\tR\nwalletName\x12\'\n\x0fraw_transaction\x18\x02 \x01(\tR\x0erawTransaction\x12\x1a\n\x08password\x18\x03 \x01(\tR\x08password"y\n\x1aSignRawTransactionResponse\x12%\n\x0etransaction_id\x18\x01 \x01(\tR\rtransactionId\x12\x34\n\x16signed_raw_transaction\x18\x02 \x01(\tR\x14signedRawTransaction"9\n\x16GetTotalBalanceRequest\x12\x1f\n\x0bwallet_name\x18\x01 \x01(\tR\nwalletName"_\n\x17GetTotalBalanceResponse\x12\x1f\n\x0bwallet_name\x18\x01 \x01(\tR\nwalletName\x12#\n\rtotal_balance\x18\x02 \x01(\x03R\x0ctotalBalance"\x85\x01\n\x12SignMessageRequest\x12\x1f\n\x0bwallet_name\x18\x01 \x01(\tR\nwalletName\x12\x1a\n\x08password\x18\x02 \x01(\tR\x08password\x12\x18\n\x07\x61\x64\x64ress\x18\x03 \x01(\tR\x07\x61\x64\x64ress\x12\x18\n\x07message\x18\x04 \x01(\tR\x07message"3\n\x13SignMessageResponse\x12\x1c\n\tsignature\x18\x01 \x01(\tR\tsignature*b\n\x0b\x41\x64\x64ressType\x12\x19\n\x15\x41\x44\x44RESS_TYPE_TREASURY\x10\x00\x12\x1a\n\x16\x41\x44\x44RESS_TYPE_VALIDATOR\x10\x01\x12\x1c\n\x18\x41\x44\x44RESS_TYPE_BLS_ACCOUNT\x10\x02\x32\xb2\x06\n\x06Wallet\x12I\n\x0c\x43reateWallet\x12\x1b.pactus.CreateWalletRequest\x1a\x1c.pactus.CreateWalletResponse\x12L\n\rRestoreWallet\x12\x1c.pactus.RestoreWalletRequest\x1a\x1d.pactus.RestoreWalletResponse\x12\x43\n\nLoadWallet\x12\x19.pactus.LoadWalletRequest\x1a\x1a.pactus.LoadWalletResponse\x12I\n\x0cUnloadWallet\x12\x1b.pactus.UnloadWalletRequest\x1a\x1c.pactus.UnloadWalletResponse\x12R\n\x0fGetTotalBalance\x12\x1e.pactus.GetTotalBalanceRequest\x1a\x1f.pactus.GetTotalBalanceResponse\x12[\n\x12SignRawTransaction\x12!.pactus.SignRawTransactionRequest\x1a".pactus.SignRawTransactionResponse\x12^\n\x13GetValidatorAddress\x12".pactus.GetValidatorAddressRequest\x1a#.pactus.GetValidatorAddressResponse\x12L\n\rGetNewAddress\x12\x1c.pactus.GetNewAddressRequest\x1a\x1d.pactus.GetNewAddressResponse\x12X\n\x11GetAddressHistory\x12 .pactus.GetAddressHistoryRequest\x1a!.pactus.GetAddressHistoryResponse\x12\x46\n\x0bSignMessage\x12\x1a.pactus.SignMessageRequest\x1a\x1b.pactus.SignMessageResponseBA\n\rpactus.walletZ0github.com/pactus-project/pactus/www/grpc/pactusb\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "wallet_pb2", globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = (
        b"\n\rpactus.walletZ0github.com/pactus-project/pactus/www/grpc/pactus"
    )
    _ADDRESSTYPE._serialized_start = 1994
    _ADDRESSTYPE._serialized_end = 2092
    _ADDRESSINFO._serialized_start = 43
    _ADDRESSINFO._serialized_end = 155
    _HISTORYINFO._serialized_start = 158
    _HISTORYINFO._serialized_end = 323
    _GETADDRESSHISTORYREQUEST._serialized_start = 325
    _GETADDRESSHISTORYREQUEST._serialized_end = 410
    _GETADDRESSHISTORYRESPONSE._serialized_start = 412
    _GETADDRESSHISTORYRESPONSE._serialized_end = 495
    _GETNEWADDRESSREQUEST._serialized_start = 498
    _GETNEWADDRESSREQUEST._serialized_end = 631
    _GETNEWADDRESSRESPONSE._serialized_start = 633
    _GETNEWADDRESSRESPONSE._serialized_end = 745
    _RESTOREWALLETREQUEST._serialized_start = 747
    _RESTOREWALLETREQUEST._serialized_end = 858
    _RESTOREWALLETRESPONSE._serialized_start = 860
    _RESTOREWALLETRESPONSE._serialized_end = 916
    _CREATEWALLETREQUEST._serialized_start = 918
    _CREATEWALLETREQUEST._serialized_end = 1000
    _CREATEWALLETRESPONSE._serialized_start = 1002
    _CREATEWALLETRESPONSE._serialized_end = 1052
    _LOADWALLETREQUEST._serialized_start = 1054
    _LOADWALLETREQUEST._serialized_end = 1106
    _LOADWALLETRESPONSE._serialized_start = 1108
    _LOADWALLETRESPONSE._serialized_end = 1161
    _UNLOADWALLETREQUEST._serialized_start = 1163
    _UNLOADWALLETREQUEST._serialized_end = 1217
    _UNLOADWALLETRESPONSE._serialized_start = 1219
    _UNLOADWALLETRESPONSE._serialized_end = 1274
    _GETVALIDATORADDRESSREQUEST._serialized_start = 1276
    _GETVALIDATORADDRESSREQUEST._serialized_end = 1335
    _GETVALIDATORADDRESSRESPONSE._serialized_start = 1337
    _GETVALIDATORADDRESSRESPONSE._serialized_end = 1392
    _SIGNRAWTRANSACTIONREQUEST._serialized_start = 1395
    _SIGNRAWTRANSACTIONREQUEST._serialized_end = 1524
    _SIGNRAWTRANSACTIONRESPONSE._serialized_start = 1526
    _SIGNRAWTRANSACTIONRESPONSE._serialized_end = 1647
    _GETTOTALBALANCEREQUEST._serialized_start = 1649
    _GETTOTALBALANCEREQUEST._serialized_end = 1706
    _GETTOTALBALANCERESPONSE._serialized_start = 1708
    _GETTOTALBALANCERESPONSE._serialized_end = 1803
    _SIGNMESSAGEREQUEST._serialized_start = 1806
    _SIGNMESSAGEREQUEST._serialized_end = 1939
    _SIGNMESSAGERESPONSE._serialized_start = 1941
    _SIGNMESSAGERESPONSE._serialized_end = 1992
    _WALLET._serialized_start = 2095
    _WALLET._serialized_end = 2913
# @@protoc_insertion_point(module_scope)
