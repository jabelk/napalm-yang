
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

class temperature(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-platform - based on the path /components/component/state/temperature. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Temperature in degrees Celsius of the component. Values include
the instantaneous, average, minimum, and maximum statistics. If
avg/min/max statistics are not supported, the target is expected
to just supply the instant value
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__instant','__avg','__min_','__max_','__interval','__alarm_status','__alarm_threshold','__alarm_severity',)

  _yang_name = 'temperature'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__instant = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=1), is_leaf=True, yang_name="instant", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='decimal64', is_config=False)
    self.__max_ = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=1), is_leaf=True, yang_name="max", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='decimal64', is_config=False)
    self.__interval = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='oc-types:stat-interval', is_config=False)
    self.__alarm_status = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="alarm-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='boolean', is_config=False)
    self.__min_ = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=1), is_leaf=True, yang_name="min", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='decimal64', is_config=False)
    self.__alarm_threshold = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="alarm-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='uint32', is_config=False)
    self.__avg = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=1), is_leaf=True, yang_name="avg", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='decimal64', is_config=False)
    self.__alarm_severity = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'MAJOR': {'@namespace': u'http://openconfig.net/yang/alarms/types', '@module': u'openconfig-alarm-types'}, u'oc-alarm-types:MAJOR': {'@namespace': u'http://openconfig.net/yang/alarms/types', '@module': u'openconfig-alarm-types'}, u'WARNING': {'@namespace': u'http://openconfig.net/yang/alarms/types', '@module': u'openconfig-alarm-types'}, u'oc-alarm-types:UNKNOWN': {'@namespace': u'http://openconfig.net/yang/alarms/types', '@module': u'openconfig-alarm-types'}, u'UNKNOWN': {'@namespace': u'http://openconfig.net/yang/alarms/types', '@module': u'openconfig-alarm-types'}, u'oc-alarm-types:WARNING': {'@namespace': u'http://openconfig.net/yang/alarms/types', '@module': u'openconfig-alarm-types'}, u'CRITICAL': {'@namespace': u'http://openconfig.net/yang/alarms/types', '@module': u'openconfig-alarm-types'}, u'oc-alarm-types:CRITICAL': {'@namespace': u'http://openconfig.net/yang/alarms/types', '@module': u'openconfig-alarm-types'}, u'MINOR': {'@namespace': u'http://openconfig.net/yang/alarms/types', '@module': u'openconfig-alarm-types'}, u'oc-alarm-types:MINOR': {'@namespace': u'http://openconfig.net/yang/alarms/types', '@module': u'openconfig-alarm-types'}},), is_leaf=True, yang_name="alarm-severity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='identityref', is_config=False)

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
      return [u'components', u'component', u'state', u'temperature']

  def _get_instant(self):
    """
    Getter method for instant, mapped from YANG variable /components/component/state/temperature/instant (decimal64)

    YANG Description: The instantaneous value of the statistic.
    """
    return self.__instant
      
  def _set_instant(self, v, load=False):
    """
    Setter method for instant, mapped from YANG variable /components/component/state/temperature/instant (decimal64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_instant is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_instant() directly.

    YANG Description: The instantaneous value of the statistic.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedPrecisionDecimalType(precision=1), is_leaf=True, yang_name="instant", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='decimal64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """instant must be of a type compatible with decimal64""",
          'defined-type': "decimal64",
          'generated-type': """YANGDynClass(base=RestrictedPrecisionDecimalType(precision=1), is_leaf=True, yang_name="instant", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='decimal64', is_config=False)""",
        })

    self.__instant = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_instant(self):
    self.__instant = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=1), is_leaf=True, yang_name="instant", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='decimal64', is_config=False)


  def _get_avg(self):
    """
    Getter method for avg, mapped from YANG variable /components/component/state/temperature/avg (decimal64)

    YANG Description: The arithmetic mean value of the statistic over the
sampling period.
    """
    return self.__avg
      
  def _set_avg(self, v, load=False):
    """
    Setter method for avg, mapped from YANG variable /components/component/state/temperature/avg (decimal64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_avg is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_avg() directly.

    YANG Description: The arithmetic mean value of the statistic over the
sampling period.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedPrecisionDecimalType(precision=1), is_leaf=True, yang_name="avg", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='decimal64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """avg must be of a type compatible with decimal64""",
          'defined-type': "decimal64",
          'generated-type': """YANGDynClass(base=RestrictedPrecisionDecimalType(precision=1), is_leaf=True, yang_name="avg", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='decimal64', is_config=False)""",
        })

    self.__avg = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_avg(self):
    self.__avg = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=1), is_leaf=True, yang_name="avg", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='decimal64', is_config=False)


  def _get_min_(self):
    """
    Getter method for min_, mapped from YANG variable /components/component/state/temperature/min (decimal64)

    YANG Description: The minimum value of the statistic over the sampling
period
    """
    return self.__min_
      
  def _set_min_(self, v, load=False):
    """
    Setter method for min_, mapped from YANG variable /components/component/state/temperature/min (decimal64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_min_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_min_() directly.

    YANG Description: The minimum value of the statistic over the sampling
period
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedPrecisionDecimalType(precision=1), is_leaf=True, yang_name="min", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='decimal64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """min_ must be of a type compatible with decimal64""",
          'defined-type': "decimal64",
          'generated-type': """YANGDynClass(base=RestrictedPrecisionDecimalType(precision=1), is_leaf=True, yang_name="min", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='decimal64', is_config=False)""",
        })

    self.__min_ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_min_(self):
    self.__min_ = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=1), is_leaf=True, yang_name="min", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='decimal64', is_config=False)


  def _get_max_(self):
    """
    Getter method for max_, mapped from YANG variable /components/component/state/temperature/max (decimal64)

    YANG Description: The maximum value of the statistic over the sampling
