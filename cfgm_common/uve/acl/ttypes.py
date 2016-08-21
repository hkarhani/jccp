#
# Autogenerated by Sandesh Compiler (1.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:new_style
# Copyright (c) 2013 Juniper Networks, Inc. All rights reserved.
#

from pysandesh.Thrift import TType, TMessageType, TException

from pysandesh.transport import TTransport
from pysandesh.protocol import TBinaryProtocol, TProtocol
try:
  from pysandesh.protocol import fastbinary
except:
  fastbinary = None

import cStringIO
import uuid
import bottle
from pysandesh import sandesh_base
from pysandesh.sandesh_http import SandeshHttp
from pysandesh.sandesh_uve import SandeshUVETypeMaps
from pysandesh.util import UTCTimestampUsec, UTCTimestampUsecToString
from pysandesh.gen_py.sandesh.constants import *



class AclRuleToVnPolicyRule(object):
  """
  Attributes:
   - acl_major
   - acl_minor
   - policy_or_group_name
   - policy_major
   - policy_minor
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'acl_major', None, None, ), # 1
    (2, TType.I32, 'acl_minor', None, None, ), # 2
    (3, TType.STRING, 'policy_or_group_name', None, None, ), # 3
    (4, TType.I32, 'policy_major', None, None, ), # 4
    (5, TType.I32, 'policy_minor', None, None, ), # 5
  )

  def __init__(self, acl_major=None, acl_minor=None, policy_or_group_name=None, policy_major=None, policy_minor=None,):
    self.acl_major = acl_major
    self.acl_minor = acl_minor
    self.policy_or_group_name = policy_or_group_name
    self.policy_major = policy_major
    self.policy_minor = policy_minor

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return 0
    read_cnt = 0
    length = iprot.readStructBegin()
    if length < 0: return -1
    read_cnt += length
    while True:
      (length, fname, ftype, fid) = iprot.readFieldBegin()
      if length < 0: return -1
      read_cnt += length
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          (length, self.acl_major) = iprot.readI32();
          if length < 0: return -1
          read_cnt += length
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          (length, self.acl_minor) = iprot.readI32();
          if length < 0: return -1
          read_cnt += length
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          (length, self.policy_or_group_name) = iprot.readString();
          if length < 0: return -1
          read_cnt += length
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I32:
          (length, self.policy_major) = iprot.readI32();
          if length < 0: return -1
          read_cnt += length
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.I32:
          (length, self.policy_minor) = iprot.readI32();
          if length < 0: return -1
          read_cnt += length
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      length = iprot.readFieldEnd()
      if length < 0: return -1
      read_cnt += length
    length = iprot.readStructEnd()
    if length < 0: return -1
    read_cnt += length
    return read_cnt

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return 0
    if oprot.writeStructBegin('AclRuleToVnPolicyRule') < 0: return -1
    if self.acl_major is not None:
      annotations = {}
      if oprot.writeFieldBegin('acl_major', TType.I32, 1, annotations) < 0: return -1
      if oprot.writeI32(self.acl_major) < 0: return -1
      if oprot.writeFieldEnd() < 0: return -1
    if self.acl_minor is not None:
      annotations = {}
      if oprot.writeFieldBegin('acl_minor', TType.I32, 2, annotations) < 0: return -1
      if oprot.writeI32(self.acl_minor) < 0: return -1
      if oprot.writeFieldEnd() < 0: return -1
    if self.policy_or_group_name is not None:
      annotations = {}
      if oprot.writeFieldBegin('policy_or_group_name', TType.STRING, 3, annotations) < 0: return -1
      if oprot.writeString(self.policy_or_group_name) < 0: return -1
      if oprot.writeFieldEnd() < 0: return -1
    if self.policy_major is not None:
      annotations = {}
      if oprot.writeFieldBegin('policy_major', TType.I32, 4, annotations) < 0: return -1
      if oprot.writeI32(self.policy_major) < 0: return -1
      if oprot.writeFieldEnd() < 0: return -1
    if self.policy_minor is not None:
      annotations = {}
      if oprot.writeFieldBegin('policy_minor', TType.I32, 5, annotations) < 0: return -1
      if oprot.writeI32(self.policy_minor) < 0: return -1
      if oprot.writeFieldEnd() < 0: return -1
    if oprot.writeFieldStop() < 0: return -1
    if oprot.writeStructEnd() < 0: return -1
    return 0

  def validate(self):
    return


  def log(self):
    log_str = cStringIO.StringIO()
    if self.acl_major is not None:
      log_str.write('acl_major = ')
      log_str.write(str(self.acl_major))
      log_str.write('  ')
    if self.acl_minor is not None:
      log_str.write('acl_minor = ')
      log_str.write(str(self.acl_minor))
      log_str.write('  ')
    if self.policy_or_group_name is not None:
      log_str.write('policy_or_group_name = ')
      log_str.write(self.policy_or_group_name)
      log_str.write('  ')
    if self.policy_major is not None:
      log_str.write('policy_major = ')
      log_str.write(str(self.policy_major))
      log_str.write('  ')
    if self.policy_minor is not None:
      log_str.write('policy_minor = ')
      log_str.write(str(self.policy_minor))
      log_str.write('  ')
    return log_str.getvalue()

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class UveAclConfig(object):
  """
  Attributes:
   - virtual_network
   - attached_policies
   - acl_rule_to_policy
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'virtual_network', None, None, ), # 1
    (2, TType.LIST, 'attached_policies', (TType.STRING,None), None, ), # 2
    (3, TType.LIST, 'acl_rule_to_policy', (TType.STRUCT,(AclRuleToVnPolicyRule, AclRuleToVnPolicyRule.thrift_spec)), None, ), # 3
  )

  def __init__(self, virtual_network=None, attached_policies=None, acl_rule_to_policy=None,):
    self.virtual_network = virtual_network
    self.attached_policies = attached_policies
    self.acl_rule_to_policy = acl_rule_to_policy

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return 0
    read_cnt = 0
    length = iprot.readStructBegin()
    if length < 0: return -1
    read_cnt += length
    while True:
      (length, fname, ftype, fid) = iprot.readFieldBegin()
      if length < 0: return -1
      read_cnt += length
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          (length, self.virtual_network) = iprot.readString();
          if length < 0: return -1
          read_cnt += length
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.LIST:
          self.attached_policies = []
          (length, _etype3, _size0) = iprot.readListBegin()
          read_cnt += length
          for _i4 in xrange(_size0):
            read_cnt += iprot.readContainerElementBegin()
            (length, _elem5) = iprot.readString();
            if length < 0: return -1
            read_cnt += length
            self.attached_policies.append(_elem5)
            read_cnt += iprot.readContainerElementEnd()
          read_cnt += iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.LIST:
          self.acl_rule_to_policy = []
          (length, _etype9, _size6) = iprot.readListBegin()
          read_cnt += length
          for _i10 in xrange(_size6):
            _elem11 = AclRuleToVnPolicyRule()
            read_cnt += _elem11.read(iprot)
            self.acl_rule_to_policy.append(_elem11)
          read_cnt += iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      length = iprot.readFieldEnd()
      if length < 0: return -1
      read_cnt += length
    length = iprot.readStructEnd()
    if length < 0: return -1
    read_cnt += length
    return read_cnt

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return 0
    if oprot.writeStructBegin('UveAclConfig') < 0: return -1
    if self.virtual_network is not None:
      annotations = {}
      if oprot.writeFieldBegin('virtual_network', TType.STRING, 1, annotations) < 0: return -1
      if oprot.writeString(self.virtual_network) < 0: return -1
      if oprot.writeFieldEnd() < 0: return -1
    if self.attached_policies is not None:
      annotations = {}
      if oprot.writeFieldBegin('attached_policies', TType.LIST, 2, annotations) < 0: return -1
      if oprot.writeListBegin(TType.STRING, len(self.attached_policies)) < 0: return -1
      for iter12 in self.attached_policies:
        if oprot.writeContainerElementBegin() < 0: return -1
        if oprot.writeString(iter12) < 0: return -1
        if oprot.writeContainerElementEnd() < 0: return -1
      if oprot.writeListEnd() < 0: return -1
      if oprot.writeFieldEnd() < 0: return -1
    if self.acl_rule_to_policy is not None:
      annotations = {}
      if oprot.writeFieldBegin('acl_rule_to_policy', TType.LIST, 3, annotations) < 0: return -1
      if oprot.writeListBegin(TType.STRUCT, len(self.acl_rule_to_policy)) < 0: return -1
      for iter13 in self.acl_rule_to_policy:
        if iter13.write(oprot) < 0: return -1
      if oprot.writeListEnd() < 0: return -1
      if oprot.writeFieldEnd() < 0: return -1
    if oprot.writeFieldStop() < 0: return -1
    if oprot.writeStructEnd() < 0: return -1
    return 0

  def validate(self):
    return


  def log(self):
    log_str = cStringIO.StringIO()
    if self.virtual_network is not None:
      log_str.write('virtual_network = ')
      log_str.write(self.virtual_network)
      log_str.write('  ')
    if self.attached_policies is not None:
      log_str.write('attached_policies = ')
      log_str.write('[ ')
      for iter14 in self.attached_policies:
        log_str.write(iter14)
        log_str.write(', ')
      log_str.write(' ]')
      log_str.write('  ')
    if self.acl_rule_to_policy is not None:
      log_str.write('acl_rule_to_policy = ')
      log_str.write('[ ')
      for iter15 in self.acl_rule_to_policy:
        log_str.write('<<  ')
        log_str.write(iter15.log())
        log_str.write('>>')
        log_str.write(', ')
      log_str.write(' ]')
      log_str.write('  ')
    return log_str.getvalue()

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class UveAclVirtualNetworkConfig(object):
  """
  Attributes:
   - name
   - deleted
   - config
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'name', None, None, ), # 1
    (2, TType.BOOL, 'deleted', None, None, ), # 2
    (3, TType.STRUCT, 'config', (UveAclConfig, UveAclConfig.thrift_spec), None, ), # 3
  )

  def __init__(self, name=None, deleted=None, config=None,):
    self.name = name
    self.deleted = deleted
    self.config = config
    self._table = 'ObjectVNTable'

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return 0
    read_cnt = 0
    length = iprot.readStructBegin()
    if length < 0: return -1
    read_cnt += length
    while True:
      (length, fname, ftype, fid) = iprot.readFieldBegin()
      if length < 0: return -1
      read_cnt += length
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          (length, self.name) = iprot.readString();
          if length < 0: return -1
          read_cnt += length
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.BOOL:
          (length, self.deleted) = iprot.readBool();
          if length < 0: return -1
          read_cnt += length
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRUCT:
          self.config = UveAclConfig()
          read_cnt += self.config.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      length = iprot.readFieldEnd()
      if length < 0: return -1
      read_cnt += length
    length = iprot.readStructEnd()
    if length < 0: return -1
    read_cnt += length
    return read_cnt

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return 0
    if oprot.writeStructBegin('UveAclVirtualNetworkConfig') < 0: return -1
    if self.name is not None:
      annotations = {}
      if self._table is None or self._table is '': return -1
      annotations['key'] = self._table
      if oprot.writeFieldBegin('name', TType.STRING, 1, annotations) < 0: return -1
      if oprot.writeString(self.name) < 0: return -1
      if oprot.writeFieldEnd() < 0: return -1
    if self.deleted is not None:
      annotations = {}
      if oprot.writeFieldBegin('deleted', TType.BOOL, 2, annotations) < 0: return -1
      if oprot.writeBool(self.deleted) < 0: return -1
      if oprot.writeFieldEnd() < 0: return -1
    if self.config is not None:
      annotations = {}
      if oprot.writeFieldBegin('config', TType.STRUCT, 3, annotations) < 0: return -1
      if self.config.write(oprot) < 0: return -1
      if oprot.writeFieldEnd() < 0: return -1
    if oprot.writeFieldStop() < 0: return -1
    if oprot.writeStructEnd() < 0: return -1
    return 0

  def validate(self):
    return


  def log(self):
    log_str = cStringIO.StringIO()
    if self.name is not None:
      log_str.write('name = ')
      log_str.write(self.name)
      log_str.write('  ')
    if self.deleted is not None:
      log_str.write('deleted = ')
      if self.deleted:
        log_str.write('True')
      else:
        log_str.write('False')
      log_str.write('  ')
    if self.config is not None:
      log_str.write('config = ')
      log_str.write('<<  ')
      log_str.write(self.config.log())
      log_str.write('>>')
      log_str.write('  ')
    return log_str.getvalue()

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class UveAclVirtualMachineConfig(object):
  """
  Attributes:
   - name
   - deleted
   - config
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'name', None, None, ), # 1
    (2, TType.BOOL, 'deleted', None, None, ), # 2
    (3, TType.STRUCT, 'config', (UveAclConfig, UveAclConfig.thrift_spec), None, ), # 3
  )

  def __init__(self, name=None, deleted=None, config=None,):
    self.name = name
    self.deleted = deleted
    self.config = config
    self._table = 'ObjectVMTable'

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return 0
    read_cnt = 0
    length = iprot.readStructBegin()
    if length < 0: return -1
    read_cnt += length
    while True:
      (length, fname, ftype, fid) = iprot.readFieldBegin()
      if length < 0: return -1
      read_cnt += length
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          (length, self.name) = iprot.readString();
          if length < 0: return -1
          read_cnt += length
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.BOOL:
          (length, self.deleted) = iprot.readBool();
          if length < 0: return -1
          read_cnt += length
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRUCT:
          self.config = UveAclConfig()
          read_cnt += self.config.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      length = iprot.readFieldEnd()
      if length < 0: return -1
      read_cnt += length
    length = iprot.readStructEnd()
    if length < 0: return -1
    read_cnt += length
    return read_cnt

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return 0
    if oprot.writeStructBegin('UveAclVirtualMachineConfig') < 0: return -1
    if self.name is not None:
      annotations = {}
      if self._table is None or self._table is '': return -1
      annotations['key'] = self._table
      if oprot.writeFieldBegin('name', TType.STRING, 1, annotations) < 0: return -1
      if oprot.writeString(self.name) < 0: return -1
      if oprot.writeFieldEnd() < 0: return -1
    if self.deleted is not None:
      annotations = {}
      if oprot.writeFieldBegin('deleted', TType.BOOL, 2, annotations) < 0: return -1
      if oprot.writeBool(self.deleted) < 0: return -1
      if oprot.writeFieldEnd() < 0: return -1
    if self.config is not None:
      annotations = {}
      if oprot.writeFieldBegin('config', TType.STRUCT, 3, annotations) < 0: return -1
      if self.config.write(oprot) < 0: return -1
      if oprot.writeFieldEnd() < 0: return -1
    if oprot.writeFieldStop() < 0: return -1
    if oprot.writeStructEnd() < 0: return -1
    return 0

  def validate(self):
    return


  def log(self):
    log_str = cStringIO.StringIO()
    if self.name is not None:
      log_str.write('name = ')
      log_str.write(self.name)
      log_str.write('  ')
    if self.deleted is not None:
      log_str.write('deleted = ')
      if self.deleted:
        log_str.write('True')
      else:
        log_str.write('False')
      log_str.write('  ')
    if self.config is not None:
      log_str.write('config = ')
      log_str.write('<<  ')
      log_str.write(self.config.log())
      log_str.write('>>')
      log_str.write('  ')
    return log_str.getvalue()

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class UveAclVirtualNetworkConfigTrace(sandesh_base.SandeshUVE):

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'data', (UveAclVirtualNetworkConfig, UveAclVirtualNetworkConfig.thrift_spec), None, ), # 1
  )

  def __init__(self, data=None, table=None, sandesh=sandesh_base.sandesh_global):
    sandesh_base.SandeshUVE.__init__(self)
    self.data = data
    self._scope = sandesh.scope()
    self._module = sandesh.module()
    self._source = sandesh.source_id()
    self._node_type = sandesh.node_type()
    self._instance_id = sandesh.instance_id()
    self._seqnum = 0
    self._timestamp = UTCTimestampUsec()
    self._versionsig = 1124326490
    self._hints = 0 | SANDESH_KEY_HINT
    if table is not None:
      self.data._table = table

  def update_uve(self, tdata):
    if self.data.name is not None:
      tdata.name = self.data.name
    if self.data.deleted is not None:
      tdata.deleted = self.data.deleted
    if self.data.config is not None:
      tdata.config = self.data.config
    return tdata

  def log(self, trace=False):
    log_str = cStringIO.StringIO()
    if trace:
      log_str.write(str(self._timestamp))
      log_str.write(' ')
    log_str.write('UveAclVirtualNetworkConfigTrace: ')                                                                                                                                                                         
    if self.data is not None:
      log_str.write('data = ')
      log_str.write('<<  ')
      log_str.write(self.data.log())
      log_str.write('>>')
      log_str.write('  ')
    return log_str.getvalue()

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return -1
    read_cnt = 0
    (length, sandesh_name) = iprot.readSandeshBegin()
    if length < 0: return -1
    read_cnt += length
    while True:
      (length, fname, ftype, fid) = iprot.readFieldBegin()
      if length < 0: return -1
      read_cnt += length
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.data = UveAclVirtualNetworkConfig()
          read_cnt += self.data.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      length = iprot.readFieldEnd()
      if length < 0: return -1
      read_cnt += length
    length = iprot.readSandeshEnd()
    if length < 0: return -1
    read_cnt += length
    return read_cnt

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return 0
    if oprot.writeSandeshBegin('UveAclVirtualNetworkConfigTrace') < 0: return -1
    if self.data is not None:
      annotations = {}
      if oprot.writeFieldBegin('data', TType.STRUCT, 1, annotations) < 0: return -1
      if self.data.write(oprot) < 0: return -1
      if oprot.writeFieldEnd() < 0: return -1
    if oprot.writeFieldStop() < 0: return -1
    if oprot.writeSandeshEnd() < 0: return -1
    return 0

  def validate(self):
    return


  def compare(self, other):
    if not isinstance(other, self.__class__):
      return False
    if self.data != other.data:
      return False
    return True

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class UveAclVirtualMachineConfigTrace(sandesh_base.SandeshUVE):

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'data', (UveAclVirtualMachineConfig, UveAclVirtualMachineConfig.thrift_spec), None, ), # 1
  )

  def __init__(self, data=None, table=None, sandesh=sandesh_base.sandesh_global):
    sandesh_base.SandeshUVE.__init__(self)
    self.data = data
    self._scope = sandesh.scope()
    self._module = sandesh.module()
    self._source = sandesh.source_id()
    self._node_type = sandesh.node_type()
    self._instance_id = sandesh.instance_id()
    self._seqnum = 0
    self._timestamp = UTCTimestampUsec()
    self._versionsig = 1124326490
    self._hints = 0 | SANDESH_KEY_HINT
    if table is not None:
      self.data._table = table

  def update_uve(self, tdata):
    if self.data.name is not None:
      tdata.name = self.data.name
    if self.data.deleted is not None:
      tdata.deleted = self.data.deleted
    if self.data.config is not None:
      tdata.config = self.data.config
    return tdata

  def log(self, trace=False):
    log_str = cStringIO.StringIO()
    if trace:
      log_str.write(str(self._timestamp))
      log_str.write(' ')
    log_str.write('UveAclVirtualMachineConfigTrace: ')                                                                                                                                                                         
    if self.data is not None:
      log_str.write('data = ')
      log_str.write('<<  ')
      log_str.write(self.data.log())
      log_str.write('>>')
      log_str.write('  ')
    return log_str.getvalue()

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return -1
    read_cnt = 0
    (length, sandesh_name) = iprot.readSandeshBegin()
    if length < 0: return -1
    read_cnt += length
    while True:
      (length, fname, ftype, fid) = iprot.readFieldBegin()
      if length < 0: return -1
      read_cnt += length
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.data = UveAclVirtualMachineConfig()
          read_cnt += self.data.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      length = iprot.readFieldEnd()
      if length < 0: return -1
      read_cnt += length
    length = iprot.readSandeshEnd()
    if length < 0: return -1
    read_cnt += length
    return read_cnt

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return 0
    if oprot.writeSandeshBegin('UveAclVirtualMachineConfigTrace') < 0: return -1
    if self.data is not None:
      annotations = {}
      if oprot.writeFieldBegin('data', TType.STRUCT, 1, annotations) < 0: return -1
      if self.data.write(oprot) < 0: return -1
      if oprot.writeFieldEnd() < 0: return -1
    if oprot.writeFieldStop() < 0: return -1
    if oprot.writeSandeshEnd() < 0: return -1
    return 0

  def validate(self):
    return


  def compare(self, other):
    if not isinstance(other, self.__class__):
      return False
    if self.data != other.data:
      return False
    return True

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)


_SANDESH_REQUEST_LIST = [
]


_SANDESH_UVE_LIST = [
'UveAclVirtualNetworkConfigTrace',
'UveAclVirtualMachineConfigTrace',
]


_SANDESH_UVE_DATA_LIST = [
'UveAclVirtualNetworkConfig',
'UveAclVirtualMachineConfig',
]


_SANDESH_ALARM_LIST = [
]


_SANDESH_ALARM_DATA_LIST = [
]
