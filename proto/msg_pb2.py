# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/msg.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fproto/msg.proto\x12\x07service\"+\n\x07Request\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\t\"-\n\x08Response\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\r\n\x05\x64\x61tas\x18\x02 \x01(\tB\x0fZ\rservice/protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.msg_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\rservice/proto'
  _globals['_REQUEST']._serialized_start=28
  _globals['_REQUEST']._serialized_end=71
  _globals['_RESPONSE']._serialized_start=73
  _globals['_RESPONSE']._serialized_end=118
# @@protoc_insertion_point(module_scope)