period
    """
    return self.__max_
      
  def _set_max_(self, v, load=False):
    """
    Setter method for max_, mapped from YANG variable /components/component/state/temperature/max (decimal64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_max_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_max_() directly.

    YANG Description: The maximum value of the statistic over the sampling
period
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedPrecisionDecimalType(precision=1), is_leaf=True, yang_name="max", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='decimal64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """max_ must be of a type compatible with decimal64""",
          'defined-type': "decimal64",
          'generated-type': """YANGDynClass(base=RestrictedPrecisionDecimalType(precision=1), is_leaf=True, yang_name="max", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='decimal64', is_config=False)""",
        })

    self.__max_ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_max_(self):
    self.__max_ = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=1), is_leaf=True, yang_name="max", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='decimal64', is_config=False)


  def _get_interval(self):
    """
    Getter method for interval, mapped from YANG variable /components/component/state/temperature/interval (oc-types:stat-interval)

    YANG Description: The time interval over which the min/max/average statistics
are computed by the system.
    """
    return self.__interval
      
  def _set_interval(self, v, load=False):
    """
    Setter method for interval, mapped from YANG variable /components/component/state/temperature/interval (oc-types:stat-interval)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interval() directly.

    YANG Description: The time interval over which the min/max/average statistics
are computed by the system.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='oc-types:stat-interval', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interval must be of a type compatible with oc-types:stat-interval""",
          'defined-type': "oc-types:stat-interval",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='oc-types:stat-interval', is_config=False)""",
        })

    self.__interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interval(self):
    self.__interval = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='oc-types:stat-interval', is_config=False)


  def _get_alarm_status(self):
    """
    Getter method for alarm_status, mapped from YANG variable /components/component/state/temperature/alarm_status (boolean)

    YANG Description: A value of true indicates the alarm has been raised or
