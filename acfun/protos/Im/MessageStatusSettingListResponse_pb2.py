# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: MessageStatusSettingListResponse.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ChatSession_pb2 as ChatSession__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&MessageStatusSettingListResponse.proto\x12\x15\x41\x63\x46unDanmu.Im.Message\x1a\x11\x43hatSession.proto\"|\n MessageStatusSettingListResponse\x12\x33\n\x07session\x18\x01 \x03(\x0b\x32\".AcFunDanmu.Im.Message.ChatSession\x12\x12\n\nnextOffset\x18\x02 \x01(\t\x12\x0f\n\x07hasMore\x18\x03 \x01(\x08\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'MessageStatusSettingListResponse_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MESSAGESTATUSSETTINGLISTRESPONSE._serialized_start=84
  _MESSAGESTATUSSETTINGLISTRESPONSE._serialized_end=208
# @@protoc_insertion_point(module_scope)