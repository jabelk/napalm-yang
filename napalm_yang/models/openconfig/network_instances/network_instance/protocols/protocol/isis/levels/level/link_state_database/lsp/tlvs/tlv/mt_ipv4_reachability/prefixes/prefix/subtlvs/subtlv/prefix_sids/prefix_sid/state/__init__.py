
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType
from pyangbind.lib.yangtypes import RestrictedClassType
from pyangbind.lib.yangtypes import TypedListType
from pyangbind.lib.yangtypes import YANGBool
from pyangbind.lib.yangtypes import YANGListType
from pyangbind.lib.yangtypes import YANGDynClass
from pyangbind.lib.yangtypes import ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import six

# PY3 support of some PY2 keywords (needs improved)
if six.PY3:
  import builtins as __builtin__
  long = int
  unicode = str
elif six.PY2:
  import __builtin__

class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/mt-ipv4-reachability/prefixes/prefix/subtlvs/subtlv/prefix-sids/prefix-sid/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters for Prefix-SID.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__value','__flags','__algorithm',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__flags = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NODE': {}, u'VALUE': {}, u'NO_PHP': {}, u'EXPLICIT_NULL': {}, u'READVERTISEMENT': {}, u'LOCAL': {}},)), is_leaf=False, yang_name="flags", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=False)
    self.__algorithm = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="algorithm", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    self.__value = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'levels', u'level', u'link-state-database', u'lsp', u'tlvs', u'tlv', u'mt-ipv4-reachability', u'prefixes', u'prefix', u'subtlvs', u'subtlv', u'prefix-sids', u'prefix-sid', u'state']

  def _get_value(self):
    """
    Getter method for value, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/subtlvs/subtlv/prefix_sids/prefix_sid/state/value (uint32)

    YANG Description: IGP Prefix-SID value.
    """
    return self.__value
      
  def _set_value(self, v, load=False):
    """
    Setter method for value, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/subtlvs/subtlv/prefix_sids/prefix_sid/state/value (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_value() directly.

    YANG Description: IGP Prefix-SID value.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """value must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)""",
        })

    self.__value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_value(self):
    self.__value = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)


  def _get_flags(self):
    """
    Getter method for flags, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/subtlvs/subtlv/prefix_sids/prefix_sid/state/flags (enumeration)

    YANG Description: Flags associated with Prefix Segment-ID.
    """
    return self.__flags
      
  def _set_flags(self, v, load=False):
    """
    Setter method for flags, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/subtlvs/subtlv/prefix_sids/prefix_sid/state/flags (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_flags is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_flags() directly.

    YANG Description: Flags associated with Prefix Segment-ID.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NODE': {}, u'VALUE': {}, u'NO_PHP': {}, u'EXPLICIT_NULL': {}, u'READVERTISEMENT': {}, u'LOCAL': {}},)), is_leaf=False, yang_name="flags", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """flags must be of a type compatible with enumeration""",
          'defined-type': "openconfig-network-instance:enumeration",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NODE': {}, u'VALUE': {}, u'NO_PHP': {}, u'EXPLICIT_NULL': {}, u'READVERTISEMENT': {}, u'LOCAL': {}},)), is_leaf=False, yang_name="flags", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=False)""",
        })

    self.__flags = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_flags(self):
    self.__flags = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NODE': {}, u'VALUE': {}, u'NO_PHP': {}, u'EXPLICIT_NULL': {}, u'READVERTISEMENT': {}, u'LOCAL': {}},)), is_leaf=False, yang_name="flags", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=False)


  def _get_algorithm(self):
    """
    Getter method for algorithm, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/subtlvs/subtlv/prefix_sids/prefix_sid/state/algorithm (uint8)

    YANG Description: Prefix-SID algorithm to be used for path computation.
    """
    return self.__algorithm
      
  def _set_algorithm(self, v, load=False):
    """
    Setter method for algorithm, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/subtlvs/subtlv/prefix_sids/prefix_sid/state/algorithm (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_algorithm is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_algorithm() directly.

    YANG Description: Prefix-SID algorithm to be used for path computation.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="algorithm", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """algorithm must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="algorithm", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)""",
        })

    self.__algorithm = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_algorithm(self):
    self.__algorithm = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="algorithm", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)

  value = __builtin__.property(_get_value)
  flags = __builtin__.property(_get_flags)
  algorithm = __builtin__.property(_get_algorithm)


  _pyangbind_elements = {'value': value, 'flags': flags, 'algorithm': algorithm, }


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/mt-ipv4-reachability/prefixes/prefix/subtlvs/subtlv/prefix-sids/prefix-sid/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters for Prefix-SID.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__value','__flags','__algorithm',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__flags = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NODE': {}, u'VALUE': {}, u'NO_PHP': {}, u'EXPLICIT_NULL': {}, u'READVERTISEMENT': {}, u'LOCAL': {}},)), is_leaf=False, yang_name="flags", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=False)
    self.__algorithm = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="algorithm", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    self.__value = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'levels', u'level', u'link-state-database', u'lsp', u'tlvs', u'tlv', u'mt-ipv4-reachability', u'prefixes', u'prefix', u'subtlvs', u'subtlv', u'prefix-sids', u'prefix-sid', u'state']

  def _get_value(self):
    """
    Getter method for value, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/subtlvs/subtlv/prefix_sids/prefix_sid/state/value (uint32)

    YANG Description: IGP Prefix-SID value.
    """
    return self.__value
      
  def _set_value(self, v, load=False):
    """
    Setter method for value, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/subtlvs/subtlv/prefix_sids/prefix_sid/state/value (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_value() directly.

    YANG Description: IGP Prefix-SID value.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """value must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)""",
        })

    self.__value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_value(self):
    self.__value = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)


  def _get_flags(self):
    """
    Getter method for flags, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/subtlvs/subtlv/prefix_sids/prefix_sid/state/flags (enumeration)

    YANG Description: Flags associated with Prefix Segment-ID.
    """
    return self.__flags
      
  def _set_flags(self, v, load=False):
    """
    Setter method for flags, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/subtlvs/subtlv/prefix_sids/prefix_sid/state/flags (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_flags is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_flags() directly.

    YANG Description: Flags associated with Prefix Segment-ID.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NODE': {}, u'VALUE': {}, u'NO_PHP': {}, u'EXPLICIT_NULL': {}, u'READVERTISEMENT': {}, u'LOCAL': {}},)), is_leaf=False, yang_name="flags", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """flags must be of a type compatible with enumeration""",
          'defined-type': "openconfig-network-instance:enumeration",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NODE': {}, u'VALUE': {}, u'NO_PHP': {}, u'EXPLICIT_NULL': {}, u'READVERTISEMENT': {}, u'LOCAL': {}},)), is_leaf=False, yang_name="flags", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=False)""",
        })

    self.__flags = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_flags(self):
    self.__flags = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NODE': {}, u'VALUE': {}, u'NO_PHP': {}, u'EXPLICIT_NULL': {}, u'READVERTISEMENT': {}, u'LOCAL': {}},)), is_leaf=False, yang_name="flags", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=False)


  def _get_algorithm(self):
    """
    Getter method for algorithm, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/subtlvs/subtlv/prefix_sids/prefix_sid/state/algorithm (uint8)

    YANG Description: Prefix-SID algorithm to be used for path computation.
    """
    return self.__algorithm
      
  def _set_algorithm(self, v, load=False):
    """
    Setter method for algorithm, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/subtlvs/subtlv/prefix_sids/prefix_sid/state/algorithm (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_algorithm is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_algorithm() directly.

    YANG Description: Prefix-SID algorithm to be used for path computation.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="algorithm", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """algorithm must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="algorithm", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)""",
        })

    self.__algorithm = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_algorithm(self):
    self.__algorithm = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="algorithm", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)

  value = __builtin__.property(_get_value)
  flags = __builtin__.property(_get_flags)
  algorithm = __builtin__.property(_get_algorithm)


  _pyangbind_elements = {'value': value, 'flags': flags, 'algorithm': algorithm, }