asserted.  The value should be false when the alarm is
cleared.
    """
    return self.__alarm_status
      
  def _set_alarm_status(self, v, load=False):
    """
    Setter method for alarm_status, mapped from YANG variable /components/component/state/temperature/alarm_status (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_alarm_status is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_alarm_status() directly.

    YANG Description: A value of true indicates the alarm has been raised or
asserted.  The value should be false when the alarm is
cleared.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="alarm-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """alarm_status must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="alarm-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='boolean', is_config=False)""",
        })

    self.__alarm_status = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_alarm_status(self):
    self.__alarm_status = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="alarm-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='boolean', is_config=False)


  def _get_alarm_threshold(self):
    """
    Getter method for alarm_threshold, mapped from YANG variable /components/component/state/temperature/alarm_threshold (uint32)

    YANG Description: The threshold value that was crossed for this alarm.
    """
    return self.__alarm_threshold
      
  def _set_alarm_threshold(self, v, load=False):
    """
    Setter method for alarm_threshold, mapped from YANG variable /components/component/state/temperature/alarm_threshold (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_alarm_threshold is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_alarm_threshold() directly.

    YANG Description: The threshold value that was crossed for this alarm.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="alarm-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """alarm_threshold must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="alarm-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='uint32', is_config=False)""",
        })

    self.__alarm_threshold = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_alarm_threshold(self):
    self.__alarm_threshold = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="alarm-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='uint32', is_config=False)


  def _get_alarm_severity(self):
    """
    Getter method for alarm_severity, mapped from YANG variable /components/component/state/temperature/alarm_severity (identityref)

    YANG Description: The severity of the current alarm.
    """
    return self.__alarm_severity
      
  def _set_alarm_severity(self, v, load=False):
    """
    Setter method for alarm_severity, mapped from YANG variable /components/component/state/temperature/alarm_severity (identityref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_alarm_severity is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_alarm_severity() directly.

    YANG Description: The severity of the current alarm.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'MAJOR': {'@namespace': u'http://openconfig.net/yang/alarms/types', '@module': u'openconfig-alarm-types'}, u'oc-alarm-types:MAJOR': {'@namespace': u'http://openconfig.net/yang/alarms/types', '@module': u'openconfig-alarm-types'}, u'WARNING': {'@namespace': u'http://openconfig.net/yang/alarms/types', '@module': u'openconfig-alarm-types'}, u'oc-alarm-types:UNKNOWN': {'@namespace': u'http://openconfig.net/yang/alarms/types', '@module': u'openconfig-alarm-types'}, u'UNKNOWN': {'@namespace': u'http://openconfig.net/yang/alarms/types', '@module': u'openconfig-alarm-types'}, u'oc-alarm-types:WARNING': {'@namespace': u'http://openconfig.net/yang/alarms/types', '@module': u'openconfig-alarm-types'}, u'CRITICAL': {'@namespace': u'http://openconfig.net/yang/alarms/types', '@module': u'openconfig-alarm-types'}, u'oc-alarm-types:CRITICAL': {'@namespace': u'http://openconfig.net/yang/alarms/types', '@module': u'openconfig-alarm-types'}, u'MINOR': {'@namespace': u'http://openconfig.net/yang/alarms/types', '@module': u'openconfig-alarm-types'}, u'oc-alarm-types:MINOR': {'@namespace': u'http://openconfig.net/yang/alarms/types', '@module': u'openconfig-alarm-types'}},), is_leaf=True, yang_name="alarm-severity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='identityref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """alarm_severity must be of a type compatible with identityref""",
          'defined-type': "openconfig-platform:identityref",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'MAJOR': {'@namespace': u'http://openconfig.net/yang/alarms/types', '@module': u'openconfig-alarm-types'}, u'oc-alarm-types:MAJOR': {'@namespace': u'http://openconfig.net/yang/alarms/types', '@module': u'openconfig-alarm-types'}, u'WARNING': {'@namespace': u'http://openconfig.net/yang/alarms/types', '@module': u'openconfig-alarm-types'}, u'oc-alarm-types:UNKNOWN': {'@namespace': u'http://openconfig.net/yang/alarms/types', '@module': u'openconfig-alarm-types'}, u'UNKNOWN': {'@namespace': u'http://openconfig.net/yang/alarms/types', '@module': u'openconfig-alarm-types'}, u'oc-alarm-types:WARNING': {'@namespace': u'http://openconfig.net/yang/alarms/types', '@module': u'openconfig-alarm-types'}, u'CRITICAL': {'@namespace': u'http://openconfig.net/yang/alarms/types', '@module': u'openconfig-alarm-types'}, u'oc-alarm-types:CRITICAL': {'@namespace': u'http://openconfig.net/yang/alarms/types', '@module': u'openconfig-alarm-types'}, u'MINOR': {'@namespace': u'http://openconfig.net/yang/alarms/types', '@module': u'openconfig-alarm-types'}, u'oc-alarm-types:MINOR': {'@namespace': u'http://openconfig.net/yang/alarms/types', '@module': u'openconfig-alarm-types'}},), is_leaf=True, yang_name="alarm-severity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='identityref', is_config=False)""",
        })

    self.__alarm_severity = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_alarm_severity(self):
    self.__alarm_severity = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'MAJOR': {'@namespace': u'http://openconfig.net/yang/alarms/types', '@module': u'openconfig-alarm-types'}, u'oc-alarm-types:MAJOR': {'@namespace': u'http://openconfig.net/yang/alarms/types', '@module': u'openconfig-alarm-types'}, u'WARNING': {'@namespace': u'http://openconfig.net/yang/alarms/types', '@module': u'openconfig-alarm-types'}, u'oc-alarm-types:UNKNOWN': {'@namespace': u'http://openconfig.net/yang/alarms/types', '@module': u'openconfig-alarm-types'}, u'UNKNOWN': {'@namespace': u'http://openconfig.net/yang/alarms/types', '@module': u'openconfig-alarm-types'}, u'oc-alarm-types:WARNING': {'@namespace': u'http://openconfig.net/yang/alarms/types', '@module': u'openconfig-alarm-types'}, u'CRITICAL': {'@namespace': u'http://openconfig.net/yang/alarms/types', '@module': u'openconfig-alarm-types'}, u'oc-alarm-types:CRITICAL': {'@namespace': u'http://openconfig.net/yang/alarms/types', '@module': u'openconfig-alarm-types'}, u'MINOR': {'@namespace': u'http://openconfig.net/yang/alarms/types', '@module': u'openconfig-alarm-types'}, u'oc-alarm-types:MINOR': {'@namespace': u'http://openconfig.net/yang/alarms/types', '@module': u'openconfig-alarm-types'}},), is_leaf=True, yang_name="alarm-severity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='identityref', is_config=False)

  instant = __builtin__.property(_get_instant)
  avg = __builtin__.property(_get_avg)
  min_ = __builtin__.property(_get_min_)
  max_ = __builtin__.property(_get_max_)
  interval = __builtin__.property(_get_interval)
  alarm_status = __builtin__.property(_get_alarm_status)
  alarm_threshold = __builtin__.property(_get_alarm_threshold)
  alarm_severity = __builtin__.property(_get_alarm_severity)


  _pyangbind_elements = {'instant': instant, 'avg': avg, 'min_': min_, 'max_': max_, 'interval': interval, 'alarm_status': alarm_status, 'alarm_threshold': alarm_threshold, 'alarm_severity': alarm_severity, }


