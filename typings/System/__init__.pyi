import typing, clr, abc
from System.Collections import IDictionary, IList, IStructuralEquatable, IStructuralComparable, IEnumerator, IComparer, IEqualityComparer
from System.Reflection import MethodBase, MethodInfo, BindingFlags, Binder, Assembly, AssemblyName, MemberInfo, ParameterInfo, Module, IReflect, MemberFilter, TypeAttributes, CustomAttributeData, GenericParameterAttributes, MemberTypes, ConstructorInfo, TypeFilter, InterfaceMapping, ParameterModifier, CallingConventions, EventInfo, FieldInfo, PropertyInfo
from System.Runtime.Remoting import ObjectHandle
from System.Globalization import CultureInfo, NumberStyles, UnicodeCategory, Calendar, DateTimeStyles, CompareOptions, CompareInfo, TimeSpanStyles, DaylightTime
from System.Collections.Generic import IEnumerable_1, IComparer_1, IReadOnlyList_1, IList_1, IEnumerator_1, IEqualityComparer_1
from System.Collections.ObjectModel import ReadOnlyCollection_1
from System.Runtime.Serialization import SerializationInfo, StreamingContext, ISerializable, IDeserializationCallback, IObjectReference
from System.Security import PermissionSet
from System.Security.Principal import PrincipalPolicy, IPrincipal
from System.Configuration.Assemblies import AssemblyHashAlgorithm
from System.IO import TextWriter, TextReader, Stream
from System.Text import Encoding, SpanLineEnumerator, SpanRuneEnumerator, StringRuneEnumerator, NormalizationForm
from System.Threading.Tasks import ValueTask
from System.Threading import WaitHandle, LazyThreadSafetyMode, CancellationToken
from System.Buffers import MemoryHandle, SpanAction_2
from System.Runtime.CompilerServices import DefaultInterpolatedStringHandler
from System.Runtime.InteropServices import StructLayoutAttribute

class AccessViolationException(SystemException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, innerException: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...


class Action_GenericClasses(abc.ABCMeta):
    Generic_Action_GenericClasses_Action_1_T = typing.TypeVar('Generic_Action_GenericClasses_Action_1_T')
    @typing.overload
    def __getitem__(self, types : typing.Type[Generic_Action_GenericClasses_Action_1_T]) -> typing.Type[Action_1[Generic_Action_GenericClasses_Action_1_T]]: ...
    Generic_Action_GenericClasses_Action_10_T1 = typing.TypeVar('Generic_Action_GenericClasses_Action_10_T1')
    Generic_Action_GenericClasses_Action_10_T2 = typing.TypeVar('Generic_Action_GenericClasses_Action_10_T2')
    Generic_Action_GenericClasses_Action_10_T3 = typing.TypeVar('Generic_Action_GenericClasses_Action_10_T3')
    Generic_Action_GenericClasses_Action_10_T4 = typing.TypeVar('Generic_Action_GenericClasses_Action_10_T4')
    Generic_Action_GenericClasses_Action_10_T5 = typing.TypeVar('Generic_Action_GenericClasses_Action_10_T5')
    Generic_Action_GenericClasses_Action_10_T6 = typing.TypeVar('Generic_Action_GenericClasses_Action_10_T6')
    Generic_Action_GenericClasses_Action_10_T7 = typing.TypeVar('Generic_Action_GenericClasses_Action_10_T7')
    Generic_Action_GenericClasses_Action_10_T8 = typing.TypeVar('Generic_Action_GenericClasses_Action_10_T8')
    Generic_Action_GenericClasses_Action_10_T9 = typing.TypeVar('Generic_Action_GenericClasses_Action_10_T9')
    Generic_Action_GenericClasses_Action_10_T10 = typing.TypeVar('Generic_Action_GenericClasses_Action_10_T10')
    @typing.overload
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_Action_GenericClasses_Action_10_T1], typing.Type[Generic_Action_GenericClasses_Action_10_T2], typing.Type[Generic_Action_GenericClasses_Action_10_T3], typing.Type[Generic_Action_GenericClasses_Action_10_T4], typing.Type[Generic_Action_GenericClasses_Action_10_T5], typing.Type[Generic_Action_GenericClasses_Action_10_T6], typing.Type[Generic_Action_GenericClasses_Action_10_T7], typing.Type[Generic_Action_GenericClasses_Action_10_T8], typing.Type[Generic_Action_GenericClasses_Action_10_T9], typing.Type[Generic_Action_GenericClasses_Action_10_T10]]) -> typing.Type[Action_10[Generic_Action_GenericClasses_Action_10_T1, Generic_Action_GenericClasses_Action_10_T2, Generic_Action_GenericClasses_Action_10_T3, Generic_Action_GenericClasses_Action_10_T4, Generic_Action_GenericClasses_Action_10_T5, Generic_Action_GenericClasses_Action_10_T6, Generic_Action_GenericClasses_Action_10_T7, Generic_Action_GenericClasses_Action_10_T8, Generic_Action_GenericClasses_Action_10_T9, Generic_Action_GenericClasses_Action_10_T10]]: ...
    Generic_Action_GenericClasses_Action_11_T1 = typing.TypeVar('Generic_Action_GenericClasses_Action_11_T1')
    Generic_Action_GenericClasses_Action_11_T2 = typing.TypeVar('Generic_Action_GenericClasses_Action_11_T2')
    Generic_Action_GenericClasses_Action_11_T3 = typing.TypeVar('Generic_Action_GenericClasses_Action_11_T3')
    Generic_Action_GenericClasses_Action_11_T4 = typing.TypeVar('Generic_Action_GenericClasses_Action_11_T4')
    Generic_Action_GenericClasses_Action_11_T5 = typing.TypeVar('Generic_Action_GenericClasses_Action_11_T5')
    Generic_Action_GenericClasses_Action_11_T6 = typing.TypeVar('Generic_Action_GenericClasses_Action_11_T6')
    Generic_Action_GenericClasses_Action_11_T7 = typing.TypeVar('Generic_Action_GenericClasses_Action_11_T7')
    Generic_Action_GenericClasses_Action_11_T8 = typing.TypeVar('Generic_Action_GenericClasses_Action_11_T8')
    Generic_Action_GenericClasses_Action_11_T9 = typing.TypeVar('Generic_Action_GenericClasses_Action_11_T9')
    Generic_Action_GenericClasses_Action_11_T10 = typing.TypeVar('Generic_Action_GenericClasses_Action_11_T10')
    Generic_Action_GenericClasses_Action_11_T11 = typing.TypeVar('Generic_Action_GenericClasses_Action_11_T11')
    @typing.overload
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_Action_GenericClasses_Action_11_T1], typing.Type[Generic_Action_GenericClasses_Action_11_T2], typing.Type[Generic_Action_GenericClasses_Action_11_T3], typing.Type[Generic_Action_GenericClasses_Action_11_T4], typing.Type[Generic_Action_GenericClasses_Action_11_T5], typing.Type[Generic_Action_GenericClasses_Action_11_T6], typing.Type[Generic_Action_GenericClasses_Action_11_T7], typing.Type[Generic_Action_GenericClasses_Action_11_T8], typing.Type[Generic_Action_GenericClasses_Action_11_T9], typing.Type[Generic_Action_GenericClasses_Action_11_T10], typing.Type[Generic_Action_GenericClasses_Action_11_T11]]) -> typing.Type[Action_11[Generic_Action_GenericClasses_Action_11_T1, Generic_Action_GenericClasses_Action_11_T2, Generic_Action_GenericClasses_Action_11_T3, Generic_Action_GenericClasses_Action_11_T4, Generic_Action_GenericClasses_Action_11_T5, Generic_Action_GenericClasses_Action_11_T6, Generic_Action_GenericClasses_Action_11_T7, Generic_Action_GenericClasses_Action_11_T8, Generic_Action_GenericClasses_Action_11_T9, Generic_Action_GenericClasses_Action_11_T10, Generic_Action_GenericClasses_Action_11_T11]]: ...
    Generic_Action_GenericClasses_Action_12_T1 = typing.TypeVar('Generic_Action_GenericClasses_Action_12_T1')
    Generic_Action_GenericClasses_Action_12_T2 = typing.TypeVar('Generic_Action_GenericClasses_Action_12_T2')
    Generic_Action_GenericClasses_Action_12_T3 = typing.TypeVar('Generic_Action_GenericClasses_Action_12_T3')
    Generic_Action_GenericClasses_Action_12_T4 = typing.TypeVar('Generic_Action_GenericClasses_Action_12_T4')
    Generic_Action_GenericClasses_Action_12_T5 = typing.TypeVar('Generic_Action_GenericClasses_Action_12_T5')
    Generic_Action_GenericClasses_Action_12_T6 = typing.TypeVar('Generic_Action_GenericClasses_Action_12_T6')
    Generic_Action_GenericClasses_Action_12_T7 = typing.TypeVar('Generic_Action_GenericClasses_Action_12_T7')
    Generic_Action_GenericClasses_Action_12_T8 = typing.TypeVar('Generic_Action_GenericClasses_Action_12_T8')
    Generic_Action_GenericClasses_Action_12_T9 = typing.TypeVar('Generic_Action_GenericClasses_Action_12_T9')
    Generic_Action_GenericClasses_Action_12_T10 = typing.TypeVar('Generic_Action_GenericClasses_Action_12_T10')
    Generic_Action_GenericClasses_Action_12_T11 = typing.TypeVar('Generic_Action_GenericClasses_Action_12_T11')
    Generic_Action_GenericClasses_Action_12_T12 = typing.TypeVar('Generic_Action_GenericClasses_Action_12_T12')
    @typing.overload
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_Action_GenericClasses_Action_12_T1], typing.Type[Generic_Action_GenericClasses_Action_12_T2], typing.Type[Generic_Action_GenericClasses_Action_12_T3], typing.Type[Generic_Action_GenericClasses_Action_12_T4], typing.Type[Generic_Action_GenericClasses_Action_12_T5], typing.Type[Generic_Action_GenericClasses_Action_12_T6], typing.Type[Generic_Action_GenericClasses_Action_12_T7], typing.Type[Generic_Action_GenericClasses_Action_12_T8], typing.Type[Generic_Action_GenericClasses_Action_12_T9], typing.Type[Generic_Action_GenericClasses_Action_12_T10], typing.Type[Generic_Action_GenericClasses_Action_12_T11], typing.Type[Generic_Action_GenericClasses_Action_12_T12]]) -> typing.Type[Action_12[Generic_Action_GenericClasses_Action_12_T1, Generic_Action_GenericClasses_Action_12_T2, Generic_Action_GenericClasses_Action_12_T3, Generic_Action_GenericClasses_Action_12_T4, Generic_Action_GenericClasses_Action_12_T5, Generic_Action_GenericClasses_Action_12_T6, Generic_Action_GenericClasses_Action_12_T7, Generic_Action_GenericClasses_Action_12_T8, Generic_Action_GenericClasses_Action_12_T9, Generic_Action_GenericClasses_Action_12_T10, Generic_Action_GenericClasses_Action_12_T11, Generic_Action_GenericClasses_Action_12_T12]]: ...
    Generic_Action_GenericClasses_Action_13_T1 = typing.TypeVar('Generic_Action_GenericClasses_Action_13_T1')
    Generic_Action_GenericClasses_Action_13_T2 = typing.TypeVar('Generic_Action_GenericClasses_Action_13_T2')
    Generic_Action_GenericClasses_Action_13_T3 = typing.TypeVar('Generic_Action_GenericClasses_Action_13_T3')
    Generic_Action_GenericClasses_Action_13_T4 = typing.TypeVar('Generic_Action_GenericClasses_Action_13_T4')
    Generic_Action_GenericClasses_Action_13_T5 = typing.TypeVar('Generic_Action_GenericClasses_Action_13_T5')
    Generic_Action_GenericClasses_Action_13_T6 = typing.TypeVar('Generic_Action_GenericClasses_Action_13_T6')
    Generic_Action_GenericClasses_Action_13_T7 = typing.TypeVar('Generic_Action_GenericClasses_Action_13_T7')
    Generic_Action_GenericClasses_Action_13_T8 = typing.TypeVar('Generic_Action_GenericClasses_Action_13_T8')
    Generic_Action_GenericClasses_Action_13_T9 = typing.TypeVar('Generic_Action_GenericClasses_Action_13_T9')
    Generic_Action_GenericClasses_Action_13_T10 = typing.TypeVar('Generic_Action_GenericClasses_Action_13_T10')
    Generic_Action_GenericClasses_Action_13_T11 = typing.TypeVar('Generic_Action_GenericClasses_Action_13_T11')
    Generic_Action_GenericClasses_Action_13_T12 = typing.TypeVar('Generic_Action_GenericClasses_Action_13_T12')
    Generic_Action_GenericClasses_Action_13_T13 = typing.TypeVar('Generic_Action_GenericClasses_Action_13_T13')
    @typing.overload
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_Action_GenericClasses_Action_13_T1], typing.Type[Generic_Action_GenericClasses_Action_13_T2], typing.Type[Generic_Action_GenericClasses_Action_13_T3], typing.Type[Generic_Action_GenericClasses_Action_13_T4], typing.Type[Generic_Action_GenericClasses_Action_13_T5], typing.Type[Generic_Action_GenericClasses_Action_13_T6], typing.Type[Generic_Action_GenericClasses_Action_13_T7], typing.Type[Generic_Action_GenericClasses_Action_13_T8], typing.Type[Generic_Action_GenericClasses_Action_13_T9], typing.Type[Generic_Action_GenericClasses_Action_13_T10], typing.Type[Generic_Action_GenericClasses_Action_13_T11], typing.Type[Generic_Action_GenericClasses_Action_13_T12], typing.Type[Generic_Action_GenericClasses_Action_13_T13]]) -> typing.Type[Action_13[Generic_Action_GenericClasses_Action_13_T1, Generic_Action_GenericClasses_Action_13_T2, Generic_Action_GenericClasses_Action_13_T3, Generic_Action_GenericClasses_Action_13_T4, Generic_Action_GenericClasses_Action_13_T5, Generic_Action_GenericClasses_Action_13_T6, Generic_Action_GenericClasses_Action_13_T7, Generic_Action_GenericClasses_Action_13_T8, Generic_Action_GenericClasses_Action_13_T9, Generic_Action_GenericClasses_Action_13_T10, Generic_Action_GenericClasses_Action_13_T11, Generic_Action_GenericClasses_Action_13_T12, Generic_Action_GenericClasses_Action_13_T13]]: ...
    Generic_Action_GenericClasses_Action_14_T1 = typing.TypeVar('Generic_Action_GenericClasses_Action_14_T1')
    Generic_Action_GenericClasses_Action_14_T2 = typing.TypeVar('Generic_Action_GenericClasses_Action_14_T2')
    Generic_Action_GenericClasses_Action_14_T3 = typing.TypeVar('Generic_Action_GenericClasses_Action_14_T3')
    Generic_Action_GenericClasses_Action_14_T4 = typing.TypeVar('Generic_Action_GenericClasses_Action_14_T4')
    Generic_Action_GenericClasses_Action_14_T5 = typing.TypeVar('Generic_Action_GenericClasses_Action_14_T5')
    Generic_Action_GenericClasses_Action_14_T6 = typing.TypeVar('Generic_Action_GenericClasses_Action_14_T6')
    Generic_Action_GenericClasses_Action_14_T7 = typing.TypeVar('Generic_Action_GenericClasses_Action_14_T7')
    Generic_Action_GenericClasses_Action_14_T8 = typing.TypeVar('Generic_Action_GenericClasses_Action_14_T8')
    Generic_Action_GenericClasses_Action_14_T9 = typing.TypeVar('Generic_Action_GenericClasses_Action_14_T9')
    Generic_Action_GenericClasses_Action_14_T10 = typing.TypeVar('Generic_Action_GenericClasses_Action_14_T10')
    Generic_Action_GenericClasses_Action_14_T11 = typing.TypeVar('Generic_Action_GenericClasses_Action_14_T11')
    Generic_Action_GenericClasses_Action_14_T12 = typing.TypeVar('Generic_Action_GenericClasses_Action_14_T12')
    Generic_Action_GenericClasses_Action_14_T13 = typing.TypeVar('Generic_Action_GenericClasses_Action_14_T13')
    Generic_Action_GenericClasses_Action_14_T14 = typing.TypeVar('Generic_Action_GenericClasses_Action_14_T14')
    @typing.overload
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_Action_GenericClasses_Action_14_T1], typing.Type[Generic_Action_GenericClasses_Action_14_T2], typing.Type[Generic_Action_GenericClasses_Action_14_T3], typing.Type[Generic_Action_GenericClasses_Action_14_T4], typing.Type[Generic_Action_GenericClasses_Action_14_T5], typing.Type[Generic_Action_GenericClasses_Action_14_T6], typing.Type[Generic_Action_GenericClasses_Action_14_T7], typing.Type[Generic_Action_GenericClasses_Action_14_T8], typing.Type[Generic_Action_GenericClasses_Action_14_T9], typing.Type[Generic_Action_GenericClasses_Action_14_T10], typing.Type[Generic_Action_GenericClasses_Action_14_T11], typing.Type[Generic_Action_GenericClasses_Action_14_T12], typing.Type[Generic_Action_GenericClasses_Action_14_T13], typing.Type[Generic_Action_GenericClasses_Action_14_T14]]) -> typing.Type[Action_14[Generic_Action_GenericClasses_Action_14_T1, Generic_Action_GenericClasses_Action_14_T2, Generic_Action_GenericClasses_Action_14_T3, Generic_Action_GenericClasses_Action_14_T4, Generic_Action_GenericClasses_Action_14_T5, Generic_Action_GenericClasses_Action_14_T6, Generic_Action_GenericClasses_Action_14_T7, Generic_Action_GenericClasses_Action_14_T8, Generic_Action_GenericClasses_Action_14_T9, Generic_Action_GenericClasses_Action_14_T10, Generic_Action_GenericClasses_Action_14_T11, Generic_Action_GenericClasses_Action_14_T12, Generic_Action_GenericClasses_Action_14_T13, Generic_Action_GenericClasses_Action_14_T14]]: ...
    Generic_Action_GenericClasses_Action_15_T1 = typing.TypeVar('Generic_Action_GenericClasses_Action_15_T1')
    Generic_Action_GenericClasses_Action_15_T2 = typing.TypeVar('Generic_Action_GenericClasses_Action_15_T2')
    Generic_Action_GenericClasses_Action_15_T3 = typing.TypeVar('Generic_Action_GenericClasses_Action_15_T3')
    Generic_Action_GenericClasses_Action_15_T4 = typing.TypeVar('Generic_Action_GenericClasses_Action_15_T4')
    Generic_Action_GenericClasses_Action_15_T5 = typing.TypeVar('Generic_Action_GenericClasses_Action_15_T5')
    Generic_Action_GenericClasses_Action_15_T6 = typing.TypeVar('Generic_Action_GenericClasses_Action_15_T6')
    Generic_Action_GenericClasses_Action_15_T7 = typing.TypeVar('Generic_Action_GenericClasses_Action_15_T7')
    Generic_Action_GenericClasses_Action_15_T8 = typing.TypeVar('Generic_Action_GenericClasses_Action_15_T8')
    Generic_Action_GenericClasses_Action_15_T9 = typing.TypeVar('Generic_Action_GenericClasses_Action_15_T9')
    Generic_Action_GenericClasses_Action_15_T10 = typing.TypeVar('Generic_Action_GenericClasses_Action_15_T10')
    Generic_Action_GenericClasses_Action_15_T11 = typing.TypeVar('Generic_Action_GenericClasses_Action_15_T11')
    Generic_Action_GenericClasses_Action_15_T12 = typing.TypeVar('Generic_Action_GenericClasses_Action_15_T12')
    Generic_Action_GenericClasses_Action_15_T13 = typing.TypeVar('Generic_Action_GenericClasses_Action_15_T13')
    Generic_Action_GenericClasses_Action_15_T14 = typing.TypeVar('Generic_Action_GenericClasses_Action_15_T14')
    Generic_Action_GenericClasses_Action_15_T15 = typing.TypeVar('Generic_Action_GenericClasses_Action_15_T15')
    @typing.overload
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_Action_GenericClasses_Action_15_T1], typing.Type[Generic_Action_GenericClasses_Action_15_T2], typing.Type[Generic_Action_GenericClasses_Action_15_T3], typing.Type[Generic_Action_GenericClasses_Action_15_T4], typing.Type[Generic_Action_GenericClasses_Action_15_T5], typing.Type[Generic_Action_GenericClasses_Action_15_T6], typing.Type[Generic_Action_GenericClasses_Action_15_T7], typing.Type[Generic_Action_GenericClasses_Action_15_T8], typing.Type[Generic_Action_GenericClasses_Action_15_T9], typing.Type[Generic_Action_GenericClasses_Action_15_T10], typing.Type[Generic_Action_GenericClasses_Action_15_T11], typing.Type[Generic_Action_GenericClasses_Action_15_T12], typing.Type[Generic_Action_GenericClasses_Action_15_T13], typing.Type[Generic_Action_GenericClasses_Action_15_T14], typing.Type[Generic_Action_GenericClasses_Action_15_T15]]) -> typing.Type[Action_15[Generic_Action_GenericClasses_Action_15_T1, Generic_Action_GenericClasses_Action_15_T2, Generic_Action_GenericClasses_Action_15_T3, Generic_Action_GenericClasses_Action_15_T4, Generic_Action_GenericClasses_Action_15_T5, Generic_Action_GenericClasses_Action_15_T6, Generic_Action_GenericClasses_Action_15_T7, Generic_Action_GenericClasses_Action_15_T8, Generic_Action_GenericClasses_Action_15_T9, Generic_Action_GenericClasses_Action_15_T10, Generic_Action_GenericClasses_Action_15_T11, Generic_Action_GenericClasses_Action_15_T12, Generic_Action_GenericClasses_Action_15_T13, Generic_Action_GenericClasses_Action_15_T14, Generic_Action_GenericClasses_Action_15_T15]]: ...
    Generic_Action_GenericClasses_Action_16_T1 = typing.TypeVar('Generic_Action_GenericClasses_Action_16_T1')
    Generic_Action_GenericClasses_Action_16_T2 = typing.TypeVar('Generic_Action_GenericClasses_Action_16_T2')
    Generic_Action_GenericClasses_Action_16_T3 = typing.TypeVar('Generic_Action_GenericClasses_Action_16_T3')
    Generic_Action_GenericClasses_Action_16_T4 = typing.TypeVar('Generic_Action_GenericClasses_Action_16_T4')
    Generic_Action_GenericClasses_Action_16_T5 = typing.TypeVar('Generic_Action_GenericClasses_Action_16_T5')
    Generic_Action_GenericClasses_Action_16_T6 = typing.TypeVar('Generic_Action_GenericClasses_Action_16_T6')
    Generic_Action_GenericClasses_Action_16_T7 = typing.TypeVar('Generic_Action_GenericClasses_Action_16_T7')
    Generic_Action_GenericClasses_Action_16_T8 = typing.TypeVar('Generic_Action_GenericClasses_Action_16_T8')
    Generic_Action_GenericClasses_Action_16_T9 = typing.TypeVar('Generic_Action_GenericClasses_Action_16_T9')
    Generic_Action_GenericClasses_Action_16_T10 = typing.TypeVar('Generic_Action_GenericClasses_Action_16_T10')
    Generic_Action_GenericClasses_Action_16_T11 = typing.TypeVar('Generic_Action_GenericClasses_Action_16_T11')
    Generic_Action_GenericClasses_Action_16_T12 = typing.TypeVar('Generic_Action_GenericClasses_Action_16_T12')
    Generic_Action_GenericClasses_Action_16_T13 = typing.TypeVar('Generic_Action_GenericClasses_Action_16_T13')
    Generic_Action_GenericClasses_Action_16_T14 = typing.TypeVar('Generic_Action_GenericClasses_Action_16_T14')
    Generic_Action_GenericClasses_Action_16_T15 = typing.TypeVar('Generic_Action_GenericClasses_Action_16_T15')
    Generic_Action_GenericClasses_Action_16_T16 = typing.TypeVar('Generic_Action_GenericClasses_Action_16_T16')
    @typing.overload
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_Action_GenericClasses_Action_16_T1], typing.Type[Generic_Action_GenericClasses_Action_16_T2], typing.Type[Generic_Action_GenericClasses_Action_16_T3], typing.Type[Generic_Action_GenericClasses_Action_16_T4], typing.Type[Generic_Action_GenericClasses_Action_16_T5], typing.Type[Generic_Action_GenericClasses_Action_16_T6], typing.Type[Generic_Action_GenericClasses_Action_16_T7], typing.Type[Generic_Action_GenericClasses_Action_16_T8], typing.Type[Generic_Action_GenericClasses_Action_16_T9], typing.Type[Generic_Action_GenericClasses_Action_16_T10], typing.Type[Generic_Action_GenericClasses_Action_16_T11], typing.Type[Generic_Action_GenericClasses_Action_16_T12], typing.Type[Generic_Action_GenericClasses_Action_16_T13], typing.Type[Generic_Action_GenericClasses_Action_16_T14], typing.Type[Generic_Action_GenericClasses_Action_16_T15], typing.Type[Generic_Action_GenericClasses_Action_16_T16]]) -> typing.Type[Action_16[Generic_Action_GenericClasses_Action_16_T1, Generic_Action_GenericClasses_Action_16_T2, Generic_Action_GenericClasses_Action_16_T3, Generic_Action_GenericClasses_Action_16_T4, Generic_Action_GenericClasses_Action_16_T5, Generic_Action_GenericClasses_Action_16_T6, Generic_Action_GenericClasses_Action_16_T7, Generic_Action_GenericClasses_Action_16_T8, Generic_Action_GenericClasses_Action_16_T9, Generic_Action_GenericClasses_Action_16_T10, Generic_Action_GenericClasses_Action_16_T11, Generic_Action_GenericClasses_Action_16_T12, Generic_Action_GenericClasses_Action_16_T13, Generic_Action_GenericClasses_Action_16_T14, Generic_Action_GenericClasses_Action_16_T15, Generic_Action_GenericClasses_Action_16_T16]]: ...
    Generic_Action_GenericClasses_Action_2_T1 = typing.TypeVar('Generic_Action_GenericClasses_Action_2_T1')
    Generic_Action_GenericClasses_Action_2_T2 = typing.TypeVar('Generic_Action_GenericClasses_Action_2_T2')
    @typing.overload
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_Action_GenericClasses_Action_2_T1], typing.Type[Generic_Action_GenericClasses_Action_2_T2]]) -> typing.Type[Action_2[Generic_Action_GenericClasses_Action_2_T1, Generic_Action_GenericClasses_Action_2_T2]]: ...
    Generic_Action_GenericClasses_Action_3_T1 = typing.TypeVar('Generic_Action_GenericClasses_Action_3_T1')
    Generic_Action_GenericClasses_Action_3_T2 = typing.TypeVar('Generic_Action_GenericClasses_Action_3_T2')
    Generic_Action_GenericClasses_Action_3_T3 = typing.TypeVar('Generic_Action_GenericClasses_Action_3_T3')
    @typing.overload
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_Action_GenericClasses_Action_3_T1], typing.Type[Generic_Action_GenericClasses_Action_3_T2], typing.Type[Generic_Action_GenericClasses_Action_3_T3]]) -> typing.Type[Action_3[Generic_Action_GenericClasses_Action_3_T1, Generic_Action_GenericClasses_Action_3_T2, Generic_Action_GenericClasses_Action_3_T3]]: ...
    Generic_Action_GenericClasses_Action_4_T1 = typing.TypeVar('Generic_Action_GenericClasses_Action_4_T1')
    Generic_Action_GenericClasses_Action_4_T2 = typing.TypeVar('Generic_Action_GenericClasses_Action_4_T2')
    Generic_Action_GenericClasses_Action_4_T3 = typing.TypeVar('Generic_Action_GenericClasses_Action_4_T3')
    Generic_Action_GenericClasses_Action_4_T4 = typing.TypeVar('Generic_Action_GenericClasses_Action_4_T4')
    @typing.overload
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_Action_GenericClasses_Action_4_T1], typing.Type[Generic_Action_GenericClasses_Action_4_T2], typing.Type[Generic_Action_GenericClasses_Action_4_T3], typing.Type[Generic_Action_GenericClasses_Action_4_T4]]) -> typing.Type[Action_4[Generic_Action_GenericClasses_Action_4_T1, Generic_Action_GenericClasses_Action_4_T2, Generic_Action_GenericClasses_Action_4_T3, Generic_Action_GenericClasses_Action_4_T4]]: ...
    Generic_Action_GenericClasses_Action_5_T1 = typing.TypeVar('Generic_Action_GenericClasses_Action_5_T1')
    Generic_Action_GenericClasses_Action_5_T2 = typing.TypeVar('Generic_Action_GenericClasses_Action_5_T2')
    Generic_Action_GenericClasses_Action_5_T3 = typing.TypeVar('Generic_Action_GenericClasses_Action_5_T3')
    Generic_Action_GenericClasses_Action_5_T4 = typing.TypeVar('Generic_Action_GenericClasses_Action_5_T4')
    Generic_Action_GenericClasses_Action_5_T5 = typing.TypeVar('Generic_Action_GenericClasses_Action_5_T5')
    @typing.overload
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_Action_GenericClasses_Action_5_T1], typing.Type[Generic_Action_GenericClasses_Action_5_T2], typing.Type[Generic_Action_GenericClasses_Action_5_T3], typing.Type[Generic_Action_GenericClasses_Action_5_T4], typing.Type[Generic_Action_GenericClasses_Action_5_T5]]) -> typing.Type[Action_5[Generic_Action_GenericClasses_Action_5_T1, Generic_Action_GenericClasses_Action_5_T2, Generic_Action_GenericClasses_Action_5_T3, Generic_Action_GenericClasses_Action_5_T4, Generic_Action_GenericClasses_Action_5_T5]]: ...
    Generic_Action_GenericClasses_Action_6_T1 = typing.TypeVar('Generic_Action_GenericClasses_Action_6_T1')
    Generic_Action_GenericClasses_Action_6_T2 = typing.TypeVar('Generic_Action_GenericClasses_Action_6_T2')
    Generic_Action_GenericClasses_Action_6_T3 = typing.TypeVar('Generic_Action_GenericClasses_Action_6_T3')
    Generic_Action_GenericClasses_Action_6_T4 = typing.TypeVar('Generic_Action_GenericClasses_Action_6_T4')
    Generic_Action_GenericClasses_Action_6_T5 = typing.TypeVar('Generic_Action_GenericClasses_Action_6_T5')
    Generic_Action_GenericClasses_Action_6_T6 = typing.TypeVar('Generic_Action_GenericClasses_Action_6_T6')
    @typing.overload
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_Action_GenericClasses_Action_6_T1], typing.Type[Generic_Action_GenericClasses_Action_6_T2], typing.Type[Generic_Action_GenericClasses_Action_6_T3], typing.Type[Generic_Action_GenericClasses_Action_6_T4], typing.Type[Generic_Action_GenericClasses_Action_6_T5], typing.Type[Generic_Action_GenericClasses_Action_6_T6]]) -> typing.Type[Action_6[Generic_Action_GenericClasses_Action_6_T1, Generic_Action_GenericClasses_Action_6_T2, Generic_Action_GenericClasses_Action_6_T3, Generic_Action_GenericClasses_Action_6_T4, Generic_Action_GenericClasses_Action_6_T5, Generic_Action_GenericClasses_Action_6_T6]]: ...
    Generic_Action_GenericClasses_Action_7_T1 = typing.TypeVar('Generic_Action_GenericClasses_Action_7_T1')
    Generic_Action_GenericClasses_Action_7_T2 = typing.TypeVar('Generic_Action_GenericClasses_Action_7_T2')
    Generic_Action_GenericClasses_Action_7_T3 = typing.TypeVar('Generic_Action_GenericClasses_Action_7_T3')
    Generic_Action_GenericClasses_Action_7_T4 = typing.TypeVar('Generic_Action_GenericClasses_Action_7_T4')
    Generic_Action_GenericClasses_Action_7_T5 = typing.TypeVar('Generic_Action_GenericClasses_Action_7_T5')
    Generic_Action_GenericClasses_Action_7_T6 = typing.TypeVar('Generic_Action_GenericClasses_Action_7_T6')
    Generic_Action_GenericClasses_Action_7_T7 = typing.TypeVar('Generic_Action_GenericClasses_Action_7_T7')
    @typing.overload
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_Action_GenericClasses_Action_7_T1], typing.Type[Generic_Action_GenericClasses_Action_7_T2], typing.Type[Generic_Action_GenericClasses_Action_7_T3], typing.Type[Generic_Action_GenericClasses_Action_7_T4], typing.Type[Generic_Action_GenericClasses_Action_7_T5], typing.Type[Generic_Action_GenericClasses_Action_7_T6], typing.Type[Generic_Action_GenericClasses_Action_7_T7]]) -> typing.Type[Action_7[Generic_Action_GenericClasses_Action_7_T1, Generic_Action_GenericClasses_Action_7_T2, Generic_Action_GenericClasses_Action_7_T3, Generic_Action_GenericClasses_Action_7_T4, Generic_Action_GenericClasses_Action_7_T5, Generic_Action_GenericClasses_Action_7_T6, Generic_Action_GenericClasses_Action_7_T7]]: ...
    Generic_Action_GenericClasses_Action_8_T1 = typing.TypeVar('Generic_Action_GenericClasses_Action_8_T1')
    Generic_Action_GenericClasses_Action_8_T2 = typing.TypeVar('Generic_Action_GenericClasses_Action_8_T2')
    Generic_Action_GenericClasses_Action_8_T3 = typing.TypeVar('Generic_Action_GenericClasses_Action_8_T3')
    Generic_Action_GenericClasses_Action_8_T4 = typing.TypeVar('Generic_Action_GenericClasses_Action_8_T4')
    Generic_Action_GenericClasses_Action_8_T5 = typing.TypeVar('Generic_Action_GenericClasses_Action_8_T5')
    Generic_Action_GenericClasses_Action_8_T6 = typing.TypeVar('Generic_Action_GenericClasses_Action_8_T6')
    Generic_Action_GenericClasses_Action_8_T7 = typing.TypeVar('Generic_Action_GenericClasses_Action_8_T7')
    Generic_Action_GenericClasses_Action_8_T8 = typing.TypeVar('Generic_Action_GenericClasses_Action_8_T8')
    @typing.overload
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_Action_GenericClasses_Action_8_T1], typing.Type[Generic_Action_GenericClasses_Action_8_T2], typing.Type[Generic_Action_GenericClasses_Action_8_T3], typing.Type[Generic_Action_GenericClasses_Action_8_T4], typing.Type[Generic_Action_GenericClasses_Action_8_T5], typing.Type[Generic_Action_GenericClasses_Action_8_T6], typing.Type[Generic_Action_GenericClasses_Action_8_T7], typing.Type[Generic_Action_GenericClasses_Action_8_T8]]) -> typing.Type[Action_8[Generic_Action_GenericClasses_Action_8_T1, Generic_Action_GenericClasses_Action_8_T2, Generic_Action_GenericClasses_Action_8_T3, Generic_Action_GenericClasses_Action_8_T4, Generic_Action_GenericClasses_Action_8_T5, Generic_Action_GenericClasses_Action_8_T6, Generic_Action_GenericClasses_Action_8_T7, Generic_Action_GenericClasses_Action_8_T8]]: ...
    Generic_Action_GenericClasses_Action_9_T1 = typing.TypeVar('Generic_Action_GenericClasses_Action_9_T1')
    Generic_Action_GenericClasses_Action_9_T2 = typing.TypeVar('Generic_Action_GenericClasses_Action_9_T2')
    Generic_Action_GenericClasses_Action_9_T3 = typing.TypeVar('Generic_Action_GenericClasses_Action_9_T3')
    Generic_Action_GenericClasses_Action_9_T4 = typing.TypeVar('Generic_Action_GenericClasses_Action_9_T4')
    Generic_Action_GenericClasses_Action_9_T5 = typing.TypeVar('Generic_Action_GenericClasses_Action_9_T5')
    Generic_Action_GenericClasses_Action_9_T6 = typing.TypeVar('Generic_Action_GenericClasses_Action_9_T6')
    Generic_Action_GenericClasses_Action_9_T7 = typing.TypeVar('Generic_Action_GenericClasses_Action_9_T7')
    Generic_Action_GenericClasses_Action_9_T8 = typing.TypeVar('Generic_Action_GenericClasses_Action_9_T8')
    Generic_Action_GenericClasses_Action_9_T9 = typing.TypeVar('Generic_Action_GenericClasses_Action_9_T9')
    @typing.overload
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_Action_GenericClasses_Action_9_T1], typing.Type[Generic_Action_GenericClasses_Action_9_T2], typing.Type[Generic_Action_GenericClasses_Action_9_T3], typing.Type[Generic_Action_GenericClasses_Action_9_T4], typing.Type[Generic_Action_GenericClasses_Action_9_T5], typing.Type[Generic_Action_GenericClasses_Action_9_T6], typing.Type[Generic_Action_GenericClasses_Action_9_T7], typing.Type[Generic_Action_GenericClasses_Action_9_T8], typing.Type[Generic_Action_GenericClasses_Action_9_T9]]) -> typing.Type[Action_9[Generic_Action_GenericClasses_Action_9_T1, Generic_Action_GenericClasses_Action_9_T2, Generic_Action_GenericClasses_Action_9_T3, Generic_Action_GenericClasses_Action_9_T4, Generic_Action_GenericClasses_Action_9_T5, Generic_Action_GenericClasses_Action_9_T6, Generic_Action_GenericClasses_Action_9_T7, Generic_Action_GenericClasses_Action_9_T8, Generic_Action_GenericClasses_Action_9_T9]]: ...

class Action(Action_0, metaclass =Action_GenericClasses): ...

class Action_0(MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self) -> None: ...


Action_1_T = typing.TypeVar('Action_1_T', contravariant=True)
class Action_1(typing.Generic[Action_1_T], MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, obj: Action_1_T, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, obj: Action_1_T) -> None: ...


Action_10_T1 = typing.TypeVar('Action_10_T1', contravariant=True)
Action_10_T2 = typing.TypeVar('Action_10_T2', contravariant=True)
Action_10_T3 = typing.TypeVar('Action_10_T3', contravariant=True)
Action_10_T4 = typing.TypeVar('Action_10_T4', contravariant=True)
Action_10_T5 = typing.TypeVar('Action_10_T5', contravariant=True)
Action_10_T6 = typing.TypeVar('Action_10_T6', contravariant=True)
Action_10_T7 = typing.TypeVar('Action_10_T7', contravariant=True)
Action_10_T8 = typing.TypeVar('Action_10_T8', contravariant=True)
Action_10_T9 = typing.TypeVar('Action_10_T9', contravariant=True)
Action_10_T10 = typing.TypeVar('Action_10_T10', contravariant=True)
class Action_10(typing.Generic[Action_10_T1, Action_10_T2, Action_10_T3, Action_10_T4, Action_10_T5, Action_10_T6, Action_10_T7, Action_10_T8, Action_10_T9, Action_10_T10], MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, arg1: Action_10_T1, arg2: Action_10_T2, arg3: Action_10_T3, arg4: Action_10_T4, arg5: Action_10_T5, arg6: Action_10_T6, arg7: Action_10_T7, arg8: Action_10_T8, arg9: Action_10_T9, arg10: Action_10_T10, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, arg1: Action_10_T1, arg2: Action_10_T2, arg3: Action_10_T3, arg4: Action_10_T4, arg5: Action_10_T5, arg6: Action_10_T6, arg7: Action_10_T7, arg8: Action_10_T8, arg9: Action_10_T9, arg10: Action_10_T10) -> None: ...


Action_11_T1 = typing.TypeVar('Action_11_T1', contravariant=True)
Action_11_T2 = typing.TypeVar('Action_11_T2', contravariant=True)
Action_11_T3 = typing.TypeVar('Action_11_T3', contravariant=True)
Action_11_T4 = typing.TypeVar('Action_11_T4', contravariant=True)
Action_11_T5 = typing.TypeVar('Action_11_T5', contravariant=True)
Action_11_T6 = typing.TypeVar('Action_11_T6', contravariant=True)
Action_11_T7 = typing.TypeVar('Action_11_T7', contravariant=True)
Action_11_T8 = typing.TypeVar('Action_11_T8', contravariant=True)
Action_11_T9 = typing.TypeVar('Action_11_T9', contravariant=True)
Action_11_T10 = typing.TypeVar('Action_11_T10', contravariant=True)
Action_11_T11 = typing.TypeVar('Action_11_T11', contravariant=True)
class Action_11(typing.Generic[Action_11_T1, Action_11_T2, Action_11_T3, Action_11_T4, Action_11_T5, Action_11_T6, Action_11_T7, Action_11_T8, Action_11_T9, Action_11_T10, Action_11_T11], MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, arg1: Action_11_T1, arg2: Action_11_T2, arg3: Action_11_T3, arg4: Action_11_T4, arg5: Action_11_T5, arg6: Action_11_T6, arg7: Action_11_T7, arg8: Action_11_T8, arg9: Action_11_T9, arg10: Action_11_T10, arg11: Action_11_T11, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, arg1: Action_11_T1, arg2: Action_11_T2, arg3: Action_11_T3, arg4: Action_11_T4, arg5: Action_11_T5, arg6: Action_11_T6, arg7: Action_11_T7, arg8: Action_11_T8, arg9: Action_11_T9, arg10: Action_11_T10, arg11: Action_11_T11) -> None: ...


Action_12_T1 = typing.TypeVar('Action_12_T1', contravariant=True)
Action_12_T2 = typing.TypeVar('Action_12_T2', contravariant=True)
Action_12_T3 = typing.TypeVar('Action_12_T3', contravariant=True)
Action_12_T4 = typing.TypeVar('Action_12_T4', contravariant=True)
Action_12_T5 = typing.TypeVar('Action_12_T5', contravariant=True)
Action_12_T6 = typing.TypeVar('Action_12_T6', contravariant=True)
Action_12_T7 = typing.TypeVar('Action_12_T7', contravariant=True)
Action_12_T8 = typing.TypeVar('Action_12_T8', contravariant=True)
Action_12_T9 = typing.TypeVar('Action_12_T9', contravariant=True)
Action_12_T10 = typing.TypeVar('Action_12_T10', contravariant=True)
Action_12_T11 = typing.TypeVar('Action_12_T11', contravariant=True)
Action_12_T12 = typing.TypeVar('Action_12_T12', contravariant=True)
class Action_12(typing.Generic[Action_12_T1, Action_12_T2, Action_12_T3, Action_12_T4, Action_12_T5, Action_12_T6, Action_12_T7, Action_12_T8, Action_12_T9, Action_12_T10, Action_12_T11, Action_12_T12], MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, arg1: Action_12_T1, arg2: Action_12_T2, arg3: Action_12_T3, arg4: Action_12_T4, arg5: Action_12_T5, arg6: Action_12_T6, arg7: Action_12_T7, arg8: Action_12_T8, arg9: Action_12_T9, arg10: Action_12_T10, arg11: Action_12_T11, arg12: Action_12_T12, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, arg1: Action_12_T1, arg2: Action_12_T2, arg3: Action_12_T3, arg4: Action_12_T4, arg5: Action_12_T5, arg6: Action_12_T6, arg7: Action_12_T7, arg8: Action_12_T8, arg9: Action_12_T9, arg10: Action_12_T10, arg11: Action_12_T11, arg12: Action_12_T12) -> None: ...


Action_13_T1 = typing.TypeVar('Action_13_T1', contravariant=True)
Action_13_T2 = typing.TypeVar('Action_13_T2', contravariant=True)
Action_13_T3 = typing.TypeVar('Action_13_T3', contravariant=True)
Action_13_T4 = typing.TypeVar('Action_13_T4', contravariant=True)
Action_13_T5 = typing.TypeVar('Action_13_T5', contravariant=True)
Action_13_T6 = typing.TypeVar('Action_13_T6', contravariant=True)
Action_13_T7 = typing.TypeVar('Action_13_T7', contravariant=True)
Action_13_T8 = typing.TypeVar('Action_13_T8', contravariant=True)
Action_13_T9 = typing.TypeVar('Action_13_T9', contravariant=True)
Action_13_T10 = typing.TypeVar('Action_13_T10', contravariant=True)
Action_13_T11 = typing.TypeVar('Action_13_T11', contravariant=True)
Action_13_T12 = typing.TypeVar('Action_13_T12', contravariant=True)
Action_13_T13 = typing.TypeVar('Action_13_T13', contravariant=True)
class Action_13(typing.Generic[Action_13_T1, Action_13_T2, Action_13_T3, Action_13_T4, Action_13_T5, Action_13_T6, Action_13_T7, Action_13_T8, Action_13_T9, Action_13_T10, Action_13_T11, Action_13_T12, Action_13_T13], MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, arg1: Action_13_T1, arg2: Action_13_T2, arg3: Action_13_T3, arg4: Action_13_T4, arg5: Action_13_T5, arg6: Action_13_T6, arg7: Action_13_T7, arg8: Action_13_T8, arg9: Action_13_T9, arg10: Action_13_T10, arg11: Action_13_T11, arg12: Action_13_T12, arg13: Action_13_T13, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, arg1: Action_13_T1, arg2: Action_13_T2, arg3: Action_13_T3, arg4: Action_13_T4, arg5: Action_13_T5, arg6: Action_13_T6, arg7: Action_13_T7, arg8: Action_13_T8, arg9: Action_13_T9, arg10: Action_13_T10, arg11: Action_13_T11, arg12: Action_13_T12, arg13: Action_13_T13) -> None: ...


Action_14_T1 = typing.TypeVar('Action_14_T1', contravariant=True)
Action_14_T2 = typing.TypeVar('Action_14_T2', contravariant=True)
Action_14_T3 = typing.TypeVar('Action_14_T3', contravariant=True)
Action_14_T4 = typing.TypeVar('Action_14_T4', contravariant=True)
Action_14_T5 = typing.TypeVar('Action_14_T5', contravariant=True)
Action_14_T6 = typing.TypeVar('Action_14_T6', contravariant=True)
Action_14_T7 = typing.TypeVar('Action_14_T7', contravariant=True)
Action_14_T8 = typing.TypeVar('Action_14_T8', contravariant=True)
Action_14_T9 = typing.TypeVar('Action_14_T9', contravariant=True)
Action_14_T10 = typing.TypeVar('Action_14_T10', contravariant=True)
Action_14_T11 = typing.TypeVar('Action_14_T11', contravariant=True)
Action_14_T12 = typing.TypeVar('Action_14_T12', contravariant=True)
Action_14_T13 = typing.TypeVar('Action_14_T13', contravariant=True)
Action_14_T14 = typing.TypeVar('Action_14_T14', contravariant=True)
class Action_14(typing.Generic[Action_14_T1, Action_14_T2, Action_14_T3, Action_14_T4, Action_14_T5, Action_14_T6, Action_14_T7, Action_14_T8, Action_14_T9, Action_14_T10, Action_14_T11, Action_14_T12, Action_14_T13, Action_14_T14], MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, arg1: Action_14_T1, arg2: Action_14_T2, arg3: Action_14_T3, arg4: Action_14_T4, arg5: Action_14_T5, arg6: Action_14_T6, arg7: Action_14_T7, arg8: Action_14_T8, arg9: Action_14_T9, arg10: Action_14_T10, arg11: Action_14_T11, arg12: Action_14_T12, arg13: Action_14_T13, arg14: Action_14_T14, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, arg1: Action_14_T1, arg2: Action_14_T2, arg3: Action_14_T3, arg4: Action_14_T4, arg5: Action_14_T5, arg6: Action_14_T6, arg7: Action_14_T7, arg8: Action_14_T8, arg9: Action_14_T9, arg10: Action_14_T10, arg11: Action_14_T11, arg12: Action_14_T12, arg13: Action_14_T13, arg14: Action_14_T14) -> None: ...


Action_15_T1 = typing.TypeVar('Action_15_T1', contravariant=True)
Action_15_T2 = typing.TypeVar('Action_15_T2', contravariant=True)
Action_15_T3 = typing.TypeVar('Action_15_T3', contravariant=True)
Action_15_T4 = typing.TypeVar('Action_15_T4', contravariant=True)
Action_15_T5 = typing.TypeVar('Action_15_T5', contravariant=True)
Action_15_T6 = typing.TypeVar('Action_15_T6', contravariant=True)
Action_15_T7 = typing.TypeVar('Action_15_T7', contravariant=True)
Action_15_T8 = typing.TypeVar('Action_15_T8', contravariant=True)
Action_15_T9 = typing.TypeVar('Action_15_T9', contravariant=True)
Action_15_T10 = typing.TypeVar('Action_15_T10', contravariant=True)
Action_15_T11 = typing.TypeVar('Action_15_T11', contravariant=True)
Action_15_T12 = typing.TypeVar('Action_15_T12', contravariant=True)
Action_15_T13 = typing.TypeVar('Action_15_T13', contravariant=True)
Action_15_T14 = typing.TypeVar('Action_15_T14', contravariant=True)
Action_15_T15 = typing.TypeVar('Action_15_T15', contravariant=True)
class Action_15(typing.Generic[Action_15_T1, Action_15_T2, Action_15_T3, Action_15_T4, Action_15_T5, Action_15_T6, Action_15_T7, Action_15_T8, Action_15_T9, Action_15_T10, Action_15_T11, Action_15_T12, Action_15_T13, Action_15_T14, Action_15_T15], MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, arg1: Action_15_T1, arg2: Action_15_T2, arg3: Action_15_T3, arg4: Action_15_T4, arg5: Action_15_T5, arg6: Action_15_T6, arg7: Action_15_T7, arg8: Action_15_T8, arg9: Action_15_T9, arg10: Action_15_T10, arg11: Action_15_T11, arg12: Action_15_T12, arg13: Action_15_T13, arg14: Action_15_T14, arg15: Action_15_T15, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, arg1: Action_15_T1, arg2: Action_15_T2, arg3: Action_15_T3, arg4: Action_15_T4, arg5: Action_15_T5, arg6: Action_15_T6, arg7: Action_15_T7, arg8: Action_15_T8, arg9: Action_15_T9, arg10: Action_15_T10, arg11: Action_15_T11, arg12: Action_15_T12, arg13: Action_15_T13, arg14: Action_15_T14, arg15: Action_15_T15) -> None: ...


Action_16_T1 = typing.TypeVar('Action_16_T1', contravariant=True)
Action_16_T2 = typing.TypeVar('Action_16_T2', contravariant=True)
Action_16_T3 = typing.TypeVar('Action_16_T3', contravariant=True)
Action_16_T4 = typing.TypeVar('Action_16_T4', contravariant=True)
Action_16_T5 = typing.TypeVar('Action_16_T5', contravariant=True)
Action_16_T6 = typing.TypeVar('Action_16_T6', contravariant=True)
Action_16_T7 = typing.TypeVar('Action_16_T7', contravariant=True)
Action_16_T8 = typing.TypeVar('Action_16_T8', contravariant=True)
Action_16_T9 = typing.TypeVar('Action_16_T9', contravariant=True)
Action_16_T10 = typing.TypeVar('Action_16_T10', contravariant=True)
Action_16_T11 = typing.TypeVar('Action_16_T11', contravariant=True)
Action_16_T12 = typing.TypeVar('Action_16_T12', contravariant=True)
Action_16_T13 = typing.TypeVar('Action_16_T13', contravariant=True)
Action_16_T14 = typing.TypeVar('Action_16_T14', contravariant=True)
Action_16_T15 = typing.TypeVar('Action_16_T15', contravariant=True)
Action_16_T16 = typing.TypeVar('Action_16_T16', contravariant=True)
class Action_16(typing.Generic[Action_16_T1, Action_16_T2, Action_16_T3, Action_16_T4, Action_16_T5, Action_16_T6, Action_16_T7, Action_16_T8, Action_16_T9, Action_16_T10, Action_16_T11, Action_16_T12, Action_16_T13, Action_16_T14, Action_16_T15, Action_16_T16], MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, arg1: Action_16_T1, arg2: Action_16_T2, arg3: Action_16_T3, arg4: Action_16_T4, arg5: Action_16_T5, arg6: Action_16_T6, arg7: Action_16_T7, arg8: Action_16_T8, arg9: Action_16_T9, arg10: Action_16_T10, arg11: Action_16_T11, arg12: Action_16_T12, arg13: Action_16_T13, arg14: Action_16_T14, arg15: Action_16_T15, arg16: Action_16_T16, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, arg1: Action_16_T1, arg2: Action_16_T2, arg3: Action_16_T3, arg4: Action_16_T4, arg5: Action_16_T5, arg6: Action_16_T6, arg7: Action_16_T7, arg8: Action_16_T8, arg9: Action_16_T9, arg10: Action_16_T10, arg11: Action_16_T11, arg12: Action_16_T12, arg13: Action_16_T13, arg14: Action_16_T14, arg15: Action_16_T15, arg16: Action_16_T16) -> None: ...


Action_2_T1 = typing.TypeVar('Action_2_T1', contravariant=True)
Action_2_T2 = typing.TypeVar('Action_2_T2', contravariant=True)
class Action_2(typing.Generic[Action_2_T1, Action_2_T2], MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, arg1: Action_2_T1, arg2: Action_2_T2, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, arg1: Action_2_T1, arg2: Action_2_T2) -> None: ...


Action_3_T1 = typing.TypeVar('Action_3_T1', contravariant=True)
Action_3_T2 = typing.TypeVar('Action_3_T2', contravariant=True)
Action_3_T3 = typing.TypeVar('Action_3_T3', contravariant=True)
class Action_3(typing.Generic[Action_3_T1, Action_3_T2, Action_3_T3], MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, arg1: Action_3_T1, arg2: Action_3_T2, arg3: Action_3_T3, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, arg1: Action_3_T1, arg2: Action_3_T2, arg3: Action_3_T3) -> None: ...


Action_4_T1 = typing.TypeVar('Action_4_T1', contravariant=True)
Action_4_T2 = typing.TypeVar('Action_4_T2', contravariant=True)
Action_4_T3 = typing.TypeVar('Action_4_T3', contravariant=True)
Action_4_T4 = typing.TypeVar('Action_4_T4', contravariant=True)
class Action_4(typing.Generic[Action_4_T1, Action_4_T2, Action_4_T3, Action_4_T4], MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, arg1: Action_4_T1, arg2: Action_4_T2, arg3: Action_4_T3, arg4: Action_4_T4, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, arg1: Action_4_T1, arg2: Action_4_T2, arg3: Action_4_T3, arg4: Action_4_T4) -> None: ...


Action_5_T1 = typing.TypeVar('Action_5_T1', contravariant=True)
Action_5_T2 = typing.TypeVar('Action_5_T2', contravariant=True)
Action_5_T3 = typing.TypeVar('Action_5_T3', contravariant=True)
Action_5_T4 = typing.TypeVar('Action_5_T4', contravariant=True)
Action_5_T5 = typing.TypeVar('Action_5_T5', contravariant=True)
class Action_5(typing.Generic[Action_5_T1, Action_5_T2, Action_5_T3, Action_5_T4, Action_5_T5], MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, arg1: Action_5_T1, arg2: Action_5_T2, arg3: Action_5_T3, arg4: Action_5_T4, arg5: Action_5_T5, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, arg1: Action_5_T1, arg2: Action_5_T2, arg3: Action_5_T3, arg4: Action_5_T4, arg5: Action_5_T5) -> None: ...


Action_6_T1 = typing.TypeVar('Action_6_T1', contravariant=True)
Action_6_T2 = typing.TypeVar('Action_6_T2', contravariant=True)
Action_6_T3 = typing.TypeVar('Action_6_T3', contravariant=True)
Action_6_T4 = typing.TypeVar('Action_6_T4', contravariant=True)
Action_6_T5 = typing.TypeVar('Action_6_T5', contravariant=True)
Action_6_T6 = typing.TypeVar('Action_6_T6', contravariant=True)
class Action_6(typing.Generic[Action_6_T1, Action_6_T2, Action_6_T3, Action_6_T4, Action_6_T5, Action_6_T6], MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, arg1: Action_6_T1, arg2: Action_6_T2, arg3: Action_6_T3, arg4: Action_6_T4, arg5: Action_6_T5, arg6: Action_6_T6, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, arg1: Action_6_T1, arg2: Action_6_T2, arg3: Action_6_T3, arg4: Action_6_T4, arg5: Action_6_T5, arg6: Action_6_T6) -> None: ...


Action_7_T1 = typing.TypeVar('Action_7_T1', contravariant=True)
Action_7_T2 = typing.TypeVar('Action_7_T2', contravariant=True)
Action_7_T3 = typing.TypeVar('Action_7_T3', contravariant=True)
Action_7_T4 = typing.TypeVar('Action_7_T4', contravariant=True)
Action_7_T5 = typing.TypeVar('Action_7_T5', contravariant=True)
Action_7_T6 = typing.TypeVar('Action_7_T6', contravariant=True)
Action_7_T7 = typing.TypeVar('Action_7_T7', contravariant=True)
class Action_7(typing.Generic[Action_7_T1, Action_7_T2, Action_7_T3, Action_7_T4, Action_7_T5, Action_7_T6, Action_7_T7], MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, arg1: Action_7_T1, arg2: Action_7_T2, arg3: Action_7_T3, arg4: Action_7_T4, arg5: Action_7_T5, arg6: Action_7_T6, arg7: Action_7_T7, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, arg1: Action_7_T1, arg2: Action_7_T2, arg3: Action_7_T3, arg4: Action_7_T4, arg5: Action_7_T5, arg6: Action_7_T6, arg7: Action_7_T7) -> None: ...


Action_8_T1 = typing.TypeVar('Action_8_T1', contravariant=True)
Action_8_T2 = typing.TypeVar('Action_8_T2', contravariant=True)
Action_8_T3 = typing.TypeVar('Action_8_T3', contravariant=True)
Action_8_T4 = typing.TypeVar('Action_8_T4', contravariant=True)
Action_8_T5 = typing.TypeVar('Action_8_T5', contravariant=True)
Action_8_T6 = typing.TypeVar('Action_8_T6', contravariant=True)
Action_8_T7 = typing.TypeVar('Action_8_T7', contravariant=True)
Action_8_T8 = typing.TypeVar('Action_8_T8', contravariant=True)
class Action_8(typing.Generic[Action_8_T1, Action_8_T2, Action_8_T3, Action_8_T4, Action_8_T5, Action_8_T6, Action_8_T7, Action_8_T8], MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, arg1: Action_8_T1, arg2: Action_8_T2, arg3: Action_8_T3, arg4: Action_8_T4, arg5: Action_8_T5, arg6: Action_8_T6, arg7: Action_8_T7, arg8: Action_8_T8, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, arg1: Action_8_T1, arg2: Action_8_T2, arg3: Action_8_T3, arg4: Action_8_T4, arg5: Action_8_T5, arg6: Action_8_T6, arg7: Action_8_T7, arg8: Action_8_T8) -> None: ...


Action_9_T1 = typing.TypeVar('Action_9_T1', contravariant=True)
Action_9_T2 = typing.TypeVar('Action_9_T2', contravariant=True)
Action_9_T3 = typing.TypeVar('Action_9_T3', contravariant=True)
Action_9_T4 = typing.TypeVar('Action_9_T4', contravariant=True)
Action_9_T5 = typing.TypeVar('Action_9_T5', contravariant=True)
Action_9_T6 = typing.TypeVar('Action_9_T6', contravariant=True)
Action_9_T7 = typing.TypeVar('Action_9_T7', contravariant=True)
Action_9_T8 = typing.TypeVar('Action_9_T8', contravariant=True)
Action_9_T9 = typing.TypeVar('Action_9_T9', contravariant=True)
class Action_9(typing.Generic[Action_9_T1, Action_9_T2, Action_9_T3, Action_9_T4, Action_9_T5, Action_9_T6, Action_9_T7, Action_9_T8, Action_9_T9], MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, arg1: Action_9_T1, arg2: Action_9_T2, arg3: Action_9_T3, arg4: Action_9_T4, arg5: Action_9_T5, arg6: Action_9_T6, arg7: Action_9_T7, arg8: Action_9_T8, arg9: Action_9_T9, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, arg1: Action_9_T1, arg2: Action_9_T2, arg3: Action_9_T3, arg4: Action_9_T4, arg5: Action_9_T5, arg6: Action_9_T6, arg7: Action_9_T7, arg8: Action_9_T8, arg9: Action_9_T9) -> None: ...


class Activator(abc.ABC):
    # Skipped CreateInstance due to it being static, abstract and generic.

    CreateInstance : CreateInstance_MethodGroup
    class CreateInstance_MethodGroup:
        def __getitem__(self, t:typing.Type[CreateInstance_1_T1]) -> CreateInstance_1[CreateInstance_1_T1]: ...

        CreateInstance_1_T1 = typing.TypeVar('CreateInstance_1_T1')
        class CreateInstance_1(typing.Generic[CreateInstance_1_T1]):
            CreateInstance_1_T = Activator.CreateInstance_MethodGroup.CreateInstance_1_T1
            def __call__(self) -> CreateInstance_1_T:...

        @typing.overload
        def __call__(self, type: typing.Type[typing.Any]) -> typing.Any:...
        @typing.overload
        def __call__(self, type: typing.Type[typing.Any], args: Array_1[typing.Any]) -> typing.Any:...
        @typing.overload
        def __call__(self, assemblyName: str, typeName: str) -> ObjectHandle:...
        @typing.overload
        def __call__(self, type: typing.Type[typing.Any], nonPublic: bool) -> typing.Any:...
        @typing.overload
        def __call__(self, type: typing.Type[typing.Any], args: Array_1[typing.Any], activationAttributes: Array_1[typing.Any]) -> typing.Any:...
        @typing.overload
        def __call__(self, assemblyName: str, typeName: str, activationAttributes: Array_1[typing.Any]) -> ObjectHandle:...
        @typing.overload
        def __call__(self, type: typing.Type[typing.Any], bindingAttr: BindingFlags, binder: Binder, args: Array_1[typing.Any], culture: CultureInfo) -> typing.Any:...
        @typing.overload
        def __call__(self, type: typing.Type[typing.Any], bindingAttr: BindingFlags, binder: Binder, args: Array_1[typing.Any], culture: CultureInfo, activationAttributes: Array_1[typing.Any]) -> typing.Any:...
        @typing.overload
        def __call__(self, assemblyName: str, typeName: str, ignoreCase: bool, bindingAttr: BindingFlags, binder: Binder, args: Array_1[typing.Any], culture: CultureInfo, activationAttributes: Array_1[typing.Any]) -> ObjectHandle:...

    # Skipped CreateInstanceFrom due to it being static, abstract and generic.

    CreateInstanceFrom : CreateInstanceFrom_MethodGroup
    class CreateInstanceFrom_MethodGroup:
        @typing.overload
        def __call__(self, assemblyFile: str, typeName: str) -> ObjectHandle:...
        @typing.overload
        def __call__(self, assemblyFile: str, typeName: str, activationAttributes: Array_1[typing.Any]) -> ObjectHandle:...
        @typing.overload
        def __call__(self, assemblyFile: str, typeName: str, ignoreCase: bool, bindingAttr: BindingFlags, binder: Binder, args: Array_1[typing.Any], culture: CultureInfo, activationAttributes: Array_1[typing.Any]) -> ObjectHandle:...



class AggregateException(Exception):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, innerExceptions: IEnumerable_1[Exception]) -> None: ...
    @typing.overload
    def __init__(self, innerExceptions: Array_1[Exception]) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, innerException: Exception) -> None: ...
    @typing.overload
    def __init__(self, message: str, innerExceptions: IEnumerable_1[Exception]) -> None: ...
    @typing.overload
    def __init__(self, message: str, innerExceptions: Array_1[Exception]) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def InnerExceptions(self) -> ReadOnlyCollection_1[Exception]: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...
    def Flatten(self) -> AggregateException: ...
    def GetBaseException(self) -> Exception: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...
    def Handle(self, predicate: Func_2[Exception, bool]) -> None: ...
    def ToString(self) -> str: ...


class AppContext(abc.ABC):
    @classmethod
    @property
    def BaseDirectory(cls) -> str: ...
    @classmethod
    @property
    def TargetFrameworkName(cls) -> str: ...
    @staticmethod
    def GetData(name: str) -> typing.Any: ...
    @staticmethod
    def SetData(name: str, data: typing.Any) -> None: ...
    @staticmethod
    def SetSwitch(switchName: str, isEnabled: bool) -> None: ...
    @staticmethod
    def TryGetSwitch(switchName: str, isEnabled: clr.Reference[bool]) -> bool: ...


class AppDomain(MarshalByRefObject):
    @property
    def BaseDirectory(self) -> str: ...
    @classmethod
    @property
    def CurrentDomain(cls) -> AppDomain: ...
    @property
    def DynamicDirectory(self) -> str: ...
    @property
    def FriendlyName(self) -> str: ...
    @property
    def Id(self) -> int: ...
    @property
    def IsFullyTrusted(self) -> bool: ...
    @property
    def IsHomogenous(self) -> bool: ...
    @classmethod
    @property
    def MonitoringIsEnabled(cls) -> bool: ...
    @classmethod
    @MonitoringIsEnabled.setter
    def MonitoringIsEnabled(cls, value: bool) -> bool: ...
    @property
    def MonitoringSurvivedMemorySize(self) -> int: ...
    @classmethod
    @property
    def MonitoringSurvivedProcessMemorySize(cls) -> int: ...
    @property
    def MonitoringTotalAllocatedMemorySize(self) -> int: ...
    @property
    def MonitoringTotalProcessorTime(self) -> TimeSpan: ...
    @property
    def PermissionSet(self) -> PermissionSet: ...
    @property
    def RelativeSearchPath(self) -> str: ...
    @property
    def SetupInformation(self) -> AppDomainSetup: ...
    @property
    def ShadowCopyFiles(self) -> bool: ...
    def AppendPrivatePath(self, path: str) -> None: ...
    def ApplyPolicy(self, assemblyName: str) -> str: ...
    def ClearPrivatePath(self) -> None: ...
    def ClearShadowCopyPath(self) -> None: ...
    @staticmethod
    def CreateDomain(friendlyName: str) -> AppDomain: ...
    def GetAssemblies(self) -> Array_1[Assembly]: ...
    @staticmethod
    def GetCurrentThreadId() -> int: ...
    def GetData(self, name: str) -> typing.Any: ...
    def IsCompatibilitySwitchSet(self, value: str) -> typing.Optional[bool]: ...
    def IsDefaultAppDomain(self) -> bool: ...
    def IsFinalizingForUnload(self) -> bool: ...
    def ReflectionOnlyGetAssemblies(self) -> Array_1[Assembly]: ...
    def SetCachePath(self, path: str) -> None: ...
    def SetData(self, name: str, data: typing.Any) -> None: ...
    def SetDynamicBase(self, path: str) -> None: ...
    def SetPrincipalPolicy(self, policy: PrincipalPolicy) -> None: ...
    def SetShadowCopyFiles(self) -> None: ...
    def SetShadowCopyPath(self, path: str) -> None: ...
    def SetThreadPrincipal(self, principal: IPrincipal) -> None: ...
    def ToString(self) -> str: ...
    @staticmethod
    def Unload(domain: AppDomain) -> None: ...
    # Skipped CreateInstance due to it being static, abstract and generic.

    CreateInstance : CreateInstance_MethodGroup
    class CreateInstance_MethodGroup:
        @typing.overload
        def __call__(self, assemblyName: str, typeName: str) -> ObjectHandle:...
        @typing.overload
        def __call__(self, assemblyName: str, typeName: str, activationAttributes: Array_1[typing.Any]) -> ObjectHandle:...
        @typing.overload
        def __call__(self, assemblyName: str, typeName: str, ignoreCase: bool, bindingAttr: BindingFlags, binder: Binder, args: Array_1[typing.Any], culture: CultureInfo, activationAttributes: Array_1[typing.Any]) -> ObjectHandle:...

    # Skipped CreateInstanceAndUnwrap due to it being static, abstract and generic.

    CreateInstanceAndUnwrap : CreateInstanceAndUnwrap_MethodGroup
    class CreateInstanceAndUnwrap_MethodGroup:
        @typing.overload
        def __call__(self, assemblyName: str, typeName: str) -> typing.Any:...
        @typing.overload
        def __call__(self, assemblyName: str, typeName: str, activationAttributes: Array_1[typing.Any]) -> typing.Any:...
        @typing.overload
        def __call__(self, assemblyName: str, typeName: str, ignoreCase: bool, bindingAttr: BindingFlags, binder: Binder, args: Array_1[typing.Any], culture: CultureInfo, activationAttributes: Array_1[typing.Any]) -> typing.Any:...

    # Skipped CreateInstanceFrom due to it being static, abstract and generic.

    CreateInstanceFrom : CreateInstanceFrom_MethodGroup
    class CreateInstanceFrom_MethodGroup:
        @typing.overload
        def __call__(self, assemblyFile: str, typeName: str) -> ObjectHandle:...
        @typing.overload
        def __call__(self, assemblyFile: str, typeName: str, activationAttributes: Array_1[typing.Any]) -> ObjectHandle:...
        @typing.overload
        def __call__(self, assemblyFile: str, typeName: str, ignoreCase: bool, bindingAttr: BindingFlags, binder: Binder, args: Array_1[typing.Any], culture: CultureInfo, activationAttributes: Array_1[typing.Any]) -> ObjectHandle:...

    # Skipped CreateInstanceFromAndUnwrap due to it being static, abstract and generic.

    CreateInstanceFromAndUnwrap : CreateInstanceFromAndUnwrap_MethodGroup
    class CreateInstanceFromAndUnwrap_MethodGroup:
        @typing.overload
        def __call__(self, assemblyFile: str, typeName: str) -> typing.Any:...
        @typing.overload
        def __call__(self, assemblyFile: str, typeName: str, activationAttributes: Array_1[typing.Any]) -> typing.Any:...
        @typing.overload
        def __call__(self, assemblyFile: str, typeName: str, ignoreCase: bool, bindingAttr: BindingFlags, binder: Binder, args: Array_1[typing.Any], culture: CultureInfo, activationAttributes: Array_1[typing.Any]) -> typing.Any:...

    # Skipped ExecuteAssembly due to it being static, abstract and generic.

    ExecuteAssembly : ExecuteAssembly_MethodGroup
    class ExecuteAssembly_MethodGroup:
        @typing.overload
        def __call__(self, assemblyFile: str) -> int:...
        @typing.overload
        def __call__(self, assemblyFile: str, args: Array_1[str]) -> int:...
        @typing.overload
        def __call__(self, assemblyFile: str, args: Array_1[str], hashValue: Array_1[int], hashAlgorithm: AssemblyHashAlgorithm) -> int:...

    # Skipped ExecuteAssemblyByName due to it being static, abstract and generic.

    ExecuteAssemblyByName : ExecuteAssemblyByName_MethodGroup
    class ExecuteAssemblyByName_MethodGroup:
        @typing.overload
        def __call__(self, assemblyName: str) -> int:...
        @typing.overload
        def __call__(self, assemblyName: str, args: Array_1[str]) -> int:...
        @typing.overload
        def __call__(self, assemblyName: AssemblyName, args: Array_1[str]) -> int:...

    # Skipped Load due to it being static, abstract and generic.

    Load : Load_MethodGroup
    class Load_MethodGroup:
        @typing.overload
        def __call__(self, rawAssembly: Array_1[int]) -> Assembly:...
        @typing.overload
        def __call__(self, assemblyString: str) -> Assembly:...
        @typing.overload
        def __call__(self, assemblyRef: AssemblyName) -> Assembly:...
        @typing.overload
        def __call__(self, rawAssembly: Array_1[int], rawSymbolStore: Array_1[int]) -> Assembly:...



class AppDomainSetup:
    @property
    def ApplicationBase(self) -> str: ...
    @property
    def TargetFrameworkName(self) -> str: ...


class AppDomainUnloadedException(SystemException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, innerException: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...


class ApplicationException(Exception):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, innerException: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...


class ApplicationId:
    def __init__(self, publicKeyToken: Array_1[int], name: str, version: Version, processorArchitecture: str, culture: str) -> None: ...
    @property
    def Culture(self) -> str: ...
    @property
    def Name(self) -> str: ...
    @property
    def ProcessorArchitecture(self) -> str: ...
    @property
    def PublicKeyToken(self) -> Array_1[int]: ...
    @property
    def Version(self) -> Version: ...
    def Copy(self) -> ApplicationId: ...
    def Equals(self, o: typing.Any) -> bool: ...
    def GetHashCode(self) -> int: ...
    def ToString(self) -> str: ...


class ArgIterator:
    @typing.overload
    def __init__(self, arglist: RuntimeArgumentHandle) -> None: ...
    @typing.overload
    def __init__(self, arglist: RuntimeArgumentHandle, ptr: clr.Reference[None]) -> None: ...
    def End(self) -> None: ...
    def Equals(self, o: typing.Any) -> bool: ...
    def GetHashCode(self) -> int: ...
    def GetNextArgType(self) -> RuntimeTypeHandle: ...
    def GetRemainingCount(self) -> int: ...
    # Skipped GetNextArg due to it being static, abstract and generic.

    GetNextArg : GetNextArg_MethodGroup
    class GetNextArg_MethodGroup:
        @typing.overload
        def __call__(self) -> TypedReference:...
        @typing.overload
        def __call__(self, rth: RuntimeTypeHandle) -> TypedReference:...



class ArgumentException(SystemException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, innerException: Exception) -> None: ...
    @typing.overload
    def __init__(self, message: str, paramName: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, paramName: str, innerException: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def ParamName(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...


class ArgumentNullException(ArgumentException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str, innerException: Exception) -> None: ...
    @typing.overload
    def __init__(self, paramName: str) -> None: ...
    @typing.overload
    def __init__(self, paramName: str, message: str) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def ParamName(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...
    @staticmethod
    def ThrowIfNull(argument: typing.Any, paramName: str = ...) -> None: ...


class ArgumentOutOfRangeException(ArgumentException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str, innerException: Exception) -> None: ...
    @typing.overload
    def __init__(self, paramName: str) -> None: ...
    @typing.overload
    def __init__(self, paramName: str, actualValue: typing.Any, message: str) -> None: ...
    @typing.overload
    def __init__(self, paramName: str, message: str) -> None: ...
    @property
    def ActualValue(self) -> typing.Any: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def ParamName(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...


class ArithmeticException(SystemException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, innerException: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...


class Array_GenericClasses(abc.ABCMeta):
    Generic_Array_1_T = typing.TypeVar('Generic_Array_1_T')
    def __getitem__(self, types : typing.Type[Generic_Array_1_T]) -> typing.Type[Array_1[Generic_Array_1_T]]: ...

class Array(Array_0, metaclass =Array_GenericClasses): ...

Array_1_T = typing.TypeVar('Array_1_T', covariant=True)
class Array_1(Array_0, typing.Generic[Array_1_T]):...


class Array_0(IList, IStructuralEquatable, IStructuralComparable, ICloneable, abc.ABC):
    @property
    def IsFixedSize(self) -> bool: ...
    @property
    def IsReadOnly(self) -> bool: ...
    @property
    def IsSynchronized(self) -> bool: ...
    @property
    def Length(self) -> int: ...
    @property
    def LongLength(self) -> int: ...
    @classmethod
    @property
    def MaxLength(cls) -> int: ...
    @property
    def Rank(self) -> int: ...
    @property
    def SyncRoot(self) -> typing.Any: ...
    def Clone(self) -> typing.Any: ...
    @staticmethod
    def ConstrainedCopy(sourceArray: Array, sourceIndex: int, destinationArray: Array, destinationIndex: int, length: int) -> None: ...
    def GetEnumerator(self) -> IEnumerator: ...
    def GetLength(self, dimension: int) -> int: ...
    def GetLongLength(self, dimension: int) -> int: ...
    def GetLowerBound(self, dimension: int) -> int: ...
    def GetUpperBound(self, dimension: int) -> int: ...
    def Initialize(self) -> None: ...
    # Skipped AsReadOnly due to it being static, abstract and generic.

    AsReadOnly : AsReadOnly_MethodGroup
    class AsReadOnly_MethodGroup:
        def __getitem__(self, t:typing.Type[AsReadOnly_1_T1]) -> AsReadOnly_1[AsReadOnly_1_T1]: ...

        AsReadOnly_1_T1 = typing.TypeVar('AsReadOnly_1_T1')
        class AsReadOnly_1(typing.Generic[AsReadOnly_1_T1]):
            AsReadOnly_1_T = Array_0.AsReadOnly_MethodGroup.AsReadOnly_1_T1
            def __call__(self, array: Array_1[AsReadOnly_1_T]) -> ReadOnlyCollection_1[AsReadOnly_1_T]:...


    # Skipped BinarySearch due to it being static, abstract and generic.

    BinarySearch : BinarySearch_MethodGroup
    class BinarySearch_MethodGroup:
        def __getitem__(self, t:typing.Type[BinarySearch_1_T1]) -> BinarySearch_1[BinarySearch_1_T1]: ...

        BinarySearch_1_T1 = typing.TypeVar('BinarySearch_1_T1')
        class BinarySearch_1(typing.Generic[BinarySearch_1_T1]):
            BinarySearch_1_T = Array_0.BinarySearch_MethodGroup.BinarySearch_1_T1
            @typing.overload
            def __call__(self, array: Array_1[BinarySearch_1_T], value: BinarySearch_1_T) -> int:...
            @typing.overload
            def __call__(self, array: Array_1[BinarySearch_1_T], value: BinarySearch_1_T, comparer: IComparer_1[BinarySearch_1_T]) -> int:...
            @typing.overload
            def __call__(self, array: Array_1[BinarySearch_1_T], index: int, length: int, value: BinarySearch_1_T) -> int:...
            @typing.overload
            def __call__(self, array: Array_1[BinarySearch_1_T], index: int, length: int, value: BinarySearch_1_T, comparer: IComparer_1[BinarySearch_1_T]) -> int:...

        @typing.overload
        def __call__(self, array: Array, value: typing.Any) -> int:...
        @typing.overload
        def __call__(self, array: Array, value: typing.Any, comparer: IComparer) -> int:...
        @typing.overload
        def __call__(self, array: Array, index: int, length: int, value: typing.Any) -> int:...
        @typing.overload
        def __call__(self, array: Array, index: int, length: int, value: typing.Any, comparer: IComparer) -> int:...

    # Skipped Clear due to it being static, abstract and generic.

    Clear : Clear_MethodGroup
    class Clear_MethodGroup:
        @typing.overload
        def __call__(self, array: Array) -> None:...
        @typing.overload
        def __call__(self, array: Array, index: int, length: int) -> None:...

    # Skipped ConvertAll due to it being static, abstract and generic.

    ConvertAll : ConvertAll_MethodGroup
    class ConvertAll_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[ConvertAll_2_T1], typing.Type[ConvertAll_2_T2]]) -> ConvertAll_2[ConvertAll_2_T1, ConvertAll_2_T2]: ...

        ConvertAll_2_T1 = typing.TypeVar('ConvertAll_2_T1')
        ConvertAll_2_T2 = typing.TypeVar('ConvertAll_2_T2')
        class ConvertAll_2(typing.Generic[ConvertAll_2_T1, ConvertAll_2_T2]):
            ConvertAll_2_TInput = Array_0.ConvertAll_MethodGroup.ConvertAll_2_T1
            ConvertAll_2_TOutput = Array_0.ConvertAll_MethodGroup.ConvertAll_2_T2
            def __call__(self, array: Array_1[ConvertAll_2_TInput], converter: Converter_2[ConvertAll_2_TInput, ConvertAll_2_TOutput]) -> Array_1[ConvertAll_2_TOutput]:...


    # Skipped Copy due to it being static, abstract and generic.

    Copy : Copy_MethodGroup
    class Copy_MethodGroup:
        @typing.overload
        def __call__(self, sourceArray: Array, destinationArray: Array, length: int) -> None:...
        # Method Copy(sourceArray : Array, destinationArray : Array, length : Int64) was skipped since it collides with above method
        @typing.overload
        def __call__(self, sourceArray: Array, sourceIndex: int, destinationArray: Array, destinationIndex: int, length: int) -> None:...
        # Method Copy(sourceArray : Array, sourceIndex : Int64, destinationArray : Array, destinationIndex : Int64, length : Int64) was skipped since it collides with above method

    # Skipped CopyTo due to it being static, abstract and generic.

    CopyTo : CopyTo_MethodGroup
    class CopyTo_MethodGroup:
        def __call__(self, array: Array, index: int) -> None:...
        # Method CopyTo(array : Array, index : Int64) was skipped since it collides with above method

    # Skipped CreateInstance due to it being static, abstract and generic.

    CreateInstance : CreateInstance_MethodGroup
    class CreateInstance_MethodGroup:
        @typing.overload
        def __call__(self, elementType: typing.Type[typing.Any], length: int) -> Array:...
        @typing.overload
        def __call__(self, elementType: typing.Type[typing.Any], lengths: Array_1[int]) -> Array:...
        # Method CreateInstance(elementType : Type, lengths : Int64[]) was skipped since it collides with above method
        @typing.overload
        def __call__(self, elementType: typing.Type[typing.Any], length1: int, length2: int) -> Array:...
        @typing.overload
        def __call__(self, elementType: typing.Type[typing.Any], lengths: Array_1[int], lowerBounds: Array_1[int]) -> Array:...
        @typing.overload
        def __call__(self, elementType: typing.Type[typing.Any], length1: int, length2: int, length3: int) -> Array:...

    # Skipped Empty due to it being static, abstract and generic.

    Empty : Empty_MethodGroup
    class Empty_MethodGroup:
        def __getitem__(self, t:typing.Type[Empty_1_T1]) -> Empty_1[Empty_1_T1]: ...

        Empty_1_T1 = typing.TypeVar('Empty_1_T1')
        class Empty_1(typing.Generic[Empty_1_T1]):
            Empty_1_T = Array_0.Empty_MethodGroup.Empty_1_T1
            def __call__(self) -> Array_1[Empty_1_T]:...


    # Skipped Exists due to it being static, abstract and generic.

    Exists : Exists_MethodGroup
    class Exists_MethodGroup:
        def __getitem__(self, t:typing.Type[Exists_1_T1]) -> Exists_1[Exists_1_T1]: ...

        Exists_1_T1 = typing.TypeVar('Exists_1_T1')
        class Exists_1(typing.Generic[Exists_1_T1]):
            Exists_1_T = Array_0.Exists_MethodGroup.Exists_1_T1
            def __call__(self, array: Array_1[Exists_1_T], match: Predicate_1[Exists_1_T]) -> bool:...


    # Skipped Fill due to it being static, abstract and generic.

    Fill : Fill_MethodGroup
    class Fill_MethodGroup:
        def __getitem__(self, t:typing.Type[Fill_1_T1]) -> Fill_1[Fill_1_T1]: ...

        Fill_1_T1 = typing.TypeVar('Fill_1_T1')
        class Fill_1(typing.Generic[Fill_1_T1]):
            Fill_1_T = Array_0.Fill_MethodGroup.Fill_1_T1
            @typing.overload
            def __call__(self, array: Array_1[Fill_1_T], value: Fill_1_T) -> None:...
            @typing.overload
            def __call__(self, array: Array_1[Fill_1_T], value: Fill_1_T, startIndex: int, count: int) -> None:...


    # Skipped Find due to it being static, abstract and generic.

    Find : Find_MethodGroup
    class Find_MethodGroup:
        def __getitem__(self, t:typing.Type[Find_1_T1]) -> Find_1[Find_1_T1]: ...

        Find_1_T1 = typing.TypeVar('Find_1_T1')
        class Find_1(typing.Generic[Find_1_T1]):
            Find_1_T = Array_0.Find_MethodGroup.Find_1_T1
            def __call__(self, array: Array_1[Find_1_T], match: Predicate_1[Find_1_T]) -> Find_1_T:...


    # Skipped FindAll due to it being static, abstract and generic.

    FindAll : FindAll_MethodGroup
    class FindAll_MethodGroup:
        def __getitem__(self, t:typing.Type[FindAll_1_T1]) -> FindAll_1[FindAll_1_T1]: ...

        FindAll_1_T1 = typing.TypeVar('FindAll_1_T1')
        class FindAll_1(typing.Generic[FindAll_1_T1]):
            FindAll_1_T = Array_0.FindAll_MethodGroup.FindAll_1_T1
            def __call__(self, array: Array_1[FindAll_1_T], match: Predicate_1[FindAll_1_T]) -> Array_1[FindAll_1_T]:...


    # Skipped FindIndex due to it being static, abstract and generic.

    FindIndex : FindIndex_MethodGroup
    class FindIndex_MethodGroup:
        def __getitem__(self, t:typing.Type[FindIndex_1_T1]) -> FindIndex_1[FindIndex_1_T1]: ...

        FindIndex_1_T1 = typing.TypeVar('FindIndex_1_T1')
        class FindIndex_1(typing.Generic[FindIndex_1_T1]):
            FindIndex_1_T = Array_0.FindIndex_MethodGroup.FindIndex_1_T1
            @typing.overload
            def __call__(self, array: Array_1[FindIndex_1_T], match: Predicate_1[FindIndex_1_T]) -> int:...
            @typing.overload
            def __call__(self, array: Array_1[FindIndex_1_T], startIndex: int, match: Predicate_1[FindIndex_1_T]) -> int:...
            @typing.overload
            def __call__(self, array: Array_1[FindIndex_1_T], startIndex: int, count: int, match: Predicate_1[FindIndex_1_T]) -> int:...


    # Skipped FindLast due to it being static, abstract and generic.

    FindLast : FindLast_MethodGroup
    class FindLast_MethodGroup:
        def __getitem__(self, t:typing.Type[FindLast_1_T1]) -> FindLast_1[FindLast_1_T1]: ...

        FindLast_1_T1 = typing.TypeVar('FindLast_1_T1')
        class FindLast_1(typing.Generic[FindLast_1_T1]):
            FindLast_1_T = Array_0.FindLast_MethodGroup.FindLast_1_T1
            def __call__(self, array: Array_1[FindLast_1_T], match: Predicate_1[FindLast_1_T]) -> FindLast_1_T:...


    # Skipped FindLastIndex due to it being static, abstract and generic.

    FindLastIndex : FindLastIndex_MethodGroup
    class FindLastIndex_MethodGroup:
        def __getitem__(self, t:typing.Type[FindLastIndex_1_T1]) -> FindLastIndex_1[FindLastIndex_1_T1]: ...

        FindLastIndex_1_T1 = typing.TypeVar('FindLastIndex_1_T1')
        class FindLastIndex_1(typing.Generic[FindLastIndex_1_T1]):
            FindLastIndex_1_T = Array_0.FindLastIndex_MethodGroup.FindLastIndex_1_T1
            @typing.overload
            def __call__(self, array: Array_1[FindLastIndex_1_T], match: Predicate_1[FindLastIndex_1_T]) -> int:...
            @typing.overload
            def __call__(self, array: Array_1[FindLastIndex_1_T], startIndex: int, match: Predicate_1[FindLastIndex_1_T]) -> int:...
            @typing.overload
            def __call__(self, array: Array_1[FindLastIndex_1_T], startIndex: int, count: int, match: Predicate_1[FindLastIndex_1_T]) -> int:...


    # Skipped ForEach due to it being static, abstract and generic.

    ForEach : ForEach_MethodGroup
    class ForEach_MethodGroup:
        def __getitem__(self, t:typing.Type[ForEach_1_T1]) -> ForEach_1[ForEach_1_T1]: ...

        ForEach_1_T1 = typing.TypeVar('ForEach_1_T1')
        class ForEach_1(typing.Generic[ForEach_1_T1]):
            ForEach_1_T = Array_0.ForEach_MethodGroup.ForEach_1_T1
            def __call__(self, array: Array_1[ForEach_1_T], action: Action_1[ForEach_1_T]) -> None:...


    # Skipped GetValue due to it being static, abstract and generic.

    GetValue : GetValue_MethodGroup
    class GetValue_MethodGroup:
        @typing.overload
        def __call__(self, index: int) -> typing.Any:...
        # Method GetValue(index : Int64) was skipped since it collides with above method
        @typing.overload
        def __call__(self, indices: Array_1[int]) -> typing.Any:...
        # Method GetValue(indices : Int64[]) was skipped since it collides with above method
        @typing.overload
        def __call__(self, index1: int, index2: int) -> typing.Any:...
        # Method GetValue(index1 : Int64, index2 : Int64) was skipped since it collides with above method
        @typing.overload
        def __call__(self, index1: int, index2: int, index3: int) -> typing.Any:...
        # Method GetValue(index1 : Int64, index2 : Int64, index3 : Int64) was skipped since it collides with above method

    # Skipped IndexOf due to it being static, abstract and generic.

    IndexOf : IndexOf_MethodGroup
    class IndexOf_MethodGroup:
        def __getitem__(self, t:typing.Type[IndexOf_1_T1]) -> IndexOf_1[IndexOf_1_T1]: ...

        IndexOf_1_T1 = typing.TypeVar('IndexOf_1_T1')
        class IndexOf_1(typing.Generic[IndexOf_1_T1]):
            IndexOf_1_T = Array_0.IndexOf_MethodGroup.IndexOf_1_T1
            @typing.overload
            def __call__(self, array: Array_1[IndexOf_1_T], value: IndexOf_1_T) -> int:...
            @typing.overload
            def __call__(self, array: Array_1[IndexOf_1_T], value: IndexOf_1_T, startIndex: int) -> int:...
            @typing.overload
            def __call__(self, array: Array_1[IndexOf_1_T], value: IndexOf_1_T, startIndex: int, count: int) -> int:...

        @typing.overload
        def __call__(self, array: Array, value: typing.Any) -> int:...
        @typing.overload
        def __call__(self, array: Array, value: typing.Any, startIndex: int) -> int:...
        @typing.overload
        def __call__(self, array: Array, value: typing.Any, startIndex: int, count: int) -> int:...

    # Skipped LastIndexOf due to it being static, abstract and generic.

    LastIndexOf : LastIndexOf_MethodGroup
    class LastIndexOf_MethodGroup:
        def __getitem__(self, t:typing.Type[LastIndexOf_1_T1]) -> LastIndexOf_1[LastIndexOf_1_T1]: ...

        LastIndexOf_1_T1 = typing.TypeVar('LastIndexOf_1_T1')
        class LastIndexOf_1(typing.Generic[LastIndexOf_1_T1]):
            LastIndexOf_1_T = Array_0.LastIndexOf_MethodGroup.LastIndexOf_1_T1
            @typing.overload
            def __call__(self, array: Array_1[LastIndexOf_1_T], value: LastIndexOf_1_T) -> int:...
            @typing.overload
            def __call__(self, array: Array_1[LastIndexOf_1_T], value: LastIndexOf_1_T, startIndex: int) -> int:...
            @typing.overload
            def __call__(self, array: Array_1[LastIndexOf_1_T], value: LastIndexOf_1_T, startIndex: int, count: int) -> int:...

        @typing.overload
        def __call__(self, array: Array, value: typing.Any) -> int:...
        @typing.overload
        def __call__(self, array: Array, value: typing.Any, startIndex: int) -> int:...
        @typing.overload
        def __call__(self, array: Array, value: typing.Any, startIndex: int, count: int) -> int:...

    # Skipped Resize due to it being static, abstract and generic.

    Resize : Resize_MethodGroup
    class Resize_MethodGroup:
        def __getitem__(self, t:typing.Type[Resize_1_T1]) -> Resize_1[Resize_1_T1]: ...

        Resize_1_T1 = typing.TypeVar('Resize_1_T1')
        class Resize_1(typing.Generic[Resize_1_T1]):
            Resize_1_T = Array_0.Resize_MethodGroup.Resize_1_T1
            def __call__(self, array: clr.Reference[Array_1[Resize_1_T]], newSize: int) -> None:...


    # Skipped Reverse due to it being static, abstract and generic.

    Reverse : Reverse_MethodGroup
    class Reverse_MethodGroup:
        def __getitem__(self, t:typing.Type[Reverse_1_T1]) -> Reverse_1[Reverse_1_T1]: ...

        Reverse_1_T1 = typing.TypeVar('Reverse_1_T1')
        class Reverse_1(typing.Generic[Reverse_1_T1]):
            Reverse_1_T = Array_0.Reverse_MethodGroup.Reverse_1_T1
            @typing.overload
            def __call__(self, array: Array_1[Reverse_1_T]) -> None:...
            @typing.overload
            def __call__(self, array: Array_1[Reverse_1_T], index: int, length: int) -> None:...

        @typing.overload
        def __call__(self, array: Array) -> None:...
        @typing.overload
        def __call__(self, array: Array, index: int, length: int) -> None:...

    # Skipped SetValue due to it being static, abstract and generic.

    SetValue : SetValue_MethodGroup
    class SetValue_MethodGroup:
        @typing.overload
        def __call__(self, value: typing.Any, index: int) -> None:...
        # Method SetValue(value : Object, index : Int64) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: typing.Any, indices: Array_1[int]) -> None:...
        # Method SetValue(value : Object, indices : Int64[]) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: typing.Any, index1: int, index2: int) -> None:...
        # Method SetValue(value : Object, index1 : Int64, index2 : Int64) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: typing.Any, index1: int, index2: int, index3: int) -> None:...
        # Method SetValue(value : Object, index1 : Int64, index2 : Int64, index3 : Int64) was skipped since it collides with above method

    # Skipped Sort due to it being static, abstract and generic.

    Sort : Sort_MethodGroup
    class Sort_MethodGroup:
        @typing.overload
        def __getitem__(self, t:typing.Type[Sort_1_T1]) -> Sort_1[Sort_1_T1]: ...

        Sort_1_T1 = typing.TypeVar('Sort_1_T1')
        class Sort_1(typing.Generic[Sort_1_T1]):
            Sort_1_T = Array_0.Sort_MethodGroup.Sort_1_T1
            @typing.overload
            def __call__(self, array: Array_1[Sort_1_T]) -> None:...
            @typing.overload
            def __call__(self, array: Array_1[Sort_1_T], comparison: Comparison_1[Sort_1_T]) -> None:...
            @typing.overload
            def __call__(self, array: Array_1[Sort_1_T], comparer: IComparer_1[Sort_1_T]) -> None:...
            @typing.overload
            def __call__(self, array: Array_1[Sort_1_T], index: int, length: int) -> None:...
            @typing.overload
            def __call__(self, array: Array_1[Sort_1_T], index: int, length: int, comparer: IComparer_1[Sort_1_T]) -> None:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Sort_2_T1], typing.Type[Sort_2_T2]]) -> Sort_2[Sort_2_T1, Sort_2_T2]: ...

        Sort_2_T1 = typing.TypeVar('Sort_2_T1')
        Sort_2_T2 = typing.TypeVar('Sort_2_T2')
        class Sort_2(typing.Generic[Sort_2_T1, Sort_2_T2]):
            Sort_2_TKey = Array_0.Sort_MethodGroup.Sort_2_T1
            Sort_2_TValue = Array_0.Sort_MethodGroup.Sort_2_T2
            @typing.overload
            def __call__(self, keys: Array_1[Sort_2_TKey], items: Array_1[Sort_2_TValue]) -> None:...
            @typing.overload
            def __call__(self, keys: Array_1[Sort_2_TKey], items: Array_1[Sort_2_TValue], comparer: IComparer_1[Sort_2_TKey]) -> None:...
            @typing.overload
            def __call__(self, keys: Array_1[Sort_2_TKey], items: Array_1[Sort_2_TValue], index: int, length: int) -> None:...
            @typing.overload
            def __call__(self, keys: Array_1[Sort_2_TKey], items: Array_1[Sort_2_TValue], index: int, length: int, comparer: IComparer_1[Sort_2_TKey]) -> None:...

        @typing.overload
        def __call__(self, array: Array) -> None:...
        @typing.overload
        def __call__(self, keys: Array, items: Array) -> None:...
        @typing.overload
        def __call__(self, array: Array, comparer: IComparer) -> None:...
        @typing.overload
        def __call__(self, array: Array, index: int, length: int) -> None:...
        @typing.overload
        def __call__(self, keys: Array, items: Array, comparer: IComparer) -> None:...
        @typing.overload
        def __call__(self, array: Array, index: int, length: int, comparer: IComparer) -> None:...
        @typing.overload
        def __call__(self, keys: Array, items: Array, index: int, length: int) -> None:...
        @typing.overload
        def __call__(self, keys: Array, items: Array, index: int, length: int, comparer: IComparer) -> None:...

    # Skipped TrueForAll due to it being static, abstract and generic.

    TrueForAll : TrueForAll_MethodGroup
    class TrueForAll_MethodGroup:
        def __getitem__(self, t:typing.Type[TrueForAll_1_T1]) -> TrueForAll_1[TrueForAll_1_T1]: ...

        TrueForAll_1_T1 = typing.TypeVar('TrueForAll_1_T1')
        class TrueForAll_1(typing.Generic[TrueForAll_1_T1]):
            TrueForAll_1_T = Array_0.TrueForAll_MethodGroup.TrueForAll_1_T1
            def __call__(self, array: Array_1[TrueForAll_1_T], match: Predicate_1[TrueForAll_1_T]) -> bool:...




class ArraySegment_GenericClasses(abc.ABCMeta):
    Generic_ArraySegment_GenericClasses_ArraySegment_1_T = typing.TypeVar('Generic_ArraySegment_GenericClasses_ArraySegment_1_T')
    def __getitem__(self, types : typing.Type[Generic_ArraySegment_GenericClasses_ArraySegment_1_T]) -> typing.Type[ArraySegment_1[Generic_ArraySegment_GenericClasses_ArraySegment_1_T]]: ...

ArraySegment : ArraySegment_GenericClasses

ArraySegment_1_T = typing.TypeVar('ArraySegment_1_T')
class ArraySegment_1(typing.Generic[ArraySegment_1_T], IReadOnlyList_1[ArraySegment_1_T], IList_1[ArraySegment_1_T]):
    @typing.overload
    def __init__(self, array: Array_1[ArraySegment_1_T]) -> None: ...
    @typing.overload
    def __init__(self, array: Array_1[ArraySegment_1_T], offset: int, count: int) -> None: ...
    @property
    def Array(self) -> Array_1[ArraySegment_1_T]: ...
    @property
    def Count(self) -> int: ...
    @classmethod
    @property
    def Empty(cls) -> ArraySegment_1[ArraySegment_1_T]: ...
    @property
    def Item(self) -> ArraySegment_1_T: ...
    @Item.setter
    def Item(self, value: ArraySegment_1_T) -> ArraySegment_1_T: ...
    @property
    def Offset(self) -> int: ...
    def GetEnumerator(self) -> ArraySegment_1.Enumerator_1[ArraySegment_1_T]: ...
    def GetHashCode(self) -> int: ...
    def __eq__(self, a: ArraySegment_1[ArraySegment_1_T], b: ArraySegment_1[ArraySegment_1_T]) -> bool: ...
    # Operator not supported op_Implicit(array: T[])
    def __ne__(self, a: ArraySegment_1[ArraySegment_1_T], b: ArraySegment_1[ArraySegment_1_T]) -> bool: ...
    def ToArray(self) -> Array_1[ArraySegment_1_T]: ...
    # Skipped CopyTo due to it being static, abstract and generic.

    CopyTo : CopyTo_MethodGroup[ArraySegment_1_T]
    CopyTo_MethodGroup_ArraySegment_1_T = typing.TypeVar('CopyTo_MethodGroup_ArraySegment_1_T')
    class CopyTo_MethodGroup(typing.Generic[CopyTo_MethodGroup_ArraySegment_1_T]):
        CopyTo_MethodGroup_ArraySegment_1_T = ArraySegment_1.CopyTo_MethodGroup_ArraySegment_1_T
        @typing.overload
        def __call__(self, destination: Array_1[CopyTo_MethodGroup_ArraySegment_1_T]) -> None:...
        @typing.overload
        def __call__(self, destination: ArraySegment_1[CopyTo_MethodGroup_ArraySegment_1_T]) -> None:...
        @typing.overload
        def __call__(self, destination: Array_1[CopyTo_MethodGroup_ArraySegment_1_T], destinationIndex: int) -> None:...

    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup[ArraySegment_1_T]
    Equals_MethodGroup_ArraySegment_1_T = typing.TypeVar('Equals_MethodGroup_ArraySegment_1_T')
    class Equals_MethodGroup(typing.Generic[Equals_MethodGroup_ArraySegment_1_T]):
        Equals_MethodGroup_ArraySegment_1_T = ArraySegment_1.Equals_MethodGroup_ArraySegment_1_T
        @typing.overload
        def __call__(self, obj: ArraySegment_1[Equals_MethodGroup_ArraySegment_1_T]) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...

    # Skipped Slice due to it being static, abstract and generic.

    Slice : Slice_MethodGroup[ArraySegment_1_T]
    Slice_MethodGroup_ArraySegment_1_T = typing.TypeVar('Slice_MethodGroup_ArraySegment_1_T')
    class Slice_MethodGroup(typing.Generic[Slice_MethodGroup_ArraySegment_1_T]):
        Slice_MethodGroup_ArraySegment_1_T = ArraySegment_1.Slice_MethodGroup_ArraySegment_1_T
        @typing.overload
        def __call__(self, index: int) -> ArraySegment_1[Slice_MethodGroup_ArraySegment_1_T]:...
        @typing.overload
        def __call__(self, index: int, count: int) -> ArraySegment_1[Slice_MethodGroup_ArraySegment_1_T]:...


    Enumerator_GenericClasses_ArraySegment_1_T = typing.TypeVar('Enumerator_GenericClasses_ArraySegment_1_T')
    class Enumerator_GenericClasses(typing.Generic[Enumerator_GenericClasses_ArraySegment_1_T], abc.ABCMeta):
        Enumerator_GenericClasses_ArraySegment_1_T = ArraySegment_1.Enumerator_GenericClasses_ArraySegment_1_T
        def __call__(self) -> ArraySegment_1.Enumerator_1[Enumerator_GenericClasses_ArraySegment_1_T]: ...

    Enumerator : Enumerator_GenericClasses[ArraySegment_1_T]

    Enumerator_1_T = typing.TypeVar('Enumerator_1_T')
    class Enumerator_1(typing.Generic[Enumerator_1_T], IEnumerator_1[Enumerator_1_T]):
        Enumerator_1_T = ArraySegment_1.Enumerator_1_T
        @property
        def Current(self) -> Enumerator_1_T: ...
        def Dispose(self) -> None: ...
        def MoveNext(self) -> bool: ...



class ArrayTypeMismatchException(SystemException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, innerException: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...


class AssemblyLoadEventArgs(EventArgs):
    def __init__(self, loadedAssembly: Assembly) -> None: ...
    @property
    def LoadedAssembly(self) -> Assembly: ...


class AssemblyLoadEventHandler(MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, sender: typing.Any, args: AssemblyLoadEventArgs, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: typing.Any, args: AssemblyLoadEventArgs) -> None: ...


class AsyncCallback(MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, ar: IAsyncResult, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, ar: IAsyncResult) -> None: ...


class Attribute(abc.ABC):
    @property
    def TypeId(self) -> typing.Any: ...
    def Equals(self, obj: typing.Any) -> bool: ...
    def GetHashCode(self) -> int: ...
    def IsDefaultAttribute(self) -> bool: ...
    def Match(self, obj: typing.Any) -> bool: ...
    # Skipped GetCustomAttribute due to it being static, abstract and generic.

    GetCustomAttribute : GetCustomAttribute_MethodGroup
    class GetCustomAttribute_MethodGroup:
        @typing.overload
        def __call__(self, element: MemberInfo, attributeType: typing.Type[typing.Any]) -> Attribute:...
        @typing.overload
        def __call__(self, element: ParameterInfo, attributeType: typing.Type[typing.Any]) -> Attribute:...
        @typing.overload
        def __call__(self, element: Module, attributeType: typing.Type[typing.Any]) -> Attribute:...
        @typing.overload
        def __call__(self, element: Assembly, attributeType: typing.Type[typing.Any]) -> Attribute:...
        @typing.overload
        def __call__(self, element: MemberInfo, attributeType: typing.Type[typing.Any], inherit: bool) -> Attribute:...
        @typing.overload
        def __call__(self, element: ParameterInfo, attributeType: typing.Type[typing.Any], inherit: bool) -> Attribute:...
        @typing.overload
        def __call__(self, element: Module, attributeType: typing.Type[typing.Any], inherit: bool) -> Attribute:...
        @typing.overload
        def __call__(self, element: Assembly, attributeType: typing.Type[typing.Any], inherit: bool) -> Attribute:...

    # Skipped GetCustomAttributes due to it being static, abstract and generic.

    GetCustomAttributes : GetCustomAttributes_MethodGroup
    class GetCustomAttributes_MethodGroup:
        @typing.overload
        def __call__(self, element: MemberInfo) -> Array_1[Attribute]:...
        @typing.overload
        def __call__(self, element: ParameterInfo) -> Array_1[Attribute]:...
        @typing.overload
        def __call__(self, element: Module) -> Array_1[Attribute]:...
        @typing.overload
        def __call__(self, element: Assembly) -> Array_1[Attribute]:...
        @typing.overload
        def __call__(self, element: MemberInfo, attributeType: typing.Type[typing.Any]) -> Array_1[Attribute]:...
        @typing.overload
        def __call__(self, element: ParameterInfo, attributeType: typing.Type[typing.Any]) -> Array_1[Attribute]:...
        @typing.overload
        def __call__(self, element: Module, attributeType: typing.Type[typing.Any]) -> Array_1[Attribute]:...
        @typing.overload
        def __call__(self, element: Assembly, attributeType: typing.Type[typing.Any]) -> Array_1[Attribute]:...
        @typing.overload
        def __call__(self, element: MemberInfo, inherit: bool) -> Array_1[Attribute]:...
        @typing.overload
        def __call__(self, element: ParameterInfo, inherit: bool) -> Array_1[Attribute]:...
        @typing.overload
        def __call__(self, element: Module, inherit: bool) -> Array_1[Attribute]:...
        @typing.overload
        def __call__(self, element: Assembly, inherit: bool) -> Array_1[Attribute]:...
        @typing.overload
        def __call__(self, element: MemberInfo, attributeType: typing.Type[typing.Any], inherit: bool) -> Array_1[Attribute]:...
        @typing.overload
        def __call__(self, element: ParameterInfo, attributeType: typing.Type[typing.Any], inherit: bool) -> Array_1[Attribute]:...
        @typing.overload
        def __call__(self, element: Module, attributeType: typing.Type[typing.Any], inherit: bool) -> Array_1[Attribute]:...
        @typing.overload
        def __call__(self, element: Assembly, attributeType: typing.Type[typing.Any], inherit: bool) -> Array_1[Attribute]:...

    # Skipped IsDefined due to it being static, abstract and generic.

    IsDefined : IsDefined_MethodGroup
    class IsDefined_MethodGroup:
        @typing.overload
        def __call__(self, element: MemberInfo, attributeType: typing.Type[typing.Any]) -> bool:...
        @typing.overload
        def __call__(self, element: ParameterInfo, attributeType: typing.Type[typing.Any]) -> bool:...
        @typing.overload
        def __call__(self, element: Module, attributeType: typing.Type[typing.Any]) -> bool:...
        @typing.overload
        def __call__(self, element: Assembly, attributeType: typing.Type[typing.Any]) -> bool:...
        @typing.overload
        def __call__(self, element: MemberInfo, attributeType: typing.Type[typing.Any], inherit: bool) -> bool:...
        @typing.overload
        def __call__(self, element: ParameterInfo, attributeType: typing.Type[typing.Any], inherit: bool) -> bool:...
        @typing.overload
        def __call__(self, element: Module, attributeType: typing.Type[typing.Any], inherit: bool) -> bool:...
        @typing.overload
        def __call__(self, element: Assembly, attributeType: typing.Type[typing.Any], inherit: bool) -> bool:...



class AttributeTargets(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Assembly : AttributeTargets # 1
    Module : AttributeTargets # 2
    Class : AttributeTargets # 4
    Struct : AttributeTargets # 8
    Enum : AttributeTargets # 16
    Constructor : AttributeTargets # 32
    Method : AttributeTargets # 64
    Property : AttributeTargets # 128
    Field : AttributeTargets # 256
    Event : AttributeTargets # 512
    Interface : AttributeTargets # 1024
    Parameter : AttributeTargets # 2048
    Delegate : AttributeTargets # 4096
    ReturnValue : AttributeTargets # 8192
    GenericParameter : AttributeTargets # 16384
    All : AttributeTargets # 32767


class AttributeUsageAttribute(Attribute):
    def __init__(self, validOn: AttributeTargets) -> None: ...
    @property
    def AllowMultiple(self) -> bool: ...
    @AllowMultiple.setter
    def AllowMultiple(self, value: bool) -> bool: ...
    @property
    def Inherited(self) -> bool: ...
    @Inherited.setter
    def Inherited(self, value: bool) -> bool: ...
    @property
    def TypeId(self) -> typing.Any: ...
    @property
    def ValidOn(self) -> AttributeTargets: ...


class BadImageFormatException(SystemException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, fileName: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, fileName: str, inner: Exception) -> None: ...
    @typing.overload
    def __init__(self, message: str, inner: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def FileName(self) -> str: ...
    @property
    def FusionLog(self) -> str: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...
    def ToString(self) -> str: ...


class Base64FormattingOptions(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    None_ : Base64FormattingOptions # 0
    InsertLineBreaks : Base64FormattingOptions # 1


class BitConverter(abc.ABC):
    IsLittleEndian : bool
    @staticmethod
    def DoubleToInt64Bits(value: float) -> int: ...
    @staticmethod
    def DoubleToUInt64Bits(value: float) -> int: ...
    @staticmethod
    def HalfToInt16Bits(value: Half) -> int: ...
    @staticmethod
    def HalfToUInt16Bits(value: Half) -> int: ...
    @staticmethod
    def Int16BitsToHalf(value: int) -> Half: ...
    @staticmethod
    def Int32BitsToSingle(value: int) -> float: ...
    @staticmethod
    def Int64BitsToDouble(value: int) -> float: ...
    @staticmethod
    def SingleToInt32Bits(value: float) -> int: ...
    @staticmethod
    def SingleToUInt32Bits(value: float) -> int: ...
    @staticmethod
    def UInt16BitsToHalf(value: int) -> Half: ...
    @staticmethod
    def UInt32BitsToSingle(value: int) -> float: ...
    @staticmethod
    def UInt64BitsToDouble(value: int) -> float: ...
    # Skipped GetBytes due to it being static, abstract and generic.

    GetBytes : GetBytes_MethodGroup
    class GetBytes_MethodGroup:
        @typing.overload
        def __call__(self, value: Half) -> Array_1[int]:...
        @typing.overload
        def __call__(self, value: float) -> Array_1[int]:...
        # Method GetBytes(value : Double) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: str) -> Array_1[int]:...
        # Method GetBytes(value : Int16) was skipped since it collides with above method
        # Method GetBytes(value : Int32) was skipped since it collides with above method
        # Method GetBytes(value : Int64) was skipped since it collides with above method
        # Method GetBytes(value : UInt16) was skipped since it collides with above method
        # Method GetBytes(value : UInt32) was skipped since it collides with above method
        # Method GetBytes(value : UInt64) was skipped since it collides with above method
        # Method GetBytes(value : Boolean) was skipped since it collides with above method

    # Skipped ToBoolean due to it being static, abstract and generic.

    ToBoolean : ToBoolean_MethodGroup
    class ToBoolean_MethodGroup:
        @typing.overload
        def __call__(self, value: ReadOnlySpan_1[int]) -> bool:...
        @typing.overload
        def __call__(self, value: Array_1[int], startIndex: int) -> bool:...

    # Skipped ToChar due to it being static, abstract and generic.

    ToChar : ToChar_MethodGroup
    class ToChar_MethodGroup:
        @typing.overload
        def __call__(self, value: ReadOnlySpan_1[int]) -> str:...
        @typing.overload
        def __call__(self, value: Array_1[int], startIndex: int) -> str:...

    # Skipped ToDouble due to it being static, abstract and generic.

    ToDouble : ToDouble_MethodGroup
    class ToDouble_MethodGroup:
        @typing.overload
        def __call__(self, value: ReadOnlySpan_1[int]) -> float:...
        @typing.overload
        def __call__(self, value: Array_1[int], startIndex: int) -> float:...

    # Skipped ToHalf due to it being static, abstract and generic.

    ToHalf : ToHalf_MethodGroup
    class ToHalf_MethodGroup:
        @typing.overload
        def __call__(self, value: ReadOnlySpan_1[int]) -> Half:...
        @typing.overload
        def __call__(self, value: Array_1[int], startIndex: int) -> Half:...

    # Skipped ToInt16 due to it being static, abstract and generic.

    ToInt16 : ToInt16_MethodGroup
    class ToInt16_MethodGroup:
        @typing.overload
        def __call__(self, value: ReadOnlySpan_1[int]) -> int:...
        @typing.overload
        def __call__(self, value: Array_1[int], startIndex: int) -> int:...

    # Skipped ToInt32 due to it being static, abstract and generic.

    ToInt32 : ToInt32_MethodGroup
    class ToInt32_MethodGroup:
        @typing.overload
        def __call__(self, value: ReadOnlySpan_1[int]) -> int:...
        @typing.overload
        def __call__(self, value: Array_1[int], startIndex: int) -> int:...

    # Skipped ToInt64 due to it being static, abstract and generic.

    ToInt64 : ToInt64_MethodGroup
    class ToInt64_MethodGroup:
        @typing.overload
        def __call__(self, value: ReadOnlySpan_1[int]) -> int:...
        @typing.overload
        def __call__(self, value: Array_1[int], startIndex: int) -> int:...

    # Skipped ToSingle due to it being static, abstract and generic.

    ToSingle : ToSingle_MethodGroup
    class ToSingle_MethodGroup:
        @typing.overload
        def __call__(self, value: ReadOnlySpan_1[int]) -> float:...
        @typing.overload
        def __call__(self, value: Array_1[int], startIndex: int) -> float:...

    # Skipped ToString due to it being static, abstract and generic.

    ToString : ToString_MethodGroup
    class ToString_MethodGroup:
        @typing.overload
        def __call__(self, value: Array_1[int]) -> str:...
        @typing.overload
        def __call__(self, value: Array_1[int], startIndex: int) -> str:...
        @typing.overload
        def __call__(self, value: Array_1[int], startIndex: int, length: int) -> str:...

    # Skipped ToUInt16 due to it being static, abstract and generic.

    ToUInt16 : ToUInt16_MethodGroup
    class ToUInt16_MethodGroup:
        @typing.overload
        def __call__(self, value: ReadOnlySpan_1[int]) -> int:...
        @typing.overload
        def __call__(self, value: Array_1[int], startIndex: int) -> int:...

    # Skipped ToUInt32 due to it being static, abstract and generic.

    ToUInt32 : ToUInt32_MethodGroup
    class ToUInt32_MethodGroup:
        @typing.overload
        def __call__(self, value: ReadOnlySpan_1[int]) -> int:...
        @typing.overload
        def __call__(self, value: Array_1[int], startIndex: int) -> int:...

    # Skipped ToUInt64 due to it being static, abstract and generic.

    ToUInt64 : ToUInt64_MethodGroup
    class ToUInt64_MethodGroup:
        @typing.overload
        def __call__(self, value: ReadOnlySpan_1[int]) -> int:...
        @typing.overload
        def __call__(self, value: Array_1[int], startIndex: int) -> int:...

    # Skipped TryWriteBytes due to it being static, abstract and generic.

    TryWriteBytes : TryWriteBytes_MethodGroup
    class TryWriteBytes_MethodGroup:
        @typing.overload
        def __call__(self, destination: Span_1[int], value: Half) -> bool:...
        @typing.overload
        def __call__(self, destination: Span_1[int], value: float) -> bool:...
        # Method TryWriteBytes(destination : Span`1, value : Double) was skipped since it collides with above method
        @typing.overload
        def __call__(self, destination: Span_1[int], value: str) -> bool:...
        # Method TryWriteBytes(destination : Span`1, value : Int16) was skipped since it collides with above method
        # Method TryWriteBytes(destination : Span`1, value : Int32) was skipped since it collides with above method
        # Method TryWriteBytes(destination : Span`1, value : Int64) was skipped since it collides with above method
        # Method TryWriteBytes(destination : Span`1, value : UInt16) was skipped since it collides with above method
        # Method TryWriteBytes(destination : Span`1, value : UInt32) was skipped since it collides with above method
        # Method TryWriteBytes(destination : Span`1, value : UInt64) was skipped since it collides with above method
        # Method TryWriteBytes(destination : Span`1, value : Boolean) was skipped since it collides with above method



class Boolean(IEquatable_1[bool], IComparable_1[bool], IConvertible, IComparable_0):
    FalseString : str
    TrueString : str
    def GetHashCode(self) -> int: ...
    def GetTypeCode(self) -> TypeCode: ...
    def TryFormat(self, destination: Span_1[str], charsWritten: clr.Reference[int]) -> bool: ...
    # Skipped CompareTo due to it being static, abstract and generic.

    CompareTo : CompareTo_MethodGroup
    class CompareTo_MethodGroup:
        @typing.overload
        def __call__(self, value: bool) -> int:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> int:...

    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, obj: bool) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...

    # Skipped Parse due to it being static, abstract and generic.

    Parse : Parse_MethodGroup
    class Parse_MethodGroup:
        @typing.overload
        def __call__(self, value: ReadOnlySpan_1[str]) -> bool:...
        @typing.overload
        def __call__(self, value: str) -> bool:...

    # Skipped ToString due to it being static, abstract and generic.

    ToString : ToString_MethodGroup
    class ToString_MethodGroup:
        @typing.overload
        def __call__(self) -> str:...
        @typing.overload
        def __call__(self, provider: IFormatProvider) -> str:...

    # Skipped TryParse due to it being static, abstract and generic.

    TryParse : TryParse_MethodGroup
    class TryParse_MethodGroup:
        @typing.overload
        def __call__(self, value: ReadOnlySpan_1[str], result: clr.Reference[bool]) -> bool:...
        @typing.overload
        def __call__(self, value: str, result: clr.Reference[bool]) -> bool:...



class Buffer(abc.ABC):
    @staticmethod
    def BlockCopy(src: Array, srcOffset: int, dst: Array, dstOffset: int, count: int) -> None: ...
    @staticmethod
    def ByteLength(array: Array) -> int: ...
    @staticmethod
    def GetByte(array: Array, index: int) -> int: ...
    @staticmethod
    def SetByte(array: Array, index: int, value: int) -> None: ...
    # Skipped MemoryCopy due to it being static, abstract and generic.

    MemoryCopy : MemoryCopy_MethodGroup
    class MemoryCopy_MethodGroup:
        def __call__(self, source: clr.Reference[None], destination: clr.Reference[None], destinationSizeInBytes: int, sourceBytesToCopy: int) -> None:...
        # Method MemoryCopy(source : Void*, destination : Void*, destinationSizeInBytes : UInt64, sourceBytesToCopy : UInt64) was skipped since it collides with above method



class Byte(IBinaryInteger_1[int], IUnsignedNumber_1[int], IMinMaxValue_1[int], IConvertible):
    MaxValue : int
    MinValue : int
    def GetHashCode(self) -> int: ...
    def GetTypeCode(self) -> TypeCode: ...
    def TryFormat(self, destination: Span_1[str], charsWritten: clr.Reference[int], format: ReadOnlySpan_1[str] = ..., provider: IFormatProvider = ...) -> bool: ...
    # Skipped CompareTo due to it being static, abstract and generic.

    CompareTo : CompareTo_MethodGroup
    class CompareTo_MethodGroup:
        @typing.overload
        def __call__(self, value: int) -> int:...
        @typing.overload
        def __call__(self, value: typing.Any) -> int:...

    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, obj: int) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...

    # Skipped Parse due to it being static, abstract and generic.

    Parse : Parse_MethodGroup
    class Parse_MethodGroup:
        @typing.overload
        def __call__(self, s: str) -> int:...
        @typing.overload
        def __call__(self, s: str, style: NumberStyles) -> int:...
        @typing.overload
        def __call__(self, s: str, provider: IFormatProvider) -> int:...
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], style: NumberStyles = ..., provider: IFormatProvider = ...) -> int:...
        @typing.overload
        def __call__(self, s: str, style: NumberStyles, provider: IFormatProvider) -> int:...

    # Skipped ToString due to it being static, abstract and generic.

    ToString : ToString_MethodGroup
    class ToString_MethodGroup:
        @typing.overload
        def __call__(self) -> str:...
        @typing.overload
        def __call__(self, format: str) -> str:...
        @typing.overload
        def __call__(self, provider: IFormatProvider) -> str:...
        @typing.overload
        def __call__(self, format: str, provider: IFormatProvider) -> str:...

    # Skipped TryParse due to it being static, abstract and generic.

    TryParse : TryParse_MethodGroup
    class TryParse_MethodGroup:
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], result: clr.Reference[int]) -> bool:...
        @typing.overload
        def __call__(self, s: str, result: clr.Reference[int]) -> bool:...
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], style: NumberStyles, provider: IFormatProvider, result: clr.Reference[int]) -> bool:...
        @typing.overload
        def __call__(self, s: str, style: NumberStyles, provider: IFormatProvider, result: clr.Reference[int]) -> bool:...



class CannotUnloadAppDomainException(SystemException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, innerException: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...


class Char(IBinaryInteger_1[str], IUnsignedNumber_1[str], IMinMaxValue_1[str], IConvertible):
    MaxValue : str
    MinValue : str
    @staticmethod
    def ConvertFromUtf32(utf32: int) -> str: ...
    def GetHashCode(self) -> int: ...
    def GetTypeCode(self) -> TypeCode: ...
    @staticmethod
    def IsAscii(c: str) -> bool: ...
    @staticmethod
    def Parse(s: str) -> str: ...
    @staticmethod
    def ToLowerInvariant(c: str) -> str: ...
    @staticmethod
    def ToUpperInvariant(c: str) -> str: ...
    @staticmethod
    def TryParse(s: str, result: clr.Reference[str]) -> bool: ...
    # Skipped CompareTo due to it being static, abstract and generic.

    CompareTo : CompareTo_MethodGroup
    class CompareTo_MethodGroup:
        @typing.overload
        def __call__(self, value: str) -> int:...
        @typing.overload
        def __call__(self, value: typing.Any) -> int:...

    # Skipped ConvertToUtf32 due to it being static, abstract and generic.

    ConvertToUtf32 : ConvertToUtf32_MethodGroup
    class ConvertToUtf32_MethodGroup:
        @typing.overload
        def __call__(self, highSurrogate: str, lowSurrogate: str) -> int:...
        @typing.overload
        def __call__(self, s: str, index: int) -> int:...

    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, obj: str) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...

    # Skipped GetNumericValue due to it being static, abstract and generic.

    GetNumericValue : GetNumericValue_MethodGroup
    class GetNumericValue_MethodGroup:
        @typing.overload
        def __call__(self, c: str) -> float:...
        @typing.overload
        def __call__(self, s: str, index: int) -> float:...

    # Skipped GetUnicodeCategory due to it being static, abstract and generic.

    GetUnicodeCategory : GetUnicodeCategory_MethodGroup
    class GetUnicodeCategory_MethodGroup:
        @typing.overload
        def __call__(self, c: str) -> UnicodeCategory:...
        @typing.overload
        def __call__(self, s: str, index: int) -> UnicodeCategory:...

    # Skipped IsControl due to it being static, abstract and generic.

    IsControl : IsControl_MethodGroup
    class IsControl_MethodGroup:
        @typing.overload
        def __call__(self, c: str) -> bool:...
        @typing.overload
        def __call__(self, s: str, index: int) -> bool:...

    # Skipped IsDigit due to it being static, abstract and generic.

    IsDigit : IsDigit_MethodGroup
    class IsDigit_MethodGroup:
        @typing.overload
        def __call__(self, c: str) -> bool:...
        @typing.overload
        def __call__(self, s: str, index: int) -> bool:...

    # Skipped IsHighSurrogate due to it being static, abstract and generic.

    IsHighSurrogate : IsHighSurrogate_MethodGroup
    class IsHighSurrogate_MethodGroup:
        @typing.overload
        def __call__(self, c: str) -> bool:...
        @typing.overload
        def __call__(self, s: str, index: int) -> bool:...

    # Skipped IsLetter due to it being static, abstract and generic.

    IsLetter : IsLetter_MethodGroup
    class IsLetter_MethodGroup:
        @typing.overload
        def __call__(self, c: str) -> bool:...
        @typing.overload
        def __call__(self, s: str, index: int) -> bool:...

    # Skipped IsLetterOrDigit due to it being static, abstract and generic.

    IsLetterOrDigit : IsLetterOrDigit_MethodGroup
    class IsLetterOrDigit_MethodGroup:
        @typing.overload
        def __call__(self, c: str) -> bool:...
        @typing.overload
        def __call__(self, s: str, index: int) -> bool:...

    # Skipped IsLower due to it being static, abstract and generic.

    IsLower : IsLower_MethodGroup
    class IsLower_MethodGroup:
        @typing.overload
        def __call__(self, c: str) -> bool:...
        @typing.overload
        def __call__(self, s: str, index: int) -> bool:...

    # Skipped IsLowSurrogate due to it being static, abstract and generic.

    IsLowSurrogate : IsLowSurrogate_MethodGroup
    class IsLowSurrogate_MethodGroup:
        @typing.overload
        def __call__(self, c: str) -> bool:...
        @typing.overload
        def __call__(self, s: str, index: int) -> bool:...

    # Skipped IsNumber due to it being static, abstract and generic.

    IsNumber : IsNumber_MethodGroup
    class IsNumber_MethodGroup:
        @typing.overload
        def __call__(self, c: str) -> bool:...
        @typing.overload
        def __call__(self, s: str, index: int) -> bool:...

    # Skipped IsPunctuation due to it being static, abstract and generic.

    IsPunctuation : IsPunctuation_MethodGroup
    class IsPunctuation_MethodGroup:
        @typing.overload
        def __call__(self, c: str) -> bool:...
        @typing.overload
        def __call__(self, s: str, index: int) -> bool:...

    # Skipped IsSeparator due to it being static, abstract and generic.

    IsSeparator : IsSeparator_MethodGroup
    class IsSeparator_MethodGroup:
        @typing.overload
        def __call__(self, c: str) -> bool:...
        @typing.overload
        def __call__(self, s: str, index: int) -> bool:...

    # Skipped IsSurrogate due to it being static, abstract and generic.

    IsSurrogate : IsSurrogate_MethodGroup
    class IsSurrogate_MethodGroup:
        @typing.overload
        def __call__(self, c: str) -> bool:...
        @typing.overload
        def __call__(self, s: str, index: int) -> bool:...

    # Skipped IsSurrogatePair due to it being static, abstract and generic.

    IsSurrogatePair : IsSurrogatePair_MethodGroup
    class IsSurrogatePair_MethodGroup:
        @typing.overload
        def __call__(self, highSurrogate: str, lowSurrogate: str) -> bool:...
        @typing.overload
        def __call__(self, s: str, index: int) -> bool:...

    # Skipped IsSymbol due to it being static, abstract and generic.

    IsSymbol : IsSymbol_MethodGroup
    class IsSymbol_MethodGroup:
        @typing.overload
        def __call__(self, c: str) -> bool:...
        @typing.overload
        def __call__(self, s: str, index: int) -> bool:...

    # Skipped IsUpper due to it being static, abstract and generic.

    IsUpper : IsUpper_MethodGroup
    class IsUpper_MethodGroup:
        @typing.overload
        def __call__(self, c: str) -> bool:...
        @typing.overload
        def __call__(self, s: str, index: int) -> bool:...

    # Skipped IsWhiteSpace due to it being static, abstract and generic.

    IsWhiteSpace : IsWhiteSpace_MethodGroup
    class IsWhiteSpace_MethodGroup:
        @typing.overload
        def __call__(self, c: str) -> bool:...
        @typing.overload
        def __call__(self, s: str, index: int) -> bool:...

    # Skipped ToLower due to it being static, abstract and generic.

    ToLower : ToLower_MethodGroup
    class ToLower_MethodGroup:
        @typing.overload
        def __call__(self, c: str) -> str:...
        @typing.overload
        def __call__(self, c: str, culture: CultureInfo) -> str:...

    # Skipped ToString due to it being static, abstract and generic.

    ToString : ToString_MethodGroup
    class ToString_MethodGroup:
        @typing.overload
        def __call__(self) -> str:...
        @typing.overload
        def __call__(self, c: str) -> str:...
        @typing.overload
        def __call__(self, provider: IFormatProvider) -> str:...

    # Skipped ToUpper due to it being static, abstract and generic.

    ToUpper : ToUpper_MethodGroup
    class ToUpper_MethodGroup:
        @typing.overload
        def __call__(self, c: str) -> str:...
        @typing.overload
        def __call__(self, c: str, culture: CultureInfo) -> str:...



class CharEnumerator(IEnumerator_1[str], ICloneable):
    @property
    def Current(self) -> str: ...
    def Clone(self) -> typing.Any: ...
    def Dispose(self) -> None: ...
    def MoveNext(self) -> bool: ...
    def Reset(self) -> None: ...


class CLSCompliantAttribute(Attribute):
    def __init__(self, isCompliant: bool) -> None: ...
    @property
    def IsCompliant(self) -> bool: ...
    @property
    def TypeId(self) -> typing.Any: ...


class Comparison_GenericClasses(abc.ABCMeta):
    Generic_Comparison_GenericClasses_Comparison_1_T = typing.TypeVar('Generic_Comparison_GenericClasses_Comparison_1_T')
    def __getitem__(self, types : typing.Type[Generic_Comparison_GenericClasses_Comparison_1_T]) -> typing.Type[Comparison_1[Generic_Comparison_GenericClasses_Comparison_1_T]]: ...

Comparison : Comparison_GenericClasses

Comparison_1_T = typing.TypeVar('Comparison_1_T', contravariant=True)
class Comparison_1(typing.Generic[Comparison_1_T], MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, x: Comparison_1_T, y: Comparison_1_T, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> int: ...
    def Invoke(self, x: Comparison_1_T, y: Comparison_1_T) -> int: ...


class Console(abc.ABC):
    @classmethod
    @property
    def BackgroundColor(cls) -> ConsoleColor: ...
    @classmethod
    @BackgroundColor.setter
    def BackgroundColor(cls, value: ConsoleColor) -> ConsoleColor: ...
    @classmethod
    @property
    def BufferHeight(cls) -> int: ...
    @classmethod
    @BufferHeight.setter
    def BufferHeight(cls, value: int) -> int: ...
    @classmethod
    @property
    def BufferWidth(cls) -> int: ...
    @classmethod
    @BufferWidth.setter
    def BufferWidth(cls, value: int) -> int: ...
    @classmethod
    @property
    def CapsLock(cls) -> bool: ...
    @classmethod
    @property
    def CursorLeft(cls) -> int: ...
    @classmethod
    @CursorLeft.setter
    def CursorLeft(cls, value: int) -> int: ...
    @classmethod
    @property
    def CursorSize(cls) -> int: ...
    @classmethod
    @CursorSize.setter
    def CursorSize(cls, value: int) -> int: ...
    @classmethod
    @property
    def CursorTop(cls) -> int: ...
    @classmethod
    @CursorTop.setter
    def CursorTop(cls, value: int) -> int: ...
    @classmethod
    @property
    def CursorVisible(cls) -> bool: ...
    @classmethod
    @CursorVisible.setter
    def CursorVisible(cls, value: bool) -> bool: ...
    @classmethod
    @property
    def Error(cls) -> TextWriter: ...
    @classmethod
    @property
    def ForegroundColor(cls) -> ConsoleColor: ...
    @classmethod
    @ForegroundColor.setter
    def ForegroundColor(cls, value: ConsoleColor) -> ConsoleColor: ...
    @classmethod
    @property
    def In(cls) -> TextReader: ...
    @classmethod
    @property
    def InputEncoding(cls) -> Encoding: ...
    @classmethod
    @InputEncoding.setter
    def InputEncoding(cls, value: Encoding) -> Encoding: ...
    @classmethod
    @property
    def IsErrorRedirected(cls) -> bool: ...
    @classmethod
    @property
    def IsInputRedirected(cls) -> bool: ...
    @classmethod
    @property
    def IsOutputRedirected(cls) -> bool: ...
    @classmethod
    @property
    def KeyAvailable(cls) -> bool: ...
    @classmethod
    @property
    def LargestWindowHeight(cls) -> int: ...
    @classmethod
    @property
    def LargestWindowWidth(cls) -> int: ...
    @classmethod
    @property
    def NumberLock(cls) -> bool: ...
    @classmethod
    @property
    def Out(cls) -> TextWriter: ...
    @classmethod
    @property
    def OutputEncoding(cls) -> Encoding: ...
    @classmethod
    @OutputEncoding.setter
    def OutputEncoding(cls, value: Encoding) -> Encoding: ...
    @classmethod
    @property
    def Title(cls) -> str: ...
    @classmethod
    @Title.setter
    def Title(cls, value: str) -> str: ...
    @classmethod
    @property
    def TreatControlCAsInput(cls) -> bool: ...
    @classmethod
    @TreatControlCAsInput.setter
    def TreatControlCAsInput(cls, value: bool) -> bool: ...
    @classmethod
    @property
    def WindowHeight(cls) -> int: ...
    @classmethod
    @WindowHeight.setter
    def WindowHeight(cls, value: int) -> int: ...
    @classmethod
    @property
    def WindowLeft(cls) -> int: ...
    @classmethod
    @WindowLeft.setter
    def WindowLeft(cls, value: int) -> int: ...
    @classmethod
    @property
    def WindowTop(cls) -> int: ...
    @classmethod
    @WindowTop.setter
    def WindowTop(cls, value: int) -> int: ...
    @classmethod
    @property
    def WindowWidth(cls) -> int: ...
    @classmethod
    @WindowWidth.setter
    def WindowWidth(cls, value: int) -> int: ...
    @staticmethod
    def Clear() -> None: ...
    @staticmethod
    def GetCursorPosition() -> ValueTuple_2[int, int]: ...
    @staticmethod
    def Read() -> int: ...
    @staticmethod
    def ReadLine() -> str: ...
    @staticmethod
    def ResetColor() -> None: ...
    @staticmethod
    def SetBufferSize(width: int, height: int) -> None: ...
    @staticmethod
    def SetCursorPosition(left: int, top: int) -> None: ...
    @staticmethod
    def SetError(newError: TextWriter) -> None: ...
    @staticmethod
    def SetIn(newIn: TextReader) -> None: ...
    @staticmethod
    def SetOut(newOut: TextWriter) -> None: ...
    @staticmethod
    def SetWindowPosition(left: int, top: int) -> None: ...
    @staticmethod
    def SetWindowSize(width: int, height: int) -> None: ...
    # Skipped Beep due to it being static, abstract and generic.

    Beep : Beep_MethodGroup
    class Beep_MethodGroup:
        @typing.overload
        def __call__(self) -> None:...
        @typing.overload
        def __call__(self, frequency: int, duration: int) -> None:...

    # Skipped MoveBufferArea due to it being static, abstract and generic.

    MoveBufferArea : MoveBufferArea_MethodGroup
    class MoveBufferArea_MethodGroup:
        @typing.overload
        def __call__(self, sourceLeft: int, sourceTop: int, sourceWidth: int, sourceHeight: int, targetLeft: int, targetTop: int) -> None:...
        @typing.overload
        def __call__(self, sourceLeft: int, sourceTop: int, sourceWidth: int, sourceHeight: int, targetLeft: int, targetTop: int, sourceChar: str, sourceForeColor: ConsoleColor, sourceBackColor: ConsoleColor) -> None:...

    # Skipped OpenStandardError due to it being static, abstract and generic.

    OpenStandardError : OpenStandardError_MethodGroup
    class OpenStandardError_MethodGroup:
        @typing.overload
        def __call__(self) -> Stream:...
        @typing.overload
        def __call__(self, bufferSize: int) -> Stream:...

    # Skipped OpenStandardInput due to it being static, abstract and generic.

    OpenStandardInput : OpenStandardInput_MethodGroup
    class OpenStandardInput_MethodGroup:
        @typing.overload
        def __call__(self) -> Stream:...
        @typing.overload
        def __call__(self, bufferSize: int) -> Stream:...

    # Skipped OpenStandardOutput due to it being static, abstract and generic.

    OpenStandardOutput : OpenStandardOutput_MethodGroup
    class OpenStandardOutput_MethodGroup:
        @typing.overload
        def __call__(self) -> Stream:...
        @typing.overload
        def __call__(self, bufferSize: int) -> Stream:...

    # Skipped ReadKey due to it being static, abstract and generic.

    ReadKey : ReadKey_MethodGroup
    class ReadKey_MethodGroup:
        @typing.overload
        def __call__(self) -> ConsoleKeyInfo:...
        @typing.overload
        def __call__(self, intercept: bool) -> ConsoleKeyInfo:...

    # Skipped Write due to it being static, abstract and generic.

    Write : Write_MethodGroup
    class Write_MethodGroup:
        @typing.overload
        def __call__(self, value: float) -> None:...
        # Method Write(value : Single) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: str) -> None:...
        # Method Write(value : Int32) was skipped since it collides with above method
        # Method Write(value : UInt32) was skipped since it collides with above method
        # Method Write(value : Int64) was skipped since it collides with above method
        # Method Write(value : UInt64) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Decimal) -> None:...
        @typing.overload
        def __call__(self, buffer: Array_1[str]) -> None:...
        # Method Write(value : Boolean) was skipped since it collides with above method
        # Method Write(value : String) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: typing.Any) -> None:...
        @typing.overload
        def __call__(self, format: str, arg: Array_1[typing.Any]) -> None:...
        @typing.overload
        def __call__(self, format: str, arg0: typing.Any) -> None:...
        @typing.overload
        def __call__(self, buffer: Array_1[str], index: int, count: int) -> None:...
        @typing.overload
        def __call__(self, format: str, arg0: typing.Any, arg1: typing.Any) -> None:...
        @typing.overload
        def __call__(self, format: str, arg0: typing.Any, arg1: typing.Any, arg2: typing.Any) -> None:...

    # Skipped WriteLine due to it being static, abstract and generic.

    WriteLine : WriteLine_MethodGroup
    class WriteLine_MethodGroup:
        @typing.overload
        def __call__(self) -> None:...
        @typing.overload
        def __call__(self, value: float) -> None:...
        # Method WriteLine(value : Single) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: str) -> None:...
        # Method WriteLine(value : Int32) was skipped since it collides with above method
        # Method WriteLine(value : UInt32) was skipped since it collides with above method
        # Method WriteLine(value : Int64) was skipped since it collides with above method
        # Method WriteLine(value : UInt64) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Decimal) -> None:...
        @typing.overload
        def __call__(self, buffer: Array_1[str]) -> None:...
        # Method WriteLine(value : Boolean) was skipped since it collides with above method
        # Method WriteLine(value : String) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: typing.Any) -> None:...
        @typing.overload
        def __call__(self, format: str, arg: Array_1[typing.Any]) -> None:...
        @typing.overload
        def __call__(self, format: str, arg0: typing.Any) -> None:...
        @typing.overload
        def __call__(self, buffer: Array_1[str], index: int, count: int) -> None:...
        @typing.overload
        def __call__(self, format: str, arg0: typing.Any, arg1: typing.Any) -> None:...
        @typing.overload
        def __call__(self, format: str, arg0: typing.Any, arg1: typing.Any, arg2: typing.Any) -> None:...



class ConsoleCancelEventArgs(EventArgs):
    @property
    def Cancel(self) -> bool: ...
    @Cancel.setter
    def Cancel(self, value: bool) -> bool: ...
    @property
    def SpecialKey(self) -> ConsoleSpecialKey: ...


class ConsoleCancelEventHandler(MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, sender: typing.Any, e: ConsoleCancelEventArgs, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: typing.Any, e: ConsoleCancelEventArgs) -> None: ...


class ConsoleColor(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Black : ConsoleColor # 0
    DarkBlue : ConsoleColor # 1
    DarkGreen : ConsoleColor # 2
    DarkCyan : ConsoleColor # 3
    DarkRed : ConsoleColor # 4
    DarkMagenta : ConsoleColor # 5
    DarkYellow : ConsoleColor # 6
    Gray : ConsoleColor # 7
    DarkGray : ConsoleColor # 8
    Blue : ConsoleColor # 9
    Green : ConsoleColor # 10
    Cyan : ConsoleColor # 11
    Red : ConsoleColor # 12
    Magenta : ConsoleColor # 13
    Yellow : ConsoleColor # 14
    White : ConsoleColor # 15


class ConsoleKey(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Backspace : ConsoleKey # 8
    Tab : ConsoleKey # 9
    Clear : ConsoleKey # 12
    Enter : ConsoleKey # 13
    Pause : ConsoleKey # 19
    Escape : ConsoleKey # 27
    Spacebar : ConsoleKey # 32
    PageUp : ConsoleKey # 33
    PageDown : ConsoleKey # 34
    End : ConsoleKey # 35
    Home : ConsoleKey # 36
    LeftArrow : ConsoleKey # 37
    UpArrow : ConsoleKey # 38
    RightArrow : ConsoleKey # 39
    DownArrow : ConsoleKey # 40
    Select : ConsoleKey # 41
    Print : ConsoleKey # 42
    Execute : ConsoleKey # 43
    PrintScreen : ConsoleKey # 44
    Insert : ConsoleKey # 45
    Delete : ConsoleKey # 46
    Help : ConsoleKey # 47
    D0 : ConsoleKey # 48
    D1 : ConsoleKey # 49
    D2 : ConsoleKey # 50
    D3 : ConsoleKey # 51
    D4 : ConsoleKey # 52
    D5 : ConsoleKey # 53
    D6 : ConsoleKey # 54
    D7 : ConsoleKey # 55
    D8 : ConsoleKey # 56
    D9 : ConsoleKey # 57
    A : ConsoleKey # 65
    B : ConsoleKey # 66
    C : ConsoleKey # 67
    D : ConsoleKey # 68
    E : ConsoleKey # 69
    F : ConsoleKey # 70
    G : ConsoleKey # 71
    H : ConsoleKey # 72
    I : ConsoleKey # 73
    J : ConsoleKey # 74
    K : ConsoleKey # 75
    L : ConsoleKey # 76
    M : ConsoleKey # 77
    N : ConsoleKey # 78
    O : ConsoleKey # 79
    P : ConsoleKey # 80
    Q : ConsoleKey # 81
    R : ConsoleKey # 82
    S : ConsoleKey # 83
    T : ConsoleKey # 84
    U : ConsoleKey # 85
    V : ConsoleKey # 86
    W : ConsoleKey # 87
    X : ConsoleKey # 88
    Y : ConsoleKey # 89
    Z : ConsoleKey # 90
    LeftWindows : ConsoleKey # 91
    RightWindows : ConsoleKey # 92
    Applications : ConsoleKey # 93
    Sleep : ConsoleKey # 95
    NumPad0 : ConsoleKey # 96
    NumPad1 : ConsoleKey # 97
    NumPad2 : ConsoleKey # 98
    NumPad3 : ConsoleKey # 99
    NumPad4 : ConsoleKey # 100
    NumPad5 : ConsoleKey # 101
    NumPad6 : ConsoleKey # 102
    NumPad7 : ConsoleKey # 103
    NumPad8 : ConsoleKey # 104
    NumPad9 : ConsoleKey # 105
    Multiply : ConsoleKey # 106
    Add : ConsoleKey # 107
    Separator : ConsoleKey # 108
    Subtract : ConsoleKey # 109
    Decimal : ConsoleKey # 110
    Divide : ConsoleKey # 111
    F1 : ConsoleKey # 112
    F2 : ConsoleKey # 113
    F3 : ConsoleKey # 114
    F4 : ConsoleKey # 115
    F5 : ConsoleKey # 116
    F6 : ConsoleKey # 117
    F7 : ConsoleKey # 118
    F8 : ConsoleKey # 119
    F9 : ConsoleKey # 120
    F10 : ConsoleKey # 121
    F11 : ConsoleKey # 122
    F12 : ConsoleKey # 123
    F13 : ConsoleKey # 124
    F14 : ConsoleKey # 125
    F15 : ConsoleKey # 126
    F16 : ConsoleKey # 127
    F17 : ConsoleKey # 128
    F18 : ConsoleKey # 129
    F19 : ConsoleKey # 130
    F20 : ConsoleKey # 131
    F21 : ConsoleKey # 132
    F22 : ConsoleKey # 133
    F23 : ConsoleKey # 134
    F24 : ConsoleKey # 135
    BrowserBack : ConsoleKey # 166
    BrowserForward : ConsoleKey # 167
    BrowserRefresh : ConsoleKey # 168
    BrowserStop : ConsoleKey # 169
    BrowserSearch : ConsoleKey # 170
    BrowserFavorites : ConsoleKey # 171
    BrowserHome : ConsoleKey # 172
    VolumeMute : ConsoleKey # 173
    VolumeDown : ConsoleKey # 174
    VolumeUp : ConsoleKey # 175
    MediaNext : ConsoleKey # 176
    MediaPrevious : ConsoleKey # 177
    MediaStop : ConsoleKey # 178
    MediaPlay : ConsoleKey # 179
    LaunchMail : ConsoleKey # 180
    LaunchMediaSelect : ConsoleKey # 181
    LaunchApp1 : ConsoleKey # 182
    LaunchApp2 : ConsoleKey # 183
    Oem1 : ConsoleKey # 186
    OemPlus : ConsoleKey # 187
    OemComma : ConsoleKey # 188
    OemMinus : ConsoleKey # 189
    OemPeriod : ConsoleKey # 190
    Oem2 : ConsoleKey # 191
    Oem3 : ConsoleKey # 192
    Oem4 : ConsoleKey # 219
    Oem5 : ConsoleKey # 220
    Oem6 : ConsoleKey # 221
    Oem7 : ConsoleKey # 222
    Oem8 : ConsoleKey # 223
    Oem102 : ConsoleKey # 226
    Process : ConsoleKey # 229
    Packet : ConsoleKey # 231
    Attention : ConsoleKey # 246
    CrSel : ConsoleKey # 247
    ExSel : ConsoleKey # 248
    EraseEndOfFile : ConsoleKey # 249
    Play : ConsoleKey # 250
    Zoom : ConsoleKey # 251
    NoName : ConsoleKey # 252
    Pa1 : ConsoleKey # 253
    OemClear : ConsoleKey # 254


class ConsoleKeyInfo(IEquatable_1[ConsoleKeyInfo]):
    def __init__(self, keyChar: str, key: ConsoleKey, shift: bool, alt: bool, control: bool) -> None: ...
    @property
    def Key(self) -> ConsoleKey: ...
    @property
    def KeyChar(self) -> str: ...
    @property
    def Modifiers(self) -> ConsoleModifiers: ...
    def GetHashCode(self) -> int: ...
    def __eq__(self, a: ConsoleKeyInfo, b: ConsoleKeyInfo) -> bool: ...
    def __ne__(self, a: ConsoleKeyInfo, b: ConsoleKeyInfo) -> bool: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, obj: ConsoleKeyInfo) -> bool:...
        @typing.overload
        def __call__(self, value: typing.Any) -> bool:...



class ConsoleModifiers(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Alt : ConsoleModifiers # 1
    Shift : ConsoleModifiers # 2
    Control : ConsoleModifiers # 4


class ConsoleSpecialKey(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    ControlC : ConsoleSpecialKey # 0
    ControlBreak : ConsoleSpecialKey # 1


class ContextBoundObject(MarshalByRefObject):
    pass


class ContextMarshalException(SystemException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, inner: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...


class ContextStaticAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class Convert(abc.ABC):
    DBNull : typing.Any
    @staticmethod
    def FromBase64CharArray(inArray: Array_1[str], offset: int, length: int) -> Array_1[int]: ...
    @staticmethod
    def FromBase64String(s: str) -> Array_1[int]: ...
    @staticmethod
    def GetTypeCode(value: typing.Any) -> TypeCode: ...
    @staticmethod
    def IsDBNull(value: typing.Any) -> bool: ...
    @staticmethod
    def TryFromBase64Chars(chars: ReadOnlySpan_1[str], bytes: Span_1[int], bytesWritten: clr.Reference[int]) -> bool: ...
    @staticmethod
    def TryFromBase64String(s: str, bytes: Span_1[int], bytesWritten: clr.Reference[int]) -> bool: ...
    @staticmethod
    def TryToBase64Chars(bytes: ReadOnlySpan_1[int], chars: Span_1[str], charsWritten: clr.Reference[int], options: Base64FormattingOptions = ...) -> bool: ...
    # Skipped ChangeType due to it being static, abstract and generic.

    ChangeType : ChangeType_MethodGroup
    class ChangeType_MethodGroup:
        @typing.overload
        def __call__(self, value: typing.Any, typeCode: TypeCode) -> typing.Any:...
        @typing.overload
        def __call__(self, value: typing.Any, conversionType: typing.Type[typing.Any]) -> typing.Any:...
        @typing.overload
        def __call__(self, value: typing.Any, typeCode: TypeCode, provider: IFormatProvider) -> typing.Any:...
        @typing.overload
        def __call__(self, value: typing.Any, conversionType: typing.Type[typing.Any], provider: IFormatProvider) -> typing.Any:...

    # Skipped FromHexString due to it being static, abstract and generic.

    FromHexString : FromHexString_MethodGroup
    class FromHexString_MethodGroup:
        @typing.overload
        def __call__(self, chars: ReadOnlySpan_1[str]) -> Array_1[int]:...
        @typing.overload
        def __call__(self, s: str) -> Array_1[int]:...

    # Skipped ToBase64CharArray due to it being static, abstract and generic.

    ToBase64CharArray : ToBase64CharArray_MethodGroup
    class ToBase64CharArray_MethodGroup:
        @typing.overload
        def __call__(self, inArray: Array_1[int], offsetIn: int, length: int, outArray: Array_1[str], offsetOut: int) -> int:...
        @typing.overload
        def __call__(self, inArray: Array_1[int], offsetIn: int, length: int, outArray: Array_1[str], offsetOut: int, options: Base64FormattingOptions) -> int:...

    # Skipped ToBase64String due to it being static, abstract and generic.

    ToBase64String : ToBase64String_MethodGroup
    class ToBase64String_MethodGroup:
        @typing.overload
        def __call__(self, inArray: Array_1[int]) -> str:...
        @typing.overload
        def __call__(self, inArray: Array_1[int], options: Base64FormattingOptions) -> str:...
        @typing.overload
        def __call__(self, bytes: ReadOnlySpan_1[int], options: Base64FormattingOptions = ...) -> str:...
        @typing.overload
        def __call__(self, inArray: Array_1[int], offset: int, length: int) -> str:...
        @typing.overload
        def __call__(self, inArray: Array_1[int], offset: int, length: int, options: Base64FormattingOptions) -> str:...

    # Skipped ToBoolean due to it being static, abstract and generic.

    ToBoolean : ToBoolean_MethodGroup
    class ToBoolean_MethodGroup:
        @typing.overload
        def __call__(self, value: float) -> bool:...
        # Method ToBoolean(value : Double) was skipped since it collides with above method
        # Method ToBoolean(value : SByte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: str) -> bool:...
        # Method ToBoolean(value : Byte) was skipped since it collides with above method
        # Method ToBoolean(value : Int16) was skipped since it collides with above method
        # Method ToBoolean(value : UInt16) was skipped since it collides with above method
        # Method ToBoolean(value : Int32) was skipped since it collides with above method
        # Method ToBoolean(value : UInt32) was skipped since it collides with above method
        # Method ToBoolean(value : Int64) was skipped since it collides with above method
        # Method ToBoolean(value : UInt64) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Decimal) -> bool:...
        @typing.overload
        def __call__(self, value: DateTime) -> bool:...
        # Method ToBoolean(value : Boolean) was skipped since it collides with above method
        # Method ToBoolean(value : String) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: typing.Any) -> bool:...
        @typing.overload
        def __call__(self, value: str, provider: IFormatProvider) -> bool:...
        @typing.overload
        def __call__(self, value: typing.Any, provider: IFormatProvider) -> bool:...

    # Skipped ToByte due to it being static, abstract and generic.

    ToByte : ToByte_MethodGroup
    class ToByte_MethodGroup:
        @typing.overload
        def __call__(self, value: float) -> int:...
        # Method ToByte(value : Double) was skipped since it collides with above method
        # Method ToByte(value : UInt64) was skipped since it collides with above method
        # Method ToByte(value : Byte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: str) -> int:...
        # Method ToByte(value : SByte) was skipped since it collides with above method
        # Method ToByte(value : Int16) was skipped since it collides with above method
        # Method ToByte(value : UInt16) was skipped since it collides with above method
        # Method ToByte(value : Int32) was skipped since it collides with above method
        # Method ToByte(value : UInt32) was skipped since it collides with above method
        # Method ToByte(value : Int64) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Decimal) -> int:...
        @typing.overload
        def __call__(self, value: DateTime) -> int:...
        # Method ToByte(value : String) was skipped since it collides with above method
        # Method ToByte(value : Boolean) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: typing.Any) -> int:...
        @typing.overload
        def __call__(self, value: str, fromBase: int) -> int:...
        @typing.overload
        def __call__(self, value: str, provider: IFormatProvider) -> int:...
        @typing.overload
        def __call__(self, value: typing.Any, provider: IFormatProvider) -> int:...

    # Skipped ToChar due to it being static, abstract and generic.

    ToChar : ToChar_MethodGroup
    class ToChar_MethodGroup:
        @typing.overload
        def __call__(self, value: float) -> str:...
        # Method ToChar(value : Double) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: str) -> str:...
        # Method ToChar(value : SByte) was skipped since it collides with above method
        # Method ToChar(value : Byte) was skipped since it collides with above method
        # Method ToChar(value : Int16) was skipped since it collides with above method
        # Method ToChar(value : UInt16) was skipped since it collides with above method
        # Method ToChar(value : Int32) was skipped since it collides with above method
        # Method ToChar(value : UInt32) was skipped since it collides with above method
        # Method ToChar(value : Int64) was skipped since it collides with above method
        # Method ToChar(value : UInt64) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Decimal) -> str:...
        @typing.overload
        def __call__(self, value: DateTime) -> str:...
        # Method ToChar(value : Boolean) was skipped since it collides with above method
        # Method ToChar(value : String) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: typing.Any) -> str:...
        @typing.overload
        def __call__(self, value: str, provider: IFormatProvider) -> str:...
        @typing.overload
        def __call__(self, value: typing.Any, provider: IFormatProvider) -> str:...

    # Skipped ToDateTime due to it being static, abstract and generic.

    ToDateTime : ToDateTime_MethodGroup
    class ToDateTime_MethodGroup:
        @typing.overload
        def __call__(self, value: float) -> DateTime:...
        # Method ToDateTime(value : Double) was skipped since it collides with above method
        # Method ToDateTime(value : SByte) was skipped since it collides with above method
        # Method ToDateTime(value : Byte) was skipped since it collides with above method
        # Method ToDateTime(value : Int16) was skipped since it collides with above method
        # Method ToDateTime(value : UInt16) was skipped since it collides with above method
        # Method ToDateTime(value : Int32) was skipped since it collides with above method
        # Method ToDateTime(value : UInt32) was skipped since it collides with above method
        # Method ToDateTime(value : Int64) was skipped since it collides with above method
        # Method ToDateTime(value : UInt64) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Decimal) -> DateTime:...
        @typing.overload
        def __call__(self, value: str) -> DateTime:...
        # Method ToDateTime(value : Char) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: DateTime) -> DateTime:...
        # Method ToDateTime(value : Boolean) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: typing.Any) -> DateTime:...
        @typing.overload
        def __call__(self, value: str, provider: IFormatProvider) -> DateTime:...
        @typing.overload
        def __call__(self, value: typing.Any, provider: IFormatProvider) -> DateTime:...

    # Skipped ToDecimal due to it being static, abstract and generic.

    ToDecimal : ToDecimal_MethodGroup
    class ToDecimal_MethodGroup:
        @typing.overload
        def __call__(self, value: float) -> Decimal:...
        # Method ToDecimal(value : Double) was skipped since it collides with above method
        # Method ToDecimal(value : SByte) was skipped since it collides with above method
        # Method ToDecimal(value : Byte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: str) -> Decimal:...
        # Method ToDecimal(value : Int16) was skipped since it collides with above method
        # Method ToDecimal(value : UInt16) was skipped since it collides with above method
        # Method ToDecimal(value : Int32) was skipped since it collides with above method
        # Method ToDecimal(value : UInt32) was skipped since it collides with above method
        # Method ToDecimal(value : Int64) was skipped since it collides with above method
        # Method ToDecimal(value : UInt64) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Decimal) -> Decimal:...
        @typing.overload
        def __call__(self, value: DateTime) -> Decimal:...
        # Method ToDecimal(value : String) was skipped since it collides with above method
        # Method ToDecimal(value : Boolean) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: typing.Any) -> Decimal:...
        @typing.overload
        def __call__(self, value: str, provider: IFormatProvider) -> Decimal:...
        @typing.overload
        def __call__(self, value: typing.Any, provider: IFormatProvider) -> Decimal:...

    # Skipped ToDouble due to it being static, abstract and generic.

    ToDouble : ToDouble_MethodGroup
    class ToDouble_MethodGroup:
        @typing.overload
        def __call__(self, value: float) -> float:...
        # Method ToDouble(value : Double) was skipped since it collides with above method
        # Method ToDouble(value : SByte) was skipped since it collides with above method
        # Method ToDouble(value : Byte) was skipped since it collides with above method
        # Method ToDouble(value : Int16) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: str) -> float:...
        # Method ToDouble(value : UInt16) was skipped since it collides with above method
        # Method ToDouble(value : Int32) was skipped since it collides with above method
        # Method ToDouble(value : UInt32) was skipped since it collides with above method
        # Method ToDouble(value : Int64) was skipped since it collides with above method
        # Method ToDouble(value : UInt64) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Decimal) -> float:...
        @typing.overload
        def __call__(self, value: DateTime) -> float:...
        # Method ToDouble(value : String) was skipped since it collides with above method
        # Method ToDouble(value : Boolean) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: typing.Any) -> float:...
        @typing.overload
        def __call__(self, value: str, provider: IFormatProvider) -> float:...
        @typing.overload
        def __call__(self, value: typing.Any, provider: IFormatProvider) -> float:...

    # Skipped ToHexString due to it being static, abstract and generic.

    ToHexString : ToHexString_MethodGroup
    class ToHexString_MethodGroup:
        @typing.overload
        def __call__(self, inArray: Array_1[int]) -> str:...
        @typing.overload
        def __call__(self, bytes: ReadOnlySpan_1[int]) -> str:...
        @typing.overload
        def __call__(self, inArray: Array_1[int], offset: int, length: int) -> str:...

    # Skipped ToInt16 due to it being static, abstract and generic.

    ToInt16 : ToInt16_MethodGroup
    class ToInt16_MethodGroup:
        @typing.overload
        def __call__(self, value: float) -> int:...
        # Method ToInt16(value : Double) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: str) -> int:...
        # Method ToInt16(value : SByte) was skipped since it collides with above method
        # Method ToInt16(value : Byte) was skipped since it collides with above method
        # Method ToInt16(value : UInt16) was skipped since it collides with above method
        # Method ToInt16(value : Int32) was skipped since it collides with above method
        # Method ToInt16(value : UInt32) was skipped since it collides with above method
        # Method ToInt16(value : Int16) was skipped since it collides with above method
        # Method ToInt16(value : Int64) was skipped since it collides with above method
        # Method ToInt16(value : UInt64) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Decimal) -> int:...
        @typing.overload
        def __call__(self, value: DateTime) -> int:...
        # Method ToInt16(value : Boolean) was skipped since it collides with above method
        # Method ToInt16(value : String) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: typing.Any) -> int:...
        @typing.overload
        def __call__(self, value: str, fromBase: int) -> int:...
        @typing.overload
        def __call__(self, value: str, provider: IFormatProvider) -> int:...
        @typing.overload
        def __call__(self, value: typing.Any, provider: IFormatProvider) -> int:...

    # Skipped ToInt32 due to it being static, abstract and generic.

    ToInt32 : ToInt32_MethodGroup
    class ToInt32_MethodGroup:
        @typing.overload
        def __call__(self, value: float) -> int:...
        # Method ToInt32(value : Double) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: str) -> int:...
        # Method ToInt32(value : SByte) was skipped since it collides with above method
        # Method ToInt32(value : Byte) was skipped since it collides with above method
        # Method ToInt32(value : Int16) was skipped since it collides with above method
        # Method ToInt32(value : UInt16) was skipped since it collides with above method
        # Method ToInt32(value : UInt32) was skipped since it collides with above method
        # Method ToInt32(value : Int32) was skipped since it collides with above method
        # Method ToInt32(value : Int64) was skipped since it collides with above method
        # Method ToInt32(value : UInt64) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Decimal) -> int:...
        @typing.overload
        def __call__(self, value: DateTime) -> int:...
        # Method ToInt32(value : Boolean) was skipped since it collides with above method
        # Method ToInt32(value : String) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: typing.Any) -> int:...
        @typing.overload
        def __call__(self, value: str, fromBase: int) -> int:...
        @typing.overload
        def __call__(self, value: str, provider: IFormatProvider) -> int:...
        @typing.overload
        def __call__(self, value: typing.Any, provider: IFormatProvider) -> int:...

    # Skipped ToInt64 due to it being static, abstract and generic.

    ToInt64 : ToInt64_MethodGroup
    class ToInt64_MethodGroup:
        @typing.overload
        def __call__(self, value: float) -> int:...
        # Method ToInt64(value : Double) was skipped since it collides with above method
        # Method ToInt64(value : Int16) was skipped since it collides with above method
        # Method ToInt64(value : UInt16) was skipped since it collides with above method
        # Method ToInt64(value : Int32) was skipped since it collides with above method
        # Method ToInt64(value : UInt32) was skipped since it collides with above method
        # Method ToInt64(value : UInt64) was skipped since it collides with above method
        # Method ToInt64(value : Int64) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: str) -> int:...
        # Method ToInt64(value : SByte) was skipped since it collides with above method
        # Method ToInt64(value : Byte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Decimal) -> int:...
        @typing.overload
        def __call__(self, value: DateTime) -> int:...
        # Method ToInt64(value : String) was skipped since it collides with above method
        # Method ToInt64(value : Boolean) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: typing.Any) -> int:...
        @typing.overload
        def __call__(self, value: str, fromBase: int) -> int:...
        @typing.overload
        def __call__(self, value: str, provider: IFormatProvider) -> int:...
        @typing.overload
        def __call__(self, value: typing.Any, provider: IFormatProvider) -> int:...

    # Skipped ToSByte due to it being static, abstract and generic.

    ToSByte : ToSByte_MethodGroup
    class ToSByte_MethodGroup:
        @typing.overload
        def __call__(self, value: float) -> int:...
        # Method ToSByte(value : Double) was skipped since it collides with above method
        # Method ToSByte(value : SByte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: str) -> int:...
        # Method ToSByte(value : Byte) was skipped since it collides with above method
        # Method ToSByte(value : Int16) was skipped since it collides with above method
        # Method ToSByte(value : UInt16) was skipped since it collides with above method
        # Method ToSByte(value : Int32) was skipped since it collides with above method
        # Method ToSByte(value : UInt32) was skipped since it collides with above method
        # Method ToSByte(value : Int64) was skipped since it collides with above method
        # Method ToSByte(value : UInt64) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Decimal) -> int:...
        @typing.overload
        def __call__(self, value: DateTime) -> int:...
        # Method ToSByte(value : Boolean) was skipped since it collides with above method
        # Method ToSByte(value : String) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: typing.Any) -> int:...
        @typing.overload
        def __call__(self, value: str, fromBase: int) -> int:...
        @typing.overload
        def __call__(self, value: str, provider: IFormatProvider) -> int:...
        @typing.overload
        def __call__(self, value: typing.Any, provider: IFormatProvider) -> int:...

    # Skipped ToSingle due to it being static, abstract and generic.

    ToSingle : ToSingle_MethodGroup
    class ToSingle_MethodGroup:
        @typing.overload
        def __call__(self, value: float) -> float:...
        # Method ToSingle(value : Double) was skipped since it collides with above method
        # Method ToSingle(value : SByte) was skipped since it collides with above method
        # Method ToSingle(value : Byte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: str) -> float:...
        # Method ToSingle(value : Int16) was skipped since it collides with above method
        # Method ToSingle(value : UInt16) was skipped since it collides with above method
        # Method ToSingle(value : Int32) was skipped since it collides with above method
        # Method ToSingle(value : UInt32) was skipped since it collides with above method
        # Method ToSingle(value : Int64) was skipped since it collides with above method
        # Method ToSingle(value : UInt64) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Decimal) -> float:...
        @typing.overload
        def __call__(self, value: DateTime) -> float:...
        # Method ToSingle(value : String) was skipped since it collides with above method
        # Method ToSingle(value : Boolean) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: typing.Any) -> float:...
        @typing.overload
        def __call__(self, value: str, provider: IFormatProvider) -> float:...
        @typing.overload
        def __call__(self, value: typing.Any, provider: IFormatProvider) -> float:...

    # Skipped ToString due to it being static, abstract and generic.

    ToString : ToString_MethodGroup
    class ToString_MethodGroup:
        @typing.overload
        def __call__(self, value: float) -> str:...
        # Method ToString(value : Double) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: str) -> str:...
        # Method ToString(value : SByte) was skipped since it collides with above method
        # Method ToString(value : Byte) was skipped since it collides with above method
        # Method ToString(value : Int16) was skipped since it collides with above method
        # Method ToString(value : UInt16) was skipped since it collides with above method
        # Method ToString(value : Int32) was skipped since it collides with above method
        # Method ToString(value : UInt32) was skipped since it collides with above method
        # Method ToString(value : Int64) was skipped since it collides with above method
        # Method ToString(value : UInt64) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Decimal) -> str:...
        @typing.overload
        def __call__(self, value: DateTime) -> str:...
        # Method ToString(value : Boolean) was skipped since it collides with above method
        # Method ToString(value : String) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: typing.Any) -> str:...
        @typing.overload
        def __call__(self, value: float, provider: IFormatProvider) -> str:...
        # Method ToString(value : Double, provider : IFormatProvider) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: int, toBase: int) -> str:...
        # Method ToString(value : Int16, toBase : Int32) was skipped since it collides with above method
        # Method ToString(value : Int32, toBase : Int32) was skipped since it collides with above method
        # Method ToString(value : Int64, toBase : Int32) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: str, provider: IFormatProvider) -> str:...
        # Method ToString(value : SByte, provider : IFormatProvider) was skipped since it collides with above method
        # Method ToString(value : Byte, provider : IFormatProvider) was skipped since it collides with above method
        # Method ToString(value : Int16, provider : IFormatProvider) was skipped since it collides with above method
        # Method ToString(value : UInt16, provider : IFormatProvider) was skipped since it collides with above method
        # Method ToString(value : Int32, provider : IFormatProvider) was skipped since it collides with above method
        # Method ToString(value : UInt32, provider : IFormatProvider) was skipped since it collides with above method
        # Method ToString(value : Int64, provider : IFormatProvider) was skipped since it collides with above method
        # Method ToString(value : UInt64, provider : IFormatProvider) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Decimal, provider: IFormatProvider) -> str:...
        @typing.overload
        def __call__(self, value: DateTime, provider: IFormatProvider) -> str:...
        # Method ToString(value : Boolean, provider : IFormatProvider) was skipped since it collides with above method
        # Method ToString(value : String, provider : IFormatProvider) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: typing.Any, provider: IFormatProvider) -> str:...

    # Skipped ToUInt16 due to it being static, abstract and generic.

    ToUInt16 : ToUInt16_MethodGroup
    class ToUInt16_MethodGroup:
        @typing.overload
        def __call__(self, value: float) -> int:...
        # Method ToUInt16(value : Double) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: str) -> int:...
        # Method ToUInt16(value : SByte) was skipped since it collides with above method
        # Method ToUInt16(value : Byte) was skipped since it collides with above method
        # Method ToUInt16(value : Int16) was skipped since it collides with above method
        # Method ToUInt16(value : Int32) was skipped since it collides with above method
        # Method ToUInt16(value : UInt16) was skipped since it collides with above method
        # Method ToUInt16(value : UInt32) was skipped since it collides with above method
        # Method ToUInt16(value : Int64) was skipped since it collides with above method
        # Method ToUInt16(value : UInt64) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Decimal) -> int:...
        @typing.overload
        def __call__(self, value: DateTime) -> int:...
        # Method ToUInt16(value : Boolean) was skipped since it collides with above method
        # Method ToUInt16(value : String) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: typing.Any) -> int:...
        @typing.overload
        def __call__(self, value: str, fromBase: int) -> int:...
        @typing.overload
        def __call__(self, value: str, provider: IFormatProvider) -> int:...
        @typing.overload
        def __call__(self, value: typing.Any, provider: IFormatProvider) -> int:...

    # Skipped ToUInt32 due to it being static, abstract and generic.

    ToUInt32 : ToUInt32_MethodGroup
    class ToUInt32_MethodGroup:
        @typing.overload
        def __call__(self, value: float) -> int:...
        # Method ToUInt32(value : Double) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: str) -> int:...
        # Method ToUInt32(value : SByte) was skipped since it collides with above method
        # Method ToUInt32(value : Byte) was skipped since it collides with above method
        # Method ToUInt32(value : Int16) was skipped since it collides with above method
        # Method ToUInt32(value : UInt16) was skipped since it collides with above method
        # Method ToUInt32(value : Int32) was skipped since it collides with above method
        # Method ToUInt32(value : UInt32) was skipped since it collides with above method
        # Method ToUInt32(value : Int64) was skipped since it collides with above method
        # Method ToUInt32(value : UInt64) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Decimal) -> int:...
        @typing.overload
        def __call__(self, value: DateTime) -> int:...
        # Method ToUInt32(value : Boolean) was skipped since it collides with above method
        # Method ToUInt32(value : String) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: typing.Any) -> int:...
        @typing.overload
        def __call__(self, value: str, fromBase: int) -> int:...
        @typing.overload
        def __call__(self, value: str, provider: IFormatProvider) -> int:...
        @typing.overload
        def __call__(self, value: typing.Any, provider: IFormatProvider) -> int:...

    # Skipped ToUInt64 due to it being static, abstract and generic.

    ToUInt64 : ToUInt64_MethodGroup
    class ToUInt64_MethodGroup:
        @typing.overload
        def __call__(self, value: float) -> int:...
        # Method ToUInt64(value : Double) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: str) -> int:...
        # Method ToUInt64(value : SByte) was skipped since it collides with above method
        # Method ToUInt64(value : Byte) was skipped since it collides with above method
        # Method ToUInt64(value : Int16) was skipped since it collides with above method
        # Method ToUInt64(value : UInt16) was skipped since it collides with above method
        # Method ToUInt64(value : Int32) was skipped since it collides with above method
        # Method ToUInt64(value : UInt32) was skipped since it collides with above method
        # Method ToUInt64(value : Int64) was skipped since it collides with above method
        # Method ToUInt64(value : UInt64) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Decimal) -> int:...
        @typing.overload
        def __call__(self, value: DateTime) -> int:...
        # Method ToUInt64(value : Boolean) was skipped since it collides with above method
        # Method ToUInt64(value : String) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: typing.Any) -> int:...
        @typing.overload
        def __call__(self, value: str, fromBase: int) -> int:...
        @typing.overload
        def __call__(self, value: str, provider: IFormatProvider) -> int:...
        @typing.overload
        def __call__(self, value: typing.Any, provider: IFormatProvider) -> int:...



class Converter_GenericClasses(abc.ABCMeta):
    Generic_Converter_GenericClasses_Converter_2_TInput = typing.TypeVar('Generic_Converter_GenericClasses_Converter_2_TInput')
    Generic_Converter_GenericClasses_Converter_2_TOutput = typing.TypeVar('Generic_Converter_GenericClasses_Converter_2_TOutput')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_Converter_GenericClasses_Converter_2_TInput], typing.Type[Generic_Converter_GenericClasses_Converter_2_TOutput]]) -> typing.Type[Converter_2[Generic_Converter_GenericClasses_Converter_2_TInput, Generic_Converter_GenericClasses_Converter_2_TOutput]]: ...

Converter : Converter_GenericClasses

Converter_2_TInput = typing.TypeVar('Converter_2_TInput', contravariant=True)
Converter_2_TOutput = typing.TypeVar('Converter_2_TOutput', covariant=True)
class Converter_2(typing.Generic[Converter_2_TInput, Converter_2_TOutput], MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, input: Converter_2_TInput, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> Converter_2_TOutput: ...
    def Invoke(self, input: Converter_2_TInput) -> Converter_2_TOutput: ...


class CultureAwareComparer(StringComparer, ISerializable):
    def Compare(self, x: str, y: str) -> int: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...
        @typing.overload
        def __call__(self, x: str, y: str) -> bool:...

    # Skipped GetHashCode due to it being static, abstract and generic.

    GetHashCode : GetHashCode_MethodGroup
    class GetHashCode_MethodGroup:
        @typing.overload
        def __call__(self) -> int:...
        @typing.overload
        def __call__(self, obj: str) -> int:...



class DataMisalignedException(SystemException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, innerException: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...


class DateOnly(IComparisonOperators_2[DateOnly, DateOnly], ISpanParseable_1[DateOnly], ISpanFormattable, IMinMaxValue_1[DateOnly]):
    @typing.overload
    def __init__(self, year: int, month: int, day: int) -> None: ...
    @typing.overload
    def __init__(self, year: int, month: int, day: int, calendar: Calendar) -> None: ...
    @property
    def Day(self) -> int: ...
    @property
    def DayNumber(self) -> int: ...
    @property
    def DayOfWeek(self) -> DayOfWeek: ...
    @property
    def DayOfYear(self) -> int: ...
    @classmethod
    @property
    def MaxValue(cls) -> DateOnly: ...
    @classmethod
    @property
    def MinValue(cls) -> DateOnly: ...
    @property
    def Month(self) -> int: ...
    @property
    def Year(self) -> int: ...
    def AddDays(self, value: int) -> DateOnly: ...
    def AddMonths(self, value: int) -> DateOnly: ...
    def AddYears(self, value: int) -> DateOnly: ...
    @staticmethod
    def FromDateTime(dateTime: DateTime) -> DateOnly: ...
    @staticmethod
    def FromDayNumber(dayNumber: int) -> DateOnly: ...
    def GetHashCode(self) -> int: ...
    def __eq__(self, left: DateOnly, right: DateOnly) -> bool: ...
    def __gt__(self, left: DateOnly, right: DateOnly) -> bool: ...
    def __ge__(self, left: DateOnly, right: DateOnly) -> bool: ...
    def __ne__(self, left: DateOnly, right: DateOnly) -> bool: ...
    def __lt__(self, left: DateOnly, right: DateOnly) -> bool: ...
    def __le__(self, left: DateOnly, right: DateOnly) -> bool: ...
    def ToLongDateString(self) -> str: ...
    def ToShortDateString(self) -> str: ...
    def TryFormat(self, destination: Span_1[str], charsWritten: clr.Reference[int], format: ReadOnlySpan_1[str] = ..., provider: IFormatProvider = ...) -> bool: ...
    # Skipped CompareTo due to it being static, abstract and generic.

    CompareTo : CompareTo_MethodGroup
    class CompareTo_MethodGroup:
        @typing.overload
        def __call__(self, value: DateOnly) -> int:...
        @typing.overload
        def __call__(self, value: typing.Any) -> int:...

    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, value: DateOnly) -> bool:...
        @typing.overload
        def __call__(self, value: typing.Any) -> bool:...

    # Skipped Parse due to it being static, abstract and generic.

    Parse : Parse_MethodGroup
    class Parse_MethodGroup:
        @typing.overload
        def __call__(self, s: str) -> DateOnly:...
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], provider: IFormatProvider = ..., style: DateTimeStyles = ...) -> DateOnly:...
        @typing.overload
        def __call__(self, s: str, provider: IFormatProvider, style: DateTimeStyles = ...) -> DateOnly:...

    # Skipped ParseExact due to it being static, abstract and generic.

    ParseExact : ParseExact_MethodGroup
    class ParseExact_MethodGroup:
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], formats: Array_1[str]) -> DateOnly:...
        @typing.overload
        def __call__(self, s: str, formats: Array_1[str]) -> DateOnly:...
        @typing.overload
        def __call__(self, s: str, format: str) -> DateOnly:...
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], formats: Array_1[str], provider: IFormatProvider, style: DateTimeStyles = ...) -> DateOnly:...
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], format: ReadOnlySpan_1[str], provider: IFormatProvider = ..., style: DateTimeStyles = ...) -> DateOnly:...
        @typing.overload
        def __call__(self, s: str, formats: Array_1[str], provider: IFormatProvider, style: DateTimeStyles = ...) -> DateOnly:...
        @typing.overload
        def __call__(self, s: str, format: str, provider: IFormatProvider, style: DateTimeStyles = ...) -> DateOnly:...

    # Skipped ToDateTime due to it being static, abstract and generic.

    ToDateTime : ToDateTime_MethodGroup
    class ToDateTime_MethodGroup:
        @typing.overload
        def __call__(self, time: TimeOnly) -> DateTime:...
        @typing.overload
        def __call__(self, time: TimeOnly, kind: DateTimeKind) -> DateTime:...

    # Skipped ToString due to it being static, abstract and generic.

    ToString : ToString_MethodGroup
    class ToString_MethodGroup:
        @typing.overload
        def __call__(self) -> str:...
        @typing.overload
        def __call__(self, format: str) -> str:...
        @typing.overload
        def __call__(self, provider: IFormatProvider) -> str:...
        @typing.overload
        def __call__(self, format: str, provider: IFormatProvider) -> str:...

    # Skipped TryParse due to it being static, abstract and generic.

    TryParse : TryParse_MethodGroup
    class TryParse_MethodGroup:
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], result: clr.Reference[DateOnly]) -> bool:...
        @typing.overload
        def __call__(self, s: str, result: clr.Reference[DateOnly]) -> bool:...
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], provider: IFormatProvider, style: DateTimeStyles, result: clr.Reference[DateOnly]) -> bool:...
        @typing.overload
        def __call__(self, s: str, provider: IFormatProvider, style: DateTimeStyles, result: clr.Reference[DateOnly]) -> bool:...

    # Skipped TryParseExact due to it being static, abstract and generic.

    TryParseExact : TryParseExact_MethodGroup
    class TryParseExact_MethodGroup:
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], formats: Array_1[str], result: clr.Reference[DateOnly]) -> bool:...
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], format: ReadOnlySpan_1[str], result: clr.Reference[DateOnly]) -> bool:...
        @typing.overload
        def __call__(self, s: str, formats: Array_1[str], result: clr.Reference[DateOnly]) -> bool:...
        @typing.overload
        def __call__(self, s: str, format: str, result: clr.Reference[DateOnly]) -> bool:...
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], formats: Array_1[str], provider: IFormatProvider, style: DateTimeStyles, result: clr.Reference[DateOnly]) -> bool:...
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], format: ReadOnlySpan_1[str], provider: IFormatProvider, style: DateTimeStyles, result: clr.Reference[DateOnly]) -> bool:...
        @typing.overload
        def __call__(self, s: str, formats: Array_1[str], provider: IFormatProvider, style: DateTimeStyles, result: clr.Reference[DateOnly]) -> bool:...
        @typing.overload
        def __call__(self, s: str, format: str, provider: IFormatProvider, style: DateTimeStyles, result: clr.Reference[DateOnly]) -> bool:...



class DateTime(IComparisonOperators_2[DateTime, DateTime], ISpanParseable_1[DateTime], ISpanFormattable, ISubtractionOperators_3[DateTime, DateTime, TimeSpan], ISubtractionOperators_3[DateTime, TimeSpan, DateTime], IMinMaxValue_1[DateTime], IAdditiveIdentity_2[DateTime, TimeSpan], IAdditionOperators_3[DateTime, TimeSpan, DateTime], ISerializable, IConvertible):
    @typing.overload
    def __init__(self, ticks: int) -> None: ...
    @typing.overload
    def __init__(self, ticks: int, kind: DateTimeKind) -> None: ...
    @typing.overload
    def __init__(self, year: int, month: int, day: int) -> None: ...
    @typing.overload
    def __init__(self, year: int, month: int, day: int, calendar: Calendar) -> None: ...
    @typing.overload
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int) -> None: ...
    @typing.overload
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int, calendar: Calendar) -> None: ...
    @typing.overload
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int, kind: DateTimeKind) -> None: ...
    @typing.overload
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int) -> None: ...
    @typing.overload
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, calendar: Calendar) -> None: ...
    @typing.overload
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, calendar: Calendar, kind: DateTimeKind) -> None: ...
    @typing.overload
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, kind: DateTimeKind) -> None: ...
    MaxValue : DateTime
    MinValue : DateTime
    UnixEpoch : DateTime
    @property
    def Date(self) -> DateTime: ...
    @property
    def Day(self) -> int: ...
    @property
    def DayOfWeek(self) -> DayOfWeek: ...
    @property
    def DayOfYear(self) -> int: ...
    @property
    def Hour(self) -> int: ...
    @property
    def Kind(self) -> DateTimeKind: ...
    @property
    def Millisecond(self) -> int: ...
    @property
    def Minute(self) -> int: ...
    @property
    def Month(self) -> int: ...
    @classmethod
    @property
    def Now(cls) -> DateTime: ...
    @property
    def Second(self) -> int: ...
    @property
    def Ticks(self) -> int: ...
    @property
    def TimeOfDay(self) -> TimeSpan: ...
    @classmethod
    @property
    def Today(cls) -> DateTime: ...
    @classmethod
    @property
    def UtcNow(cls) -> DateTime: ...
    @property
    def Year(self) -> int: ...
    def Add(self, value: TimeSpan) -> DateTime: ...
    def AddDays(self, value: float) -> DateTime: ...
    def AddHours(self, value: float) -> DateTime: ...
    def AddMilliseconds(self, value: float) -> DateTime: ...
    def AddMinutes(self, value: float) -> DateTime: ...
    def AddMonths(self, months: int) -> DateTime: ...
    def AddSeconds(self, value: float) -> DateTime: ...
    def AddTicks(self, value: int) -> DateTime: ...
    def AddYears(self, value: int) -> DateTime: ...
    @staticmethod
    def Compare(t1: DateTime, t2: DateTime) -> int: ...
    @staticmethod
    def DaysInMonth(year: int, month: int) -> int: ...
    @staticmethod
    def FromBinary(dateData: int) -> DateTime: ...
    @staticmethod
    def FromFileTime(fileTime: int) -> DateTime: ...
    @staticmethod
    def FromFileTimeUtc(fileTime: int) -> DateTime: ...
    @staticmethod
    def FromOADate(d: float) -> DateTime: ...
    def GetHashCode(self) -> int: ...
    def GetTypeCode(self) -> TypeCode: ...
    def IsDaylightSavingTime(self) -> bool: ...
    @staticmethod
    def IsLeapYear(year: int) -> bool: ...
    def __add__(self, d: DateTime, t: TimeSpan) -> DateTime: ...
    def __eq__(self, d1: DateTime, d2: DateTime) -> bool: ...
    def __gt__(self, t1: DateTime, t2: DateTime) -> bool: ...
    def __ge__(self, t1: DateTime, t2: DateTime) -> bool: ...
    def __ne__(self, d1: DateTime, d2: DateTime) -> bool: ...
    def __lt__(self, t1: DateTime, t2: DateTime) -> bool: ...
    def __le__(self, t1: DateTime, t2: DateTime) -> bool: ...
    @typing.overload
    def __sub__(self, d1: DateTime, d2: DateTime) -> TimeSpan: ...
    @typing.overload
    def __sub__(self, d: DateTime, t: TimeSpan) -> DateTime: ...
    @staticmethod
    def SpecifyKind(value: DateTime, kind: DateTimeKind) -> DateTime: ...
    def ToBinary(self) -> int: ...
    def ToFileTime(self) -> int: ...
    def ToFileTimeUtc(self) -> int: ...
    def ToLocalTime(self) -> DateTime: ...
    def ToLongDateString(self) -> str: ...
    def ToLongTimeString(self) -> str: ...
    def ToOADate(self) -> float: ...
    def ToShortDateString(self) -> str: ...
    def ToShortTimeString(self) -> str: ...
    def ToUniversalTime(self) -> DateTime: ...
    def TryFormat(self, destination: Span_1[str], charsWritten: clr.Reference[int], format: ReadOnlySpan_1[str] = ..., provider: IFormatProvider = ...) -> bool: ...
    # Skipped CompareTo due to it being static, abstract and generic.

    CompareTo : CompareTo_MethodGroup
    class CompareTo_MethodGroup:
        @typing.overload
        def __call__(self, value: DateTime) -> int:...
        @typing.overload
        def __call__(self, value: typing.Any) -> int:...

    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, value: DateTime) -> bool:...
        @typing.overload
        def __call__(self, value: typing.Any) -> bool:...
        @typing.overload
        def __call__(self, t1: DateTime, t2: DateTime) -> bool:...

    # Skipped GetDateTimeFormats due to it being static, abstract and generic.

    GetDateTimeFormats : GetDateTimeFormats_MethodGroup
    class GetDateTimeFormats_MethodGroup:
        @typing.overload
        def __call__(self) -> Array_1[str]:...
        @typing.overload
        def __call__(self, format: str) -> Array_1[str]:...
        @typing.overload
        def __call__(self, provider: IFormatProvider) -> Array_1[str]:...
        @typing.overload
        def __call__(self, format: str, provider: IFormatProvider) -> Array_1[str]:...

    # Skipped Parse due to it being static, abstract and generic.

    Parse : Parse_MethodGroup
    class Parse_MethodGroup:
        @typing.overload
        def __call__(self, s: str) -> DateTime:...
        @typing.overload
        def __call__(self, s: str, provider: IFormatProvider) -> DateTime:...
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], provider: IFormatProvider = ..., styles: DateTimeStyles = ...) -> DateTime:...
        @typing.overload
        def __call__(self, s: str, provider: IFormatProvider, styles: DateTimeStyles) -> DateTime:...

    # Skipped ParseExact due to it being static, abstract and generic.

    ParseExact : ParseExact_MethodGroup
    class ParseExact_MethodGroup:
        @typing.overload
        def __call__(self, s: str, format: str, provider: IFormatProvider) -> DateTime:...
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], formats: Array_1[str], provider: IFormatProvider, style: DateTimeStyles = ...) -> DateTime:...
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], format: ReadOnlySpan_1[str], provider: IFormatProvider, style: DateTimeStyles = ...) -> DateTime:...
        @typing.overload
        def __call__(self, s: str, formats: Array_1[str], provider: IFormatProvider, style: DateTimeStyles) -> DateTime:...
        @typing.overload
        def __call__(self, s: str, format: str, provider: IFormatProvider, style: DateTimeStyles) -> DateTime:...

    # Skipped Subtract due to it being static, abstract and generic.

    Subtract : Subtract_MethodGroup
    class Subtract_MethodGroup:
        @typing.overload
        def __call__(self, value: DateTime) -> TimeSpan:...
        @typing.overload
        def __call__(self, value: TimeSpan) -> DateTime:...

    # Skipped ToString due to it being static, abstract and generic.

    ToString : ToString_MethodGroup
    class ToString_MethodGroup:
        @typing.overload
        def __call__(self) -> str:...
        @typing.overload
        def __call__(self, format: str) -> str:...
        @typing.overload
        def __call__(self, provider: IFormatProvider) -> str:...
        @typing.overload
        def __call__(self, format: str, provider: IFormatProvider) -> str:...

    # Skipped TryParse due to it being static, abstract and generic.

    TryParse : TryParse_MethodGroup
    class TryParse_MethodGroup:
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], result: clr.Reference[DateTime]) -> bool:...
        @typing.overload
        def __call__(self, s: str, result: clr.Reference[DateTime]) -> bool:...
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], provider: IFormatProvider, styles: DateTimeStyles, result: clr.Reference[DateTime]) -> bool:...
        @typing.overload
        def __call__(self, s: str, provider: IFormatProvider, styles: DateTimeStyles, result: clr.Reference[DateTime]) -> bool:...

    # Skipped TryParseExact due to it being static, abstract and generic.

    TryParseExact : TryParseExact_MethodGroup
    class TryParseExact_MethodGroup:
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], formats: Array_1[str], provider: IFormatProvider, style: DateTimeStyles, result: clr.Reference[DateTime]) -> bool:...
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], format: ReadOnlySpan_1[str], provider: IFormatProvider, style: DateTimeStyles, result: clr.Reference[DateTime]) -> bool:...
        @typing.overload
        def __call__(self, s: str, formats: Array_1[str], provider: IFormatProvider, style: DateTimeStyles, result: clr.Reference[DateTime]) -> bool:...
        @typing.overload
        def __call__(self, s: str, format: str, provider: IFormatProvider, style: DateTimeStyles, result: clr.Reference[DateTime]) -> bool:...



class DateTimeKind(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Unspecified : DateTimeKind # 0
    Utc : DateTimeKind # 1
    Local : DateTimeKind # 2


class DateTimeOffset(IComparisonOperators_2[DateTimeOffset, DateTimeOffset], ISpanParseable_1[DateTimeOffset], ISpanFormattable, ISubtractionOperators_3[DateTimeOffset, DateTimeOffset, TimeSpan], ISubtractionOperators_3[DateTimeOffset, TimeSpan, DateTimeOffset], IMinMaxValue_1[DateTimeOffset], IAdditiveIdentity_2[DateTimeOffset, TimeSpan], IAdditionOperators_3[DateTimeOffset, TimeSpan, DateTimeOffset], IDeserializationCallback, ISerializable):
    @typing.overload
    def __init__(self, dateTime: DateTime) -> None: ...
    @typing.overload
    def __init__(self, dateTime: DateTime, offset: TimeSpan) -> None: ...
    @typing.overload
    def __init__(self, ticks: int, offset: TimeSpan) -> None: ...
    @typing.overload
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, calendar: Calendar, offset: TimeSpan) -> None: ...
    @typing.overload
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, offset: TimeSpan) -> None: ...
    @typing.overload
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int, offset: TimeSpan) -> None: ...
    MaxValue : DateTimeOffset
    MinValue : DateTimeOffset
    UnixEpoch : DateTimeOffset
    @property
    def Date(self) -> DateTime: ...
    @property
    def DateTime(self) -> DateTime: ...
    @property
    def Day(self) -> int: ...
    @property
    def DayOfWeek(self) -> DayOfWeek: ...
    @property
    def DayOfYear(self) -> int: ...
    @property
    def Hour(self) -> int: ...
    @property
    def LocalDateTime(self) -> DateTime: ...
    @property
    def Millisecond(self) -> int: ...
    @property
    def Minute(self) -> int: ...
    @property
    def Month(self) -> int: ...
    @classmethod
    @property
    def Now(cls) -> DateTimeOffset: ...
    @property
    def Offset(self) -> TimeSpan: ...
    @property
    def Second(self) -> int: ...
    @property
    def Ticks(self) -> int: ...
    @property
    def TimeOfDay(self) -> TimeSpan: ...
    @property
    def UtcDateTime(self) -> DateTime: ...
    @classmethod
    @property
    def UtcNow(cls) -> DateTimeOffset: ...
    @property
    def UtcTicks(self) -> int: ...
    @property
    def Year(self) -> int: ...
    def Add(self, timeSpan: TimeSpan) -> DateTimeOffset: ...
    def AddDays(self, days: float) -> DateTimeOffset: ...
    def AddHours(self, hours: float) -> DateTimeOffset: ...
    def AddMilliseconds(self, milliseconds: float) -> DateTimeOffset: ...
    def AddMinutes(self, minutes: float) -> DateTimeOffset: ...
    def AddMonths(self, months: int) -> DateTimeOffset: ...
    def AddSeconds(self, seconds: float) -> DateTimeOffset: ...
    def AddTicks(self, ticks: int) -> DateTimeOffset: ...
    def AddYears(self, years: int) -> DateTimeOffset: ...
    @staticmethod
    def Compare(first: DateTimeOffset, second: DateTimeOffset) -> int: ...
    def CompareTo(self, other: DateTimeOffset) -> int: ...
    def EqualsExact(self, other: DateTimeOffset) -> bool: ...
    @staticmethod
    def FromFileTime(fileTime: int) -> DateTimeOffset: ...
    @staticmethod
    def FromUnixTimeMilliseconds(milliseconds: int) -> DateTimeOffset: ...
    @staticmethod
    def FromUnixTimeSeconds(seconds: int) -> DateTimeOffset: ...
    def GetHashCode(self) -> int: ...
    def __add__(self, dateTimeOffset: DateTimeOffset, timeSpan: TimeSpan) -> DateTimeOffset: ...
    def __eq__(self, left: DateTimeOffset, right: DateTimeOffset) -> bool: ...
    def __gt__(self, left: DateTimeOffset, right: DateTimeOffset) -> bool: ...
    def __ge__(self, left: DateTimeOffset, right: DateTimeOffset) -> bool: ...
    # Operator not supported op_Implicit(dateTime: DateTime)
    def __ne__(self, left: DateTimeOffset, right: DateTimeOffset) -> bool: ...
    def __lt__(self, left: DateTimeOffset, right: DateTimeOffset) -> bool: ...
    def __le__(self, left: DateTimeOffset, right: DateTimeOffset) -> bool: ...
    @typing.overload
    def __sub__(self, dateTimeOffset: DateTimeOffset, timeSpan: TimeSpan) -> DateTimeOffset: ...
    @typing.overload
    def __sub__(self, left: DateTimeOffset, right: DateTimeOffset) -> TimeSpan: ...
    def ToFileTime(self) -> int: ...
    def ToLocalTime(self) -> DateTimeOffset: ...
    def ToOffset(self, offset: TimeSpan) -> DateTimeOffset: ...
    def ToUniversalTime(self) -> DateTimeOffset: ...
    def ToUnixTimeMilliseconds(self) -> int: ...
    def ToUnixTimeSeconds(self) -> int: ...
    def TryFormat(self, destination: Span_1[str], charsWritten: clr.Reference[int], format: ReadOnlySpan_1[str] = ..., formatProvider: IFormatProvider = ...) -> bool: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, other: DateTimeOffset) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...
        @typing.overload
        def __call__(self, first: DateTimeOffset, second: DateTimeOffset) -> bool:...

    # Skipped Parse due to it being static, abstract and generic.

    Parse : Parse_MethodGroup
    class Parse_MethodGroup:
        @typing.overload
        def __call__(self, input: str) -> DateTimeOffset:...
        @typing.overload
        def __call__(self, input: str, formatProvider: IFormatProvider) -> DateTimeOffset:...
        @typing.overload
        def __call__(self, input: ReadOnlySpan_1[str], formatProvider: IFormatProvider = ..., styles: DateTimeStyles = ...) -> DateTimeOffset:...
        @typing.overload
        def __call__(self, input: str, formatProvider: IFormatProvider, styles: DateTimeStyles) -> DateTimeOffset:...

    # Skipped ParseExact due to it being static, abstract and generic.

    ParseExact : ParseExact_MethodGroup
    class ParseExact_MethodGroup:
        @typing.overload
        def __call__(self, input: str, format: str, formatProvider: IFormatProvider) -> DateTimeOffset:...
        @typing.overload
        def __call__(self, input: ReadOnlySpan_1[str], formats: Array_1[str], formatProvider: IFormatProvider, styles: DateTimeStyles = ...) -> DateTimeOffset:...
        @typing.overload
        def __call__(self, input: ReadOnlySpan_1[str], format: ReadOnlySpan_1[str], formatProvider: IFormatProvider, styles: DateTimeStyles = ...) -> DateTimeOffset:...
        @typing.overload
        def __call__(self, input: str, formats: Array_1[str], formatProvider: IFormatProvider, styles: DateTimeStyles) -> DateTimeOffset:...
        @typing.overload
        def __call__(self, input: str, format: str, formatProvider: IFormatProvider, styles: DateTimeStyles) -> DateTimeOffset:...

    # Skipped Subtract due to it being static, abstract and generic.

    Subtract : Subtract_MethodGroup
    class Subtract_MethodGroup:
        @typing.overload
        def __call__(self, value: DateTimeOffset) -> TimeSpan:...
        @typing.overload
        def __call__(self, value: TimeSpan) -> DateTimeOffset:...

    # Skipped ToString due to it being static, abstract and generic.

    ToString : ToString_MethodGroup
    class ToString_MethodGroup:
        @typing.overload
        def __call__(self) -> str:...
        @typing.overload
        def __call__(self, format: str) -> str:...
        @typing.overload
        def __call__(self, formatProvider: IFormatProvider) -> str:...
        @typing.overload
        def __call__(self, format: str, formatProvider: IFormatProvider) -> str:...

    # Skipped TryParse due to it being static, abstract and generic.

    TryParse : TryParse_MethodGroup
    class TryParse_MethodGroup:
        @typing.overload
        def __call__(self, input: ReadOnlySpan_1[str], result: clr.Reference[DateTimeOffset]) -> bool:...
        @typing.overload
        def __call__(self, input: str, result: clr.Reference[DateTimeOffset]) -> bool:...
        @typing.overload
        def __call__(self, input: ReadOnlySpan_1[str], formatProvider: IFormatProvider, styles: DateTimeStyles, result: clr.Reference[DateTimeOffset]) -> bool:...
        @typing.overload
        def __call__(self, input: str, formatProvider: IFormatProvider, styles: DateTimeStyles, result: clr.Reference[DateTimeOffset]) -> bool:...

    # Skipped TryParseExact due to it being static, abstract and generic.

    TryParseExact : TryParseExact_MethodGroup
    class TryParseExact_MethodGroup:
        @typing.overload
        def __call__(self, input: ReadOnlySpan_1[str], formats: Array_1[str], formatProvider: IFormatProvider, styles: DateTimeStyles, result: clr.Reference[DateTimeOffset]) -> bool:...
        @typing.overload
        def __call__(self, input: ReadOnlySpan_1[str], format: ReadOnlySpan_1[str], formatProvider: IFormatProvider, styles: DateTimeStyles, result: clr.Reference[DateTimeOffset]) -> bool:...
        @typing.overload
        def __call__(self, input: str, formats: Array_1[str], formatProvider: IFormatProvider, styles: DateTimeStyles, result: clr.Reference[DateTimeOffset]) -> bool:...
        @typing.overload
        def __call__(self, input: str, format: str, formatProvider: IFormatProvider, styles: DateTimeStyles, result: clr.Reference[DateTimeOffset]) -> bool:...



class DayOfWeek(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Sunday : DayOfWeek # 0
    Monday : DayOfWeek # 1
    Tuesday : DayOfWeek # 2
    Wednesday : DayOfWeek # 3
    Thursday : DayOfWeek # 4
    Friday : DayOfWeek # 5
    Saturday : DayOfWeek # 6


class DBNull(IConvertible, ISerializable):
    Value : DBNull
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...
    def GetTypeCode(self) -> TypeCode: ...
    # Skipped ToString due to it being static, abstract and generic.

    ToString : ToString_MethodGroup
    class ToString_MethodGroup:
        @typing.overload
        def __call__(self) -> str:...
        @typing.overload
        def __call__(self, provider: IFormatProvider) -> str:...



class Decimal(ISignedNumber_1[Decimal], IMinMaxValue_1[Decimal], IDeserializationCallback, ISerializable, IConvertible):
    # Constructor .ctor(value : UInt32) was skipped since it collides with above method
    # Constructor .ctor(value : Int64) was skipped since it collides with above method
    # Constructor .ctor(value : UInt64) was skipped since it collides with above method
    # Constructor .ctor(value : Single) was skipped since it collides with above method
    # Constructor .ctor(value : Double) was skipped since it collides with above method
    @typing.overload
    def __init__(self, bits: Array_1[int]) -> None: ...
    @typing.overload
    def __init__(self, bits: ReadOnlySpan_1[int]) -> None: ...
    @typing.overload
    def __init__(self, lo: int, mid: int, hi: int, isNegative: bool, scale: int) -> None: ...
    @typing.overload
    def __init__(self, value: int) -> None: ...
    MaxValue : Decimal
    MinusOne : Decimal
    MinValue : Decimal
    One : Decimal
    Zero : Decimal
    @staticmethod
    def Add(d1: Decimal, d2: Decimal) -> Decimal: ...
    @staticmethod
    def Ceiling(d: Decimal) -> Decimal: ...
    @staticmethod
    def Compare(d1: Decimal, d2: Decimal) -> int: ...
    @staticmethod
    def Divide(d1: Decimal, d2: Decimal) -> Decimal: ...
    @staticmethod
    def Floor(d: Decimal) -> Decimal: ...
    @staticmethod
    def FromOACurrency(cy: int) -> Decimal: ...
    def GetHashCode(self) -> int: ...
    def GetTypeCode(self) -> TypeCode: ...
    @staticmethod
    def Multiply(d1: Decimal, d2: Decimal) -> Decimal: ...
    @staticmethod
    def Negate(d: Decimal) -> Decimal: ...
    def __add__(self, d1: Decimal, d2: Decimal) -> Decimal: ...
    # Operator not supported op_Decrement(d: Decimal)
    def __truediv__(self, d1: Decimal, d2: Decimal) -> Decimal: ...
    def __eq__(self, d1: Decimal, d2: Decimal) -> bool: ...
    # Operator not supported op_Explicit(value: Single)
    # Operator not supported op_Explicit(value: Double)
    # Operator not supported op_Explicit(value: Decimal)
    # Operator not supported op_Explicit(value: Decimal)
    # Operator not supported op_Explicit(value: Decimal)
    # Operator not supported op_Explicit(value: Decimal)
    # Operator not supported op_Explicit(value: Decimal)
    # Operator not supported op_Explicit(value: Decimal)
    # Operator not supported op_Explicit(value: Decimal)
    # Operator not supported op_Explicit(value: Decimal)
    # Operator not supported op_Explicit(value: Decimal)
    # Operator not supported op_Explicit(value: Decimal)
    # Operator not supported op_Explicit(value: Decimal)
    def __gt__(self, d1: Decimal, d2: Decimal) -> bool: ...
    def __ge__(self, d1: Decimal, d2: Decimal) -> bool: ...
    # Operator not supported op_Implicit(value: Int16)
    # Operator not supported op_Implicit(value: UInt16)
    # Operator not supported op_Implicit(value: Char)
    # Operator not supported op_Implicit(value: Int32)
    # Operator not supported op_Implicit(value: UInt32)
    # Operator not supported op_Implicit(value: Int64)
    # Operator not supported op_Implicit(value: UInt64)
    # Operator not supported op_Implicit(value: Byte)
    # Operator not supported op_Implicit(value: SByte)
    # Operator not supported op_Increment(d: Decimal)
    def __ne__(self, d1: Decimal, d2: Decimal) -> bool: ...
    def __lt__(self, d1: Decimal, d2: Decimal) -> bool: ...
    def __le__(self, d1: Decimal, d2: Decimal) -> bool: ...
    def __mod__(self, d1: Decimal, d2: Decimal) -> Decimal: ...
    def __mul__(self, d1: Decimal, d2: Decimal) -> Decimal: ...
    def __sub__(self, d1: Decimal, d2: Decimal) -> Decimal: ...
    def __neg__(self, d: Decimal) -> Decimal: ...
    def __pos__(self, d: Decimal) -> Decimal: ...
    @staticmethod
    def Remainder(d1: Decimal, d2: Decimal) -> Decimal: ...
    @staticmethod
    def Subtract(d1: Decimal, d2: Decimal) -> Decimal: ...
    @staticmethod
    def ToByte(value: Decimal) -> int: ...
    @staticmethod
    def ToDouble(d: Decimal) -> float: ...
    @staticmethod
    def ToInt16(value: Decimal) -> int: ...
    @staticmethod
    def ToInt32(d: Decimal) -> int: ...
    @staticmethod
    def ToInt64(d: Decimal) -> int: ...
    @staticmethod
    def ToOACurrency(value: Decimal) -> int: ...
    @staticmethod
    def ToSByte(value: Decimal) -> int: ...
    @staticmethod
    def ToSingle(d: Decimal) -> float: ...
    @staticmethod
    def ToUInt16(value: Decimal) -> int: ...
    @staticmethod
    def ToUInt32(d: Decimal) -> int: ...
    @staticmethod
    def ToUInt64(d: Decimal) -> int: ...
    @staticmethod
    def Truncate(d: Decimal) -> Decimal: ...
    def TryFormat(self, destination: Span_1[str], charsWritten: clr.Reference[int], format: ReadOnlySpan_1[str] = ..., provider: IFormatProvider = ...) -> bool: ...
    @staticmethod
    def TryGetBits(d: Decimal, destination: Span_1[int], valuesWritten: clr.Reference[int]) -> bool: ...
    # Skipped CompareTo due to it being static, abstract and generic.

    CompareTo : CompareTo_MethodGroup
    class CompareTo_MethodGroup:
        @typing.overload
        def __call__(self, value: Decimal) -> int:...
        @typing.overload
        def __call__(self, value: typing.Any) -> int:...

    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, value: Decimal) -> bool:...
        @typing.overload
        def __call__(self, value: typing.Any) -> bool:...
        @typing.overload
        def __call__(self, d1: Decimal, d2: Decimal) -> bool:...

    # Skipped GetBits due to it being static, abstract and generic.

    GetBits : GetBits_MethodGroup
    class GetBits_MethodGroup:
        @typing.overload
        def __call__(self, d: Decimal) -> Array_1[int]:...
        @typing.overload
        def __call__(self, d: Decimal, destination: Span_1[int]) -> int:...

    # Skipped Parse due to it being static, abstract and generic.

    Parse : Parse_MethodGroup
    class Parse_MethodGroup:
        @typing.overload
        def __call__(self, s: str) -> Decimal:...
        @typing.overload
        def __call__(self, s: str, style: NumberStyles) -> Decimal:...
        @typing.overload
        def __call__(self, s: str, provider: IFormatProvider) -> Decimal:...
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], style: NumberStyles = ..., provider: IFormatProvider = ...) -> Decimal:...
        @typing.overload
        def __call__(self, s: str, style: NumberStyles, provider: IFormatProvider) -> Decimal:...

    # Skipped Round due to it being static, abstract and generic.

    Round : Round_MethodGroup
    class Round_MethodGroup:
        @typing.overload
        def __call__(self, d: Decimal) -> Decimal:...
        @typing.overload
        def __call__(self, d: Decimal, decimals: int) -> Decimal:...
        @typing.overload
        def __call__(self, d: Decimal, mode: MidpointRounding) -> Decimal:...
        @typing.overload
        def __call__(self, d: Decimal, decimals: int, mode: MidpointRounding) -> Decimal:...

    # Skipped ToString due to it being static, abstract and generic.

    ToString : ToString_MethodGroup
    class ToString_MethodGroup:
        @typing.overload
        def __call__(self) -> str:...
        @typing.overload
        def __call__(self, format: str) -> str:...
        @typing.overload
        def __call__(self, provider: IFormatProvider) -> str:...
        @typing.overload
        def __call__(self, format: str, provider: IFormatProvider) -> str:...

    # Skipped TryParse due to it being static, abstract and generic.

    TryParse : TryParse_MethodGroup
    class TryParse_MethodGroup:
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], result: clr.Reference[Decimal]) -> bool:...
        @typing.overload
        def __call__(self, s: str, result: clr.Reference[Decimal]) -> bool:...
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], style: NumberStyles, provider: IFormatProvider, result: clr.Reference[Decimal]) -> bool:...
        @typing.overload
        def __call__(self, s: str, style: NumberStyles, provider: IFormatProvider, result: clr.Reference[Decimal]) -> bool:...



class Delegate(ISerializable, ICloneable, abc.ABC):
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def Clone(self) -> typing.Any: ...
    def DynamicInvoke(self, args: Array_1[typing.Any]) -> typing.Any: ...
    def Equals(self, obj: typing.Any) -> bool: ...
    def GetHashCode(self) -> int: ...
    def GetInvocationList(self) -> Array_1[Delegate]: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...
    def __eq__(self, d1: Delegate, d2: Delegate) -> bool: ...
    def __ne__(self, d1: Delegate, d2: Delegate) -> bool: ...
    @staticmethod
    def Remove(source: Delegate, value: Delegate) -> Delegate: ...
    @staticmethod
    def RemoveAll(source: Delegate, value: Delegate) -> Delegate: ...
    # Skipped Combine due to it being static, abstract and generic.

    Combine : Combine_MethodGroup
    class Combine_MethodGroup:
        @typing.overload
        def __call__(self, delegates: Array_1[Delegate]) -> Delegate:...
        @typing.overload
        def __call__(self, a: Delegate, b: Delegate) -> Delegate:...

    # Skipped CreateDelegate due to it being static, abstract and generic.

    CreateDelegate : CreateDelegate_MethodGroup
    class CreateDelegate_MethodGroup:
        @typing.overload
        def __call__(self, type: typing.Type[typing.Any], method: MethodInfo) -> Delegate:...
        @typing.overload
        def __call__(self, type: typing.Type[typing.Any], method: MethodInfo, throwOnBindFailure: bool) -> Delegate:...
        @typing.overload
        def __call__(self, type: typing.Type[typing.Any], target: typing.Type[typing.Any], method: str) -> Delegate:...
        @typing.overload
        def __call__(self, type: typing.Type[typing.Any], firstArgument: typing.Any, method: MethodInfo) -> Delegate:...
        @typing.overload
        def __call__(self, type: typing.Type[typing.Any], target: typing.Any, method: str) -> Delegate:...
        @typing.overload
        def __call__(self, type: typing.Type[typing.Any], target: typing.Type[typing.Any], method: str, ignoreCase: bool) -> Delegate:...
        @typing.overload
        def __call__(self, type: typing.Type[typing.Any], firstArgument: typing.Any, method: MethodInfo, throwOnBindFailure: bool) -> Delegate:...
        @typing.overload
        def __call__(self, type: typing.Type[typing.Any], target: typing.Any, method: str, ignoreCase: bool) -> Delegate:...
        @typing.overload
        def __call__(self, type: typing.Type[typing.Any], target: typing.Type[typing.Any], method: str, ignoreCase: bool, throwOnBindFailure: bool) -> Delegate:...
        @typing.overload
        def __call__(self, type: typing.Type[typing.Any], target: typing.Any, method: str, ignoreCase: bool, throwOnBindFailure: bool) -> Delegate:...



class DivideByZeroException(ArithmeticException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, innerException: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...


class DllNotFoundException(TypeLoadException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, inner: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...
    @property
    def TypeName(self) -> str: ...


class Double(IBinaryFloatingPoint_1[float], IMinMaxValue_1[float], IConvertible):
    Epsilon : float
    MaxValue : float
    MinValue : float
    NaN : float
    NegativeInfinity : float
    PositiveInfinity : float
    def GetHashCode(self) -> int: ...
    def GetTypeCode(self) -> TypeCode: ...
    @staticmethod
    def IsFinite(d: float) -> bool: ...
    @staticmethod
    def IsInfinity(d: float) -> bool: ...
    @staticmethod
    def IsNaN(d: float) -> bool: ...
    @staticmethod
    def IsNegative(d: float) -> bool: ...
    @staticmethod
    def IsNegativeInfinity(d: float) -> bool: ...
    @staticmethod
    def IsNormal(d: float) -> bool: ...
    @staticmethod
    def IsPositiveInfinity(d: float) -> bool: ...
    @staticmethod
    def IsSubnormal(d: float) -> bool: ...
    def __eq__(self, left: float, right: float) -> bool: ...
    def __gt__(self, left: float, right: float) -> bool: ...
    def __ge__(self, left: float, right: float) -> bool: ...
    def __ne__(self, left: float, right: float) -> bool: ...
    def __lt__(self, left: float, right: float) -> bool: ...
    def __le__(self, left: float, right: float) -> bool: ...
    def TryFormat(self, destination: Span_1[str], charsWritten: clr.Reference[int], format: ReadOnlySpan_1[str] = ..., provider: IFormatProvider = ...) -> bool: ...
    # Skipped CompareTo due to it being static, abstract and generic.

    CompareTo : CompareTo_MethodGroup
    class CompareTo_MethodGroup:
        @typing.overload
        def __call__(self, value: float) -> int:...
        @typing.overload
        def __call__(self, value: typing.Any) -> int:...

    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, obj: float) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...

    # Skipped Parse due to it being static, abstract and generic.

    Parse : Parse_MethodGroup
    class Parse_MethodGroup:
        @typing.overload
        def __call__(self, s: str) -> float:...
        @typing.overload
        def __call__(self, s: str, style: NumberStyles) -> float:...
        @typing.overload
        def __call__(self, s: str, provider: IFormatProvider) -> float:...
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], style: NumberStyles = ..., provider: IFormatProvider = ...) -> float:...
        @typing.overload
        def __call__(self, s: str, style: NumberStyles, provider: IFormatProvider) -> float:...

    # Skipped ToString due to it being static, abstract and generic.

    ToString : ToString_MethodGroup
    class ToString_MethodGroup:
        @typing.overload
        def __call__(self) -> str:...
        @typing.overload
        def __call__(self, format: str) -> str:...
        @typing.overload
        def __call__(self, provider: IFormatProvider) -> str:...
        @typing.overload
        def __call__(self, format: str, provider: IFormatProvider) -> str:...

    # Skipped TryParse due to it being static, abstract and generic.

    TryParse : TryParse_MethodGroup
    class TryParse_MethodGroup:
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], result: clr.Reference[float]) -> bool:...
        @typing.overload
        def __call__(self, s: str, result: clr.Reference[float]) -> bool:...
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], style: NumberStyles, provider: IFormatProvider, result: clr.Reference[float]) -> bool:...
        @typing.overload
        def __call__(self, s: str, style: NumberStyles, provider: IFormatProvider, result: clr.Reference[float]) -> bool:...



class DuplicateWaitObjectException(ArgumentException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str, innerException: Exception) -> None: ...
    @typing.overload
    def __init__(self, parameterName: str) -> None: ...
    @typing.overload
    def __init__(self, parameterName: str, message: str) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def ParamName(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...


class EntryPointNotFoundException(TypeLoadException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, inner: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...
    @property
    def TypeName(self) -> str: ...


class Enum(IConvertible, IFormattable, IComparable_0):
    def CompareTo(self, target: typing.Any) -> int: ...
    def Equals(self, obj: typing.Any) -> bool: ...
    @staticmethod
    def Format(enumType: typing.Type[typing.Any], value: typing.Any, format: str) -> str: ...
    def GetHashCode(self) -> int: ...
    def GetTypeCode(self) -> TypeCode: ...
    @staticmethod
    def GetUnderlyingType(enumType: typing.Type[typing.Any]) -> typing.Type[typing.Any]: ...
    def HasFlag(self, flag: Enum) -> bool: ...
    # Skipped GetName due to it being static, abstract and generic.

    GetName : GetName_MethodGroup
    class GetName_MethodGroup:
        def __getitem__(self, t:typing.Type[GetName_1_T1]) -> GetName_1[GetName_1_T1]: ...

        GetName_1_T1 = typing.TypeVar('GetName_1_T1')
        class GetName_1(typing.Generic[GetName_1_T1]):
            GetName_1_TEnum = Enum.GetName_MethodGroup.GetName_1_T1
            def __call__(self, value: GetName_1_TEnum) -> str:...

        def __call__(self, enumType: typing.Type[typing.Any], value: typing.Any) -> str:...

    # Skipped GetNames due to it being static, abstract and generic.

    GetNames : GetNames_MethodGroup
    class GetNames_MethodGroup:
        def __getitem__(self, t:typing.Type[GetNames_1_T1]) -> GetNames_1[GetNames_1_T1]: ...

        GetNames_1_T1 = typing.TypeVar('GetNames_1_T1')
        class GetNames_1(typing.Generic[GetNames_1_T1]):
            GetNames_1_TEnum = Enum.GetNames_MethodGroup.GetNames_1_T1
            def __call__(self) -> Array_1[str]:...

        def __call__(self, enumType: typing.Type[typing.Any]) -> Array_1[str]:...

    # Skipped GetValues due to it being static, abstract and generic.

    GetValues : GetValues_MethodGroup
    class GetValues_MethodGroup:
        def __getitem__(self, t:typing.Type[GetValues_1_T1]) -> GetValues_1[GetValues_1_T1]: ...

        GetValues_1_T1 = typing.TypeVar('GetValues_1_T1')
        class GetValues_1(typing.Generic[GetValues_1_T1]):
            GetValues_1_TEnum = Enum.GetValues_MethodGroup.GetValues_1_T1
            def __call__(self) -> Array_1[GetValues_1_TEnum]:...

        def __call__(self, enumType: typing.Type[typing.Any]) -> Array:...

    # Skipped IsDefined due to it being static, abstract and generic.

    IsDefined : IsDefined_MethodGroup
    class IsDefined_MethodGroup:
        def __getitem__(self, t:typing.Type[IsDefined_1_T1]) -> IsDefined_1[IsDefined_1_T1]: ...

        IsDefined_1_T1 = typing.TypeVar('IsDefined_1_T1')
        class IsDefined_1(typing.Generic[IsDefined_1_T1]):
            IsDefined_1_TEnum = Enum.IsDefined_MethodGroup.IsDefined_1_T1
            def __call__(self, value: IsDefined_1_TEnum) -> bool:...

        def __call__(self, enumType: typing.Type[typing.Any], value: typing.Any) -> bool:...

    # Skipped Parse due to it being static, abstract and generic.

    Parse : Parse_MethodGroup
    class Parse_MethodGroup:
        def __getitem__(self, t:typing.Type[Parse_1_T1]) -> Parse_1[Parse_1_T1]: ...

        Parse_1_T1 = typing.TypeVar('Parse_1_T1')
        class Parse_1(typing.Generic[Parse_1_T1]):
            Parse_1_TEnum = Enum.Parse_MethodGroup.Parse_1_T1
            @typing.overload
            def __call__(self, value: ReadOnlySpan_1[str]) -> Parse_1_TEnum:...
            @typing.overload
            def __call__(self, value: str) -> Parse_1_TEnum:...
            @typing.overload
            def __call__(self, value: ReadOnlySpan_1[str], ignoreCase: bool) -> Parse_1_TEnum:...
            @typing.overload
            def __call__(self, value: str, ignoreCase: bool) -> Parse_1_TEnum:...

        @typing.overload
        def __call__(self, enumType: typing.Type[typing.Any], value: ReadOnlySpan_1[str]) -> typing.Any:...
        @typing.overload
        def __call__(self, enumType: typing.Type[typing.Any], value: str) -> typing.Any:...
        @typing.overload
        def __call__(self, enumType: typing.Type[typing.Any], value: ReadOnlySpan_1[str], ignoreCase: bool) -> typing.Any:...
        @typing.overload
        def __call__(self, enumType: typing.Type[typing.Any], value: str, ignoreCase: bool) -> typing.Any:...

    # Skipped ToObject due to it being static, abstract and generic.

    ToObject : ToObject_MethodGroup
    class ToObject_MethodGroup:
        @typing.overload
        def __call__(self, enumType: typing.Type[typing.Any], value: int) -> typing.Any:...
        # Method ToObject(enumType : Type, value : Int16) was skipped since it collides with above method
        # Method ToObject(enumType : Type, value : Int32) was skipped since it collides with above method
        # Method ToObject(enumType : Type, value : Byte) was skipped since it collides with above method
        # Method ToObject(enumType : Type, value : UInt16) was skipped since it collides with above method
        # Method ToObject(enumType : Type, value : UInt32) was skipped since it collides with above method
        # Method ToObject(enumType : Type, value : Int64) was skipped since it collides with above method
        # Method ToObject(enumType : Type, value : UInt64) was skipped since it collides with above method
        @typing.overload
        def __call__(self, enumType: typing.Type[typing.Any], value: typing.Any) -> typing.Any:...

    # Skipped ToString due to it being static, abstract and generic.

    ToString : ToString_MethodGroup
    class ToString_MethodGroup:
        @typing.overload
        def __call__(self) -> str:...
        @typing.overload
        def __call__(self, format: str) -> str:...
        @typing.overload
        def __call__(self, provider: IFormatProvider) -> str:...
        @typing.overload
        def __call__(self, format: str, provider: IFormatProvider) -> str:...

    # Skipped TryParse due to it being static, abstract and generic.

    TryParse : TryParse_MethodGroup
    class TryParse_MethodGroup:
        def __getitem__(self, t:typing.Type[TryParse_1_T1]) -> TryParse_1[TryParse_1_T1]: ...

        TryParse_1_T1 = typing.TypeVar('TryParse_1_T1')
        class TryParse_1(typing.Generic[TryParse_1_T1]):
            TryParse_1_TEnum = Enum.TryParse_MethodGroup.TryParse_1_T1
            @typing.overload
            def __call__(self, value: ReadOnlySpan_1[str], result: clr.Reference[TryParse_1_TEnum]) -> bool:...
            @typing.overload
            def __call__(self, value: str, result: clr.Reference[TryParse_1_TEnum]) -> bool:...
            @typing.overload
            def __call__(self, value: ReadOnlySpan_1[str], ignoreCase: bool, result: clr.Reference[TryParse_1_TEnum]) -> bool:...
            @typing.overload
            def __call__(self, value: str, ignoreCase: bool, result: clr.Reference[TryParse_1_TEnum]) -> bool:...

        @typing.overload
        def __call__(self, enumType: typing.Type[typing.Any], value: ReadOnlySpan_1[str], result: clr.Reference[typing.Any]) -> bool:...
        @typing.overload
        def __call__(self, enumType: typing.Type[typing.Any], value: str, result: clr.Reference[typing.Any]) -> bool:...
        @typing.overload
        def __call__(self, enumType: typing.Type[typing.Any], value: ReadOnlySpan_1[str], ignoreCase: bool, result: clr.Reference[typing.Any]) -> bool:...
        @typing.overload
        def __call__(self, enumType: typing.Type[typing.Any], value: str, ignoreCase: bool, result: clr.Reference[typing.Any]) -> bool:...



class Environment(abc.ABC):
    @classmethod
    @property
    def CommandLine(cls) -> str: ...
    @classmethod
    @property
    def CurrentDirectory(cls) -> str: ...
    @classmethod
    @CurrentDirectory.setter
    def CurrentDirectory(cls, value: str) -> str: ...
    @classmethod
    @property
    def CurrentManagedThreadId(cls) -> int: ...
    @classmethod
    @property
    def ExitCode(cls) -> int: ...
    @classmethod
    @ExitCode.setter
    def ExitCode(cls, value: int) -> int: ...
    @classmethod
    @property
    def HasShutdownStarted(cls) -> bool: ...
    @classmethod
    @property
    def Is64BitOperatingSystem(cls) -> bool: ...
    @classmethod
    @property
    def Is64BitProcess(cls) -> bool: ...
    @classmethod
    @property
    def MachineName(cls) -> str: ...
    @classmethod
    @property
    def NewLine(cls) -> str: ...
    @classmethod
    @property
    def OSVersion(cls) -> OperatingSystem: ...
    @classmethod
    @property
    def ProcessId(cls) -> int: ...
    @classmethod
    @property
    def ProcessorCount(cls) -> int: ...
    @classmethod
    @property
    def ProcessPath(cls) -> str: ...
    @classmethod
    @property
    def StackTrace(cls) -> str: ...
    @classmethod
    @property
    def SystemDirectory(cls) -> str: ...
    @classmethod
    @property
    def SystemPageSize(cls) -> int: ...
    @classmethod
    @property
    def TickCount(cls) -> int: ...
    @classmethod
    @property
    def TickCount64(cls) -> int: ...
    @classmethod
    @property
    def UserDomainName(cls) -> str: ...
    @classmethod
    @property
    def UserInteractive(cls) -> bool: ...
    @classmethod
    @property
    def UserName(cls) -> str: ...
    @classmethod
    @property
    def Version(cls) -> Version: ...
    @classmethod
    @property
    def WorkingSet(cls) -> int: ...
    @staticmethod
    def Exit(exitCode: int) -> None: ...
    @staticmethod
    def ExpandEnvironmentVariables(name: str) -> str: ...
    @staticmethod
    def GetCommandLineArgs() -> Array_1[str]: ...
    @staticmethod
    def GetLogicalDrives() -> Array_1[str]: ...
    # Skipped FailFast due to it being static, abstract and generic.

    FailFast : FailFast_MethodGroup
    class FailFast_MethodGroup:
        @typing.overload
        def __call__(self, message: str) -> None:...
        @typing.overload
        def __call__(self, message: str, exception: Exception) -> None:...
        @typing.overload
        def __call__(self, message: str, exception: Exception, errorMessage: str) -> None:...

    # Skipped GetEnvironmentVariable due to it being static, abstract and generic.

    GetEnvironmentVariable : GetEnvironmentVariable_MethodGroup
    class GetEnvironmentVariable_MethodGroup:
        @typing.overload
        def __call__(self, variable: str) -> str:...
        @typing.overload
        def __call__(self, variable: str, target: EnvironmentVariableTarget) -> str:...

    # Skipped GetEnvironmentVariables due to it being static, abstract and generic.

    GetEnvironmentVariables : GetEnvironmentVariables_MethodGroup
    class GetEnvironmentVariables_MethodGroup:
        @typing.overload
        def __call__(self) -> IDictionary:...
        @typing.overload
        def __call__(self, target: EnvironmentVariableTarget) -> IDictionary:...

    # Skipped GetFolderPath due to it being static, abstract and generic.

    GetFolderPath : GetFolderPath_MethodGroup
    class GetFolderPath_MethodGroup:
        @typing.overload
        def __call__(self, folder: Environment.SpecialFolder) -> str:...
        @typing.overload
        def __call__(self, folder: Environment.SpecialFolder, option: Environment.SpecialFolderOption) -> str:...

    # Skipped SetEnvironmentVariable due to it being static, abstract and generic.

    SetEnvironmentVariable : SetEnvironmentVariable_MethodGroup
    class SetEnvironmentVariable_MethodGroup:
        @typing.overload
        def __call__(self, variable: str, value: str) -> None:...
        @typing.overload
        def __call__(self, variable: str, value: str, target: EnvironmentVariableTarget) -> None:...


    class SpecialFolder(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        Desktop : Environment.SpecialFolder # 0
        Programs : Environment.SpecialFolder # 2
        MyDocuments : Environment.SpecialFolder # 5
        Personal : Environment.SpecialFolder # 5
        Favorites : Environment.SpecialFolder # 6
        Startup : Environment.SpecialFolder # 7
        Recent : Environment.SpecialFolder # 8
        SendTo : Environment.SpecialFolder # 9
        StartMenu : Environment.SpecialFolder # 11
        MyMusic : Environment.SpecialFolder # 13
        MyVideos : Environment.SpecialFolder # 14
        DesktopDirectory : Environment.SpecialFolder # 16
        MyComputer : Environment.SpecialFolder # 17
        NetworkShortcuts : Environment.SpecialFolder # 19
        Fonts : Environment.SpecialFolder # 20
        Templates : Environment.SpecialFolder # 21
        CommonStartMenu : Environment.SpecialFolder # 22
        CommonPrograms : Environment.SpecialFolder # 23
        CommonStartup : Environment.SpecialFolder # 24
        CommonDesktopDirectory : Environment.SpecialFolder # 25
        ApplicationData : Environment.SpecialFolder # 26
        PrinterShortcuts : Environment.SpecialFolder # 27
        LocalApplicationData : Environment.SpecialFolder # 28
        InternetCache : Environment.SpecialFolder # 32
        Cookies : Environment.SpecialFolder # 33
        History : Environment.SpecialFolder # 34
        CommonApplicationData : Environment.SpecialFolder # 35
        Windows : Environment.SpecialFolder # 36
        System : Environment.SpecialFolder # 37
        ProgramFiles : Environment.SpecialFolder # 38
        MyPictures : Environment.SpecialFolder # 39
        UserProfile : Environment.SpecialFolder # 40
        SystemX86 : Environment.SpecialFolder # 41
        ProgramFilesX86 : Environment.SpecialFolder # 42
        CommonProgramFiles : Environment.SpecialFolder # 43
        CommonProgramFilesX86 : Environment.SpecialFolder # 44
        CommonTemplates : Environment.SpecialFolder # 45
        CommonDocuments : Environment.SpecialFolder # 46
        CommonAdminTools : Environment.SpecialFolder # 47
        AdminTools : Environment.SpecialFolder # 48
        CommonMusic : Environment.SpecialFolder # 53
        CommonPictures : Environment.SpecialFolder # 54
        CommonVideos : Environment.SpecialFolder # 55
        Resources : Environment.SpecialFolder # 56
        LocalizedResources : Environment.SpecialFolder # 57
        CommonOemLinks : Environment.SpecialFolder # 58
        CDBurning : Environment.SpecialFolder # 59


    class SpecialFolderOption(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        None_ : Environment.SpecialFolderOption # 0
        DoNotVerify : Environment.SpecialFolderOption # 16384
        Create : Environment.SpecialFolderOption # 32768



class EnvironmentVariableTarget(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Process : EnvironmentVariableTarget # 0
    User : EnvironmentVariableTarget # 1
    Machine : EnvironmentVariableTarget # 2


class EventArgs:
    def __init__(self) -> None: ...
    Empty : EventArgs


class EventHandler_GenericClasses(abc.ABCMeta):
    Generic_EventHandler_GenericClasses_EventHandler_1_TEventArgs = typing.TypeVar('Generic_EventHandler_GenericClasses_EventHandler_1_TEventArgs')
    def __getitem__(self, types : typing.Type[Generic_EventHandler_GenericClasses_EventHandler_1_TEventArgs]) -> typing.Type[EventHandler_1[Generic_EventHandler_GenericClasses_EventHandler_1_TEventArgs]]: ...

class EventHandler(EventHandler_0, metaclass =EventHandler_GenericClasses): ...

class EventHandler_0(MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, sender: typing.Any, e: EventArgs, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: typing.Any, e: EventArgs) -> None: ...


EventHandler_1_TEventArgs = typing.TypeVar('EventHandler_1_TEventArgs')
class EventHandler_1(typing.Generic[EventHandler_1_TEventArgs], MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, sender: typing.Any, e: EventHandler_1_TEventArgs, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: typing.Any, e: EventHandler_1_TEventArgs) -> None: ...


class Exception(ISerializable):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, innerException: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...
    def GetBaseException(self) -> Exception: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...
    def GetType(self) -> typing.Type[typing.Any]: ...
    def ToString(self) -> str: ...


class ExecutionEngineException(SystemException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, innerException: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...


class FieldAccessException(MemberAccessException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, inner: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...


class FlagsAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class FormatException(SystemException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, innerException: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...


class FormattableString(IFormattable, abc.ABC):
    @property
    def ArgumentCount(self) -> int: ...
    @property
    def Format(self) -> str: ...
    @staticmethod
    def CurrentCulture(formattable: FormattableString) -> str: ...
    @abc.abstractmethod
    def GetArgument(self, index: int) -> typing.Any: ...
    @abc.abstractmethod
    def GetArguments(self) -> Array_1[typing.Any]: ...
    @staticmethod
    def Invariant(formattable: FormattableString) -> str: ...
    # Skipped ToString due to it being static, abstract and generic.

    ToString : ToString_MethodGroup
    class ToString_MethodGroup:
        @typing.overload
        def __call__(self) -> str:...
        @typing.overload
        def __call__(self, formatProvider: IFormatProvider) -> str:...



class Func_GenericClasses(abc.ABCMeta):
    Generic_Func_GenericClasses_Func_1_TResult = typing.TypeVar('Generic_Func_GenericClasses_Func_1_TResult')
    @typing.overload
    def __getitem__(self, types : typing.Type[Generic_Func_GenericClasses_Func_1_TResult]) -> typing.Type[Func_1[Generic_Func_GenericClasses_Func_1_TResult]]: ...
    Generic_Func_GenericClasses_Func_10_T1 = typing.TypeVar('Generic_Func_GenericClasses_Func_10_T1')
    Generic_Func_GenericClasses_Func_10_T2 = typing.TypeVar('Generic_Func_GenericClasses_Func_10_T2')
    Generic_Func_GenericClasses_Func_10_T3 = typing.TypeVar('Generic_Func_GenericClasses_Func_10_T3')
    Generic_Func_GenericClasses_Func_10_T4 = typing.TypeVar('Generic_Func_GenericClasses_Func_10_T4')
    Generic_Func_GenericClasses_Func_10_T5 = typing.TypeVar('Generic_Func_GenericClasses_Func_10_T5')
    Generic_Func_GenericClasses_Func_10_T6 = typing.TypeVar('Generic_Func_GenericClasses_Func_10_T6')
    Generic_Func_GenericClasses_Func_10_T7 = typing.TypeVar('Generic_Func_GenericClasses_Func_10_T7')
    Generic_Func_GenericClasses_Func_10_T8 = typing.TypeVar('Generic_Func_GenericClasses_Func_10_T8')
    Generic_Func_GenericClasses_Func_10_T9 = typing.TypeVar('Generic_Func_GenericClasses_Func_10_T9')
    Generic_Func_GenericClasses_Func_10_TResult = typing.TypeVar('Generic_Func_GenericClasses_Func_10_TResult')
    @typing.overload
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_Func_GenericClasses_Func_10_T1], typing.Type[Generic_Func_GenericClasses_Func_10_T2], typing.Type[Generic_Func_GenericClasses_Func_10_T3], typing.Type[Generic_Func_GenericClasses_Func_10_T4], typing.Type[Generic_Func_GenericClasses_Func_10_T5], typing.Type[Generic_Func_GenericClasses_Func_10_T6], typing.Type[Generic_Func_GenericClasses_Func_10_T7], typing.Type[Generic_Func_GenericClasses_Func_10_T8], typing.Type[Generic_Func_GenericClasses_Func_10_T9], typing.Type[Generic_Func_GenericClasses_Func_10_TResult]]) -> typing.Type[Func_10[Generic_Func_GenericClasses_Func_10_T1, Generic_Func_GenericClasses_Func_10_T2, Generic_Func_GenericClasses_Func_10_T3, Generic_Func_GenericClasses_Func_10_T4, Generic_Func_GenericClasses_Func_10_T5, Generic_Func_GenericClasses_Func_10_T6, Generic_Func_GenericClasses_Func_10_T7, Generic_Func_GenericClasses_Func_10_T8, Generic_Func_GenericClasses_Func_10_T9, Generic_Func_GenericClasses_Func_10_TResult]]: ...
    Generic_Func_GenericClasses_Func_11_T1 = typing.TypeVar('Generic_Func_GenericClasses_Func_11_T1')
    Generic_Func_GenericClasses_Func_11_T2 = typing.TypeVar('Generic_Func_GenericClasses_Func_11_T2')
    Generic_Func_GenericClasses_Func_11_T3 = typing.TypeVar('Generic_Func_GenericClasses_Func_11_T3')
    Generic_Func_GenericClasses_Func_11_T4 = typing.TypeVar('Generic_Func_GenericClasses_Func_11_T4')
    Generic_Func_GenericClasses_Func_11_T5 = typing.TypeVar('Generic_Func_GenericClasses_Func_11_T5')
    Generic_Func_GenericClasses_Func_11_T6 = typing.TypeVar('Generic_Func_GenericClasses_Func_11_T6')
    Generic_Func_GenericClasses_Func_11_T7 = typing.TypeVar('Generic_Func_GenericClasses_Func_11_T7')
    Generic_Func_GenericClasses_Func_11_T8 = typing.TypeVar('Generic_Func_GenericClasses_Func_11_T8')
    Generic_Func_GenericClasses_Func_11_T9 = typing.TypeVar('Generic_Func_GenericClasses_Func_11_T9')
    Generic_Func_GenericClasses_Func_11_T10 = typing.TypeVar('Generic_Func_GenericClasses_Func_11_T10')
    Generic_Func_GenericClasses_Func_11_TResult = typing.TypeVar('Generic_Func_GenericClasses_Func_11_TResult')
    @typing.overload
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_Func_GenericClasses_Func_11_T1], typing.Type[Generic_Func_GenericClasses_Func_11_T2], typing.Type[Generic_Func_GenericClasses_Func_11_T3], typing.Type[Generic_Func_GenericClasses_Func_11_T4], typing.Type[Generic_Func_GenericClasses_Func_11_T5], typing.Type[Generic_Func_GenericClasses_Func_11_T6], typing.Type[Generic_Func_GenericClasses_Func_11_T7], typing.Type[Generic_Func_GenericClasses_Func_11_T8], typing.Type[Generic_Func_GenericClasses_Func_11_T9], typing.Type[Generic_Func_GenericClasses_Func_11_T10], typing.Type[Generic_Func_GenericClasses_Func_11_TResult]]) -> typing.Type[Func_11[Generic_Func_GenericClasses_Func_11_T1, Generic_Func_GenericClasses_Func_11_T2, Generic_Func_GenericClasses_Func_11_T3, Generic_Func_GenericClasses_Func_11_T4, Generic_Func_GenericClasses_Func_11_T5, Generic_Func_GenericClasses_Func_11_T6, Generic_Func_GenericClasses_Func_11_T7, Generic_Func_GenericClasses_Func_11_T8, Generic_Func_GenericClasses_Func_11_T9, Generic_Func_GenericClasses_Func_11_T10, Generic_Func_GenericClasses_Func_11_TResult]]: ...
    Generic_Func_GenericClasses_Func_12_T1 = typing.TypeVar('Generic_Func_GenericClasses_Func_12_T1')
    Generic_Func_GenericClasses_Func_12_T2 = typing.TypeVar('Generic_Func_GenericClasses_Func_12_T2')
    Generic_Func_GenericClasses_Func_12_T3 = typing.TypeVar('Generic_Func_GenericClasses_Func_12_T3')
    Generic_Func_GenericClasses_Func_12_T4 = typing.TypeVar('Generic_Func_GenericClasses_Func_12_T4')
    Generic_Func_GenericClasses_Func_12_T5 = typing.TypeVar('Generic_Func_GenericClasses_Func_12_T5')
    Generic_Func_GenericClasses_Func_12_T6 = typing.TypeVar('Generic_Func_GenericClasses_Func_12_T6')
    Generic_Func_GenericClasses_Func_12_T7 = typing.TypeVar('Generic_Func_GenericClasses_Func_12_T7')
    Generic_Func_GenericClasses_Func_12_T8 = typing.TypeVar('Generic_Func_GenericClasses_Func_12_T8')
    Generic_Func_GenericClasses_Func_12_T9 = typing.TypeVar('Generic_Func_GenericClasses_Func_12_T9')
    Generic_Func_GenericClasses_Func_12_T10 = typing.TypeVar('Generic_Func_GenericClasses_Func_12_T10')
    Generic_Func_GenericClasses_Func_12_T11 = typing.TypeVar('Generic_Func_GenericClasses_Func_12_T11')
    Generic_Func_GenericClasses_Func_12_TResult = typing.TypeVar('Generic_Func_GenericClasses_Func_12_TResult')
    @typing.overload
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_Func_GenericClasses_Func_12_T1], typing.Type[Generic_Func_GenericClasses_Func_12_T2], typing.Type[Generic_Func_GenericClasses_Func_12_T3], typing.Type[Generic_Func_GenericClasses_Func_12_T4], typing.Type[Generic_Func_GenericClasses_Func_12_T5], typing.Type[Generic_Func_GenericClasses_Func_12_T6], typing.Type[Generic_Func_GenericClasses_Func_12_T7], typing.Type[Generic_Func_GenericClasses_Func_12_T8], typing.Type[Generic_Func_GenericClasses_Func_12_T9], typing.Type[Generic_Func_GenericClasses_Func_12_T10], typing.Type[Generic_Func_GenericClasses_Func_12_T11], typing.Type[Generic_Func_GenericClasses_Func_12_TResult]]) -> typing.Type[Func_12[Generic_Func_GenericClasses_Func_12_T1, Generic_Func_GenericClasses_Func_12_T2, Generic_Func_GenericClasses_Func_12_T3, Generic_Func_GenericClasses_Func_12_T4, Generic_Func_GenericClasses_Func_12_T5, Generic_Func_GenericClasses_Func_12_T6, Generic_Func_GenericClasses_Func_12_T7, Generic_Func_GenericClasses_Func_12_T8, Generic_Func_GenericClasses_Func_12_T9, Generic_Func_GenericClasses_Func_12_T10, Generic_Func_GenericClasses_Func_12_T11, Generic_Func_GenericClasses_Func_12_TResult]]: ...
    Generic_Func_GenericClasses_Func_13_T1 = typing.TypeVar('Generic_Func_GenericClasses_Func_13_T1')
    Generic_Func_GenericClasses_Func_13_T2 = typing.TypeVar('Generic_Func_GenericClasses_Func_13_T2')
    Generic_Func_GenericClasses_Func_13_T3 = typing.TypeVar('Generic_Func_GenericClasses_Func_13_T3')
    Generic_Func_GenericClasses_Func_13_T4 = typing.TypeVar('Generic_Func_GenericClasses_Func_13_T4')
    Generic_Func_GenericClasses_Func_13_T5 = typing.TypeVar('Generic_Func_GenericClasses_Func_13_T5')
    Generic_Func_GenericClasses_Func_13_T6 = typing.TypeVar('Generic_Func_GenericClasses_Func_13_T6')
    Generic_Func_GenericClasses_Func_13_T7 = typing.TypeVar('Generic_Func_GenericClasses_Func_13_T7')
    Generic_Func_GenericClasses_Func_13_T8 = typing.TypeVar('Generic_Func_GenericClasses_Func_13_T8')
    Generic_Func_GenericClasses_Func_13_T9 = typing.TypeVar('Generic_Func_GenericClasses_Func_13_T9')
    Generic_Func_GenericClasses_Func_13_T10 = typing.TypeVar('Generic_Func_GenericClasses_Func_13_T10')
    Generic_Func_GenericClasses_Func_13_T11 = typing.TypeVar('Generic_Func_GenericClasses_Func_13_T11')
    Generic_Func_GenericClasses_Func_13_T12 = typing.TypeVar('Generic_Func_GenericClasses_Func_13_T12')
    Generic_Func_GenericClasses_Func_13_TResult = typing.TypeVar('Generic_Func_GenericClasses_Func_13_TResult')
    @typing.overload
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_Func_GenericClasses_Func_13_T1], typing.Type[Generic_Func_GenericClasses_Func_13_T2], typing.Type[Generic_Func_GenericClasses_Func_13_T3], typing.Type[Generic_Func_GenericClasses_Func_13_T4], typing.Type[Generic_Func_GenericClasses_Func_13_T5], typing.Type[Generic_Func_GenericClasses_Func_13_T6], typing.Type[Generic_Func_GenericClasses_Func_13_T7], typing.Type[Generic_Func_GenericClasses_Func_13_T8], typing.Type[Generic_Func_GenericClasses_Func_13_T9], typing.Type[Generic_Func_GenericClasses_Func_13_T10], typing.Type[Generic_Func_GenericClasses_Func_13_T11], typing.Type[Generic_Func_GenericClasses_Func_13_T12], typing.Type[Generic_Func_GenericClasses_Func_13_TResult]]) -> typing.Type[Func_13[Generic_Func_GenericClasses_Func_13_T1, Generic_Func_GenericClasses_Func_13_T2, Generic_Func_GenericClasses_Func_13_T3, Generic_Func_GenericClasses_Func_13_T4, Generic_Func_GenericClasses_Func_13_T5, Generic_Func_GenericClasses_Func_13_T6, Generic_Func_GenericClasses_Func_13_T7, Generic_Func_GenericClasses_Func_13_T8, Generic_Func_GenericClasses_Func_13_T9, Generic_Func_GenericClasses_Func_13_T10, Generic_Func_GenericClasses_Func_13_T11, Generic_Func_GenericClasses_Func_13_T12, Generic_Func_GenericClasses_Func_13_TResult]]: ...
    Generic_Func_GenericClasses_Func_14_T1 = typing.TypeVar('Generic_Func_GenericClasses_Func_14_T1')
    Generic_Func_GenericClasses_Func_14_T2 = typing.TypeVar('Generic_Func_GenericClasses_Func_14_T2')
    Generic_Func_GenericClasses_Func_14_T3 = typing.TypeVar('Generic_Func_GenericClasses_Func_14_T3')
    Generic_Func_GenericClasses_Func_14_T4 = typing.TypeVar('Generic_Func_GenericClasses_Func_14_T4')
    Generic_Func_GenericClasses_Func_14_T5 = typing.TypeVar('Generic_Func_GenericClasses_Func_14_T5')
    Generic_Func_GenericClasses_Func_14_T6 = typing.TypeVar('Generic_Func_GenericClasses_Func_14_T6')
    Generic_Func_GenericClasses_Func_14_T7 = typing.TypeVar('Generic_Func_GenericClasses_Func_14_T7')
    Generic_Func_GenericClasses_Func_14_T8 = typing.TypeVar('Generic_Func_GenericClasses_Func_14_T8')
    Generic_Func_GenericClasses_Func_14_T9 = typing.TypeVar('Generic_Func_GenericClasses_Func_14_T9')
    Generic_Func_GenericClasses_Func_14_T10 = typing.TypeVar('Generic_Func_GenericClasses_Func_14_T10')
    Generic_Func_GenericClasses_Func_14_T11 = typing.TypeVar('Generic_Func_GenericClasses_Func_14_T11')
    Generic_Func_GenericClasses_Func_14_T12 = typing.TypeVar('Generic_Func_GenericClasses_Func_14_T12')
    Generic_Func_GenericClasses_Func_14_T13 = typing.TypeVar('Generic_Func_GenericClasses_Func_14_T13')
    Generic_Func_GenericClasses_Func_14_TResult = typing.TypeVar('Generic_Func_GenericClasses_Func_14_TResult')
    @typing.overload
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_Func_GenericClasses_Func_14_T1], typing.Type[Generic_Func_GenericClasses_Func_14_T2], typing.Type[Generic_Func_GenericClasses_Func_14_T3], typing.Type[Generic_Func_GenericClasses_Func_14_T4], typing.Type[Generic_Func_GenericClasses_Func_14_T5], typing.Type[Generic_Func_GenericClasses_Func_14_T6], typing.Type[Generic_Func_GenericClasses_Func_14_T7], typing.Type[Generic_Func_GenericClasses_Func_14_T8], typing.Type[Generic_Func_GenericClasses_Func_14_T9], typing.Type[Generic_Func_GenericClasses_Func_14_T10], typing.Type[Generic_Func_GenericClasses_Func_14_T11], typing.Type[Generic_Func_GenericClasses_Func_14_T12], typing.Type[Generic_Func_GenericClasses_Func_14_T13], typing.Type[Generic_Func_GenericClasses_Func_14_TResult]]) -> typing.Type[Func_14[Generic_Func_GenericClasses_Func_14_T1, Generic_Func_GenericClasses_Func_14_T2, Generic_Func_GenericClasses_Func_14_T3, Generic_Func_GenericClasses_Func_14_T4, Generic_Func_GenericClasses_Func_14_T5, Generic_Func_GenericClasses_Func_14_T6, Generic_Func_GenericClasses_Func_14_T7, Generic_Func_GenericClasses_Func_14_T8, Generic_Func_GenericClasses_Func_14_T9, Generic_Func_GenericClasses_Func_14_T10, Generic_Func_GenericClasses_Func_14_T11, Generic_Func_GenericClasses_Func_14_T12, Generic_Func_GenericClasses_Func_14_T13, Generic_Func_GenericClasses_Func_14_TResult]]: ...
    Generic_Func_GenericClasses_Func_15_T1 = typing.TypeVar('Generic_Func_GenericClasses_Func_15_T1')
    Generic_Func_GenericClasses_Func_15_T2 = typing.TypeVar('Generic_Func_GenericClasses_Func_15_T2')
    Generic_Func_GenericClasses_Func_15_T3 = typing.TypeVar('Generic_Func_GenericClasses_Func_15_T3')
    Generic_Func_GenericClasses_Func_15_T4 = typing.TypeVar('Generic_Func_GenericClasses_Func_15_T4')
    Generic_Func_GenericClasses_Func_15_T5 = typing.TypeVar('Generic_Func_GenericClasses_Func_15_T5')
    Generic_Func_GenericClasses_Func_15_T6 = typing.TypeVar('Generic_Func_GenericClasses_Func_15_T6')
    Generic_Func_GenericClasses_Func_15_T7 = typing.TypeVar('Generic_Func_GenericClasses_Func_15_T7')
    Generic_Func_GenericClasses_Func_15_T8 = typing.TypeVar('Generic_Func_GenericClasses_Func_15_T8')
    Generic_Func_GenericClasses_Func_15_T9 = typing.TypeVar('Generic_Func_GenericClasses_Func_15_T9')
    Generic_Func_GenericClasses_Func_15_T10 = typing.TypeVar('Generic_Func_GenericClasses_Func_15_T10')
    Generic_Func_GenericClasses_Func_15_T11 = typing.TypeVar('Generic_Func_GenericClasses_Func_15_T11')
    Generic_Func_GenericClasses_Func_15_T12 = typing.TypeVar('Generic_Func_GenericClasses_Func_15_T12')
    Generic_Func_GenericClasses_Func_15_T13 = typing.TypeVar('Generic_Func_GenericClasses_Func_15_T13')
    Generic_Func_GenericClasses_Func_15_T14 = typing.TypeVar('Generic_Func_GenericClasses_Func_15_T14')
    Generic_Func_GenericClasses_Func_15_TResult = typing.TypeVar('Generic_Func_GenericClasses_Func_15_TResult')
    @typing.overload
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_Func_GenericClasses_Func_15_T1], typing.Type[Generic_Func_GenericClasses_Func_15_T2], typing.Type[Generic_Func_GenericClasses_Func_15_T3], typing.Type[Generic_Func_GenericClasses_Func_15_T4], typing.Type[Generic_Func_GenericClasses_Func_15_T5], typing.Type[Generic_Func_GenericClasses_Func_15_T6], typing.Type[Generic_Func_GenericClasses_Func_15_T7], typing.Type[Generic_Func_GenericClasses_Func_15_T8], typing.Type[Generic_Func_GenericClasses_Func_15_T9], typing.Type[Generic_Func_GenericClasses_Func_15_T10], typing.Type[Generic_Func_GenericClasses_Func_15_T11], typing.Type[Generic_Func_GenericClasses_Func_15_T12], typing.Type[Generic_Func_GenericClasses_Func_15_T13], typing.Type[Generic_Func_GenericClasses_Func_15_T14], typing.Type[Generic_Func_GenericClasses_Func_15_TResult]]) -> typing.Type[Func_15[Generic_Func_GenericClasses_Func_15_T1, Generic_Func_GenericClasses_Func_15_T2, Generic_Func_GenericClasses_Func_15_T3, Generic_Func_GenericClasses_Func_15_T4, Generic_Func_GenericClasses_Func_15_T5, Generic_Func_GenericClasses_Func_15_T6, Generic_Func_GenericClasses_Func_15_T7, Generic_Func_GenericClasses_Func_15_T8, Generic_Func_GenericClasses_Func_15_T9, Generic_Func_GenericClasses_Func_15_T10, Generic_Func_GenericClasses_Func_15_T11, Generic_Func_GenericClasses_Func_15_T12, Generic_Func_GenericClasses_Func_15_T13, Generic_Func_GenericClasses_Func_15_T14, Generic_Func_GenericClasses_Func_15_TResult]]: ...
    Generic_Func_GenericClasses_Func_16_T1 = typing.TypeVar('Generic_Func_GenericClasses_Func_16_T1')
    Generic_Func_GenericClasses_Func_16_T2 = typing.TypeVar('Generic_Func_GenericClasses_Func_16_T2')
    Generic_Func_GenericClasses_Func_16_T3 = typing.TypeVar('Generic_Func_GenericClasses_Func_16_T3')
    Generic_Func_GenericClasses_Func_16_T4 = typing.TypeVar('Generic_Func_GenericClasses_Func_16_T4')
    Generic_Func_GenericClasses_Func_16_T5 = typing.TypeVar('Generic_Func_GenericClasses_Func_16_T5')
    Generic_Func_GenericClasses_Func_16_T6 = typing.TypeVar('Generic_Func_GenericClasses_Func_16_T6')
    Generic_Func_GenericClasses_Func_16_T7 = typing.TypeVar('Generic_Func_GenericClasses_Func_16_T7')
    Generic_Func_GenericClasses_Func_16_T8 = typing.TypeVar('Generic_Func_GenericClasses_Func_16_T8')
    Generic_Func_GenericClasses_Func_16_T9 = typing.TypeVar('Generic_Func_GenericClasses_Func_16_T9')
    Generic_Func_GenericClasses_Func_16_T10 = typing.TypeVar('Generic_Func_GenericClasses_Func_16_T10')
    Generic_Func_GenericClasses_Func_16_T11 = typing.TypeVar('Generic_Func_GenericClasses_Func_16_T11')
    Generic_Func_GenericClasses_Func_16_T12 = typing.TypeVar('Generic_Func_GenericClasses_Func_16_T12')
    Generic_Func_GenericClasses_Func_16_T13 = typing.TypeVar('Generic_Func_GenericClasses_Func_16_T13')
    Generic_Func_GenericClasses_Func_16_T14 = typing.TypeVar('Generic_Func_GenericClasses_Func_16_T14')
    Generic_Func_GenericClasses_Func_16_T15 = typing.TypeVar('Generic_Func_GenericClasses_Func_16_T15')
    Generic_Func_GenericClasses_Func_16_TResult = typing.TypeVar('Generic_Func_GenericClasses_Func_16_TResult')
    @typing.overload
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_Func_GenericClasses_Func_16_T1], typing.Type[Generic_Func_GenericClasses_Func_16_T2], typing.Type[Generic_Func_GenericClasses_Func_16_T3], typing.Type[Generic_Func_GenericClasses_Func_16_T4], typing.Type[Generic_Func_GenericClasses_Func_16_T5], typing.Type[Generic_Func_GenericClasses_Func_16_T6], typing.Type[Generic_Func_GenericClasses_Func_16_T7], typing.Type[Generic_Func_GenericClasses_Func_16_T8], typing.Type[Generic_Func_GenericClasses_Func_16_T9], typing.Type[Generic_Func_GenericClasses_Func_16_T10], typing.Type[Generic_Func_GenericClasses_Func_16_T11], typing.Type[Generic_Func_GenericClasses_Func_16_T12], typing.Type[Generic_Func_GenericClasses_Func_16_T13], typing.Type[Generic_Func_GenericClasses_Func_16_T14], typing.Type[Generic_Func_GenericClasses_Func_16_T15], typing.Type[Generic_Func_GenericClasses_Func_16_TResult]]) -> typing.Type[Func_16[Generic_Func_GenericClasses_Func_16_T1, Generic_Func_GenericClasses_Func_16_T2, Generic_Func_GenericClasses_Func_16_T3, Generic_Func_GenericClasses_Func_16_T4, Generic_Func_GenericClasses_Func_16_T5, Generic_Func_GenericClasses_Func_16_T6, Generic_Func_GenericClasses_Func_16_T7, Generic_Func_GenericClasses_Func_16_T8, Generic_Func_GenericClasses_Func_16_T9, Generic_Func_GenericClasses_Func_16_T10, Generic_Func_GenericClasses_Func_16_T11, Generic_Func_GenericClasses_Func_16_T12, Generic_Func_GenericClasses_Func_16_T13, Generic_Func_GenericClasses_Func_16_T14, Generic_Func_GenericClasses_Func_16_T15, Generic_Func_GenericClasses_Func_16_TResult]]: ...
    Generic_Func_GenericClasses_Func_17_T1 = typing.TypeVar('Generic_Func_GenericClasses_Func_17_T1')
    Generic_Func_GenericClasses_Func_17_T2 = typing.TypeVar('Generic_Func_GenericClasses_Func_17_T2')
    Generic_Func_GenericClasses_Func_17_T3 = typing.TypeVar('Generic_Func_GenericClasses_Func_17_T3')
    Generic_Func_GenericClasses_Func_17_T4 = typing.TypeVar('Generic_Func_GenericClasses_Func_17_T4')
    Generic_Func_GenericClasses_Func_17_T5 = typing.TypeVar('Generic_Func_GenericClasses_Func_17_T5')
    Generic_Func_GenericClasses_Func_17_T6 = typing.TypeVar('Generic_Func_GenericClasses_Func_17_T6')
    Generic_Func_GenericClasses_Func_17_T7 = typing.TypeVar('Generic_Func_GenericClasses_Func_17_T7')
    Generic_Func_GenericClasses_Func_17_T8 = typing.TypeVar('Generic_Func_GenericClasses_Func_17_T8')
    Generic_Func_GenericClasses_Func_17_T9 = typing.TypeVar('Generic_Func_GenericClasses_Func_17_T9')
    Generic_Func_GenericClasses_Func_17_T10 = typing.TypeVar('Generic_Func_GenericClasses_Func_17_T10')
    Generic_Func_GenericClasses_Func_17_T11 = typing.TypeVar('Generic_Func_GenericClasses_Func_17_T11')
    Generic_Func_GenericClasses_Func_17_T12 = typing.TypeVar('Generic_Func_GenericClasses_Func_17_T12')
    Generic_Func_GenericClasses_Func_17_T13 = typing.TypeVar('Generic_Func_GenericClasses_Func_17_T13')
    Generic_Func_GenericClasses_Func_17_T14 = typing.TypeVar('Generic_Func_GenericClasses_Func_17_T14')
    Generic_Func_GenericClasses_Func_17_T15 = typing.TypeVar('Generic_Func_GenericClasses_Func_17_T15')
    Generic_Func_GenericClasses_Func_17_T16 = typing.TypeVar('Generic_Func_GenericClasses_Func_17_T16')
    Generic_Func_GenericClasses_Func_17_TResult = typing.TypeVar('Generic_Func_GenericClasses_Func_17_TResult')
    @typing.overload
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_Func_GenericClasses_Func_17_T1], typing.Type[Generic_Func_GenericClasses_Func_17_T2], typing.Type[Generic_Func_GenericClasses_Func_17_T3], typing.Type[Generic_Func_GenericClasses_Func_17_T4], typing.Type[Generic_Func_GenericClasses_Func_17_T5], typing.Type[Generic_Func_GenericClasses_Func_17_T6], typing.Type[Generic_Func_GenericClasses_Func_17_T7], typing.Type[Generic_Func_GenericClasses_Func_17_T8], typing.Type[Generic_Func_GenericClasses_Func_17_T9], typing.Type[Generic_Func_GenericClasses_Func_17_T10], typing.Type[Generic_Func_GenericClasses_Func_17_T11], typing.Type[Generic_Func_GenericClasses_Func_17_T12], typing.Type[Generic_Func_GenericClasses_Func_17_T13], typing.Type[Generic_Func_GenericClasses_Func_17_T14], typing.Type[Generic_Func_GenericClasses_Func_17_T15], typing.Type[Generic_Func_GenericClasses_Func_17_T16], typing.Type[Generic_Func_GenericClasses_Func_17_TResult]]) -> typing.Type[Func_17[Generic_Func_GenericClasses_Func_17_T1, Generic_Func_GenericClasses_Func_17_T2, Generic_Func_GenericClasses_Func_17_T3, Generic_Func_GenericClasses_Func_17_T4, Generic_Func_GenericClasses_Func_17_T5, Generic_Func_GenericClasses_Func_17_T6, Generic_Func_GenericClasses_Func_17_T7, Generic_Func_GenericClasses_Func_17_T8, Generic_Func_GenericClasses_Func_17_T9, Generic_Func_GenericClasses_Func_17_T10, Generic_Func_GenericClasses_Func_17_T11, Generic_Func_GenericClasses_Func_17_T12, Generic_Func_GenericClasses_Func_17_T13, Generic_Func_GenericClasses_Func_17_T14, Generic_Func_GenericClasses_Func_17_T15, Generic_Func_GenericClasses_Func_17_T16, Generic_Func_GenericClasses_Func_17_TResult]]: ...
    Generic_Func_GenericClasses_Func_2_T = typing.TypeVar('Generic_Func_GenericClasses_Func_2_T')
    Generic_Func_GenericClasses_Func_2_TResult = typing.TypeVar('Generic_Func_GenericClasses_Func_2_TResult')
    @typing.overload
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_Func_GenericClasses_Func_2_T], typing.Type[Generic_Func_GenericClasses_Func_2_TResult]]) -> typing.Type[Func_2[Generic_Func_GenericClasses_Func_2_T, Generic_Func_GenericClasses_Func_2_TResult]]: ...
    Generic_Func_GenericClasses_Func_3_T1 = typing.TypeVar('Generic_Func_GenericClasses_Func_3_T1')
    Generic_Func_GenericClasses_Func_3_T2 = typing.TypeVar('Generic_Func_GenericClasses_Func_3_T2')
    Generic_Func_GenericClasses_Func_3_TResult = typing.TypeVar('Generic_Func_GenericClasses_Func_3_TResult')
    @typing.overload
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_Func_GenericClasses_Func_3_T1], typing.Type[Generic_Func_GenericClasses_Func_3_T2], typing.Type[Generic_Func_GenericClasses_Func_3_TResult]]) -> typing.Type[Func_3[Generic_Func_GenericClasses_Func_3_T1, Generic_Func_GenericClasses_Func_3_T2, Generic_Func_GenericClasses_Func_3_TResult]]: ...
    Generic_Func_GenericClasses_Func_4_T1 = typing.TypeVar('Generic_Func_GenericClasses_Func_4_T1')
    Generic_Func_GenericClasses_Func_4_T2 = typing.TypeVar('Generic_Func_GenericClasses_Func_4_T2')
    Generic_Func_GenericClasses_Func_4_T3 = typing.TypeVar('Generic_Func_GenericClasses_Func_4_T3')
    Generic_Func_GenericClasses_Func_4_TResult = typing.TypeVar('Generic_Func_GenericClasses_Func_4_TResult')
    @typing.overload
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_Func_GenericClasses_Func_4_T1], typing.Type[Generic_Func_GenericClasses_Func_4_T2], typing.Type[Generic_Func_GenericClasses_Func_4_T3], typing.Type[Generic_Func_GenericClasses_Func_4_TResult]]) -> typing.Type[Func_4[Generic_Func_GenericClasses_Func_4_T1, Generic_Func_GenericClasses_Func_4_T2, Generic_Func_GenericClasses_Func_4_T3, Generic_Func_GenericClasses_Func_4_TResult]]: ...
    Generic_Func_GenericClasses_Func_5_T1 = typing.TypeVar('Generic_Func_GenericClasses_Func_5_T1')
    Generic_Func_GenericClasses_Func_5_T2 = typing.TypeVar('Generic_Func_GenericClasses_Func_5_T2')
    Generic_Func_GenericClasses_Func_5_T3 = typing.TypeVar('Generic_Func_GenericClasses_Func_5_T3')
    Generic_Func_GenericClasses_Func_5_T4 = typing.TypeVar('Generic_Func_GenericClasses_Func_5_T4')
    Generic_Func_GenericClasses_Func_5_TResult = typing.TypeVar('Generic_Func_GenericClasses_Func_5_TResult')
    @typing.overload
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_Func_GenericClasses_Func_5_T1], typing.Type[Generic_Func_GenericClasses_Func_5_T2], typing.Type[Generic_Func_GenericClasses_Func_5_T3], typing.Type[Generic_Func_GenericClasses_Func_5_T4], typing.Type[Generic_Func_GenericClasses_Func_5_TResult]]) -> typing.Type[Func_5[Generic_Func_GenericClasses_Func_5_T1, Generic_Func_GenericClasses_Func_5_T2, Generic_Func_GenericClasses_Func_5_T3, Generic_Func_GenericClasses_Func_5_T4, Generic_Func_GenericClasses_Func_5_TResult]]: ...
    Generic_Func_GenericClasses_Func_6_T1 = typing.TypeVar('Generic_Func_GenericClasses_Func_6_T1')
    Generic_Func_GenericClasses_Func_6_T2 = typing.TypeVar('Generic_Func_GenericClasses_Func_6_T2')
    Generic_Func_GenericClasses_Func_6_T3 = typing.TypeVar('Generic_Func_GenericClasses_Func_6_T3')
    Generic_Func_GenericClasses_Func_6_T4 = typing.TypeVar('Generic_Func_GenericClasses_Func_6_T4')
    Generic_Func_GenericClasses_Func_6_T5 = typing.TypeVar('Generic_Func_GenericClasses_Func_6_T5')
    Generic_Func_GenericClasses_Func_6_TResult = typing.TypeVar('Generic_Func_GenericClasses_Func_6_TResult')
    @typing.overload
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_Func_GenericClasses_Func_6_T1], typing.Type[Generic_Func_GenericClasses_Func_6_T2], typing.Type[Generic_Func_GenericClasses_Func_6_T3], typing.Type[Generic_Func_GenericClasses_Func_6_T4], typing.Type[Generic_Func_GenericClasses_Func_6_T5], typing.Type[Generic_Func_GenericClasses_Func_6_TResult]]) -> typing.Type[Func_6[Generic_Func_GenericClasses_Func_6_T1, Generic_Func_GenericClasses_Func_6_T2, Generic_Func_GenericClasses_Func_6_T3, Generic_Func_GenericClasses_Func_6_T4, Generic_Func_GenericClasses_Func_6_T5, Generic_Func_GenericClasses_Func_6_TResult]]: ...
    Generic_Func_GenericClasses_Func_7_T1 = typing.TypeVar('Generic_Func_GenericClasses_Func_7_T1')
    Generic_Func_GenericClasses_Func_7_T2 = typing.TypeVar('Generic_Func_GenericClasses_Func_7_T2')
    Generic_Func_GenericClasses_Func_7_T3 = typing.TypeVar('Generic_Func_GenericClasses_Func_7_T3')
    Generic_Func_GenericClasses_Func_7_T4 = typing.TypeVar('Generic_Func_GenericClasses_Func_7_T4')
    Generic_Func_GenericClasses_Func_7_T5 = typing.TypeVar('Generic_Func_GenericClasses_Func_7_T5')
    Generic_Func_GenericClasses_Func_7_T6 = typing.TypeVar('Generic_Func_GenericClasses_Func_7_T6')
    Generic_Func_GenericClasses_Func_7_TResult = typing.TypeVar('Generic_Func_GenericClasses_Func_7_TResult')
    @typing.overload
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_Func_GenericClasses_Func_7_T1], typing.Type[Generic_Func_GenericClasses_Func_7_T2], typing.Type[Generic_Func_GenericClasses_Func_7_T3], typing.Type[Generic_Func_GenericClasses_Func_7_T4], typing.Type[Generic_Func_GenericClasses_Func_7_T5], typing.Type[Generic_Func_GenericClasses_Func_7_T6], typing.Type[Generic_Func_GenericClasses_Func_7_TResult]]) -> typing.Type[Func_7[Generic_Func_GenericClasses_Func_7_T1, Generic_Func_GenericClasses_Func_7_T2, Generic_Func_GenericClasses_Func_7_T3, Generic_Func_GenericClasses_Func_7_T4, Generic_Func_GenericClasses_Func_7_T5, Generic_Func_GenericClasses_Func_7_T6, Generic_Func_GenericClasses_Func_7_TResult]]: ...
    Generic_Func_GenericClasses_Func_8_T1 = typing.TypeVar('Generic_Func_GenericClasses_Func_8_T1')
    Generic_Func_GenericClasses_Func_8_T2 = typing.TypeVar('Generic_Func_GenericClasses_Func_8_T2')
    Generic_Func_GenericClasses_Func_8_T3 = typing.TypeVar('Generic_Func_GenericClasses_Func_8_T3')
    Generic_Func_GenericClasses_Func_8_T4 = typing.TypeVar('Generic_Func_GenericClasses_Func_8_T4')
    Generic_Func_GenericClasses_Func_8_T5 = typing.TypeVar('Generic_Func_GenericClasses_Func_8_T5')
    Generic_Func_GenericClasses_Func_8_T6 = typing.TypeVar('Generic_Func_GenericClasses_Func_8_T6')
    Generic_Func_GenericClasses_Func_8_T7 = typing.TypeVar('Generic_Func_GenericClasses_Func_8_T7')
    Generic_Func_GenericClasses_Func_8_TResult = typing.TypeVar('Generic_Func_GenericClasses_Func_8_TResult')
    @typing.overload
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_Func_GenericClasses_Func_8_T1], typing.Type[Generic_Func_GenericClasses_Func_8_T2], typing.Type[Generic_Func_GenericClasses_Func_8_T3], typing.Type[Generic_Func_GenericClasses_Func_8_T4], typing.Type[Generic_Func_GenericClasses_Func_8_T5], typing.Type[Generic_Func_GenericClasses_Func_8_T6], typing.Type[Generic_Func_GenericClasses_Func_8_T7], typing.Type[Generic_Func_GenericClasses_Func_8_TResult]]) -> typing.Type[Func_8[Generic_Func_GenericClasses_Func_8_T1, Generic_Func_GenericClasses_Func_8_T2, Generic_Func_GenericClasses_Func_8_T3, Generic_Func_GenericClasses_Func_8_T4, Generic_Func_GenericClasses_Func_8_T5, Generic_Func_GenericClasses_Func_8_T6, Generic_Func_GenericClasses_Func_8_T7, Generic_Func_GenericClasses_Func_8_TResult]]: ...
    Generic_Func_GenericClasses_Func_9_T1 = typing.TypeVar('Generic_Func_GenericClasses_Func_9_T1')
    Generic_Func_GenericClasses_Func_9_T2 = typing.TypeVar('Generic_Func_GenericClasses_Func_9_T2')
    Generic_Func_GenericClasses_Func_9_T3 = typing.TypeVar('Generic_Func_GenericClasses_Func_9_T3')
    Generic_Func_GenericClasses_Func_9_T4 = typing.TypeVar('Generic_Func_GenericClasses_Func_9_T4')
    Generic_Func_GenericClasses_Func_9_T5 = typing.TypeVar('Generic_Func_GenericClasses_Func_9_T5')
    Generic_Func_GenericClasses_Func_9_T6 = typing.TypeVar('Generic_Func_GenericClasses_Func_9_T6')
    Generic_Func_GenericClasses_Func_9_T7 = typing.TypeVar('Generic_Func_GenericClasses_Func_9_T7')
    Generic_Func_GenericClasses_Func_9_T8 = typing.TypeVar('Generic_Func_GenericClasses_Func_9_T8')
    Generic_Func_GenericClasses_Func_9_TResult = typing.TypeVar('Generic_Func_GenericClasses_Func_9_TResult')
    @typing.overload
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_Func_GenericClasses_Func_9_T1], typing.Type[Generic_Func_GenericClasses_Func_9_T2], typing.Type[Generic_Func_GenericClasses_Func_9_T3], typing.Type[Generic_Func_GenericClasses_Func_9_T4], typing.Type[Generic_Func_GenericClasses_Func_9_T5], typing.Type[Generic_Func_GenericClasses_Func_9_T6], typing.Type[Generic_Func_GenericClasses_Func_9_T7], typing.Type[Generic_Func_GenericClasses_Func_9_T8], typing.Type[Generic_Func_GenericClasses_Func_9_TResult]]) -> typing.Type[Func_9[Generic_Func_GenericClasses_Func_9_T1, Generic_Func_GenericClasses_Func_9_T2, Generic_Func_GenericClasses_Func_9_T3, Generic_Func_GenericClasses_Func_9_T4, Generic_Func_GenericClasses_Func_9_T5, Generic_Func_GenericClasses_Func_9_T6, Generic_Func_GenericClasses_Func_9_T7, Generic_Func_GenericClasses_Func_9_T8, Generic_Func_GenericClasses_Func_9_TResult]]: ...

Func : Func_GenericClasses

Func_1_TResult = typing.TypeVar('Func_1_TResult', covariant=True)
class Func_1(typing.Generic[Func_1_TResult], MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> Func_1_TResult: ...
    def Invoke(self) -> Func_1_TResult: ...


Func_10_T1 = typing.TypeVar('Func_10_T1', contravariant=True)
Func_10_T2 = typing.TypeVar('Func_10_T2', contravariant=True)
Func_10_T3 = typing.TypeVar('Func_10_T3', contravariant=True)
Func_10_T4 = typing.TypeVar('Func_10_T4', contravariant=True)
Func_10_T5 = typing.TypeVar('Func_10_T5', contravariant=True)
Func_10_T6 = typing.TypeVar('Func_10_T6', contravariant=True)
Func_10_T7 = typing.TypeVar('Func_10_T7', contravariant=True)
Func_10_T8 = typing.TypeVar('Func_10_T8', contravariant=True)
Func_10_T9 = typing.TypeVar('Func_10_T9', contravariant=True)
Func_10_TResult = typing.TypeVar('Func_10_TResult', covariant=True)
class Func_10(typing.Generic[Func_10_T1, Func_10_T2, Func_10_T3, Func_10_T4, Func_10_T5, Func_10_T6, Func_10_T7, Func_10_T8, Func_10_T9, Func_10_TResult], MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, arg1: Func_10_T1, arg2: Func_10_T2, arg3: Func_10_T3, arg4: Func_10_T4, arg5: Func_10_T5, arg6: Func_10_T6, arg7: Func_10_T7, arg8: Func_10_T8, arg9: Func_10_T9, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> Func_10_TResult: ...
    def Invoke(self, arg1: Func_10_T1, arg2: Func_10_T2, arg3: Func_10_T3, arg4: Func_10_T4, arg5: Func_10_T5, arg6: Func_10_T6, arg7: Func_10_T7, arg8: Func_10_T8, arg9: Func_10_T9) -> Func_10_TResult: ...


Func_11_T1 = typing.TypeVar('Func_11_T1', contravariant=True)
Func_11_T2 = typing.TypeVar('Func_11_T2', contravariant=True)
Func_11_T3 = typing.TypeVar('Func_11_T3', contravariant=True)
Func_11_T4 = typing.TypeVar('Func_11_T4', contravariant=True)
Func_11_T5 = typing.TypeVar('Func_11_T5', contravariant=True)
Func_11_T6 = typing.TypeVar('Func_11_T6', contravariant=True)
Func_11_T7 = typing.TypeVar('Func_11_T7', contravariant=True)
Func_11_T8 = typing.TypeVar('Func_11_T8', contravariant=True)
Func_11_T9 = typing.TypeVar('Func_11_T9', contravariant=True)
Func_11_T10 = typing.TypeVar('Func_11_T10', contravariant=True)
Func_11_TResult = typing.TypeVar('Func_11_TResult', covariant=True)
class Func_11(typing.Generic[Func_11_T1, Func_11_T2, Func_11_T3, Func_11_T4, Func_11_T5, Func_11_T6, Func_11_T7, Func_11_T8, Func_11_T9, Func_11_T10, Func_11_TResult], MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, arg1: Func_11_T1, arg2: Func_11_T2, arg3: Func_11_T3, arg4: Func_11_T4, arg5: Func_11_T5, arg6: Func_11_T6, arg7: Func_11_T7, arg8: Func_11_T8, arg9: Func_11_T9, arg10: Func_11_T10, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> Func_11_TResult: ...
    def Invoke(self, arg1: Func_11_T1, arg2: Func_11_T2, arg3: Func_11_T3, arg4: Func_11_T4, arg5: Func_11_T5, arg6: Func_11_T6, arg7: Func_11_T7, arg8: Func_11_T8, arg9: Func_11_T9, arg10: Func_11_T10) -> Func_11_TResult: ...


Func_12_T1 = typing.TypeVar('Func_12_T1', contravariant=True)
Func_12_T2 = typing.TypeVar('Func_12_T2', contravariant=True)
Func_12_T3 = typing.TypeVar('Func_12_T3', contravariant=True)
Func_12_T4 = typing.TypeVar('Func_12_T4', contravariant=True)
Func_12_T5 = typing.TypeVar('Func_12_T5', contravariant=True)
Func_12_T6 = typing.TypeVar('Func_12_T6', contravariant=True)
Func_12_T7 = typing.TypeVar('Func_12_T7', contravariant=True)
Func_12_T8 = typing.TypeVar('Func_12_T8', contravariant=True)
Func_12_T9 = typing.TypeVar('Func_12_T9', contravariant=True)
Func_12_T10 = typing.TypeVar('Func_12_T10', contravariant=True)
Func_12_T11 = typing.TypeVar('Func_12_T11', contravariant=True)
Func_12_TResult = typing.TypeVar('Func_12_TResult', covariant=True)
class Func_12(typing.Generic[Func_12_T1, Func_12_T2, Func_12_T3, Func_12_T4, Func_12_T5, Func_12_T6, Func_12_T7, Func_12_T8, Func_12_T9, Func_12_T10, Func_12_T11, Func_12_TResult], MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, arg1: Func_12_T1, arg2: Func_12_T2, arg3: Func_12_T3, arg4: Func_12_T4, arg5: Func_12_T5, arg6: Func_12_T6, arg7: Func_12_T7, arg8: Func_12_T8, arg9: Func_12_T9, arg10: Func_12_T10, arg11: Func_12_T11, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> Func_12_TResult: ...
    def Invoke(self, arg1: Func_12_T1, arg2: Func_12_T2, arg3: Func_12_T3, arg4: Func_12_T4, arg5: Func_12_T5, arg6: Func_12_T6, arg7: Func_12_T7, arg8: Func_12_T8, arg9: Func_12_T9, arg10: Func_12_T10, arg11: Func_12_T11) -> Func_12_TResult: ...


Func_13_T1 = typing.TypeVar('Func_13_T1', contravariant=True)
Func_13_T2 = typing.TypeVar('Func_13_T2', contravariant=True)
Func_13_T3 = typing.TypeVar('Func_13_T3', contravariant=True)
Func_13_T4 = typing.TypeVar('Func_13_T4', contravariant=True)
Func_13_T5 = typing.TypeVar('Func_13_T5', contravariant=True)
Func_13_T6 = typing.TypeVar('Func_13_T6', contravariant=True)
Func_13_T7 = typing.TypeVar('Func_13_T7', contravariant=True)
Func_13_T8 = typing.TypeVar('Func_13_T8', contravariant=True)
Func_13_T9 = typing.TypeVar('Func_13_T9', contravariant=True)
Func_13_T10 = typing.TypeVar('Func_13_T10', contravariant=True)
Func_13_T11 = typing.TypeVar('Func_13_T11', contravariant=True)
Func_13_T12 = typing.TypeVar('Func_13_T12', contravariant=True)
Func_13_TResult = typing.TypeVar('Func_13_TResult', covariant=True)
class Func_13(typing.Generic[Func_13_T1, Func_13_T2, Func_13_T3, Func_13_T4, Func_13_T5, Func_13_T6, Func_13_T7, Func_13_T8, Func_13_T9, Func_13_T10, Func_13_T11, Func_13_T12, Func_13_TResult], MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, arg1: Func_13_T1, arg2: Func_13_T2, arg3: Func_13_T3, arg4: Func_13_T4, arg5: Func_13_T5, arg6: Func_13_T6, arg7: Func_13_T7, arg8: Func_13_T8, arg9: Func_13_T9, arg10: Func_13_T10, arg11: Func_13_T11, arg12: Func_13_T12, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> Func_13_TResult: ...
    def Invoke(self, arg1: Func_13_T1, arg2: Func_13_T2, arg3: Func_13_T3, arg4: Func_13_T4, arg5: Func_13_T5, arg6: Func_13_T6, arg7: Func_13_T7, arg8: Func_13_T8, arg9: Func_13_T9, arg10: Func_13_T10, arg11: Func_13_T11, arg12: Func_13_T12) -> Func_13_TResult: ...


Func_14_T1 = typing.TypeVar('Func_14_T1', contravariant=True)
Func_14_T2 = typing.TypeVar('Func_14_T2', contravariant=True)
Func_14_T3 = typing.TypeVar('Func_14_T3', contravariant=True)
Func_14_T4 = typing.TypeVar('Func_14_T4', contravariant=True)
Func_14_T5 = typing.TypeVar('Func_14_T5', contravariant=True)
Func_14_T6 = typing.TypeVar('Func_14_T6', contravariant=True)
Func_14_T7 = typing.TypeVar('Func_14_T7', contravariant=True)
Func_14_T8 = typing.TypeVar('Func_14_T8', contravariant=True)
Func_14_T9 = typing.TypeVar('Func_14_T9', contravariant=True)
Func_14_T10 = typing.TypeVar('Func_14_T10', contravariant=True)
Func_14_T11 = typing.TypeVar('Func_14_T11', contravariant=True)
Func_14_T12 = typing.TypeVar('Func_14_T12', contravariant=True)
Func_14_T13 = typing.TypeVar('Func_14_T13', contravariant=True)
Func_14_TResult = typing.TypeVar('Func_14_TResult', covariant=True)
class Func_14(typing.Generic[Func_14_T1, Func_14_T2, Func_14_T3, Func_14_T4, Func_14_T5, Func_14_T6, Func_14_T7, Func_14_T8, Func_14_T9, Func_14_T10, Func_14_T11, Func_14_T12, Func_14_T13, Func_14_TResult], MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, arg1: Func_14_T1, arg2: Func_14_T2, arg3: Func_14_T3, arg4: Func_14_T4, arg5: Func_14_T5, arg6: Func_14_T6, arg7: Func_14_T7, arg8: Func_14_T8, arg9: Func_14_T9, arg10: Func_14_T10, arg11: Func_14_T11, arg12: Func_14_T12, arg13: Func_14_T13, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> Func_14_TResult: ...
    def Invoke(self, arg1: Func_14_T1, arg2: Func_14_T2, arg3: Func_14_T3, arg4: Func_14_T4, arg5: Func_14_T5, arg6: Func_14_T6, arg7: Func_14_T7, arg8: Func_14_T8, arg9: Func_14_T9, arg10: Func_14_T10, arg11: Func_14_T11, arg12: Func_14_T12, arg13: Func_14_T13) -> Func_14_TResult: ...


Func_15_T1 = typing.TypeVar('Func_15_T1', contravariant=True)
Func_15_T2 = typing.TypeVar('Func_15_T2', contravariant=True)
Func_15_T3 = typing.TypeVar('Func_15_T3', contravariant=True)
Func_15_T4 = typing.TypeVar('Func_15_T4', contravariant=True)
Func_15_T5 = typing.TypeVar('Func_15_T5', contravariant=True)
Func_15_T6 = typing.TypeVar('Func_15_T6', contravariant=True)
Func_15_T7 = typing.TypeVar('Func_15_T7', contravariant=True)
Func_15_T8 = typing.TypeVar('Func_15_T8', contravariant=True)
Func_15_T9 = typing.TypeVar('Func_15_T9', contravariant=True)
Func_15_T10 = typing.TypeVar('Func_15_T10', contravariant=True)
Func_15_T11 = typing.TypeVar('Func_15_T11', contravariant=True)
Func_15_T12 = typing.TypeVar('Func_15_T12', contravariant=True)
Func_15_T13 = typing.TypeVar('Func_15_T13', contravariant=True)
Func_15_T14 = typing.TypeVar('Func_15_T14', contravariant=True)
Func_15_TResult = typing.TypeVar('Func_15_TResult', covariant=True)
class Func_15(typing.Generic[Func_15_T1, Func_15_T2, Func_15_T3, Func_15_T4, Func_15_T5, Func_15_T6, Func_15_T7, Func_15_T8, Func_15_T9, Func_15_T10, Func_15_T11, Func_15_T12, Func_15_T13, Func_15_T14, Func_15_TResult], MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, arg1: Func_15_T1, arg2: Func_15_T2, arg3: Func_15_T3, arg4: Func_15_T4, arg5: Func_15_T5, arg6: Func_15_T6, arg7: Func_15_T7, arg8: Func_15_T8, arg9: Func_15_T9, arg10: Func_15_T10, arg11: Func_15_T11, arg12: Func_15_T12, arg13: Func_15_T13, arg14: Func_15_T14, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> Func_15_TResult: ...
    def Invoke(self, arg1: Func_15_T1, arg2: Func_15_T2, arg3: Func_15_T3, arg4: Func_15_T4, arg5: Func_15_T5, arg6: Func_15_T6, arg7: Func_15_T7, arg8: Func_15_T8, arg9: Func_15_T9, arg10: Func_15_T10, arg11: Func_15_T11, arg12: Func_15_T12, arg13: Func_15_T13, arg14: Func_15_T14) -> Func_15_TResult: ...


Func_16_T1 = typing.TypeVar('Func_16_T1', contravariant=True)
Func_16_T2 = typing.TypeVar('Func_16_T2', contravariant=True)
Func_16_T3 = typing.TypeVar('Func_16_T3', contravariant=True)
Func_16_T4 = typing.TypeVar('Func_16_T4', contravariant=True)
Func_16_T5 = typing.TypeVar('Func_16_T5', contravariant=True)
Func_16_T6 = typing.TypeVar('Func_16_T6', contravariant=True)
Func_16_T7 = typing.TypeVar('Func_16_T7', contravariant=True)
Func_16_T8 = typing.TypeVar('Func_16_T8', contravariant=True)
Func_16_T9 = typing.TypeVar('Func_16_T9', contravariant=True)
Func_16_T10 = typing.TypeVar('Func_16_T10', contravariant=True)
Func_16_T11 = typing.TypeVar('Func_16_T11', contravariant=True)
Func_16_T12 = typing.TypeVar('Func_16_T12', contravariant=True)
Func_16_T13 = typing.TypeVar('Func_16_T13', contravariant=True)
Func_16_T14 = typing.TypeVar('Func_16_T14', contravariant=True)
Func_16_T15 = typing.TypeVar('Func_16_T15', contravariant=True)
Func_16_TResult = typing.TypeVar('Func_16_TResult', covariant=True)
class Func_16(typing.Generic[Func_16_T1, Func_16_T2, Func_16_T3, Func_16_T4, Func_16_T5, Func_16_T6, Func_16_T7, Func_16_T8, Func_16_T9, Func_16_T10, Func_16_T11, Func_16_T12, Func_16_T13, Func_16_T14, Func_16_T15, Func_16_TResult], MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, arg1: Func_16_T1, arg2: Func_16_T2, arg3: Func_16_T3, arg4: Func_16_T4, arg5: Func_16_T5, arg6: Func_16_T6, arg7: Func_16_T7, arg8: Func_16_T8, arg9: Func_16_T9, arg10: Func_16_T10, arg11: Func_16_T11, arg12: Func_16_T12, arg13: Func_16_T13, arg14: Func_16_T14, arg15: Func_16_T15, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> Func_16_TResult: ...
    def Invoke(self, arg1: Func_16_T1, arg2: Func_16_T2, arg3: Func_16_T3, arg4: Func_16_T4, arg5: Func_16_T5, arg6: Func_16_T6, arg7: Func_16_T7, arg8: Func_16_T8, arg9: Func_16_T9, arg10: Func_16_T10, arg11: Func_16_T11, arg12: Func_16_T12, arg13: Func_16_T13, arg14: Func_16_T14, arg15: Func_16_T15) -> Func_16_TResult: ...


Func_17_T1 = typing.TypeVar('Func_17_T1', contravariant=True)
Func_17_T2 = typing.TypeVar('Func_17_T2', contravariant=True)
Func_17_T3 = typing.TypeVar('Func_17_T3', contravariant=True)
Func_17_T4 = typing.TypeVar('Func_17_T4', contravariant=True)
Func_17_T5 = typing.TypeVar('Func_17_T5', contravariant=True)
Func_17_T6 = typing.TypeVar('Func_17_T6', contravariant=True)
Func_17_T7 = typing.TypeVar('Func_17_T7', contravariant=True)
Func_17_T8 = typing.TypeVar('Func_17_T8', contravariant=True)
Func_17_T9 = typing.TypeVar('Func_17_T9', contravariant=True)
Func_17_T10 = typing.TypeVar('Func_17_T10', contravariant=True)
Func_17_T11 = typing.TypeVar('Func_17_T11', contravariant=True)
Func_17_T12 = typing.TypeVar('Func_17_T12', contravariant=True)
Func_17_T13 = typing.TypeVar('Func_17_T13', contravariant=True)
Func_17_T14 = typing.TypeVar('Func_17_T14', contravariant=True)
Func_17_T15 = typing.TypeVar('Func_17_T15', contravariant=True)
Func_17_T16 = typing.TypeVar('Func_17_T16', contravariant=True)
Func_17_TResult = typing.TypeVar('Func_17_TResult', covariant=True)
class Func_17(typing.Generic[Func_17_T1, Func_17_T2, Func_17_T3, Func_17_T4, Func_17_T5, Func_17_T6, Func_17_T7, Func_17_T8, Func_17_T9, Func_17_T10, Func_17_T11, Func_17_T12, Func_17_T13, Func_17_T14, Func_17_T15, Func_17_T16, Func_17_TResult], MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, arg1: Func_17_T1, arg2: Func_17_T2, arg3: Func_17_T3, arg4: Func_17_T4, arg5: Func_17_T5, arg6: Func_17_T6, arg7: Func_17_T7, arg8: Func_17_T8, arg9: Func_17_T9, arg10: Func_17_T10, arg11: Func_17_T11, arg12: Func_17_T12, arg13: Func_17_T13, arg14: Func_17_T14, arg15: Func_17_T15, arg16: Func_17_T16, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> Func_17_TResult: ...
    def Invoke(self, arg1: Func_17_T1, arg2: Func_17_T2, arg3: Func_17_T3, arg4: Func_17_T4, arg5: Func_17_T5, arg6: Func_17_T6, arg7: Func_17_T7, arg8: Func_17_T8, arg9: Func_17_T9, arg10: Func_17_T10, arg11: Func_17_T11, arg12: Func_17_T12, arg13: Func_17_T13, arg14: Func_17_T14, arg15: Func_17_T15, arg16: Func_17_T16) -> Func_17_TResult: ...


Func_2_T = typing.TypeVar('Func_2_T', contravariant=True)
Func_2_TResult = typing.TypeVar('Func_2_TResult', covariant=True)
class Func_2(typing.Generic[Func_2_T, Func_2_TResult], MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, arg: Func_2_T, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> Func_2_TResult: ...
    def Invoke(self, arg: Func_2_T) -> Func_2_TResult: ...


Func_3_T1 = typing.TypeVar('Func_3_T1', contravariant=True)
Func_3_T2 = typing.TypeVar('Func_3_T2', contravariant=True)
Func_3_TResult = typing.TypeVar('Func_3_TResult', covariant=True)
class Func_3(typing.Generic[Func_3_T1, Func_3_T2, Func_3_TResult], MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, arg1: Func_3_T1, arg2: Func_3_T2, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> Func_3_TResult: ...
    def Invoke(self, arg1: Func_3_T1, arg2: Func_3_T2) -> Func_3_TResult: ...


Func_4_T1 = typing.TypeVar('Func_4_T1', contravariant=True)
Func_4_T2 = typing.TypeVar('Func_4_T2', contravariant=True)
Func_4_T3 = typing.TypeVar('Func_4_T3', contravariant=True)
Func_4_TResult = typing.TypeVar('Func_4_TResult', covariant=True)
class Func_4(typing.Generic[Func_4_T1, Func_4_T2, Func_4_T3, Func_4_TResult], MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, arg1: Func_4_T1, arg2: Func_4_T2, arg3: Func_4_T3, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> Func_4_TResult: ...
    def Invoke(self, arg1: Func_4_T1, arg2: Func_4_T2, arg3: Func_4_T3) -> Func_4_TResult: ...


Func_5_T1 = typing.TypeVar('Func_5_T1', contravariant=True)
Func_5_T2 = typing.TypeVar('Func_5_T2', contravariant=True)
Func_5_T3 = typing.TypeVar('Func_5_T3', contravariant=True)
Func_5_T4 = typing.TypeVar('Func_5_T4', contravariant=True)
Func_5_TResult = typing.TypeVar('Func_5_TResult', covariant=True)
class Func_5(typing.Generic[Func_5_T1, Func_5_T2, Func_5_T3, Func_5_T4, Func_5_TResult], MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, arg1: Func_5_T1, arg2: Func_5_T2, arg3: Func_5_T3, arg4: Func_5_T4, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> Func_5_TResult: ...
    def Invoke(self, arg1: Func_5_T1, arg2: Func_5_T2, arg3: Func_5_T3, arg4: Func_5_T4) -> Func_5_TResult: ...


Func_6_T1 = typing.TypeVar('Func_6_T1', contravariant=True)
Func_6_T2 = typing.TypeVar('Func_6_T2', contravariant=True)
Func_6_T3 = typing.TypeVar('Func_6_T3', contravariant=True)
Func_6_T4 = typing.TypeVar('Func_6_T4', contravariant=True)
Func_6_T5 = typing.TypeVar('Func_6_T5', contravariant=True)
Func_6_TResult = typing.TypeVar('Func_6_TResult', covariant=True)
class Func_6(typing.Generic[Func_6_T1, Func_6_T2, Func_6_T3, Func_6_T4, Func_6_T5, Func_6_TResult], MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, arg1: Func_6_T1, arg2: Func_6_T2, arg3: Func_6_T3, arg4: Func_6_T4, arg5: Func_6_T5, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> Func_6_TResult: ...
    def Invoke(self, arg1: Func_6_T1, arg2: Func_6_T2, arg3: Func_6_T3, arg4: Func_6_T4, arg5: Func_6_T5) -> Func_6_TResult: ...


Func_7_T1 = typing.TypeVar('Func_7_T1', contravariant=True)
Func_7_T2 = typing.TypeVar('Func_7_T2', contravariant=True)
Func_7_T3 = typing.TypeVar('Func_7_T3', contravariant=True)
Func_7_T4 = typing.TypeVar('Func_7_T4', contravariant=True)
Func_7_T5 = typing.TypeVar('Func_7_T5', contravariant=True)
Func_7_T6 = typing.TypeVar('Func_7_T6', contravariant=True)
Func_7_TResult = typing.TypeVar('Func_7_TResult', covariant=True)
class Func_7(typing.Generic[Func_7_T1, Func_7_T2, Func_7_T3, Func_7_T4, Func_7_T5, Func_7_T6, Func_7_TResult], MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, arg1: Func_7_T1, arg2: Func_7_T2, arg3: Func_7_T3, arg4: Func_7_T4, arg5: Func_7_T5, arg6: Func_7_T6, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> Func_7_TResult: ...
    def Invoke(self, arg1: Func_7_T1, arg2: Func_7_T2, arg3: Func_7_T3, arg4: Func_7_T4, arg5: Func_7_T5, arg6: Func_7_T6) -> Func_7_TResult: ...


Func_8_T1 = typing.TypeVar('Func_8_T1', contravariant=True)
Func_8_T2 = typing.TypeVar('Func_8_T2', contravariant=True)
Func_8_T3 = typing.TypeVar('Func_8_T3', contravariant=True)
Func_8_T4 = typing.TypeVar('Func_8_T4', contravariant=True)
Func_8_T5 = typing.TypeVar('Func_8_T5', contravariant=True)
Func_8_T6 = typing.TypeVar('Func_8_T6', contravariant=True)
Func_8_T7 = typing.TypeVar('Func_8_T7', contravariant=True)
Func_8_TResult = typing.TypeVar('Func_8_TResult', covariant=True)
class Func_8(typing.Generic[Func_8_T1, Func_8_T2, Func_8_T3, Func_8_T4, Func_8_T5, Func_8_T6, Func_8_T7, Func_8_TResult], MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, arg1: Func_8_T1, arg2: Func_8_T2, arg3: Func_8_T3, arg4: Func_8_T4, arg5: Func_8_T5, arg6: Func_8_T6, arg7: Func_8_T7, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> Func_8_TResult: ...
    def Invoke(self, arg1: Func_8_T1, arg2: Func_8_T2, arg3: Func_8_T3, arg4: Func_8_T4, arg5: Func_8_T5, arg6: Func_8_T6, arg7: Func_8_T7) -> Func_8_TResult: ...


Func_9_T1 = typing.TypeVar('Func_9_T1', contravariant=True)
Func_9_T2 = typing.TypeVar('Func_9_T2', contravariant=True)
Func_9_T3 = typing.TypeVar('Func_9_T3', contravariant=True)
Func_9_T4 = typing.TypeVar('Func_9_T4', contravariant=True)
Func_9_T5 = typing.TypeVar('Func_9_T5', contravariant=True)
Func_9_T6 = typing.TypeVar('Func_9_T6', contravariant=True)
Func_9_T7 = typing.TypeVar('Func_9_T7', contravariant=True)
Func_9_T8 = typing.TypeVar('Func_9_T8', contravariant=True)
Func_9_TResult = typing.TypeVar('Func_9_TResult', covariant=True)
class Func_9(typing.Generic[Func_9_T1, Func_9_T2, Func_9_T3, Func_9_T4, Func_9_T5, Func_9_T6, Func_9_T7, Func_9_T8, Func_9_TResult], MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, arg1: Func_9_T1, arg2: Func_9_T2, arg3: Func_9_T3, arg4: Func_9_T4, arg5: Func_9_T5, arg6: Func_9_T6, arg7: Func_9_T7, arg8: Func_9_T8, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> Func_9_TResult: ...
    def Invoke(self, arg1: Func_9_T1, arg2: Func_9_T2, arg3: Func_9_T3, arg4: Func_9_T4, arg5: Func_9_T5, arg6: Func_9_T6, arg7: Func_9_T7, arg8: Func_9_T8) -> Func_9_TResult: ...


class GC(abc.ABC):
    @classmethod
    @property
    def MaxGeneration(cls) -> int: ...
    @staticmethod
    def AddMemoryPressure(bytesAllocated: int) -> None: ...
    @staticmethod
    def CancelFullGCNotification() -> None: ...
    @staticmethod
    def CollectionCount(generation: int) -> int: ...
    @staticmethod
    def EndNoGCRegion() -> None: ...
    @staticmethod
    def GetAllocatedBytesForCurrentThread() -> int: ...
    @staticmethod
    def GetTotalAllocatedBytes(precise: bool = ...) -> int: ...
    @staticmethod
    def GetTotalMemory(forceFullCollection: bool) -> int: ...
    @staticmethod
    def GetTotalPauseDuration() -> TimeSpan: ...
    @staticmethod
    def KeepAlive(obj: typing.Any) -> None: ...
    @staticmethod
    def RegisterForFullGCNotification(maxGenerationThreshold: int, largeObjectHeapThreshold: int) -> None: ...
    @staticmethod
    def RemoveMemoryPressure(bytesAllocated: int) -> None: ...
    @staticmethod
    def ReRegisterForFinalize(obj: typing.Any) -> None: ...
    @staticmethod
    def SuppressFinalize(obj: typing.Any) -> None: ...
    @staticmethod
    def WaitForPendingFinalizers() -> None: ...
    # Skipped AllocateArray due to it being static, abstract and generic.

    AllocateArray : AllocateArray_MethodGroup
    class AllocateArray_MethodGroup:
        def __getitem__(self, t:typing.Type[AllocateArray_1_T1]) -> AllocateArray_1[AllocateArray_1_T1]: ...

        AllocateArray_1_T1 = typing.TypeVar('AllocateArray_1_T1')
        class AllocateArray_1(typing.Generic[AllocateArray_1_T1]):
            AllocateArray_1_T = GC.AllocateArray_MethodGroup.AllocateArray_1_T1
            def __call__(self, length: int, pinned: bool = ...) -> Array_1[AllocateArray_1_T]:...


    # Skipped AllocateUninitializedArray due to it being static, abstract and generic.

    AllocateUninitializedArray : AllocateUninitializedArray_MethodGroup
    class AllocateUninitializedArray_MethodGroup:
        def __getitem__(self, t:typing.Type[AllocateUninitializedArray_1_T1]) -> AllocateUninitializedArray_1[AllocateUninitializedArray_1_T1]: ...

        AllocateUninitializedArray_1_T1 = typing.TypeVar('AllocateUninitializedArray_1_T1')
        class AllocateUninitializedArray_1(typing.Generic[AllocateUninitializedArray_1_T1]):
            AllocateUninitializedArray_1_T = GC.AllocateUninitializedArray_MethodGroup.AllocateUninitializedArray_1_T1
            def __call__(self, length: int, pinned: bool = ...) -> Array_1[AllocateUninitializedArray_1_T]:...


    # Skipped Collect due to it being static, abstract and generic.

    Collect : Collect_MethodGroup
    class Collect_MethodGroup:
        @typing.overload
        def __call__(self) -> None:...
        @typing.overload
        def __call__(self, generation: int) -> None:...
        @typing.overload
        def __call__(self, generation: int, mode: GCCollectionMode) -> None:...
        @typing.overload
        def __call__(self, generation: int, mode: GCCollectionMode, blocking: bool) -> None:...
        @typing.overload
        def __call__(self, generation: int, mode: GCCollectionMode, blocking: bool, compacting: bool) -> None:...

    # Skipped GetGCMemoryInfo due to it being static, abstract and generic.

    GetGCMemoryInfo : GetGCMemoryInfo_MethodGroup
    class GetGCMemoryInfo_MethodGroup:
        @typing.overload
        def __call__(self) -> GCMemoryInfo:...
        @typing.overload
        def __call__(self, kind: GCKind) -> GCMemoryInfo:...

    # Skipped GetGeneration due to it being static, abstract and generic.

    GetGeneration : GetGeneration_MethodGroup
    class GetGeneration_MethodGroup:
        @typing.overload
        def __call__(self, wo: WeakReference) -> int:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> int:...

    # Skipped TryStartNoGCRegion due to it being static, abstract and generic.

    TryStartNoGCRegion : TryStartNoGCRegion_MethodGroup
    class TryStartNoGCRegion_MethodGroup:
        @typing.overload
        def __call__(self, totalSize: int) -> bool:...
        @typing.overload
        def __call__(self, totalSize: int, lohSize: int) -> bool:...
        # Method TryStartNoGCRegion(totalSize : Int64, disallowFullBlockingGC : Boolean) was skipped since it collides with above method
        @typing.overload
        def __call__(self, totalSize: int, lohSize: int, disallowFullBlockingGC: bool) -> bool:...

    # Skipped WaitForFullGCApproach due to it being static, abstract and generic.

    WaitForFullGCApproach : WaitForFullGCApproach_MethodGroup
    class WaitForFullGCApproach_MethodGroup:
        @typing.overload
        def __call__(self) -> GCNotificationStatus:...
        @typing.overload
        def __call__(self, millisecondsTimeout: int) -> GCNotificationStatus:...

    # Skipped WaitForFullGCComplete due to it being static, abstract and generic.

    WaitForFullGCComplete : WaitForFullGCComplete_MethodGroup
    class WaitForFullGCComplete_MethodGroup:
        @typing.overload
        def __call__(self) -> GCNotificationStatus:...
        @typing.overload
        def __call__(self, millisecondsTimeout: int) -> GCNotificationStatus:...



class GCCollectionMode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Default : GCCollectionMode # 0
    Forced : GCCollectionMode # 1
    Optimized : GCCollectionMode # 2


class GCGenerationInfo:
    @property
    def FragmentationAfterBytes(self) -> int: ...
    @property
    def FragmentationBeforeBytes(self) -> int: ...
    @property
    def SizeAfterBytes(self) -> int: ...
    @property
    def SizeBeforeBytes(self) -> int: ...


class GCKind(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Any : GCKind # 0
    Ephemeral : GCKind # 1
    FullBlocking : GCKind # 2
    Background : GCKind # 3


class GCMemoryInfo:
    @property
    def Compacted(self) -> bool: ...
    @property
    def Concurrent(self) -> bool: ...
    @property
    def FinalizationPendingCount(self) -> int: ...
    @property
    def FragmentedBytes(self) -> int: ...
    @property
    def Generation(self) -> int: ...
    @property
    def GenerationInfo(self) -> ReadOnlySpan_1[GCGenerationInfo]: ...
    @property
    def HeapSizeBytes(self) -> int: ...
    @property
    def HighMemoryLoadThresholdBytes(self) -> int: ...
    @property
    def Index(self) -> int: ...
    @property
    def MemoryLoadBytes(self) -> int: ...
    @property
    def PauseDurations(self) -> ReadOnlySpan_1[TimeSpan]: ...
    @property
    def PauseTimePercentage(self) -> float: ...
    @property
    def PinnedObjectsCount(self) -> int: ...
    @property
    def PromotedBytes(self) -> int: ...
    @property
    def TotalAvailableMemoryBytes(self) -> int: ...
    @property
    def TotalCommittedBytes(self) -> int: ...


class GCNotificationStatus(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Succeeded : GCNotificationStatus # 0
    Failed : GCNotificationStatus # 1
    Canceled : GCNotificationStatus # 2
    Timeout : GCNotificationStatus # 3
    NotApplicable : GCNotificationStatus # 4


class Guid(IComparisonOperators_2[Guid, Guid], ISpanParseable_1[Guid], ISpanFormattable):
    # Constructor .ctor(a : Int32, b : Int16, c : Int16, d : Byte, e : Byte, f : Byte, g : Byte, h : Byte, i : Byte, j : Byte, k : Byte) was skipped since it collides with above method
    @typing.overload
    def __init__(self, a: int, b: int, c: int, d: Array_1[int]) -> None: ...
    @typing.overload
    def __init__(self, a: int, b: int, c: int, d: int, e: int, f: int, g: int, h: int, i: int, j: int, k: int) -> None: ...
    @typing.overload
    def __init__(self, b: Array_1[int]) -> None: ...
    @typing.overload
    def __init__(self, b: ReadOnlySpan_1[int]) -> None: ...
    @typing.overload
    def __init__(self, g: str) -> None: ...
    Empty : Guid
    def GetHashCode(self) -> int: ...
    @staticmethod
    def NewGuid() -> Guid: ...
    def __eq__(self, a: Guid, b: Guid) -> bool: ...
    def __ne__(self, a: Guid, b: Guid) -> bool: ...
    def ToByteArray(self) -> Array_1[int]: ...
    def TryFormat(self, destination: Span_1[str], charsWritten: clr.Reference[int], format: ReadOnlySpan_1[str] = ...) -> bool: ...
    def TryWriteBytes(self, destination: Span_1[int]) -> bool: ...
    # Skipped CompareTo due to it being static, abstract and generic.

    CompareTo : CompareTo_MethodGroup
    class CompareTo_MethodGroup:
        @typing.overload
        def __call__(self, value: Guid) -> int:...
        @typing.overload
        def __call__(self, value: typing.Any) -> int:...

    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, g: Guid) -> bool:...
        @typing.overload
        def __call__(self, o: typing.Any) -> bool:...

    # Skipped Parse due to it being static, abstract and generic.

    Parse : Parse_MethodGroup
    class Parse_MethodGroup:
        @typing.overload
        def __call__(self, input: ReadOnlySpan_1[str]) -> Guid:...
        @typing.overload
        def __call__(self, input: str) -> Guid:...

    # Skipped ParseExact due to it being static, abstract and generic.

    ParseExact : ParseExact_MethodGroup
    class ParseExact_MethodGroup:
        @typing.overload
        def __call__(self, input: ReadOnlySpan_1[str], format: ReadOnlySpan_1[str]) -> Guid:...
        @typing.overload
        def __call__(self, input: str, format: str) -> Guid:...

    # Skipped ToString due to it being static, abstract and generic.

    ToString : ToString_MethodGroup
    class ToString_MethodGroup:
        @typing.overload
        def __call__(self) -> str:...
        @typing.overload
        def __call__(self, format: str) -> str:...
        @typing.overload
        def __call__(self, format: str, provider: IFormatProvider) -> str:...

    # Skipped TryParse due to it being static, abstract and generic.

    TryParse : TryParse_MethodGroup
    class TryParse_MethodGroup:
        @typing.overload
        def __call__(self, input: ReadOnlySpan_1[str], result: clr.Reference[Guid]) -> bool:...
        @typing.overload
        def __call__(self, input: str, result: clr.Reference[Guid]) -> bool:...

    # Skipped TryParseExact due to it being static, abstract and generic.

    TryParseExact : TryParseExact_MethodGroup
    class TryParseExact_MethodGroup:
        @typing.overload
        def __call__(self, input: ReadOnlySpan_1[str], format: ReadOnlySpan_1[str], result: clr.Reference[Guid]) -> bool:...
        @typing.overload
        def __call__(self, input: str, format: str, result: clr.Reference[Guid]) -> bool:...



class Half(IBinaryFloatingPoint_1[Half], IMinMaxValue_1[Half]):
    @classmethod
    @property
    def Epsilon(cls) -> Half: ...
    @classmethod
    @property
    def MaxValue(cls) -> Half: ...
    @classmethod
    @property
    def MinValue(cls) -> Half: ...
    @classmethod
    @property
    def NaN(cls) -> Half: ...
    @classmethod
    @property
    def NegativeInfinity(cls) -> Half: ...
    @classmethod
    @property
    def PositiveInfinity(cls) -> Half: ...
    def GetHashCode(self) -> int: ...
    @staticmethod
    def IsFinite(value: Half) -> bool: ...
    @staticmethod
    def IsInfinity(value: Half) -> bool: ...
    @staticmethod
    def IsNaN(value: Half) -> bool: ...
    @staticmethod
    def IsNegative(value: Half) -> bool: ...
    @staticmethod
    def IsNegativeInfinity(value: Half) -> bool: ...
    @staticmethod
    def IsNormal(value: Half) -> bool: ...
    @staticmethod
    def IsPositiveInfinity(value: Half) -> bool: ...
    @staticmethod
    def IsSubnormal(value: Half) -> bool: ...
    def __eq__(self, left: Half, right: Half) -> bool: ...
    # Operator not supported op_Explicit(value: Single)
    # Operator not supported op_Explicit(value: Double)
    # Operator not supported op_Explicit(value: Half)
    # Operator not supported op_Explicit(value: Half)
    def __gt__(self, left: Half, right: Half) -> bool: ...
    def __ge__(self, left: Half, right: Half) -> bool: ...
    def __ne__(self, left: Half, right: Half) -> bool: ...
    def __lt__(self, left: Half, right: Half) -> bool: ...
    def __le__(self, left: Half, right: Half) -> bool: ...
    def TryFormat(self, destination: Span_1[str], charsWritten: clr.Reference[int], format: ReadOnlySpan_1[str] = ..., provider: IFormatProvider = ...) -> bool: ...
    # Skipped CompareTo due to it being static, abstract and generic.

    CompareTo : CompareTo_MethodGroup
    class CompareTo_MethodGroup:
        @typing.overload
        def __call__(self, other: Half) -> int:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> int:...

    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, other: Half) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...

    # Skipped Parse due to it being static, abstract and generic.

    Parse : Parse_MethodGroup
    class Parse_MethodGroup:
        @typing.overload
        def __call__(self, s: str) -> Half:...
        @typing.overload
        def __call__(self, s: str, style: NumberStyles) -> Half:...
        @typing.overload
        def __call__(self, s: str, provider: IFormatProvider) -> Half:...
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], style: NumberStyles = ..., provider: IFormatProvider = ...) -> Half:...
        @typing.overload
        def __call__(self, s: str, style: NumberStyles = ..., provider: IFormatProvider = ...) -> Half:...

    # Skipped ToString due to it being static, abstract and generic.

    ToString : ToString_MethodGroup
    class ToString_MethodGroup:
        @typing.overload
        def __call__(self) -> str:...
        @typing.overload
        def __call__(self, format: str) -> str:...
        @typing.overload
        def __call__(self, provider: IFormatProvider) -> str:...
        @typing.overload
        def __call__(self, format: str, provider: IFormatProvider) -> str:...

    # Skipped TryParse due to it being static, abstract and generic.

    TryParse : TryParse_MethodGroup
    class TryParse_MethodGroup:
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], result: clr.Reference[Half]) -> bool:...
        @typing.overload
        def __call__(self, s: str, result: clr.Reference[Half]) -> bool:...
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], style: NumberStyles, provider: IFormatProvider, result: clr.Reference[Half]) -> bool:...
        @typing.overload
        def __call__(self, s: str, style: NumberStyles, provider: IFormatProvider, result: clr.Reference[Half]) -> bool:...



class HashCode:
    def AddBytes(self, value: ReadOnlySpan_1[int]) -> None: ...
    def Equals(self, obj: typing.Any) -> bool: ...
    def GetHashCode(self) -> int: ...
    def ToHashCode(self) -> int: ...
    # Skipped Add due to it being static, abstract and generic.

    Add : Add_MethodGroup
    class Add_MethodGroup:
        def __getitem__(self, t:typing.Type[Add_1_T1]) -> Add_1[Add_1_T1]: ...

        Add_1_T1 = typing.TypeVar('Add_1_T1')
        class Add_1(typing.Generic[Add_1_T1]):
            Add_1_T = HashCode.Add_MethodGroup.Add_1_T1
            @typing.overload
            def __call__(self, value: Add_1_T) -> None:...
            @typing.overload
            def __call__(self, value: Add_1_T, comparer: IEqualityComparer_1[Add_1_T]) -> None:...


    # Skipped Combine due to it being static, abstract and generic.

    Combine : Combine_MethodGroup
    class Combine_MethodGroup:
        @typing.overload
        def __getitem__(self, t:typing.Type[Combine_1_T1]) -> Combine_1[Combine_1_T1]: ...

        Combine_1_T1 = typing.TypeVar('Combine_1_T1')
        class Combine_1(typing.Generic[Combine_1_T1]):
            Combine_1_T1 = HashCode.Combine_MethodGroup.Combine_1_T1
            def __call__(self, value1: Combine_1_T1) -> int:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Combine_2_T1], typing.Type[Combine_2_T2]]) -> Combine_2[Combine_2_T1, Combine_2_T2]: ...

        Combine_2_T1 = typing.TypeVar('Combine_2_T1')
        Combine_2_T2 = typing.TypeVar('Combine_2_T2')
        class Combine_2(typing.Generic[Combine_2_T1, Combine_2_T2]):
            Combine_2_T1 = HashCode.Combine_MethodGroup.Combine_2_T1
            Combine_2_T2 = HashCode.Combine_MethodGroup.Combine_2_T2
            def __call__(self, value1: Combine_2_T1, value2: Combine_2_T2) -> int:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Combine_3_T1], typing.Type[Combine_3_T2], typing.Type[Combine_3_T3]]) -> Combine_3[Combine_3_T1, Combine_3_T2, Combine_3_T3]: ...

        Combine_3_T1 = typing.TypeVar('Combine_3_T1')
        Combine_3_T2 = typing.TypeVar('Combine_3_T2')
        Combine_3_T3 = typing.TypeVar('Combine_3_T3')
        class Combine_3(typing.Generic[Combine_3_T1, Combine_3_T2, Combine_3_T3]):
            Combine_3_T1 = HashCode.Combine_MethodGroup.Combine_3_T1
            Combine_3_T2 = HashCode.Combine_MethodGroup.Combine_3_T2
            Combine_3_T3 = HashCode.Combine_MethodGroup.Combine_3_T3
            def __call__(self, value1: Combine_3_T1, value2: Combine_3_T2, value3: Combine_3_T3) -> int:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Combine_4_T1], typing.Type[Combine_4_T2], typing.Type[Combine_4_T3], typing.Type[Combine_4_T4]]) -> Combine_4[Combine_4_T1, Combine_4_T2, Combine_4_T3, Combine_4_T4]: ...

        Combine_4_T1 = typing.TypeVar('Combine_4_T1')
        Combine_4_T2 = typing.TypeVar('Combine_4_T2')
        Combine_4_T3 = typing.TypeVar('Combine_4_T3')
        Combine_4_T4 = typing.TypeVar('Combine_4_T4')
        class Combine_4(typing.Generic[Combine_4_T1, Combine_4_T2, Combine_4_T3, Combine_4_T4]):
            Combine_4_T1 = HashCode.Combine_MethodGroup.Combine_4_T1
            Combine_4_T2 = HashCode.Combine_MethodGroup.Combine_4_T2
            Combine_4_T3 = HashCode.Combine_MethodGroup.Combine_4_T3
            Combine_4_T4 = HashCode.Combine_MethodGroup.Combine_4_T4
            def __call__(self, value1: Combine_4_T1, value2: Combine_4_T2, value3: Combine_4_T3, value4: Combine_4_T4) -> int:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Combine_5_T1], typing.Type[Combine_5_T2], typing.Type[Combine_5_T3], typing.Type[Combine_5_T4], typing.Type[Combine_5_T5]]) -> Combine_5[Combine_5_T1, Combine_5_T2, Combine_5_T3, Combine_5_T4, Combine_5_T5]: ...

        Combine_5_T1 = typing.TypeVar('Combine_5_T1')
        Combine_5_T2 = typing.TypeVar('Combine_5_T2')
        Combine_5_T3 = typing.TypeVar('Combine_5_T3')
        Combine_5_T4 = typing.TypeVar('Combine_5_T4')
        Combine_5_T5 = typing.TypeVar('Combine_5_T5')
        class Combine_5(typing.Generic[Combine_5_T1, Combine_5_T2, Combine_5_T3, Combine_5_T4, Combine_5_T5]):
            Combine_5_T1 = HashCode.Combine_MethodGroup.Combine_5_T1
            Combine_5_T2 = HashCode.Combine_MethodGroup.Combine_5_T2
            Combine_5_T3 = HashCode.Combine_MethodGroup.Combine_5_T3
            Combine_5_T4 = HashCode.Combine_MethodGroup.Combine_5_T4
            Combine_5_T5 = HashCode.Combine_MethodGroup.Combine_5_T5
            def __call__(self, value1: Combine_5_T1, value2: Combine_5_T2, value3: Combine_5_T3, value4: Combine_5_T4, value5: Combine_5_T5) -> int:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Combine_6_T1], typing.Type[Combine_6_T2], typing.Type[Combine_6_T3], typing.Type[Combine_6_T4], typing.Type[Combine_6_T5], typing.Type[Combine_6_T6]]) -> Combine_6[Combine_6_T1, Combine_6_T2, Combine_6_T3, Combine_6_T4, Combine_6_T5, Combine_6_T6]: ...

        Combine_6_T1 = typing.TypeVar('Combine_6_T1')
        Combine_6_T2 = typing.TypeVar('Combine_6_T2')
        Combine_6_T3 = typing.TypeVar('Combine_6_T3')
        Combine_6_T4 = typing.TypeVar('Combine_6_T4')
        Combine_6_T5 = typing.TypeVar('Combine_6_T5')
        Combine_6_T6 = typing.TypeVar('Combine_6_T6')
        class Combine_6(typing.Generic[Combine_6_T1, Combine_6_T2, Combine_6_T3, Combine_6_T4, Combine_6_T5, Combine_6_T6]):
            Combine_6_T1 = HashCode.Combine_MethodGroup.Combine_6_T1
            Combine_6_T2 = HashCode.Combine_MethodGroup.Combine_6_T2
            Combine_6_T3 = HashCode.Combine_MethodGroup.Combine_6_T3
            Combine_6_T4 = HashCode.Combine_MethodGroup.Combine_6_T4
            Combine_6_T5 = HashCode.Combine_MethodGroup.Combine_6_T5
            Combine_6_T6 = HashCode.Combine_MethodGroup.Combine_6_T6
            def __call__(self, value1: Combine_6_T1, value2: Combine_6_T2, value3: Combine_6_T3, value4: Combine_6_T4, value5: Combine_6_T5, value6: Combine_6_T6) -> int:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Combine_7_T1], typing.Type[Combine_7_T2], typing.Type[Combine_7_T3], typing.Type[Combine_7_T4], typing.Type[Combine_7_T5], typing.Type[Combine_7_T6], typing.Type[Combine_7_T7]]) -> Combine_7[Combine_7_T1, Combine_7_T2, Combine_7_T3, Combine_7_T4, Combine_7_T5, Combine_7_T6, Combine_7_T7]: ...

        Combine_7_T1 = typing.TypeVar('Combine_7_T1')
        Combine_7_T2 = typing.TypeVar('Combine_7_T2')
        Combine_7_T3 = typing.TypeVar('Combine_7_T3')
        Combine_7_T4 = typing.TypeVar('Combine_7_T4')
        Combine_7_T5 = typing.TypeVar('Combine_7_T5')
        Combine_7_T6 = typing.TypeVar('Combine_7_T6')
        Combine_7_T7 = typing.TypeVar('Combine_7_T7')
        class Combine_7(typing.Generic[Combine_7_T1, Combine_7_T2, Combine_7_T3, Combine_7_T4, Combine_7_T5, Combine_7_T6, Combine_7_T7]):
            Combine_7_T1 = HashCode.Combine_MethodGroup.Combine_7_T1
            Combine_7_T2 = HashCode.Combine_MethodGroup.Combine_7_T2
            Combine_7_T3 = HashCode.Combine_MethodGroup.Combine_7_T3
            Combine_7_T4 = HashCode.Combine_MethodGroup.Combine_7_T4
            Combine_7_T5 = HashCode.Combine_MethodGroup.Combine_7_T5
            Combine_7_T6 = HashCode.Combine_MethodGroup.Combine_7_T6
            Combine_7_T7 = HashCode.Combine_MethodGroup.Combine_7_T7
            def __call__(self, value1: Combine_7_T1, value2: Combine_7_T2, value3: Combine_7_T3, value4: Combine_7_T4, value5: Combine_7_T5, value6: Combine_7_T6, value7: Combine_7_T7) -> int:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Combine_8_T1], typing.Type[Combine_8_T2], typing.Type[Combine_8_T3], typing.Type[Combine_8_T4], typing.Type[Combine_8_T5], typing.Type[Combine_8_T6], typing.Type[Combine_8_T7], typing.Type[Combine_8_T8]]) -> Combine_8[Combine_8_T1, Combine_8_T2, Combine_8_T3, Combine_8_T4, Combine_8_T5, Combine_8_T6, Combine_8_T7, Combine_8_T8]: ...

        Combine_8_T1 = typing.TypeVar('Combine_8_T1')
        Combine_8_T2 = typing.TypeVar('Combine_8_T2')
        Combine_8_T3 = typing.TypeVar('Combine_8_T3')
        Combine_8_T4 = typing.TypeVar('Combine_8_T4')
        Combine_8_T5 = typing.TypeVar('Combine_8_T5')
        Combine_8_T6 = typing.TypeVar('Combine_8_T6')
        Combine_8_T7 = typing.TypeVar('Combine_8_T7')
        Combine_8_T8 = typing.TypeVar('Combine_8_T8')
        class Combine_8(typing.Generic[Combine_8_T1, Combine_8_T2, Combine_8_T3, Combine_8_T4, Combine_8_T5, Combine_8_T6, Combine_8_T7, Combine_8_T8]):
            Combine_8_T1 = HashCode.Combine_MethodGroup.Combine_8_T1
            Combine_8_T2 = HashCode.Combine_MethodGroup.Combine_8_T2
            Combine_8_T3 = HashCode.Combine_MethodGroup.Combine_8_T3
            Combine_8_T4 = HashCode.Combine_MethodGroup.Combine_8_T4
            Combine_8_T5 = HashCode.Combine_MethodGroup.Combine_8_T5
            Combine_8_T6 = HashCode.Combine_MethodGroup.Combine_8_T6
            Combine_8_T7 = HashCode.Combine_MethodGroup.Combine_8_T7
            Combine_8_T8 = HashCode.Combine_MethodGroup.Combine_8_T8
            def __call__(self, value1: Combine_8_T1, value2: Combine_8_T2, value3: Combine_8_T3, value4: Combine_8_T4, value5: Combine_8_T5, value6: Combine_8_T6, value7: Combine_8_T7, value8: Combine_8_T8) -> int:...




class IAdditionOperators_GenericClasses(abc.ABCMeta):
    Generic_IAdditionOperators_GenericClasses_IAdditionOperators_3_TSelf = typing.TypeVar('Generic_IAdditionOperators_GenericClasses_IAdditionOperators_3_TSelf')
    Generic_IAdditionOperators_GenericClasses_IAdditionOperators_3_TOther = typing.TypeVar('Generic_IAdditionOperators_GenericClasses_IAdditionOperators_3_TOther')
    Generic_IAdditionOperators_GenericClasses_IAdditionOperators_3_TResult = typing.TypeVar('Generic_IAdditionOperators_GenericClasses_IAdditionOperators_3_TResult')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_IAdditionOperators_GenericClasses_IAdditionOperators_3_TSelf], typing.Type[Generic_IAdditionOperators_GenericClasses_IAdditionOperators_3_TOther], typing.Type[Generic_IAdditionOperators_GenericClasses_IAdditionOperators_3_TResult]]) -> typing.Type[IAdditionOperators_3[Generic_IAdditionOperators_GenericClasses_IAdditionOperators_3_TSelf, Generic_IAdditionOperators_GenericClasses_IAdditionOperators_3_TOther, Generic_IAdditionOperators_GenericClasses_IAdditionOperators_3_TResult]]: ...

IAdditionOperators : IAdditionOperators_GenericClasses

IAdditionOperators_3_TSelf = typing.TypeVar('IAdditionOperators_3_TSelf')
IAdditionOperators_3_TOther = typing.TypeVar('IAdditionOperators_3_TOther')
IAdditionOperators_3_TResult = typing.TypeVar('IAdditionOperators_3_TResult')
class IAdditionOperators_3(typing.Generic[IAdditionOperators_3_TSelf, IAdditionOperators_3_TOther, IAdditionOperators_3_TResult], typing.Protocol):
    @abc.abstractmethod
    def __add__(self, left: IAdditionOperators_3_TSelf, right: IAdditionOperators_3_TOther) -> IAdditionOperators_3_TResult: ...


class IAdditiveIdentity_GenericClasses(abc.ABCMeta):
    Generic_IAdditiveIdentity_GenericClasses_IAdditiveIdentity_2_TSelf = typing.TypeVar('Generic_IAdditiveIdentity_GenericClasses_IAdditiveIdentity_2_TSelf')
    Generic_IAdditiveIdentity_GenericClasses_IAdditiveIdentity_2_TResult = typing.TypeVar('Generic_IAdditiveIdentity_GenericClasses_IAdditiveIdentity_2_TResult')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_IAdditiveIdentity_GenericClasses_IAdditiveIdentity_2_TSelf], typing.Type[Generic_IAdditiveIdentity_GenericClasses_IAdditiveIdentity_2_TResult]]) -> typing.Type[IAdditiveIdentity_2[Generic_IAdditiveIdentity_GenericClasses_IAdditiveIdentity_2_TSelf, Generic_IAdditiveIdentity_GenericClasses_IAdditiveIdentity_2_TResult]]: ...

IAdditiveIdentity : IAdditiveIdentity_GenericClasses

IAdditiveIdentity_2_TSelf = typing.TypeVar('IAdditiveIdentity_2_TSelf')
IAdditiveIdentity_2_TResult = typing.TypeVar('IAdditiveIdentity_2_TResult')
class IAdditiveIdentity_2(typing.Generic[IAdditiveIdentity_2_TSelf, IAdditiveIdentity_2_TResult], typing.Protocol):
    @classmethod
    @property
    def AdditiveIdentity(cls) -> IAdditiveIdentity_2_TResult: ...


class IAsyncDisposable(typing.Protocol):
    @abc.abstractmethod
    def DisposeAsync(self) -> ValueTask: ...


class IAsyncResult(typing.Protocol):
    @property
    def AsyncState(self) -> typing.Any: ...
    @property
    def AsyncWaitHandle(self) -> WaitHandle: ...
    @property
    def CompletedSynchronously(self) -> bool: ...
    @property
    def IsCompleted(self) -> bool: ...


class IBinaryFloatingPoint_GenericClasses(abc.ABCMeta):
    Generic_IBinaryFloatingPoint_GenericClasses_IBinaryFloatingPoint_1_TSelf = typing.TypeVar('Generic_IBinaryFloatingPoint_GenericClasses_IBinaryFloatingPoint_1_TSelf')
    def __getitem__(self, types : typing.Type[Generic_IBinaryFloatingPoint_GenericClasses_IBinaryFloatingPoint_1_TSelf]) -> typing.Type[IBinaryFloatingPoint_1[Generic_IBinaryFloatingPoint_GenericClasses_IBinaryFloatingPoint_1_TSelf]]: ...

IBinaryFloatingPoint : IBinaryFloatingPoint_GenericClasses

IBinaryFloatingPoint_1_TSelf = typing.TypeVar('IBinaryFloatingPoint_1_TSelf')
class IBinaryFloatingPoint_1(typing.Generic[IBinaryFloatingPoint_1_TSelf], IFloatingPoint_1[IBinaryFloatingPoint_1_TSelf], IBinaryNumber_1[IBinaryFloatingPoint_1_TSelf], typing.Protocol):
    pass


class IBinaryInteger_GenericClasses(abc.ABCMeta):
    Generic_IBinaryInteger_GenericClasses_IBinaryInteger_1_TSelf = typing.TypeVar('Generic_IBinaryInteger_GenericClasses_IBinaryInteger_1_TSelf')
    def __getitem__(self, types : typing.Type[Generic_IBinaryInteger_GenericClasses_IBinaryInteger_1_TSelf]) -> typing.Type[IBinaryInteger_1[Generic_IBinaryInteger_GenericClasses_IBinaryInteger_1_TSelf]]: ...

IBinaryInteger : IBinaryInteger_GenericClasses

IBinaryInteger_1_TSelf = typing.TypeVar('IBinaryInteger_1_TSelf')
class IBinaryInteger_1(typing.Generic[IBinaryInteger_1_TSelf], IBinaryNumber_1[IBinaryInteger_1_TSelf], IShiftOperators_2[IBinaryInteger_1_TSelf, IBinaryInteger_1_TSelf], typing.Protocol):
    @staticmethod
    @abc.abstractmethod
    def LeadingZeroCount(value: IBinaryInteger_1_TSelf) -> IBinaryInteger_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def PopCount(value: IBinaryInteger_1_TSelf) -> IBinaryInteger_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def RotateLeft(value: IBinaryInteger_1_TSelf, rotateAmount: int) -> IBinaryInteger_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def RotateRight(value: IBinaryInteger_1_TSelf, rotateAmount: int) -> IBinaryInteger_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def TrailingZeroCount(value: IBinaryInteger_1_TSelf) -> IBinaryInteger_1_TSelf: ...


class IBinaryNumber_GenericClasses(abc.ABCMeta):
    Generic_IBinaryNumber_GenericClasses_IBinaryNumber_1_TSelf = typing.TypeVar('Generic_IBinaryNumber_GenericClasses_IBinaryNumber_1_TSelf')
    def __getitem__(self, types : typing.Type[Generic_IBinaryNumber_GenericClasses_IBinaryNumber_1_TSelf]) -> typing.Type[IBinaryNumber_1[Generic_IBinaryNumber_GenericClasses_IBinaryNumber_1_TSelf]]: ...

IBinaryNumber : IBinaryNumber_GenericClasses

IBinaryNumber_1_TSelf = typing.TypeVar('IBinaryNumber_1_TSelf')
class IBinaryNumber_1(typing.Generic[IBinaryNumber_1_TSelf], INumber_1[IBinaryNumber_1_TSelf], IBitwiseOperators_3[IBinaryNumber_1_TSelf, IBinaryNumber_1_TSelf, IBinaryNumber_1_TSelf], typing.Protocol):
    @staticmethod
    @abc.abstractmethod
    def IsPow2(value: IBinaryNumber_1_TSelf) -> bool: ...
    @staticmethod
    @abc.abstractmethod
    def Log2(value: IBinaryNumber_1_TSelf) -> IBinaryNumber_1_TSelf: ...


class IBitwiseOperators_GenericClasses(abc.ABCMeta):
    Generic_IBitwiseOperators_GenericClasses_IBitwiseOperators_3_TSelf = typing.TypeVar('Generic_IBitwiseOperators_GenericClasses_IBitwiseOperators_3_TSelf')
    Generic_IBitwiseOperators_GenericClasses_IBitwiseOperators_3_TOther = typing.TypeVar('Generic_IBitwiseOperators_GenericClasses_IBitwiseOperators_3_TOther')
    Generic_IBitwiseOperators_GenericClasses_IBitwiseOperators_3_TResult = typing.TypeVar('Generic_IBitwiseOperators_GenericClasses_IBitwiseOperators_3_TResult')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_IBitwiseOperators_GenericClasses_IBitwiseOperators_3_TSelf], typing.Type[Generic_IBitwiseOperators_GenericClasses_IBitwiseOperators_3_TOther], typing.Type[Generic_IBitwiseOperators_GenericClasses_IBitwiseOperators_3_TResult]]) -> typing.Type[IBitwiseOperators_3[Generic_IBitwiseOperators_GenericClasses_IBitwiseOperators_3_TSelf, Generic_IBitwiseOperators_GenericClasses_IBitwiseOperators_3_TOther, Generic_IBitwiseOperators_GenericClasses_IBitwiseOperators_3_TResult]]: ...

IBitwiseOperators : IBitwiseOperators_GenericClasses

IBitwiseOperators_3_TSelf = typing.TypeVar('IBitwiseOperators_3_TSelf')
IBitwiseOperators_3_TOther = typing.TypeVar('IBitwiseOperators_3_TOther')
IBitwiseOperators_3_TResult = typing.TypeVar('IBitwiseOperators_3_TResult')
class IBitwiseOperators_3(typing.Generic[IBitwiseOperators_3_TSelf, IBitwiseOperators_3_TOther, IBitwiseOperators_3_TResult], typing.Protocol):
    @abc.abstractmethod
    def __and__(self, left: IBitwiseOperators_3_TSelf, right: IBitwiseOperators_3_TOther) -> IBitwiseOperators_3_TResult: ...
    @abc.abstractmethod
    def __or__(self, left: IBitwiseOperators_3_TSelf, right: IBitwiseOperators_3_TOther) -> IBitwiseOperators_3_TResult: ...
    @abc.abstractmethod
    def __xor__(self, left: IBitwiseOperators_3_TSelf, right: IBitwiseOperators_3_TOther) -> IBitwiseOperators_3_TResult: ...
    @abc.abstractmethod
    def __invert__(self, value: IBitwiseOperators_3_TSelf) -> IBitwiseOperators_3_TResult: ...


class ICloneable(typing.Protocol):
    @abc.abstractmethod
    def Clone(self) -> typing.Any: ...


class IComparable_GenericClasses(abc.ABCMeta):
    Generic_IComparable_GenericClasses_IComparable_1_T = typing.TypeVar('Generic_IComparable_GenericClasses_IComparable_1_T')
    def __getitem__(self, types : typing.Type[Generic_IComparable_GenericClasses_IComparable_1_T]) -> typing.Type[IComparable_1[Generic_IComparable_GenericClasses_IComparable_1_T]]: ...

class IComparable(IComparable_0, metaclass =IComparable_GenericClasses): ...

class IComparable_0(typing.Protocol):
    @abc.abstractmethod
    def CompareTo(self, obj: typing.Any) -> int: ...


IComparable_1_T = typing.TypeVar('IComparable_1_T', contravariant=True)
class IComparable_1(typing.Generic[IComparable_1_T], typing.Protocol):
    @abc.abstractmethod
    def CompareTo(self, other: IComparable_1_T) -> int: ...


class IComparisonOperators_GenericClasses(abc.ABCMeta):
    Generic_IComparisonOperators_GenericClasses_IComparisonOperators_2_TSelf = typing.TypeVar('Generic_IComparisonOperators_GenericClasses_IComparisonOperators_2_TSelf')
    Generic_IComparisonOperators_GenericClasses_IComparisonOperators_2_TOther = typing.TypeVar('Generic_IComparisonOperators_GenericClasses_IComparisonOperators_2_TOther')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_IComparisonOperators_GenericClasses_IComparisonOperators_2_TSelf], typing.Type[Generic_IComparisonOperators_GenericClasses_IComparisonOperators_2_TOther]]) -> typing.Type[IComparisonOperators_2[Generic_IComparisonOperators_GenericClasses_IComparisonOperators_2_TSelf, Generic_IComparisonOperators_GenericClasses_IComparisonOperators_2_TOther]]: ...

IComparisonOperators : IComparisonOperators_GenericClasses

IComparisonOperators_2_TSelf = typing.TypeVar('IComparisonOperators_2_TSelf')
IComparisonOperators_2_TOther = typing.TypeVar('IComparisonOperators_2_TOther')
class IComparisonOperators_2(typing.Generic[IComparisonOperators_2_TSelf, IComparisonOperators_2_TOther], IEqualityOperators_2[IComparisonOperators_2_TSelf, IComparisonOperators_2_TOther], IComparable_1[IComparisonOperators_2_TOther], IComparable_0, typing.Protocol):
    @abc.abstractmethod
    def __gt__(self, left: IComparisonOperators_2_TSelf, right: IComparisonOperators_2_TOther) -> bool: ...
    @abc.abstractmethod
    def __ge__(self, left: IComparisonOperators_2_TSelf, right: IComparisonOperators_2_TOther) -> bool: ...
    @abc.abstractmethod
    def __lt__(self, left: IComparisonOperators_2_TSelf, right: IComparisonOperators_2_TOther) -> bool: ...
    @abc.abstractmethod
    def __le__(self, left: IComparisonOperators_2_TSelf, right: IComparisonOperators_2_TOther) -> bool: ...


class IConvertible(typing.Protocol):
    @abc.abstractmethod
    def GetTypeCode(self) -> TypeCode: ...
    @abc.abstractmethod
    def ToBoolean(self, provider: IFormatProvider) -> bool: ...
    @abc.abstractmethod
    def ToByte(self, provider: IFormatProvider) -> int: ...
    @abc.abstractmethod
    def ToChar(self, provider: IFormatProvider) -> str: ...
    @abc.abstractmethod
    def ToDateTime(self, provider: IFormatProvider) -> DateTime: ...
    @abc.abstractmethod
    def ToDecimal(self, provider: IFormatProvider) -> Decimal: ...
    @abc.abstractmethod
    def ToDouble(self, provider: IFormatProvider) -> float: ...
    @abc.abstractmethod
    def ToInt16(self, provider: IFormatProvider) -> int: ...
    @abc.abstractmethod
    def ToInt32(self, provider: IFormatProvider) -> int: ...
    @abc.abstractmethod
    def ToInt64(self, provider: IFormatProvider) -> int: ...
    @abc.abstractmethod
    def ToSByte(self, provider: IFormatProvider) -> int: ...
    @abc.abstractmethod
    def ToSingle(self, provider: IFormatProvider) -> float: ...
    @abc.abstractmethod
    def ToString(self, provider: IFormatProvider) -> str: ...
    @abc.abstractmethod
    def ToType(self, conversionType: typing.Type[typing.Any], provider: IFormatProvider) -> typing.Any: ...
    @abc.abstractmethod
    def ToUInt16(self, provider: IFormatProvider) -> int: ...
    @abc.abstractmethod
    def ToUInt32(self, provider: IFormatProvider) -> int: ...
    @abc.abstractmethod
    def ToUInt64(self, provider: IFormatProvider) -> int: ...


class ICustomFormatter(typing.Protocol):
    @abc.abstractmethod
    def Format(self, format: str, arg: typing.Any, formatProvider: IFormatProvider) -> str: ...


class IDecrementOperators_GenericClasses(abc.ABCMeta):
    Generic_IDecrementOperators_GenericClasses_IDecrementOperators_1_TSelf = typing.TypeVar('Generic_IDecrementOperators_GenericClasses_IDecrementOperators_1_TSelf')
    def __getitem__(self, types : typing.Type[Generic_IDecrementOperators_GenericClasses_IDecrementOperators_1_TSelf]) -> typing.Type[IDecrementOperators_1[Generic_IDecrementOperators_GenericClasses_IDecrementOperators_1_TSelf]]: ...

IDecrementOperators : IDecrementOperators_GenericClasses

IDecrementOperators_1_TSelf = typing.TypeVar('IDecrementOperators_1_TSelf')
class IDecrementOperators_1(typing.Generic[IDecrementOperators_1_TSelf], typing.Protocol):
    # Operator not supported op_Decrement(value: TSelf)
    pass


class IDisposable(typing.Protocol):
    @abc.abstractmethod
    def Dispose(self) -> None: ...


class IDivisionOperators_GenericClasses(abc.ABCMeta):
    Generic_IDivisionOperators_GenericClasses_IDivisionOperators_3_TSelf = typing.TypeVar('Generic_IDivisionOperators_GenericClasses_IDivisionOperators_3_TSelf')
    Generic_IDivisionOperators_GenericClasses_IDivisionOperators_3_TOther = typing.TypeVar('Generic_IDivisionOperators_GenericClasses_IDivisionOperators_3_TOther')
    Generic_IDivisionOperators_GenericClasses_IDivisionOperators_3_TResult = typing.TypeVar('Generic_IDivisionOperators_GenericClasses_IDivisionOperators_3_TResult')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_IDivisionOperators_GenericClasses_IDivisionOperators_3_TSelf], typing.Type[Generic_IDivisionOperators_GenericClasses_IDivisionOperators_3_TOther], typing.Type[Generic_IDivisionOperators_GenericClasses_IDivisionOperators_3_TResult]]) -> typing.Type[IDivisionOperators_3[Generic_IDivisionOperators_GenericClasses_IDivisionOperators_3_TSelf, Generic_IDivisionOperators_GenericClasses_IDivisionOperators_3_TOther, Generic_IDivisionOperators_GenericClasses_IDivisionOperators_3_TResult]]: ...

IDivisionOperators : IDivisionOperators_GenericClasses

IDivisionOperators_3_TSelf = typing.TypeVar('IDivisionOperators_3_TSelf')
IDivisionOperators_3_TOther = typing.TypeVar('IDivisionOperators_3_TOther')
IDivisionOperators_3_TResult = typing.TypeVar('IDivisionOperators_3_TResult')
class IDivisionOperators_3(typing.Generic[IDivisionOperators_3_TSelf, IDivisionOperators_3_TOther, IDivisionOperators_3_TResult], typing.Protocol):
    @abc.abstractmethod
    def __truediv__(self, left: IDivisionOperators_3_TSelf, right: IDivisionOperators_3_TOther) -> IDivisionOperators_3_TResult: ...


class IEqualityOperators_GenericClasses(abc.ABCMeta):
    Generic_IEqualityOperators_GenericClasses_IEqualityOperators_2_TSelf = typing.TypeVar('Generic_IEqualityOperators_GenericClasses_IEqualityOperators_2_TSelf')
    Generic_IEqualityOperators_GenericClasses_IEqualityOperators_2_TOther = typing.TypeVar('Generic_IEqualityOperators_GenericClasses_IEqualityOperators_2_TOther')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_IEqualityOperators_GenericClasses_IEqualityOperators_2_TSelf], typing.Type[Generic_IEqualityOperators_GenericClasses_IEqualityOperators_2_TOther]]) -> typing.Type[IEqualityOperators_2[Generic_IEqualityOperators_GenericClasses_IEqualityOperators_2_TSelf, Generic_IEqualityOperators_GenericClasses_IEqualityOperators_2_TOther]]: ...

IEqualityOperators : IEqualityOperators_GenericClasses

IEqualityOperators_2_TSelf = typing.TypeVar('IEqualityOperators_2_TSelf')
IEqualityOperators_2_TOther = typing.TypeVar('IEqualityOperators_2_TOther')
class IEqualityOperators_2(typing.Generic[IEqualityOperators_2_TSelf, IEqualityOperators_2_TOther], IEquatable_1[IEqualityOperators_2_TOther], typing.Protocol):
    @abc.abstractmethod
    def __eq__(self, left: IEqualityOperators_2_TSelf, right: IEqualityOperators_2_TOther) -> bool: ...
    @abc.abstractmethod
    def __ne__(self, left: IEqualityOperators_2_TSelf, right: IEqualityOperators_2_TOther) -> bool: ...


class IEquatable_GenericClasses(abc.ABCMeta):
    Generic_IEquatable_GenericClasses_IEquatable_1_T = typing.TypeVar('Generic_IEquatable_GenericClasses_IEquatable_1_T')
    def __getitem__(self, types : typing.Type[Generic_IEquatable_GenericClasses_IEquatable_1_T]) -> typing.Type[IEquatable_1[Generic_IEquatable_GenericClasses_IEquatable_1_T]]: ...

IEquatable : IEquatable_GenericClasses

IEquatable_1_T = typing.TypeVar('IEquatable_1_T')
class IEquatable_1(typing.Generic[IEquatable_1_T], typing.Protocol):
    @abc.abstractmethod
    def Equals(self, other: IEquatable_1_T) -> bool: ...


class IFloatingPoint_GenericClasses(abc.ABCMeta):
    Generic_IFloatingPoint_GenericClasses_IFloatingPoint_1_TSelf = typing.TypeVar('Generic_IFloatingPoint_GenericClasses_IFloatingPoint_1_TSelf')
    def __getitem__(self, types : typing.Type[Generic_IFloatingPoint_GenericClasses_IFloatingPoint_1_TSelf]) -> typing.Type[IFloatingPoint_1[Generic_IFloatingPoint_GenericClasses_IFloatingPoint_1_TSelf]]: ...

IFloatingPoint : IFloatingPoint_GenericClasses

IFloatingPoint_1_TSelf = typing.TypeVar('IFloatingPoint_1_TSelf')
class IFloatingPoint_1(typing.Generic[IFloatingPoint_1_TSelf], ISignedNumber_1[IFloatingPoint_1_TSelf], typing.Protocol):
    @classmethod
    @property
    def E(cls) -> IFloatingPoint_1_TSelf: ...
    @classmethod
    @property
    def Epsilon(cls) -> IFloatingPoint_1_TSelf: ...
    @classmethod
    @property
    def NaN(cls) -> IFloatingPoint_1_TSelf: ...
    @classmethod
    @property
    def NegativeInfinity(cls) -> IFloatingPoint_1_TSelf: ...
    @classmethod
    @property
    def NegativeZero(cls) -> IFloatingPoint_1_TSelf: ...
    @classmethod
    @property
    def Pi(cls) -> IFloatingPoint_1_TSelf: ...
    @classmethod
    @property
    def PositiveInfinity(cls) -> IFloatingPoint_1_TSelf: ...
    @classmethod
    @property
    def Tau(cls) -> IFloatingPoint_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def Acos(x: IFloatingPoint_1_TSelf) -> IFloatingPoint_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def Acosh(x: IFloatingPoint_1_TSelf) -> IFloatingPoint_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def Asin(x: IFloatingPoint_1_TSelf) -> IFloatingPoint_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def Asinh(x: IFloatingPoint_1_TSelf) -> IFloatingPoint_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def Atan(x: IFloatingPoint_1_TSelf) -> IFloatingPoint_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def Atan2(y: IFloatingPoint_1_TSelf, x: IFloatingPoint_1_TSelf) -> IFloatingPoint_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def Atanh(x: IFloatingPoint_1_TSelf) -> IFloatingPoint_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def BitDecrement(x: IFloatingPoint_1_TSelf) -> IFloatingPoint_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def BitIncrement(x: IFloatingPoint_1_TSelf) -> IFloatingPoint_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def Cbrt(x: IFloatingPoint_1_TSelf) -> IFloatingPoint_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def Ceiling(x: IFloatingPoint_1_TSelf) -> IFloatingPoint_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def CopySign(x: IFloatingPoint_1_TSelf, y: IFloatingPoint_1_TSelf) -> IFloatingPoint_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def Cos(x: IFloatingPoint_1_TSelf) -> IFloatingPoint_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def Cosh(x: IFloatingPoint_1_TSelf) -> IFloatingPoint_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def Exp(x: IFloatingPoint_1_TSelf) -> IFloatingPoint_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def Floor(x: IFloatingPoint_1_TSelf) -> IFloatingPoint_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def FusedMultiplyAdd(left: IFloatingPoint_1_TSelf, right: IFloatingPoint_1_TSelf, addend: IFloatingPoint_1_TSelf) -> IFloatingPoint_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def IEEERemainder(left: IFloatingPoint_1_TSelf, right: IFloatingPoint_1_TSelf) -> IFloatingPoint_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def IsFinite(value: IFloatingPoint_1_TSelf) -> bool: ...
    @staticmethod
    @abc.abstractmethod
    def IsInfinity(value: IFloatingPoint_1_TSelf) -> bool: ...
    @staticmethod
    @abc.abstractmethod
    def IsNaN(value: IFloatingPoint_1_TSelf) -> bool: ...
    @staticmethod
    @abc.abstractmethod
    def IsNegative(value: IFloatingPoint_1_TSelf) -> bool: ...
    @staticmethod
    @abc.abstractmethod
    def IsNegativeInfinity(value: IFloatingPoint_1_TSelf) -> bool: ...
    @staticmethod
    @abc.abstractmethod
    def IsNormal(value: IFloatingPoint_1_TSelf) -> bool: ...
    @staticmethod
    @abc.abstractmethod
    def IsPositiveInfinity(value: IFloatingPoint_1_TSelf) -> bool: ...
    @staticmethod
    @abc.abstractmethod
    def IsSubnormal(value: IFloatingPoint_1_TSelf) -> bool: ...
    @staticmethod
    @abc.abstractmethod
    def Log10(x: IFloatingPoint_1_TSelf) -> IFloatingPoint_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def Log2(x: IFloatingPoint_1_TSelf) -> IFloatingPoint_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def MaxMagnitude(x: IFloatingPoint_1_TSelf, y: IFloatingPoint_1_TSelf) -> IFloatingPoint_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def MinMagnitude(x: IFloatingPoint_1_TSelf, y: IFloatingPoint_1_TSelf) -> IFloatingPoint_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def Pow(x: IFloatingPoint_1_TSelf, y: IFloatingPoint_1_TSelf) -> IFloatingPoint_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def Sin(x: IFloatingPoint_1_TSelf) -> IFloatingPoint_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def Sinh(x: IFloatingPoint_1_TSelf) -> IFloatingPoint_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def Sqrt(x: IFloatingPoint_1_TSelf) -> IFloatingPoint_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def Tan(x: IFloatingPoint_1_TSelf) -> IFloatingPoint_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def Tanh(x: IFloatingPoint_1_TSelf) -> IFloatingPoint_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def Truncate(x: IFloatingPoint_1_TSelf) -> IFloatingPoint_1_TSelf: ...


class IFormatProvider(typing.Protocol):
    @abc.abstractmethod
    def GetFormat(self, formatType: typing.Type[typing.Any]) -> typing.Any: ...


class IFormattable(typing.Protocol):
    @abc.abstractmethod
    def ToString(self, format: str, formatProvider: IFormatProvider) -> str: ...


class IIncrementOperators_GenericClasses(abc.ABCMeta):
    Generic_IIncrementOperators_GenericClasses_IIncrementOperators_1_TSelf = typing.TypeVar('Generic_IIncrementOperators_GenericClasses_IIncrementOperators_1_TSelf')
    def __getitem__(self, types : typing.Type[Generic_IIncrementOperators_GenericClasses_IIncrementOperators_1_TSelf]) -> typing.Type[IIncrementOperators_1[Generic_IIncrementOperators_GenericClasses_IIncrementOperators_1_TSelf]]: ...

IIncrementOperators : IIncrementOperators_GenericClasses

IIncrementOperators_1_TSelf = typing.TypeVar('IIncrementOperators_1_TSelf')
class IIncrementOperators_1(typing.Generic[IIncrementOperators_1_TSelf], typing.Protocol):
    # Operator not supported op_Increment(value: TSelf)
    pass


class IMinMaxValue_GenericClasses(abc.ABCMeta):
    Generic_IMinMaxValue_GenericClasses_IMinMaxValue_1_TSelf = typing.TypeVar('Generic_IMinMaxValue_GenericClasses_IMinMaxValue_1_TSelf')
    def __getitem__(self, types : typing.Type[Generic_IMinMaxValue_GenericClasses_IMinMaxValue_1_TSelf]) -> typing.Type[IMinMaxValue_1[Generic_IMinMaxValue_GenericClasses_IMinMaxValue_1_TSelf]]: ...

IMinMaxValue : IMinMaxValue_GenericClasses

IMinMaxValue_1_TSelf = typing.TypeVar('IMinMaxValue_1_TSelf')
class IMinMaxValue_1(typing.Generic[IMinMaxValue_1_TSelf], typing.Protocol):
    @classmethod
    @property
    def MaxValue(cls) -> IMinMaxValue_1_TSelf: ...
    @classmethod
    @property
    def MinValue(cls) -> IMinMaxValue_1_TSelf: ...


class IModulusOperators_GenericClasses(abc.ABCMeta):
    Generic_IModulusOperators_GenericClasses_IModulusOperators_3_TSelf = typing.TypeVar('Generic_IModulusOperators_GenericClasses_IModulusOperators_3_TSelf')
    Generic_IModulusOperators_GenericClasses_IModulusOperators_3_TOther = typing.TypeVar('Generic_IModulusOperators_GenericClasses_IModulusOperators_3_TOther')
    Generic_IModulusOperators_GenericClasses_IModulusOperators_3_TResult = typing.TypeVar('Generic_IModulusOperators_GenericClasses_IModulusOperators_3_TResult')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_IModulusOperators_GenericClasses_IModulusOperators_3_TSelf], typing.Type[Generic_IModulusOperators_GenericClasses_IModulusOperators_3_TOther], typing.Type[Generic_IModulusOperators_GenericClasses_IModulusOperators_3_TResult]]) -> typing.Type[IModulusOperators_3[Generic_IModulusOperators_GenericClasses_IModulusOperators_3_TSelf, Generic_IModulusOperators_GenericClasses_IModulusOperators_3_TOther, Generic_IModulusOperators_GenericClasses_IModulusOperators_3_TResult]]: ...

IModulusOperators : IModulusOperators_GenericClasses

IModulusOperators_3_TSelf = typing.TypeVar('IModulusOperators_3_TSelf')
IModulusOperators_3_TOther = typing.TypeVar('IModulusOperators_3_TOther')
IModulusOperators_3_TResult = typing.TypeVar('IModulusOperators_3_TResult')
class IModulusOperators_3(typing.Generic[IModulusOperators_3_TSelf, IModulusOperators_3_TOther, IModulusOperators_3_TResult], typing.Protocol):
    @abc.abstractmethod
    def __mod__(self, left: IModulusOperators_3_TSelf, right: IModulusOperators_3_TOther) -> IModulusOperators_3_TResult: ...


class IMultiplicativeIdentity_GenericClasses(abc.ABCMeta):
    Generic_IMultiplicativeIdentity_GenericClasses_IMultiplicativeIdentity_2_TSelf = typing.TypeVar('Generic_IMultiplicativeIdentity_GenericClasses_IMultiplicativeIdentity_2_TSelf')
    Generic_IMultiplicativeIdentity_GenericClasses_IMultiplicativeIdentity_2_TResult = typing.TypeVar('Generic_IMultiplicativeIdentity_GenericClasses_IMultiplicativeIdentity_2_TResult')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_IMultiplicativeIdentity_GenericClasses_IMultiplicativeIdentity_2_TSelf], typing.Type[Generic_IMultiplicativeIdentity_GenericClasses_IMultiplicativeIdentity_2_TResult]]) -> typing.Type[IMultiplicativeIdentity_2[Generic_IMultiplicativeIdentity_GenericClasses_IMultiplicativeIdentity_2_TSelf, Generic_IMultiplicativeIdentity_GenericClasses_IMultiplicativeIdentity_2_TResult]]: ...

IMultiplicativeIdentity : IMultiplicativeIdentity_GenericClasses

IMultiplicativeIdentity_2_TSelf = typing.TypeVar('IMultiplicativeIdentity_2_TSelf')
IMultiplicativeIdentity_2_TResult = typing.TypeVar('IMultiplicativeIdentity_2_TResult')
class IMultiplicativeIdentity_2(typing.Generic[IMultiplicativeIdentity_2_TSelf, IMultiplicativeIdentity_2_TResult], typing.Protocol):
    @classmethod
    @property
    def MultiplicativeIdentity(cls) -> IMultiplicativeIdentity_2_TResult: ...


class IMultiplyOperators_GenericClasses(abc.ABCMeta):
    Generic_IMultiplyOperators_GenericClasses_IMultiplyOperators_3_TSelf = typing.TypeVar('Generic_IMultiplyOperators_GenericClasses_IMultiplyOperators_3_TSelf')
    Generic_IMultiplyOperators_GenericClasses_IMultiplyOperators_3_TOther = typing.TypeVar('Generic_IMultiplyOperators_GenericClasses_IMultiplyOperators_3_TOther')
    Generic_IMultiplyOperators_GenericClasses_IMultiplyOperators_3_TResult = typing.TypeVar('Generic_IMultiplyOperators_GenericClasses_IMultiplyOperators_3_TResult')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_IMultiplyOperators_GenericClasses_IMultiplyOperators_3_TSelf], typing.Type[Generic_IMultiplyOperators_GenericClasses_IMultiplyOperators_3_TOther], typing.Type[Generic_IMultiplyOperators_GenericClasses_IMultiplyOperators_3_TResult]]) -> typing.Type[IMultiplyOperators_3[Generic_IMultiplyOperators_GenericClasses_IMultiplyOperators_3_TSelf, Generic_IMultiplyOperators_GenericClasses_IMultiplyOperators_3_TOther, Generic_IMultiplyOperators_GenericClasses_IMultiplyOperators_3_TResult]]: ...

IMultiplyOperators : IMultiplyOperators_GenericClasses

IMultiplyOperators_3_TSelf = typing.TypeVar('IMultiplyOperators_3_TSelf')
IMultiplyOperators_3_TOther = typing.TypeVar('IMultiplyOperators_3_TOther')
IMultiplyOperators_3_TResult = typing.TypeVar('IMultiplyOperators_3_TResult')
class IMultiplyOperators_3(typing.Generic[IMultiplyOperators_3_TSelf, IMultiplyOperators_3_TOther, IMultiplyOperators_3_TResult], typing.Protocol):
    @abc.abstractmethod
    def __mul__(self, left: IMultiplyOperators_3_TSelf, right: IMultiplyOperators_3_TOther) -> IMultiplyOperators_3_TResult: ...


class Index(IEquatable_1[Index]):
    def __init__(self, value: int, fromEnd: bool = ...) -> None: ...
    @classmethod
    @property
    def End(cls) -> Index: ...
    @property
    def IsFromEnd(self) -> bool: ...
    @classmethod
    @property
    def Start(cls) -> Index: ...
    @property
    def Value(self) -> int: ...
    @staticmethod
    def FromEnd(value: int) -> Index: ...
    @staticmethod
    def FromStart(value: int) -> Index: ...
    def GetHashCode(self) -> int: ...
    def GetOffset(self, length: int) -> int: ...
    # Operator not supported op_Implicit(value: Int32)
    def ToString(self) -> str: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, other: Index) -> bool:...
        @typing.overload
        def __call__(self, value: typing.Any) -> bool:...



class IndexOutOfRangeException(SystemException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, innerException: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...


class InsufficientExecutionStackException(SystemException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, innerException: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...


class InsufficientMemoryException(OutOfMemoryException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, innerException: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...


class Int16(IBinaryInteger_1[int], ISignedNumber_1[int], IMinMaxValue_1[int], IConvertible):
    MaxValue : int
    MinValue : int
    def GetHashCode(self) -> int: ...
    def GetTypeCode(self) -> TypeCode: ...
    def TryFormat(self, destination: Span_1[str], charsWritten: clr.Reference[int], format: ReadOnlySpan_1[str] = ..., provider: IFormatProvider = ...) -> bool: ...
    # Skipped CompareTo due to it being static, abstract and generic.

    CompareTo : CompareTo_MethodGroup
    class CompareTo_MethodGroup:
        @typing.overload
        def __call__(self, value: int) -> int:...
        @typing.overload
        def __call__(self, value: typing.Any) -> int:...

    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, obj: int) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...

    # Skipped Parse due to it being static, abstract and generic.

    Parse : Parse_MethodGroup
    class Parse_MethodGroup:
        @typing.overload
        def __call__(self, s: str) -> int:...
        @typing.overload
        def __call__(self, s: str, style: NumberStyles) -> int:...
        @typing.overload
        def __call__(self, s: str, provider: IFormatProvider) -> int:...
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], style: NumberStyles = ..., provider: IFormatProvider = ...) -> int:...
        @typing.overload
        def __call__(self, s: str, style: NumberStyles, provider: IFormatProvider) -> int:...

    # Skipped ToString due to it being static, abstract and generic.

    ToString : ToString_MethodGroup
    class ToString_MethodGroup:
        @typing.overload
        def __call__(self) -> str:...
        @typing.overload
        def __call__(self, format: str) -> str:...
        @typing.overload
        def __call__(self, provider: IFormatProvider) -> str:...
        @typing.overload
        def __call__(self, format: str, provider: IFormatProvider) -> str:...

    # Skipped TryParse due to it being static, abstract and generic.

    TryParse : TryParse_MethodGroup
    class TryParse_MethodGroup:
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], result: clr.Reference[int]) -> bool:...
        @typing.overload
        def __call__(self, s: str, result: clr.Reference[int]) -> bool:...
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], style: NumberStyles, provider: IFormatProvider, result: clr.Reference[int]) -> bool:...
        @typing.overload
        def __call__(self, s: str, style: NumberStyles, provider: IFormatProvider, result: clr.Reference[int]) -> bool:...



class Int32(IBinaryInteger_1[int], ISignedNumber_1[int], IMinMaxValue_1[int], IConvertible):
    MaxValue : int
    MinValue : int
    def GetHashCode(self) -> int: ...
    def GetTypeCode(self) -> TypeCode: ...
    def TryFormat(self, destination: Span_1[str], charsWritten: clr.Reference[int], format: ReadOnlySpan_1[str] = ..., provider: IFormatProvider = ...) -> bool: ...
    # Skipped CompareTo due to it being static, abstract and generic.

    CompareTo : CompareTo_MethodGroup
    class CompareTo_MethodGroup:
        @typing.overload
        def __call__(self, value: int) -> int:...
        @typing.overload
        def __call__(self, value: typing.Any) -> int:...

    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, obj: int) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...

    # Skipped Parse due to it being static, abstract and generic.

    Parse : Parse_MethodGroup
    class Parse_MethodGroup:
        @typing.overload
        def __call__(self, s: str) -> int:...
        @typing.overload
        def __call__(self, s: str, style: NumberStyles) -> int:...
        @typing.overload
        def __call__(self, s: str, provider: IFormatProvider) -> int:...
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], style: NumberStyles = ..., provider: IFormatProvider = ...) -> int:...
        @typing.overload
        def __call__(self, s: str, style: NumberStyles, provider: IFormatProvider) -> int:...

    # Skipped ToString due to it being static, abstract and generic.

    ToString : ToString_MethodGroup
    class ToString_MethodGroup:
        @typing.overload
        def __call__(self) -> str:...
        @typing.overload
        def __call__(self, format: str) -> str:...
        @typing.overload
        def __call__(self, provider: IFormatProvider) -> str:...
        @typing.overload
        def __call__(self, format: str, provider: IFormatProvider) -> str:...

    # Skipped TryParse due to it being static, abstract and generic.

    TryParse : TryParse_MethodGroup
    class TryParse_MethodGroup:
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], result: clr.Reference[int]) -> bool:...
        @typing.overload
        def __call__(self, s: str, result: clr.Reference[int]) -> bool:...
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], style: NumberStyles, provider: IFormatProvider, result: clr.Reference[int]) -> bool:...
        @typing.overload
        def __call__(self, s: str, style: NumberStyles, provider: IFormatProvider, result: clr.Reference[int]) -> bool:...



class Int64(IBinaryInteger_1[int], ISignedNumber_1[int], IMinMaxValue_1[int], IConvertible):
    MaxValue : int
    MinValue : int
    def GetHashCode(self) -> int: ...
    def GetTypeCode(self) -> TypeCode: ...
    def TryFormat(self, destination: Span_1[str], charsWritten: clr.Reference[int], format: ReadOnlySpan_1[str] = ..., provider: IFormatProvider = ...) -> bool: ...
    # Skipped CompareTo due to it being static, abstract and generic.

    CompareTo : CompareTo_MethodGroup
    class CompareTo_MethodGroup:
        @typing.overload
        def __call__(self, value: int) -> int:...
        @typing.overload
        def __call__(self, value: typing.Any) -> int:...

    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, obj: int) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...

    # Skipped Parse due to it being static, abstract and generic.

    Parse : Parse_MethodGroup
    class Parse_MethodGroup:
        @typing.overload
        def __call__(self, s: str) -> int:...
        @typing.overload
        def __call__(self, s: str, style: NumberStyles) -> int:...
        @typing.overload
        def __call__(self, s: str, provider: IFormatProvider) -> int:...
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], style: NumberStyles = ..., provider: IFormatProvider = ...) -> int:...
        @typing.overload
        def __call__(self, s: str, style: NumberStyles, provider: IFormatProvider) -> int:...

    # Skipped ToString due to it being static, abstract and generic.

    ToString : ToString_MethodGroup
    class ToString_MethodGroup:
        @typing.overload
        def __call__(self) -> str:...
        @typing.overload
        def __call__(self, format: str) -> str:...
        @typing.overload
        def __call__(self, provider: IFormatProvider) -> str:...
        @typing.overload
        def __call__(self, format: str, provider: IFormatProvider) -> str:...

    # Skipped TryParse due to it being static, abstract and generic.

    TryParse : TryParse_MethodGroup
    class TryParse_MethodGroup:
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], result: clr.Reference[int]) -> bool:...
        @typing.overload
        def __call__(self, s: str, result: clr.Reference[int]) -> bool:...
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], style: NumberStyles, provider: IFormatProvider, result: clr.Reference[int]) -> bool:...
        @typing.overload
        def __call__(self, s: str, style: NumberStyles, provider: IFormatProvider, result: clr.Reference[int]) -> bool:...



class IntPtr(IBinaryInteger_1[int], ISignedNumber_1[int], IMinMaxValue_1[int], ISerializable):
    # Constructor .ctor(value : Int64) was skipped since it collides with above method
    @typing.overload
    def __init__(self, value: int) -> None: ...
    @typing.overload
    def __init__(self, value: clr.Reference[None]) -> None: ...
    Zero : int
    @classmethod
    @property
    def MaxValue(cls) -> int: ...
    @classmethod
    @property
    def MinValue(cls) -> int: ...
    @classmethod
    @property
    def Size(cls) -> int: ...
    @staticmethod
    def Add(pointer: int, offset: int) -> int: ...
    def GetHashCode(self) -> int: ...
    def __add__(self, pointer: int, offset: int) -> int: ...
    def __eq__(self, value1: int, value2: int) -> bool: ...
    # Operator not supported op_Explicit(value: Int32)
    # Operator not supported op_Explicit(value: Int64)
    # Operator not supported op_Explicit(value: IntPtr)
    # Operator not supported op_Explicit(value: IntPtr)
    # Operator not supported op_Explicit(value: IntPtr)
    # Operator not supported op_Explicit(value: Void*)
    def __ne__(self, value1: int, value2: int) -> bool: ...
    def __sub__(self, pointer: int, offset: int) -> int: ...
    @staticmethod
    def Subtract(pointer: int, offset: int) -> int: ...
    def ToInt32(self) -> int: ...
    def ToInt64(self) -> int: ...
    def ToPointer(self) -> clr.Reference[None]: ...
    def TryFormat(self, destination: Span_1[str], charsWritten: clr.Reference[int], format: ReadOnlySpan_1[str] = ..., provider: IFormatProvider = ...) -> bool: ...
    # Skipped CompareTo due to it being static, abstract and generic.

    CompareTo : CompareTo_MethodGroup
    class CompareTo_MethodGroup:
        @typing.overload
        def __call__(self, value: int) -> int:...
        @typing.overload
        def __call__(self, value: typing.Any) -> int:...

    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, other: int) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...

    # Skipped Parse due to it being static, abstract and generic.

    Parse : Parse_MethodGroup
    class Parse_MethodGroup:
        @typing.overload
        def __call__(self, s: str) -> int:...
        @typing.overload
        def __call__(self, s: str, style: NumberStyles) -> int:...
        @typing.overload
        def __call__(self, s: str, provider: IFormatProvider) -> int:...
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], style: NumberStyles = ..., provider: IFormatProvider = ...) -> int:...
        @typing.overload
        def __call__(self, s: str, style: NumberStyles, provider: IFormatProvider) -> int:...

    # Skipped ToString due to it being static, abstract and generic.

    ToString : ToString_MethodGroup
    class ToString_MethodGroup:
        @typing.overload
        def __call__(self) -> str:...
        @typing.overload
        def __call__(self, format: str) -> str:...
        @typing.overload
        def __call__(self, provider: IFormatProvider) -> str:...
        @typing.overload
        def __call__(self, format: str, provider: IFormatProvider) -> str:...

    # Skipped TryParse due to it being static, abstract and generic.

    TryParse : TryParse_MethodGroup
    class TryParse_MethodGroup:
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], result: clr.Reference[int]) -> bool:...
        @typing.overload
        def __call__(self, s: str, result: clr.Reference[int]) -> bool:...
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], style: NumberStyles, provider: IFormatProvider, result: clr.Reference[int]) -> bool:...
        @typing.overload
        def __call__(self, s: str, style: NumberStyles, provider: IFormatProvider, result: clr.Reference[int]) -> bool:...



class INumber_GenericClasses(abc.ABCMeta):
    Generic_INumber_GenericClasses_INumber_1_TSelf = typing.TypeVar('Generic_INumber_GenericClasses_INumber_1_TSelf')
    def __getitem__(self, types : typing.Type[Generic_INumber_GenericClasses_INumber_1_TSelf]) -> typing.Type[INumber_1[Generic_INumber_GenericClasses_INumber_1_TSelf]]: ...

INumber : INumber_GenericClasses

INumber_1_TSelf = typing.TypeVar('INumber_1_TSelf')
class INumber_1(typing.Generic[INumber_1_TSelf], IComparisonOperators_2[INumber_1_TSelf, INumber_1_TSelf], ISpanParseable_1[INumber_1_TSelf], ISpanFormattable, IUnaryPlusOperators_2[INumber_1_TSelf, INumber_1_TSelf], IUnaryNegationOperators_2[INumber_1_TSelf, INumber_1_TSelf], ISubtractionOperators_3[INumber_1_TSelf, INumber_1_TSelf, INumber_1_TSelf], IMultiplyOperators_3[INumber_1_TSelf, INumber_1_TSelf, INumber_1_TSelf], IMultiplicativeIdentity_2[INumber_1_TSelf, INumber_1_TSelf], IModulusOperators_3[INumber_1_TSelf, INumber_1_TSelf, INumber_1_TSelf], IIncrementOperators_1[INumber_1_TSelf], IDivisionOperators_3[INumber_1_TSelf, INumber_1_TSelf, INumber_1_TSelf], IDecrementOperators_1[INumber_1_TSelf], IAdditiveIdentity_2[INumber_1_TSelf, INumber_1_TSelf], IAdditionOperators_3[INumber_1_TSelf, INumber_1_TSelf, INumber_1_TSelf], typing.Protocol):
    @classmethod
    @property
    def One(cls) -> INumber_1_TSelf: ...
    @classmethod
    @property
    def Zero(cls) -> INumber_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def Abs(value: INumber_1_TSelf) -> INumber_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def Clamp(value: INumber_1_TSelf, min: INumber_1_TSelf, max: INumber_1_TSelf) -> INumber_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def DivRem(left: INumber_1_TSelf, right: INumber_1_TSelf) -> ValueTuple_2[INumber_1_TSelf, INumber_1_TSelf]: ...
    @staticmethod
    @abc.abstractmethod
    def Max(x: INumber_1_TSelf, y: INumber_1_TSelf) -> INumber_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def Min(x: INumber_1_TSelf, y: INumber_1_TSelf) -> INumber_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def Sign(value: INumber_1_TSelf) -> INumber_1_TSelf: ...


class InvalidCastException(SystemException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, errorCode: int) -> None: ...
    @typing.overload
    def __init__(self, message: str, innerException: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...


class InvalidOperationException(SystemException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, innerException: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...


class InvalidProgramException(SystemException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, inner: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...


class InvalidTimeZoneException(Exception):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, innerException: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...


class IObservable_GenericClasses(abc.ABCMeta):
    Generic_IObservable_GenericClasses_IObservable_1_T = typing.TypeVar('Generic_IObservable_GenericClasses_IObservable_1_T')
    def __getitem__(self, types : typing.Type[Generic_IObservable_GenericClasses_IObservable_1_T]) -> typing.Type[IObservable_1[Generic_IObservable_GenericClasses_IObservable_1_T]]: ...

IObservable : IObservable_GenericClasses

IObservable_1_T = typing.TypeVar('IObservable_1_T', covariant=True)
class IObservable_1(typing.Generic[IObservable_1_T], typing.Protocol):
    @abc.abstractmethod
    def Subscribe(self, observer: IObserver_1[IObservable_1_T]) -> IDisposable: ...


class IObserver_GenericClasses(abc.ABCMeta):
    Generic_IObserver_GenericClasses_IObserver_1_T = typing.TypeVar('Generic_IObserver_GenericClasses_IObserver_1_T')
    def __getitem__(self, types : typing.Type[Generic_IObserver_GenericClasses_IObserver_1_T]) -> typing.Type[IObserver_1[Generic_IObserver_GenericClasses_IObserver_1_T]]: ...

IObserver : IObserver_GenericClasses

IObserver_1_T = typing.TypeVar('IObserver_1_T', contravariant=True)
class IObserver_1(typing.Generic[IObserver_1_T], typing.Protocol):
    @abc.abstractmethod
    def OnCompleted(self) -> None: ...
    @abc.abstractmethod
    def OnError(self, error: Exception) -> None: ...
    @abc.abstractmethod
    def OnNext(self, value: IObserver_1_T) -> None: ...


class IParseable_GenericClasses(abc.ABCMeta):
    Generic_IParseable_GenericClasses_IParseable_1_TSelf = typing.TypeVar('Generic_IParseable_GenericClasses_IParseable_1_TSelf')
    def __getitem__(self, types : typing.Type[Generic_IParseable_GenericClasses_IParseable_1_TSelf]) -> typing.Type[IParseable_1[Generic_IParseable_GenericClasses_IParseable_1_TSelf]]: ...

IParseable : IParseable_GenericClasses

IParseable_1_TSelf = typing.TypeVar('IParseable_1_TSelf')
class IParseable_1(typing.Generic[IParseable_1_TSelf], typing.Protocol):
    @staticmethod
    @abc.abstractmethod
    def Parse(s: str, provider: IFormatProvider) -> IParseable_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def TryParse(s: str, provider: IFormatProvider, result: clr.Reference[IParseable_1_TSelf]) -> bool: ...


class IProgress_GenericClasses(abc.ABCMeta):
    Generic_IProgress_GenericClasses_IProgress_1_T = typing.TypeVar('Generic_IProgress_GenericClasses_IProgress_1_T')
    def __getitem__(self, types : typing.Type[Generic_IProgress_GenericClasses_IProgress_1_T]) -> typing.Type[IProgress_1[Generic_IProgress_GenericClasses_IProgress_1_T]]: ...

IProgress : IProgress_GenericClasses

IProgress_1_T = typing.TypeVar('IProgress_1_T', contravariant=True)
class IProgress_1(typing.Generic[IProgress_1_T], typing.Protocol):
    @abc.abstractmethod
    def Report(self, value: IProgress_1_T) -> None: ...


class IShiftOperators_GenericClasses(abc.ABCMeta):
    Generic_IShiftOperators_GenericClasses_IShiftOperators_2_TSelf = typing.TypeVar('Generic_IShiftOperators_GenericClasses_IShiftOperators_2_TSelf')
    Generic_IShiftOperators_GenericClasses_IShiftOperators_2_TResult = typing.TypeVar('Generic_IShiftOperators_GenericClasses_IShiftOperators_2_TResult')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_IShiftOperators_GenericClasses_IShiftOperators_2_TSelf], typing.Type[Generic_IShiftOperators_GenericClasses_IShiftOperators_2_TResult]]) -> typing.Type[IShiftOperators_2[Generic_IShiftOperators_GenericClasses_IShiftOperators_2_TSelf, Generic_IShiftOperators_GenericClasses_IShiftOperators_2_TResult]]: ...

IShiftOperators : IShiftOperators_GenericClasses

IShiftOperators_2_TSelf = typing.TypeVar('IShiftOperators_2_TSelf')
IShiftOperators_2_TResult = typing.TypeVar('IShiftOperators_2_TResult')
class IShiftOperators_2(typing.Generic[IShiftOperators_2_TSelf, IShiftOperators_2_TResult], typing.Protocol):
    @abc.abstractmethod
    def __lshift__(self, value: IShiftOperators_2_TSelf, shiftAmount: int) -> IShiftOperators_2_TResult: ...
    @abc.abstractmethod
    def __rshift__(self, value: IShiftOperators_2_TSelf, shiftAmount: int) -> IShiftOperators_2_TResult: ...


class ISignedNumber_GenericClasses(abc.ABCMeta):
    Generic_ISignedNumber_GenericClasses_ISignedNumber_1_TSelf = typing.TypeVar('Generic_ISignedNumber_GenericClasses_ISignedNumber_1_TSelf')
    def __getitem__(self, types : typing.Type[Generic_ISignedNumber_GenericClasses_ISignedNumber_1_TSelf]) -> typing.Type[ISignedNumber_1[Generic_ISignedNumber_GenericClasses_ISignedNumber_1_TSelf]]: ...

ISignedNumber : ISignedNumber_GenericClasses

ISignedNumber_1_TSelf = typing.TypeVar('ISignedNumber_1_TSelf')
class ISignedNumber_1(typing.Generic[ISignedNumber_1_TSelf], INumber_1[ISignedNumber_1_TSelf], typing.Protocol):
    @classmethod
    @property
    def NegativeOne(cls) -> ISignedNumber_1_TSelf: ...


class ISpanFormattable(IFormattable, typing.Protocol):
    @abc.abstractmethod
    def TryFormat(self, destination: Span_1[str], charsWritten: clr.Reference[int], format: ReadOnlySpan_1[str], provider: IFormatProvider) -> bool: ...


class ISpanParseable_GenericClasses(abc.ABCMeta):
    Generic_ISpanParseable_GenericClasses_ISpanParseable_1_TSelf = typing.TypeVar('Generic_ISpanParseable_GenericClasses_ISpanParseable_1_TSelf')
    def __getitem__(self, types : typing.Type[Generic_ISpanParseable_GenericClasses_ISpanParseable_1_TSelf]) -> typing.Type[ISpanParseable_1[Generic_ISpanParseable_GenericClasses_ISpanParseable_1_TSelf]]: ...

ISpanParseable : ISpanParseable_GenericClasses

ISpanParseable_1_TSelf = typing.TypeVar('ISpanParseable_1_TSelf')
class ISpanParseable_1(typing.Generic[ISpanParseable_1_TSelf], IParseable_1[ISpanParseable_1_TSelf], typing.Protocol):
    @staticmethod
    @abc.abstractmethod
    def Parse(s: ReadOnlySpan_1[str], provider: IFormatProvider) -> ISpanParseable_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def TryParse(s: ReadOnlySpan_1[str], provider: IFormatProvider, result: clr.Reference[ISpanParseable_1_TSelf]) -> bool: ...


class ISubtractionOperators_GenericClasses(abc.ABCMeta):
    Generic_ISubtractionOperators_GenericClasses_ISubtractionOperators_3_TSelf = typing.TypeVar('Generic_ISubtractionOperators_GenericClasses_ISubtractionOperators_3_TSelf')
    Generic_ISubtractionOperators_GenericClasses_ISubtractionOperators_3_TOther = typing.TypeVar('Generic_ISubtractionOperators_GenericClasses_ISubtractionOperators_3_TOther')
    Generic_ISubtractionOperators_GenericClasses_ISubtractionOperators_3_TResult = typing.TypeVar('Generic_ISubtractionOperators_GenericClasses_ISubtractionOperators_3_TResult')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_ISubtractionOperators_GenericClasses_ISubtractionOperators_3_TSelf], typing.Type[Generic_ISubtractionOperators_GenericClasses_ISubtractionOperators_3_TOther], typing.Type[Generic_ISubtractionOperators_GenericClasses_ISubtractionOperators_3_TResult]]) -> typing.Type[ISubtractionOperators_3[Generic_ISubtractionOperators_GenericClasses_ISubtractionOperators_3_TSelf, Generic_ISubtractionOperators_GenericClasses_ISubtractionOperators_3_TOther, Generic_ISubtractionOperators_GenericClasses_ISubtractionOperators_3_TResult]]: ...

ISubtractionOperators : ISubtractionOperators_GenericClasses

ISubtractionOperators_3_TSelf = typing.TypeVar('ISubtractionOperators_3_TSelf')
ISubtractionOperators_3_TOther = typing.TypeVar('ISubtractionOperators_3_TOther')
ISubtractionOperators_3_TResult = typing.TypeVar('ISubtractionOperators_3_TResult')
class ISubtractionOperators_3(typing.Generic[ISubtractionOperators_3_TSelf, ISubtractionOperators_3_TOther, ISubtractionOperators_3_TResult], typing.Protocol):
    @abc.abstractmethod
    def __sub__(self, left: ISubtractionOperators_3_TSelf, right: ISubtractionOperators_3_TOther) -> ISubtractionOperators_3_TResult: ...


class IUnaryNegationOperators_GenericClasses(abc.ABCMeta):
    Generic_IUnaryNegationOperators_GenericClasses_IUnaryNegationOperators_2_TSelf = typing.TypeVar('Generic_IUnaryNegationOperators_GenericClasses_IUnaryNegationOperators_2_TSelf')
    Generic_IUnaryNegationOperators_GenericClasses_IUnaryNegationOperators_2_TResult = typing.TypeVar('Generic_IUnaryNegationOperators_GenericClasses_IUnaryNegationOperators_2_TResult')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_IUnaryNegationOperators_GenericClasses_IUnaryNegationOperators_2_TSelf], typing.Type[Generic_IUnaryNegationOperators_GenericClasses_IUnaryNegationOperators_2_TResult]]) -> typing.Type[IUnaryNegationOperators_2[Generic_IUnaryNegationOperators_GenericClasses_IUnaryNegationOperators_2_TSelf, Generic_IUnaryNegationOperators_GenericClasses_IUnaryNegationOperators_2_TResult]]: ...

IUnaryNegationOperators : IUnaryNegationOperators_GenericClasses

IUnaryNegationOperators_2_TSelf = typing.TypeVar('IUnaryNegationOperators_2_TSelf')
IUnaryNegationOperators_2_TResult = typing.TypeVar('IUnaryNegationOperators_2_TResult')
class IUnaryNegationOperators_2(typing.Generic[IUnaryNegationOperators_2_TSelf, IUnaryNegationOperators_2_TResult], typing.Protocol):
    @abc.abstractmethod
    def __neg__(self, value: IUnaryNegationOperators_2_TSelf) -> IUnaryNegationOperators_2_TResult: ...


class IUnaryPlusOperators_GenericClasses(abc.ABCMeta):
    Generic_IUnaryPlusOperators_GenericClasses_IUnaryPlusOperators_2_TSelf = typing.TypeVar('Generic_IUnaryPlusOperators_GenericClasses_IUnaryPlusOperators_2_TSelf')
    Generic_IUnaryPlusOperators_GenericClasses_IUnaryPlusOperators_2_TResult = typing.TypeVar('Generic_IUnaryPlusOperators_GenericClasses_IUnaryPlusOperators_2_TResult')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_IUnaryPlusOperators_GenericClasses_IUnaryPlusOperators_2_TSelf], typing.Type[Generic_IUnaryPlusOperators_GenericClasses_IUnaryPlusOperators_2_TResult]]) -> typing.Type[IUnaryPlusOperators_2[Generic_IUnaryPlusOperators_GenericClasses_IUnaryPlusOperators_2_TSelf, Generic_IUnaryPlusOperators_GenericClasses_IUnaryPlusOperators_2_TResult]]: ...

IUnaryPlusOperators : IUnaryPlusOperators_GenericClasses

IUnaryPlusOperators_2_TSelf = typing.TypeVar('IUnaryPlusOperators_2_TSelf')
IUnaryPlusOperators_2_TResult = typing.TypeVar('IUnaryPlusOperators_2_TResult')
class IUnaryPlusOperators_2(typing.Generic[IUnaryPlusOperators_2_TSelf, IUnaryPlusOperators_2_TResult], typing.Protocol):
    @abc.abstractmethod
    def __pos__(self, value: IUnaryPlusOperators_2_TSelf) -> IUnaryPlusOperators_2_TResult: ...


class IUnsignedNumber_GenericClasses(abc.ABCMeta):
    Generic_IUnsignedNumber_GenericClasses_IUnsignedNumber_1_TSelf = typing.TypeVar('Generic_IUnsignedNumber_GenericClasses_IUnsignedNumber_1_TSelf')
    def __getitem__(self, types : typing.Type[Generic_IUnsignedNumber_GenericClasses_IUnsignedNumber_1_TSelf]) -> typing.Type[IUnsignedNumber_1[Generic_IUnsignedNumber_GenericClasses_IUnsignedNumber_1_TSelf]]: ...

IUnsignedNumber : IUnsignedNumber_GenericClasses

IUnsignedNumber_1_TSelf = typing.TypeVar('IUnsignedNumber_1_TSelf')
class IUnsignedNumber_1(typing.Generic[IUnsignedNumber_1_TSelf], INumber_1[IUnsignedNumber_1_TSelf], typing.Protocol):
    pass


class Lazy_GenericClasses(abc.ABCMeta):
    Generic_Lazy_GenericClasses_Lazy_1_T = typing.TypeVar('Generic_Lazy_GenericClasses_Lazy_1_T')
    @typing.overload
    def __getitem__(self, types : typing.Type[Generic_Lazy_GenericClasses_Lazy_1_T]) -> typing.Type[Lazy_1[Generic_Lazy_GenericClasses_Lazy_1_T]]: ...
    Generic_Lazy_GenericClasses_Lazy_2_T = typing.TypeVar('Generic_Lazy_GenericClasses_Lazy_2_T')
    Generic_Lazy_GenericClasses_Lazy_2_TMetadata = typing.TypeVar('Generic_Lazy_GenericClasses_Lazy_2_TMetadata')
    @typing.overload
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_Lazy_GenericClasses_Lazy_2_T], typing.Type[Generic_Lazy_GenericClasses_Lazy_2_TMetadata]]) -> typing.Type[Lazy_2[Generic_Lazy_GenericClasses_Lazy_2_T, Generic_Lazy_GenericClasses_Lazy_2_TMetadata]]: ...

Lazy : Lazy_GenericClasses

Lazy_1_T = typing.TypeVar('Lazy_1_T')
class Lazy_1(typing.Generic[Lazy_1_T]):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, isThreadSafe: bool) -> None: ...
    @typing.overload
    def __init__(self, mode: LazyThreadSafetyMode) -> None: ...
    @typing.overload
    def __init__(self, value: Lazy_1_T) -> None: ...
    @typing.overload
    def __init__(self, valueFactory: Func_1[Lazy_1_T]) -> None: ...
    @typing.overload
    def __init__(self, valueFactory: Func_1[Lazy_1_T], isThreadSafe: bool) -> None: ...
    @typing.overload
    def __init__(self, valueFactory: Func_1[Lazy_1_T], mode: LazyThreadSafetyMode) -> None: ...
    @property
    def IsValueCreated(self) -> bool: ...
    @property
    def Value(self) -> Lazy_1_T: ...
    def ToString(self) -> str: ...


Lazy_2_T = typing.TypeVar('Lazy_2_T')
Lazy_2_TMetadata = typing.TypeVar('Lazy_2_TMetadata')
class Lazy_2(typing.Generic[Lazy_2_T, Lazy_2_TMetadata], Lazy_1[Lazy_2_T]):
    @typing.overload
    def __init__(self, metadata: Lazy_2_TMetadata) -> None: ...
    @typing.overload
    def __init__(self, metadata: Lazy_2_TMetadata, isThreadSafe: bool) -> None: ...
    @typing.overload
    def __init__(self, metadata: Lazy_2_TMetadata, mode: LazyThreadSafetyMode) -> None: ...
    @typing.overload
    def __init__(self, valueFactory: Func_1[Lazy_2_T], metadata: Lazy_2_TMetadata) -> None: ...
    @typing.overload
    def __init__(self, valueFactory: Func_1[Lazy_2_T], metadata: Lazy_2_TMetadata, isThreadSafe: bool) -> None: ...
    @typing.overload
    def __init__(self, valueFactory: Func_1[Lazy_2_T], metadata: Lazy_2_TMetadata, mode: LazyThreadSafetyMode) -> None: ...
    @property
    def IsValueCreated(self) -> bool: ...
    @property
    def Metadata(self) -> Lazy_2_TMetadata: ...
    @property
    def Value(self) -> Lazy_2_T: ...


class LoaderOptimization(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    NotSpecified : LoaderOptimization # 0
    SingleDomain : LoaderOptimization # 1
    MultiDomain : LoaderOptimization # 2
    DomainMask : LoaderOptimization # 3
    MultiDomainHost : LoaderOptimization # 3
    DisallowBindings : LoaderOptimization # 4


class LoaderOptimizationAttribute(Attribute):
    @typing.overload
    def __init__(self, value: int) -> None: ...
    @typing.overload
    def __init__(self, value: LoaderOptimization) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...
    @property
    def Value(self) -> LoaderOptimization: ...


class LocalDataStoreSlot:
    pass


class MarshalByRefObject(abc.ABC):
    def GetLifetimeService(self) -> typing.Any: ...
    def InitializeLifetimeService(self) -> typing.Any: ...


class Math(abc.ABC):
    E : float
    PI : float
    Tau : float
    @staticmethod
    def Acos(d: float) -> float: ...
    @staticmethod
    def Acosh(d: float) -> float: ...
    @staticmethod
    def Asin(d: float) -> float: ...
    @staticmethod
    def Asinh(d: float) -> float: ...
    @staticmethod
    def Atan(d: float) -> float: ...
    @staticmethod
    def Atan2(y: float, x: float) -> float: ...
    @staticmethod
    def Atanh(d: float) -> float: ...
    @staticmethod
    def BitDecrement(x: float) -> float: ...
    @staticmethod
    def BitIncrement(x: float) -> float: ...
    @staticmethod
    def Cbrt(d: float) -> float: ...
    @staticmethod
    def CopySign(x: float, y: float) -> float: ...
    @staticmethod
    def Cos(d: float) -> float: ...
    @staticmethod
    def Cosh(value: float) -> float: ...
    @staticmethod
    def Exp(d: float) -> float: ...
    @staticmethod
    def FusedMultiplyAdd(x: float, y: float, z: float) -> float: ...
    @staticmethod
    def IEEERemainder(x: float, y: float) -> float: ...
    @staticmethod
    def ILogB(x: float) -> int: ...
    @staticmethod
    def Log10(d: float) -> float: ...
    @staticmethod
    def Log2(x: float) -> float: ...
    @staticmethod
    def MaxMagnitude(x: float, y: float) -> float: ...
    @staticmethod
    def MinMagnitude(x: float, y: float) -> float: ...
    @staticmethod
    def Pow(x: float, y: float) -> float: ...
    @staticmethod
    def ReciprocalEstimate(d: float) -> float: ...
    @staticmethod
    def ReciprocalSqrtEstimate(d: float) -> float: ...
    @staticmethod
    def ScaleB(x: float, n: int) -> float: ...
    @staticmethod
    def Sin(a: float) -> float: ...
    @staticmethod
    def SinCos(x: float) -> ValueTuple_2[float, float]: ...
    @staticmethod
    def Sinh(value: float) -> float: ...
    @staticmethod
    def Sqrt(d: float) -> float: ...
    @staticmethod
    def Tan(a: float) -> float: ...
    @staticmethod
    def Tanh(value: float) -> float: ...
    # Skipped Abs due to it being static, abstract and generic.

    Abs : Abs_MethodGroup
    class Abs_MethodGroup:
        @typing.overload
        def __call__(self, value: float) -> float:...
        # Method Abs(value : Single) was skipped since it collides with above method
        # Method Abs(value : Int16) was skipped since it collides with above method
        # Method Abs(value : Int32) was skipped since it collides with above method
        # Method Abs(value : Int64) was skipped since it collides with above method
        # Method Abs(value : IntPtr) was skipped since it collides with above method
        # Method Abs(value : SByte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Decimal) -> Decimal:...

    # Skipped BigMul due to it being static, abstract and generic.

    BigMul : BigMul_MethodGroup
    class BigMul_MethodGroup:
        @typing.overload
        def __call__(self, a: int, b: int) -> int:...
        @typing.overload
        def __call__(self, a: int, b: int, low: clr.Reference[int]) -> int:...
        # Method BigMul(a : Int64, b : Int64, low : Int64&) was skipped since it collides with above method

    # Skipped Ceiling due to it being static, abstract and generic.

    Ceiling : Ceiling_MethodGroup
    class Ceiling_MethodGroup:
        @typing.overload
        def __call__(self, a: float) -> float:...
        @typing.overload
        def __call__(self, d: Decimal) -> Decimal:...

    # Skipped Clamp due to it being static, abstract and generic.

    Clamp : Clamp_MethodGroup
    class Clamp_MethodGroup:
        @typing.overload
        def __call__(self, value: float, min: float, max: float) -> float:...
        # Method Clamp(value : Single, min : Single, max : Single) was skipped since it collides with above method
        # Method Clamp(value : Byte, min : Byte, max : Byte) was skipped since it collides with above method
        # Method Clamp(value : Int16, min : Int16, max : Int16) was skipped since it collides with above method
        # Method Clamp(value : Int32, min : Int32, max : Int32) was skipped since it collides with above method
        # Method Clamp(value : Int64, min : Int64, max : Int64) was skipped since it collides with above method
        # Method Clamp(value : IntPtr, min : IntPtr, max : IntPtr) was skipped since it collides with above method
        # Method Clamp(value : SByte, min : SByte, max : SByte) was skipped since it collides with above method
        # Method Clamp(value : UInt16, min : UInt16, max : UInt16) was skipped since it collides with above method
        # Method Clamp(value : UInt32, min : UInt32, max : UInt32) was skipped since it collides with above method
        # Method Clamp(value : UInt64, min : UInt64, max : UInt64) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: UIntPtr, min: UIntPtr, max: UIntPtr) -> UIntPtr:...
        @typing.overload
        def __call__(self, value: Decimal, min: Decimal, max: Decimal) -> Decimal:...

    # Skipped DivRem due to it being static, abstract and generic.

    DivRem : DivRem_MethodGroup
    class DivRem_MethodGroup:
        @typing.overload
        def __call__(self, left: int, right: int) -> ValueTuple_2[int, int]:...
        # Method DivRem(left : Byte, right : Byte) was skipped since it collides with above method
        # Method DivRem(left : Int16, right : Int16) was skipped since it collides with above method
        # Method DivRem(left : UInt16, right : UInt16) was skipped since it collides with above method
        # Method DivRem(left : Int32, right : Int32) was skipped since it collides with above method
        # Method DivRem(left : UInt32, right : UInt32) was skipped since it collides with above method
        # Method DivRem(left : Int64, right : Int64) was skipped since it collides with above method
        # Method DivRem(left : UInt64, right : UInt64) was skipped since it collides with above method
        # Method DivRem(left : IntPtr, right : IntPtr) was skipped since it collides with above method
        @typing.overload
        def __call__(self, left: UIntPtr, right: UIntPtr) -> ValueTuple_2[UIntPtr, UIntPtr]:...
        @typing.overload
        def __call__(self, a: int, b: int, result: clr.Reference[int]) -> int:...
        # Method DivRem(a : Int64, b : Int64, result : Int64&) was skipped since it collides with above method

    # Skipped Floor due to it being static, abstract and generic.

    Floor : Floor_MethodGroup
    class Floor_MethodGroup:
        @typing.overload
        def __call__(self, d: float) -> float:...
        @typing.overload
        def __call__(self, d: Decimal) -> Decimal:...

    # Skipped Log due to it being static, abstract and generic.

    Log : Log_MethodGroup
    class Log_MethodGroup:
        @typing.overload
        def __call__(self, d: float) -> float:...
        @typing.overload
        def __call__(self, a: float, newBase: float) -> float:...

    # Skipped Max due to it being static, abstract and generic.

    Max : Max_MethodGroup
    class Max_MethodGroup:
        @typing.overload
        def __call__(self, val1: float, val2: float) -> float:...
        # Method Max(val1 : Single, val2 : Single) was skipped since it collides with above method
        # Method Max(val1 : Byte, val2 : Byte) was skipped since it collides with above method
        # Method Max(val1 : Int16, val2 : Int16) was skipped since it collides with above method
        # Method Max(val1 : Int32, val2 : Int32) was skipped since it collides with above method
        # Method Max(val1 : Int64, val2 : Int64) was skipped since it collides with above method
        # Method Max(val1 : IntPtr, val2 : IntPtr) was skipped since it collides with above method
        # Method Max(val1 : SByte, val2 : SByte) was skipped since it collides with above method
        # Method Max(val1 : UInt16, val2 : UInt16) was skipped since it collides with above method
        # Method Max(val1 : UInt32, val2 : UInt32) was skipped since it collides with above method
        # Method Max(val1 : UInt64, val2 : UInt64) was skipped since it collides with above method
        @typing.overload
        def __call__(self, val1: UIntPtr, val2: UIntPtr) -> UIntPtr:...
        @typing.overload
        def __call__(self, val1: Decimal, val2: Decimal) -> Decimal:...

    # Skipped Min due to it being static, abstract and generic.

    Min : Min_MethodGroup
    class Min_MethodGroup:
        @typing.overload
        def __call__(self, val1: float, val2: float) -> float:...
        # Method Min(val1 : Single, val2 : Single) was skipped since it collides with above method
        # Method Min(val1 : Byte, val2 : Byte) was skipped since it collides with above method
        # Method Min(val1 : Int16, val2 : Int16) was skipped since it collides with above method
        # Method Min(val1 : Int32, val2 : Int32) was skipped since it collides with above method
        # Method Min(val1 : Int64, val2 : Int64) was skipped since it collides with above method
        # Method Min(val1 : IntPtr, val2 : IntPtr) was skipped since it collides with above method
        # Method Min(val1 : SByte, val2 : SByte) was skipped since it collides with above method
        # Method Min(val1 : UInt16, val2 : UInt16) was skipped since it collides with above method
        # Method Min(val1 : UInt32, val2 : UInt32) was skipped since it collides with above method
        # Method Min(val1 : UInt64, val2 : UInt64) was skipped since it collides with above method
        @typing.overload
        def __call__(self, val1: UIntPtr, val2: UIntPtr) -> UIntPtr:...
        @typing.overload
        def __call__(self, val1: Decimal, val2: Decimal) -> Decimal:...

    # Skipped Round due to it being static, abstract and generic.

    Round : Round_MethodGroup
    class Round_MethodGroup:
        @typing.overload
        def __call__(self, a: float) -> float:...
        @typing.overload
        def __call__(self, d: Decimal) -> Decimal:...
        @typing.overload
        def __call__(self, value: float, digits: int) -> float:...
        @typing.overload
        def __call__(self, value: float, mode: MidpointRounding) -> float:...
        @typing.overload
        def __call__(self, d: Decimal, decimals: int) -> Decimal:...
        @typing.overload
        def __call__(self, d: Decimal, mode: MidpointRounding) -> Decimal:...
        @typing.overload
        def __call__(self, value: float, digits: int, mode: MidpointRounding) -> float:...
        @typing.overload
        def __call__(self, d: Decimal, decimals: int, mode: MidpointRounding) -> Decimal:...

    # Skipped Sign due to it being static, abstract and generic.

    Sign : Sign_MethodGroup
    class Sign_MethodGroup:
        @typing.overload
        def __call__(self, value: float) -> int:...
        # Method Sign(value : Single) was skipped since it collides with above method
        # Method Sign(value : Int16) was skipped since it collides with above method
        # Method Sign(value : Int32) was skipped since it collides with above method
        # Method Sign(value : Int64) was skipped since it collides with above method
        # Method Sign(value : IntPtr) was skipped since it collides with above method
        # Method Sign(value : SByte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Decimal) -> int:...

    # Skipped Truncate due to it being static, abstract and generic.

    Truncate : Truncate_MethodGroup
    class Truncate_MethodGroup:
        @typing.overload
        def __call__(self, d: float) -> float:...
        @typing.overload
        def __call__(self, d: Decimal) -> Decimal:...



class MathF(abc.ABC):
    E : float
    PI : float
    Tau : float
    @staticmethod
    def Abs(x: float) -> float: ...
    @staticmethod
    def Acos(x: float) -> float: ...
    @staticmethod
    def Acosh(x: float) -> float: ...
    @staticmethod
    def Asin(x: float) -> float: ...
    @staticmethod
    def Asinh(x: float) -> float: ...
    @staticmethod
    def Atan(x: float) -> float: ...
    @staticmethod
    def Atan2(y: float, x: float) -> float: ...
    @staticmethod
    def Atanh(x: float) -> float: ...
    @staticmethod
    def BitDecrement(x: float) -> float: ...
    @staticmethod
    def BitIncrement(x: float) -> float: ...
    @staticmethod
    def Cbrt(x: float) -> float: ...
    @staticmethod
    def Ceiling(x: float) -> float: ...
    @staticmethod
    def CopySign(x: float, y: float) -> float: ...
    @staticmethod
    def Cos(x: float) -> float: ...
    @staticmethod
    def Cosh(x: float) -> float: ...
    @staticmethod
    def Exp(x: float) -> float: ...
    @staticmethod
    def Floor(x: float) -> float: ...
    @staticmethod
    def FusedMultiplyAdd(x: float, y: float, z: float) -> float: ...
    @staticmethod
    def IEEERemainder(x: float, y: float) -> float: ...
    @staticmethod
    def ILogB(x: float) -> int: ...
    @staticmethod
    def Log10(x: float) -> float: ...
    @staticmethod
    def Log2(x: float) -> float: ...
    @staticmethod
    def Max(x: float, y: float) -> float: ...
    @staticmethod
    def MaxMagnitude(x: float, y: float) -> float: ...
    @staticmethod
    def Min(x: float, y: float) -> float: ...
    @staticmethod
    def MinMagnitude(x: float, y: float) -> float: ...
    @staticmethod
    def Pow(x: float, y: float) -> float: ...
    @staticmethod
    def ReciprocalEstimate(x: float) -> float: ...
    @staticmethod
    def ReciprocalSqrtEstimate(x: float) -> float: ...
    @staticmethod
    def ScaleB(x: float, n: int) -> float: ...
    @staticmethod
    def Sign(x: float) -> int: ...
    @staticmethod
    def Sin(x: float) -> float: ...
    @staticmethod
    def SinCos(x: float) -> ValueTuple_2[float, float]: ...
    @staticmethod
    def Sinh(x: float) -> float: ...
    @staticmethod
    def Sqrt(x: float) -> float: ...
    @staticmethod
    def Tan(x: float) -> float: ...
    @staticmethod
    def Tanh(x: float) -> float: ...
    @staticmethod
    def Truncate(x: float) -> float: ...
    # Skipped Log due to it being static, abstract and generic.

    Log : Log_MethodGroup
    class Log_MethodGroup:
        @typing.overload
        def __call__(self, x: float) -> float:...
        @typing.overload
        def __call__(self, x: float, y: float) -> float:...

    # Skipped Round due to it being static, abstract and generic.

    Round : Round_MethodGroup
    class Round_MethodGroup:
        @typing.overload
        def __call__(self, x: float) -> float:...
        @typing.overload
        def __call__(self, x: float, digits: int) -> float:...
        @typing.overload
        def __call__(self, x: float, mode: MidpointRounding) -> float:...
        @typing.overload
        def __call__(self, x: float, digits: int, mode: MidpointRounding) -> float:...



class MemberAccessException(SystemException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, inner: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...


class Memory_GenericClasses(abc.ABCMeta):
    Generic_Memory_GenericClasses_Memory_1_T = typing.TypeVar('Generic_Memory_GenericClasses_Memory_1_T')
    def __getitem__(self, types : typing.Type[Generic_Memory_GenericClasses_Memory_1_T]) -> typing.Type[Memory_1[Generic_Memory_GenericClasses_Memory_1_T]]: ...

Memory : Memory_GenericClasses

Memory_1_T = typing.TypeVar('Memory_1_T')
class Memory_1(typing.Generic[Memory_1_T], IEquatable_1[Memory_1[Memory_1_T]]):
    @typing.overload
    def __init__(self, array: Array_1[Memory_1_T]) -> None: ...
    @typing.overload
    def __init__(self, array: Array_1[Memory_1_T], start: int, length: int) -> None: ...
    @classmethod
    @property
    def Empty(cls) -> Memory_1[Memory_1_T]: ...
    @property
    def IsEmpty(self) -> bool: ...
    @property
    def Length(self) -> int: ...
    @property
    def Span(self) -> Span_1[Memory_1_T]: ...
    def CopyTo(self, destination: Memory_1[Memory_1_T]) -> None: ...
    def GetHashCode(self) -> int: ...
    # Operator not supported op_Implicit(array: T[])
    # Operator not supported op_Implicit(segment: ArraySegment`1)
    # Operator not supported op_Implicit(memory: Memory`1)
    def Pin(self) -> MemoryHandle: ...
    def ToArray(self) -> Array_1[Memory_1_T]: ...
    def ToString(self) -> str: ...
    def TryCopyTo(self, destination: Memory_1[Memory_1_T]) -> bool: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup[Memory_1_T]
    Equals_MethodGroup_Memory_1_T = typing.TypeVar('Equals_MethodGroup_Memory_1_T')
    class Equals_MethodGroup(typing.Generic[Equals_MethodGroup_Memory_1_T]):
        Equals_MethodGroup_Memory_1_T = Memory_1.Equals_MethodGroup_Memory_1_T
        @typing.overload
        def __call__(self, other: Memory_1[Equals_MethodGroup_Memory_1_T]) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...

    # Skipped Slice due to it being static, abstract and generic.

    Slice : Slice_MethodGroup[Memory_1_T]
    Slice_MethodGroup_Memory_1_T = typing.TypeVar('Slice_MethodGroup_Memory_1_T')
    class Slice_MethodGroup(typing.Generic[Slice_MethodGroup_Memory_1_T]):
        Slice_MethodGroup_Memory_1_T = Memory_1.Slice_MethodGroup_Memory_1_T
        @typing.overload
        def __call__(self, start: int) -> Memory_1[Slice_MethodGroup_Memory_1_T]:...
        @typing.overload
        def __call__(self, start: int, length: int) -> Memory_1[Slice_MethodGroup_Memory_1_T]:...



class MemoryExtensions(abc.ABC):
    @staticmethod
    def CompareTo(span: ReadOnlySpan_1[str], other: ReadOnlySpan_1[str], comparisonType: StringComparison) -> int: ...
    @staticmethod
    def Equals(span: ReadOnlySpan_1[str], other: ReadOnlySpan_1[str], comparisonType: StringComparison) -> bool: ...
    @staticmethod
    def IsWhiteSpace(span: ReadOnlySpan_1[str]) -> bool: ...
    @staticmethod
    def ToLower(source: ReadOnlySpan_1[str], destination: Span_1[str], culture: CultureInfo) -> int: ...
    @staticmethod
    def ToLowerInvariant(source: ReadOnlySpan_1[str], destination: Span_1[str]) -> int: ...
    @staticmethod
    def ToUpper(source: ReadOnlySpan_1[str], destination: Span_1[str], culture: CultureInfo) -> int: ...
    @staticmethod
    def ToUpperInvariant(source: ReadOnlySpan_1[str], destination: Span_1[str]) -> int: ...
    # Skipped AsMemory due to it being static, abstract and generic.

    AsMemory : AsMemory_MethodGroup
    class AsMemory_MethodGroup:
        def __getitem__(self, t:typing.Type[AsMemory_1_T1]) -> AsMemory_1[AsMemory_1_T1]: ...

        AsMemory_1_T1 = typing.TypeVar('AsMemory_1_T1')
        class AsMemory_1(typing.Generic[AsMemory_1_T1]):
            AsMemory_1_T = MemoryExtensions.AsMemory_MethodGroup.AsMemory_1_T1
            @typing.overload
            def __call__(self, array: Array_1[AsMemory_1_T]) -> Memory_1[AsMemory_1_T]:...
            @typing.overload
            def __call__(self, segment: ArraySegment_1[AsMemory_1_T]) -> Memory_1[AsMemory_1_T]:...
            @typing.overload
            def __call__(self, array: Array_1[AsMemory_1_T], start: int) -> Memory_1[AsMemory_1_T]:...
            @typing.overload
            def __call__(self, segment: ArraySegment_1[AsMemory_1_T], start: int) -> Memory_1[AsMemory_1_T]:...
            @typing.overload
            def __call__(self, array: Array_1[AsMemory_1_T], range: Range) -> Memory_1[AsMemory_1_T]:...
            @typing.overload
            def __call__(self, array: Array_1[AsMemory_1_T], startIndex: Index) -> Memory_1[AsMemory_1_T]:...
            @typing.overload
            def __call__(self, array: Array_1[AsMemory_1_T], start: int, length: int) -> Memory_1[AsMemory_1_T]:...
            @typing.overload
            def __call__(self, segment: ArraySegment_1[AsMemory_1_T], start: int, length: int) -> Memory_1[AsMemory_1_T]:...

        @typing.overload
        def __call__(self, text: str) -> ReadOnlyMemory_1[str]:...
        @typing.overload
        def __call__(self, text: str, start: int) -> ReadOnlyMemory_1[str]:...
        @typing.overload
        def __call__(self, text: str, range: Range) -> ReadOnlyMemory_1[str]:...
        @typing.overload
        def __call__(self, text: str, startIndex: Index) -> ReadOnlyMemory_1[str]:...
        @typing.overload
        def __call__(self, text: str, start: int, length: int) -> ReadOnlyMemory_1[str]:...

    # Skipped AsSpan due to it being static, abstract and generic.

    AsSpan : AsSpan_MethodGroup
    class AsSpan_MethodGroup:
        def __getitem__(self, t:typing.Type[AsSpan_1_T1]) -> AsSpan_1[AsSpan_1_T1]: ...

        AsSpan_1_T1 = typing.TypeVar('AsSpan_1_T1')
        class AsSpan_1(typing.Generic[AsSpan_1_T1]):
            AsSpan_1_T = MemoryExtensions.AsSpan_MethodGroup.AsSpan_1_T1
            @typing.overload
            def __call__(self, array: Array_1[AsSpan_1_T]) -> Span_1[AsSpan_1_T]:...
            @typing.overload
            def __call__(self, segment: ArraySegment_1[AsSpan_1_T]) -> Span_1[AsSpan_1_T]:...
            @typing.overload
            def __call__(self, array: Array_1[AsSpan_1_T], start: int) -> Span_1[AsSpan_1_T]:...
            @typing.overload
            def __call__(self, segment: ArraySegment_1[AsSpan_1_T], start: int) -> Span_1[AsSpan_1_T]:...
            @typing.overload
            def __call__(self, array: Array_1[AsSpan_1_T], range: Range) -> Span_1[AsSpan_1_T]:...
            @typing.overload
            def __call__(self, array: Array_1[AsSpan_1_T], startIndex: Index) -> Span_1[AsSpan_1_T]:...
            @typing.overload
            def __call__(self, segment: ArraySegment_1[AsSpan_1_T], range: Range) -> Span_1[AsSpan_1_T]:...
            @typing.overload
            def __call__(self, segment: ArraySegment_1[AsSpan_1_T], startIndex: Index) -> Span_1[AsSpan_1_T]:...
            @typing.overload
            def __call__(self, array: Array_1[AsSpan_1_T], start: int, length: int) -> Span_1[AsSpan_1_T]:...
            @typing.overload
            def __call__(self, segment: ArraySegment_1[AsSpan_1_T], start: int, length: int) -> Span_1[AsSpan_1_T]:...

        @typing.overload
        def __call__(self, text: str) -> ReadOnlySpan_1[str]:...
        @typing.overload
        def __call__(self, text: str, start: int) -> ReadOnlySpan_1[str]:...
        @typing.overload
        def __call__(self, text: str, start: int, length: int) -> ReadOnlySpan_1[str]:...

    # Skipped BinarySearch due to it being static, abstract and generic.

    BinarySearch : BinarySearch_MethodGroup
    class BinarySearch_MethodGroup:
        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[BinarySearch_2_T1], typing.Type[BinarySearch_2_T2]]) -> BinarySearch_2[BinarySearch_2_T1, BinarySearch_2_T2]: ...

        BinarySearch_2_T1 = typing.TypeVar('BinarySearch_2_T1')
        BinarySearch_2_T2 = typing.TypeVar('BinarySearch_2_T2')
        class BinarySearch_2(typing.Generic[BinarySearch_2_T1, BinarySearch_2_T2]):
            BinarySearch_2_T = MemoryExtensions.BinarySearch_MethodGroup.BinarySearch_2_T1
            BinarySearch_2_TComparable = MemoryExtensions.BinarySearch_MethodGroup.BinarySearch_2_T2
            BinarySearch_2_TComparer = MemoryExtensions.BinarySearch_MethodGroup.BinarySearch_2_T2
            @typing.overload
            def __call__(self, span: Span_1[BinarySearch_2_T], comparable: BinarySearch_2_TComparable) -> int:...
            @typing.overload
            def __call__(self, span: ReadOnlySpan_1[BinarySearch_2_T], comparable: BinarySearch_2_TComparable) -> int:...
            @typing.overload
            def __call__(self, span: Span_1[BinarySearch_2_T], value: BinarySearch_2_T, comparer: BinarySearch_2_TComparer) -> int:...
            @typing.overload
            def __call__(self, span: ReadOnlySpan_1[BinarySearch_2_T], value: BinarySearch_2_T, comparer: BinarySearch_2_TComparer) -> int:...

        @typing.overload
        def __getitem__(self, t:typing.Type[BinarySearch_1_T1]) -> BinarySearch_1[BinarySearch_1_T1]: ...

        BinarySearch_1_T1 = typing.TypeVar('BinarySearch_1_T1')
        class BinarySearch_1(typing.Generic[BinarySearch_1_T1]):
            BinarySearch_1_T = MemoryExtensions.BinarySearch_MethodGroup.BinarySearch_1_T1
            @typing.overload
            def __call__(self, span: Span_1[BinarySearch_1_T], comparable: IComparable_1[BinarySearch_1_T]) -> int:...
            @typing.overload
            def __call__(self, span: ReadOnlySpan_1[BinarySearch_1_T], comparable: IComparable_1[BinarySearch_1_T]) -> int:...


    # Skipped Contains due to it being static, abstract and generic.

    Contains : Contains_MethodGroup
    class Contains_MethodGroup:
        def __getitem__(self, t:typing.Type[Contains_1_T1]) -> Contains_1[Contains_1_T1]: ...

        Contains_1_T1 = typing.TypeVar('Contains_1_T1')
        class Contains_1(typing.Generic[Contains_1_T1]):
            Contains_1_T = MemoryExtensions.Contains_MethodGroup.Contains_1_T1
            @typing.overload
            def __call__(self, span: Span_1[Contains_1_T], value: Contains_1_T) -> bool:...
            @typing.overload
            def __call__(self, span: ReadOnlySpan_1[Contains_1_T], value: Contains_1_T) -> bool:...

        def __call__(self, span: ReadOnlySpan_1[str], value: ReadOnlySpan_1[str], comparisonType: StringComparison) -> bool:...

    # Skipped CopyTo due to it being static, abstract and generic.

    CopyTo : CopyTo_MethodGroup
    class CopyTo_MethodGroup:
        def __getitem__(self, t:typing.Type[CopyTo_1_T1]) -> CopyTo_1[CopyTo_1_T1]: ...

        CopyTo_1_T1 = typing.TypeVar('CopyTo_1_T1')
        class CopyTo_1(typing.Generic[CopyTo_1_T1]):
            CopyTo_1_T = MemoryExtensions.CopyTo_MethodGroup.CopyTo_1_T1
            @typing.overload
            def __call__(self, source: Array_1[CopyTo_1_T], destination: Span_1[CopyTo_1_T]) -> None:...
            @typing.overload
            def __call__(self, source: Array_1[CopyTo_1_T], destination: Memory_1[CopyTo_1_T]) -> None:...


    # Skipped EndsWith due to it being static, abstract and generic.

    EndsWith : EndsWith_MethodGroup
    class EndsWith_MethodGroup:
        def __getitem__(self, t:typing.Type[EndsWith_1_T1]) -> EndsWith_1[EndsWith_1_T1]: ...

        EndsWith_1_T1 = typing.TypeVar('EndsWith_1_T1')
        class EndsWith_1(typing.Generic[EndsWith_1_T1]):
            EndsWith_1_T = MemoryExtensions.EndsWith_MethodGroup.EndsWith_1_T1
            @typing.overload
            def __call__(self, span: Span_1[EndsWith_1_T], value: ReadOnlySpan_1[EndsWith_1_T]) -> bool:...
            @typing.overload
            def __call__(self, span: ReadOnlySpan_1[EndsWith_1_T], value: ReadOnlySpan_1[EndsWith_1_T]) -> bool:...

        def __call__(self, span: ReadOnlySpan_1[str], value: ReadOnlySpan_1[str], comparisonType: StringComparison) -> bool:...

    # Skipped EnumerateLines due to it being static, abstract and generic.

    EnumerateLines : EnumerateLines_MethodGroup
    class EnumerateLines_MethodGroup:
        @typing.overload
        def __call__(self, span: ReadOnlySpan_1[str]) -> SpanLineEnumerator:...
        @typing.overload
        def __call__(self, span: Span_1[str]) -> SpanLineEnumerator:...

    # Skipped EnumerateRunes due to it being static, abstract and generic.

    EnumerateRunes : EnumerateRunes_MethodGroup
    class EnumerateRunes_MethodGroup:
        @typing.overload
        def __call__(self, span: ReadOnlySpan_1[str]) -> SpanRuneEnumerator:...
        @typing.overload
        def __call__(self, span: Span_1[str]) -> SpanRuneEnumerator:...

    # Skipped IndexOf due to it being static, abstract and generic.

    IndexOf : IndexOf_MethodGroup
    class IndexOf_MethodGroup:
        def __getitem__(self, t:typing.Type[IndexOf_1_T1]) -> IndexOf_1[IndexOf_1_T1]: ...

        IndexOf_1_T1 = typing.TypeVar('IndexOf_1_T1')
        class IndexOf_1(typing.Generic[IndexOf_1_T1]):
            IndexOf_1_T = MemoryExtensions.IndexOf_MethodGroup.IndexOf_1_T1
            @typing.overload
            def __call__(self, span: Span_1[IndexOf_1_T], value: ReadOnlySpan_1[IndexOf_1_T]) -> int:...
            @typing.overload
            def __call__(self, span: ReadOnlySpan_1[IndexOf_1_T], value: ReadOnlySpan_1[IndexOf_1_T]) -> int:...
            @typing.overload
            def __call__(self, span: Span_1[IndexOf_1_T], value: IndexOf_1_T) -> int:...
            @typing.overload
            def __call__(self, span: ReadOnlySpan_1[IndexOf_1_T], value: IndexOf_1_T) -> int:...

        def __call__(self, span: ReadOnlySpan_1[str], value: ReadOnlySpan_1[str], comparisonType: StringComparison) -> int:...

    # Skipped IndexOfAny due to it being static, abstract and generic.

    IndexOfAny : IndexOfAny_MethodGroup
    class IndexOfAny_MethodGroup:
        def __getitem__(self, t:typing.Type[IndexOfAny_1_T1]) -> IndexOfAny_1[IndexOfAny_1_T1]: ...

        IndexOfAny_1_T1 = typing.TypeVar('IndexOfAny_1_T1')
        class IndexOfAny_1(typing.Generic[IndexOfAny_1_T1]):
            IndexOfAny_1_T = MemoryExtensions.IndexOfAny_MethodGroup.IndexOfAny_1_T1
            @typing.overload
            def __call__(self, span: Span_1[IndexOfAny_1_T], values: ReadOnlySpan_1[IndexOfAny_1_T]) -> int:...
            @typing.overload
            def __call__(self, span: ReadOnlySpan_1[IndexOfAny_1_T], values: ReadOnlySpan_1[IndexOfAny_1_T]) -> int:...
            @typing.overload
            def __call__(self, span: Span_1[IndexOfAny_1_T], value0: IndexOfAny_1_T, value1: IndexOfAny_1_T) -> int:...
            @typing.overload
            def __call__(self, span: ReadOnlySpan_1[IndexOfAny_1_T], value0: IndexOfAny_1_T, value1: IndexOfAny_1_T) -> int:...
            @typing.overload
            def __call__(self, span: Span_1[IndexOfAny_1_T], value0: IndexOfAny_1_T, value1: IndexOfAny_1_T, value2: IndexOfAny_1_T) -> int:...
            @typing.overload
            def __call__(self, span: ReadOnlySpan_1[IndexOfAny_1_T], value0: IndexOfAny_1_T, value1: IndexOfAny_1_T, value2: IndexOfAny_1_T) -> int:...


    # Skipped LastIndexOf due to it being static, abstract and generic.

    LastIndexOf : LastIndexOf_MethodGroup
    class LastIndexOf_MethodGroup:
        def __getitem__(self, t:typing.Type[LastIndexOf_1_T1]) -> LastIndexOf_1[LastIndexOf_1_T1]: ...

        LastIndexOf_1_T1 = typing.TypeVar('LastIndexOf_1_T1')
        class LastIndexOf_1(typing.Generic[LastIndexOf_1_T1]):
            LastIndexOf_1_T = MemoryExtensions.LastIndexOf_MethodGroup.LastIndexOf_1_T1
            @typing.overload
            def __call__(self, span: Span_1[LastIndexOf_1_T], value: ReadOnlySpan_1[LastIndexOf_1_T]) -> int:...
            @typing.overload
            def __call__(self, span: ReadOnlySpan_1[LastIndexOf_1_T], value: ReadOnlySpan_1[LastIndexOf_1_T]) -> int:...
            @typing.overload
            def __call__(self, span: Span_1[LastIndexOf_1_T], value: LastIndexOf_1_T) -> int:...
            @typing.overload
            def __call__(self, span: ReadOnlySpan_1[LastIndexOf_1_T], value: LastIndexOf_1_T) -> int:...

        def __call__(self, span: ReadOnlySpan_1[str], value: ReadOnlySpan_1[str], comparisonType: StringComparison) -> int:...

    # Skipped LastIndexOfAny due to it being static, abstract and generic.

    LastIndexOfAny : LastIndexOfAny_MethodGroup
    class LastIndexOfAny_MethodGroup:
        def __getitem__(self, t:typing.Type[LastIndexOfAny_1_T1]) -> LastIndexOfAny_1[LastIndexOfAny_1_T1]: ...

        LastIndexOfAny_1_T1 = typing.TypeVar('LastIndexOfAny_1_T1')
        class LastIndexOfAny_1(typing.Generic[LastIndexOfAny_1_T1]):
            LastIndexOfAny_1_T = MemoryExtensions.LastIndexOfAny_MethodGroup.LastIndexOfAny_1_T1
            @typing.overload
            def __call__(self, span: Span_1[LastIndexOfAny_1_T], values: ReadOnlySpan_1[LastIndexOfAny_1_T]) -> int:...
            @typing.overload
            def __call__(self, span: ReadOnlySpan_1[LastIndexOfAny_1_T], values: ReadOnlySpan_1[LastIndexOfAny_1_T]) -> int:...
            @typing.overload
            def __call__(self, span: Span_1[LastIndexOfAny_1_T], value0: LastIndexOfAny_1_T, value1: LastIndexOfAny_1_T) -> int:...
            @typing.overload
            def __call__(self, span: ReadOnlySpan_1[LastIndexOfAny_1_T], value0: LastIndexOfAny_1_T, value1: LastIndexOfAny_1_T) -> int:...
            @typing.overload
            def __call__(self, span: Span_1[LastIndexOfAny_1_T], value0: LastIndexOfAny_1_T, value1: LastIndexOfAny_1_T, value2: LastIndexOfAny_1_T) -> int:...
            @typing.overload
            def __call__(self, span: ReadOnlySpan_1[LastIndexOfAny_1_T], value0: LastIndexOfAny_1_T, value1: LastIndexOfAny_1_T, value2: LastIndexOfAny_1_T) -> int:...


    # Skipped Overlaps due to it being static, abstract and generic.

    Overlaps : Overlaps_MethodGroup
    class Overlaps_MethodGroup:
        def __getitem__(self, t:typing.Type[Overlaps_1_T1]) -> Overlaps_1[Overlaps_1_T1]: ...

        Overlaps_1_T1 = typing.TypeVar('Overlaps_1_T1')
        class Overlaps_1(typing.Generic[Overlaps_1_T1]):
            Overlaps_1_T = MemoryExtensions.Overlaps_MethodGroup.Overlaps_1_T1
            @typing.overload
            def __call__(self, span: Span_1[Overlaps_1_T], other: ReadOnlySpan_1[Overlaps_1_T]) -> bool:...
            @typing.overload
            def __call__(self, span: ReadOnlySpan_1[Overlaps_1_T], other: ReadOnlySpan_1[Overlaps_1_T]) -> bool:...
            @typing.overload
            def __call__(self, span: Span_1[Overlaps_1_T], other: ReadOnlySpan_1[Overlaps_1_T], elementOffset: clr.Reference[int]) -> bool:...
            @typing.overload
            def __call__(self, span: ReadOnlySpan_1[Overlaps_1_T], other: ReadOnlySpan_1[Overlaps_1_T], elementOffset: clr.Reference[int]) -> bool:...


    # Skipped Reverse due to it being static, abstract and generic.

    Reverse : Reverse_MethodGroup
    class Reverse_MethodGroup:
        def __getitem__(self, t:typing.Type[Reverse_1_T1]) -> Reverse_1[Reverse_1_T1]: ...

        Reverse_1_T1 = typing.TypeVar('Reverse_1_T1')
        class Reverse_1(typing.Generic[Reverse_1_T1]):
            Reverse_1_T = MemoryExtensions.Reverse_MethodGroup.Reverse_1_T1
            def __call__(self, span: Span_1[Reverse_1_T]) -> None:...


    # Skipped SequenceCompareTo due to it being static, abstract and generic.

    SequenceCompareTo : SequenceCompareTo_MethodGroup
    class SequenceCompareTo_MethodGroup:
        def __getitem__(self, t:typing.Type[SequenceCompareTo_1_T1]) -> SequenceCompareTo_1[SequenceCompareTo_1_T1]: ...

        SequenceCompareTo_1_T1 = typing.TypeVar('SequenceCompareTo_1_T1')
        class SequenceCompareTo_1(typing.Generic[SequenceCompareTo_1_T1]):
            SequenceCompareTo_1_T = MemoryExtensions.SequenceCompareTo_MethodGroup.SequenceCompareTo_1_T1
            @typing.overload
            def __call__(self, span: Span_1[SequenceCompareTo_1_T], other: ReadOnlySpan_1[SequenceCompareTo_1_T]) -> int:...
            @typing.overload
            def __call__(self, span: ReadOnlySpan_1[SequenceCompareTo_1_T], other: ReadOnlySpan_1[SequenceCompareTo_1_T]) -> int:...


    # Skipped SequenceEqual due to it being static, abstract and generic.

    SequenceEqual : SequenceEqual_MethodGroup
    class SequenceEqual_MethodGroup:
        def __getitem__(self, t:typing.Type[SequenceEqual_1_T1]) -> SequenceEqual_1[SequenceEqual_1_T1]: ...

        SequenceEqual_1_T1 = typing.TypeVar('SequenceEqual_1_T1')
        class SequenceEqual_1(typing.Generic[SequenceEqual_1_T1]):
            SequenceEqual_1_T = MemoryExtensions.SequenceEqual_MethodGroup.SequenceEqual_1_T1
            @typing.overload
            def __call__(self, span: Span_1[SequenceEqual_1_T], other: ReadOnlySpan_1[SequenceEqual_1_T]) -> bool:...
            @typing.overload
            def __call__(self, span: ReadOnlySpan_1[SequenceEqual_1_T], other: ReadOnlySpan_1[SequenceEqual_1_T]) -> bool:...
            @typing.overload
            def __call__(self, span: Span_1[SequenceEqual_1_T], other: ReadOnlySpan_1[SequenceEqual_1_T], comparer: IEqualityComparer_1[SequenceEqual_1_T] = ...) -> bool:...
            @typing.overload
            def __call__(self, span: ReadOnlySpan_1[SequenceEqual_1_T], other: ReadOnlySpan_1[SequenceEqual_1_T], comparer: IEqualityComparer_1[SequenceEqual_1_T] = ...) -> bool:...


    # Skipped Sort due to it being static, abstract and generic.

    Sort : Sort_MethodGroup
    class Sort_MethodGroup:
        @typing.overload
        def __getitem__(self, t:typing.Type[Sort_1_T1]) -> Sort_1[Sort_1_T1]: ...

        Sort_1_T1 = typing.TypeVar('Sort_1_T1')
        class Sort_1(typing.Generic[Sort_1_T1]):
            Sort_1_T = MemoryExtensions.Sort_MethodGroup.Sort_1_T1
            @typing.overload
            def __call__(self, span: Span_1[Sort_1_T]) -> None:...
            @typing.overload
            def __call__(self, span: Span_1[Sort_1_T], comparison: Comparison_1[Sort_1_T]) -> None:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Sort_2_T1], typing.Type[Sort_2_T2]]) -> Sort_2[Sort_2_T1, Sort_2_T2]: ...

        Sort_2_T1 = typing.TypeVar('Sort_2_T1')
        Sort_2_T2 = typing.TypeVar('Sort_2_T2')
        class Sort_2(typing.Generic[Sort_2_T1, Sort_2_T2]):
            Sort_2_TKey = MemoryExtensions.Sort_MethodGroup.Sort_2_T1
            Sort_2_T = MemoryExtensions.Sort_MethodGroup.Sort_2_T1
            Sort_2_TValue = MemoryExtensions.Sort_MethodGroup.Sort_2_T2
            Sort_2_TComparer = MemoryExtensions.Sort_MethodGroup.Sort_2_T2
            @typing.overload
            def __call__(self, keys: Span_1[Sort_2_TKey], items: Span_1[Sort_2_TValue]) -> None:...
            @typing.overload
            def __call__(self, span: Span_1[Sort_2_T], comparer: Sort_2_TComparer) -> None:...
            @typing.overload
            def __call__(self, keys: Span_1[Sort_2_TKey], items: Span_1[Sort_2_TValue], comparison: Comparison_1[Sort_2_TKey]) -> None:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Sort_3_T1], typing.Type[Sort_3_T2], typing.Type[Sort_3_T3]]) -> Sort_3[Sort_3_T1, Sort_3_T2, Sort_3_T3]: ...

        Sort_3_T1 = typing.TypeVar('Sort_3_T1')
        Sort_3_T2 = typing.TypeVar('Sort_3_T2')
        Sort_3_T3 = typing.TypeVar('Sort_3_T3')
        class Sort_3(typing.Generic[Sort_3_T1, Sort_3_T2, Sort_3_T3]):
            Sort_3_TKey = MemoryExtensions.Sort_MethodGroup.Sort_3_T1
            Sort_3_TValue = MemoryExtensions.Sort_MethodGroup.Sort_3_T2
            Sort_3_TComparer = MemoryExtensions.Sort_MethodGroup.Sort_3_T3
            def __call__(self, keys: Span_1[Sort_3_TKey], items: Span_1[Sort_3_TValue], comparer: Sort_3_TComparer) -> None:...


    # Skipped StartsWith due to it being static, abstract and generic.

    StartsWith : StartsWith_MethodGroup
    class StartsWith_MethodGroup:
        def __getitem__(self, t:typing.Type[StartsWith_1_T1]) -> StartsWith_1[StartsWith_1_T1]: ...

        StartsWith_1_T1 = typing.TypeVar('StartsWith_1_T1')
        class StartsWith_1(typing.Generic[StartsWith_1_T1]):
            StartsWith_1_T = MemoryExtensions.StartsWith_MethodGroup.StartsWith_1_T1
            @typing.overload
            def __call__(self, span: Span_1[StartsWith_1_T], value: ReadOnlySpan_1[StartsWith_1_T]) -> bool:...
            @typing.overload
            def __call__(self, span: ReadOnlySpan_1[StartsWith_1_T], value: ReadOnlySpan_1[StartsWith_1_T]) -> bool:...

        def __call__(self, span: ReadOnlySpan_1[str], value: ReadOnlySpan_1[str], comparisonType: StringComparison) -> bool:...

    # Skipped Trim due to it being static, abstract and generic.

    Trim : Trim_MethodGroup
    class Trim_MethodGroup:
        def __getitem__(self, t:typing.Type[Trim_1_T1]) -> Trim_1[Trim_1_T1]: ...

        Trim_1_T1 = typing.TypeVar('Trim_1_T1')
        class Trim_1(typing.Generic[Trim_1_T1]):
            Trim_1_T = MemoryExtensions.Trim_MethodGroup.Trim_1_T1
            @typing.overload
            def __call__(self, memory: ReadOnlyMemory_1[Trim_1_T], trimElements: ReadOnlySpan_1[Trim_1_T]) -> ReadOnlyMemory_1[Trim_1_T]:...
            @typing.overload
            def __call__(self, memory: Memory_1[Trim_1_T], trimElements: ReadOnlySpan_1[Trim_1_T]) -> Memory_1[Trim_1_T]:...
            @typing.overload
            def __call__(self, span: Span_1[Trim_1_T], trimElements: ReadOnlySpan_1[Trim_1_T]) -> Span_1[Trim_1_T]:...
            @typing.overload
            def __call__(self, span: ReadOnlySpan_1[Trim_1_T], trimElements: ReadOnlySpan_1[Trim_1_T]) -> ReadOnlySpan_1[Trim_1_T]:...
            @typing.overload
            def __call__(self, memory: Memory_1[Trim_1_T], trimElement: Trim_1_T) -> Memory_1[Trim_1_T]:...
            @typing.overload
            def __call__(self, memory: ReadOnlyMemory_1[Trim_1_T], trimElement: Trim_1_T) -> ReadOnlyMemory_1[Trim_1_T]:...
            @typing.overload
            def __call__(self, span: Span_1[Trim_1_T], trimElement: Trim_1_T) -> Span_1[Trim_1_T]:...
            @typing.overload
            def __call__(self, span: ReadOnlySpan_1[Trim_1_T], trimElement: Trim_1_T) -> ReadOnlySpan_1[Trim_1_T]:...

        @typing.overload
        def __call__(self, memory: Memory_1[str]) -> Memory_1[str]:...
        @typing.overload
        def __call__(self, memory: ReadOnlyMemory_1[str]) -> ReadOnlyMemory_1[str]:...
        @typing.overload
        def __call__(self, span: ReadOnlySpan_1[str]) -> ReadOnlySpan_1[str]:...
        @typing.overload
        def __call__(self, span: Span_1[str]) -> Span_1[str]:...
        @typing.overload
        def __call__(self, span: ReadOnlySpan_1[str], trimChar: str) -> ReadOnlySpan_1[str]:...
        @typing.overload
        def __call__(self, span: ReadOnlySpan_1[str], trimChars: ReadOnlySpan_1[str]) -> ReadOnlySpan_1[str]:...

    # Skipped TrimEnd due to it being static, abstract and generic.

    TrimEnd : TrimEnd_MethodGroup
    class TrimEnd_MethodGroup:
        def __getitem__(self, t:typing.Type[TrimEnd_1_T1]) -> TrimEnd_1[TrimEnd_1_T1]: ...

        TrimEnd_1_T1 = typing.TypeVar('TrimEnd_1_T1')
        class TrimEnd_1(typing.Generic[TrimEnd_1_T1]):
            TrimEnd_1_T = MemoryExtensions.TrimEnd_MethodGroup.TrimEnd_1_T1
            @typing.overload
            def __call__(self, memory: Memory_1[TrimEnd_1_T], trimElements: ReadOnlySpan_1[TrimEnd_1_T]) -> Memory_1[TrimEnd_1_T]:...
            @typing.overload
            def __call__(self, memory: ReadOnlyMemory_1[TrimEnd_1_T], trimElements: ReadOnlySpan_1[TrimEnd_1_T]) -> ReadOnlyMemory_1[TrimEnd_1_T]:...
            @typing.overload
            def __call__(self, span: Span_1[TrimEnd_1_T], trimElements: ReadOnlySpan_1[TrimEnd_1_T]) -> Span_1[TrimEnd_1_T]:...
            @typing.overload
            def __call__(self, span: ReadOnlySpan_1[TrimEnd_1_T], trimElements: ReadOnlySpan_1[TrimEnd_1_T]) -> ReadOnlySpan_1[TrimEnd_1_T]:...
            @typing.overload
            def __call__(self, memory: Memory_1[TrimEnd_1_T], trimElement: TrimEnd_1_T) -> Memory_1[TrimEnd_1_T]:...
            @typing.overload
            def __call__(self, memory: ReadOnlyMemory_1[TrimEnd_1_T], trimElement: TrimEnd_1_T) -> ReadOnlyMemory_1[TrimEnd_1_T]:...
            @typing.overload
            def __call__(self, span: Span_1[TrimEnd_1_T], trimElement: TrimEnd_1_T) -> Span_1[TrimEnd_1_T]:...
            @typing.overload
            def __call__(self, span: ReadOnlySpan_1[TrimEnd_1_T], trimElement: TrimEnd_1_T) -> ReadOnlySpan_1[TrimEnd_1_T]:...

        @typing.overload
        def __call__(self, memory: Memory_1[str]) -> Memory_1[str]:...
        @typing.overload
        def __call__(self, memory: ReadOnlyMemory_1[str]) -> ReadOnlyMemory_1[str]:...
        @typing.overload
        def __call__(self, span: ReadOnlySpan_1[str]) -> ReadOnlySpan_1[str]:...
        @typing.overload
        def __call__(self, span: Span_1[str]) -> Span_1[str]:...
        @typing.overload
        def __call__(self, span: ReadOnlySpan_1[str], trimChar: str) -> ReadOnlySpan_1[str]:...
        @typing.overload
        def __call__(self, span: ReadOnlySpan_1[str], trimChars: ReadOnlySpan_1[str]) -> ReadOnlySpan_1[str]:...

    # Skipped TrimStart due to it being static, abstract and generic.

    TrimStart : TrimStart_MethodGroup
    class TrimStart_MethodGroup:
        def __getitem__(self, t:typing.Type[TrimStart_1_T1]) -> TrimStart_1[TrimStart_1_T1]: ...

        TrimStart_1_T1 = typing.TypeVar('TrimStart_1_T1')
        class TrimStart_1(typing.Generic[TrimStart_1_T1]):
            TrimStart_1_T = MemoryExtensions.TrimStart_MethodGroup.TrimStart_1_T1
            @typing.overload
            def __call__(self, memory: Memory_1[TrimStart_1_T], trimElements: ReadOnlySpan_1[TrimStart_1_T]) -> Memory_1[TrimStart_1_T]:...
            @typing.overload
            def __call__(self, memory: ReadOnlyMemory_1[TrimStart_1_T], trimElements: ReadOnlySpan_1[TrimStart_1_T]) -> ReadOnlyMemory_1[TrimStart_1_T]:...
            @typing.overload
            def __call__(self, span: Span_1[TrimStart_1_T], trimElements: ReadOnlySpan_1[TrimStart_1_T]) -> Span_1[TrimStart_1_T]:...
            @typing.overload
            def __call__(self, span: ReadOnlySpan_1[TrimStart_1_T], trimElements: ReadOnlySpan_1[TrimStart_1_T]) -> ReadOnlySpan_1[TrimStart_1_T]:...
            @typing.overload
            def __call__(self, memory: Memory_1[TrimStart_1_T], trimElement: TrimStart_1_T) -> Memory_1[TrimStart_1_T]:...
            @typing.overload
            def __call__(self, memory: ReadOnlyMemory_1[TrimStart_1_T], trimElement: TrimStart_1_T) -> ReadOnlyMemory_1[TrimStart_1_T]:...
            @typing.overload
            def __call__(self, span: Span_1[TrimStart_1_T], trimElement: TrimStart_1_T) -> Span_1[TrimStart_1_T]:...
            @typing.overload
            def __call__(self, span: ReadOnlySpan_1[TrimStart_1_T], trimElement: TrimStart_1_T) -> ReadOnlySpan_1[TrimStart_1_T]:...

        @typing.overload
        def __call__(self, memory: Memory_1[str]) -> Memory_1[str]:...
        @typing.overload
        def __call__(self, memory: ReadOnlyMemory_1[str]) -> ReadOnlyMemory_1[str]:...
        @typing.overload
        def __call__(self, span: ReadOnlySpan_1[str]) -> ReadOnlySpan_1[str]:...
        @typing.overload
        def __call__(self, span: Span_1[str]) -> Span_1[str]:...
        @typing.overload
        def __call__(self, span: ReadOnlySpan_1[str], trimChar: str) -> ReadOnlySpan_1[str]:...
        @typing.overload
        def __call__(self, span: ReadOnlySpan_1[str], trimChars: ReadOnlySpan_1[str]) -> ReadOnlySpan_1[str]:...

    # Skipped TryWrite due to it being static, abstract and generic.

    TryWrite : TryWrite_MethodGroup
    class TryWrite_MethodGroup:
        @typing.overload
        def __call__(self, destination: Span_1[str], handler: clr.Reference[MemoryExtensions.TryWriteInterpolatedStringHandler], charsWritten: clr.Reference[int]) -> bool:...
        @typing.overload
        def __call__(self, destination: Span_1[str], provider: IFormatProvider, handler: clr.Reference[MemoryExtensions.TryWriteInterpolatedStringHandler], charsWritten: clr.Reference[int]) -> bool:...


    class TryWriteInterpolatedStringHandler:
        @typing.overload
        def __init__(self, literalLength: int, formattedCount: int, destination: Span_1[str], provider: IFormatProvider, shouldAppend: clr.Reference[bool]) -> None: ...
        @typing.overload
        def __init__(self, literalLength: int, formattedCount: int, destination: Span_1[str], shouldAppend: clr.Reference[bool]) -> None: ...
        def AppendLiteral(self, value: str) -> bool: ...
        # Skipped AppendFormatted due to it being static, abstract and generic.

        AppendFormatted : AppendFormatted_MethodGroup
        class AppendFormatted_MethodGroup:
            def __getitem__(self, t:typing.Type[AppendFormatted_1_T1]) -> AppendFormatted_1[AppendFormatted_1_T1]: ...

            AppendFormatted_1_T1 = typing.TypeVar('AppendFormatted_1_T1')
            class AppendFormatted_1(typing.Generic[AppendFormatted_1_T1]):
                AppendFormatted_1_T = MemoryExtensions.TryWriteInterpolatedStringHandler.AppendFormatted_MethodGroup.AppendFormatted_1_T1
                @typing.overload
                def __call__(self, value: AppendFormatted_1_T) -> bool:...
                @typing.overload
                def __call__(self, value: AppendFormatted_1_T, alignment: int) -> bool:...
                @typing.overload
                def __call__(self, value: AppendFormatted_1_T, format: str) -> bool:...
                @typing.overload
                def __call__(self, value: AppendFormatted_1_T, alignment: int, format: str) -> bool:...

            @typing.overload
            def __call__(self, value: ReadOnlySpan_1[str]) -> bool:...
            @typing.overload
            def __call__(self, value: str) -> bool:...
            @typing.overload
            def __call__(self, value: ReadOnlySpan_1[str], alignment: int = ..., format: str = ...) -> bool:...
            @typing.overload
            def __call__(self, value: str, alignment: int = ..., format: str = ...) -> bool:...
            @typing.overload
            def __call__(self, value: typing.Any, alignment: int = ..., format: str = ...) -> bool:...




class MethodAccessException(MemberAccessException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, inner: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...


class MidpointRounding(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    ToEven : MidpointRounding # 0
    AwayFromZero : MidpointRounding # 1
    ToZero : MidpointRounding # 2
    ToNegativeInfinity : MidpointRounding # 3
    ToPositiveInfinity : MidpointRounding # 4


class MissingFieldException(MissingMemberException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, className: str, fieldName: str) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, inner: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...


class MissingMemberException(MemberAccessException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, className: str, memberName: str) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, inner: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...


class MissingMethodException(MissingMemberException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, className: str, methodName: str) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, inner: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...


class ModuleHandle:
    EmptyHandle : ModuleHandle
    @property
    def MDStreamVersion(self) -> int: ...
    def GetHashCode(self) -> int: ...
    def GetRuntimeFieldHandleFromMetadataToken(self, fieldToken: int) -> RuntimeFieldHandle: ...
    def GetRuntimeMethodHandleFromMetadataToken(self, methodToken: int) -> RuntimeMethodHandle: ...
    def GetRuntimeTypeHandleFromMetadataToken(self, typeToken: int) -> RuntimeTypeHandle: ...
    def __eq__(self, left: ModuleHandle, right: ModuleHandle) -> bool: ...
    def __ne__(self, left: ModuleHandle, right: ModuleHandle) -> bool: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, handle: ModuleHandle) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...

    # Skipped ResolveFieldHandle due to it being static, abstract and generic.

    ResolveFieldHandle : ResolveFieldHandle_MethodGroup
    class ResolveFieldHandle_MethodGroup:
        @typing.overload
        def __call__(self, fieldToken: int) -> RuntimeFieldHandle:...
        @typing.overload
        def __call__(self, fieldToken: int, typeInstantiationContext: Array_1[RuntimeTypeHandle], methodInstantiationContext: Array_1[RuntimeTypeHandle]) -> RuntimeFieldHandle:...

    # Skipped ResolveMethodHandle due to it being static, abstract and generic.

    ResolveMethodHandle : ResolveMethodHandle_MethodGroup
    class ResolveMethodHandle_MethodGroup:
        @typing.overload
        def __call__(self, methodToken: int) -> RuntimeMethodHandle:...
        @typing.overload
        def __call__(self, methodToken: int, typeInstantiationContext: Array_1[RuntimeTypeHandle], methodInstantiationContext: Array_1[RuntimeTypeHandle]) -> RuntimeMethodHandle:...

    # Skipped ResolveTypeHandle due to it being static, abstract and generic.

    ResolveTypeHandle : ResolveTypeHandle_MethodGroup
    class ResolveTypeHandle_MethodGroup:
        @typing.overload
        def __call__(self, typeToken: int) -> RuntimeTypeHandle:...
        @typing.overload
        def __call__(self, typeToken: int, typeInstantiationContext: Array_1[RuntimeTypeHandle], methodInstantiationContext: Array_1[RuntimeTypeHandle]) -> RuntimeTypeHandle:...



class MTAThreadAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class MulticastDelegate(Delegate):
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def Equals(self, obj: typing.Any) -> bool: ...
    def GetHashCode(self) -> int: ...
    def GetInvocationList(self) -> Array_1[Delegate]: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...
    def __eq__(self, d1: MulticastDelegate, d2: MulticastDelegate) -> bool: ...
    def __ne__(self, d1: MulticastDelegate, d2: MulticastDelegate) -> bool: ...


class MulticastNotSupportedException(SystemException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, inner: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...


class NonSerializedAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class NotFiniteNumberException(ArithmeticException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, innerException: Exception) -> None: ...
    @typing.overload
    def __init__(self, message: str, offendingNumber: float) -> None: ...
    @typing.overload
    def __init__(self, message: str, offendingNumber: float, innerException: Exception) -> None: ...
    @typing.overload
    def __init__(self, offendingNumber: float) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def OffendingNumber(self) -> float: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...


class NotImplementedException(SystemException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, inner: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...


class NotSupportedException(SystemException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, innerException: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...


class Nullable_GenericClasses(abc.ABCMeta):
    Generic_Nullable_GenericClasses_Nullable_1_T = typing.TypeVar('Generic_Nullable_GenericClasses_Nullable_1_T')
    def __getitem__(self, types : typing.Type[Generic_Nullable_GenericClasses_Nullable_1_T]) -> typing.Type[Nullable_1[Generic_Nullable_GenericClasses_Nullable_1_T]]: ...

class Nullable(Nullable_0, metaclass =Nullable_GenericClasses): ...

class Nullable_0(abc.ABC):
    @staticmethod
    def GetUnderlyingType(nullableType: typing.Type[typing.Any]) -> typing.Type[typing.Any]: ...
    # Skipped Compare due to it being static, abstract and generic.

    Compare : Compare_MethodGroup
    class Compare_MethodGroup:
        def __getitem__(self, t:typing.Type[Compare_1_T1]) -> Compare_1[Compare_1_T1]: ...

        Compare_1_T1 = typing.TypeVar('Compare_1_T1')
        class Compare_1(typing.Generic[Compare_1_T1]):
            Compare_1_T = Nullable_0.Compare_MethodGroup.Compare_1_T1
            def __call__(self, n1: typing.Optional[Compare_1_T], n2: typing.Optional[Compare_1_T]) -> int:...


    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        def __getitem__(self, t:typing.Type[Equals_1_T1]) -> Equals_1[Equals_1_T1]: ...

        Equals_1_T1 = typing.TypeVar('Equals_1_T1')
        class Equals_1(typing.Generic[Equals_1_T1]):
            Equals_1_T = Nullable_0.Equals_MethodGroup.Equals_1_T1
            def __call__(self, n1: typing.Optional[Equals_1_T], n2: typing.Optional[Equals_1_T]) -> bool:...




Nullable_1_T = typing.TypeVar('Nullable_1_T')
class Nullable_1(typing.Generic[Nullable_1_T]):
    def __init__(self, value: Nullable_1_T) -> None: ...
    @property
    def HasValue(self) -> bool: ...
    @property
    def Value(self) -> Nullable_1_T: ...
    def Equals(self, other: typing.Any) -> bool: ...
    def GetHashCode(self) -> int: ...
    # Operator not supported op_Explicit(value: Nullable`1)
    # Operator not supported op_Implicit(value: T)
    def ToString(self) -> str: ...
    # Skipped GetValueOrDefault due to it being static, abstract and generic.

    GetValueOrDefault : GetValueOrDefault_MethodGroup[Nullable_1_T]
    GetValueOrDefault_MethodGroup_Nullable_1_T = typing.TypeVar('GetValueOrDefault_MethodGroup_Nullable_1_T')
    class GetValueOrDefault_MethodGroup(typing.Generic[GetValueOrDefault_MethodGroup_Nullable_1_T]):
        GetValueOrDefault_MethodGroup_Nullable_1_T = Nullable_1.GetValueOrDefault_MethodGroup_Nullable_1_T
        @typing.overload
        def __call__(self) -> GetValueOrDefault_MethodGroup_Nullable_1_T:...
        @typing.overload
        def __call__(self, defaultValue: GetValueOrDefault_MethodGroup_Nullable_1_T) -> GetValueOrDefault_MethodGroup_Nullable_1_T:...



class NullReferenceException(SystemException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, innerException: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...


class Object:
    def __init__(self) -> None: ...
    def GetHashCode(self) -> int: ...
    def GetType(self) -> typing.Type[typing.Any]: ...
    @staticmethod
    def ReferenceEquals(objA: typing.Any, objB: typing.Any) -> bool: ...
    def ToString(self) -> str: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...
        @typing.overload
        def __call__(self, objA: typing.Any, objB: typing.Any) -> bool:...



class ObjectDisposedException(InvalidOperationException):
    @typing.overload
    def __init__(self, message: str, innerException: Exception) -> None: ...
    @typing.overload
    def __init__(self, objectName: str) -> None: ...
    @typing.overload
    def __init__(self, objectName: str, message: str) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def ObjectName(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...


class ObsoleteAttribute(Attribute):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, error: bool) -> None: ...
    @property
    def DiagnosticId(self) -> str: ...
    @DiagnosticId.setter
    def DiagnosticId(self, value: str) -> str: ...
    @property
    def IsError(self) -> bool: ...
    @property
    def Message(self) -> str: ...
    @property
    def TypeId(self) -> typing.Any: ...
    @property
    def UrlFormat(self) -> str: ...
    @UrlFormat.setter
    def UrlFormat(self, value: str) -> str: ...


class OperatingSystem(ICloneable, ISerializable):
    def __init__(self, platform: PlatformID, version: Version) -> None: ...
    @property
    def Platform(self) -> PlatformID: ...
    @property
    def ServicePack(self) -> str: ...
    @property
    def Version(self) -> Version: ...
    @property
    def VersionString(self) -> str: ...
    def Clone(self) -> typing.Any: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...
    @staticmethod
    def IsAndroid() -> bool: ...
    @staticmethod
    def IsAndroidVersionAtLeast(major: int, minor: int = ..., build: int = ..., revision: int = ...) -> bool: ...
    @staticmethod
    def IsBrowser() -> bool: ...
    @staticmethod
    def IsFreeBSD() -> bool: ...
    @staticmethod
    def IsFreeBSDVersionAtLeast(major: int, minor: int = ..., build: int = ..., revision: int = ...) -> bool: ...
    @staticmethod
    def IsIOS() -> bool: ...
    @staticmethod
    def IsIOSVersionAtLeast(major: int, minor: int = ..., build: int = ...) -> bool: ...
    @staticmethod
    def IsLinux() -> bool: ...
    @staticmethod
    def IsMacCatalyst() -> bool: ...
    @staticmethod
    def IsMacCatalystVersionAtLeast(major: int, minor: int = ..., build: int = ...) -> bool: ...
    @staticmethod
    def IsMacOS() -> bool: ...
    @staticmethod
    def IsMacOSVersionAtLeast(major: int, minor: int = ..., build: int = ...) -> bool: ...
    @staticmethod
    def IsOSPlatform(platform: str) -> bool: ...
    @staticmethod
    def IsOSPlatformVersionAtLeast(platform: str, major: int, minor: int = ..., build: int = ..., revision: int = ...) -> bool: ...
    @staticmethod
    def IsTvOS() -> bool: ...
    @staticmethod
    def IsTvOSVersionAtLeast(major: int, minor: int = ..., build: int = ...) -> bool: ...
    @staticmethod
    def IsWatchOS() -> bool: ...
    @staticmethod
    def IsWatchOSVersionAtLeast(major: int, minor: int = ..., build: int = ...) -> bool: ...
    @staticmethod
    def IsWindows() -> bool: ...
    @staticmethod
    def IsWindowsVersionAtLeast(major: int, minor: int = ..., build: int = ..., revision: int = ...) -> bool: ...
    def ToString(self) -> str: ...


class OperationCanceledException(SystemException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, innerException: Exception) -> None: ...
    @typing.overload
    def __init__(self, message: str, innerException: Exception, token: CancellationToken) -> None: ...
    @typing.overload
    def __init__(self, message: str, token: CancellationToken) -> None: ...
    @typing.overload
    def __init__(self, token: CancellationToken) -> None: ...
    @property
    def CancellationToken(self) -> CancellationToken: ...
    @CancellationToken.setter
    def CancellationToken(self, value: CancellationToken) -> CancellationToken: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...


class OrdinalComparer(StringComparer):
    def Compare(self, x: str, y: str) -> int: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...
        @typing.overload
        def __call__(self, x: str, y: str) -> bool:...

    # Skipped GetHashCode due to it being static, abstract and generic.

    GetHashCode : GetHashCode_MethodGroup
    class GetHashCode_MethodGroup:
        @typing.overload
        def __call__(self) -> int:...
        @typing.overload
        def __call__(self, obj: str) -> int:...



class OutOfMemoryException(SystemException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, innerException: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...


class OverflowException(ArithmeticException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, innerException: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...


class ParamArrayAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class PlatformID(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Win32S : PlatformID # 0
    Win32Windows : PlatformID # 1
    Win32NT : PlatformID # 2
    WinCE : PlatformID # 3
    Unix : PlatformID # 4
    Xbox : PlatformID # 5
    MacOSX : PlatformID # 6
    Other : PlatformID # 7


class PlatformNotSupportedException(NotSupportedException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, inner: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...


class Predicate_GenericClasses(abc.ABCMeta):
    Generic_Predicate_GenericClasses_Predicate_1_T = typing.TypeVar('Generic_Predicate_GenericClasses_Predicate_1_T')
    def __getitem__(self, types : typing.Type[Generic_Predicate_GenericClasses_Predicate_1_T]) -> typing.Type[Predicate_1[Generic_Predicate_GenericClasses_Predicate_1_T]]: ...

Predicate : Predicate_GenericClasses

Predicate_1_T = typing.TypeVar('Predicate_1_T', contravariant=True)
class Predicate_1(typing.Generic[Predicate_1_T], MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, obj: Predicate_1_T, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> bool: ...
    def Invoke(self, obj: Predicate_1_T) -> bool: ...


class Progress_GenericClasses(abc.ABCMeta):
    Generic_Progress_GenericClasses_Progress_1_T = typing.TypeVar('Generic_Progress_GenericClasses_Progress_1_T')
    def __getitem__(self, types : typing.Type[Generic_Progress_GenericClasses_Progress_1_T]) -> typing.Type[Progress_1[Generic_Progress_GenericClasses_Progress_1_T]]: ...

Progress : Progress_GenericClasses

Progress_1_T = typing.TypeVar('Progress_1_T')
class Progress_1(typing.Generic[Progress_1_T], IProgress_1[Progress_1_T]):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, handler: Action_1[Progress_1_T]) -> None: ...


class Random:
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, Seed: int) -> None: ...
    @classmethod
    @property
    def Shared(cls) -> Random: ...
    def NextDouble(self) -> float: ...
    def NextSingle(self) -> float: ...
    # Skipped Next due to it being static, abstract and generic.

    Next : Next_MethodGroup
    class Next_MethodGroup:
        @typing.overload
        def __call__(self) -> int:...
        @typing.overload
        def __call__(self, maxValue: int) -> int:...
        @typing.overload
        def __call__(self, minValue: int, maxValue: int) -> int:...

    # Skipped NextBytes due to it being static, abstract and generic.

    NextBytes : NextBytes_MethodGroup
    class NextBytes_MethodGroup:
        @typing.overload
        def __call__(self, buffer: Array_1[int]) -> None:...
        @typing.overload
        def __call__(self, buffer: Span_1[int]) -> None:...

    # Skipped NextInt64 due to it being static, abstract and generic.

    NextInt64 : NextInt64_MethodGroup
    class NextInt64_MethodGroup:
        @typing.overload
        def __call__(self) -> int:...
        @typing.overload
        def __call__(self, maxValue: int) -> int:...
        @typing.overload
        def __call__(self, minValue: int, maxValue: int) -> int:...



class Range(IEquatable_1[Range]):
    def __init__(self, start: Index, end: Index) -> None: ...
    @classmethod
    @property
    def All(cls) -> Range: ...
    @property
    def End(self) -> Index: ...
    @property
    def Start(self) -> Index: ...
    @staticmethod
    def EndAt(end: Index) -> Range: ...
    def GetHashCode(self) -> int: ...
    def GetOffsetAndLength(self, length: int) -> ValueTuple_2[int, int]: ...
    @staticmethod
    def StartAt(start: Index) -> Range: ...
    def ToString(self) -> str: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, other: Range) -> bool:...
        @typing.overload
        def __call__(self, value: typing.Any) -> bool:...



class RankException(SystemException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, innerException: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...


class ReadOnlyMemory_GenericClasses(abc.ABCMeta):
    Generic_ReadOnlyMemory_GenericClasses_ReadOnlyMemory_1_T = typing.TypeVar('Generic_ReadOnlyMemory_GenericClasses_ReadOnlyMemory_1_T')
    def __getitem__(self, types : typing.Type[Generic_ReadOnlyMemory_GenericClasses_ReadOnlyMemory_1_T]) -> typing.Type[ReadOnlyMemory_1[Generic_ReadOnlyMemory_GenericClasses_ReadOnlyMemory_1_T]]: ...

ReadOnlyMemory : ReadOnlyMemory_GenericClasses

ReadOnlyMemory_1_T = typing.TypeVar('ReadOnlyMemory_1_T')
class ReadOnlyMemory_1(typing.Generic[ReadOnlyMemory_1_T], IEquatable_1[ReadOnlyMemory_1[ReadOnlyMemory_1_T]]):
    @typing.overload
    def __init__(self, array: Array_1[ReadOnlyMemory_1_T]) -> None: ...
    @typing.overload
    def __init__(self, array: Array_1[ReadOnlyMemory_1_T], start: int, length: int) -> None: ...
    @classmethod
    @property
    def Empty(cls) -> ReadOnlyMemory_1[ReadOnlyMemory_1_T]: ...
    @property
    def IsEmpty(self) -> bool: ...
    @property
    def Length(self) -> int: ...
    @property
    def Span(self) -> ReadOnlySpan_1[ReadOnlyMemory_1_T]: ...
    def CopyTo(self, destination: Memory_1[ReadOnlyMemory_1_T]) -> None: ...
    def GetHashCode(self) -> int: ...
    # Operator not supported op_Implicit(array: T[])
    # Operator not supported op_Implicit(segment: ArraySegment`1)
    def Pin(self) -> MemoryHandle: ...
    def ToArray(self) -> Array_1[ReadOnlyMemory_1_T]: ...
    def ToString(self) -> str: ...
    def TryCopyTo(self, destination: Memory_1[ReadOnlyMemory_1_T]) -> bool: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup[ReadOnlyMemory_1_T]
    Equals_MethodGroup_ReadOnlyMemory_1_T = typing.TypeVar('Equals_MethodGroup_ReadOnlyMemory_1_T')
    class Equals_MethodGroup(typing.Generic[Equals_MethodGroup_ReadOnlyMemory_1_T]):
        Equals_MethodGroup_ReadOnlyMemory_1_T = ReadOnlyMemory_1.Equals_MethodGroup_ReadOnlyMemory_1_T
        @typing.overload
        def __call__(self, other: ReadOnlyMemory_1[Equals_MethodGroup_ReadOnlyMemory_1_T]) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...

    # Skipped Slice due to it being static, abstract and generic.

    Slice : Slice_MethodGroup[ReadOnlyMemory_1_T]
    Slice_MethodGroup_ReadOnlyMemory_1_T = typing.TypeVar('Slice_MethodGroup_ReadOnlyMemory_1_T')
    class Slice_MethodGroup(typing.Generic[Slice_MethodGroup_ReadOnlyMemory_1_T]):
        Slice_MethodGroup_ReadOnlyMemory_1_T = ReadOnlyMemory_1.Slice_MethodGroup_ReadOnlyMemory_1_T
        @typing.overload
        def __call__(self, start: int) -> ReadOnlyMemory_1[Slice_MethodGroup_ReadOnlyMemory_1_T]:...
        @typing.overload
        def __call__(self, start: int, length: int) -> ReadOnlyMemory_1[Slice_MethodGroup_ReadOnlyMemory_1_T]:...



class ReadOnlySpan_GenericClasses(abc.ABCMeta):
    Generic_ReadOnlySpan_GenericClasses_ReadOnlySpan_1_T = typing.TypeVar('Generic_ReadOnlySpan_GenericClasses_ReadOnlySpan_1_T')
    def __getitem__(self, types : typing.Type[Generic_ReadOnlySpan_GenericClasses_ReadOnlySpan_1_T]) -> typing.Type[ReadOnlySpan_1[Generic_ReadOnlySpan_GenericClasses_ReadOnlySpan_1_T]]: ...

ReadOnlySpan : ReadOnlySpan_GenericClasses

ReadOnlySpan_1_T = typing.TypeVar('ReadOnlySpan_1_T')
class ReadOnlySpan_1(typing.Generic[ReadOnlySpan_1_T]):
    @typing.overload
    def __init__(self, array: Array_1[ReadOnlySpan_1_T]) -> None: ...
    @typing.overload
    def __init__(self, array: Array_1[ReadOnlySpan_1_T], start: int, length: int) -> None: ...
    @typing.overload
    def __init__(self, pointer: clr.Reference[None], length: int) -> None: ...
    @classmethod
    @property
    def Empty(cls) -> ReadOnlySpan_1[ReadOnlySpan_1_T]: ...
    @property
    def IsEmpty(self) -> bool: ...
    @property
    def Item(self) -> clr.Reference[ReadOnlySpan_1_T]: ...
    @property
    def Length(self) -> int: ...
    def CopyTo(self, destination: Span_1[ReadOnlySpan_1_T]) -> None: ...
    def Equals(self, obj: typing.Any) -> bool: ...
    def GetEnumerator(self) -> ReadOnlySpan_1.Enumerator_1[ReadOnlySpan_1_T]: ...
    def GetHashCode(self) -> int: ...
    def GetPinnableReference(self) -> clr.Reference[ReadOnlySpan_1_T]: ...
    def __eq__(self, left: ReadOnlySpan_1[ReadOnlySpan_1_T], right: ReadOnlySpan_1[ReadOnlySpan_1_T]) -> bool: ...
    # Operator not supported op_Implicit(array: T[])
    # Operator not supported op_Implicit(segment: ArraySegment`1)
    def __ne__(self, left: ReadOnlySpan_1[ReadOnlySpan_1_T], right: ReadOnlySpan_1[ReadOnlySpan_1_T]) -> bool: ...
    def ToArray(self) -> Array_1[ReadOnlySpan_1_T]: ...
    def ToString(self) -> str: ...
    def TryCopyTo(self, destination: Span_1[ReadOnlySpan_1_T]) -> bool: ...
    # Skipped Slice due to it being static, abstract and generic.

    Slice : Slice_MethodGroup[ReadOnlySpan_1_T]
    Slice_MethodGroup_ReadOnlySpan_1_T = typing.TypeVar('Slice_MethodGroup_ReadOnlySpan_1_T')
    class Slice_MethodGroup(typing.Generic[Slice_MethodGroup_ReadOnlySpan_1_T]):
        Slice_MethodGroup_ReadOnlySpan_1_T = ReadOnlySpan_1.Slice_MethodGroup_ReadOnlySpan_1_T
        @typing.overload
        def __call__(self, start: int) -> ReadOnlySpan_1[Slice_MethodGroup_ReadOnlySpan_1_T]:...
        @typing.overload
        def __call__(self, start: int, length: int) -> ReadOnlySpan_1[Slice_MethodGroup_ReadOnlySpan_1_T]:...


    Enumerator_GenericClasses_ReadOnlySpan_1_T = typing.TypeVar('Enumerator_GenericClasses_ReadOnlySpan_1_T')
    class Enumerator_GenericClasses(typing.Generic[Enumerator_GenericClasses_ReadOnlySpan_1_T], abc.ABCMeta):
        Enumerator_GenericClasses_ReadOnlySpan_1_T = ReadOnlySpan_1.Enumerator_GenericClasses_ReadOnlySpan_1_T
        def __call__(self) -> ReadOnlySpan_1.Enumerator_1[Enumerator_GenericClasses_ReadOnlySpan_1_T]: ...

    Enumerator : Enumerator_GenericClasses[ReadOnlySpan_1_T]

    Enumerator_1_T = typing.TypeVar('Enumerator_1_T')
    class Enumerator_1(typing.Generic[Enumerator_1_T]):
        Enumerator_1_T = ReadOnlySpan_1.Enumerator_1_T
        @property
        def Current(self) -> clr.Reference[Enumerator_1_T]: ...
        def MoveNext(self) -> bool: ...



class ResolveEventArgs(EventArgs):
    @typing.overload
    def __init__(self, name: str) -> None: ...
    @typing.overload
    def __init__(self, name: str, requestingAssembly: Assembly) -> None: ...
    @property
    def Name(self) -> str: ...
    @property
    def RequestingAssembly(self) -> Assembly: ...


class ResolveEventHandler(MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, sender: typing.Any, args: ResolveEventArgs, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> Assembly: ...
    def Invoke(self, sender: typing.Any, args: ResolveEventArgs) -> Assembly: ...


class RuntimeArgumentHandle:
    pass


class RuntimeFieldHandle(ISerializable):
    @property
    def Value(self) -> int: ...
    def GetHashCode(self) -> int: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...
    def __eq__(self, left: RuntimeFieldHandle, right: RuntimeFieldHandle) -> bool: ...
    def __ne__(self, left: RuntimeFieldHandle, right: RuntimeFieldHandle) -> bool: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, handle: RuntimeFieldHandle) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...



class RuntimeMethodHandle(ISerializable):
    @property
    def Value(self) -> int: ...
    def GetFunctionPointer(self) -> int: ...
    def GetHashCode(self) -> int: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...
    def __eq__(self, left: RuntimeMethodHandle, right: RuntimeMethodHandle) -> bool: ...
    def __ne__(self, left: RuntimeMethodHandle, right: RuntimeMethodHandle) -> bool: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, handle: RuntimeMethodHandle) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...



class RuntimeTypeHandle(ISerializable):
    @property
    def Value(self) -> int: ...
    def GetHashCode(self) -> int: ...
    def GetModuleHandle(self) -> ModuleHandle: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...
    @typing.overload
    def __eq__(self, left: RuntimeTypeHandle, right: typing.Any) -> bool: ...
    @typing.overload
    def __eq__(self, left: typing.Any, right: RuntimeTypeHandle) -> bool: ...
    @typing.overload
    def __ne__(self, left: RuntimeTypeHandle, right: typing.Any) -> bool: ...
    @typing.overload
    def __ne__(self, left: typing.Any, right: RuntimeTypeHandle) -> bool: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, handle: RuntimeTypeHandle) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...



class SByte(IBinaryInteger_1[int], ISignedNumber_1[int], IMinMaxValue_1[int], IConvertible):
    MaxValue : int
    MinValue : int
    def GetHashCode(self) -> int: ...
    def GetTypeCode(self) -> TypeCode: ...
    def TryFormat(self, destination: Span_1[str], charsWritten: clr.Reference[int], format: ReadOnlySpan_1[str] = ..., provider: IFormatProvider = ...) -> bool: ...
    # Skipped CompareTo due to it being static, abstract and generic.

    CompareTo : CompareTo_MethodGroup
    class CompareTo_MethodGroup:
        @typing.overload
        def __call__(self, value: int) -> int:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> int:...

    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, obj: int) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...

    # Skipped Parse due to it being static, abstract and generic.

    Parse : Parse_MethodGroup
    class Parse_MethodGroup:
        @typing.overload
        def __call__(self, s: str) -> int:...
        @typing.overload
        def __call__(self, s: str, style: NumberStyles) -> int:...
        @typing.overload
        def __call__(self, s: str, provider: IFormatProvider) -> int:...
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], style: NumberStyles = ..., provider: IFormatProvider = ...) -> int:...
        @typing.overload
        def __call__(self, s: str, style: NumberStyles, provider: IFormatProvider) -> int:...

    # Skipped ToString due to it being static, abstract and generic.

    ToString : ToString_MethodGroup
    class ToString_MethodGroup:
        @typing.overload
        def __call__(self) -> str:...
        @typing.overload
        def __call__(self, format: str) -> str:...
        @typing.overload
        def __call__(self, provider: IFormatProvider) -> str:...
        @typing.overload
        def __call__(self, format: str, provider: IFormatProvider) -> str:...

    # Skipped TryParse due to it being static, abstract and generic.

    TryParse : TryParse_MethodGroup
    class TryParse_MethodGroup:
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], result: clr.Reference[int]) -> bool:...
        @typing.overload
        def __call__(self, s: str, result: clr.Reference[int]) -> bool:...
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], style: NumberStyles, provider: IFormatProvider, result: clr.Reference[int]) -> bool:...
        @typing.overload
        def __call__(self, s: str, style: NumberStyles, provider: IFormatProvider, result: clr.Reference[int]) -> bool:...



class SerializableAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class Single(IBinaryFloatingPoint_1[float], IMinMaxValue_1[float], IConvertible):
    Epsilon : float
    MaxValue : float
    MinValue : float
    NaN : float
    NegativeInfinity : float
    PositiveInfinity : float
    def GetHashCode(self) -> int: ...
    def GetTypeCode(self) -> TypeCode: ...
    @staticmethod
    def IsFinite(f: float) -> bool: ...
    @staticmethod
    def IsInfinity(f: float) -> bool: ...
    @staticmethod
    def IsNaN(f: float) -> bool: ...
    @staticmethod
    def IsNegative(f: float) -> bool: ...
    @staticmethod
    def IsNegativeInfinity(f: float) -> bool: ...
    @staticmethod
    def IsNormal(f: float) -> bool: ...
    @staticmethod
    def IsPositiveInfinity(f: float) -> bool: ...
    @staticmethod
    def IsSubnormal(f: float) -> bool: ...
    def __eq__(self, left: float, right: float) -> bool: ...
    def __gt__(self, left: float, right: float) -> bool: ...
    def __ge__(self, left: float, right: float) -> bool: ...
    def __ne__(self, left: float, right: float) -> bool: ...
    def __lt__(self, left: float, right: float) -> bool: ...
    def __le__(self, left: float, right: float) -> bool: ...
    def TryFormat(self, destination: Span_1[str], charsWritten: clr.Reference[int], format: ReadOnlySpan_1[str] = ..., provider: IFormatProvider = ...) -> bool: ...
    # Skipped CompareTo due to it being static, abstract and generic.

    CompareTo : CompareTo_MethodGroup
    class CompareTo_MethodGroup:
        @typing.overload
        def __call__(self, value: float) -> int:...
        @typing.overload
        def __call__(self, value: typing.Any) -> int:...

    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, obj: float) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...

    # Skipped Parse due to it being static, abstract and generic.

    Parse : Parse_MethodGroup
    class Parse_MethodGroup:
        @typing.overload
        def __call__(self, s: str) -> float:...
        @typing.overload
        def __call__(self, s: str, style: NumberStyles) -> float:...
        @typing.overload
        def __call__(self, s: str, provider: IFormatProvider) -> float:...
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], style: NumberStyles = ..., provider: IFormatProvider = ...) -> float:...
        @typing.overload
        def __call__(self, s: str, style: NumberStyles, provider: IFormatProvider) -> float:...

    # Skipped ToString due to it being static, abstract and generic.

    ToString : ToString_MethodGroup
    class ToString_MethodGroup:
        @typing.overload
        def __call__(self) -> str:...
        @typing.overload
        def __call__(self, format: str) -> str:...
        @typing.overload
        def __call__(self, provider: IFormatProvider) -> str:...
        @typing.overload
        def __call__(self, format: str, provider: IFormatProvider) -> str:...

    # Skipped TryParse due to it being static, abstract and generic.

    TryParse : TryParse_MethodGroup
    class TryParse_MethodGroup:
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], result: clr.Reference[float]) -> bool:...
        @typing.overload
        def __call__(self, s: str, result: clr.Reference[float]) -> bool:...
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], style: NumberStyles, provider: IFormatProvider, result: clr.Reference[float]) -> bool:...
        @typing.overload
        def __call__(self, s: str, style: NumberStyles, provider: IFormatProvider, result: clr.Reference[float]) -> bool:...



class Span_GenericClasses(abc.ABCMeta):
    Generic_Span_GenericClasses_Span_1_T = typing.TypeVar('Generic_Span_GenericClasses_Span_1_T')
    def __getitem__(self, types : typing.Type[Generic_Span_GenericClasses_Span_1_T]) -> typing.Type[Span_1[Generic_Span_GenericClasses_Span_1_T]]: ...

Span : Span_GenericClasses

Span_1_T = typing.TypeVar('Span_1_T')
class Span_1(typing.Generic[Span_1_T]):
    @typing.overload
    def __init__(self, array: Array_1[Span_1_T]) -> None: ...
    @typing.overload
    def __init__(self, array: Array_1[Span_1_T], start: int, length: int) -> None: ...
    @typing.overload
    def __init__(self, pointer: clr.Reference[None], length: int) -> None: ...
    @classmethod
    @property
    def Empty(cls) -> Span_1[Span_1_T]: ...
    @property
    def IsEmpty(self) -> bool: ...
    @property
    def Item(self) -> clr.Reference[Span_1_T]: ...
    @property
    def Length(self) -> int: ...
    def Clear(self) -> None: ...
    def CopyTo(self, destination: Span_1[Span_1_T]) -> None: ...
    def Equals(self, obj: typing.Any) -> bool: ...
    def Fill(self, value: Span_1_T) -> None: ...
    def GetEnumerator(self) -> Span_1.Enumerator_1[Span_1_T]: ...
    def GetHashCode(self) -> int: ...
    def GetPinnableReference(self) -> clr.Reference[Span_1_T]: ...
    def __eq__(self, left: Span_1[Span_1_T], right: Span_1[Span_1_T]) -> bool: ...
    # Operator not supported op_Implicit(array: T[])
    # Operator not supported op_Implicit(segment: ArraySegment`1)
    # Operator not supported op_Implicit(span: Span`1)
    def __ne__(self, left: Span_1[Span_1_T], right: Span_1[Span_1_T]) -> bool: ...
    def ToArray(self) -> Array_1[Span_1_T]: ...
    def ToString(self) -> str: ...
    def TryCopyTo(self, destination: Span_1[Span_1_T]) -> bool: ...
    # Skipped Slice due to it being static, abstract and generic.

    Slice : Slice_MethodGroup[Span_1_T]
    Slice_MethodGroup_Span_1_T = typing.TypeVar('Slice_MethodGroup_Span_1_T')
    class Slice_MethodGroup(typing.Generic[Slice_MethodGroup_Span_1_T]):
        Slice_MethodGroup_Span_1_T = Span_1.Slice_MethodGroup_Span_1_T
        @typing.overload
        def __call__(self, start: int) -> Span_1[Slice_MethodGroup_Span_1_T]:...
        @typing.overload
        def __call__(self, start: int, length: int) -> Span_1[Slice_MethodGroup_Span_1_T]:...


    Enumerator_GenericClasses_Span_1_T = typing.TypeVar('Enumerator_GenericClasses_Span_1_T')
    class Enumerator_GenericClasses(typing.Generic[Enumerator_GenericClasses_Span_1_T], abc.ABCMeta):
        Enumerator_GenericClasses_Span_1_T = Span_1.Enumerator_GenericClasses_Span_1_T
        def __call__(self) -> Span_1.Enumerator_1[Enumerator_GenericClasses_Span_1_T]: ...

    Enumerator : Enumerator_GenericClasses[Span_1_T]

    Enumerator_1_T = typing.TypeVar('Enumerator_1_T')
    class Enumerator_1(typing.Generic[Enumerator_1_T]):
        Enumerator_1_T = Span_1.Enumerator_1_T
        @property
        def Current(self) -> clr.Reference[Enumerator_1_T]: ...
        def MoveNext(self) -> bool: ...



class StackOverflowException(SystemException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, innerException: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...


class STAThreadAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class String(IEnumerable_1[str], ICloneable, IEquatable_1[str], IComparable_1[str], IConvertible, IComparable_0):
    @typing.overload
    def __init__(self, c: str, count: int) -> None: ...
    @typing.overload
    def __init__(self, value: Array_1[str]) -> None: ...
    @typing.overload
    def __init__(self, value: clr.Reference[str]) -> None: ...
    @typing.overload
    def __init__(self, value: clr.Reference[int]) -> None: ...
    @typing.overload
    def __init__(self, value: ReadOnlySpan_1[str]) -> None: ...
    @typing.overload
    def __init__(self, value: Array_1[str], startIndex: int, length: int) -> None: ...
    @typing.overload
    def __init__(self, value: clr.Reference[str], startIndex: int, length: int) -> None: ...
    @typing.overload
    def __init__(self, value: clr.Reference[int], startIndex: int, length: int) -> None: ...
    @typing.overload
    def __init__(self, value: clr.Reference[int], startIndex: int, length: int, enc: Encoding) -> None: ...
    Empty : str
    @property
    def Chars(self) -> str: ...
    @property
    def Length(self) -> int: ...
    def Clone(self) -> typing.Any: ...
    @staticmethod
    def Copy(str: str) -> str: ...
    def EnumerateRunes(self) -> StringRuneEnumerator: ...
    def GetEnumerator(self) -> CharEnumerator: ...
    def GetPinnableReference(self) -> clr.Reference[str]: ...
    def GetTypeCode(self) -> TypeCode: ...
    def Insert(self, startIndex: int, value: str) -> str: ...
    @staticmethod
    def Intern(str: str) -> str: ...
    @staticmethod
    def IsInterned(str: str) -> str: ...
    @staticmethod
    def IsNullOrEmpty(value: str) -> bool: ...
    @staticmethod
    def IsNullOrWhiteSpace(value: str) -> bool: ...
    def __eq__(self, a: str, b: str) -> bool: ...
    # Operator not supported op_Implicit(value: String)
    def __ne__(self, a: str, b: str) -> bool: ...
    def ToLowerInvariant(self) -> str: ...
    def ToUpperInvariant(self) -> str: ...
    def TryCopyTo(self, destination: Span_1[str]) -> bool: ...
    # Skipped Compare due to it being static, abstract and generic.

    Compare : Compare_MethodGroup
    class Compare_MethodGroup:
        @typing.overload
        def __call__(self, strA: str, strB: str) -> int:...
        @typing.overload
        def __call__(self, strA: str, strB: str, comparisonType: StringComparison) -> int:...
        @typing.overload
        def __call__(self, strA: str, strB: str, ignoreCase: bool) -> int:...
        @typing.overload
        def __call__(self, strA: str, strB: str, ignoreCase: bool, culture: CultureInfo) -> int:...
        @typing.overload
        def __call__(self, strA: str, strB: str, culture: CultureInfo, options: CompareOptions) -> int:...
        @typing.overload
        def __call__(self, strA: str, indexA: int, strB: str, indexB: int, length: int) -> int:...
        @typing.overload
        def __call__(self, strA: str, indexA: int, strB: str, indexB: int, length: int, comparisonType: StringComparison) -> int:...
        @typing.overload
        def __call__(self, strA: str, indexA: int, strB: str, indexB: int, length: int, ignoreCase: bool) -> int:...
        @typing.overload
        def __call__(self, strA: str, indexA: int, strB: str, indexB: int, length: int, ignoreCase: bool, culture: CultureInfo) -> int:...
        @typing.overload
        def __call__(self, strA: str, indexA: int, strB: str, indexB: int, length: int, culture: CultureInfo, options: CompareOptions) -> int:...

    # Skipped CompareOrdinal due to it being static, abstract and generic.

    CompareOrdinal : CompareOrdinal_MethodGroup
    class CompareOrdinal_MethodGroup:
        @typing.overload
        def __call__(self, strA: str, strB: str) -> int:...
        @typing.overload
        def __call__(self, strA: str, indexA: int, strB: str, indexB: int, length: int) -> int:...

    # Skipped CompareTo due to it being static, abstract and generic.

    CompareTo : CompareTo_MethodGroup
    class CompareTo_MethodGroup:
        @typing.overload
        def __call__(self, strB: str) -> int:...
        @typing.overload
        def __call__(self, value: typing.Any) -> int:...

    # Skipped Concat due to it being static, abstract and generic.

    Concat : Concat_MethodGroup
    class Concat_MethodGroup:
        def __getitem__(self, t:typing.Type[Concat_1_T1]) -> Concat_1[Concat_1_T1]: ...

        Concat_1_T1 = typing.TypeVar('Concat_1_T1')
        class Concat_1(typing.Generic[Concat_1_T1]):
            Concat_1_T = String.Concat_MethodGroup.Concat_1_T1
            def __call__(self, values: IEnumerable_1[Concat_1_T]) -> str:...

        @typing.overload
        def __call__(self, values: Array_1[str]) -> str:...
        @typing.overload
        def __call__(self, args: Array_1[typing.Any]) -> str:...
        @typing.overload
        def __call__(self, values: IEnumerable_1[str]) -> str:...
        @typing.overload
        def __call__(self, arg0: typing.Any) -> str:...
        @typing.overload
        def __call__(self, str0: ReadOnlySpan_1[str], str1: ReadOnlySpan_1[str]) -> str:...
        @typing.overload
        def __call__(self, str0: str, str1: str) -> str:...
        @typing.overload
        def __call__(self, arg0: typing.Any, arg1: typing.Any) -> str:...
        @typing.overload
        def __call__(self, str0: ReadOnlySpan_1[str], str1: ReadOnlySpan_1[str], str2: ReadOnlySpan_1[str]) -> str:...
        @typing.overload
        def __call__(self, str0: str, str1: str, str2: str) -> str:...
        @typing.overload
        def __call__(self, arg0: typing.Any, arg1: typing.Any, arg2: typing.Any) -> str:...
        @typing.overload
        def __call__(self, str0: ReadOnlySpan_1[str], str1: ReadOnlySpan_1[str], str2: ReadOnlySpan_1[str], str3: ReadOnlySpan_1[str]) -> str:...
        @typing.overload
        def __call__(self, str0: str, str1: str, str2: str, str3: str) -> str:...

    # Skipped Contains due to it being static, abstract and generic.

    Contains : Contains_MethodGroup
    class Contains_MethodGroup:
        @typing.overload
        def __call__(self, value: str) -> bool:...
        # Method Contains(value : Char) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: str, comparisonType: StringComparison) -> bool:...
        # Method Contains(value : Char, comparisonType : StringComparison) was skipped since it collides with above method

    # Skipped CopyTo due to it being static, abstract and generic.

    CopyTo : CopyTo_MethodGroup
    class CopyTo_MethodGroup:
        @typing.overload
        def __call__(self, destination: Span_1[str]) -> None:...
        @typing.overload
        def __call__(self, sourceIndex: int, destination: Array_1[str], destinationIndex: int, count: int) -> None:...

    # Skipped Create due to it being static, abstract and generic.

    Create : Create_MethodGroup
    class Create_MethodGroup:
        def __getitem__(self, t:typing.Type[Create_1_T1]) -> Create_1[Create_1_T1]: ...

        Create_1_T1 = typing.TypeVar('Create_1_T1')
        class Create_1(typing.Generic[Create_1_T1]):
            Create_1_TState = String.Create_MethodGroup.Create_1_T1
            def __call__(self, length: int, state: Create_1_TState, action: SpanAction_2[str, Create_1_TState]) -> str:...

        @typing.overload
        def __call__(self, provider: IFormatProvider, handler: clr.Reference[DefaultInterpolatedStringHandler]) -> str:...
        @typing.overload
        def __call__(self, provider: IFormatProvider, initialBuffer: Span_1[str], handler: clr.Reference[DefaultInterpolatedStringHandler]) -> str:...

    # Skipped EndsWith due to it being static, abstract and generic.

    EndsWith : EndsWith_MethodGroup
    class EndsWith_MethodGroup:
        @typing.overload
        def __call__(self, value: str) -> bool:...
        # Method EndsWith(value : Char) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: str, comparisonType: StringComparison) -> bool:...
        @typing.overload
        def __call__(self, value: str, ignoreCase: bool, culture: CultureInfo) -> bool:...

    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, value: str) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...
        @typing.overload
        def __call__(self, value: str, comparisonType: StringComparison) -> bool:...
        @typing.overload
        def __call__(self, a: str, b: str) -> bool:...
        @typing.overload
        def __call__(self, a: str, b: str, comparisonType: StringComparison) -> bool:...

    # Skipped Format due to it being static, abstract and generic.

    Format : Format_MethodGroup
    class Format_MethodGroup:
        @typing.overload
        def __call__(self, format: str, args: Array_1[typing.Any]) -> str:...
        @typing.overload
        def __call__(self, format: str, arg0: typing.Any) -> str:...
        @typing.overload
        def __call__(self, format: str, arg0: typing.Any, arg1: typing.Any) -> str:...
        @typing.overload
        def __call__(self, provider: IFormatProvider, format: str, args: Array_1[typing.Any]) -> str:...
        @typing.overload
        def __call__(self, provider: IFormatProvider, format: str, arg0: typing.Any) -> str:...
        @typing.overload
        def __call__(self, format: str, arg0: typing.Any, arg1: typing.Any, arg2: typing.Any) -> str:...
        @typing.overload
        def __call__(self, provider: IFormatProvider, format: str, arg0: typing.Any, arg1: typing.Any) -> str:...
        @typing.overload
        def __call__(self, provider: IFormatProvider, format: str, arg0: typing.Any, arg1: typing.Any, arg2: typing.Any) -> str:...

    # Skipped GetHashCode due to it being static, abstract and generic.

    GetHashCode : GetHashCode_MethodGroup
    class GetHashCode_MethodGroup:
        @typing.overload
        def __call__(self) -> int:...
        @typing.overload
        def __call__(self, comparisonType: StringComparison) -> int:...
        @typing.overload
        def __call__(self, value: ReadOnlySpan_1[str]) -> int:...
        @typing.overload
        def __call__(self, value: ReadOnlySpan_1[str], comparisonType: StringComparison) -> int:...

    # Skipped IndexOf due to it being static, abstract and generic.

    IndexOf : IndexOf_MethodGroup
    class IndexOf_MethodGroup:
        @typing.overload
        def __call__(self, value: str) -> int:...
        # Method IndexOf(value : String) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: str, startIndex: int) -> int:...
        # Method IndexOf(value : String, startIndex : Int32) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: str, comparisonType: StringComparison) -> int:...
        # Method IndexOf(value : String, comparisonType : StringComparison) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: str, startIndex: int, count: int) -> int:...
        # Method IndexOf(value : String, startIndex : Int32, count : Int32) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: str, startIndex: int, comparisonType: StringComparison) -> int:...
        @typing.overload
        def __call__(self, value: str, startIndex: int, count: int, comparisonType: StringComparison) -> int:...

    # Skipped IndexOfAny due to it being static, abstract and generic.

    IndexOfAny : IndexOfAny_MethodGroup
    class IndexOfAny_MethodGroup:
        @typing.overload
        def __call__(self, anyOf: Array_1[str]) -> int:...
        @typing.overload
        def __call__(self, anyOf: Array_1[str], startIndex: int) -> int:...
        @typing.overload
        def __call__(self, anyOf: Array_1[str], startIndex: int, count: int) -> int:...

    # Skipped IsNormalized due to it being static, abstract and generic.

    IsNormalized : IsNormalized_MethodGroup
    class IsNormalized_MethodGroup:
        @typing.overload
        def __call__(self) -> bool:...
        @typing.overload
        def __call__(self, normalizationForm: NormalizationForm) -> bool:...

    # Skipped Join due to it being static, abstract and generic.

    Join : Join_MethodGroup
    class Join_MethodGroup:
        def __getitem__(self, t:typing.Type[Join_1_T1]) -> Join_1[Join_1_T1]: ...

        Join_1_T1 = typing.TypeVar('Join_1_T1')
        class Join_1(typing.Generic[Join_1_T1]):
            Join_1_T = String.Join_MethodGroup.Join_1_T1
            def __call__(self, separator: str, values: IEnumerable_1[Join_1_T]) -> str:...
            # Method Join(separator : String, values : IEnumerable`1) was skipped since it collides with above method

        @typing.overload
        def __call__(self, separator: str, value: Array_1[str]) -> str:...
        # Method Join(separator : String, value : String[]) was skipped since it collides with above method
        @typing.overload
        def __call__(self, separator: str, values: Array_1[typing.Any]) -> str:...
        # Method Join(separator : String, values : Object[]) was skipped since it collides with above method
        @typing.overload
        def __call__(self, separator: str, values: IEnumerable_1[str]) -> str:...
        @typing.overload
        def __call__(self, separator: str, value: Array_1[str], startIndex: int, count: int) -> str:...
        # Method Join(separator : String, value : String[], startIndex : Int32, count : Int32) was skipped since it collides with above method

    # Skipped LastIndexOf due to it being static, abstract and generic.

    LastIndexOf : LastIndexOf_MethodGroup
    class LastIndexOf_MethodGroup:
        @typing.overload
        def __call__(self, value: str) -> int:...
        # Method LastIndexOf(value : String) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: str, startIndex: int) -> int:...
        # Method LastIndexOf(value : Char, startIndex : Int32) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: str, comparisonType: StringComparison) -> int:...
        @typing.overload
        def __call__(self, value: str, startIndex: int, count: int) -> int:...
        # Method LastIndexOf(value : Char, startIndex : Int32, count : Int32) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: str, startIndex: int, comparisonType: StringComparison) -> int:...
        @typing.overload
        def __call__(self, value: str, startIndex: int, count: int, comparisonType: StringComparison) -> int:...

    # Skipped LastIndexOfAny due to it being static, abstract and generic.

    LastIndexOfAny : LastIndexOfAny_MethodGroup
    class LastIndexOfAny_MethodGroup:
        @typing.overload
        def __call__(self, anyOf: Array_1[str]) -> int:...
        @typing.overload
        def __call__(self, anyOf: Array_1[str], startIndex: int) -> int:...
        @typing.overload
        def __call__(self, anyOf: Array_1[str], startIndex: int, count: int) -> int:...

    # Skipped Normalize due to it being static, abstract and generic.

    Normalize : Normalize_MethodGroup
    class Normalize_MethodGroup:
        @typing.overload
        def __call__(self) -> str:...
        @typing.overload
        def __call__(self, normalizationForm: NormalizationForm) -> str:...

    # Skipped PadLeft due to it being static, abstract and generic.

    PadLeft : PadLeft_MethodGroup
    class PadLeft_MethodGroup:
        @typing.overload
        def __call__(self, totalWidth: int) -> str:...
        @typing.overload
        def __call__(self, totalWidth: int, paddingChar: str) -> str:...

    # Skipped PadRight due to it being static, abstract and generic.

    PadRight : PadRight_MethodGroup
    class PadRight_MethodGroup:
        @typing.overload
        def __call__(self, totalWidth: int) -> str:...
        @typing.overload
        def __call__(self, totalWidth: int, paddingChar: str) -> str:...

    # Skipped Remove due to it being static, abstract and generic.

    Remove : Remove_MethodGroup
    class Remove_MethodGroup:
        @typing.overload
        def __call__(self, startIndex: int) -> str:...
        @typing.overload
        def __call__(self, startIndex: int, count: int) -> str:...

    # Skipped Replace due to it being static, abstract and generic.

    Replace : Replace_MethodGroup
    class Replace_MethodGroup:
        @typing.overload
        def __call__(self, oldChar: str, newChar: str) -> str:...
        # Method Replace(oldValue : String, newValue : String) was skipped since it collides with above method
        @typing.overload
        def __call__(self, oldValue: str, newValue: str, comparisonType: StringComparison) -> str:...
        @typing.overload
        def __call__(self, oldValue: str, newValue: str, ignoreCase: bool, culture: CultureInfo) -> str:...

    # Skipped ReplaceLineEndings due to it being static, abstract and generic.

    ReplaceLineEndings : ReplaceLineEndings_MethodGroup
    class ReplaceLineEndings_MethodGroup:
        @typing.overload
        def __call__(self) -> str:...
        @typing.overload
        def __call__(self, replacementText: str) -> str:...

    # Skipped Split due to it being static, abstract and generic.

    Split : Split_MethodGroup
    class Split_MethodGroup:
        @typing.overload
        def __call__(self, separator: Array_1[str]) -> Array_1[str]:...
        @typing.overload
        def __call__(self, separator: str, options: StringSplitOptions = ...) -> Array_1[str]:...
        @typing.overload
        def __call__(self, separator: Array_1[str], count: int) -> Array_1[str]:...
        @typing.overload
        def __call__(self, separator: Array_1[str], options: StringSplitOptions) -> Array_1[str]:...
        # Method Split(separator : String[], options : StringSplitOptions) was skipped since it collides with above method
        # Method Split(separator : String, options : StringSplitOptions) was skipped since it collides with above method
        @typing.overload
        def __call__(self, separator: str, count: int, options: StringSplitOptions = ...) -> Array_1[str]:...
        @typing.overload
        def __call__(self, separator: Array_1[str], count: int, options: StringSplitOptions) -> Array_1[str]:...
        # Method Split(separator : String[], count : Int32, options : StringSplitOptions) was skipped since it collides with above method
        # Method Split(separator : String, count : Int32, options : StringSplitOptions) was skipped since it collides with above method

    # Skipped StartsWith due to it being static, abstract and generic.

    StartsWith : StartsWith_MethodGroup
    class StartsWith_MethodGroup:
        @typing.overload
        def __call__(self, value: str) -> bool:...
        # Method StartsWith(value : Char) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: str, comparisonType: StringComparison) -> bool:...
        @typing.overload
        def __call__(self, value: str, ignoreCase: bool, culture: CultureInfo) -> bool:...

    # Skipped Substring due to it being static, abstract and generic.

    Substring : Substring_MethodGroup
    class Substring_MethodGroup:
        @typing.overload
        def __call__(self, startIndex: int) -> str:...
        @typing.overload
        def __call__(self, startIndex: int, length: int) -> str:...

    # Skipped ToCharArray due to it being static, abstract and generic.

    ToCharArray : ToCharArray_MethodGroup
    class ToCharArray_MethodGroup:
        @typing.overload
        def __call__(self) -> Array_1[str]:...
        @typing.overload
        def __call__(self, startIndex: int, length: int) -> Array_1[str]:...

    # Skipped ToLower due to it being static, abstract and generic.

    ToLower : ToLower_MethodGroup
    class ToLower_MethodGroup:
        @typing.overload
        def __call__(self) -> str:...
        @typing.overload
        def __call__(self, culture: CultureInfo) -> str:...

    # Skipped ToString due to it being static, abstract and generic.

    ToString : ToString_MethodGroup
    class ToString_MethodGroup:
        @typing.overload
        def __call__(self) -> str:...
        @typing.overload
        def __call__(self, provider: IFormatProvider) -> str:...

    # Skipped ToUpper due to it being static, abstract and generic.

    ToUpper : ToUpper_MethodGroup
    class ToUpper_MethodGroup:
        @typing.overload
        def __call__(self) -> str:...
        @typing.overload
        def __call__(self, culture: CultureInfo) -> str:...

    # Skipped Trim due to it being static, abstract and generic.

    Trim : Trim_MethodGroup
    class Trim_MethodGroup:
        @typing.overload
        def __call__(self) -> str:...
        @typing.overload
        def __call__(self, trimChar: str) -> str:...
        @typing.overload
        def __call__(self, trimChars: Array_1[str]) -> str:...

    # Skipped TrimEnd due to it being static, abstract and generic.

    TrimEnd : TrimEnd_MethodGroup
    class TrimEnd_MethodGroup:
        @typing.overload
        def __call__(self) -> str:...
        @typing.overload
        def __call__(self, trimChar: str) -> str:...
        @typing.overload
        def __call__(self, trimChars: Array_1[str]) -> str:...

    # Skipped TrimStart due to it being static, abstract and generic.

    TrimStart : TrimStart_MethodGroup
    class TrimStart_MethodGroup:
        @typing.overload
        def __call__(self) -> str:...
        @typing.overload
        def __call__(self, trimChar: str) -> str:...
        @typing.overload
        def __call__(self, trimChars: Array_1[str]) -> str:...



class StringComparer(IEqualityComparer_1[str], IComparer_1[str], IEqualityComparer, IComparer, abc.ABC):
    @classmethod
    @property
    def CurrentCulture(cls) -> StringComparer: ...
    @classmethod
    @property
    def CurrentCultureIgnoreCase(cls) -> StringComparer: ...
    @classmethod
    @property
    def InvariantCulture(cls) -> StringComparer: ...
    @classmethod
    @property
    def InvariantCultureIgnoreCase(cls) -> StringComparer: ...
    @classmethod
    @property
    def Ordinal(cls) -> StringComparer: ...
    @classmethod
    @property
    def OrdinalIgnoreCase(cls) -> StringComparer: ...
    @staticmethod
    def FromComparison(comparisonType: StringComparison) -> StringComparer: ...
    @staticmethod
    def IsWellKnownCultureAwareComparer(comparer: IEqualityComparer_1[str], compareInfo: clr.Reference[CompareInfo], compareOptions: clr.Reference[CompareOptions]) -> bool: ...
    @staticmethod
    def IsWellKnownOrdinalComparer(comparer: IEqualityComparer_1[str], ignoreCase: clr.Reference[bool]) -> bool: ...
    # Skipped Compare due to it being static, abstract and generic.

    Compare : Compare_MethodGroup
    class Compare_MethodGroup:
        @typing.overload
        def __call__(self, x: str, y: str) -> int:...
        @typing.overload
        def __call__(self, x: typing.Any, y: typing.Any) -> int:...

    # Skipped Create due to it being static, abstract and generic.

    Create : Create_MethodGroup
    class Create_MethodGroup:
        @typing.overload
        def __call__(self, culture: CultureInfo, options: CompareOptions) -> StringComparer:...
        @typing.overload
        def __call__(self, culture: CultureInfo, ignoreCase: bool) -> StringComparer:...

    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, x: str, y: str) -> bool:...
        @typing.overload
        def __call__(self, x: typing.Any, y: typing.Any) -> bool:...

    # Skipped GetHashCode due to it being static, abstract and generic.

    GetHashCode : GetHashCode_MethodGroup
    class GetHashCode_MethodGroup:
        @typing.overload
        def __call__(self, obj: str) -> int:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> int:...



class StringComparison(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    CurrentCulture : StringComparison # 0
    CurrentCultureIgnoreCase : StringComparison # 1
    InvariantCulture : StringComparison # 2
    InvariantCultureIgnoreCase : StringComparison # 3
    Ordinal : StringComparison # 4
    OrdinalIgnoreCase : StringComparison # 5


class StringNormalizationExtensions(abc.ABC):
    # Skipped IsNormalized due to it being static, abstract and generic.

    IsNormalized : IsNormalized_MethodGroup
    class IsNormalized_MethodGroup:
        @typing.overload
        def __call__(self, strInput: str) -> bool:...
        @typing.overload
        def __call__(self, strInput: str, normalizationForm: NormalizationForm) -> bool:...

    # Skipped Normalize due to it being static, abstract and generic.

    Normalize : Normalize_MethodGroup
    class Normalize_MethodGroup:
        @typing.overload
        def __call__(self, strInput: str) -> str:...
        @typing.overload
        def __call__(self, strInput: str, normalizationForm: NormalizationForm) -> str:...



class StringSplitOptions(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    None_ : StringSplitOptions # 0
    RemoveEmptyEntries : StringSplitOptions # 1
    TrimEntries : StringSplitOptions # 2


class SystemException(Exception):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, innerException: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...


class ThreadStaticAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class TimeOnly(IComparisonOperators_2[TimeOnly, TimeOnly], ISpanParseable_1[TimeOnly], ISpanFormattable, ISubtractionOperators_3[TimeOnly, TimeOnly, TimeSpan], IMinMaxValue_1[TimeOnly]):
    @typing.overload
    def __init__(self, hour: int, minute: int) -> None: ...
    @typing.overload
    def __init__(self, hour: int, minute: int, second: int) -> None: ...
    @typing.overload
    def __init__(self, hour: int, minute: int, second: int, millisecond: int) -> None: ...
    @typing.overload
    def __init__(self, ticks: int) -> None: ...
    @property
    def Hour(self) -> int: ...
    @classmethod
    @property
    def MaxValue(cls) -> TimeOnly: ...
    @property
    def Millisecond(self) -> int: ...
    @property
    def Minute(self) -> int: ...
    @classmethod
    @property
    def MinValue(cls) -> TimeOnly: ...
    @property
    def Second(self) -> int: ...
    @property
    def Ticks(self) -> int: ...
    @staticmethod
    def FromDateTime(dateTime: DateTime) -> TimeOnly: ...
    @staticmethod
    def FromTimeSpan(timeSpan: TimeSpan) -> TimeOnly: ...
    def GetHashCode(self) -> int: ...
    def IsBetween(self, start: TimeOnly, end: TimeOnly) -> bool: ...
    def __eq__(self, left: TimeOnly, right: TimeOnly) -> bool: ...
    def __gt__(self, left: TimeOnly, right: TimeOnly) -> bool: ...
    def __ge__(self, left: TimeOnly, right: TimeOnly) -> bool: ...
    def __ne__(self, left: TimeOnly, right: TimeOnly) -> bool: ...
    def __lt__(self, left: TimeOnly, right: TimeOnly) -> bool: ...
    def __le__(self, left: TimeOnly, right: TimeOnly) -> bool: ...
    def __sub__(self, t1: TimeOnly, t2: TimeOnly) -> TimeSpan: ...
    def ToLongTimeString(self) -> str: ...
    def ToShortTimeString(self) -> str: ...
    def ToTimeSpan(self) -> TimeSpan: ...
    def TryFormat(self, destination: Span_1[str], charsWritten: clr.Reference[int], format: ReadOnlySpan_1[str] = ..., provider: IFormatProvider = ...) -> bool: ...
    # Skipped Add due to it being static, abstract and generic.

    Add : Add_MethodGroup
    class Add_MethodGroup:
        @typing.overload
        def __call__(self, value: TimeSpan) -> TimeOnly:...
        @typing.overload
        def __call__(self, value: TimeSpan, wrappedDays: clr.Reference[int]) -> TimeOnly:...

    # Skipped AddHours due to it being static, abstract and generic.

    AddHours : AddHours_MethodGroup
    class AddHours_MethodGroup:
        @typing.overload
        def __call__(self, value: float) -> TimeOnly:...
        @typing.overload
        def __call__(self, value: float, wrappedDays: clr.Reference[int]) -> TimeOnly:...

    # Skipped AddMinutes due to it being static, abstract and generic.

    AddMinutes : AddMinutes_MethodGroup
    class AddMinutes_MethodGroup:
        @typing.overload
        def __call__(self, value: float) -> TimeOnly:...
        @typing.overload
        def __call__(self, value: float, wrappedDays: clr.Reference[int]) -> TimeOnly:...

    # Skipped CompareTo due to it being static, abstract and generic.

    CompareTo : CompareTo_MethodGroup
    class CompareTo_MethodGroup:
        @typing.overload
        def __call__(self, value: TimeOnly) -> int:...
        @typing.overload
        def __call__(self, value: typing.Any) -> int:...

    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, value: TimeOnly) -> bool:...
        @typing.overload
        def __call__(self, value: typing.Any) -> bool:...

    # Skipped Parse due to it being static, abstract and generic.

    Parse : Parse_MethodGroup
    class Parse_MethodGroup:
        @typing.overload
        def __call__(self, s: str) -> TimeOnly:...
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], provider: IFormatProvider = ..., style: DateTimeStyles = ...) -> TimeOnly:...
        @typing.overload
        def __call__(self, s: str, provider: IFormatProvider, style: DateTimeStyles = ...) -> TimeOnly:...

    # Skipped ParseExact due to it being static, abstract and generic.

    ParseExact : ParseExact_MethodGroup
    class ParseExact_MethodGroup:
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], formats: Array_1[str]) -> TimeOnly:...
        @typing.overload
        def __call__(self, s: str, formats: Array_1[str]) -> TimeOnly:...
        @typing.overload
        def __call__(self, s: str, format: str) -> TimeOnly:...
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], formats: Array_1[str], provider: IFormatProvider, style: DateTimeStyles = ...) -> TimeOnly:...
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], format: ReadOnlySpan_1[str], provider: IFormatProvider = ..., style: DateTimeStyles = ...) -> TimeOnly:...
        @typing.overload
        def __call__(self, s: str, formats: Array_1[str], provider: IFormatProvider, style: DateTimeStyles = ...) -> TimeOnly:...
        @typing.overload
        def __call__(self, s: str, format: str, provider: IFormatProvider, style: DateTimeStyles = ...) -> TimeOnly:...

    # Skipped ToString due to it being static, abstract and generic.

    ToString : ToString_MethodGroup
    class ToString_MethodGroup:
        @typing.overload
        def __call__(self) -> str:...
        @typing.overload
        def __call__(self, format: str) -> str:...
        @typing.overload
        def __call__(self, provider: IFormatProvider) -> str:...
        @typing.overload
        def __call__(self, format: str, provider: IFormatProvider) -> str:...

    # Skipped TryParse due to it being static, abstract and generic.

    TryParse : TryParse_MethodGroup
    class TryParse_MethodGroup:
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], result: clr.Reference[TimeOnly]) -> bool:...
        @typing.overload
        def __call__(self, s: str, result: clr.Reference[TimeOnly]) -> bool:...
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], provider: IFormatProvider, style: DateTimeStyles, result: clr.Reference[TimeOnly]) -> bool:...
        @typing.overload
        def __call__(self, s: str, provider: IFormatProvider, style: DateTimeStyles, result: clr.Reference[TimeOnly]) -> bool:...

    # Skipped TryParseExact due to it being static, abstract and generic.

    TryParseExact : TryParseExact_MethodGroup
    class TryParseExact_MethodGroup:
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], formats: Array_1[str], result: clr.Reference[TimeOnly]) -> bool:...
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], format: ReadOnlySpan_1[str], result: clr.Reference[TimeOnly]) -> bool:...
        @typing.overload
        def __call__(self, s: str, formats: Array_1[str], result: clr.Reference[TimeOnly]) -> bool:...
        @typing.overload
        def __call__(self, s: str, format: str, result: clr.Reference[TimeOnly]) -> bool:...
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], formats: Array_1[str], provider: IFormatProvider, style: DateTimeStyles, result: clr.Reference[TimeOnly]) -> bool:...
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], format: ReadOnlySpan_1[str], provider: IFormatProvider, style: DateTimeStyles, result: clr.Reference[TimeOnly]) -> bool:...
        @typing.overload
        def __call__(self, s: str, formats: Array_1[str], provider: IFormatProvider, style: DateTimeStyles, result: clr.Reference[TimeOnly]) -> bool:...
        @typing.overload
        def __call__(self, s: str, format: str, provider: IFormatProvider, style: DateTimeStyles, result: clr.Reference[TimeOnly]) -> bool:...



class TimeoutException(SystemException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, innerException: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...


class TimeSpan(IComparisonOperators_2[TimeSpan, TimeSpan], ISpanParseable_1[TimeSpan], ISpanFormattable, IUnaryPlusOperators_2[TimeSpan, TimeSpan], IUnaryNegationOperators_2[TimeSpan, TimeSpan], ISubtractionOperators_3[TimeSpan, TimeSpan, TimeSpan], IMultiplicativeIdentity_2[TimeSpan, float], IMultiplyOperators_3[TimeSpan, float, TimeSpan], IMinMaxValue_1[TimeSpan], IDivisionOperators_3[TimeSpan, TimeSpan, float], IDivisionOperators_3[TimeSpan, float, TimeSpan], IAdditiveIdentity_2[TimeSpan, TimeSpan], IAdditionOperators_3[TimeSpan, TimeSpan, TimeSpan]):
    @typing.overload
    def __init__(self, days: int, hours: int, minutes: int, seconds: int) -> None: ...
    @typing.overload
    def __init__(self, days: int, hours: int, minutes: int, seconds: int, milliseconds: int) -> None: ...
    @typing.overload
    def __init__(self, hours: int, minutes: int, seconds: int) -> None: ...
    @typing.overload
    def __init__(self, ticks: int) -> None: ...
    MaxValue : TimeSpan
    MinValue : TimeSpan
    TicksPerDay : int
    TicksPerHour : int
    TicksPerMillisecond : int
    TicksPerMinute : int
    TicksPerSecond : int
    Zero : TimeSpan
    @property
    def Days(self) -> int: ...
    @property
    def Hours(self) -> int: ...
    @property
    def Milliseconds(self) -> int: ...
    @property
    def Minutes(self) -> int: ...
    @property
    def Seconds(self) -> int: ...
    @property
    def Ticks(self) -> int: ...
    @property
    def TotalDays(self) -> float: ...
    @property
    def TotalHours(self) -> float: ...
    @property
    def TotalMilliseconds(self) -> float: ...
    @property
    def TotalMinutes(self) -> float: ...
    @property
    def TotalSeconds(self) -> float: ...
    def Add(self, ts: TimeSpan) -> TimeSpan: ...
    @staticmethod
    def Compare(t1: TimeSpan, t2: TimeSpan) -> int: ...
    def Duration(self) -> TimeSpan: ...
    @staticmethod
    def FromDays(value: float) -> TimeSpan: ...
    @staticmethod
    def FromHours(value: float) -> TimeSpan: ...
    @staticmethod
    def FromMilliseconds(value: float) -> TimeSpan: ...
    @staticmethod
    def FromMinutes(value: float) -> TimeSpan: ...
    @staticmethod
    def FromSeconds(value: float) -> TimeSpan: ...
    @staticmethod
    def FromTicks(value: int) -> TimeSpan: ...
    def GetHashCode(self) -> int: ...
    def Multiply(self, factor: float) -> TimeSpan: ...
    def Negate(self) -> TimeSpan: ...
    def __add__(self, t1: TimeSpan, t2: TimeSpan) -> TimeSpan: ...
    @typing.overload
    def __truediv__(self, timeSpan: TimeSpan, divisor: float) -> TimeSpan: ...
    @typing.overload
    def __truediv__(self, t1: TimeSpan, t2: TimeSpan) -> float: ...
    def __eq__(self, t1: TimeSpan, t2: TimeSpan) -> bool: ...
    def __gt__(self, t1: TimeSpan, t2: TimeSpan) -> bool: ...
    def __ge__(self, t1: TimeSpan, t2: TimeSpan) -> bool: ...
    def __ne__(self, t1: TimeSpan, t2: TimeSpan) -> bool: ...
    def __lt__(self, t1: TimeSpan, t2: TimeSpan) -> bool: ...
    def __le__(self, t1: TimeSpan, t2: TimeSpan) -> bool: ...
    @typing.overload
    def __mul__(self, factor: float, timeSpan: TimeSpan) -> TimeSpan: ...
    @typing.overload
    def __mul__(self, timeSpan: TimeSpan, factor: float) -> TimeSpan: ...
    def __sub__(self, t1: TimeSpan, t2: TimeSpan) -> TimeSpan: ...
    def __neg__(self, t: TimeSpan) -> TimeSpan: ...
    def __pos__(self, t: TimeSpan) -> TimeSpan: ...
    def Subtract(self, ts: TimeSpan) -> TimeSpan: ...
    def TryFormat(self, destination: Span_1[str], charsWritten: clr.Reference[int], format: ReadOnlySpan_1[str] = ..., formatProvider: IFormatProvider = ...) -> bool: ...
    # Skipped CompareTo due to it being static, abstract and generic.

    CompareTo : CompareTo_MethodGroup
    class CompareTo_MethodGroup:
        @typing.overload
        def __call__(self, value: TimeSpan) -> int:...
        @typing.overload
        def __call__(self, value: typing.Any) -> int:...

    # Skipped Divide due to it being static, abstract and generic.

    Divide : Divide_MethodGroup
    class Divide_MethodGroup:
        @typing.overload
        def __call__(self, divisor: float) -> TimeSpan:...
        @typing.overload
        def __call__(self, ts: TimeSpan) -> float:...

    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, obj: TimeSpan) -> bool:...
        @typing.overload
        def __call__(self, value: typing.Any) -> bool:...
        @typing.overload
        def __call__(self, t1: TimeSpan, t2: TimeSpan) -> bool:...

    # Skipped Parse due to it being static, abstract and generic.

    Parse : Parse_MethodGroup
    class Parse_MethodGroup:
        @typing.overload
        def __call__(self, s: str) -> TimeSpan:...
        @typing.overload
        def __call__(self, input: ReadOnlySpan_1[str], formatProvider: IFormatProvider = ...) -> TimeSpan:...
        @typing.overload
        def __call__(self, input: str, formatProvider: IFormatProvider) -> TimeSpan:...

    # Skipped ParseExact due to it being static, abstract and generic.

    ParseExact : ParseExact_MethodGroup
    class ParseExact_MethodGroup:
        @typing.overload
        def __call__(self, input: str, formats: Array_1[str], formatProvider: IFormatProvider) -> TimeSpan:...
        @typing.overload
        def __call__(self, input: str, format: str, formatProvider: IFormatProvider) -> TimeSpan:...
        @typing.overload
        def __call__(self, input: ReadOnlySpan_1[str], formats: Array_1[str], formatProvider: IFormatProvider, styles: TimeSpanStyles = ...) -> TimeSpan:...
        @typing.overload
        def __call__(self, input: ReadOnlySpan_1[str], format: ReadOnlySpan_1[str], formatProvider: IFormatProvider, styles: TimeSpanStyles = ...) -> TimeSpan:...
        @typing.overload
        def __call__(self, input: str, formats: Array_1[str], formatProvider: IFormatProvider, styles: TimeSpanStyles) -> TimeSpan:...
        @typing.overload
        def __call__(self, input: str, format: str, formatProvider: IFormatProvider, styles: TimeSpanStyles) -> TimeSpan:...

    # Skipped ToString due to it being static, abstract and generic.

    ToString : ToString_MethodGroup
    class ToString_MethodGroup:
        @typing.overload
        def __call__(self) -> str:...
        @typing.overload
        def __call__(self, format: str) -> str:...
        @typing.overload
        def __call__(self, format: str, formatProvider: IFormatProvider) -> str:...

    # Skipped TryParse due to it being static, abstract and generic.

    TryParse : TryParse_MethodGroup
    class TryParse_MethodGroup:
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], result: clr.Reference[TimeSpan]) -> bool:...
        @typing.overload
        def __call__(self, s: str, result: clr.Reference[TimeSpan]) -> bool:...
        @typing.overload
        def __call__(self, input: ReadOnlySpan_1[str], formatProvider: IFormatProvider, result: clr.Reference[TimeSpan]) -> bool:...
        @typing.overload
        def __call__(self, input: str, formatProvider: IFormatProvider, result: clr.Reference[TimeSpan]) -> bool:...

    # Skipped TryParseExact due to it being static, abstract and generic.

    TryParseExact : TryParseExact_MethodGroup
    class TryParseExact_MethodGroup:
        @typing.overload
        def __call__(self, input: ReadOnlySpan_1[str], formats: Array_1[str], formatProvider: IFormatProvider, result: clr.Reference[TimeSpan]) -> bool:...
        @typing.overload
        def __call__(self, input: ReadOnlySpan_1[str], format: ReadOnlySpan_1[str], formatProvider: IFormatProvider, result: clr.Reference[TimeSpan]) -> bool:...
        @typing.overload
        def __call__(self, input: str, formats: Array_1[str], formatProvider: IFormatProvider, result: clr.Reference[TimeSpan]) -> bool:...
        @typing.overload
        def __call__(self, input: str, format: str, formatProvider: IFormatProvider, result: clr.Reference[TimeSpan]) -> bool:...
        @typing.overload
        def __call__(self, input: ReadOnlySpan_1[str], formats: Array_1[str], formatProvider: IFormatProvider, styles: TimeSpanStyles, result: clr.Reference[TimeSpan]) -> bool:...
        @typing.overload
        def __call__(self, input: ReadOnlySpan_1[str], format: ReadOnlySpan_1[str], formatProvider: IFormatProvider, styles: TimeSpanStyles, result: clr.Reference[TimeSpan]) -> bool:...
        @typing.overload
        def __call__(self, input: str, formats: Array_1[str], formatProvider: IFormatProvider, styles: TimeSpanStyles, result: clr.Reference[TimeSpan]) -> bool:...
        @typing.overload
        def __call__(self, input: str, format: str, formatProvider: IFormatProvider, styles: TimeSpanStyles, result: clr.Reference[TimeSpan]) -> bool:...



class TimeZone(abc.ABC):
    @classmethod
    @property
    def CurrentTimeZone(cls) -> TimeZone: ...
    @property
    def DaylightName(self) -> str: ...
    @property
    def StandardName(self) -> str: ...
    @abc.abstractmethod
    def GetDaylightChanges(self, year: int) -> DaylightTime: ...
    @abc.abstractmethod
    def GetUtcOffset(self, time: DateTime) -> TimeSpan: ...
    def ToLocalTime(self, time: DateTime) -> DateTime: ...
    def ToUniversalTime(self, time: DateTime) -> DateTime: ...
    # Skipped IsDaylightSavingTime due to it being static, abstract and generic.

    IsDaylightSavingTime : IsDaylightSavingTime_MethodGroup
    class IsDaylightSavingTime_MethodGroup:
        @typing.overload
        def __call__(self, time: DateTime) -> bool:...
        @typing.overload
        def __call__(self, time: DateTime, daylightTimes: DaylightTime) -> bool:...



class TimeZoneInfo(IDeserializationCallback, ISerializable, IEquatable_1[TimeZoneInfo]):
    @property
    def BaseUtcOffset(self) -> TimeSpan: ...
    @property
    def DaylightName(self) -> str: ...
    @property
    def DisplayName(self) -> str: ...
    @property
    def HasIanaId(self) -> bool: ...
    @property
    def Id(self) -> str: ...
    @classmethod
    @property
    def Local(cls) -> TimeZoneInfo: ...
    @property
    def StandardName(self) -> str: ...
    @property
    def SupportsDaylightSavingTime(self) -> bool: ...
    @classmethod
    @property
    def Utc(cls) -> TimeZoneInfo: ...
    @staticmethod
    def ClearCachedData() -> None: ...
    @staticmethod
    def ConvertTimeFromUtc(dateTime: DateTime, destinationTimeZone: TimeZoneInfo) -> DateTime: ...
    @staticmethod
    def FindSystemTimeZoneById(id: str) -> TimeZoneInfo: ...
    @staticmethod
    def FromSerializedString(source: str) -> TimeZoneInfo: ...
    def GetAdjustmentRules(self) -> Array_1[TimeZoneInfo.AdjustmentRule]: ...
    def GetHashCode(self) -> int: ...
    @staticmethod
    def GetSystemTimeZones() -> ReadOnlyCollection_1[TimeZoneInfo]: ...
    def HasSameRules(self, other: TimeZoneInfo) -> bool: ...
    def IsInvalidTime(self, dateTime: DateTime) -> bool: ...
    def ToSerializedString(self) -> str: ...
    def ToString(self) -> str: ...
    @staticmethod
    def TryConvertIanaIdToWindowsId(ianaId: str, windowsId: clr.Reference[str]) -> bool: ...
    # Skipped ConvertTime due to it being static, abstract and generic.

    ConvertTime : ConvertTime_MethodGroup
    class ConvertTime_MethodGroup:
        @typing.overload
        def __call__(self, dateTimeOffset: DateTimeOffset, destinationTimeZone: TimeZoneInfo) -> DateTimeOffset:...
        @typing.overload
        def __call__(self, dateTime: DateTime, destinationTimeZone: TimeZoneInfo) -> DateTime:...
        @typing.overload
        def __call__(self, dateTime: DateTime, sourceTimeZone: TimeZoneInfo, destinationTimeZone: TimeZoneInfo) -> DateTime:...

    # Skipped ConvertTimeBySystemTimeZoneId due to it being static, abstract and generic.

    ConvertTimeBySystemTimeZoneId : ConvertTimeBySystemTimeZoneId_MethodGroup
    class ConvertTimeBySystemTimeZoneId_MethodGroup:
        @typing.overload
        def __call__(self, dateTimeOffset: DateTimeOffset, destinationTimeZoneId: str) -> DateTimeOffset:...
        @typing.overload
        def __call__(self, dateTime: DateTime, destinationTimeZoneId: str) -> DateTime:...
        @typing.overload
        def __call__(self, dateTime: DateTime, sourceTimeZoneId: str, destinationTimeZoneId: str) -> DateTime:...

    # Skipped ConvertTimeToUtc due to it being static, abstract and generic.

    ConvertTimeToUtc : ConvertTimeToUtc_MethodGroup
    class ConvertTimeToUtc_MethodGroup:
        @typing.overload
        def __call__(self, dateTime: DateTime) -> DateTime:...
        @typing.overload
        def __call__(self, dateTime: DateTime, sourceTimeZone: TimeZoneInfo) -> DateTime:...

    # Skipped CreateCustomTimeZone due to it being static, abstract and generic.

    CreateCustomTimeZone : CreateCustomTimeZone_MethodGroup
    class CreateCustomTimeZone_MethodGroup:
        @typing.overload
        def __call__(self, id: str, baseUtcOffset: TimeSpan, displayName: str, standardDisplayName: str) -> TimeZoneInfo:...
        @typing.overload
        def __call__(self, id: str, baseUtcOffset: TimeSpan, displayName: str, standardDisplayName: str, daylightDisplayName: str, adjustmentRules: Array_1[TimeZoneInfo.AdjustmentRule]) -> TimeZoneInfo:...
        @typing.overload
        def __call__(self, id: str, baseUtcOffset: TimeSpan, displayName: str, standardDisplayName: str, daylightDisplayName: str, adjustmentRules: Array_1[TimeZoneInfo.AdjustmentRule], disableDaylightSavingTime: bool) -> TimeZoneInfo:...

    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, other: TimeZoneInfo) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...

    # Skipped GetAmbiguousTimeOffsets due to it being static, abstract and generic.

    GetAmbiguousTimeOffsets : GetAmbiguousTimeOffsets_MethodGroup
    class GetAmbiguousTimeOffsets_MethodGroup:
        @typing.overload
        def __call__(self, dateTime: DateTime) -> Array_1[TimeSpan]:...
        @typing.overload
        def __call__(self, dateTimeOffset: DateTimeOffset) -> Array_1[TimeSpan]:...

    # Skipped GetUtcOffset due to it being static, abstract and generic.

    GetUtcOffset : GetUtcOffset_MethodGroup
    class GetUtcOffset_MethodGroup:
        @typing.overload
        def __call__(self, dateTime: DateTime) -> TimeSpan:...
        @typing.overload
        def __call__(self, dateTimeOffset: DateTimeOffset) -> TimeSpan:...

    # Skipped IsAmbiguousTime due to it being static, abstract and generic.

    IsAmbiguousTime : IsAmbiguousTime_MethodGroup
    class IsAmbiguousTime_MethodGroup:
        @typing.overload
        def __call__(self, dateTime: DateTime) -> bool:...
        @typing.overload
        def __call__(self, dateTimeOffset: DateTimeOffset) -> bool:...

    # Skipped IsDaylightSavingTime due to it being static, abstract and generic.

    IsDaylightSavingTime : IsDaylightSavingTime_MethodGroup
    class IsDaylightSavingTime_MethodGroup:
        @typing.overload
        def __call__(self, dateTime: DateTime) -> bool:...
        @typing.overload
        def __call__(self, dateTimeOffset: DateTimeOffset) -> bool:...

    # Skipped TryConvertWindowsIdToIanaId due to it being static, abstract and generic.

    TryConvertWindowsIdToIanaId : TryConvertWindowsIdToIanaId_MethodGroup
    class TryConvertWindowsIdToIanaId_MethodGroup:
        @typing.overload
        def __call__(self, windowsId: str, ianaId: clr.Reference[str]) -> bool:...
        @typing.overload
        def __call__(self, windowsId: str, region: str, ianaId: clr.Reference[str]) -> bool:...


    class AdjustmentRule(IDeserializationCallback, ISerializable, IEquatable_1[TimeZoneInfo.AdjustmentRule]):
        @property
        def BaseUtcOffsetDelta(self) -> TimeSpan: ...
        @property
        def DateEnd(self) -> DateTime: ...
        @property
        def DateStart(self) -> DateTime: ...
        @property
        def DaylightDelta(self) -> TimeSpan: ...
        @property
        def DaylightTransitionEnd(self) -> TimeZoneInfo.TransitionTime: ...
        @property
        def DaylightTransitionStart(self) -> TimeZoneInfo.TransitionTime: ...
        def Equals(self, other: TimeZoneInfo.AdjustmentRule) -> bool: ...
        def GetHashCode(self) -> int: ...
        # Skipped CreateAdjustmentRule due to it being static, abstract and generic.

        CreateAdjustmentRule : CreateAdjustmentRule_MethodGroup
        class CreateAdjustmentRule_MethodGroup:
            @typing.overload
            def __call__(self, dateStart: DateTime, dateEnd: DateTime, daylightDelta: TimeSpan, daylightTransitionStart: TimeZoneInfo.TransitionTime, daylightTransitionEnd: TimeZoneInfo.TransitionTime) -> TimeZoneInfo.AdjustmentRule:...
            @typing.overload
            def __call__(self, dateStart: DateTime, dateEnd: DateTime, daylightDelta: TimeSpan, daylightTransitionStart: TimeZoneInfo.TransitionTime, daylightTransitionEnd: TimeZoneInfo.TransitionTime, baseUtcOffsetDelta: TimeSpan) -> TimeZoneInfo.AdjustmentRule:...



    class TransitionTime(IDeserializationCallback, ISerializable, IEquatable_1[TimeZoneInfo.TransitionTime]):
        @property
        def Day(self) -> int: ...
        @property
        def DayOfWeek(self) -> DayOfWeek: ...
        @property
        def IsFixedDateRule(self) -> bool: ...
        @property
        def Month(self) -> int: ...
        @property
        def TimeOfDay(self) -> DateTime: ...
        @property
        def Week(self) -> int: ...
        @staticmethod
        def CreateFixedDateRule(timeOfDay: DateTime, month: int, day: int) -> TimeZoneInfo.TransitionTime: ...
        @staticmethod
        def CreateFloatingDateRule(timeOfDay: DateTime, month: int, week: int, dayOfWeek: DayOfWeek) -> TimeZoneInfo.TransitionTime: ...
        def GetHashCode(self) -> int: ...
        def __eq__(self, t1: TimeZoneInfo.TransitionTime, t2: TimeZoneInfo.TransitionTime) -> bool: ...
        def __ne__(self, t1: TimeZoneInfo.TransitionTime, t2: TimeZoneInfo.TransitionTime) -> bool: ...
        # Skipped Equals due to it being static, abstract and generic.

        Equals : Equals_MethodGroup
        class Equals_MethodGroup:
            @typing.overload
            def __call__(self, other: TimeZoneInfo.TransitionTime) -> bool:...
            @typing.overload
            def __call__(self, obj: typing.Any) -> bool:...




class TimeZoneNotFoundException(Exception):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, innerException: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...


class Tuple_GenericClasses(abc.ABCMeta):
    Generic_Tuple_GenericClasses_Tuple_1_T1 = typing.TypeVar('Generic_Tuple_GenericClasses_Tuple_1_T1')
    @typing.overload
    def __getitem__(self, types : typing.Type[Generic_Tuple_GenericClasses_Tuple_1_T1]) -> typing.Type[Tuple_1[Generic_Tuple_GenericClasses_Tuple_1_T1]]: ...
    Generic_Tuple_GenericClasses_Tuple_2_T1 = typing.TypeVar('Generic_Tuple_GenericClasses_Tuple_2_T1')
    Generic_Tuple_GenericClasses_Tuple_2_T2 = typing.TypeVar('Generic_Tuple_GenericClasses_Tuple_2_T2')
    @typing.overload
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_Tuple_GenericClasses_Tuple_2_T1], typing.Type[Generic_Tuple_GenericClasses_Tuple_2_T2]]) -> typing.Type[Tuple_2[Generic_Tuple_GenericClasses_Tuple_2_T1, Generic_Tuple_GenericClasses_Tuple_2_T2]]: ...
    Generic_Tuple_GenericClasses_Tuple_3_T1 = typing.TypeVar('Generic_Tuple_GenericClasses_Tuple_3_T1')
    Generic_Tuple_GenericClasses_Tuple_3_T2 = typing.TypeVar('Generic_Tuple_GenericClasses_Tuple_3_T2')
    Generic_Tuple_GenericClasses_Tuple_3_T3 = typing.TypeVar('Generic_Tuple_GenericClasses_Tuple_3_T3')
    @typing.overload
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_Tuple_GenericClasses_Tuple_3_T1], typing.Type[Generic_Tuple_GenericClasses_Tuple_3_T2], typing.Type[Generic_Tuple_GenericClasses_Tuple_3_T3]]) -> typing.Type[Tuple_3[Generic_Tuple_GenericClasses_Tuple_3_T1, Generic_Tuple_GenericClasses_Tuple_3_T2, Generic_Tuple_GenericClasses_Tuple_3_T3]]: ...
    Generic_Tuple_GenericClasses_Tuple_4_T1 = typing.TypeVar('Generic_Tuple_GenericClasses_Tuple_4_T1')
    Generic_Tuple_GenericClasses_Tuple_4_T2 = typing.TypeVar('Generic_Tuple_GenericClasses_Tuple_4_T2')
    Generic_Tuple_GenericClasses_Tuple_4_T3 = typing.TypeVar('Generic_Tuple_GenericClasses_Tuple_4_T3')
    Generic_Tuple_GenericClasses_Tuple_4_T4 = typing.TypeVar('Generic_Tuple_GenericClasses_Tuple_4_T4')
    @typing.overload
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_Tuple_GenericClasses_Tuple_4_T1], typing.Type[Generic_Tuple_GenericClasses_Tuple_4_T2], typing.Type[Generic_Tuple_GenericClasses_Tuple_4_T3], typing.Type[Generic_Tuple_GenericClasses_Tuple_4_T4]]) -> typing.Type[Tuple_4[Generic_Tuple_GenericClasses_Tuple_4_T1, Generic_Tuple_GenericClasses_Tuple_4_T2, Generic_Tuple_GenericClasses_Tuple_4_T3, Generic_Tuple_GenericClasses_Tuple_4_T4]]: ...
    Generic_Tuple_GenericClasses_Tuple_5_T1 = typing.TypeVar('Generic_Tuple_GenericClasses_Tuple_5_T1')
    Generic_Tuple_GenericClasses_Tuple_5_T2 = typing.TypeVar('Generic_Tuple_GenericClasses_Tuple_5_T2')
    Generic_Tuple_GenericClasses_Tuple_5_T3 = typing.TypeVar('Generic_Tuple_GenericClasses_Tuple_5_T3')
    Generic_Tuple_GenericClasses_Tuple_5_T4 = typing.TypeVar('Generic_Tuple_GenericClasses_Tuple_5_T4')
    Generic_Tuple_GenericClasses_Tuple_5_T5 = typing.TypeVar('Generic_Tuple_GenericClasses_Tuple_5_T5')
    @typing.overload
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_Tuple_GenericClasses_Tuple_5_T1], typing.Type[Generic_Tuple_GenericClasses_Tuple_5_T2], typing.Type[Generic_Tuple_GenericClasses_Tuple_5_T3], typing.Type[Generic_Tuple_GenericClasses_Tuple_5_T4], typing.Type[Generic_Tuple_GenericClasses_Tuple_5_T5]]) -> typing.Type[Tuple_5[Generic_Tuple_GenericClasses_Tuple_5_T1, Generic_Tuple_GenericClasses_Tuple_5_T2, Generic_Tuple_GenericClasses_Tuple_5_T3, Generic_Tuple_GenericClasses_Tuple_5_T4, Generic_Tuple_GenericClasses_Tuple_5_T5]]: ...
    Generic_Tuple_GenericClasses_Tuple_6_T1 = typing.TypeVar('Generic_Tuple_GenericClasses_Tuple_6_T1')
    Generic_Tuple_GenericClasses_Tuple_6_T2 = typing.TypeVar('Generic_Tuple_GenericClasses_Tuple_6_T2')
    Generic_Tuple_GenericClasses_Tuple_6_T3 = typing.TypeVar('Generic_Tuple_GenericClasses_Tuple_6_T3')
    Generic_Tuple_GenericClasses_Tuple_6_T4 = typing.TypeVar('Generic_Tuple_GenericClasses_Tuple_6_T4')
    Generic_Tuple_GenericClasses_Tuple_6_T5 = typing.TypeVar('Generic_Tuple_GenericClasses_Tuple_6_T5')
    Generic_Tuple_GenericClasses_Tuple_6_T6 = typing.TypeVar('Generic_Tuple_GenericClasses_Tuple_6_T6')
    @typing.overload
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_Tuple_GenericClasses_Tuple_6_T1], typing.Type[Generic_Tuple_GenericClasses_Tuple_6_T2], typing.Type[Generic_Tuple_GenericClasses_Tuple_6_T3], typing.Type[Generic_Tuple_GenericClasses_Tuple_6_T4], typing.Type[Generic_Tuple_GenericClasses_Tuple_6_T5], typing.Type[Generic_Tuple_GenericClasses_Tuple_6_T6]]) -> typing.Type[Tuple_6[Generic_Tuple_GenericClasses_Tuple_6_T1, Generic_Tuple_GenericClasses_Tuple_6_T2, Generic_Tuple_GenericClasses_Tuple_6_T3, Generic_Tuple_GenericClasses_Tuple_6_T4, Generic_Tuple_GenericClasses_Tuple_6_T5, Generic_Tuple_GenericClasses_Tuple_6_T6]]: ...
    Generic_Tuple_GenericClasses_Tuple_7_T1 = typing.TypeVar('Generic_Tuple_GenericClasses_Tuple_7_T1')
    Generic_Tuple_GenericClasses_Tuple_7_T2 = typing.TypeVar('Generic_Tuple_GenericClasses_Tuple_7_T2')
    Generic_Tuple_GenericClasses_Tuple_7_T3 = typing.TypeVar('Generic_Tuple_GenericClasses_Tuple_7_T3')
    Generic_Tuple_GenericClasses_Tuple_7_T4 = typing.TypeVar('Generic_Tuple_GenericClasses_Tuple_7_T4')
    Generic_Tuple_GenericClasses_Tuple_7_T5 = typing.TypeVar('Generic_Tuple_GenericClasses_Tuple_7_T5')
    Generic_Tuple_GenericClasses_Tuple_7_T6 = typing.TypeVar('Generic_Tuple_GenericClasses_Tuple_7_T6')
    Generic_Tuple_GenericClasses_Tuple_7_T7 = typing.TypeVar('Generic_Tuple_GenericClasses_Tuple_7_T7')
    @typing.overload
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_Tuple_GenericClasses_Tuple_7_T1], typing.Type[Generic_Tuple_GenericClasses_Tuple_7_T2], typing.Type[Generic_Tuple_GenericClasses_Tuple_7_T3], typing.Type[Generic_Tuple_GenericClasses_Tuple_7_T4], typing.Type[Generic_Tuple_GenericClasses_Tuple_7_T5], typing.Type[Generic_Tuple_GenericClasses_Tuple_7_T6], typing.Type[Generic_Tuple_GenericClasses_Tuple_7_T7]]) -> typing.Type[Tuple_7[Generic_Tuple_GenericClasses_Tuple_7_T1, Generic_Tuple_GenericClasses_Tuple_7_T2, Generic_Tuple_GenericClasses_Tuple_7_T3, Generic_Tuple_GenericClasses_Tuple_7_T4, Generic_Tuple_GenericClasses_Tuple_7_T5, Generic_Tuple_GenericClasses_Tuple_7_T6, Generic_Tuple_GenericClasses_Tuple_7_T7]]: ...
    Generic_Tuple_GenericClasses_Tuple_8_T1 = typing.TypeVar('Generic_Tuple_GenericClasses_Tuple_8_T1')
    Generic_Tuple_GenericClasses_Tuple_8_T2 = typing.TypeVar('Generic_Tuple_GenericClasses_Tuple_8_T2')
    Generic_Tuple_GenericClasses_Tuple_8_T3 = typing.TypeVar('Generic_Tuple_GenericClasses_Tuple_8_T3')
    Generic_Tuple_GenericClasses_Tuple_8_T4 = typing.TypeVar('Generic_Tuple_GenericClasses_Tuple_8_T4')
    Generic_Tuple_GenericClasses_Tuple_8_T5 = typing.TypeVar('Generic_Tuple_GenericClasses_Tuple_8_T5')
    Generic_Tuple_GenericClasses_Tuple_8_T6 = typing.TypeVar('Generic_Tuple_GenericClasses_Tuple_8_T6')
    Generic_Tuple_GenericClasses_Tuple_8_T7 = typing.TypeVar('Generic_Tuple_GenericClasses_Tuple_8_T7')
    Generic_Tuple_GenericClasses_Tuple_8_TRest = typing.TypeVar('Generic_Tuple_GenericClasses_Tuple_8_TRest')
    @typing.overload
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_Tuple_GenericClasses_Tuple_8_T1], typing.Type[Generic_Tuple_GenericClasses_Tuple_8_T2], typing.Type[Generic_Tuple_GenericClasses_Tuple_8_T3], typing.Type[Generic_Tuple_GenericClasses_Tuple_8_T4], typing.Type[Generic_Tuple_GenericClasses_Tuple_8_T5], typing.Type[Generic_Tuple_GenericClasses_Tuple_8_T6], typing.Type[Generic_Tuple_GenericClasses_Tuple_8_T7], typing.Type[Generic_Tuple_GenericClasses_Tuple_8_TRest]]) -> typing.Type[Tuple_8[Generic_Tuple_GenericClasses_Tuple_8_T1, Generic_Tuple_GenericClasses_Tuple_8_T2, Generic_Tuple_GenericClasses_Tuple_8_T3, Generic_Tuple_GenericClasses_Tuple_8_T4, Generic_Tuple_GenericClasses_Tuple_8_T5, Generic_Tuple_GenericClasses_Tuple_8_T6, Generic_Tuple_GenericClasses_Tuple_8_T7, Generic_Tuple_GenericClasses_Tuple_8_TRest]]: ...

class Tuple(Tuple_0, metaclass =Tuple_GenericClasses): ...

class Tuple_0(abc.ABC):
    # Skipped Create due to it being static, abstract and generic.

    Create : Create_MethodGroup
    class Create_MethodGroup:
        @typing.overload
        def __getitem__(self, t:typing.Type[Create_1_T1]) -> Create_1[Create_1_T1]: ...

        Create_1_T1 = typing.TypeVar('Create_1_T1')
        class Create_1(typing.Generic[Create_1_T1]):
            Create_1_T1 = Tuple_0.Create_MethodGroup.Create_1_T1
            def __call__(self, item1: Create_1_T1) -> Tuple_1[Create_1_T1]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Create_2_T1], typing.Type[Create_2_T2]]) -> Create_2[Create_2_T1, Create_2_T2]: ...

        Create_2_T1 = typing.TypeVar('Create_2_T1')
        Create_2_T2 = typing.TypeVar('Create_2_T2')
        class Create_2(typing.Generic[Create_2_T1, Create_2_T2]):
            Create_2_T1 = Tuple_0.Create_MethodGroup.Create_2_T1
            Create_2_T2 = Tuple_0.Create_MethodGroup.Create_2_T2
            def __call__(self, item1: Create_2_T1, item2: Create_2_T2) -> Tuple_2[Create_2_T1, Create_2_T2]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Create_3_T1], typing.Type[Create_3_T2], typing.Type[Create_3_T3]]) -> Create_3[Create_3_T1, Create_3_T2, Create_3_T3]: ...

        Create_3_T1 = typing.TypeVar('Create_3_T1')
        Create_3_T2 = typing.TypeVar('Create_3_T2')
        Create_3_T3 = typing.TypeVar('Create_3_T3')
        class Create_3(typing.Generic[Create_3_T1, Create_3_T2, Create_3_T3]):
            Create_3_T1 = Tuple_0.Create_MethodGroup.Create_3_T1
            Create_3_T2 = Tuple_0.Create_MethodGroup.Create_3_T2
            Create_3_T3 = Tuple_0.Create_MethodGroup.Create_3_T3
            def __call__(self, item1: Create_3_T1, item2: Create_3_T2, item3: Create_3_T3) -> Tuple_3[Create_3_T1, Create_3_T2, Create_3_T3]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Create_4_T1], typing.Type[Create_4_T2], typing.Type[Create_4_T3], typing.Type[Create_4_T4]]) -> Create_4[Create_4_T1, Create_4_T2, Create_4_T3, Create_4_T4]: ...

        Create_4_T1 = typing.TypeVar('Create_4_T1')
        Create_4_T2 = typing.TypeVar('Create_4_T2')
        Create_4_T3 = typing.TypeVar('Create_4_T3')
        Create_4_T4 = typing.TypeVar('Create_4_T4')
        class Create_4(typing.Generic[Create_4_T1, Create_4_T2, Create_4_T3, Create_4_T4]):
            Create_4_T1 = Tuple_0.Create_MethodGroup.Create_4_T1
            Create_4_T2 = Tuple_0.Create_MethodGroup.Create_4_T2
            Create_4_T3 = Tuple_0.Create_MethodGroup.Create_4_T3
            Create_4_T4 = Tuple_0.Create_MethodGroup.Create_4_T4
            def __call__(self, item1: Create_4_T1, item2: Create_4_T2, item3: Create_4_T3, item4: Create_4_T4) -> Tuple_4[Create_4_T1, Create_4_T2, Create_4_T3, Create_4_T4]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Create_5_T1], typing.Type[Create_5_T2], typing.Type[Create_5_T3], typing.Type[Create_5_T4], typing.Type[Create_5_T5]]) -> Create_5[Create_5_T1, Create_5_T2, Create_5_T3, Create_5_T4, Create_5_T5]: ...

        Create_5_T1 = typing.TypeVar('Create_5_T1')
        Create_5_T2 = typing.TypeVar('Create_5_T2')
        Create_5_T3 = typing.TypeVar('Create_5_T3')
        Create_5_T4 = typing.TypeVar('Create_5_T4')
        Create_5_T5 = typing.TypeVar('Create_5_T5')
        class Create_5(typing.Generic[Create_5_T1, Create_5_T2, Create_5_T3, Create_5_T4, Create_5_T5]):
            Create_5_T1 = Tuple_0.Create_MethodGroup.Create_5_T1
            Create_5_T2 = Tuple_0.Create_MethodGroup.Create_5_T2
            Create_5_T3 = Tuple_0.Create_MethodGroup.Create_5_T3
            Create_5_T4 = Tuple_0.Create_MethodGroup.Create_5_T4
            Create_5_T5 = Tuple_0.Create_MethodGroup.Create_5_T5
            def __call__(self, item1: Create_5_T1, item2: Create_5_T2, item3: Create_5_T3, item4: Create_5_T4, item5: Create_5_T5) -> Tuple_5[Create_5_T1, Create_5_T2, Create_5_T3, Create_5_T4, Create_5_T5]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Create_6_T1], typing.Type[Create_6_T2], typing.Type[Create_6_T3], typing.Type[Create_6_T4], typing.Type[Create_6_T5], typing.Type[Create_6_T6]]) -> Create_6[Create_6_T1, Create_6_T2, Create_6_T3, Create_6_T4, Create_6_T5, Create_6_T6]: ...

        Create_6_T1 = typing.TypeVar('Create_6_T1')
        Create_6_T2 = typing.TypeVar('Create_6_T2')
        Create_6_T3 = typing.TypeVar('Create_6_T3')
        Create_6_T4 = typing.TypeVar('Create_6_T4')
        Create_6_T5 = typing.TypeVar('Create_6_T5')
        Create_6_T6 = typing.TypeVar('Create_6_T6')
        class Create_6(typing.Generic[Create_6_T1, Create_6_T2, Create_6_T3, Create_6_T4, Create_6_T5, Create_6_T6]):
            Create_6_T1 = Tuple_0.Create_MethodGroup.Create_6_T1
            Create_6_T2 = Tuple_0.Create_MethodGroup.Create_6_T2
            Create_6_T3 = Tuple_0.Create_MethodGroup.Create_6_T3
            Create_6_T4 = Tuple_0.Create_MethodGroup.Create_6_T4
            Create_6_T5 = Tuple_0.Create_MethodGroup.Create_6_T5
            Create_6_T6 = Tuple_0.Create_MethodGroup.Create_6_T6
            def __call__(self, item1: Create_6_T1, item2: Create_6_T2, item3: Create_6_T3, item4: Create_6_T4, item5: Create_6_T5, item6: Create_6_T6) -> Tuple_6[Create_6_T1, Create_6_T2, Create_6_T3, Create_6_T4, Create_6_T5, Create_6_T6]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Create_7_T1], typing.Type[Create_7_T2], typing.Type[Create_7_T3], typing.Type[Create_7_T4], typing.Type[Create_7_T5], typing.Type[Create_7_T6], typing.Type[Create_7_T7]]) -> Create_7[Create_7_T1, Create_7_T2, Create_7_T3, Create_7_T4, Create_7_T5, Create_7_T6, Create_7_T7]: ...

        Create_7_T1 = typing.TypeVar('Create_7_T1')
        Create_7_T2 = typing.TypeVar('Create_7_T2')
        Create_7_T3 = typing.TypeVar('Create_7_T3')
        Create_7_T4 = typing.TypeVar('Create_7_T4')
        Create_7_T5 = typing.TypeVar('Create_7_T5')
        Create_7_T6 = typing.TypeVar('Create_7_T6')
        Create_7_T7 = typing.TypeVar('Create_7_T7')
        class Create_7(typing.Generic[Create_7_T1, Create_7_T2, Create_7_T3, Create_7_T4, Create_7_T5, Create_7_T6, Create_7_T7]):
            Create_7_T1 = Tuple_0.Create_MethodGroup.Create_7_T1
            Create_7_T2 = Tuple_0.Create_MethodGroup.Create_7_T2
            Create_7_T3 = Tuple_0.Create_MethodGroup.Create_7_T3
            Create_7_T4 = Tuple_0.Create_MethodGroup.Create_7_T4
            Create_7_T5 = Tuple_0.Create_MethodGroup.Create_7_T5
            Create_7_T6 = Tuple_0.Create_MethodGroup.Create_7_T6
            Create_7_T7 = Tuple_0.Create_MethodGroup.Create_7_T7
            def __call__(self, item1: Create_7_T1, item2: Create_7_T2, item3: Create_7_T3, item4: Create_7_T4, item5: Create_7_T5, item6: Create_7_T6, item7: Create_7_T7) -> Tuple_7[Create_7_T1, Create_7_T2, Create_7_T3, Create_7_T4, Create_7_T5, Create_7_T6, Create_7_T7]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Create_8_T1], typing.Type[Create_8_T2], typing.Type[Create_8_T3], typing.Type[Create_8_T4], typing.Type[Create_8_T5], typing.Type[Create_8_T6], typing.Type[Create_8_T7], typing.Type[Create_8_T8]]) -> Create_8[Create_8_T1, Create_8_T2, Create_8_T3, Create_8_T4, Create_8_T5, Create_8_T6, Create_8_T7, Create_8_T8]: ...

        Create_8_T1 = typing.TypeVar('Create_8_T1')
        Create_8_T2 = typing.TypeVar('Create_8_T2')
        Create_8_T3 = typing.TypeVar('Create_8_T3')
        Create_8_T4 = typing.TypeVar('Create_8_T4')
        Create_8_T5 = typing.TypeVar('Create_8_T5')
        Create_8_T6 = typing.TypeVar('Create_8_T6')
        Create_8_T7 = typing.TypeVar('Create_8_T7')
        Create_8_T8 = typing.TypeVar('Create_8_T8')
        class Create_8(typing.Generic[Create_8_T1, Create_8_T2, Create_8_T3, Create_8_T4, Create_8_T5, Create_8_T6, Create_8_T7, Create_8_T8]):
            Create_8_T1 = Tuple_0.Create_MethodGroup.Create_8_T1
            Create_8_T2 = Tuple_0.Create_MethodGroup.Create_8_T2
            Create_8_T3 = Tuple_0.Create_MethodGroup.Create_8_T3
            Create_8_T4 = Tuple_0.Create_MethodGroup.Create_8_T4
            Create_8_T5 = Tuple_0.Create_MethodGroup.Create_8_T5
            Create_8_T6 = Tuple_0.Create_MethodGroup.Create_8_T6
            Create_8_T7 = Tuple_0.Create_MethodGroup.Create_8_T7
            Create_8_T8 = Tuple_0.Create_MethodGroup.Create_8_T8
            def __call__(self, item1: Create_8_T1, item2: Create_8_T2, item3: Create_8_T3, item4: Create_8_T4, item5: Create_8_T5, item6: Create_8_T6, item7: Create_8_T7, item8: Create_8_T8) -> Tuple_8[Create_8_T1, Create_8_T2, Create_8_T3, Create_8_T4, Create_8_T5, Create_8_T6, Create_8_T7, Tuple_1[Create_8_T8]]:...




Tuple_1_T1 = typing.TypeVar('Tuple_1_T1')
class Tuple_1(typing.Generic[Tuple_1_T1], IComparable_0, IStructuralComparable, IStructuralEquatable):
    def __init__(self, item1: Tuple_1_T1) -> None: ...
    @property
    def Item1(self) -> Tuple_1_T1: ...
    def Equals(self, obj: typing.Any) -> bool: ...
    def GetHashCode(self) -> int: ...
    def ToString(self) -> str: ...


Tuple_2_T1 = typing.TypeVar('Tuple_2_T1')
Tuple_2_T2 = typing.TypeVar('Tuple_2_T2')
class Tuple_2(typing.Generic[Tuple_2_T1, Tuple_2_T2], IComparable_0, IStructuralComparable, IStructuralEquatable):
    def __init__(self, item1: Tuple_2_T1, item2: Tuple_2_T2) -> None: ...
    @property
    def Item1(self) -> Tuple_2_T1: ...
    @property
    def Item2(self) -> Tuple_2_T2: ...
    def Equals(self, obj: typing.Any) -> bool: ...
    def GetHashCode(self) -> int: ...
    def ToString(self) -> str: ...


Tuple_3_T1 = typing.TypeVar('Tuple_3_T1')
Tuple_3_T2 = typing.TypeVar('Tuple_3_T2')
Tuple_3_T3 = typing.TypeVar('Tuple_3_T3')
class Tuple_3(typing.Generic[Tuple_3_T1, Tuple_3_T2, Tuple_3_T3], IComparable_0, IStructuralComparable, IStructuralEquatable):
    def __init__(self, item1: Tuple_3_T1, item2: Tuple_3_T2, item3: Tuple_3_T3) -> None: ...
    @property
    def Item1(self) -> Tuple_3_T1: ...
    @property
    def Item2(self) -> Tuple_3_T2: ...
    @property
    def Item3(self) -> Tuple_3_T3: ...
    def Equals(self, obj: typing.Any) -> bool: ...
    def GetHashCode(self) -> int: ...
    def ToString(self) -> str: ...


Tuple_4_T1 = typing.TypeVar('Tuple_4_T1')
Tuple_4_T2 = typing.TypeVar('Tuple_4_T2')
Tuple_4_T3 = typing.TypeVar('Tuple_4_T3')
Tuple_4_T4 = typing.TypeVar('Tuple_4_T4')
class Tuple_4(typing.Generic[Tuple_4_T1, Tuple_4_T2, Tuple_4_T3, Tuple_4_T4], IComparable_0, IStructuralComparable, IStructuralEquatable):
    def __init__(self, item1: Tuple_4_T1, item2: Tuple_4_T2, item3: Tuple_4_T3, item4: Tuple_4_T4) -> None: ...
    @property
    def Item1(self) -> Tuple_4_T1: ...
    @property
    def Item2(self) -> Tuple_4_T2: ...
    @property
    def Item3(self) -> Tuple_4_T3: ...
    @property
    def Item4(self) -> Tuple_4_T4: ...
    def Equals(self, obj: typing.Any) -> bool: ...
    def GetHashCode(self) -> int: ...
    def ToString(self) -> str: ...


Tuple_5_T1 = typing.TypeVar('Tuple_5_T1')
Tuple_5_T2 = typing.TypeVar('Tuple_5_T2')
Tuple_5_T3 = typing.TypeVar('Tuple_5_T3')
Tuple_5_T4 = typing.TypeVar('Tuple_5_T4')
Tuple_5_T5 = typing.TypeVar('Tuple_5_T5')
class Tuple_5(typing.Generic[Tuple_5_T1, Tuple_5_T2, Tuple_5_T3, Tuple_5_T4, Tuple_5_T5], IComparable_0, IStructuralComparable, IStructuralEquatable):
    def __init__(self, item1: Tuple_5_T1, item2: Tuple_5_T2, item3: Tuple_5_T3, item4: Tuple_5_T4, item5: Tuple_5_T5) -> None: ...
    @property
    def Item1(self) -> Tuple_5_T1: ...
    @property
    def Item2(self) -> Tuple_5_T2: ...
    @property
    def Item3(self) -> Tuple_5_T3: ...
    @property
    def Item4(self) -> Tuple_5_T4: ...
    @property
    def Item5(self) -> Tuple_5_T5: ...
    def Equals(self, obj: typing.Any) -> bool: ...
    def GetHashCode(self) -> int: ...
    def ToString(self) -> str: ...


Tuple_6_T1 = typing.TypeVar('Tuple_6_T1')
Tuple_6_T2 = typing.TypeVar('Tuple_6_T2')
Tuple_6_T3 = typing.TypeVar('Tuple_6_T3')
Tuple_6_T4 = typing.TypeVar('Tuple_6_T4')
Tuple_6_T5 = typing.TypeVar('Tuple_6_T5')
Tuple_6_T6 = typing.TypeVar('Tuple_6_T6')
class Tuple_6(typing.Generic[Tuple_6_T1, Tuple_6_T2, Tuple_6_T3, Tuple_6_T4, Tuple_6_T5, Tuple_6_T6], IComparable_0, IStructuralComparable, IStructuralEquatable):
    def __init__(self, item1: Tuple_6_T1, item2: Tuple_6_T2, item3: Tuple_6_T3, item4: Tuple_6_T4, item5: Tuple_6_T5, item6: Tuple_6_T6) -> None: ...
    @property
    def Item1(self) -> Tuple_6_T1: ...
    @property
    def Item2(self) -> Tuple_6_T2: ...
    @property
    def Item3(self) -> Tuple_6_T3: ...
    @property
    def Item4(self) -> Tuple_6_T4: ...
    @property
    def Item5(self) -> Tuple_6_T5: ...
    @property
    def Item6(self) -> Tuple_6_T6: ...
    def Equals(self, obj: typing.Any) -> bool: ...
    def GetHashCode(self) -> int: ...
    def ToString(self) -> str: ...


Tuple_7_T1 = typing.TypeVar('Tuple_7_T1')
Tuple_7_T2 = typing.TypeVar('Tuple_7_T2')
Tuple_7_T3 = typing.TypeVar('Tuple_7_T3')
Tuple_7_T4 = typing.TypeVar('Tuple_7_T4')
Tuple_7_T5 = typing.TypeVar('Tuple_7_T5')
Tuple_7_T6 = typing.TypeVar('Tuple_7_T6')
Tuple_7_T7 = typing.TypeVar('Tuple_7_T7')
class Tuple_7(typing.Generic[Tuple_7_T1, Tuple_7_T2, Tuple_7_T3, Tuple_7_T4, Tuple_7_T5, Tuple_7_T6, Tuple_7_T7], IComparable_0, IStructuralComparable, IStructuralEquatable):
    def __init__(self, item1: Tuple_7_T1, item2: Tuple_7_T2, item3: Tuple_7_T3, item4: Tuple_7_T4, item5: Tuple_7_T5, item6: Tuple_7_T6, item7: Tuple_7_T7) -> None: ...
    @property
    def Item1(self) -> Tuple_7_T1: ...
    @property
    def Item2(self) -> Tuple_7_T2: ...
    @property
    def Item3(self) -> Tuple_7_T3: ...
    @property
    def Item4(self) -> Tuple_7_T4: ...
    @property
    def Item5(self) -> Tuple_7_T5: ...
    @property
    def Item6(self) -> Tuple_7_T6: ...
    @property
    def Item7(self) -> Tuple_7_T7: ...
    def Equals(self, obj: typing.Any) -> bool: ...
    def GetHashCode(self) -> int: ...
    def ToString(self) -> str: ...


Tuple_8_T1 = typing.TypeVar('Tuple_8_T1')
Tuple_8_T2 = typing.TypeVar('Tuple_8_T2')
Tuple_8_T3 = typing.TypeVar('Tuple_8_T3')
Tuple_8_T4 = typing.TypeVar('Tuple_8_T4')
Tuple_8_T5 = typing.TypeVar('Tuple_8_T5')
Tuple_8_T6 = typing.TypeVar('Tuple_8_T6')
Tuple_8_T7 = typing.TypeVar('Tuple_8_T7')
Tuple_8_TRest = typing.TypeVar('Tuple_8_TRest')
class Tuple_8(typing.Generic[Tuple_8_T1, Tuple_8_T2, Tuple_8_T3, Tuple_8_T4, Tuple_8_T5, Tuple_8_T6, Tuple_8_T7, Tuple_8_TRest], IComparable_0, IStructuralComparable, IStructuralEquatable):
    def __init__(self, item1: Tuple_8_T1, item2: Tuple_8_T2, item3: Tuple_8_T3, item4: Tuple_8_T4, item5: Tuple_8_T5, item6: Tuple_8_T6, item7: Tuple_8_T7, rest: Tuple_8_TRest) -> None: ...
    @property
    def Item1(self) -> Tuple_8_T1: ...
    @property
    def Item2(self) -> Tuple_8_T2: ...
    @property
    def Item3(self) -> Tuple_8_T3: ...
    @property
    def Item4(self) -> Tuple_8_T4: ...
    @property
    def Item5(self) -> Tuple_8_T5: ...
    @property
    def Item6(self) -> Tuple_8_T6: ...
    @property
    def Item7(self) -> Tuple_8_T7: ...
    @property
    def Rest(self) -> Tuple_8_TRest: ...
    def Equals(self, obj: typing.Any) -> bool: ...
    def GetHashCode(self) -> int: ...
    def ToString(self) -> str: ...


class TupleExtensions(abc.ABC):
    # Skipped Deconstruct due to it being static, abstract and generic.

    Deconstruct : Deconstruct_MethodGroup
    class Deconstruct_MethodGroup:
        @typing.overload
        def __getitem__(self, t:typing.Type[Deconstruct_1_T1]) -> Deconstruct_1[Deconstruct_1_T1]: ...

        Deconstruct_1_T1 = typing.TypeVar('Deconstruct_1_T1')
        class Deconstruct_1(typing.Generic[Deconstruct_1_T1]):
            Deconstruct_1_T1 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_1_T1
            def __call__(self, value: Tuple_1[Deconstruct_1_T1], item1: clr.Reference[Deconstruct_1_T1]) -> None:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Deconstruct_2_T1], typing.Type[Deconstruct_2_T2]]) -> Deconstruct_2[Deconstruct_2_T1, Deconstruct_2_T2]: ...

        Deconstruct_2_T1 = typing.TypeVar('Deconstruct_2_T1')
        Deconstruct_2_T2 = typing.TypeVar('Deconstruct_2_T2')
        class Deconstruct_2(typing.Generic[Deconstruct_2_T1, Deconstruct_2_T2]):
            Deconstruct_2_T1 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_2_T1
            Deconstruct_2_T2 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_2_T2
            def __call__(self, value: Tuple_2[Deconstruct_2_T1, Deconstruct_2_T2], item1: clr.Reference[Deconstruct_2_T1], item2: clr.Reference[Deconstruct_2_T2]) -> None:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Deconstruct_3_T1], typing.Type[Deconstruct_3_T2], typing.Type[Deconstruct_3_T3]]) -> Deconstruct_3[Deconstruct_3_T1, Deconstruct_3_T2, Deconstruct_3_T3]: ...

        Deconstruct_3_T1 = typing.TypeVar('Deconstruct_3_T1')
        Deconstruct_3_T2 = typing.TypeVar('Deconstruct_3_T2')
        Deconstruct_3_T3 = typing.TypeVar('Deconstruct_3_T3')
        class Deconstruct_3(typing.Generic[Deconstruct_3_T1, Deconstruct_3_T2, Deconstruct_3_T3]):
            Deconstruct_3_T1 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_3_T1
            Deconstruct_3_T2 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_3_T2
            Deconstruct_3_T3 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_3_T3
            def __call__(self, value: Tuple_3[Deconstruct_3_T1, Deconstruct_3_T2, Deconstruct_3_T3], item1: clr.Reference[Deconstruct_3_T1], item2: clr.Reference[Deconstruct_3_T2], item3: clr.Reference[Deconstruct_3_T3]) -> None:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Deconstruct_4_T1], typing.Type[Deconstruct_4_T2], typing.Type[Deconstruct_4_T3], typing.Type[Deconstruct_4_T4]]) -> Deconstruct_4[Deconstruct_4_T1, Deconstruct_4_T2, Deconstruct_4_T3, Deconstruct_4_T4]: ...

        Deconstruct_4_T1 = typing.TypeVar('Deconstruct_4_T1')
        Deconstruct_4_T2 = typing.TypeVar('Deconstruct_4_T2')
        Deconstruct_4_T3 = typing.TypeVar('Deconstruct_4_T3')
        Deconstruct_4_T4 = typing.TypeVar('Deconstruct_4_T4')
        class Deconstruct_4(typing.Generic[Deconstruct_4_T1, Deconstruct_4_T2, Deconstruct_4_T3, Deconstruct_4_T4]):
            Deconstruct_4_T1 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_4_T1
            Deconstruct_4_T2 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_4_T2
            Deconstruct_4_T3 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_4_T3
            Deconstruct_4_T4 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_4_T4
            def __call__(self, value: Tuple_4[Deconstruct_4_T1, Deconstruct_4_T2, Deconstruct_4_T3, Deconstruct_4_T4], item1: clr.Reference[Deconstruct_4_T1], item2: clr.Reference[Deconstruct_4_T2], item3: clr.Reference[Deconstruct_4_T3], item4: clr.Reference[Deconstruct_4_T4]) -> None:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Deconstruct_5_T1], typing.Type[Deconstruct_5_T2], typing.Type[Deconstruct_5_T3], typing.Type[Deconstruct_5_T4], typing.Type[Deconstruct_5_T5]]) -> Deconstruct_5[Deconstruct_5_T1, Deconstruct_5_T2, Deconstruct_5_T3, Deconstruct_5_T4, Deconstruct_5_T5]: ...

        Deconstruct_5_T1 = typing.TypeVar('Deconstruct_5_T1')
        Deconstruct_5_T2 = typing.TypeVar('Deconstruct_5_T2')
        Deconstruct_5_T3 = typing.TypeVar('Deconstruct_5_T3')
        Deconstruct_5_T4 = typing.TypeVar('Deconstruct_5_T4')
        Deconstruct_5_T5 = typing.TypeVar('Deconstruct_5_T5')
        class Deconstruct_5(typing.Generic[Deconstruct_5_T1, Deconstruct_5_T2, Deconstruct_5_T3, Deconstruct_5_T4, Deconstruct_5_T5]):
            Deconstruct_5_T1 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_5_T1
            Deconstruct_5_T2 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_5_T2
            Deconstruct_5_T3 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_5_T3
            Deconstruct_5_T4 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_5_T4
            Deconstruct_5_T5 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_5_T5
            def __call__(self, value: Tuple_5[Deconstruct_5_T1, Deconstruct_5_T2, Deconstruct_5_T3, Deconstruct_5_T4, Deconstruct_5_T5], item1: clr.Reference[Deconstruct_5_T1], item2: clr.Reference[Deconstruct_5_T2], item3: clr.Reference[Deconstruct_5_T3], item4: clr.Reference[Deconstruct_5_T4], item5: clr.Reference[Deconstruct_5_T5]) -> None:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Deconstruct_6_T1], typing.Type[Deconstruct_6_T2], typing.Type[Deconstruct_6_T3], typing.Type[Deconstruct_6_T4], typing.Type[Deconstruct_6_T5], typing.Type[Deconstruct_6_T6]]) -> Deconstruct_6[Deconstruct_6_T1, Deconstruct_6_T2, Deconstruct_6_T3, Deconstruct_6_T4, Deconstruct_6_T5, Deconstruct_6_T6]: ...

        Deconstruct_6_T1 = typing.TypeVar('Deconstruct_6_T1')
        Deconstruct_6_T2 = typing.TypeVar('Deconstruct_6_T2')
        Deconstruct_6_T3 = typing.TypeVar('Deconstruct_6_T3')
        Deconstruct_6_T4 = typing.TypeVar('Deconstruct_6_T4')
        Deconstruct_6_T5 = typing.TypeVar('Deconstruct_6_T5')
        Deconstruct_6_T6 = typing.TypeVar('Deconstruct_6_T6')
        class Deconstruct_6(typing.Generic[Deconstruct_6_T1, Deconstruct_6_T2, Deconstruct_6_T3, Deconstruct_6_T4, Deconstruct_6_T5, Deconstruct_6_T6]):
            Deconstruct_6_T1 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_6_T1
            Deconstruct_6_T2 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_6_T2
            Deconstruct_6_T3 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_6_T3
            Deconstruct_6_T4 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_6_T4
            Deconstruct_6_T5 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_6_T5
            Deconstruct_6_T6 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_6_T6
            def __call__(self, value: Tuple_6[Deconstruct_6_T1, Deconstruct_6_T2, Deconstruct_6_T3, Deconstruct_6_T4, Deconstruct_6_T5, Deconstruct_6_T6], item1: clr.Reference[Deconstruct_6_T1], item2: clr.Reference[Deconstruct_6_T2], item3: clr.Reference[Deconstruct_6_T3], item4: clr.Reference[Deconstruct_6_T4], item5: clr.Reference[Deconstruct_6_T5], item6: clr.Reference[Deconstruct_6_T6]) -> None:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Deconstruct_7_T1], typing.Type[Deconstruct_7_T2], typing.Type[Deconstruct_7_T3], typing.Type[Deconstruct_7_T4], typing.Type[Deconstruct_7_T5], typing.Type[Deconstruct_7_T6], typing.Type[Deconstruct_7_T7]]) -> Deconstruct_7[Deconstruct_7_T1, Deconstruct_7_T2, Deconstruct_7_T3, Deconstruct_7_T4, Deconstruct_7_T5, Deconstruct_7_T6, Deconstruct_7_T7]: ...

        Deconstruct_7_T1 = typing.TypeVar('Deconstruct_7_T1')
        Deconstruct_7_T2 = typing.TypeVar('Deconstruct_7_T2')
        Deconstruct_7_T3 = typing.TypeVar('Deconstruct_7_T3')
        Deconstruct_7_T4 = typing.TypeVar('Deconstruct_7_T4')
        Deconstruct_7_T5 = typing.TypeVar('Deconstruct_7_T5')
        Deconstruct_7_T6 = typing.TypeVar('Deconstruct_7_T6')
        Deconstruct_7_T7 = typing.TypeVar('Deconstruct_7_T7')
        class Deconstruct_7(typing.Generic[Deconstruct_7_T1, Deconstruct_7_T2, Deconstruct_7_T3, Deconstruct_7_T4, Deconstruct_7_T5, Deconstruct_7_T6, Deconstruct_7_T7]):
            Deconstruct_7_T1 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_7_T1
            Deconstruct_7_T2 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_7_T2
            Deconstruct_7_T3 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_7_T3
            Deconstruct_7_T4 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_7_T4
            Deconstruct_7_T5 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_7_T5
            Deconstruct_7_T6 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_7_T6
            Deconstruct_7_T7 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_7_T7
            def __call__(self, value: Tuple_7[Deconstruct_7_T1, Deconstruct_7_T2, Deconstruct_7_T3, Deconstruct_7_T4, Deconstruct_7_T5, Deconstruct_7_T6, Deconstruct_7_T7], item1: clr.Reference[Deconstruct_7_T1], item2: clr.Reference[Deconstruct_7_T2], item3: clr.Reference[Deconstruct_7_T3], item4: clr.Reference[Deconstruct_7_T4], item5: clr.Reference[Deconstruct_7_T5], item6: clr.Reference[Deconstruct_7_T6], item7: clr.Reference[Deconstruct_7_T7]) -> None:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Deconstruct_8_T1], typing.Type[Deconstruct_8_T2], typing.Type[Deconstruct_8_T3], typing.Type[Deconstruct_8_T4], typing.Type[Deconstruct_8_T5], typing.Type[Deconstruct_8_T6], typing.Type[Deconstruct_8_T7], typing.Type[Deconstruct_8_T8]]) -> Deconstruct_8[Deconstruct_8_T1, Deconstruct_8_T2, Deconstruct_8_T3, Deconstruct_8_T4, Deconstruct_8_T5, Deconstruct_8_T6, Deconstruct_8_T7, Deconstruct_8_T8]: ...

        Deconstruct_8_T1 = typing.TypeVar('Deconstruct_8_T1')
        Deconstruct_8_T2 = typing.TypeVar('Deconstruct_8_T2')
        Deconstruct_8_T3 = typing.TypeVar('Deconstruct_8_T3')
        Deconstruct_8_T4 = typing.TypeVar('Deconstruct_8_T4')
        Deconstruct_8_T5 = typing.TypeVar('Deconstruct_8_T5')
        Deconstruct_8_T6 = typing.TypeVar('Deconstruct_8_T6')
        Deconstruct_8_T7 = typing.TypeVar('Deconstruct_8_T7')
        Deconstruct_8_T8 = typing.TypeVar('Deconstruct_8_T8')
        class Deconstruct_8(typing.Generic[Deconstruct_8_T1, Deconstruct_8_T2, Deconstruct_8_T3, Deconstruct_8_T4, Deconstruct_8_T5, Deconstruct_8_T6, Deconstruct_8_T7, Deconstruct_8_T8]):
            Deconstruct_8_T1 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_8_T1
            Deconstruct_8_T2 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_8_T2
            Deconstruct_8_T3 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_8_T3
            Deconstruct_8_T4 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_8_T4
            Deconstruct_8_T5 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_8_T5
            Deconstruct_8_T6 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_8_T6
            Deconstruct_8_T7 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_8_T7
            Deconstruct_8_T8 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_8_T8
            def __call__(self, value: Tuple_8[Deconstruct_8_T1, Deconstruct_8_T2, Deconstruct_8_T3, Deconstruct_8_T4, Deconstruct_8_T5, Deconstruct_8_T6, Deconstruct_8_T7, Tuple_1[Deconstruct_8_T8]], item1: clr.Reference[Deconstruct_8_T1], item2: clr.Reference[Deconstruct_8_T2], item3: clr.Reference[Deconstruct_8_T3], item4: clr.Reference[Deconstruct_8_T4], item5: clr.Reference[Deconstruct_8_T5], item6: clr.Reference[Deconstruct_8_T6], item7: clr.Reference[Deconstruct_8_T7], item8: clr.Reference[Deconstruct_8_T8]) -> None:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Deconstruct_9_T1], typing.Type[Deconstruct_9_T2], typing.Type[Deconstruct_9_T3], typing.Type[Deconstruct_9_T4], typing.Type[Deconstruct_9_T5], typing.Type[Deconstruct_9_T6], typing.Type[Deconstruct_9_T7], typing.Type[Deconstruct_9_T8], typing.Type[Deconstruct_9_T9]]) -> Deconstruct_9[Deconstruct_9_T1, Deconstruct_9_T2, Deconstruct_9_T3, Deconstruct_9_T4, Deconstruct_9_T5, Deconstruct_9_T6, Deconstruct_9_T7, Deconstruct_9_T8, Deconstruct_9_T9]: ...

        Deconstruct_9_T1 = typing.TypeVar('Deconstruct_9_T1')
        Deconstruct_9_T2 = typing.TypeVar('Deconstruct_9_T2')
        Deconstruct_9_T3 = typing.TypeVar('Deconstruct_9_T3')
        Deconstruct_9_T4 = typing.TypeVar('Deconstruct_9_T4')
        Deconstruct_9_T5 = typing.TypeVar('Deconstruct_9_T5')
        Deconstruct_9_T6 = typing.TypeVar('Deconstruct_9_T6')
        Deconstruct_9_T7 = typing.TypeVar('Deconstruct_9_T7')
        Deconstruct_9_T8 = typing.TypeVar('Deconstruct_9_T8')
        Deconstruct_9_T9 = typing.TypeVar('Deconstruct_9_T9')
        class Deconstruct_9(typing.Generic[Deconstruct_9_T1, Deconstruct_9_T2, Deconstruct_9_T3, Deconstruct_9_T4, Deconstruct_9_T5, Deconstruct_9_T6, Deconstruct_9_T7, Deconstruct_9_T8, Deconstruct_9_T9]):
            Deconstruct_9_T1 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_9_T1
            Deconstruct_9_T2 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_9_T2
            Deconstruct_9_T3 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_9_T3
            Deconstruct_9_T4 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_9_T4
            Deconstruct_9_T5 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_9_T5
            Deconstruct_9_T6 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_9_T6
            Deconstruct_9_T7 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_9_T7
            Deconstruct_9_T8 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_9_T8
            Deconstruct_9_T9 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_9_T9
            def __call__(self, value: Tuple_8[Deconstruct_9_T1, Deconstruct_9_T2, Deconstruct_9_T3, Deconstruct_9_T4, Deconstruct_9_T5, Deconstruct_9_T6, Deconstruct_9_T7, Tuple_2[Deconstruct_9_T8, Deconstruct_9_T9]], item1: clr.Reference[Deconstruct_9_T1], item2: clr.Reference[Deconstruct_9_T2], item3: clr.Reference[Deconstruct_9_T3], item4: clr.Reference[Deconstruct_9_T4], item5: clr.Reference[Deconstruct_9_T5], item6: clr.Reference[Deconstruct_9_T6], item7: clr.Reference[Deconstruct_9_T7], item8: clr.Reference[Deconstruct_9_T8], item9: clr.Reference[Deconstruct_9_T9]) -> None:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Deconstruct_10_T1], typing.Type[Deconstruct_10_T2], typing.Type[Deconstruct_10_T3], typing.Type[Deconstruct_10_T4], typing.Type[Deconstruct_10_T5], typing.Type[Deconstruct_10_T6], typing.Type[Deconstruct_10_T7], typing.Type[Deconstruct_10_T8], typing.Type[Deconstruct_10_T9], typing.Type[Deconstruct_10_T10]]) -> Deconstruct_10[Deconstruct_10_T1, Deconstruct_10_T2, Deconstruct_10_T3, Deconstruct_10_T4, Deconstruct_10_T5, Deconstruct_10_T6, Deconstruct_10_T7, Deconstruct_10_T8, Deconstruct_10_T9, Deconstruct_10_T10]: ...

        Deconstruct_10_T1 = typing.TypeVar('Deconstruct_10_T1')
        Deconstruct_10_T2 = typing.TypeVar('Deconstruct_10_T2')
        Deconstruct_10_T3 = typing.TypeVar('Deconstruct_10_T3')
        Deconstruct_10_T4 = typing.TypeVar('Deconstruct_10_T4')
        Deconstruct_10_T5 = typing.TypeVar('Deconstruct_10_T5')
        Deconstruct_10_T6 = typing.TypeVar('Deconstruct_10_T6')
        Deconstruct_10_T7 = typing.TypeVar('Deconstruct_10_T7')
        Deconstruct_10_T8 = typing.TypeVar('Deconstruct_10_T8')
        Deconstruct_10_T9 = typing.TypeVar('Deconstruct_10_T9')
        Deconstruct_10_T10 = typing.TypeVar('Deconstruct_10_T10')
        class Deconstruct_10(typing.Generic[Deconstruct_10_T1, Deconstruct_10_T2, Deconstruct_10_T3, Deconstruct_10_T4, Deconstruct_10_T5, Deconstruct_10_T6, Deconstruct_10_T7, Deconstruct_10_T8, Deconstruct_10_T9, Deconstruct_10_T10]):
            Deconstruct_10_T1 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_10_T1
            Deconstruct_10_T2 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_10_T2
            Deconstruct_10_T3 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_10_T3
            Deconstruct_10_T4 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_10_T4
            Deconstruct_10_T5 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_10_T5
            Deconstruct_10_T6 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_10_T6
            Deconstruct_10_T7 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_10_T7
            Deconstruct_10_T8 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_10_T8
            Deconstruct_10_T9 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_10_T9
            Deconstruct_10_T10 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_10_T10
            def __call__(self, value: Tuple_8[Deconstruct_10_T1, Deconstruct_10_T2, Deconstruct_10_T3, Deconstruct_10_T4, Deconstruct_10_T5, Deconstruct_10_T6, Deconstruct_10_T7, Tuple_3[Deconstruct_10_T8, Deconstruct_10_T9, Deconstruct_10_T10]], item1: clr.Reference[Deconstruct_10_T1], item2: clr.Reference[Deconstruct_10_T2], item3: clr.Reference[Deconstruct_10_T3], item4: clr.Reference[Deconstruct_10_T4], item5: clr.Reference[Deconstruct_10_T5], item6: clr.Reference[Deconstruct_10_T6], item7: clr.Reference[Deconstruct_10_T7], item8: clr.Reference[Deconstruct_10_T8], item9: clr.Reference[Deconstruct_10_T9], item10: clr.Reference[Deconstruct_10_T10]) -> None:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Deconstruct_11_T1], typing.Type[Deconstruct_11_T2], typing.Type[Deconstruct_11_T3], typing.Type[Deconstruct_11_T4], typing.Type[Deconstruct_11_T5], typing.Type[Deconstruct_11_T6], typing.Type[Deconstruct_11_T7], typing.Type[Deconstruct_11_T8], typing.Type[Deconstruct_11_T9], typing.Type[Deconstruct_11_T10], typing.Type[Deconstruct_11_T11]]) -> Deconstruct_11[Deconstruct_11_T1, Deconstruct_11_T2, Deconstruct_11_T3, Deconstruct_11_T4, Deconstruct_11_T5, Deconstruct_11_T6, Deconstruct_11_T7, Deconstruct_11_T8, Deconstruct_11_T9, Deconstruct_11_T10, Deconstruct_11_T11]: ...

        Deconstruct_11_T1 = typing.TypeVar('Deconstruct_11_T1')
        Deconstruct_11_T2 = typing.TypeVar('Deconstruct_11_T2')
        Deconstruct_11_T3 = typing.TypeVar('Deconstruct_11_T3')
        Deconstruct_11_T4 = typing.TypeVar('Deconstruct_11_T4')
        Deconstruct_11_T5 = typing.TypeVar('Deconstruct_11_T5')
        Deconstruct_11_T6 = typing.TypeVar('Deconstruct_11_T6')
        Deconstruct_11_T7 = typing.TypeVar('Deconstruct_11_T7')
        Deconstruct_11_T8 = typing.TypeVar('Deconstruct_11_T8')
        Deconstruct_11_T9 = typing.TypeVar('Deconstruct_11_T9')
        Deconstruct_11_T10 = typing.TypeVar('Deconstruct_11_T10')
        Deconstruct_11_T11 = typing.TypeVar('Deconstruct_11_T11')
        class Deconstruct_11(typing.Generic[Deconstruct_11_T1, Deconstruct_11_T2, Deconstruct_11_T3, Deconstruct_11_T4, Deconstruct_11_T5, Deconstruct_11_T6, Deconstruct_11_T7, Deconstruct_11_T8, Deconstruct_11_T9, Deconstruct_11_T10, Deconstruct_11_T11]):
            Deconstruct_11_T1 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_11_T1
            Deconstruct_11_T2 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_11_T2
            Deconstruct_11_T3 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_11_T3
            Deconstruct_11_T4 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_11_T4
            Deconstruct_11_T5 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_11_T5
            Deconstruct_11_T6 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_11_T6
            Deconstruct_11_T7 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_11_T7
            Deconstruct_11_T8 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_11_T8
            Deconstruct_11_T9 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_11_T9
            Deconstruct_11_T10 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_11_T10
            Deconstruct_11_T11 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_11_T11
            def __call__(self, value: Tuple_8[Deconstruct_11_T1, Deconstruct_11_T2, Deconstruct_11_T3, Deconstruct_11_T4, Deconstruct_11_T5, Deconstruct_11_T6, Deconstruct_11_T7, Tuple_4[Deconstruct_11_T8, Deconstruct_11_T9, Deconstruct_11_T10, Deconstruct_11_T11]], item1: clr.Reference[Deconstruct_11_T1], item2: clr.Reference[Deconstruct_11_T2], item3: clr.Reference[Deconstruct_11_T3], item4: clr.Reference[Deconstruct_11_T4], item5: clr.Reference[Deconstruct_11_T5], item6: clr.Reference[Deconstruct_11_T6], item7: clr.Reference[Deconstruct_11_T7], item8: clr.Reference[Deconstruct_11_T8], item9: clr.Reference[Deconstruct_11_T9], item10: clr.Reference[Deconstruct_11_T10], item11: clr.Reference[Deconstruct_11_T11]) -> None:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Deconstruct_12_T1], typing.Type[Deconstruct_12_T2], typing.Type[Deconstruct_12_T3], typing.Type[Deconstruct_12_T4], typing.Type[Deconstruct_12_T5], typing.Type[Deconstruct_12_T6], typing.Type[Deconstruct_12_T7], typing.Type[Deconstruct_12_T8], typing.Type[Deconstruct_12_T9], typing.Type[Deconstruct_12_T10], typing.Type[Deconstruct_12_T11], typing.Type[Deconstruct_12_T12]]) -> Deconstruct_12[Deconstruct_12_T1, Deconstruct_12_T2, Deconstruct_12_T3, Deconstruct_12_T4, Deconstruct_12_T5, Deconstruct_12_T6, Deconstruct_12_T7, Deconstruct_12_T8, Deconstruct_12_T9, Deconstruct_12_T10, Deconstruct_12_T11, Deconstruct_12_T12]: ...

        Deconstruct_12_T1 = typing.TypeVar('Deconstruct_12_T1')
        Deconstruct_12_T2 = typing.TypeVar('Deconstruct_12_T2')
        Deconstruct_12_T3 = typing.TypeVar('Deconstruct_12_T3')
        Deconstruct_12_T4 = typing.TypeVar('Deconstruct_12_T4')
        Deconstruct_12_T5 = typing.TypeVar('Deconstruct_12_T5')
        Deconstruct_12_T6 = typing.TypeVar('Deconstruct_12_T6')
        Deconstruct_12_T7 = typing.TypeVar('Deconstruct_12_T7')
        Deconstruct_12_T8 = typing.TypeVar('Deconstruct_12_T8')
        Deconstruct_12_T9 = typing.TypeVar('Deconstruct_12_T9')
        Deconstruct_12_T10 = typing.TypeVar('Deconstruct_12_T10')
        Deconstruct_12_T11 = typing.TypeVar('Deconstruct_12_T11')
        Deconstruct_12_T12 = typing.TypeVar('Deconstruct_12_T12')
        class Deconstruct_12(typing.Generic[Deconstruct_12_T1, Deconstruct_12_T2, Deconstruct_12_T3, Deconstruct_12_T4, Deconstruct_12_T5, Deconstruct_12_T6, Deconstruct_12_T7, Deconstruct_12_T8, Deconstruct_12_T9, Deconstruct_12_T10, Deconstruct_12_T11, Deconstruct_12_T12]):
            Deconstruct_12_T1 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_12_T1
            Deconstruct_12_T2 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_12_T2
            Deconstruct_12_T3 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_12_T3
            Deconstruct_12_T4 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_12_T4
            Deconstruct_12_T5 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_12_T5
            Deconstruct_12_T6 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_12_T6
            Deconstruct_12_T7 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_12_T7
            Deconstruct_12_T8 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_12_T8
            Deconstruct_12_T9 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_12_T9
            Deconstruct_12_T10 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_12_T10
            Deconstruct_12_T11 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_12_T11
            Deconstruct_12_T12 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_12_T12
            def __call__(self, value: Tuple_8[Deconstruct_12_T1, Deconstruct_12_T2, Deconstruct_12_T3, Deconstruct_12_T4, Deconstruct_12_T5, Deconstruct_12_T6, Deconstruct_12_T7, Tuple_5[Deconstruct_12_T8, Deconstruct_12_T9, Deconstruct_12_T10, Deconstruct_12_T11, Deconstruct_12_T12]], item1: clr.Reference[Deconstruct_12_T1], item2: clr.Reference[Deconstruct_12_T2], item3: clr.Reference[Deconstruct_12_T3], item4: clr.Reference[Deconstruct_12_T4], item5: clr.Reference[Deconstruct_12_T5], item6: clr.Reference[Deconstruct_12_T6], item7: clr.Reference[Deconstruct_12_T7], item8: clr.Reference[Deconstruct_12_T8], item9: clr.Reference[Deconstruct_12_T9], item10: clr.Reference[Deconstruct_12_T10], item11: clr.Reference[Deconstruct_12_T11], item12: clr.Reference[Deconstruct_12_T12]) -> None:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Deconstruct_13_T1], typing.Type[Deconstruct_13_T2], typing.Type[Deconstruct_13_T3], typing.Type[Deconstruct_13_T4], typing.Type[Deconstruct_13_T5], typing.Type[Deconstruct_13_T6], typing.Type[Deconstruct_13_T7], typing.Type[Deconstruct_13_T8], typing.Type[Deconstruct_13_T9], typing.Type[Deconstruct_13_T10], typing.Type[Deconstruct_13_T11], typing.Type[Deconstruct_13_T12], typing.Type[Deconstruct_13_T13]]) -> Deconstruct_13[Deconstruct_13_T1, Deconstruct_13_T2, Deconstruct_13_T3, Deconstruct_13_T4, Deconstruct_13_T5, Deconstruct_13_T6, Deconstruct_13_T7, Deconstruct_13_T8, Deconstruct_13_T9, Deconstruct_13_T10, Deconstruct_13_T11, Deconstruct_13_T12, Deconstruct_13_T13]: ...

        Deconstruct_13_T1 = typing.TypeVar('Deconstruct_13_T1')
        Deconstruct_13_T2 = typing.TypeVar('Deconstruct_13_T2')
        Deconstruct_13_T3 = typing.TypeVar('Deconstruct_13_T3')
        Deconstruct_13_T4 = typing.TypeVar('Deconstruct_13_T4')
        Deconstruct_13_T5 = typing.TypeVar('Deconstruct_13_T5')
        Deconstruct_13_T6 = typing.TypeVar('Deconstruct_13_T6')
        Deconstruct_13_T7 = typing.TypeVar('Deconstruct_13_T7')
        Deconstruct_13_T8 = typing.TypeVar('Deconstruct_13_T8')
        Deconstruct_13_T9 = typing.TypeVar('Deconstruct_13_T9')
        Deconstruct_13_T10 = typing.TypeVar('Deconstruct_13_T10')
        Deconstruct_13_T11 = typing.TypeVar('Deconstruct_13_T11')
        Deconstruct_13_T12 = typing.TypeVar('Deconstruct_13_T12')
        Deconstruct_13_T13 = typing.TypeVar('Deconstruct_13_T13')
        class Deconstruct_13(typing.Generic[Deconstruct_13_T1, Deconstruct_13_T2, Deconstruct_13_T3, Deconstruct_13_T4, Deconstruct_13_T5, Deconstruct_13_T6, Deconstruct_13_T7, Deconstruct_13_T8, Deconstruct_13_T9, Deconstruct_13_T10, Deconstruct_13_T11, Deconstruct_13_T12, Deconstruct_13_T13]):
            Deconstruct_13_T1 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_13_T1
            Deconstruct_13_T2 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_13_T2
            Deconstruct_13_T3 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_13_T3
            Deconstruct_13_T4 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_13_T4
            Deconstruct_13_T5 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_13_T5
            Deconstruct_13_T6 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_13_T6
            Deconstruct_13_T7 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_13_T7
            Deconstruct_13_T8 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_13_T8
            Deconstruct_13_T9 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_13_T9
            Deconstruct_13_T10 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_13_T10
            Deconstruct_13_T11 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_13_T11
            Deconstruct_13_T12 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_13_T12
            Deconstruct_13_T13 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_13_T13
            def __call__(self, value: Tuple_8[Deconstruct_13_T1, Deconstruct_13_T2, Deconstruct_13_T3, Deconstruct_13_T4, Deconstruct_13_T5, Deconstruct_13_T6, Deconstruct_13_T7, Tuple_6[Deconstruct_13_T8, Deconstruct_13_T9, Deconstruct_13_T10, Deconstruct_13_T11, Deconstruct_13_T12, Deconstruct_13_T13]], item1: clr.Reference[Deconstruct_13_T1], item2: clr.Reference[Deconstruct_13_T2], item3: clr.Reference[Deconstruct_13_T3], item4: clr.Reference[Deconstruct_13_T4], item5: clr.Reference[Deconstruct_13_T5], item6: clr.Reference[Deconstruct_13_T6], item7: clr.Reference[Deconstruct_13_T7], item8: clr.Reference[Deconstruct_13_T8], item9: clr.Reference[Deconstruct_13_T9], item10: clr.Reference[Deconstruct_13_T10], item11: clr.Reference[Deconstruct_13_T11], item12: clr.Reference[Deconstruct_13_T12], item13: clr.Reference[Deconstruct_13_T13]) -> None:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Deconstruct_14_T1], typing.Type[Deconstruct_14_T2], typing.Type[Deconstruct_14_T3], typing.Type[Deconstruct_14_T4], typing.Type[Deconstruct_14_T5], typing.Type[Deconstruct_14_T6], typing.Type[Deconstruct_14_T7], typing.Type[Deconstruct_14_T8], typing.Type[Deconstruct_14_T9], typing.Type[Deconstruct_14_T10], typing.Type[Deconstruct_14_T11], typing.Type[Deconstruct_14_T12], typing.Type[Deconstruct_14_T13], typing.Type[Deconstruct_14_T14]]) -> Deconstruct_14[Deconstruct_14_T1, Deconstruct_14_T2, Deconstruct_14_T3, Deconstruct_14_T4, Deconstruct_14_T5, Deconstruct_14_T6, Deconstruct_14_T7, Deconstruct_14_T8, Deconstruct_14_T9, Deconstruct_14_T10, Deconstruct_14_T11, Deconstruct_14_T12, Deconstruct_14_T13, Deconstruct_14_T14]: ...

        Deconstruct_14_T1 = typing.TypeVar('Deconstruct_14_T1')
        Deconstruct_14_T2 = typing.TypeVar('Deconstruct_14_T2')
        Deconstruct_14_T3 = typing.TypeVar('Deconstruct_14_T3')
        Deconstruct_14_T4 = typing.TypeVar('Deconstruct_14_T4')
        Deconstruct_14_T5 = typing.TypeVar('Deconstruct_14_T5')
        Deconstruct_14_T6 = typing.TypeVar('Deconstruct_14_T6')
        Deconstruct_14_T7 = typing.TypeVar('Deconstruct_14_T7')
        Deconstruct_14_T8 = typing.TypeVar('Deconstruct_14_T8')
        Deconstruct_14_T9 = typing.TypeVar('Deconstruct_14_T9')
        Deconstruct_14_T10 = typing.TypeVar('Deconstruct_14_T10')
        Deconstruct_14_T11 = typing.TypeVar('Deconstruct_14_T11')
        Deconstruct_14_T12 = typing.TypeVar('Deconstruct_14_T12')
        Deconstruct_14_T13 = typing.TypeVar('Deconstruct_14_T13')
        Deconstruct_14_T14 = typing.TypeVar('Deconstruct_14_T14')
        class Deconstruct_14(typing.Generic[Deconstruct_14_T1, Deconstruct_14_T2, Deconstruct_14_T3, Deconstruct_14_T4, Deconstruct_14_T5, Deconstruct_14_T6, Deconstruct_14_T7, Deconstruct_14_T8, Deconstruct_14_T9, Deconstruct_14_T10, Deconstruct_14_T11, Deconstruct_14_T12, Deconstruct_14_T13, Deconstruct_14_T14]):
            Deconstruct_14_T1 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_14_T1
            Deconstruct_14_T2 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_14_T2
            Deconstruct_14_T3 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_14_T3
            Deconstruct_14_T4 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_14_T4
            Deconstruct_14_T5 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_14_T5
            Deconstruct_14_T6 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_14_T6
            Deconstruct_14_T7 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_14_T7
            Deconstruct_14_T8 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_14_T8
            Deconstruct_14_T9 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_14_T9
            Deconstruct_14_T10 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_14_T10
            Deconstruct_14_T11 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_14_T11
            Deconstruct_14_T12 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_14_T12
            Deconstruct_14_T13 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_14_T13
            Deconstruct_14_T14 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_14_T14
            def __call__(self, value: Tuple_8[Deconstruct_14_T1, Deconstruct_14_T2, Deconstruct_14_T3, Deconstruct_14_T4, Deconstruct_14_T5, Deconstruct_14_T6, Deconstruct_14_T7, Tuple_7[Deconstruct_14_T8, Deconstruct_14_T9, Deconstruct_14_T10, Deconstruct_14_T11, Deconstruct_14_T12, Deconstruct_14_T13, Deconstruct_14_T14]], item1: clr.Reference[Deconstruct_14_T1], item2: clr.Reference[Deconstruct_14_T2], item3: clr.Reference[Deconstruct_14_T3], item4: clr.Reference[Deconstruct_14_T4], item5: clr.Reference[Deconstruct_14_T5], item6: clr.Reference[Deconstruct_14_T6], item7: clr.Reference[Deconstruct_14_T7], item8: clr.Reference[Deconstruct_14_T8], item9: clr.Reference[Deconstruct_14_T9], item10: clr.Reference[Deconstruct_14_T10], item11: clr.Reference[Deconstruct_14_T11], item12: clr.Reference[Deconstruct_14_T12], item13: clr.Reference[Deconstruct_14_T13], item14: clr.Reference[Deconstruct_14_T14]) -> None:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Deconstruct_15_T1], typing.Type[Deconstruct_15_T2], typing.Type[Deconstruct_15_T3], typing.Type[Deconstruct_15_T4], typing.Type[Deconstruct_15_T5], typing.Type[Deconstruct_15_T6], typing.Type[Deconstruct_15_T7], typing.Type[Deconstruct_15_T8], typing.Type[Deconstruct_15_T9], typing.Type[Deconstruct_15_T10], typing.Type[Deconstruct_15_T11], typing.Type[Deconstruct_15_T12], typing.Type[Deconstruct_15_T13], typing.Type[Deconstruct_15_T14], typing.Type[Deconstruct_15_T15]]) -> Deconstruct_15[Deconstruct_15_T1, Deconstruct_15_T2, Deconstruct_15_T3, Deconstruct_15_T4, Deconstruct_15_T5, Deconstruct_15_T6, Deconstruct_15_T7, Deconstruct_15_T8, Deconstruct_15_T9, Deconstruct_15_T10, Deconstruct_15_T11, Deconstruct_15_T12, Deconstruct_15_T13, Deconstruct_15_T14, Deconstruct_15_T15]: ...

        Deconstruct_15_T1 = typing.TypeVar('Deconstruct_15_T1')
        Deconstruct_15_T2 = typing.TypeVar('Deconstruct_15_T2')
        Deconstruct_15_T3 = typing.TypeVar('Deconstruct_15_T3')
        Deconstruct_15_T4 = typing.TypeVar('Deconstruct_15_T4')
        Deconstruct_15_T5 = typing.TypeVar('Deconstruct_15_T5')
        Deconstruct_15_T6 = typing.TypeVar('Deconstruct_15_T6')
        Deconstruct_15_T7 = typing.TypeVar('Deconstruct_15_T7')
        Deconstruct_15_T8 = typing.TypeVar('Deconstruct_15_T8')
        Deconstruct_15_T9 = typing.TypeVar('Deconstruct_15_T9')
        Deconstruct_15_T10 = typing.TypeVar('Deconstruct_15_T10')
        Deconstruct_15_T11 = typing.TypeVar('Deconstruct_15_T11')
        Deconstruct_15_T12 = typing.TypeVar('Deconstruct_15_T12')
        Deconstruct_15_T13 = typing.TypeVar('Deconstruct_15_T13')
        Deconstruct_15_T14 = typing.TypeVar('Deconstruct_15_T14')
        Deconstruct_15_T15 = typing.TypeVar('Deconstruct_15_T15')
        class Deconstruct_15(typing.Generic[Deconstruct_15_T1, Deconstruct_15_T2, Deconstruct_15_T3, Deconstruct_15_T4, Deconstruct_15_T5, Deconstruct_15_T6, Deconstruct_15_T7, Deconstruct_15_T8, Deconstruct_15_T9, Deconstruct_15_T10, Deconstruct_15_T11, Deconstruct_15_T12, Deconstruct_15_T13, Deconstruct_15_T14, Deconstruct_15_T15]):
            Deconstruct_15_T1 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_15_T1
            Deconstruct_15_T2 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_15_T2
            Deconstruct_15_T3 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_15_T3
            Deconstruct_15_T4 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_15_T4
            Deconstruct_15_T5 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_15_T5
            Deconstruct_15_T6 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_15_T6
            Deconstruct_15_T7 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_15_T7
            Deconstruct_15_T8 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_15_T8
            Deconstruct_15_T9 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_15_T9
            Deconstruct_15_T10 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_15_T10
            Deconstruct_15_T11 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_15_T11
            Deconstruct_15_T12 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_15_T12
            Deconstruct_15_T13 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_15_T13
            Deconstruct_15_T14 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_15_T14
            Deconstruct_15_T15 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_15_T15
            def __call__(self, value: Tuple_8[Deconstruct_15_T1, Deconstruct_15_T2, Deconstruct_15_T3, Deconstruct_15_T4, Deconstruct_15_T5, Deconstruct_15_T6, Deconstruct_15_T7, Tuple_8[Deconstruct_15_T8, Deconstruct_15_T9, Deconstruct_15_T10, Deconstruct_15_T11, Deconstruct_15_T12, Deconstruct_15_T13, Deconstruct_15_T14, Tuple_1[Deconstruct_15_T15]]], item1: clr.Reference[Deconstruct_15_T1], item2: clr.Reference[Deconstruct_15_T2], item3: clr.Reference[Deconstruct_15_T3], item4: clr.Reference[Deconstruct_15_T4], item5: clr.Reference[Deconstruct_15_T5], item6: clr.Reference[Deconstruct_15_T6], item7: clr.Reference[Deconstruct_15_T7], item8: clr.Reference[Deconstruct_15_T8], item9: clr.Reference[Deconstruct_15_T9], item10: clr.Reference[Deconstruct_15_T10], item11: clr.Reference[Deconstruct_15_T11], item12: clr.Reference[Deconstruct_15_T12], item13: clr.Reference[Deconstruct_15_T13], item14: clr.Reference[Deconstruct_15_T14], item15: clr.Reference[Deconstruct_15_T15]) -> None:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Deconstruct_16_T1], typing.Type[Deconstruct_16_T2], typing.Type[Deconstruct_16_T3], typing.Type[Deconstruct_16_T4], typing.Type[Deconstruct_16_T5], typing.Type[Deconstruct_16_T6], typing.Type[Deconstruct_16_T7], typing.Type[Deconstruct_16_T8], typing.Type[Deconstruct_16_T9], typing.Type[Deconstruct_16_T10], typing.Type[Deconstruct_16_T11], typing.Type[Deconstruct_16_T12], typing.Type[Deconstruct_16_T13], typing.Type[Deconstruct_16_T14], typing.Type[Deconstruct_16_T15], typing.Type[Deconstruct_16_T16]]) -> Deconstruct_16[Deconstruct_16_T1, Deconstruct_16_T2, Deconstruct_16_T3, Deconstruct_16_T4, Deconstruct_16_T5, Deconstruct_16_T6, Deconstruct_16_T7, Deconstruct_16_T8, Deconstruct_16_T9, Deconstruct_16_T10, Deconstruct_16_T11, Deconstruct_16_T12, Deconstruct_16_T13, Deconstruct_16_T14, Deconstruct_16_T15, Deconstruct_16_T16]: ...

        Deconstruct_16_T1 = typing.TypeVar('Deconstruct_16_T1')
        Deconstruct_16_T2 = typing.TypeVar('Deconstruct_16_T2')
        Deconstruct_16_T3 = typing.TypeVar('Deconstruct_16_T3')
        Deconstruct_16_T4 = typing.TypeVar('Deconstruct_16_T4')
        Deconstruct_16_T5 = typing.TypeVar('Deconstruct_16_T5')
        Deconstruct_16_T6 = typing.TypeVar('Deconstruct_16_T6')
        Deconstruct_16_T7 = typing.TypeVar('Deconstruct_16_T7')
        Deconstruct_16_T8 = typing.TypeVar('Deconstruct_16_T8')
        Deconstruct_16_T9 = typing.TypeVar('Deconstruct_16_T9')
        Deconstruct_16_T10 = typing.TypeVar('Deconstruct_16_T10')
        Deconstruct_16_T11 = typing.TypeVar('Deconstruct_16_T11')
        Deconstruct_16_T12 = typing.TypeVar('Deconstruct_16_T12')
        Deconstruct_16_T13 = typing.TypeVar('Deconstruct_16_T13')
        Deconstruct_16_T14 = typing.TypeVar('Deconstruct_16_T14')
        Deconstruct_16_T15 = typing.TypeVar('Deconstruct_16_T15')
        Deconstruct_16_T16 = typing.TypeVar('Deconstruct_16_T16')
        class Deconstruct_16(typing.Generic[Deconstruct_16_T1, Deconstruct_16_T2, Deconstruct_16_T3, Deconstruct_16_T4, Deconstruct_16_T5, Deconstruct_16_T6, Deconstruct_16_T7, Deconstruct_16_T8, Deconstruct_16_T9, Deconstruct_16_T10, Deconstruct_16_T11, Deconstruct_16_T12, Deconstruct_16_T13, Deconstruct_16_T14, Deconstruct_16_T15, Deconstruct_16_T16]):
            Deconstruct_16_T1 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_16_T1
            Deconstruct_16_T2 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_16_T2
            Deconstruct_16_T3 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_16_T3
            Deconstruct_16_T4 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_16_T4
            Deconstruct_16_T5 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_16_T5
            Deconstruct_16_T6 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_16_T6
            Deconstruct_16_T7 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_16_T7
            Deconstruct_16_T8 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_16_T8
            Deconstruct_16_T9 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_16_T9
            Deconstruct_16_T10 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_16_T10
            Deconstruct_16_T11 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_16_T11
            Deconstruct_16_T12 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_16_T12
            Deconstruct_16_T13 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_16_T13
            Deconstruct_16_T14 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_16_T14
            Deconstruct_16_T15 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_16_T15
            Deconstruct_16_T16 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_16_T16
            def __call__(self, value: Tuple_8[Deconstruct_16_T1, Deconstruct_16_T2, Deconstruct_16_T3, Deconstruct_16_T4, Deconstruct_16_T5, Deconstruct_16_T6, Deconstruct_16_T7, Tuple_8[Deconstruct_16_T8, Deconstruct_16_T9, Deconstruct_16_T10, Deconstruct_16_T11, Deconstruct_16_T12, Deconstruct_16_T13, Deconstruct_16_T14, Tuple_2[Deconstruct_16_T15, Deconstruct_16_T16]]], item1: clr.Reference[Deconstruct_16_T1], item2: clr.Reference[Deconstruct_16_T2], item3: clr.Reference[Deconstruct_16_T3], item4: clr.Reference[Deconstruct_16_T4], item5: clr.Reference[Deconstruct_16_T5], item6: clr.Reference[Deconstruct_16_T6], item7: clr.Reference[Deconstruct_16_T7], item8: clr.Reference[Deconstruct_16_T8], item9: clr.Reference[Deconstruct_16_T9], item10: clr.Reference[Deconstruct_16_T10], item11: clr.Reference[Deconstruct_16_T11], item12: clr.Reference[Deconstruct_16_T12], item13: clr.Reference[Deconstruct_16_T13], item14: clr.Reference[Deconstruct_16_T14], item15: clr.Reference[Deconstruct_16_T15], item16: clr.Reference[Deconstruct_16_T16]) -> None:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Deconstruct_17_T1], typing.Type[Deconstruct_17_T2], typing.Type[Deconstruct_17_T3], typing.Type[Deconstruct_17_T4], typing.Type[Deconstruct_17_T5], typing.Type[Deconstruct_17_T6], typing.Type[Deconstruct_17_T7], typing.Type[Deconstruct_17_T8], typing.Type[Deconstruct_17_T9], typing.Type[Deconstruct_17_T10], typing.Type[Deconstruct_17_T11], typing.Type[Deconstruct_17_T12], typing.Type[Deconstruct_17_T13], typing.Type[Deconstruct_17_T14], typing.Type[Deconstruct_17_T15], typing.Type[Deconstruct_17_T16], typing.Type[Deconstruct_17_T17]]) -> Deconstruct_17[Deconstruct_17_T1, Deconstruct_17_T2, Deconstruct_17_T3, Deconstruct_17_T4, Deconstruct_17_T5, Deconstruct_17_T6, Deconstruct_17_T7, Deconstruct_17_T8, Deconstruct_17_T9, Deconstruct_17_T10, Deconstruct_17_T11, Deconstruct_17_T12, Deconstruct_17_T13, Deconstruct_17_T14, Deconstruct_17_T15, Deconstruct_17_T16, Deconstruct_17_T17]: ...

        Deconstruct_17_T1 = typing.TypeVar('Deconstruct_17_T1')
        Deconstruct_17_T2 = typing.TypeVar('Deconstruct_17_T2')
        Deconstruct_17_T3 = typing.TypeVar('Deconstruct_17_T3')
        Deconstruct_17_T4 = typing.TypeVar('Deconstruct_17_T4')
        Deconstruct_17_T5 = typing.TypeVar('Deconstruct_17_T5')
        Deconstruct_17_T6 = typing.TypeVar('Deconstruct_17_T6')
        Deconstruct_17_T7 = typing.TypeVar('Deconstruct_17_T7')
        Deconstruct_17_T8 = typing.TypeVar('Deconstruct_17_T8')
        Deconstruct_17_T9 = typing.TypeVar('Deconstruct_17_T9')
        Deconstruct_17_T10 = typing.TypeVar('Deconstruct_17_T10')
        Deconstruct_17_T11 = typing.TypeVar('Deconstruct_17_T11')
        Deconstruct_17_T12 = typing.TypeVar('Deconstruct_17_T12')
        Deconstruct_17_T13 = typing.TypeVar('Deconstruct_17_T13')
        Deconstruct_17_T14 = typing.TypeVar('Deconstruct_17_T14')
        Deconstruct_17_T15 = typing.TypeVar('Deconstruct_17_T15')
        Deconstruct_17_T16 = typing.TypeVar('Deconstruct_17_T16')
        Deconstruct_17_T17 = typing.TypeVar('Deconstruct_17_T17')
        class Deconstruct_17(typing.Generic[Deconstruct_17_T1, Deconstruct_17_T2, Deconstruct_17_T3, Deconstruct_17_T4, Deconstruct_17_T5, Deconstruct_17_T6, Deconstruct_17_T7, Deconstruct_17_T8, Deconstruct_17_T9, Deconstruct_17_T10, Deconstruct_17_T11, Deconstruct_17_T12, Deconstruct_17_T13, Deconstruct_17_T14, Deconstruct_17_T15, Deconstruct_17_T16, Deconstruct_17_T17]):
            Deconstruct_17_T1 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_17_T1
            Deconstruct_17_T2 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_17_T2
            Deconstruct_17_T3 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_17_T3
            Deconstruct_17_T4 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_17_T4
            Deconstruct_17_T5 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_17_T5
            Deconstruct_17_T6 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_17_T6
            Deconstruct_17_T7 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_17_T7
            Deconstruct_17_T8 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_17_T8
            Deconstruct_17_T9 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_17_T9
            Deconstruct_17_T10 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_17_T10
            Deconstruct_17_T11 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_17_T11
            Deconstruct_17_T12 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_17_T12
            Deconstruct_17_T13 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_17_T13
            Deconstruct_17_T14 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_17_T14
            Deconstruct_17_T15 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_17_T15
            Deconstruct_17_T16 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_17_T16
            Deconstruct_17_T17 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_17_T17
            def __call__(self, value: Tuple_8[Deconstruct_17_T1, Deconstruct_17_T2, Deconstruct_17_T3, Deconstruct_17_T4, Deconstruct_17_T5, Deconstruct_17_T6, Deconstruct_17_T7, Tuple_8[Deconstruct_17_T8, Deconstruct_17_T9, Deconstruct_17_T10, Deconstruct_17_T11, Deconstruct_17_T12, Deconstruct_17_T13, Deconstruct_17_T14, Tuple_3[Deconstruct_17_T15, Deconstruct_17_T16, Deconstruct_17_T17]]], item1: clr.Reference[Deconstruct_17_T1], item2: clr.Reference[Deconstruct_17_T2], item3: clr.Reference[Deconstruct_17_T3], item4: clr.Reference[Deconstruct_17_T4], item5: clr.Reference[Deconstruct_17_T5], item6: clr.Reference[Deconstruct_17_T6], item7: clr.Reference[Deconstruct_17_T7], item8: clr.Reference[Deconstruct_17_T8], item9: clr.Reference[Deconstruct_17_T9], item10: clr.Reference[Deconstruct_17_T10], item11: clr.Reference[Deconstruct_17_T11], item12: clr.Reference[Deconstruct_17_T12], item13: clr.Reference[Deconstruct_17_T13], item14: clr.Reference[Deconstruct_17_T14], item15: clr.Reference[Deconstruct_17_T15], item16: clr.Reference[Deconstruct_17_T16], item17: clr.Reference[Deconstruct_17_T17]) -> None:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Deconstruct_18_T1], typing.Type[Deconstruct_18_T2], typing.Type[Deconstruct_18_T3], typing.Type[Deconstruct_18_T4], typing.Type[Deconstruct_18_T5], typing.Type[Deconstruct_18_T6], typing.Type[Deconstruct_18_T7], typing.Type[Deconstruct_18_T8], typing.Type[Deconstruct_18_T9], typing.Type[Deconstruct_18_T10], typing.Type[Deconstruct_18_T11], typing.Type[Deconstruct_18_T12], typing.Type[Deconstruct_18_T13], typing.Type[Deconstruct_18_T14], typing.Type[Deconstruct_18_T15], typing.Type[Deconstruct_18_T16], typing.Type[Deconstruct_18_T17], typing.Type[Deconstruct_18_T18]]) -> Deconstruct_18[Deconstruct_18_T1, Deconstruct_18_T2, Deconstruct_18_T3, Deconstruct_18_T4, Deconstruct_18_T5, Deconstruct_18_T6, Deconstruct_18_T7, Deconstruct_18_T8, Deconstruct_18_T9, Deconstruct_18_T10, Deconstruct_18_T11, Deconstruct_18_T12, Deconstruct_18_T13, Deconstruct_18_T14, Deconstruct_18_T15, Deconstruct_18_T16, Deconstruct_18_T17, Deconstruct_18_T18]: ...

        Deconstruct_18_T1 = typing.TypeVar('Deconstruct_18_T1')
        Deconstruct_18_T2 = typing.TypeVar('Deconstruct_18_T2')
        Deconstruct_18_T3 = typing.TypeVar('Deconstruct_18_T3')
        Deconstruct_18_T4 = typing.TypeVar('Deconstruct_18_T4')
        Deconstruct_18_T5 = typing.TypeVar('Deconstruct_18_T5')
        Deconstruct_18_T6 = typing.TypeVar('Deconstruct_18_T6')
        Deconstruct_18_T7 = typing.TypeVar('Deconstruct_18_T7')
        Deconstruct_18_T8 = typing.TypeVar('Deconstruct_18_T8')
        Deconstruct_18_T9 = typing.TypeVar('Deconstruct_18_T9')
        Deconstruct_18_T10 = typing.TypeVar('Deconstruct_18_T10')
        Deconstruct_18_T11 = typing.TypeVar('Deconstruct_18_T11')
        Deconstruct_18_T12 = typing.TypeVar('Deconstruct_18_T12')
        Deconstruct_18_T13 = typing.TypeVar('Deconstruct_18_T13')
        Deconstruct_18_T14 = typing.TypeVar('Deconstruct_18_T14')
        Deconstruct_18_T15 = typing.TypeVar('Deconstruct_18_T15')
        Deconstruct_18_T16 = typing.TypeVar('Deconstruct_18_T16')
        Deconstruct_18_T17 = typing.TypeVar('Deconstruct_18_T17')
        Deconstruct_18_T18 = typing.TypeVar('Deconstruct_18_T18')
        class Deconstruct_18(typing.Generic[Deconstruct_18_T1, Deconstruct_18_T2, Deconstruct_18_T3, Deconstruct_18_T4, Deconstruct_18_T5, Deconstruct_18_T6, Deconstruct_18_T7, Deconstruct_18_T8, Deconstruct_18_T9, Deconstruct_18_T10, Deconstruct_18_T11, Deconstruct_18_T12, Deconstruct_18_T13, Deconstruct_18_T14, Deconstruct_18_T15, Deconstruct_18_T16, Deconstruct_18_T17, Deconstruct_18_T18]):
            Deconstruct_18_T1 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_18_T1
            Deconstruct_18_T2 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_18_T2
            Deconstruct_18_T3 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_18_T3
            Deconstruct_18_T4 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_18_T4
            Deconstruct_18_T5 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_18_T5
            Deconstruct_18_T6 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_18_T6
            Deconstruct_18_T7 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_18_T7
            Deconstruct_18_T8 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_18_T8
            Deconstruct_18_T9 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_18_T9
            Deconstruct_18_T10 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_18_T10
            Deconstruct_18_T11 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_18_T11
            Deconstruct_18_T12 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_18_T12
            Deconstruct_18_T13 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_18_T13
            Deconstruct_18_T14 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_18_T14
            Deconstruct_18_T15 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_18_T15
            Deconstruct_18_T16 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_18_T16
            Deconstruct_18_T17 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_18_T17
            Deconstruct_18_T18 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_18_T18
            def __call__(self, value: Tuple_8[Deconstruct_18_T1, Deconstruct_18_T2, Deconstruct_18_T3, Deconstruct_18_T4, Deconstruct_18_T5, Deconstruct_18_T6, Deconstruct_18_T7, Tuple_8[Deconstruct_18_T8, Deconstruct_18_T9, Deconstruct_18_T10, Deconstruct_18_T11, Deconstruct_18_T12, Deconstruct_18_T13, Deconstruct_18_T14, Tuple_4[Deconstruct_18_T15, Deconstruct_18_T16, Deconstruct_18_T17, Deconstruct_18_T18]]], item1: clr.Reference[Deconstruct_18_T1], item2: clr.Reference[Deconstruct_18_T2], item3: clr.Reference[Deconstruct_18_T3], item4: clr.Reference[Deconstruct_18_T4], item5: clr.Reference[Deconstruct_18_T5], item6: clr.Reference[Deconstruct_18_T6], item7: clr.Reference[Deconstruct_18_T7], item8: clr.Reference[Deconstruct_18_T8], item9: clr.Reference[Deconstruct_18_T9], item10: clr.Reference[Deconstruct_18_T10], item11: clr.Reference[Deconstruct_18_T11], item12: clr.Reference[Deconstruct_18_T12], item13: clr.Reference[Deconstruct_18_T13], item14: clr.Reference[Deconstruct_18_T14], item15: clr.Reference[Deconstruct_18_T15], item16: clr.Reference[Deconstruct_18_T16], item17: clr.Reference[Deconstruct_18_T17], item18: clr.Reference[Deconstruct_18_T18]) -> None:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Deconstruct_19_T1], typing.Type[Deconstruct_19_T2], typing.Type[Deconstruct_19_T3], typing.Type[Deconstruct_19_T4], typing.Type[Deconstruct_19_T5], typing.Type[Deconstruct_19_T6], typing.Type[Deconstruct_19_T7], typing.Type[Deconstruct_19_T8], typing.Type[Deconstruct_19_T9], typing.Type[Deconstruct_19_T10], typing.Type[Deconstruct_19_T11], typing.Type[Deconstruct_19_T12], typing.Type[Deconstruct_19_T13], typing.Type[Deconstruct_19_T14], typing.Type[Deconstruct_19_T15], typing.Type[Deconstruct_19_T16], typing.Type[Deconstruct_19_T17], typing.Type[Deconstruct_19_T18], typing.Type[Deconstruct_19_T19]]) -> Deconstruct_19[Deconstruct_19_T1, Deconstruct_19_T2, Deconstruct_19_T3, Deconstruct_19_T4, Deconstruct_19_T5, Deconstruct_19_T6, Deconstruct_19_T7, Deconstruct_19_T8, Deconstruct_19_T9, Deconstruct_19_T10, Deconstruct_19_T11, Deconstruct_19_T12, Deconstruct_19_T13, Deconstruct_19_T14, Deconstruct_19_T15, Deconstruct_19_T16, Deconstruct_19_T17, Deconstruct_19_T18, Deconstruct_19_T19]: ...

        Deconstruct_19_T1 = typing.TypeVar('Deconstruct_19_T1')
        Deconstruct_19_T2 = typing.TypeVar('Deconstruct_19_T2')
        Deconstruct_19_T3 = typing.TypeVar('Deconstruct_19_T3')
        Deconstruct_19_T4 = typing.TypeVar('Deconstruct_19_T4')
        Deconstruct_19_T5 = typing.TypeVar('Deconstruct_19_T5')
        Deconstruct_19_T6 = typing.TypeVar('Deconstruct_19_T6')
        Deconstruct_19_T7 = typing.TypeVar('Deconstruct_19_T7')
        Deconstruct_19_T8 = typing.TypeVar('Deconstruct_19_T8')
        Deconstruct_19_T9 = typing.TypeVar('Deconstruct_19_T9')
        Deconstruct_19_T10 = typing.TypeVar('Deconstruct_19_T10')
        Deconstruct_19_T11 = typing.TypeVar('Deconstruct_19_T11')
        Deconstruct_19_T12 = typing.TypeVar('Deconstruct_19_T12')
        Deconstruct_19_T13 = typing.TypeVar('Deconstruct_19_T13')
        Deconstruct_19_T14 = typing.TypeVar('Deconstruct_19_T14')
        Deconstruct_19_T15 = typing.TypeVar('Deconstruct_19_T15')
        Deconstruct_19_T16 = typing.TypeVar('Deconstruct_19_T16')
        Deconstruct_19_T17 = typing.TypeVar('Deconstruct_19_T17')
        Deconstruct_19_T18 = typing.TypeVar('Deconstruct_19_T18')
        Deconstruct_19_T19 = typing.TypeVar('Deconstruct_19_T19')
        class Deconstruct_19(typing.Generic[Deconstruct_19_T1, Deconstruct_19_T2, Deconstruct_19_T3, Deconstruct_19_T4, Deconstruct_19_T5, Deconstruct_19_T6, Deconstruct_19_T7, Deconstruct_19_T8, Deconstruct_19_T9, Deconstruct_19_T10, Deconstruct_19_T11, Deconstruct_19_T12, Deconstruct_19_T13, Deconstruct_19_T14, Deconstruct_19_T15, Deconstruct_19_T16, Deconstruct_19_T17, Deconstruct_19_T18, Deconstruct_19_T19]):
            Deconstruct_19_T1 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_19_T1
            Deconstruct_19_T2 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_19_T2
            Deconstruct_19_T3 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_19_T3
            Deconstruct_19_T4 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_19_T4
            Deconstruct_19_T5 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_19_T5
            Deconstruct_19_T6 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_19_T6
            Deconstruct_19_T7 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_19_T7
            Deconstruct_19_T8 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_19_T8
            Deconstruct_19_T9 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_19_T9
            Deconstruct_19_T10 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_19_T10
            Deconstruct_19_T11 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_19_T11
            Deconstruct_19_T12 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_19_T12
            Deconstruct_19_T13 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_19_T13
            Deconstruct_19_T14 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_19_T14
            Deconstruct_19_T15 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_19_T15
            Deconstruct_19_T16 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_19_T16
            Deconstruct_19_T17 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_19_T17
            Deconstruct_19_T18 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_19_T18
            Deconstruct_19_T19 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_19_T19
            def __call__(self, value: Tuple_8[Deconstruct_19_T1, Deconstruct_19_T2, Deconstruct_19_T3, Deconstruct_19_T4, Deconstruct_19_T5, Deconstruct_19_T6, Deconstruct_19_T7, Tuple_8[Deconstruct_19_T8, Deconstruct_19_T9, Deconstruct_19_T10, Deconstruct_19_T11, Deconstruct_19_T12, Deconstruct_19_T13, Deconstruct_19_T14, Tuple_5[Deconstruct_19_T15, Deconstruct_19_T16, Deconstruct_19_T17, Deconstruct_19_T18, Deconstruct_19_T19]]], item1: clr.Reference[Deconstruct_19_T1], item2: clr.Reference[Deconstruct_19_T2], item3: clr.Reference[Deconstruct_19_T3], item4: clr.Reference[Deconstruct_19_T4], item5: clr.Reference[Deconstruct_19_T5], item6: clr.Reference[Deconstruct_19_T6], item7: clr.Reference[Deconstruct_19_T7], item8: clr.Reference[Deconstruct_19_T8], item9: clr.Reference[Deconstruct_19_T9], item10: clr.Reference[Deconstruct_19_T10], item11: clr.Reference[Deconstruct_19_T11], item12: clr.Reference[Deconstruct_19_T12], item13: clr.Reference[Deconstruct_19_T13], item14: clr.Reference[Deconstruct_19_T14], item15: clr.Reference[Deconstruct_19_T15], item16: clr.Reference[Deconstruct_19_T16], item17: clr.Reference[Deconstruct_19_T17], item18: clr.Reference[Deconstruct_19_T18], item19: clr.Reference[Deconstruct_19_T19]) -> None:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Deconstruct_20_T1], typing.Type[Deconstruct_20_T2], typing.Type[Deconstruct_20_T3], typing.Type[Deconstruct_20_T4], typing.Type[Deconstruct_20_T5], typing.Type[Deconstruct_20_T6], typing.Type[Deconstruct_20_T7], typing.Type[Deconstruct_20_T8], typing.Type[Deconstruct_20_T9], typing.Type[Deconstruct_20_T10], typing.Type[Deconstruct_20_T11], typing.Type[Deconstruct_20_T12], typing.Type[Deconstruct_20_T13], typing.Type[Deconstruct_20_T14], typing.Type[Deconstruct_20_T15], typing.Type[Deconstruct_20_T16], typing.Type[Deconstruct_20_T17], typing.Type[Deconstruct_20_T18], typing.Type[Deconstruct_20_T19], typing.Type[Deconstruct_20_T20]]) -> Deconstruct_20[Deconstruct_20_T1, Deconstruct_20_T2, Deconstruct_20_T3, Deconstruct_20_T4, Deconstruct_20_T5, Deconstruct_20_T6, Deconstruct_20_T7, Deconstruct_20_T8, Deconstruct_20_T9, Deconstruct_20_T10, Deconstruct_20_T11, Deconstruct_20_T12, Deconstruct_20_T13, Deconstruct_20_T14, Deconstruct_20_T15, Deconstruct_20_T16, Deconstruct_20_T17, Deconstruct_20_T18, Deconstruct_20_T19, Deconstruct_20_T20]: ...

        Deconstruct_20_T1 = typing.TypeVar('Deconstruct_20_T1')
        Deconstruct_20_T2 = typing.TypeVar('Deconstruct_20_T2')
        Deconstruct_20_T3 = typing.TypeVar('Deconstruct_20_T3')
        Deconstruct_20_T4 = typing.TypeVar('Deconstruct_20_T4')
        Deconstruct_20_T5 = typing.TypeVar('Deconstruct_20_T5')
        Deconstruct_20_T6 = typing.TypeVar('Deconstruct_20_T6')
        Deconstruct_20_T7 = typing.TypeVar('Deconstruct_20_T7')
        Deconstruct_20_T8 = typing.TypeVar('Deconstruct_20_T8')
        Deconstruct_20_T9 = typing.TypeVar('Deconstruct_20_T9')
        Deconstruct_20_T10 = typing.TypeVar('Deconstruct_20_T10')
        Deconstruct_20_T11 = typing.TypeVar('Deconstruct_20_T11')
        Deconstruct_20_T12 = typing.TypeVar('Deconstruct_20_T12')
        Deconstruct_20_T13 = typing.TypeVar('Deconstruct_20_T13')
        Deconstruct_20_T14 = typing.TypeVar('Deconstruct_20_T14')
        Deconstruct_20_T15 = typing.TypeVar('Deconstruct_20_T15')
        Deconstruct_20_T16 = typing.TypeVar('Deconstruct_20_T16')
        Deconstruct_20_T17 = typing.TypeVar('Deconstruct_20_T17')
        Deconstruct_20_T18 = typing.TypeVar('Deconstruct_20_T18')
        Deconstruct_20_T19 = typing.TypeVar('Deconstruct_20_T19')
        Deconstruct_20_T20 = typing.TypeVar('Deconstruct_20_T20')
        class Deconstruct_20(typing.Generic[Deconstruct_20_T1, Deconstruct_20_T2, Deconstruct_20_T3, Deconstruct_20_T4, Deconstruct_20_T5, Deconstruct_20_T6, Deconstruct_20_T7, Deconstruct_20_T8, Deconstruct_20_T9, Deconstruct_20_T10, Deconstruct_20_T11, Deconstruct_20_T12, Deconstruct_20_T13, Deconstruct_20_T14, Deconstruct_20_T15, Deconstruct_20_T16, Deconstruct_20_T17, Deconstruct_20_T18, Deconstruct_20_T19, Deconstruct_20_T20]):
            Deconstruct_20_T1 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_20_T1
            Deconstruct_20_T2 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_20_T2
            Deconstruct_20_T3 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_20_T3
            Deconstruct_20_T4 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_20_T4
            Deconstruct_20_T5 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_20_T5
            Deconstruct_20_T6 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_20_T6
            Deconstruct_20_T7 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_20_T7
            Deconstruct_20_T8 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_20_T8
            Deconstruct_20_T9 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_20_T9
            Deconstruct_20_T10 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_20_T10
            Deconstruct_20_T11 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_20_T11
            Deconstruct_20_T12 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_20_T12
            Deconstruct_20_T13 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_20_T13
            Deconstruct_20_T14 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_20_T14
            Deconstruct_20_T15 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_20_T15
            Deconstruct_20_T16 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_20_T16
            Deconstruct_20_T17 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_20_T17
            Deconstruct_20_T18 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_20_T18
            Deconstruct_20_T19 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_20_T19
            Deconstruct_20_T20 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_20_T20
            def __call__(self, value: Tuple_8[Deconstruct_20_T1, Deconstruct_20_T2, Deconstruct_20_T3, Deconstruct_20_T4, Deconstruct_20_T5, Deconstruct_20_T6, Deconstruct_20_T7, Tuple_8[Deconstruct_20_T8, Deconstruct_20_T9, Deconstruct_20_T10, Deconstruct_20_T11, Deconstruct_20_T12, Deconstruct_20_T13, Deconstruct_20_T14, Tuple_6[Deconstruct_20_T15, Deconstruct_20_T16, Deconstruct_20_T17, Deconstruct_20_T18, Deconstruct_20_T19, Deconstruct_20_T20]]], item1: clr.Reference[Deconstruct_20_T1], item2: clr.Reference[Deconstruct_20_T2], item3: clr.Reference[Deconstruct_20_T3], item4: clr.Reference[Deconstruct_20_T4], item5: clr.Reference[Deconstruct_20_T5], item6: clr.Reference[Deconstruct_20_T6], item7: clr.Reference[Deconstruct_20_T7], item8: clr.Reference[Deconstruct_20_T8], item9: clr.Reference[Deconstruct_20_T9], item10: clr.Reference[Deconstruct_20_T10], item11: clr.Reference[Deconstruct_20_T11], item12: clr.Reference[Deconstruct_20_T12], item13: clr.Reference[Deconstruct_20_T13], item14: clr.Reference[Deconstruct_20_T14], item15: clr.Reference[Deconstruct_20_T15], item16: clr.Reference[Deconstruct_20_T16], item17: clr.Reference[Deconstruct_20_T17], item18: clr.Reference[Deconstruct_20_T18], item19: clr.Reference[Deconstruct_20_T19], item20: clr.Reference[Deconstruct_20_T20]) -> None:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Deconstruct_21_T1], typing.Type[Deconstruct_21_T2], typing.Type[Deconstruct_21_T3], typing.Type[Deconstruct_21_T4], typing.Type[Deconstruct_21_T5], typing.Type[Deconstruct_21_T6], typing.Type[Deconstruct_21_T7], typing.Type[Deconstruct_21_T8], typing.Type[Deconstruct_21_T9], typing.Type[Deconstruct_21_T10], typing.Type[Deconstruct_21_T11], typing.Type[Deconstruct_21_T12], typing.Type[Deconstruct_21_T13], typing.Type[Deconstruct_21_T14], typing.Type[Deconstruct_21_T15], typing.Type[Deconstruct_21_T16], typing.Type[Deconstruct_21_T17], typing.Type[Deconstruct_21_T18], typing.Type[Deconstruct_21_T19], typing.Type[Deconstruct_21_T20], typing.Type[Deconstruct_21_T21]]) -> Deconstruct_21[Deconstruct_21_T1, Deconstruct_21_T2, Deconstruct_21_T3, Deconstruct_21_T4, Deconstruct_21_T5, Deconstruct_21_T6, Deconstruct_21_T7, Deconstruct_21_T8, Deconstruct_21_T9, Deconstruct_21_T10, Deconstruct_21_T11, Deconstruct_21_T12, Deconstruct_21_T13, Deconstruct_21_T14, Deconstruct_21_T15, Deconstruct_21_T16, Deconstruct_21_T17, Deconstruct_21_T18, Deconstruct_21_T19, Deconstruct_21_T20, Deconstruct_21_T21]: ...

        Deconstruct_21_T1 = typing.TypeVar('Deconstruct_21_T1')
        Deconstruct_21_T2 = typing.TypeVar('Deconstruct_21_T2')
        Deconstruct_21_T3 = typing.TypeVar('Deconstruct_21_T3')
        Deconstruct_21_T4 = typing.TypeVar('Deconstruct_21_T4')
        Deconstruct_21_T5 = typing.TypeVar('Deconstruct_21_T5')
        Deconstruct_21_T6 = typing.TypeVar('Deconstruct_21_T6')
        Deconstruct_21_T7 = typing.TypeVar('Deconstruct_21_T7')
        Deconstruct_21_T8 = typing.TypeVar('Deconstruct_21_T8')
        Deconstruct_21_T9 = typing.TypeVar('Deconstruct_21_T9')
        Deconstruct_21_T10 = typing.TypeVar('Deconstruct_21_T10')
        Deconstruct_21_T11 = typing.TypeVar('Deconstruct_21_T11')
        Deconstruct_21_T12 = typing.TypeVar('Deconstruct_21_T12')
        Deconstruct_21_T13 = typing.TypeVar('Deconstruct_21_T13')
        Deconstruct_21_T14 = typing.TypeVar('Deconstruct_21_T14')
        Deconstruct_21_T15 = typing.TypeVar('Deconstruct_21_T15')
        Deconstruct_21_T16 = typing.TypeVar('Deconstruct_21_T16')
        Deconstruct_21_T17 = typing.TypeVar('Deconstruct_21_T17')
        Deconstruct_21_T18 = typing.TypeVar('Deconstruct_21_T18')
        Deconstruct_21_T19 = typing.TypeVar('Deconstruct_21_T19')
        Deconstruct_21_T20 = typing.TypeVar('Deconstruct_21_T20')
        Deconstruct_21_T21 = typing.TypeVar('Deconstruct_21_T21')
        class Deconstruct_21(typing.Generic[Deconstruct_21_T1, Deconstruct_21_T2, Deconstruct_21_T3, Deconstruct_21_T4, Deconstruct_21_T5, Deconstruct_21_T6, Deconstruct_21_T7, Deconstruct_21_T8, Deconstruct_21_T9, Deconstruct_21_T10, Deconstruct_21_T11, Deconstruct_21_T12, Deconstruct_21_T13, Deconstruct_21_T14, Deconstruct_21_T15, Deconstruct_21_T16, Deconstruct_21_T17, Deconstruct_21_T18, Deconstruct_21_T19, Deconstruct_21_T20, Deconstruct_21_T21]):
            Deconstruct_21_T1 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_21_T1
            Deconstruct_21_T2 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_21_T2
            Deconstruct_21_T3 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_21_T3
            Deconstruct_21_T4 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_21_T4
            Deconstruct_21_T5 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_21_T5
            Deconstruct_21_T6 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_21_T6
            Deconstruct_21_T7 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_21_T7
            Deconstruct_21_T8 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_21_T8
            Deconstruct_21_T9 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_21_T9
            Deconstruct_21_T10 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_21_T10
            Deconstruct_21_T11 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_21_T11
            Deconstruct_21_T12 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_21_T12
            Deconstruct_21_T13 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_21_T13
            Deconstruct_21_T14 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_21_T14
            Deconstruct_21_T15 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_21_T15
            Deconstruct_21_T16 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_21_T16
            Deconstruct_21_T17 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_21_T17
            Deconstruct_21_T18 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_21_T18
            Deconstruct_21_T19 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_21_T19
            Deconstruct_21_T20 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_21_T20
            Deconstruct_21_T21 = TupleExtensions.Deconstruct_MethodGroup.Deconstruct_21_T21
            def __call__(self, value: Tuple_8[Deconstruct_21_T1, Deconstruct_21_T2, Deconstruct_21_T3, Deconstruct_21_T4, Deconstruct_21_T5, Deconstruct_21_T6, Deconstruct_21_T7, Tuple_8[Deconstruct_21_T8, Deconstruct_21_T9, Deconstruct_21_T10, Deconstruct_21_T11, Deconstruct_21_T12, Deconstruct_21_T13, Deconstruct_21_T14, Tuple_7[Deconstruct_21_T15, Deconstruct_21_T16, Deconstruct_21_T17, Deconstruct_21_T18, Deconstruct_21_T19, Deconstruct_21_T20, Deconstruct_21_T21]]], item1: clr.Reference[Deconstruct_21_T1], item2: clr.Reference[Deconstruct_21_T2], item3: clr.Reference[Deconstruct_21_T3], item4: clr.Reference[Deconstruct_21_T4], item5: clr.Reference[Deconstruct_21_T5], item6: clr.Reference[Deconstruct_21_T6], item7: clr.Reference[Deconstruct_21_T7], item8: clr.Reference[Deconstruct_21_T8], item9: clr.Reference[Deconstruct_21_T9], item10: clr.Reference[Deconstruct_21_T10], item11: clr.Reference[Deconstruct_21_T11], item12: clr.Reference[Deconstruct_21_T12], item13: clr.Reference[Deconstruct_21_T13], item14: clr.Reference[Deconstruct_21_T14], item15: clr.Reference[Deconstruct_21_T15], item16: clr.Reference[Deconstruct_21_T16], item17: clr.Reference[Deconstruct_21_T17], item18: clr.Reference[Deconstruct_21_T18], item19: clr.Reference[Deconstruct_21_T19], item20: clr.Reference[Deconstruct_21_T20], item21: clr.Reference[Deconstruct_21_T21]) -> None:...


    # Skipped ToTuple due to it being static, abstract and generic.

    ToTuple : ToTuple_MethodGroup
    class ToTuple_MethodGroup:
        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[ToTuple_10_T1], typing.Type[ToTuple_10_T2], typing.Type[ToTuple_10_T3], typing.Type[ToTuple_10_T4], typing.Type[ToTuple_10_T5], typing.Type[ToTuple_10_T6], typing.Type[ToTuple_10_T7], typing.Type[ToTuple_10_T8], typing.Type[ToTuple_10_T9], typing.Type[ToTuple_10_T10]]) -> ToTuple_10[ToTuple_10_T1, ToTuple_10_T2, ToTuple_10_T3, ToTuple_10_T4, ToTuple_10_T5, ToTuple_10_T6, ToTuple_10_T7, ToTuple_10_T8, ToTuple_10_T9, ToTuple_10_T10]: ...

        ToTuple_10_T1 = typing.TypeVar('ToTuple_10_T1')
        ToTuple_10_T2 = typing.TypeVar('ToTuple_10_T2')
        ToTuple_10_T3 = typing.TypeVar('ToTuple_10_T3')
        ToTuple_10_T4 = typing.TypeVar('ToTuple_10_T4')
        ToTuple_10_T5 = typing.TypeVar('ToTuple_10_T5')
        ToTuple_10_T6 = typing.TypeVar('ToTuple_10_T6')
        ToTuple_10_T7 = typing.TypeVar('ToTuple_10_T7')
        ToTuple_10_T8 = typing.TypeVar('ToTuple_10_T8')
        ToTuple_10_T9 = typing.TypeVar('ToTuple_10_T9')
        ToTuple_10_T10 = typing.TypeVar('ToTuple_10_T10')
        class ToTuple_10(typing.Generic[ToTuple_10_T1, ToTuple_10_T2, ToTuple_10_T3, ToTuple_10_T4, ToTuple_10_T5, ToTuple_10_T6, ToTuple_10_T7, ToTuple_10_T8, ToTuple_10_T9, ToTuple_10_T10]):
            ToTuple_10_T1 = TupleExtensions.ToTuple_MethodGroup.ToTuple_10_T1
            ToTuple_10_T2 = TupleExtensions.ToTuple_MethodGroup.ToTuple_10_T2
            ToTuple_10_T3 = TupleExtensions.ToTuple_MethodGroup.ToTuple_10_T3
            ToTuple_10_T4 = TupleExtensions.ToTuple_MethodGroup.ToTuple_10_T4
            ToTuple_10_T5 = TupleExtensions.ToTuple_MethodGroup.ToTuple_10_T5
            ToTuple_10_T6 = TupleExtensions.ToTuple_MethodGroup.ToTuple_10_T6
            ToTuple_10_T7 = TupleExtensions.ToTuple_MethodGroup.ToTuple_10_T7
            ToTuple_10_T8 = TupleExtensions.ToTuple_MethodGroup.ToTuple_10_T8
            ToTuple_10_T9 = TupleExtensions.ToTuple_MethodGroup.ToTuple_10_T9
            ToTuple_10_T10 = TupleExtensions.ToTuple_MethodGroup.ToTuple_10_T10
            def __call__(self, value: ValueTuple_8[ToTuple_10_T1, ToTuple_10_T2, ToTuple_10_T3, ToTuple_10_T4, ToTuple_10_T5, ToTuple_10_T6, ToTuple_10_T7, ValueTuple_3[ToTuple_10_T8, ToTuple_10_T9, ToTuple_10_T10]]) -> Tuple_8[ToTuple_10_T1, ToTuple_10_T2, ToTuple_10_T3, ToTuple_10_T4, ToTuple_10_T5, ToTuple_10_T6, ToTuple_10_T7, Tuple_3[ToTuple_10_T8, ToTuple_10_T9, ToTuple_10_T10]]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[ToTuple_11_T1], typing.Type[ToTuple_11_T2], typing.Type[ToTuple_11_T3], typing.Type[ToTuple_11_T4], typing.Type[ToTuple_11_T5], typing.Type[ToTuple_11_T6], typing.Type[ToTuple_11_T7], typing.Type[ToTuple_11_T8], typing.Type[ToTuple_11_T9], typing.Type[ToTuple_11_T10], typing.Type[ToTuple_11_T11]]) -> ToTuple_11[ToTuple_11_T1, ToTuple_11_T2, ToTuple_11_T3, ToTuple_11_T4, ToTuple_11_T5, ToTuple_11_T6, ToTuple_11_T7, ToTuple_11_T8, ToTuple_11_T9, ToTuple_11_T10, ToTuple_11_T11]: ...

        ToTuple_11_T1 = typing.TypeVar('ToTuple_11_T1')
        ToTuple_11_T2 = typing.TypeVar('ToTuple_11_T2')
        ToTuple_11_T3 = typing.TypeVar('ToTuple_11_T3')
        ToTuple_11_T4 = typing.TypeVar('ToTuple_11_T4')
        ToTuple_11_T5 = typing.TypeVar('ToTuple_11_T5')
        ToTuple_11_T6 = typing.TypeVar('ToTuple_11_T6')
        ToTuple_11_T7 = typing.TypeVar('ToTuple_11_T7')
        ToTuple_11_T8 = typing.TypeVar('ToTuple_11_T8')
        ToTuple_11_T9 = typing.TypeVar('ToTuple_11_T9')
        ToTuple_11_T10 = typing.TypeVar('ToTuple_11_T10')
        ToTuple_11_T11 = typing.TypeVar('ToTuple_11_T11')
        class ToTuple_11(typing.Generic[ToTuple_11_T1, ToTuple_11_T2, ToTuple_11_T3, ToTuple_11_T4, ToTuple_11_T5, ToTuple_11_T6, ToTuple_11_T7, ToTuple_11_T8, ToTuple_11_T9, ToTuple_11_T10, ToTuple_11_T11]):
            ToTuple_11_T1 = TupleExtensions.ToTuple_MethodGroup.ToTuple_11_T1
            ToTuple_11_T2 = TupleExtensions.ToTuple_MethodGroup.ToTuple_11_T2
            ToTuple_11_T3 = TupleExtensions.ToTuple_MethodGroup.ToTuple_11_T3
            ToTuple_11_T4 = TupleExtensions.ToTuple_MethodGroup.ToTuple_11_T4
            ToTuple_11_T5 = TupleExtensions.ToTuple_MethodGroup.ToTuple_11_T5
            ToTuple_11_T6 = TupleExtensions.ToTuple_MethodGroup.ToTuple_11_T6
            ToTuple_11_T7 = TupleExtensions.ToTuple_MethodGroup.ToTuple_11_T7
            ToTuple_11_T8 = TupleExtensions.ToTuple_MethodGroup.ToTuple_11_T8
            ToTuple_11_T9 = TupleExtensions.ToTuple_MethodGroup.ToTuple_11_T9
            ToTuple_11_T10 = TupleExtensions.ToTuple_MethodGroup.ToTuple_11_T10
            ToTuple_11_T11 = TupleExtensions.ToTuple_MethodGroup.ToTuple_11_T11
            def __call__(self, value: ValueTuple_8[ToTuple_11_T1, ToTuple_11_T2, ToTuple_11_T3, ToTuple_11_T4, ToTuple_11_T5, ToTuple_11_T6, ToTuple_11_T7, ValueTuple_4[ToTuple_11_T8, ToTuple_11_T9, ToTuple_11_T10, ToTuple_11_T11]]) -> Tuple_8[ToTuple_11_T1, ToTuple_11_T2, ToTuple_11_T3, ToTuple_11_T4, ToTuple_11_T5, ToTuple_11_T6, ToTuple_11_T7, Tuple_4[ToTuple_11_T8, ToTuple_11_T9, ToTuple_11_T10, ToTuple_11_T11]]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[ToTuple_12_T1], typing.Type[ToTuple_12_T2], typing.Type[ToTuple_12_T3], typing.Type[ToTuple_12_T4], typing.Type[ToTuple_12_T5], typing.Type[ToTuple_12_T6], typing.Type[ToTuple_12_T7], typing.Type[ToTuple_12_T8], typing.Type[ToTuple_12_T9], typing.Type[ToTuple_12_T10], typing.Type[ToTuple_12_T11], typing.Type[ToTuple_12_T12]]) -> ToTuple_12[ToTuple_12_T1, ToTuple_12_T2, ToTuple_12_T3, ToTuple_12_T4, ToTuple_12_T5, ToTuple_12_T6, ToTuple_12_T7, ToTuple_12_T8, ToTuple_12_T9, ToTuple_12_T10, ToTuple_12_T11, ToTuple_12_T12]: ...

        ToTuple_12_T1 = typing.TypeVar('ToTuple_12_T1')
        ToTuple_12_T2 = typing.TypeVar('ToTuple_12_T2')
        ToTuple_12_T3 = typing.TypeVar('ToTuple_12_T3')
        ToTuple_12_T4 = typing.TypeVar('ToTuple_12_T4')
        ToTuple_12_T5 = typing.TypeVar('ToTuple_12_T5')
        ToTuple_12_T6 = typing.TypeVar('ToTuple_12_T6')
        ToTuple_12_T7 = typing.TypeVar('ToTuple_12_T7')
        ToTuple_12_T8 = typing.TypeVar('ToTuple_12_T8')
        ToTuple_12_T9 = typing.TypeVar('ToTuple_12_T9')
        ToTuple_12_T10 = typing.TypeVar('ToTuple_12_T10')
        ToTuple_12_T11 = typing.TypeVar('ToTuple_12_T11')
        ToTuple_12_T12 = typing.TypeVar('ToTuple_12_T12')
        class ToTuple_12(typing.Generic[ToTuple_12_T1, ToTuple_12_T2, ToTuple_12_T3, ToTuple_12_T4, ToTuple_12_T5, ToTuple_12_T6, ToTuple_12_T7, ToTuple_12_T8, ToTuple_12_T9, ToTuple_12_T10, ToTuple_12_T11, ToTuple_12_T12]):
            ToTuple_12_T1 = TupleExtensions.ToTuple_MethodGroup.ToTuple_12_T1
            ToTuple_12_T2 = TupleExtensions.ToTuple_MethodGroup.ToTuple_12_T2
            ToTuple_12_T3 = TupleExtensions.ToTuple_MethodGroup.ToTuple_12_T3
            ToTuple_12_T4 = TupleExtensions.ToTuple_MethodGroup.ToTuple_12_T4
            ToTuple_12_T5 = TupleExtensions.ToTuple_MethodGroup.ToTuple_12_T5
            ToTuple_12_T6 = TupleExtensions.ToTuple_MethodGroup.ToTuple_12_T6
            ToTuple_12_T7 = TupleExtensions.ToTuple_MethodGroup.ToTuple_12_T7
            ToTuple_12_T8 = TupleExtensions.ToTuple_MethodGroup.ToTuple_12_T8
            ToTuple_12_T9 = TupleExtensions.ToTuple_MethodGroup.ToTuple_12_T9
            ToTuple_12_T10 = TupleExtensions.ToTuple_MethodGroup.ToTuple_12_T10
            ToTuple_12_T11 = TupleExtensions.ToTuple_MethodGroup.ToTuple_12_T11
            ToTuple_12_T12 = TupleExtensions.ToTuple_MethodGroup.ToTuple_12_T12
            def __call__(self, value: ValueTuple_8[ToTuple_12_T1, ToTuple_12_T2, ToTuple_12_T3, ToTuple_12_T4, ToTuple_12_T5, ToTuple_12_T6, ToTuple_12_T7, ValueTuple_5[ToTuple_12_T8, ToTuple_12_T9, ToTuple_12_T10, ToTuple_12_T11, ToTuple_12_T12]]) -> Tuple_8[ToTuple_12_T1, ToTuple_12_T2, ToTuple_12_T3, ToTuple_12_T4, ToTuple_12_T5, ToTuple_12_T6, ToTuple_12_T7, Tuple_5[ToTuple_12_T8, ToTuple_12_T9, ToTuple_12_T10, ToTuple_12_T11, ToTuple_12_T12]]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[ToTuple_13_T1], typing.Type[ToTuple_13_T2], typing.Type[ToTuple_13_T3], typing.Type[ToTuple_13_T4], typing.Type[ToTuple_13_T5], typing.Type[ToTuple_13_T6], typing.Type[ToTuple_13_T7], typing.Type[ToTuple_13_T8], typing.Type[ToTuple_13_T9], typing.Type[ToTuple_13_T10], typing.Type[ToTuple_13_T11], typing.Type[ToTuple_13_T12], typing.Type[ToTuple_13_T13]]) -> ToTuple_13[ToTuple_13_T1, ToTuple_13_T2, ToTuple_13_T3, ToTuple_13_T4, ToTuple_13_T5, ToTuple_13_T6, ToTuple_13_T7, ToTuple_13_T8, ToTuple_13_T9, ToTuple_13_T10, ToTuple_13_T11, ToTuple_13_T12, ToTuple_13_T13]: ...

        ToTuple_13_T1 = typing.TypeVar('ToTuple_13_T1')
        ToTuple_13_T2 = typing.TypeVar('ToTuple_13_T2')
        ToTuple_13_T3 = typing.TypeVar('ToTuple_13_T3')
        ToTuple_13_T4 = typing.TypeVar('ToTuple_13_T4')
        ToTuple_13_T5 = typing.TypeVar('ToTuple_13_T5')
        ToTuple_13_T6 = typing.TypeVar('ToTuple_13_T6')
        ToTuple_13_T7 = typing.TypeVar('ToTuple_13_T7')
        ToTuple_13_T8 = typing.TypeVar('ToTuple_13_T8')
        ToTuple_13_T9 = typing.TypeVar('ToTuple_13_T9')
        ToTuple_13_T10 = typing.TypeVar('ToTuple_13_T10')
        ToTuple_13_T11 = typing.TypeVar('ToTuple_13_T11')
        ToTuple_13_T12 = typing.TypeVar('ToTuple_13_T12')
        ToTuple_13_T13 = typing.TypeVar('ToTuple_13_T13')
        class ToTuple_13(typing.Generic[ToTuple_13_T1, ToTuple_13_T2, ToTuple_13_T3, ToTuple_13_T4, ToTuple_13_T5, ToTuple_13_T6, ToTuple_13_T7, ToTuple_13_T8, ToTuple_13_T9, ToTuple_13_T10, ToTuple_13_T11, ToTuple_13_T12, ToTuple_13_T13]):
            ToTuple_13_T1 = TupleExtensions.ToTuple_MethodGroup.ToTuple_13_T1
            ToTuple_13_T2 = TupleExtensions.ToTuple_MethodGroup.ToTuple_13_T2
            ToTuple_13_T3 = TupleExtensions.ToTuple_MethodGroup.ToTuple_13_T3
            ToTuple_13_T4 = TupleExtensions.ToTuple_MethodGroup.ToTuple_13_T4
            ToTuple_13_T5 = TupleExtensions.ToTuple_MethodGroup.ToTuple_13_T5
            ToTuple_13_T6 = TupleExtensions.ToTuple_MethodGroup.ToTuple_13_T6
            ToTuple_13_T7 = TupleExtensions.ToTuple_MethodGroup.ToTuple_13_T7
            ToTuple_13_T8 = TupleExtensions.ToTuple_MethodGroup.ToTuple_13_T8
            ToTuple_13_T9 = TupleExtensions.ToTuple_MethodGroup.ToTuple_13_T9
            ToTuple_13_T10 = TupleExtensions.ToTuple_MethodGroup.ToTuple_13_T10
            ToTuple_13_T11 = TupleExtensions.ToTuple_MethodGroup.ToTuple_13_T11
            ToTuple_13_T12 = TupleExtensions.ToTuple_MethodGroup.ToTuple_13_T12
            ToTuple_13_T13 = TupleExtensions.ToTuple_MethodGroup.ToTuple_13_T13
            def __call__(self, value: ValueTuple_8[ToTuple_13_T1, ToTuple_13_T2, ToTuple_13_T3, ToTuple_13_T4, ToTuple_13_T5, ToTuple_13_T6, ToTuple_13_T7, ValueTuple_6[ToTuple_13_T8, ToTuple_13_T9, ToTuple_13_T10, ToTuple_13_T11, ToTuple_13_T12, ToTuple_13_T13]]) -> Tuple_8[ToTuple_13_T1, ToTuple_13_T2, ToTuple_13_T3, ToTuple_13_T4, ToTuple_13_T5, ToTuple_13_T6, ToTuple_13_T7, Tuple_6[ToTuple_13_T8, ToTuple_13_T9, ToTuple_13_T10, ToTuple_13_T11, ToTuple_13_T12, ToTuple_13_T13]]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[ToTuple_14_T1], typing.Type[ToTuple_14_T2], typing.Type[ToTuple_14_T3], typing.Type[ToTuple_14_T4], typing.Type[ToTuple_14_T5], typing.Type[ToTuple_14_T6], typing.Type[ToTuple_14_T7], typing.Type[ToTuple_14_T8], typing.Type[ToTuple_14_T9], typing.Type[ToTuple_14_T10], typing.Type[ToTuple_14_T11], typing.Type[ToTuple_14_T12], typing.Type[ToTuple_14_T13], typing.Type[ToTuple_14_T14]]) -> ToTuple_14[ToTuple_14_T1, ToTuple_14_T2, ToTuple_14_T3, ToTuple_14_T4, ToTuple_14_T5, ToTuple_14_T6, ToTuple_14_T7, ToTuple_14_T8, ToTuple_14_T9, ToTuple_14_T10, ToTuple_14_T11, ToTuple_14_T12, ToTuple_14_T13, ToTuple_14_T14]: ...

        ToTuple_14_T1 = typing.TypeVar('ToTuple_14_T1')
        ToTuple_14_T2 = typing.TypeVar('ToTuple_14_T2')
        ToTuple_14_T3 = typing.TypeVar('ToTuple_14_T3')
        ToTuple_14_T4 = typing.TypeVar('ToTuple_14_T4')
        ToTuple_14_T5 = typing.TypeVar('ToTuple_14_T5')
        ToTuple_14_T6 = typing.TypeVar('ToTuple_14_T6')
        ToTuple_14_T7 = typing.TypeVar('ToTuple_14_T7')
        ToTuple_14_T8 = typing.TypeVar('ToTuple_14_T8')
        ToTuple_14_T9 = typing.TypeVar('ToTuple_14_T9')
        ToTuple_14_T10 = typing.TypeVar('ToTuple_14_T10')
        ToTuple_14_T11 = typing.TypeVar('ToTuple_14_T11')
        ToTuple_14_T12 = typing.TypeVar('ToTuple_14_T12')
        ToTuple_14_T13 = typing.TypeVar('ToTuple_14_T13')
        ToTuple_14_T14 = typing.TypeVar('ToTuple_14_T14')
        class ToTuple_14(typing.Generic[ToTuple_14_T1, ToTuple_14_T2, ToTuple_14_T3, ToTuple_14_T4, ToTuple_14_T5, ToTuple_14_T6, ToTuple_14_T7, ToTuple_14_T8, ToTuple_14_T9, ToTuple_14_T10, ToTuple_14_T11, ToTuple_14_T12, ToTuple_14_T13, ToTuple_14_T14]):
            ToTuple_14_T1 = TupleExtensions.ToTuple_MethodGroup.ToTuple_14_T1
            ToTuple_14_T2 = TupleExtensions.ToTuple_MethodGroup.ToTuple_14_T2
            ToTuple_14_T3 = TupleExtensions.ToTuple_MethodGroup.ToTuple_14_T3
            ToTuple_14_T4 = TupleExtensions.ToTuple_MethodGroup.ToTuple_14_T4
            ToTuple_14_T5 = TupleExtensions.ToTuple_MethodGroup.ToTuple_14_T5
            ToTuple_14_T6 = TupleExtensions.ToTuple_MethodGroup.ToTuple_14_T6
            ToTuple_14_T7 = TupleExtensions.ToTuple_MethodGroup.ToTuple_14_T7
            ToTuple_14_T8 = TupleExtensions.ToTuple_MethodGroup.ToTuple_14_T8
            ToTuple_14_T9 = TupleExtensions.ToTuple_MethodGroup.ToTuple_14_T9
            ToTuple_14_T10 = TupleExtensions.ToTuple_MethodGroup.ToTuple_14_T10
            ToTuple_14_T11 = TupleExtensions.ToTuple_MethodGroup.ToTuple_14_T11
            ToTuple_14_T12 = TupleExtensions.ToTuple_MethodGroup.ToTuple_14_T12
            ToTuple_14_T13 = TupleExtensions.ToTuple_MethodGroup.ToTuple_14_T13
            ToTuple_14_T14 = TupleExtensions.ToTuple_MethodGroup.ToTuple_14_T14
            def __call__(self, value: ValueTuple_8[ToTuple_14_T1, ToTuple_14_T2, ToTuple_14_T3, ToTuple_14_T4, ToTuple_14_T5, ToTuple_14_T6, ToTuple_14_T7, ValueTuple_7[ToTuple_14_T8, ToTuple_14_T9, ToTuple_14_T10, ToTuple_14_T11, ToTuple_14_T12, ToTuple_14_T13, ToTuple_14_T14]]) -> Tuple_8[ToTuple_14_T1, ToTuple_14_T2, ToTuple_14_T3, ToTuple_14_T4, ToTuple_14_T5, ToTuple_14_T6, ToTuple_14_T7, Tuple_7[ToTuple_14_T8, ToTuple_14_T9, ToTuple_14_T10, ToTuple_14_T11, ToTuple_14_T12, ToTuple_14_T13, ToTuple_14_T14]]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[ToTuple_15_T1], typing.Type[ToTuple_15_T2], typing.Type[ToTuple_15_T3], typing.Type[ToTuple_15_T4], typing.Type[ToTuple_15_T5], typing.Type[ToTuple_15_T6], typing.Type[ToTuple_15_T7], typing.Type[ToTuple_15_T8], typing.Type[ToTuple_15_T9], typing.Type[ToTuple_15_T10], typing.Type[ToTuple_15_T11], typing.Type[ToTuple_15_T12], typing.Type[ToTuple_15_T13], typing.Type[ToTuple_15_T14], typing.Type[ToTuple_15_T15]]) -> ToTuple_15[ToTuple_15_T1, ToTuple_15_T2, ToTuple_15_T3, ToTuple_15_T4, ToTuple_15_T5, ToTuple_15_T6, ToTuple_15_T7, ToTuple_15_T8, ToTuple_15_T9, ToTuple_15_T10, ToTuple_15_T11, ToTuple_15_T12, ToTuple_15_T13, ToTuple_15_T14, ToTuple_15_T15]: ...

        ToTuple_15_T1 = typing.TypeVar('ToTuple_15_T1')
        ToTuple_15_T2 = typing.TypeVar('ToTuple_15_T2')
        ToTuple_15_T3 = typing.TypeVar('ToTuple_15_T3')
        ToTuple_15_T4 = typing.TypeVar('ToTuple_15_T4')
        ToTuple_15_T5 = typing.TypeVar('ToTuple_15_T5')
        ToTuple_15_T6 = typing.TypeVar('ToTuple_15_T6')
        ToTuple_15_T7 = typing.TypeVar('ToTuple_15_T7')
        ToTuple_15_T8 = typing.TypeVar('ToTuple_15_T8')
        ToTuple_15_T9 = typing.TypeVar('ToTuple_15_T9')
        ToTuple_15_T10 = typing.TypeVar('ToTuple_15_T10')
        ToTuple_15_T11 = typing.TypeVar('ToTuple_15_T11')
        ToTuple_15_T12 = typing.TypeVar('ToTuple_15_T12')
        ToTuple_15_T13 = typing.TypeVar('ToTuple_15_T13')
        ToTuple_15_T14 = typing.TypeVar('ToTuple_15_T14')
        ToTuple_15_T15 = typing.TypeVar('ToTuple_15_T15')
        class ToTuple_15(typing.Generic[ToTuple_15_T1, ToTuple_15_T2, ToTuple_15_T3, ToTuple_15_T4, ToTuple_15_T5, ToTuple_15_T6, ToTuple_15_T7, ToTuple_15_T8, ToTuple_15_T9, ToTuple_15_T10, ToTuple_15_T11, ToTuple_15_T12, ToTuple_15_T13, ToTuple_15_T14, ToTuple_15_T15]):
            ToTuple_15_T1 = TupleExtensions.ToTuple_MethodGroup.ToTuple_15_T1
            ToTuple_15_T2 = TupleExtensions.ToTuple_MethodGroup.ToTuple_15_T2
            ToTuple_15_T3 = TupleExtensions.ToTuple_MethodGroup.ToTuple_15_T3
            ToTuple_15_T4 = TupleExtensions.ToTuple_MethodGroup.ToTuple_15_T4
            ToTuple_15_T5 = TupleExtensions.ToTuple_MethodGroup.ToTuple_15_T5
            ToTuple_15_T6 = TupleExtensions.ToTuple_MethodGroup.ToTuple_15_T6
            ToTuple_15_T7 = TupleExtensions.ToTuple_MethodGroup.ToTuple_15_T7
            ToTuple_15_T8 = TupleExtensions.ToTuple_MethodGroup.ToTuple_15_T8
            ToTuple_15_T9 = TupleExtensions.ToTuple_MethodGroup.ToTuple_15_T9
            ToTuple_15_T10 = TupleExtensions.ToTuple_MethodGroup.ToTuple_15_T10
            ToTuple_15_T11 = TupleExtensions.ToTuple_MethodGroup.ToTuple_15_T11
            ToTuple_15_T12 = TupleExtensions.ToTuple_MethodGroup.ToTuple_15_T12
            ToTuple_15_T13 = TupleExtensions.ToTuple_MethodGroup.ToTuple_15_T13
            ToTuple_15_T14 = TupleExtensions.ToTuple_MethodGroup.ToTuple_15_T14
            ToTuple_15_T15 = TupleExtensions.ToTuple_MethodGroup.ToTuple_15_T15
            def __call__(self, value: ValueTuple_8[ToTuple_15_T1, ToTuple_15_T2, ToTuple_15_T3, ToTuple_15_T4, ToTuple_15_T5, ToTuple_15_T6, ToTuple_15_T7, ValueTuple_8[ToTuple_15_T8, ToTuple_15_T9, ToTuple_15_T10, ToTuple_15_T11, ToTuple_15_T12, ToTuple_15_T13, ToTuple_15_T14, ValueTuple_1[ToTuple_15_T15]]]) -> Tuple_8[ToTuple_15_T1, ToTuple_15_T2, ToTuple_15_T3, ToTuple_15_T4, ToTuple_15_T5, ToTuple_15_T6, ToTuple_15_T7, Tuple_8[ToTuple_15_T8, ToTuple_15_T9, ToTuple_15_T10, ToTuple_15_T11, ToTuple_15_T12, ToTuple_15_T13, ToTuple_15_T14, Tuple_1[ToTuple_15_T15]]]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[ToTuple_16_T1], typing.Type[ToTuple_16_T2], typing.Type[ToTuple_16_T3], typing.Type[ToTuple_16_T4], typing.Type[ToTuple_16_T5], typing.Type[ToTuple_16_T6], typing.Type[ToTuple_16_T7], typing.Type[ToTuple_16_T8], typing.Type[ToTuple_16_T9], typing.Type[ToTuple_16_T10], typing.Type[ToTuple_16_T11], typing.Type[ToTuple_16_T12], typing.Type[ToTuple_16_T13], typing.Type[ToTuple_16_T14], typing.Type[ToTuple_16_T15], typing.Type[ToTuple_16_T16]]) -> ToTuple_16[ToTuple_16_T1, ToTuple_16_T2, ToTuple_16_T3, ToTuple_16_T4, ToTuple_16_T5, ToTuple_16_T6, ToTuple_16_T7, ToTuple_16_T8, ToTuple_16_T9, ToTuple_16_T10, ToTuple_16_T11, ToTuple_16_T12, ToTuple_16_T13, ToTuple_16_T14, ToTuple_16_T15, ToTuple_16_T16]: ...

        ToTuple_16_T1 = typing.TypeVar('ToTuple_16_T1')
        ToTuple_16_T2 = typing.TypeVar('ToTuple_16_T2')
        ToTuple_16_T3 = typing.TypeVar('ToTuple_16_T3')
        ToTuple_16_T4 = typing.TypeVar('ToTuple_16_T4')
        ToTuple_16_T5 = typing.TypeVar('ToTuple_16_T5')
        ToTuple_16_T6 = typing.TypeVar('ToTuple_16_T6')
        ToTuple_16_T7 = typing.TypeVar('ToTuple_16_T7')
        ToTuple_16_T8 = typing.TypeVar('ToTuple_16_T8')
        ToTuple_16_T9 = typing.TypeVar('ToTuple_16_T9')
        ToTuple_16_T10 = typing.TypeVar('ToTuple_16_T10')
        ToTuple_16_T11 = typing.TypeVar('ToTuple_16_T11')
        ToTuple_16_T12 = typing.TypeVar('ToTuple_16_T12')
        ToTuple_16_T13 = typing.TypeVar('ToTuple_16_T13')
        ToTuple_16_T14 = typing.TypeVar('ToTuple_16_T14')
        ToTuple_16_T15 = typing.TypeVar('ToTuple_16_T15')
        ToTuple_16_T16 = typing.TypeVar('ToTuple_16_T16')
        class ToTuple_16(typing.Generic[ToTuple_16_T1, ToTuple_16_T2, ToTuple_16_T3, ToTuple_16_T4, ToTuple_16_T5, ToTuple_16_T6, ToTuple_16_T7, ToTuple_16_T8, ToTuple_16_T9, ToTuple_16_T10, ToTuple_16_T11, ToTuple_16_T12, ToTuple_16_T13, ToTuple_16_T14, ToTuple_16_T15, ToTuple_16_T16]):
            ToTuple_16_T1 = TupleExtensions.ToTuple_MethodGroup.ToTuple_16_T1
            ToTuple_16_T2 = TupleExtensions.ToTuple_MethodGroup.ToTuple_16_T2
            ToTuple_16_T3 = TupleExtensions.ToTuple_MethodGroup.ToTuple_16_T3
            ToTuple_16_T4 = TupleExtensions.ToTuple_MethodGroup.ToTuple_16_T4
            ToTuple_16_T5 = TupleExtensions.ToTuple_MethodGroup.ToTuple_16_T5
            ToTuple_16_T6 = TupleExtensions.ToTuple_MethodGroup.ToTuple_16_T6
            ToTuple_16_T7 = TupleExtensions.ToTuple_MethodGroup.ToTuple_16_T7
            ToTuple_16_T8 = TupleExtensions.ToTuple_MethodGroup.ToTuple_16_T8
            ToTuple_16_T9 = TupleExtensions.ToTuple_MethodGroup.ToTuple_16_T9
            ToTuple_16_T10 = TupleExtensions.ToTuple_MethodGroup.ToTuple_16_T10
            ToTuple_16_T11 = TupleExtensions.ToTuple_MethodGroup.ToTuple_16_T11
            ToTuple_16_T12 = TupleExtensions.ToTuple_MethodGroup.ToTuple_16_T12
            ToTuple_16_T13 = TupleExtensions.ToTuple_MethodGroup.ToTuple_16_T13
            ToTuple_16_T14 = TupleExtensions.ToTuple_MethodGroup.ToTuple_16_T14
            ToTuple_16_T15 = TupleExtensions.ToTuple_MethodGroup.ToTuple_16_T15
            ToTuple_16_T16 = TupleExtensions.ToTuple_MethodGroup.ToTuple_16_T16
            def __call__(self, value: ValueTuple_8[ToTuple_16_T1, ToTuple_16_T2, ToTuple_16_T3, ToTuple_16_T4, ToTuple_16_T5, ToTuple_16_T6, ToTuple_16_T7, ValueTuple_8[ToTuple_16_T8, ToTuple_16_T9, ToTuple_16_T10, ToTuple_16_T11, ToTuple_16_T12, ToTuple_16_T13, ToTuple_16_T14, ValueTuple_2[ToTuple_16_T15, ToTuple_16_T16]]]) -> Tuple_8[ToTuple_16_T1, ToTuple_16_T2, ToTuple_16_T3, ToTuple_16_T4, ToTuple_16_T5, ToTuple_16_T6, ToTuple_16_T7, Tuple_8[ToTuple_16_T8, ToTuple_16_T9, ToTuple_16_T10, ToTuple_16_T11, ToTuple_16_T12, ToTuple_16_T13, ToTuple_16_T14, Tuple_2[ToTuple_16_T15, ToTuple_16_T16]]]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[ToTuple_17_T1], typing.Type[ToTuple_17_T2], typing.Type[ToTuple_17_T3], typing.Type[ToTuple_17_T4], typing.Type[ToTuple_17_T5], typing.Type[ToTuple_17_T6], typing.Type[ToTuple_17_T7], typing.Type[ToTuple_17_T8], typing.Type[ToTuple_17_T9], typing.Type[ToTuple_17_T10], typing.Type[ToTuple_17_T11], typing.Type[ToTuple_17_T12], typing.Type[ToTuple_17_T13], typing.Type[ToTuple_17_T14], typing.Type[ToTuple_17_T15], typing.Type[ToTuple_17_T16], typing.Type[ToTuple_17_T17]]) -> ToTuple_17[ToTuple_17_T1, ToTuple_17_T2, ToTuple_17_T3, ToTuple_17_T4, ToTuple_17_T5, ToTuple_17_T6, ToTuple_17_T7, ToTuple_17_T8, ToTuple_17_T9, ToTuple_17_T10, ToTuple_17_T11, ToTuple_17_T12, ToTuple_17_T13, ToTuple_17_T14, ToTuple_17_T15, ToTuple_17_T16, ToTuple_17_T17]: ...

        ToTuple_17_T1 = typing.TypeVar('ToTuple_17_T1')
        ToTuple_17_T2 = typing.TypeVar('ToTuple_17_T2')
        ToTuple_17_T3 = typing.TypeVar('ToTuple_17_T3')
        ToTuple_17_T4 = typing.TypeVar('ToTuple_17_T4')
        ToTuple_17_T5 = typing.TypeVar('ToTuple_17_T5')
        ToTuple_17_T6 = typing.TypeVar('ToTuple_17_T6')
        ToTuple_17_T7 = typing.TypeVar('ToTuple_17_T7')
        ToTuple_17_T8 = typing.TypeVar('ToTuple_17_T8')
        ToTuple_17_T9 = typing.TypeVar('ToTuple_17_T9')
        ToTuple_17_T10 = typing.TypeVar('ToTuple_17_T10')
        ToTuple_17_T11 = typing.TypeVar('ToTuple_17_T11')
        ToTuple_17_T12 = typing.TypeVar('ToTuple_17_T12')
        ToTuple_17_T13 = typing.TypeVar('ToTuple_17_T13')
        ToTuple_17_T14 = typing.TypeVar('ToTuple_17_T14')
        ToTuple_17_T15 = typing.TypeVar('ToTuple_17_T15')
        ToTuple_17_T16 = typing.TypeVar('ToTuple_17_T16')
        ToTuple_17_T17 = typing.TypeVar('ToTuple_17_T17')
        class ToTuple_17(typing.Generic[ToTuple_17_T1, ToTuple_17_T2, ToTuple_17_T3, ToTuple_17_T4, ToTuple_17_T5, ToTuple_17_T6, ToTuple_17_T7, ToTuple_17_T8, ToTuple_17_T9, ToTuple_17_T10, ToTuple_17_T11, ToTuple_17_T12, ToTuple_17_T13, ToTuple_17_T14, ToTuple_17_T15, ToTuple_17_T16, ToTuple_17_T17]):
            ToTuple_17_T1 = TupleExtensions.ToTuple_MethodGroup.ToTuple_17_T1
            ToTuple_17_T2 = TupleExtensions.ToTuple_MethodGroup.ToTuple_17_T2
            ToTuple_17_T3 = TupleExtensions.ToTuple_MethodGroup.ToTuple_17_T3
            ToTuple_17_T4 = TupleExtensions.ToTuple_MethodGroup.ToTuple_17_T4
            ToTuple_17_T5 = TupleExtensions.ToTuple_MethodGroup.ToTuple_17_T5
            ToTuple_17_T6 = TupleExtensions.ToTuple_MethodGroup.ToTuple_17_T6
            ToTuple_17_T7 = TupleExtensions.ToTuple_MethodGroup.ToTuple_17_T7
            ToTuple_17_T8 = TupleExtensions.ToTuple_MethodGroup.ToTuple_17_T8
            ToTuple_17_T9 = TupleExtensions.ToTuple_MethodGroup.ToTuple_17_T9
            ToTuple_17_T10 = TupleExtensions.ToTuple_MethodGroup.ToTuple_17_T10
            ToTuple_17_T11 = TupleExtensions.ToTuple_MethodGroup.ToTuple_17_T11
            ToTuple_17_T12 = TupleExtensions.ToTuple_MethodGroup.ToTuple_17_T12
            ToTuple_17_T13 = TupleExtensions.ToTuple_MethodGroup.ToTuple_17_T13
            ToTuple_17_T14 = TupleExtensions.ToTuple_MethodGroup.ToTuple_17_T14
            ToTuple_17_T15 = TupleExtensions.ToTuple_MethodGroup.ToTuple_17_T15
            ToTuple_17_T16 = TupleExtensions.ToTuple_MethodGroup.ToTuple_17_T16
            ToTuple_17_T17 = TupleExtensions.ToTuple_MethodGroup.ToTuple_17_T17
            def __call__(self, value: ValueTuple_8[ToTuple_17_T1, ToTuple_17_T2, ToTuple_17_T3, ToTuple_17_T4, ToTuple_17_T5, ToTuple_17_T6, ToTuple_17_T7, ValueTuple_8[ToTuple_17_T8, ToTuple_17_T9, ToTuple_17_T10, ToTuple_17_T11, ToTuple_17_T12, ToTuple_17_T13, ToTuple_17_T14, ValueTuple_3[ToTuple_17_T15, ToTuple_17_T16, ToTuple_17_T17]]]) -> Tuple_8[ToTuple_17_T1, ToTuple_17_T2, ToTuple_17_T3, ToTuple_17_T4, ToTuple_17_T5, ToTuple_17_T6, ToTuple_17_T7, Tuple_8[ToTuple_17_T8, ToTuple_17_T9, ToTuple_17_T10, ToTuple_17_T11, ToTuple_17_T12, ToTuple_17_T13, ToTuple_17_T14, Tuple_3[ToTuple_17_T15, ToTuple_17_T16, ToTuple_17_T17]]]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[ToTuple_18_T1], typing.Type[ToTuple_18_T2], typing.Type[ToTuple_18_T3], typing.Type[ToTuple_18_T4], typing.Type[ToTuple_18_T5], typing.Type[ToTuple_18_T6], typing.Type[ToTuple_18_T7], typing.Type[ToTuple_18_T8], typing.Type[ToTuple_18_T9], typing.Type[ToTuple_18_T10], typing.Type[ToTuple_18_T11], typing.Type[ToTuple_18_T12], typing.Type[ToTuple_18_T13], typing.Type[ToTuple_18_T14], typing.Type[ToTuple_18_T15], typing.Type[ToTuple_18_T16], typing.Type[ToTuple_18_T17], typing.Type[ToTuple_18_T18]]) -> ToTuple_18[ToTuple_18_T1, ToTuple_18_T2, ToTuple_18_T3, ToTuple_18_T4, ToTuple_18_T5, ToTuple_18_T6, ToTuple_18_T7, ToTuple_18_T8, ToTuple_18_T9, ToTuple_18_T10, ToTuple_18_T11, ToTuple_18_T12, ToTuple_18_T13, ToTuple_18_T14, ToTuple_18_T15, ToTuple_18_T16, ToTuple_18_T17, ToTuple_18_T18]: ...

        ToTuple_18_T1 = typing.TypeVar('ToTuple_18_T1')
        ToTuple_18_T2 = typing.TypeVar('ToTuple_18_T2')
        ToTuple_18_T3 = typing.TypeVar('ToTuple_18_T3')
        ToTuple_18_T4 = typing.TypeVar('ToTuple_18_T4')
        ToTuple_18_T5 = typing.TypeVar('ToTuple_18_T5')
        ToTuple_18_T6 = typing.TypeVar('ToTuple_18_T6')
        ToTuple_18_T7 = typing.TypeVar('ToTuple_18_T7')
        ToTuple_18_T8 = typing.TypeVar('ToTuple_18_T8')
        ToTuple_18_T9 = typing.TypeVar('ToTuple_18_T9')
        ToTuple_18_T10 = typing.TypeVar('ToTuple_18_T10')
        ToTuple_18_T11 = typing.TypeVar('ToTuple_18_T11')
        ToTuple_18_T12 = typing.TypeVar('ToTuple_18_T12')
        ToTuple_18_T13 = typing.TypeVar('ToTuple_18_T13')
        ToTuple_18_T14 = typing.TypeVar('ToTuple_18_T14')
        ToTuple_18_T15 = typing.TypeVar('ToTuple_18_T15')
        ToTuple_18_T16 = typing.TypeVar('ToTuple_18_T16')
        ToTuple_18_T17 = typing.TypeVar('ToTuple_18_T17')
        ToTuple_18_T18 = typing.TypeVar('ToTuple_18_T18')
        class ToTuple_18(typing.Generic[ToTuple_18_T1, ToTuple_18_T2, ToTuple_18_T3, ToTuple_18_T4, ToTuple_18_T5, ToTuple_18_T6, ToTuple_18_T7, ToTuple_18_T8, ToTuple_18_T9, ToTuple_18_T10, ToTuple_18_T11, ToTuple_18_T12, ToTuple_18_T13, ToTuple_18_T14, ToTuple_18_T15, ToTuple_18_T16, ToTuple_18_T17, ToTuple_18_T18]):
            ToTuple_18_T1 = TupleExtensions.ToTuple_MethodGroup.ToTuple_18_T1
            ToTuple_18_T2 = TupleExtensions.ToTuple_MethodGroup.ToTuple_18_T2
            ToTuple_18_T3 = TupleExtensions.ToTuple_MethodGroup.ToTuple_18_T3
            ToTuple_18_T4 = TupleExtensions.ToTuple_MethodGroup.ToTuple_18_T4
            ToTuple_18_T5 = TupleExtensions.ToTuple_MethodGroup.ToTuple_18_T5
            ToTuple_18_T6 = TupleExtensions.ToTuple_MethodGroup.ToTuple_18_T6
            ToTuple_18_T7 = TupleExtensions.ToTuple_MethodGroup.ToTuple_18_T7
            ToTuple_18_T8 = TupleExtensions.ToTuple_MethodGroup.ToTuple_18_T8
            ToTuple_18_T9 = TupleExtensions.ToTuple_MethodGroup.ToTuple_18_T9
            ToTuple_18_T10 = TupleExtensions.ToTuple_MethodGroup.ToTuple_18_T10
            ToTuple_18_T11 = TupleExtensions.ToTuple_MethodGroup.ToTuple_18_T11
            ToTuple_18_T12 = TupleExtensions.ToTuple_MethodGroup.ToTuple_18_T12
            ToTuple_18_T13 = TupleExtensions.ToTuple_MethodGroup.ToTuple_18_T13
            ToTuple_18_T14 = TupleExtensions.ToTuple_MethodGroup.ToTuple_18_T14
            ToTuple_18_T15 = TupleExtensions.ToTuple_MethodGroup.ToTuple_18_T15
            ToTuple_18_T16 = TupleExtensions.ToTuple_MethodGroup.ToTuple_18_T16
            ToTuple_18_T17 = TupleExtensions.ToTuple_MethodGroup.ToTuple_18_T17
            ToTuple_18_T18 = TupleExtensions.ToTuple_MethodGroup.ToTuple_18_T18
            def __call__(self, value: ValueTuple_8[ToTuple_18_T1, ToTuple_18_T2, ToTuple_18_T3, ToTuple_18_T4, ToTuple_18_T5, ToTuple_18_T6, ToTuple_18_T7, ValueTuple_8[ToTuple_18_T8, ToTuple_18_T9, ToTuple_18_T10, ToTuple_18_T11, ToTuple_18_T12, ToTuple_18_T13, ToTuple_18_T14, ValueTuple_4[ToTuple_18_T15, ToTuple_18_T16, ToTuple_18_T17, ToTuple_18_T18]]]) -> Tuple_8[ToTuple_18_T1, ToTuple_18_T2, ToTuple_18_T3, ToTuple_18_T4, ToTuple_18_T5, ToTuple_18_T6, ToTuple_18_T7, Tuple_8[ToTuple_18_T8, ToTuple_18_T9, ToTuple_18_T10, ToTuple_18_T11, ToTuple_18_T12, ToTuple_18_T13, ToTuple_18_T14, Tuple_4[ToTuple_18_T15, ToTuple_18_T16, ToTuple_18_T17, ToTuple_18_T18]]]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[ToTuple_19_T1], typing.Type[ToTuple_19_T2], typing.Type[ToTuple_19_T3], typing.Type[ToTuple_19_T4], typing.Type[ToTuple_19_T5], typing.Type[ToTuple_19_T6], typing.Type[ToTuple_19_T7], typing.Type[ToTuple_19_T8], typing.Type[ToTuple_19_T9], typing.Type[ToTuple_19_T10], typing.Type[ToTuple_19_T11], typing.Type[ToTuple_19_T12], typing.Type[ToTuple_19_T13], typing.Type[ToTuple_19_T14], typing.Type[ToTuple_19_T15], typing.Type[ToTuple_19_T16], typing.Type[ToTuple_19_T17], typing.Type[ToTuple_19_T18], typing.Type[ToTuple_19_T19]]) -> ToTuple_19[ToTuple_19_T1, ToTuple_19_T2, ToTuple_19_T3, ToTuple_19_T4, ToTuple_19_T5, ToTuple_19_T6, ToTuple_19_T7, ToTuple_19_T8, ToTuple_19_T9, ToTuple_19_T10, ToTuple_19_T11, ToTuple_19_T12, ToTuple_19_T13, ToTuple_19_T14, ToTuple_19_T15, ToTuple_19_T16, ToTuple_19_T17, ToTuple_19_T18, ToTuple_19_T19]: ...

        ToTuple_19_T1 = typing.TypeVar('ToTuple_19_T1')
        ToTuple_19_T2 = typing.TypeVar('ToTuple_19_T2')
        ToTuple_19_T3 = typing.TypeVar('ToTuple_19_T3')
        ToTuple_19_T4 = typing.TypeVar('ToTuple_19_T4')
        ToTuple_19_T5 = typing.TypeVar('ToTuple_19_T5')
        ToTuple_19_T6 = typing.TypeVar('ToTuple_19_T6')
        ToTuple_19_T7 = typing.TypeVar('ToTuple_19_T7')
        ToTuple_19_T8 = typing.TypeVar('ToTuple_19_T8')
        ToTuple_19_T9 = typing.TypeVar('ToTuple_19_T9')
        ToTuple_19_T10 = typing.TypeVar('ToTuple_19_T10')
        ToTuple_19_T11 = typing.TypeVar('ToTuple_19_T11')
        ToTuple_19_T12 = typing.TypeVar('ToTuple_19_T12')
        ToTuple_19_T13 = typing.TypeVar('ToTuple_19_T13')
        ToTuple_19_T14 = typing.TypeVar('ToTuple_19_T14')
        ToTuple_19_T15 = typing.TypeVar('ToTuple_19_T15')
        ToTuple_19_T16 = typing.TypeVar('ToTuple_19_T16')
        ToTuple_19_T17 = typing.TypeVar('ToTuple_19_T17')
        ToTuple_19_T18 = typing.TypeVar('ToTuple_19_T18')
        ToTuple_19_T19 = typing.TypeVar('ToTuple_19_T19')
        class ToTuple_19(typing.Generic[ToTuple_19_T1, ToTuple_19_T2, ToTuple_19_T3, ToTuple_19_T4, ToTuple_19_T5, ToTuple_19_T6, ToTuple_19_T7, ToTuple_19_T8, ToTuple_19_T9, ToTuple_19_T10, ToTuple_19_T11, ToTuple_19_T12, ToTuple_19_T13, ToTuple_19_T14, ToTuple_19_T15, ToTuple_19_T16, ToTuple_19_T17, ToTuple_19_T18, ToTuple_19_T19]):
            ToTuple_19_T1 = TupleExtensions.ToTuple_MethodGroup.ToTuple_19_T1
            ToTuple_19_T2 = TupleExtensions.ToTuple_MethodGroup.ToTuple_19_T2
            ToTuple_19_T3 = TupleExtensions.ToTuple_MethodGroup.ToTuple_19_T3
            ToTuple_19_T4 = TupleExtensions.ToTuple_MethodGroup.ToTuple_19_T4
            ToTuple_19_T5 = TupleExtensions.ToTuple_MethodGroup.ToTuple_19_T5
            ToTuple_19_T6 = TupleExtensions.ToTuple_MethodGroup.ToTuple_19_T6
            ToTuple_19_T7 = TupleExtensions.ToTuple_MethodGroup.ToTuple_19_T7
            ToTuple_19_T8 = TupleExtensions.ToTuple_MethodGroup.ToTuple_19_T8
            ToTuple_19_T9 = TupleExtensions.ToTuple_MethodGroup.ToTuple_19_T9
            ToTuple_19_T10 = TupleExtensions.ToTuple_MethodGroup.ToTuple_19_T10
            ToTuple_19_T11 = TupleExtensions.ToTuple_MethodGroup.ToTuple_19_T11
            ToTuple_19_T12 = TupleExtensions.ToTuple_MethodGroup.ToTuple_19_T12
            ToTuple_19_T13 = TupleExtensions.ToTuple_MethodGroup.ToTuple_19_T13
            ToTuple_19_T14 = TupleExtensions.ToTuple_MethodGroup.ToTuple_19_T14
            ToTuple_19_T15 = TupleExtensions.ToTuple_MethodGroup.ToTuple_19_T15
            ToTuple_19_T16 = TupleExtensions.ToTuple_MethodGroup.ToTuple_19_T16
            ToTuple_19_T17 = TupleExtensions.ToTuple_MethodGroup.ToTuple_19_T17
            ToTuple_19_T18 = TupleExtensions.ToTuple_MethodGroup.ToTuple_19_T18
            ToTuple_19_T19 = TupleExtensions.ToTuple_MethodGroup.ToTuple_19_T19
            def __call__(self, value: ValueTuple_8[ToTuple_19_T1, ToTuple_19_T2, ToTuple_19_T3, ToTuple_19_T4, ToTuple_19_T5, ToTuple_19_T6, ToTuple_19_T7, ValueTuple_8[ToTuple_19_T8, ToTuple_19_T9, ToTuple_19_T10, ToTuple_19_T11, ToTuple_19_T12, ToTuple_19_T13, ToTuple_19_T14, ValueTuple_5[ToTuple_19_T15, ToTuple_19_T16, ToTuple_19_T17, ToTuple_19_T18, ToTuple_19_T19]]]) -> Tuple_8[ToTuple_19_T1, ToTuple_19_T2, ToTuple_19_T3, ToTuple_19_T4, ToTuple_19_T5, ToTuple_19_T6, ToTuple_19_T7, Tuple_8[ToTuple_19_T8, ToTuple_19_T9, ToTuple_19_T10, ToTuple_19_T11, ToTuple_19_T12, ToTuple_19_T13, ToTuple_19_T14, Tuple_5[ToTuple_19_T15, ToTuple_19_T16, ToTuple_19_T17, ToTuple_19_T18, ToTuple_19_T19]]]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[ToTuple_20_T1], typing.Type[ToTuple_20_T2], typing.Type[ToTuple_20_T3], typing.Type[ToTuple_20_T4], typing.Type[ToTuple_20_T5], typing.Type[ToTuple_20_T6], typing.Type[ToTuple_20_T7], typing.Type[ToTuple_20_T8], typing.Type[ToTuple_20_T9], typing.Type[ToTuple_20_T10], typing.Type[ToTuple_20_T11], typing.Type[ToTuple_20_T12], typing.Type[ToTuple_20_T13], typing.Type[ToTuple_20_T14], typing.Type[ToTuple_20_T15], typing.Type[ToTuple_20_T16], typing.Type[ToTuple_20_T17], typing.Type[ToTuple_20_T18], typing.Type[ToTuple_20_T19], typing.Type[ToTuple_20_T20]]) -> ToTuple_20[ToTuple_20_T1, ToTuple_20_T2, ToTuple_20_T3, ToTuple_20_T4, ToTuple_20_T5, ToTuple_20_T6, ToTuple_20_T7, ToTuple_20_T8, ToTuple_20_T9, ToTuple_20_T10, ToTuple_20_T11, ToTuple_20_T12, ToTuple_20_T13, ToTuple_20_T14, ToTuple_20_T15, ToTuple_20_T16, ToTuple_20_T17, ToTuple_20_T18, ToTuple_20_T19, ToTuple_20_T20]: ...

        ToTuple_20_T1 = typing.TypeVar('ToTuple_20_T1')
        ToTuple_20_T2 = typing.TypeVar('ToTuple_20_T2')
        ToTuple_20_T3 = typing.TypeVar('ToTuple_20_T3')
        ToTuple_20_T4 = typing.TypeVar('ToTuple_20_T4')
        ToTuple_20_T5 = typing.TypeVar('ToTuple_20_T5')
        ToTuple_20_T6 = typing.TypeVar('ToTuple_20_T6')
        ToTuple_20_T7 = typing.TypeVar('ToTuple_20_T7')
        ToTuple_20_T8 = typing.TypeVar('ToTuple_20_T8')
        ToTuple_20_T9 = typing.TypeVar('ToTuple_20_T9')
        ToTuple_20_T10 = typing.TypeVar('ToTuple_20_T10')
        ToTuple_20_T11 = typing.TypeVar('ToTuple_20_T11')
        ToTuple_20_T12 = typing.TypeVar('ToTuple_20_T12')
        ToTuple_20_T13 = typing.TypeVar('ToTuple_20_T13')
        ToTuple_20_T14 = typing.TypeVar('ToTuple_20_T14')
        ToTuple_20_T15 = typing.TypeVar('ToTuple_20_T15')
        ToTuple_20_T16 = typing.TypeVar('ToTuple_20_T16')
        ToTuple_20_T17 = typing.TypeVar('ToTuple_20_T17')
        ToTuple_20_T18 = typing.TypeVar('ToTuple_20_T18')
        ToTuple_20_T19 = typing.TypeVar('ToTuple_20_T19')
        ToTuple_20_T20 = typing.TypeVar('ToTuple_20_T20')
        class ToTuple_20(typing.Generic[ToTuple_20_T1, ToTuple_20_T2, ToTuple_20_T3, ToTuple_20_T4, ToTuple_20_T5, ToTuple_20_T6, ToTuple_20_T7, ToTuple_20_T8, ToTuple_20_T9, ToTuple_20_T10, ToTuple_20_T11, ToTuple_20_T12, ToTuple_20_T13, ToTuple_20_T14, ToTuple_20_T15, ToTuple_20_T16, ToTuple_20_T17, ToTuple_20_T18, ToTuple_20_T19, ToTuple_20_T20]):
            ToTuple_20_T1 = TupleExtensions.ToTuple_MethodGroup.ToTuple_20_T1
            ToTuple_20_T2 = TupleExtensions.ToTuple_MethodGroup.ToTuple_20_T2
            ToTuple_20_T3 = TupleExtensions.ToTuple_MethodGroup.ToTuple_20_T3
            ToTuple_20_T4 = TupleExtensions.ToTuple_MethodGroup.ToTuple_20_T4
            ToTuple_20_T5 = TupleExtensions.ToTuple_MethodGroup.ToTuple_20_T5
            ToTuple_20_T6 = TupleExtensions.ToTuple_MethodGroup.ToTuple_20_T6
            ToTuple_20_T7 = TupleExtensions.ToTuple_MethodGroup.ToTuple_20_T7
            ToTuple_20_T8 = TupleExtensions.ToTuple_MethodGroup.ToTuple_20_T8
            ToTuple_20_T9 = TupleExtensions.ToTuple_MethodGroup.ToTuple_20_T9
            ToTuple_20_T10 = TupleExtensions.ToTuple_MethodGroup.ToTuple_20_T10
            ToTuple_20_T11 = TupleExtensions.ToTuple_MethodGroup.ToTuple_20_T11
            ToTuple_20_T12 = TupleExtensions.ToTuple_MethodGroup.ToTuple_20_T12
            ToTuple_20_T13 = TupleExtensions.ToTuple_MethodGroup.ToTuple_20_T13
            ToTuple_20_T14 = TupleExtensions.ToTuple_MethodGroup.ToTuple_20_T14
            ToTuple_20_T15 = TupleExtensions.ToTuple_MethodGroup.ToTuple_20_T15
            ToTuple_20_T16 = TupleExtensions.ToTuple_MethodGroup.ToTuple_20_T16
            ToTuple_20_T17 = TupleExtensions.ToTuple_MethodGroup.ToTuple_20_T17
            ToTuple_20_T18 = TupleExtensions.ToTuple_MethodGroup.ToTuple_20_T18
            ToTuple_20_T19 = TupleExtensions.ToTuple_MethodGroup.ToTuple_20_T19
            ToTuple_20_T20 = TupleExtensions.ToTuple_MethodGroup.ToTuple_20_T20
            def __call__(self, value: ValueTuple_8[ToTuple_20_T1, ToTuple_20_T2, ToTuple_20_T3, ToTuple_20_T4, ToTuple_20_T5, ToTuple_20_T6, ToTuple_20_T7, ValueTuple_8[ToTuple_20_T8, ToTuple_20_T9, ToTuple_20_T10, ToTuple_20_T11, ToTuple_20_T12, ToTuple_20_T13, ToTuple_20_T14, ValueTuple_6[ToTuple_20_T15, ToTuple_20_T16, ToTuple_20_T17, ToTuple_20_T18, ToTuple_20_T19, ToTuple_20_T20]]]) -> Tuple_8[ToTuple_20_T1, ToTuple_20_T2, ToTuple_20_T3, ToTuple_20_T4, ToTuple_20_T5, ToTuple_20_T6, ToTuple_20_T7, Tuple_8[ToTuple_20_T8, ToTuple_20_T9, ToTuple_20_T10, ToTuple_20_T11, ToTuple_20_T12, ToTuple_20_T13, ToTuple_20_T14, Tuple_6[ToTuple_20_T15, ToTuple_20_T16, ToTuple_20_T17, ToTuple_20_T18, ToTuple_20_T19, ToTuple_20_T20]]]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[ToTuple_21_T1], typing.Type[ToTuple_21_T2], typing.Type[ToTuple_21_T3], typing.Type[ToTuple_21_T4], typing.Type[ToTuple_21_T5], typing.Type[ToTuple_21_T6], typing.Type[ToTuple_21_T7], typing.Type[ToTuple_21_T8], typing.Type[ToTuple_21_T9], typing.Type[ToTuple_21_T10], typing.Type[ToTuple_21_T11], typing.Type[ToTuple_21_T12], typing.Type[ToTuple_21_T13], typing.Type[ToTuple_21_T14], typing.Type[ToTuple_21_T15], typing.Type[ToTuple_21_T16], typing.Type[ToTuple_21_T17], typing.Type[ToTuple_21_T18], typing.Type[ToTuple_21_T19], typing.Type[ToTuple_21_T20], typing.Type[ToTuple_21_T21]]) -> ToTuple_21[ToTuple_21_T1, ToTuple_21_T2, ToTuple_21_T3, ToTuple_21_T4, ToTuple_21_T5, ToTuple_21_T6, ToTuple_21_T7, ToTuple_21_T8, ToTuple_21_T9, ToTuple_21_T10, ToTuple_21_T11, ToTuple_21_T12, ToTuple_21_T13, ToTuple_21_T14, ToTuple_21_T15, ToTuple_21_T16, ToTuple_21_T17, ToTuple_21_T18, ToTuple_21_T19, ToTuple_21_T20, ToTuple_21_T21]: ...

        ToTuple_21_T1 = typing.TypeVar('ToTuple_21_T1')
        ToTuple_21_T2 = typing.TypeVar('ToTuple_21_T2')
        ToTuple_21_T3 = typing.TypeVar('ToTuple_21_T3')
        ToTuple_21_T4 = typing.TypeVar('ToTuple_21_T4')
        ToTuple_21_T5 = typing.TypeVar('ToTuple_21_T5')
        ToTuple_21_T6 = typing.TypeVar('ToTuple_21_T6')
        ToTuple_21_T7 = typing.TypeVar('ToTuple_21_T7')
        ToTuple_21_T8 = typing.TypeVar('ToTuple_21_T8')
        ToTuple_21_T9 = typing.TypeVar('ToTuple_21_T9')
        ToTuple_21_T10 = typing.TypeVar('ToTuple_21_T10')
        ToTuple_21_T11 = typing.TypeVar('ToTuple_21_T11')
        ToTuple_21_T12 = typing.TypeVar('ToTuple_21_T12')
        ToTuple_21_T13 = typing.TypeVar('ToTuple_21_T13')
        ToTuple_21_T14 = typing.TypeVar('ToTuple_21_T14')
        ToTuple_21_T15 = typing.TypeVar('ToTuple_21_T15')
        ToTuple_21_T16 = typing.TypeVar('ToTuple_21_T16')
        ToTuple_21_T17 = typing.TypeVar('ToTuple_21_T17')
        ToTuple_21_T18 = typing.TypeVar('ToTuple_21_T18')
        ToTuple_21_T19 = typing.TypeVar('ToTuple_21_T19')
        ToTuple_21_T20 = typing.TypeVar('ToTuple_21_T20')
        ToTuple_21_T21 = typing.TypeVar('ToTuple_21_T21')
        class ToTuple_21(typing.Generic[ToTuple_21_T1, ToTuple_21_T2, ToTuple_21_T3, ToTuple_21_T4, ToTuple_21_T5, ToTuple_21_T6, ToTuple_21_T7, ToTuple_21_T8, ToTuple_21_T9, ToTuple_21_T10, ToTuple_21_T11, ToTuple_21_T12, ToTuple_21_T13, ToTuple_21_T14, ToTuple_21_T15, ToTuple_21_T16, ToTuple_21_T17, ToTuple_21_T18, ToTuple_21_T19, ToTuple_21_T20, ToTuple_21_T21]):
            ToTuple_21_T1 = TupleExtensions.ToTuple_MethodGroup.ToTuple_21_T1
            ToTuple_21_T2 = TupleExtensions.ToTuple_MethodGroup.ToTuple_21_T2
            ToTuple_21_T3 = TupleExtensions.ToTuple_MethodGroup.ToTuple_21_T3
            ToTuple_21_T4 = TupleExtensions.ToTuple_MethodGroup.ToTuple_21_T4
            ToTuple_21_T5 = TupleExtensions.ToTuple_MethodGroup.ToTuple_21_T5
            ToTuple_21_T6 = TupleExtensions.ToTuple_MethodGroup.ToTuple_21_T6
            ToTuple_21_T7 = TupleExtensions.ToTuple_MethodGroup.ToTuple_21_T7
            ToTuple_21_T8 = TupleExtensions.ToTuple_MethodGroup.ToTuple_21_T8
            ToTuple_21_T9 = TupleExtensions.ToTuple_MethodGroup.ToTuple_21_T9
            ToTuple_21_T10 = TupleExtensions.ToTuple_MethodGroup.ToTuple_21_T10
            ToTuple_21_T11 = TupleExtensions.ToTuple_MethodGroup.ToTuple_21_T11
            ToTuple_21_T12 = TupleExtensions.ToTuple_MethodGroup.ToTuple_21_T12
            ToTuple_21_T13 = TupleExtensions.ToTuple_MethodGroup.ToTuple_21_T13
            ToTuple_21_T14 = TupleExtensions.ToTuple_MethodGroup.ToTuple_21_T14
            ToTuple_21_T15 = TupleExtensions.ToTuple_MethodGroup.ToTuple_21_T15
            ToTuple_21_T16 = TupleExtensions.ToTuple_MethodGroup.ToTuple_21_T16
            ToTuple_21_T17 = TupleExtensions.ToTuple_MethodGroup.ToTuple_21_T17
            ToTuple_21_T18 = TupleExtensions.ToTuple_MethodGroup.ToTuple_21_T18
            ToTuple_21_T19 = TupleExtensions.ToTuple_MethodGroup.ToTuple_21_T19
            ToTuple_21_T20 = TupleExtensions.ToTuple_MethodGroup.ToTuple_21_T20
            ToTuple_21_T21 = TupleExtensions.ToTuple_MethodGroup.ToTuple_21_T21
            def __call__(self, value: ValueTuple_8[ToTuple_21_T1, ToTuple_21_T2, ToTuple_21_T3, ToTuple_21_T4, ToTuple_21_T5, ToTuple_21_T6, ToTuple_21_T7, ValueTuple_8[ToTuple_21_T8, ToTuple_21_T9, ToTuple_21_T10, ToTuple_21_T11, ToTuple_21_T12, ToTuple_21_T13, ToTuple_21_T14, ValueTuple_7[ToTuple_21_T15, ToTuple_21_T16, ToTuple_21_T17, ToTuple_21_T18, ToTuple_21_T19, ToTuple_21_T20, ToTuple_21_T21]]]) -> Tuple_8[ToTuple_21_T1, ToTuple_21_T2, ToTuple_21_T3, ToTuple_21_T4, ToTuple_21_T5, ToTuple_21_T6, ToTuple_21_T7, Tuple_8[ToTuple_21_T8, ToTuple_21_T9, ToTuple_21_T10, ToTuple_21_T11, ToTuple_21_T12, ToTuple_21_T13, ToTuple_21_T14, Tuple_7[ToTuple_21_T15, ToTuple_21_T16, ToTuple_21_T17, ToTuple_21_T18, ToTuple_21_T19, ToTuple_21_T20, ToTuple_21_T21]]]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[ToTuple_8_T1], typing.Type[ToTuple_8_T2], typing.Type[ToTuple_8_T3], typing.Type[ToTuple_8_T4], typing.Type[ToTuple_8_T5], typing.Type[ToTuple_8_T6], typing.Type[ToTuple_8_T7], typing.Type[ToTuple_8_T8]]) -> ToTuple_8[ToTuple_8_T1, ToTuple_8_T2, ToTuple_8_T3, ToTuple_8_T4, ToTuple_8_T5, ToTuple_8_T6, ToTuple_8_T7, ToTuple_8_T8]: ...

        ToTuple_8_T1 = typing.TypeVar('ToTuple_8_T1')
        ToTuple_8_T2 = typing.TypeVar('ToTuple_8_T2')
        ToTuple_8_T3 = typing.TypeVar('ToTuple_8_T3')
        ToTuple_8_T4 = typing.TypeVar('ToTuple_8_T4')
        ToTuple_8_T5 = typing.TypeVar('ToTuple_8_T5')
        ToTuple_8_T6 = typing.TypeVar('ToTuple_8_T6')
        ToTuple_8_T7 = typing.TypeVar('ToTuple_8_T7')
        ToTuple_8_T8 = typing.TypeVar('ToTuple_8_T8')
        class ToTuple_8(typing.Generic[ToTuple_8_T1, ToTuple_8_T2, ToTuple_8_T3, ToTuple_8_T4, ToTuple_8_T5, ToTuple_8_T6, ToTuple_8_T7, ToTuple_8_T8]):
            ToTuple_8_T1 = TupleExtensions.ToTuple_MethodGroup.ToTuple_8_T1
            ToTuple_8_T2 = TupleExtensions.ToTuple_MethodGroup.ToTuple_8_T2
            ToTuple_8_T3 = TupleExtensions.ToTuple_MethodGroup.ToTuple_8_T3
            ToTuple_8_T4 = TupleExtensions.ToTuple_MethodGroup.ToTuple_8_T4
            ToTuple_8_T5 = TupleExtensions.ToTuple_MethodGroup.ToTuple_8_T5
            ToTuple_8_T6 = TupleExtensions.ToTuple_MethodGroup.ToTuple_8_T6
            ToTuple_8_T7 = TupleExtensions.ToTuple_MethodGroup.ToTuple_8_T7
            ToTuple_8_T8 = TupleExtensions.ToTuple_MethodGroup.ToTuple_8_T8
            def __call__(self, value: ValueTuple_8[ToTuple_8_T1, ToTuple_8_T2, ToTuple_8_T3, ToTuple_8_T4, ToTuple_8_T5, ToTuple_8_T6, ToTuple_8_T7, ValueTuple_1[ToTuple_8_T8]]) -> Tuple_8[ToTuple_8_T1, ToTuple_8_T2, ToTuple_8_T3, ToTuple_8_T4, ToTuple_8_T5, ToTuple_8_T6, ToTuple_8_T7, Tuple_1[ToTuple_8_T8]]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[ToTuple_9_T1], typing.Type[ToTuple_9_T2], typing.Type[ToTuple_9_T3], typing.Type[ToTuple_9_T4], typing.Type[ToTuple_9_T5], typing.Type[ToTuple_9_T6], typing.Type[ToTuple_9_T7], typing.Type[ToTuple_9_T8], typing.Type[ToTuple_9_T9]]) -> ToTuple_9[ToTuple_9_T1, ToTuple_9_T2, ToTuple_9_T3, ToTuple_9_T4, ToTuple_9_T5, ToTuple_9_T6, ToTuple_9_T7, ToTuple_9_T8, ToTuple_9_T9]: ...

        ToTuple_9_T1 = typing.TypeVar('ToTuple_9_T1')
        ToTuple_9_T2 = typing.TypeVar('ToTuple_9_T2')
        ToTuple_9_T3 = typing.TypeVar('ToTuple_9_T3')
        ToTuple_9_T4 = typing.TypeVar('ToTuple_9_T4')
        ToTuple_9_T5 = typing.TypeVar('ToTuple_9_T5')
        ToTuple_9_T6 = typing.TypeVar('ToTuple_9_T6')
        ToTuple_9_T7 = typing.TypeVar('ToTuple_9_T7')
        ToTuple_9_T8 = typing.TypeVar('ToTuple_9_T8')
        ToTuple_9_T9 = typing.TypeVar('ToTuple_9_T9')
        class ToTuple_9(typing.Generic[ToTuple_9_T1, ToTuple_9_T2, ToTuple_9_T3, ToTuple_9_T4, ToTuple_9_T5, ToTuple_9_T6, ToTuple_9_T7, ToTuple_9_T8, ToTuple_9_T9]):
            ToTuple_9_T1 = TupleExtensions.ToTuple_MethodGroup.ToTuple_9_T1
            ToTuple_9_T2 = TupleExtensions.ToTuple_MethodGroup.ToTuple_9_T2
            ToTuple_9_T3 = TupleExtensions.ToTuple_MethodGroup.ToTuple_9_T3
            ToTuple_9_T4 = TupleExtensions.ToTuple_MethodGroup.ToTuple_9_T4
            ToTuple_9_T5 = TupleExtensions.ToTuple_MethodGroup.ToTuple_9_T5
            ToTuple_9_T6 = TupleExtensions.ToTuple_MethodGroup.ToTuple_9_T6
            ToTuple_9_T7 = TupleExtensions.ToTuple_MethodGroup.ToTuple_9_T7
            ToTuple_9_T8 = TupleExtensions.ToTuple_MethodGroup.ToTuple_9_T8
            ToTuple_9_T9 = TupleExtensions.ToTuple_MethodGroup.ToTuple_9_T9
            def __call__(self, value: ValueTuple_8[ToTuple_9_T1, ToTuple_9_T2, ToTuple_9_T3, ToTuple_9_T4, ToTuple_9_T5, ToTuple_9_T6, ToTuple_9_T7, ValueTuple_2[ToTuple_9_T8, ToTuple_9_T9]]) -> Tuple_8[ToTuple_9_T1, ToTuple_9_T2, ToTuple_9_T3, ToTuple_9_T4, ToTuple_9_T5, ToTuple_9_T6, ToTuple_9_T7, Tuple_2[ToTuple_9_T8, ToTuple_9_T9]]:...

        @typing.overload
        def __getitem__(self, t:typing.Type[ToTuple_1_T1]) -> ToTuple_1[ToTuple_1_T1]: ...

        ToTuple_1_T1 = typing.TypeVar('ToTuple_1_T1')
        class ToTuple_1(typing.Generic[ToTuple_1_T1]):
            ToTuple_1_T1 = TupleExtensions.ToTuple_MethodGroup.ToTuple_1_T1
            def __call__(self, value: ValueTuple_1[ToTuple_1_T1]) -> Tuple_1[ToTuple_1_T1]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[ToTuple_2_T1], typing.Type[ToTuple_2_T2]]) -> ToTuple_2[ToTuple_2_T1, ToTuple_2_T2]: ...

        ToTuple_2_T1 = typing.TypeVar('ToTuple_2_T1')
        ToTuple_2_T2 = typing.TypeVar('ToTuple_2_T2')
        class ToTuple_2(typing.Generic[ToTuple_2_T1, ToTuple_2_T2]):
            ToTuple_2_T1 = TupleExtensions.ToTuple_MethodGroup.ToTuple_2_T1
            ToTuple_2_T2 = TupleExtensions.ToTuple_MethodGroup.ToTuple_2_T2
            def __call__(self, value: ValueTuple_2[ToTuple_2_T1, ToTuple_2_T2]) -> Tuple_2[ToTuple_2_T1, ToTuple_2_T2]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[ToTuple_3_T1], typing.Type[ToTuple_3_T2], typing.Type[ToTuple_3_T3]]) -> ToTuple_3[ToTuple_3_T1, ToTuple_3_T2, ToTuple_3_T3]: ...

        ToTuple_3_T1 = typing.TypeVar('ToTuple_3_T1')
        ToTuple_3_T2 = typing.TypeVar('ToTuple_3_T2')
        ToTuple_3_T3 = typing.TypeVar('ToTuple_3_T3')
        class ToTuple_3(typing.Generic[ToTuple_3_T1, ToTuple_3_T2, ToTuple_3_T3]):
            ToTuple_3_T1 = TupleExtensions.ToTuple_MethodGroup.ToTuple_3_T1
            ToTuple_3_T2 = TupleExtensions.ToTuple_MethodGroup.ToTuple_3_T2
            ToTuple_3_T3 = TupleExtensions.ToTuple_MethodGroup.ToTuple_3_T3
            def __call__(self, value: ValueTuple_3[ToTuple_3_T1, ToTuple_3_T2, ToTuple_3_T3]) -> Tuple_3[ToTuple_3_T1, ToTuple_3_T2, ToTuple_3_T3]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[ToTuple_4_T1], typing.Type[ToTuple_4_T2], typing.Type[ToTuple_4_T3], typing.Type[ToTuple_4_T4]]) -> ToTuple_4[ToTuple_4_T1, ToTuple_4_T2, ToTuple_4_T3, ToTuple_4_T4]: ...

        ToTuple_4_T1 = typing.TypeVar('ToTuple_4_T1')
        ToTuple_4_T2 = typing.TypeVar('ToTuple_4_T2')
        ToTuple_4_T3 = typing.TypeVar('ToTuple_4_T3')
        ToTuple_4_T4 = typing.TypeVar('ToTuple_4_T4')
        class ToTuple_4(typing.Generic[ToTuple_4_T1, ToTuple_4_T2, ToTuple_4_T3, ToTuple_4_T4]):
            ToTuple_4_T1 = TupleExtensions.ToTuple_MethodGroup.ToTuple_4_T1
            ToTuple_4_T2 = TupleExtensions.ToTuple_MethodGroup.ToTuple_4_T2
            ToTuple_4_T3 = TupleExtensions.ToTuple_MethodGroup.ToTuple_4_T3
            ToTuple_4_T4 = TupleExtensions.ToTuple_MethodGroup.ToTuple_4_T4
            def __call__(self, value: ValueTuple_4[ToTuple_4_T1, ToTuple_4_T2, ToTuple_4_T3, ToTuple_4_T4]) -> Tuple_4[ToTuple_4_T1, ToTuple_4_T2, ToTuple_4_T3, ToTuple_4_T4]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[ToTuple_5_T1], typing.Type[ToTuple_5_T2], typing.Type[ToTuple_5_T3], typing.Type[ToTuple_5_T4], typing.Type[ToTuple_5_T5]]) -> ToTuple_5[ToTuple_5_T1, ToTuple_5_T2, ToTuple_5_T3, ToTuple_5_T4, ToTuple_5_T5]: ...

        ToTuple_5_T1 = typing.TypeVar('ToTuple_5_T1')
        ToTuple_5_T2 = typing.TypeVar('ToTuple_5_T2')
        ToTuple_5_T3 = typing.TypeVar('ToTuple_5_T3')
        ToTuple_5_T4 = typing.TypeVar('ToTuple_5_T4')
        ToTuple_5_T5 = typing.TypeVar('ToTuple_5_T5')
        class ToTuple_5(typing.Generic[ToTuple_5_T1, ToTuple_5_T2, ToTuple_5_T3, ToTuple_5_T4, ToTuple_5_T5]):
            ToTuple_5_T1 = TupleExtensions.ToTuple_MethodGroup.ToTuple_5_T1
            ToTuple_5_T2 = TupleExtensions.ToTuple_MethodGroup.ToTuple_5_T2
            ToTuple_5_T3 = TupleExtensions.ToTuple_MethodGroup.ToTuple_5_T3
            ToTuple_5_T4 = TupleExtensions.ToTuple_MethodGroup.ToTuple_5_T4
            ToTuple_5_T5 = TupleExtensions.ToTuple_MethodGroup.ToTuple_5_T5
            def __call__(self, value: ValueTuple_5[ToTuple_5_T1, ToTuple_5_T2, ToTuple_5_T3, ToTuple_5_T4, ToTuple_5_T5]) -> Tuple_5[ToTuple_5_T1, ToTuple_5_T2, ToTuple_5_T3, ToTuple_5_T4, ToTuple_5_T5]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[ToTuple_6_T1], typing.Type[ToTuple_6_T2], typing.Type[ToTuple_6_T3], typing.Type[ToTuple_6_T4], typing.Type[ToTuple_6_T5], typing.Type[ToTuple_6_T6]]) -> ToTuple_6[ToTuple_6_T1, ToTuple_6_T2, ToTuple_6_T3, ToTuple_6_T4, ToTuple_6_T5, ToTuple_6_T6]: ...

        ToTuple_6_T1 = typing.TypeVar('ToTuple_6_T1')
        ToTuple_6_T2 = typing.TypeVar('ToTuple_6_T2')
        ToTuple_6_T3 = typing.TypeVar('ToTuple_6_T3')
        ToTuple_6_T4 = typing.TypeVar('ToTuple_6_T4')
        ToTuple_6_T5 = typing.TypeVar('ToTuple_6_T5')
        ToTuple_6_T6 = typing.TypeVar('ToTuple_6_T6')
        class ToTuple_6(typing.Generic[ToTuple_6_T1, ToTuple_6_T2, ToTuple_6_T3, ToTuple_6_T4, ToTuple_6_T5, ToTuple_6_T6]):
            ToTuple_6_T1 = TupleExtensions.ToTuple_MethodGroup.ToTuple_6_T1
            ToTuple_6_T2 = TupleExtensions.ToTuple_MethodGroup.ToTuple_6_T2
            ToTuple_6_T3 = TupleExtensions.ToTuple_MethodGroup.ToTuple_6_T3
            ToTuple_6_T4 = TupleExtensions.ToTuple_MethodGroup.ToTuple_6_T4
            ToTuple_6_T5 = TupleExtensions.ToTuple_MethodGroup.ToTuple_6_T5
            ToTuple_6_T6 = TupleExtensions.ToTuple_MethodGroup.ToTuple_6_T6
            def __call__(self, value: ValueTuple_6[ToTuple_6_T1, ToTuple_6_T2, ToTuple_6_T3, ToTuple_6_T4, ToTuple_6_T5, ToTuple_6_T6]) -> Tuple_6[ToTuple_6_T1, ToTuple_6_T2, ToTuple_6_T3, ToTuple_6_T4, ToTuple_6_T5, ToTuple_6_T6]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[ToTuple_7_T1], typing.Type[ToTuple_7_T2], typing.Type[ToTuple_7_T3], typing.Type[ToTuple_7_T4], typing.Type[ToTuple_7_T5], typing.Type[ToTuple_7_T6], typing.Type[ToTuple_7_T7]]) -> ToTuple_7[ToTuple_7_T1, ToTuple_7_T2, ToTuple_7_T3, ToTuple_7_T4, ToTuple_7_T5, ToTuple_7_T6, ToTuple_7_T7]: ...

        ToTuple_7_T1 = typing.TypeVar('ToTuple_7_T1')
        ToTuple_7_T2 = typing.TypeVar('ToTuple_7_T2')
        ToTuple_7_T3 = typing.TypeVar('ToTuple_7_T3')
        ToTuple_7_T4 = typing.TypeVar('ToTuple_7_T4')
        ToTuple_7_T5 = typing.TypeVar('ToTuple_7_T5')
        ToTuple_7_T6 = typing.TypeVar('ToTuple_7_T6')
        ToTuple_7_T7 = typing.TypeVar('ToTuple_7_T7')
        class ToTuple_7(typing.Generic[ToTuple_7_T1, ToTuple_7_T2, ToTuple_7_T3, ToTuple_7_T4, ToTuple_7_T5, ToTuple_7_T6, ToTuple_7_T7]):
            ToTuple_7_T1 = TupleExtensions.ToTuple_MethodGroup.ToTuple_7_T1
            ToTuple_7_T2 = TupleExtensions.ToTuple_MethodGroup.ToTuple_7_T2
            ToTuple_7_T3 = TupleExtensions.ToTuple_MethodGroup.ToTuple_7_T3
            ToTuple_7_T4 = TupleExtensions.ToTuple_MethodGroup.ToTuple_7_T4
            ToTuple_7_T5 = TupleExtensions.ToTuple_MethodGroup.ToTuple_7_T5
            ToTuple_7_T6 = TupleExtensions.ToTuple_MethodGroup.ToTuple_7_T6
            ToTuple_7_T7 = TupleExtensions.ToTuple_MethodGroup.ToTuple_7_T7
            def __call__(self, value: ValueTuple_7[ToTuple_7_T1, ToTuple_7_T2, ToTuple_7_T3, ToTuple_7_T4, ToTuple_7_T5, ToTuple_7_T6, ToTuple_7_T7]) -> Tuple_7[ToTuple_7_T1, ToTuple_7_T2, ToTuple_7_T3, ToTuple_7_T4, ToTuple_7_T5, ToTuple_7_T6, ToTuple_7_T7]:...


    # Skipped ToValueTuple due to it being static, abstract and generic.

    ToValueTuple : ToValueTuple_MethodGroup
    class ToValueTuple_MethodGroup:
        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[ToValueTuple_8_T1], typing.Type[ToValueTuple_8_T2], typing.Type[ToValueTuple_8_T3], typing.Type[ToValueTuple_8_T4], typing.Type[ToValueTuple_8_T5], typing.Type[ToValueTuple_8_T6], typing.Type[ToValueTuple_8_T7], typing.Type[ToValueTuple_8_T8]]) -> ToValueTuple_8[ToValueTuple_8_T1, ToValueTuple_8_T2, ToValueTuple_8_T3, ToValueTuple_8_T4, ToValueTuple_8_T5, ToValueTuple_8_T6, ToValueTuple_8_T7, ToValueTuple_8_T8]: ...

        ToValueTuple_8_T1 = typing.TypeVar('ToValueTuple_8_T1')
        ToValueTuple_8_T2 = typing.TypeVar('ToValueTuple_8_T2')
        ToValueTuple_8_T3 = typing.TypeVar('ToValueTuple_8_T3')
        ToValueTuple_8_T4 = typing.TypeVar('ToValueTuple_8_T4')
        ToValueTuple_8_T5 = typing.TypeVar('ToValueTuple_8_T5')
        ToValueTuple_8_T6 = typing.TypeVar('ToValueTuple_8_T6')
        ToValueTuple_8_T7 = typing.TypeVar('ToValueTuple_8_T7')
        ToValueTuple_8_T8 = typing.TypeVar('ToValueTuple_8_T8')
        class ToValueTuple_8(typing.Generic[ToValueTuple_8_T1, ToValueTuple_8_T2, ToValueTuple_8_T3, ToValueTuple_8_T4, ToValueTuple_8_T5, ToValueTuple_8_T6, ToValueTuple_8_T7, ToValueTuple_8_T8]):
            ToValueTuple_8_T1 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_8_T1
            ToValueTuple_8_T2 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_8_T2
            ToValueTuple_8_T3 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_8_T3
            ToValueTuple_8_T4 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_8_T4
            ToValueTuple_8_T5 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_8_T5
            ToValueTuple_8_T6 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_8_T6
            ToValueTuple_8_T7 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_8_T7
            ToValueTuple_8_T8 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_8_T8
            def __call__(self, value: Tuple_8[ToValueTuple_8_T1, ToValueTuple_8_T2, ToValueTuple_8_T3, ToValueTuple_8_T4, ToValueTuple_8_T5, ToValueTuple_8_T6, ToValueTuple_8_T7, Tuple_1[ToValueTuple_8_T8]]) -> ValueTuple_8[ToValueTuple_8_T1, ToValueTuple_8_T2, ToValueTuple_8_T3, ToValueTuple_8_T4, ToValueTuple_8_T5, ToValueTuple_8_T6, ToValueTuple_8_T7, ValueTuple_1[ToValueTuple_8_T8]]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[ToValueTuple_9_T1], typing.Type[ToValueTuple_9_T2], typing.Type[ToValueTuple_9_T3], typing.Type[ToValueTuple_9_T4], typing.Type[ToValueTuple_9_T5], typing.Type[ToValueTuple_9_T6], typing.Type[ToValueTuple_9_T7], typing.Type[ToValueTuple_9_T8], typing.Type[ToValueTuple_9_T9]]) -> ToValueTuple_9[ToValueTuple_9_T1, ToValueTuple_9_T2, ToValueTuple_9_T3, ToValueTuple_9_T4, ToValueTuple_9_T5, ToValueTuple_9_T6, ToValueTuple_9_T7, ToValueTuple_9_T8, ToValueTuple_9_T9]: ...

        ToValueTuple_9_T1 = typing.TypeVar('ToValueTuple_9_T1')
        ToValueTuple_9_T2 = typing.TypeVar('ToValueTuple_9_T2')
        ToValueTuple_9_T3 = typing.TypeVar('ToValueTuple_9_T3')
        ToValueTuple_9_T4 = typing.TypeVar('ToValueTuple_9_T4')
        ToValueTuple_9_T5 = typing.TypeVar('ToValueTuple_9_T5')
        ToValueTuple_9_T6 = typing.TypeVar('ToValueTuple_9_T6')
        ToValueTuple_9_T7 = typing.TypeVar('ToValueTuple_9_T7')
        ToValueTuple_9_T8 = typing.TypeVar('ToValueTuple_9_T8')
        ToValueTuple_9_T9 = typing.TypeVar('ToValueTuple_9_T9')
        class ToValueTuple_9(typing.Generic[ToValueTuple_9_T1, ToValueTuple_9_T2, ToValueTuple_9_T3, ToValueTuple_9_T4, ToValueTuple_9_T5, ToValueTuple_9_T6, ToValueTuple_9_T7, ToValueTuple_9_T8, ToValueTuple_9_T9]):
            ToValueTuple_9_T1 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_9_T1
            ToValueTuple_9_T2 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_9_T2
            ToValueTuple_9_T3 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_9_T3
            ToValueTuple_9_T4 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_9_T4
            ToValueTuple_9_T5 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_9_T5
            ToValueTuple_9_T6 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_9_T6
            ToValueTuple_9_T7 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_9_T7
            ToValueTuple_9_T8 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_9_T8
            ToValueTuple_9_T9 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_9_T9
            def __call__(self, value: Tuple_8[ToValueTuple_9_T1, ToValueTuple_9_T2, ToValueTuple_9_T3, ToValueTuple_9_T4, ToValueTuple_9_T5, ToValueTuple_9_T6, ToValueTuple_9_T7, Tuple_2[ToValueTuple_9_T8, ToValueTuple_9_T9]]) -> ValueTuple_8[ToValueTuple_9_T1, ToValueTuple_9_T2, ToValueTuple_9_T3, ToValueTuple_9_T4, ToValueTuple_9_T5, ToValueTuple_9_T6, ToValueTuple_9_T7, ValueTuple_2[ToValueTuple_9_T8, ToValueTuple_9_T9]]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[ToValueTuple_10_T1], typing.Type[ToValueTuple_10_T2], typing.Type[ToValueTuple_10_T3], typing.Type[ToValueTuple_10_T4], typing.Type[ToValueTuple_10_T5], typing.Type[ToValueTuple_10_T6], typing.Type[ToValueTuple_10_T7], typing.Type[ToValueTuple_10_T8], typing.Type[ToValueTuple_10_T9], typing.Type[ToValueTuple_10_T10]]) -> ToValueTuple_10[ToValueTuple_10_T1, ToValueTuple_10_T2, ToValueTuple_10_T3, ToValueTuple_10_T4, ToValueTuple_10_T5, ToValueTuple_10_T6, ToValueTuple_10_T7, ToValueTuple_10_T8, ToValueTuple_10_T9, ToValueTuple_10_T10]: ...

        ToValueTuple_10_T1 = typing.TypeVar('ToValueTuple_10_T1')
        ToValueTuple_10_T2 = typing.TypeVar('ToValueTuple_10_T2')
        ToValueTuple_10_T3 = typing.TypeVar('ToValueTuple_10_T3')
        ToValueTuple_10_T4 = typing.TypeVar('ToValueTuple_10_T4')
        ToValueTuple_10_T5 = typing.TypeVar('ToValueTuple_10_T5')
        ToValueTuple_10_T6 = typing.TypeVar('ToValueTuple_10_T6')
        ToValueTuple_10_T7 = typing.TypeVar('ToValueTuple_10_T7')
        ToValueTuple_10_T8 = typing.TypeVar('ToValueTuple_10_T8')
        ToValueTuple_10_T9 = typing.TypeVar('ToValueTuple_10_T9')
        ToValueTuple_10_T10 = typing.TypeVar('ToValueTuple_10_T10')
        class ToValueTuple_10(typing.Generic[ToValueTuple_10_T1, ToValueTuple_10_T2, ToValueTuple_10_T3, ToValueTuple_10_T4, ToValueTuple_10_T5, ToValueTuple_10_T6, ToValueTuple_10_T7, ToValueTuple_10_T8, ToValueTuple_10_T9, ToValueTuple_10_T10]):
            ToValueTuple_10_T1 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_10_T1
            ToValueTuple_10_T2 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_10_T2
            ToValueTuple_10_T3 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_10_T3
            ToValueTuple_10_T4 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_10_T4
            ToValueTuple_10_T5 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_10_T5
            ToValueTuple_10_T6 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_10_T6
            ToValueTuple_10_T7 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_10_T7
            ToValueTuple_10_T8 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_10_T8
            ToValueTuple_10_T9 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_10_T9
            ToValueTuple_10_T10 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_10_T10
            def __call__(self, value: Tuple_8[ToValueTuple_10_T1, ToValueTuple_10_T2, ToValueTuple_10_T3, ToValueTuple_10_T4, ToValueTuple_10_T5, ToValueTuple_10_T6, ToValueTuple_10_T7, Tuple_3[ToValueTuple_10_T8, ToValueTuple_10_T9, ToValueTuple_10_T10]]) -> ValueTuple_8[ToValueTuple_10_T1, ToValueTuple_10_T2, ToValueTuple_10_T3, ToValueTuple_10_T4, ToValueTuple_10_T5, ToValueTuple_10_T6, ToValueTuple_10_T7, ValueTuple_3[ToValueTuple_10_T8, ToValueTuple_10_T9, ToValueTuple_10_T10]]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[ToValueTuple_11_T1], typing.Type[ToValueTuple_11_T2], typing.Type[ToValueTuple_11_T3], typing.Type[ToValueTuple_11_T4], typing.Type[ToValueTuple_11_T5], typing.Type[ToValueTuple_11_T6], typing.Type[ToValueTuple_11_T7], typing.Type[ToValueTuple_11_T8], typing.Type[ToValueTuple_11_T9], typing.Type[ToValueTuple_11_T10], typing.Type[ToValueTuple_11_T11]]) -> ToValueTuple_11[ToValueTuple_11_T1, ToValueTuple_11_T2, ToValueTuple_11_T3, ToValueTuple_11_T4, ToValueTuple_11_T5, ToValueTuple_11_T6, ToValueTuple_11_T7, ToValueTuple_11_T8, ToValueTuple_11_T9, ToValueTuple_11_T10, ToValueTuple_11_T11]: ...

        ToValueTuple_11_T1 = typing.TypeVar('ToValueTuple_11_T1')
        ToValueTuple_11_T2 = typing.TypeVar('ToValueTuple_11_T2')
        ToValueTuple_11_T3 = typing.TypeVar('ToValueTuple_11_T3')
        ToValueTuple_11_T4 = typing.TypeVar('ToValueTuple_11_T4')
        ToValueTuple_11_T5 = typing.TypeVar('ToValueTuple_11_T5')
        ToValueTuple_11_T6 = typing.TypeVar('ToValueTuple_11_T6')
        ToValueTuple_11_T7 = typing.TypeVar('ToValueTuple_11_T7')
        ToValueTuple_11_T8 = typing.TypeVar('ToValueTuple_11_T8')
        ToValueTuple_11_T9 = typing.TypeVar('ToValueTuple_11_T9')
        ToValueTuple_11_T10 = typing.TypeVar('ToValueTuple_11_T10')
        ToValueTuple_11_T11 = typing.TypeVar('ToValueTuple_11_T11')
        class ToValueTuple_11(typing.Generic[ToValueTuple_11_T1, ToValueTuple_11_T2, ToValueTuple_11_T3, ToValueTuple_11_T4, ToValueTuple_11_T5, ToValueTuple_11_T6, ToValueTuple_11_T7, ToValueTuple_11_T8, ToValueTuple_11_T9, ToValueTuple_11_T10, ToValueTuple_11_T11]):
            ToValueTuple_11_T1 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_11_T1
            ToValueTuple_11_T2 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_11_T2
            ToValueTuple_11_T3 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_11_T3
            ToValueTuple_11_T4 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_11_T4
            ToValueTuple_11_T5 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_11_T5
            ToValueTuple_11_T6 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_11_T6
            ToValueTuple_11_T7 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_11_T7
            ToValueTuple_11_T8 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_11_T8
            ToValueTuple_11_T9 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_11_T9
            ToValueTuple_11_T10 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_11_T10
            ToValueTuple_11_T11 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_11_T11
            def __call__(self, value: Tuple_8[ToValueTuple_11_T1, ToValueTuple_11_T2, ToValueTuple_11_T3, ToValueTuple_11_T4, ToValueTuple_11_T5, ToValueTuple_11_T6, ToValueTuple_11_T7, Tuple_4[ToValueTuple_11_T8, ToValueTuple_11_T9, ToValueTuple_11_T10, ToValueTuple_11_T11]]) -> ValueTuple_8[ToValueTuple_11_T1, ToValueTuple_11_T2, ToValueTuple_11_T3, ToValueTuple_11_T4, ToValueTuple_11_T5, ToValueTuple_11_T6, ToValueTuple_11_T7, ValueTuple_4[ToValueTuple_11_T8, ToValueTuple_11_T9, ToValueTuple_11_T10, ToValueTuple_11_T11]]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[ToValueTuple_12_T1], typing.Type[ToValueTuple_12_T2], typing.Type[ToValueTuple_12_T3], typing.Type[ToValueTuple_12_T4], typing.Type[ToValueTuple_12_T5], typing.Type[ToValueTuple_12_T6], typing.Type[ToValueTuple_12_T7], typing.Type[ToValueTuple_12_T8], typing.Type[ToValueTuple_12_T9], typing.Type[ToValueTuple_12_T10], typing.Type[ToValueTuple_12_T11], typing.Type[ToValueTuple_12_T12]]) -> ToValueTuple_12[ToValueTuple_12_T1, ToValueTuple_12_T2, ToValueTuple_12_T3, ToValueTuple_12_T4, ToValueTuple_12_T5, ToValueTuple_12_T6, ToValueTuple_12_T7, ToValueTuple_12_T8, ToValueTuple_12_T9, ToValueTuple_12_T10, ToValueTuple_12_T11, ToValueTuple_12_T12]: ...

        ToValueTuple_12_T1 = typing.TypeVar('ToValueTuple_12_T1')
        ToValueTuple_12_T2 = typing.TypeVar('ToValueTuple_12_T2')
        ToValueTuple_12_T3 = typing.TypeVar('ToValueTuple_12_T3')
        ToValueTuple_12_T4 = typing.TypeVar('ToValueTuple_12_T4')
        ToValueTuple_12_T5 = typing.TypeVar('ToValueTuple_12_T5')
        ToValueTuple_12_T6 = typing.TypeVar('ToValueTuple_12_T6')
        ToValueTuple_12_T7 = typing.TypeVar('ToValueTuple_12_T7')
        ToValueTuple_12_T8 = typing.TypeVar('ToValueTuple_12_T8')
        ToValueTuple_12_T9 = typing.TypeVar('ToValueTuple_12_T9')
        ToValueTuple_12_T10 = typing.TypeVar('ToValueTuple_12_T10')
        ToValueTuple_12_T11 = typing.TypeVar('ToValueTuple_12_T11')
        ToValueTuple_12_T12 = typing.TypeVar('ToValueTuple_12_T12')
        class ToValueTuple_12(typing.Generic[ToValueTuple_12_T1, ToValueTuple_12_T2, ToValueTuple_12_T3, ToValueTuple_12_T4, ToValueTuple_12_T5, ToValueTuple_12_T6, ToValueTuple_12_T7, ToValueTuple_12_T8, ToValueTuple_12_T9, ToValueTuple_12_T10, ToValueTuple_12_T11, ToValueTuple_12_T12]):
            ToValueTuple_12_T1 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_12_T1
            ToValueTuple_12_T2 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_12_T2
            ToValueTuple_12_T3 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_12_T3
            ToValueTuple_12_T4 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_12_T4
            ToValueTuple_12_T5 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_12_T5
            ToValueTuple_12_T6 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_12_T6
            ToValueTuple_12_T7 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_12_T7
            ToValueTuple_12_T8 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_12_T8
            ToValueTuple_12_T9 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_12_T9
            ToValueTuple_12_T10 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_12_T10
            ToValueTuple_12_T11 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_12_T11
            ToValueTuple_12_T12 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_12_T12
            def __call__(self, value: Tuple_8[ToValueTuple_12_T1, ToValueTuple_12_T2, ToValueTuple_12_T3, ToValueTuple_12_T4, ToValueTuple_12_T5, ToValueTuple_12_T6, ToValueTuple_12_T7, Tuple_5[ToValueTuple_12_T8, ToValueTuple_12_T9, ToValueTuple_12_T10, ToValueTuple_12_T11, ToValueTuple_12_T12]]) -> ValueTuple_8[ToValueTuple_12_T1, ToValueTuple_12_T2, ToValueTuple_12_T3, ToValueTuple_12_T4, ToValueTuple_12_T5, ToValueTuple_12_T6, ToValueTuple_12_T7, ValueTuple_5[ToValueTuple_12_T8, ToValueTuple_12_T9, ToValueTuple_12_T10, ToValueTuple_12_T11, ToValueTuple_12_T12]]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[ToValueTuple_13_T1], typing.Type[ToValueTuple_13_T2], typing.Type[ToValueTuple_13_T3], typing.Type[ToValueTuple_13_T4], typing.Type[ToValueTuple_13_T5], typing.Type[ToValueTuple_13_T6], typing.Type[ToValueTuple_13_T7], typing.Type[ToValueTuple_13_T8], typing.Type[ToValueTuple_13_T9], typing.Type[ToValueTuple_13_T10], typing.Type[ToValueTuple_13_T11], typing.Type[ToValueTuple_13_T12], typing.Type[ToValueTuple_13_T13]]) -> ToValueTuple_13[ToValueTuple_13_T1, ToValueTuple_13_T2, ToValueTuple_13_T3, ToValueTuple_13_T4, ToValueTuple_13_T5, ToValueTuple_13_T6, ToValueTuple_13_T7, ToValueTuple_13_T8, ToValueTuple_13_T9, ToValueTuple_13_T10, ToValueTuple_13_T11, ToValueTuple_13_T12, ToValueTuple_13_T13]: ...

        ToValueTuple_13_T1 = typing.TypeVar('ToValueTuple_13_T1')
        ToValueTuple_13_T2 = typing.TypeVar('ToValueTuple_13_T2')
        ToValueTuple_13_T3 = typing.TypeVar('ToValueTuple_13_T3')
        ToValueTuple_13_T4 = typing.TypeVar('ToValueTuple_13_T4')
        ToValueTuple_13_T5 = typing.TypeVar('ToValueTuple_13_T5')
        ToValueTuple_13_T6 = typing.TypeVar('ToValueTuple_13_T6')
        ToValueTuple_13_T7 = typing.TypeVar('ToValueTuple_13_T7')
        ToValueTuple_13_T8 = typing.TypeVar('ToValueTuple_13_T8')
        ToValueTuple_13_T9 = typing.TypeVar('ToValueTuple_13_T9')
        ToValueTuple_13_T10 = typing.TypeVar('ToValueTuple_13_T10')
        ToValueTuple_13_T11 = typing.TypeVar('ToValueTuple_13_T11')
        ToValueTuple_13_T12 = typing.TypeVar('ToValueTuple_13_T12')
        ToValueTuple_13_T13 = typing.TypeVar('ToValueTuple_13_T13')
        class ToValueTuple_13(typing.Generic[ToValueTuple_13_T1, ToValueTuple_13_T2, ToValueTuple_13_T3, ToValueTuple_13_T4, ToValueTuple_13_T5, ToValueTuple_13_T6, ToValueTuple_13_T7, ToValueTuple_13_T8, ToValueTuple_13_T9, ToValueTuple_13_T10, ToValueTuple_13_T11, ToValueTuple_13_T12, ToValueTuple_13_T13]):
            ToValueTuple_13_T1 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_13_T1
            ToValueTuple_13_T2 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_13_T2
            ToValueTuple_13_T3 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_13_T3
            ToValueTuple_13_T4 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_13_T4
            ToValueTuple_13_T5 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_13_T5
            ToValueTuple_13_T6 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_13_T6
            ToValueTuple_13_T7 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_13_T7
            ToValueTuple_13_T8 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_13_T8
            ToValueTuple_13_T9 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_13_T9
            ToValueTuple_13_T10 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_13_T10
            ToValueTuple_13_T11 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_13_T11
            ToValueTuple_13_T12 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_13_T12
            ToValueTuple_13_T13 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_13_T13
            def __call__(self, value: Tuple_8[ToValueTuple_13_T1, ToValueTuple_13_T2, ToValueTuple_13_T3, ToValueTuple_13_T4, ToValueTuple_13_T5, ToValueTuple_13_T6, ToValueTuple_13_T7, Tuple_6[ToValueTuple_13_T8, ToValueTuple_13_T9, ToValueTuple_13_T10, ToValueTuple_13_T11, ToValueTuple_13_T12, ToValueTuple_13_T13]]) -> ValueTuple_8[ToValueTuple_13_T1, ToValueTuple_13_T2, ToValueTuple_13_T3, ToValueTuple_13_T4, ToValueTuple_13_T5, ToValueTuple_13_T6, ToValueTuple_13_T7, ValueTuple_6[ToValueTuple_13_T8, ToValueTuple_13_T9, ToValueTuple_13_T10, ToValueTuple_13_T11, ToValueTuple_13_T12, ToValueTuple_13_T13]]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[ToValueTuple_14_T1], typing.Type[ToValueTuple_14_T2], typing.Type[ToValueTuple_14_T3], typing.Type[ToValueTuple_14_T4], typing.Type[ToValueTuple_14_T5], typing.Type[ToValueTuple_14_T6], typing.Type[ToValueTuple_14_T7], typing.Type[ToValueTuple_14_T8], typing.Type[ToValueTuple_14_T9], typing.Type[ToValueTuple_14_T10], typing.Type[ToValueTuple_14_T11], typing.Type[ToValueTuple_14_T12], typing.Type[ToValueTuple_14_T13], typing.Type[ToValueTuple_14_T14]]) -> ToValueTuple_14[ToValueTuple_14_T1, ToValueTuple_14_T2, ToValueTuple_14_T3, ToValueTuple_14_T4, ToValueTuple_14_T5, ToValueTuple_14_T6, ToValueTuple_14_T7, ToValueTuple_14_T8, ToValueTuple_14_T9, ToValueTuple_14_T10, ToValueTuple_14_T11, ToValueTuple_14_T12, ToValueTuple_14_T13, ToValueTuple_14_T14]: ...

        ToValueTuple_14_T1 = typing.TypeVar('ToValueTuple_14_T1')
        ToValueTuple_14_T2 = typing.TypeVar('ToValueTuple_14_T2')
        ToValueTuple_14_T3 = typing.TypeVar('ToValueTuple_14_T3')
        ToValueTuple_14_T4 = typing.TypeVar('ToValueTuple_14_T4')
        ToValueTuple_14_T5 = typing.TypeVar('ToValueTuple_14_T5')
        ToValueTuple_14_T6 = typing.TypeVar('ToValueTuple_14_T6')
        ToValueTuple_14_T7 = typing.TypeVar('ToValueTuple_14_T7')
        ToValueTuple_14_T8 = typing.TypeVar('ToValueTuple_14_T8')
        ToValueTuple_14_T9 = typing.TypeVar('ToValueTuple_14_T9')
        ToValueTuple_14_T10 = typing.TypeVar('ToValueTuple_14_T10')
        ToValueTuple_14_T11 = typing.TypeVar('ToValueTuple_14_T11')
        ToValueTuple_14_T12 = typing.TypeVar('ToValueTuple_14_T12')
        ToValueTuple_14_T13 = typing.TypeVar('ToValueTuple_14_T13')
        ToValueTuple_14_T14 = typing.TypeVar('ToValueTuple_14_T14')
        class ToValueTuple_14(typing.Generic[ToValueTuple_14_T1, ToValueTuple_14_T2, ToValueTuple_14_T3, ToValueTuple_14_T4, ToValueTuple_14_T5, ToValueTuple_14_T6, ToValueTuple_14_T7, ToValueTuple_14_T8, ToValueTuple_14_T9, ToValueTuple_14_T10, ToValueTuple_14_T11, ToValueTuple_14_T12, ToValueTuple_14_T13, ToValueTuple_14_T14]):
            ToValueTuple_14_T1 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_14_T1
            ToValueTuple_14_T2 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_14_T2
            ToValueTuple_14_T3 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_14_T3
            ToValueTuple_14_T4 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_14_T4
            ToValueTuple_14_T5 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_14_T5
            ToValueTuple_14_T6 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_14_T6
            ToValueTuple_14_T7 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_14_T7
            ToValueTuple_14_T8 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_14_T8
            ToValueTuple_14_T9 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_14_T9
            ToValueTuple_14_T10 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_14_T10
            ToValueTuple_14_T11 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_14_T11
            ToValueTuple_14_T12 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_14_T12
            ToValueTuple_14_T13 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_14_T13
            ToValueTuple_14_T14 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_14_T14
            def __call__(self, value: Tuple_8[ToValueTuple_14_T1, ToValueTuple_14_T2, ToValueTuple_14_T3, ToValueTuple_14_T4, ToValueTuple_14_T5, ToValueTuple_14_T6, ToValueTuple_14_T7, Tuple_7[ToValueTuple_14_T8, ToValueTuple_14_T9, ToValueTuple_14_T10, ToValueTuple_14_T11, ToValueTuple_14_T12, ToValueTuple_14_T13, ToValueTuple_14_T14]]) -> ValueTuple_8[ToValueTuple_14_T1, ToValueTuple_14_T2, ToValueTuple_14_T3, ToValueTuple_14_T4, ToValueTuple_14_T5, ToValueTuple_14_T6, ToValueTuple_14_T7, ValueTuple_7[ToValueTuple_14_T8, ToValueTuple_14_T9, ToValueTuple_14_T10, ToValueTuple_14_T11, ToValueTuple_14_T12, ToValueTuple_14_T13, ToValueTuple_14_T14]]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[ToValueTuple_15_T1], typing.Type[ToValueTuple_15_T2], typing.Type[ToValueTuple_15_T3], typing.Type[ToValueTuple_15_T4], typing.Type[ToValueTuple_15_T5], typing.Type[ToValueTuple_15_T6], typing.Type[ToValueTuple_15_T7], typing.Type[ToValueTuple_15_T8], typing.Type[ToValueTuple_15_T9], typing.Type[ToValueTuple_15_T10], typing.Type[ToValueTuple_15_T11], typing.Type[ToValueTuple_15_T12], typing.Type[ToValueTuple_15_T13], typing.Type[ToValueTuple_15_T14], typing.Type[ToValueTuple_15_T15]]) -> ToValueTuple_15[ToValueTuple_15_T1, ToValueTuple_15_T2, ToValueTuple_15_T3, ToValueTuple_15_T4, ToValueTuple_15_T5, ToValueTuple_15_T6, ToValueTuple_15_T7, ToValueTuple_15_T8, ToValueTuple_15_T9, ToValueTuple_15_T10, ToValueTuple_15_T11, ToValueTuple_15_T12, ToValueTuple_15_T13, ToValueTuple_15_T14, ToValueTuple_15_T15]: ...

        ToValueTuple_15_T1 = typing.TypeVar('ToValueTuple_15_T1')
        ToValueTuple_15_T2 = typing.TypeVar('ToValueTuple_15_T2')
        ToValueTuple_15_T3 = typing.TypeVar('ToValueTuple_15_T3')
        ToValueTuple_15_T4 = typing.TypeVar('ToValueTuple_15_T4')
        ToValueTuple_15_T5 = typing.TypeVar('ToValueTuple_15_T5')
        ToValueTuple_15_T6 = typing.TypeVar('ToValueTuple_15_T6')
        ToValueTuple_15_T7 = typing.TypeVar('ToValueTuple_15_T7')
        ToValueTuple_15_T8 = typing.TypeVar('ToValueTuple_15_T8')
        ToValueTuple_15_T9 = typing.TypeVar('ToValueTuple_15_T9')
        ToValueTuple_15_T10 = typing.TypeVar('ToValueTuple_15_T10')
        ToValueTuple_15_T11 = typing.TypeVar('ToValueTuple_15_T11')
        ToValueTuple_15_T12 = typing.TypeVar('ToValueTuple_15_T12')
        ToValueTuple_15_T13 = typing.TypeVar('ToValueTuple_15_T13')
        ToValueTuple_15_T14 = typing.TypeVar('ToValueTuple_15_T14')
        ToValueTuple_15_T15 = typing.TypeVar('ToValueTuple_15_T15')
        class ToValueTuple_15(typing.Generic[ToValueTuple_15_T1, ToValueTuple_15_T2, ToValueTuple_15_T3, ToValueTuple_15_T4, ToValueTuple_15_T5, ToValueTuple_15_T6, ToValueTuple_15_T7, ToValueTuple_15_T8, ToValueTuple_15_T9, ToValueTuple_15_T10, ToValueTuple_15_T11, ToValueTuple_15_T12, ToValueTuple_15_T13, ToValueTuple_15_T14, ToValueTuple_15_T15]):
            ToValueTuple_15_T1 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_15_T1
            ToValueTuple_15_T2 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_15_T2
            ToValueTuple_15_T3 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_15_T3
            ToValueTuple_15_T4 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_15_T4
            ToValueTuple_15_T5 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_15_T5
            ToValueTuple_15_T6 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_15_T6
            ToValueTuple_15_T7 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_15_T7
            ToValueTuple_15_T8 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_15_T8
            ToValueTuple_15_T9 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_15_T9
            ToValueTuple_15_T10 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_15_T10
            ToValueTuple_15_T11 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_15_T11
            ToValueTuple_15_T12 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_15_T12
            ToValueTuple_15_T13 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_15_T13
            ToValueTuple_15_T14 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_15_T14
            ToValueTuple_15_T15 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_15_T15
            def __call__(self, value: Tuple_8[ToValueTuple_15_T1, ToValueTuple_15_T2, ToValueTuple_15_T3, ToValueTuple_15_T4, ToValueTuple_15_T5, ToValueTuple_15_T6, ToValueTuple_15_T7, Tuple_8[ToValueTuple_15_T8, ToValueTuple_15_T9, ToValueTuple_15_T10, ToValueTuple_15_T11, ToValueTuple_15_T12, ToValueTuple_15_T13, ToValueTuple_15_T14, Tuple_1[ToValueTuple_15_T15]]]) -> ValueTuple_8[ToValueTuple_15_T1, ToValueTuple_15_T2, ToValueTuple_15_T3, ToValueTuple_15_T4, ToValueTuple_15_T5, ToValueTuple_15_T6, ToValueTuple_15_T7, ValueTuple_8[ToValueTuple_15_T8, ToValueTuple_15_T9, ToValueTuple_15_T10, ToValueTuple_15_T11, ToValueTuple_15_T12, ToValueTuple_15_T13, ToValueTuple_15_T14, ValueTuple_1[ToValueTuple_15_T15]]]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[ToValueTuple_16_T1], typing.Type[ToValueTuple_16_T2], typing.Type[ToValueTuple_16_T3], typing.Type[ToValueTuple_16_T4], typing.Type[ToValueTuple_16_T5], typing.Type[ToValueTuple_16_T6], typing.Type[ToValueTuple_16_T7], typing.Type[ToValueTuple_16_T8], typing.Type[ToValueTuple_16_T9], typing.Type[ToValueTuple_16_T10], typing.Type[ToValueTuple_16_T11], typing.Type[ToValueTuple_16_T12], typing.Type[ToValueTuple_16_T13], typing.Type[ToValueTuple_16_T14], typing.Type[ToValueTuple_16_T15], typing.Type[ToValueTuple_16_T16]]) -> ToValueTuple_16[ToValueTuple_16_T1, ToValueTuple_16_T2, ToValueTuple_16_T3, ToValueTuple_16_T4, ToValueTuple_16_T5, ToValueTuple_16_T6, ToValueTuple_16_T7, ToValueTuple_16_T8, ToValueTuple_16_T9, ToValueTuple_16_T10, ToValueTuple_16_T11, ToValueTuple_16_T12, ToValueTuple_16_T13, ToValueTuple_16_T14, ToValueTuple_16_T15, ToValueTuple_16_T16]: ...

        ToValueTuple_16_T1 = typing.TypeVar('ToValueTuple_16_T1')
        ToValueTuple_16_T2 = typing.TypeVar('ToValueTuple_16_T2')
        ToValueTuple_16_T3 = typing.TypeVar('ToValueTuple_16_T3')
        ToValueTuple_16_T4 = typing.TypeVar('ToValueTuple_16_T4')
        ToValueTuple_16_T5 = typing.TypeVar('ToValueTuple_16_T5')
        ToValueTuple_16_T6 = typing.TypeVar('ToValueTuple_16_T6')
        ToValueTuple_16_T7 = typing.TypeVar('ToValueTuple_16_T7')
        ToValueTuple_16_T8 = typing.TypeVar('ToValueTuple_16_T8')
        ToValueTuple_16_T9 = typing.TypeVar('ToValueTuple_16_T9')
        ToValueTuple_16_T10 = typing.TypeVar('ToValueTuple_16_T10')
        ToValueTuple_16_T11 = typing.TypeVar('ToValueTuple_16_T11')
        ToValueTuple_16_T12 = typing.TypeVar('ToValueTuple_16_T12')
        ToValueTuple_16_T13 = typing.TypeVar('ToValueTuple_16_T13')
        ToValueTuple_16_T14 = typing.TypeVar('ToValueTuple_16_T14')
        ToValueTuple_16_T15 = typing.TypeVar('ToValueTuple_16_T15')
        ToValueTuple_16_T16 = typing.TypeVar('ToValueTuple_16_T16')
        class ToValueTuple_16(typing.Generic[ToValueTuple_16_T1, ToValueTuple_16_T2, ToValueTuple_16_T3, ToValueTuple_16_T4, ToValueTuple_16_T5, ToValueTuple_16_T6, ToValueTuple_16_T7, ToValueTuple_16_T8, ToValueTuple_16_T9, ToValueTuple_16_T10, ToValueTuple_16_T11, ToValueTuple_16_T12, ToValueTuple_16_T13, ToValueTuple_16_T14, ToValueTuple_16_T15, ToValueTuple_16_T16]):
            ToValueTuple_16_T1 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_16_T1
            ToValueTuple_16_T2 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_16_T2
            ToValueTuple_16_T3 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_16_T3
            ToValueTuple_16_T4 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_16_T4
            ToValueTuple_16_T5 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_16_T5
            ToValueTuple_16_T6 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_16_T6
            ToValueTuple_16_T7 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_16_T7
            ToValueTuple_16_T8 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_16_T8
            ToValueTuple_16_T9 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_16_T9
            ToValueTuple_16_T10 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_16_T10
            ToValueTuple_16_T11 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_16_T11
            ToValueTuple_16_T12 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_16_T12
            ToValueTuple_16_T13 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_16_T13
            ToValueTuple_16_T14 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_16_T14
            ToValueTuple_16_T15 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_16_T15
            ToValueTuple_16_T16 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_16_T16
            def __call__(self, value: Tuple_8[ToValueTuple_16_T1, ToValueTuple_16_T2, ToValueTuple_16_T3, ToValueTuple_16_T4, ToValueTuple_16_T5, ToValueTuple_16_T6, ToValueTuple_16_T7, Tuple_8[ToValueTuple_16_T8, ToValueTuple_16_T9, ToValueTuple_16_T10, ToValueTuple_16_T11, ToValueTuple_16_T12, ToValueTuple_16_T13, ToValueTuple_16_T14, Tuple_2[ToValueTuple_16_T15, ToValueTuple_16_T16]]]) -> ValueTuple_8[ToValueTuple_16_T1, ToValueTuple_16_T2, ToValueTuple_16_T3, ToValueTuple_16_T4, ToValueTuple_16_T5, ToValueTuple_16_T6, ToValueTuple_16_T7, ValueTuple_8[ToValueTuple_16_T8, ToValueTuple_16_T9, ToValueTuple_16_T10, ToValueTuple_16_T11, ToValueTuple_16_T12, ToValueTuple_16_T13, ToValueTuple_16_T14, ValueTuple_2[ToValueTuple_16_T15, ToValueTuple_16_T16]]]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[ToValueTuple_17_T1], typing.Type[ToValueTuple_17_T2], typing.Type[ToValueTuple_17_T3], typing.Type[ToValueTuple_17_T4], typing.Type[ToValueTuple_17_T5], typing.Type[ToValueTuple_17_T6], typing.Type[ToValueTuple_17_T7], typing.Type[ToValueTuple_17_T8], typing.Type[ToValueTuple_17_T9], typing.Type[ToValueTuple_17_T10], typing.Type[ToValueTuple_17_T11], typing.Type[ToValueTuple_17_T12], typing.Type[ToValueTuple_17_T13], typing.Type[ToValueTuple_17_T14], typing.Type[ToValueTuple_17_T15], typing.Type[ToValueTuple_17_T16], typing.Type[ToValueTuple_17_T17]]) -> ToValueTuple_17[ToValueTuple_17_T1, ToValueTuple_17_T2, ToValueTuple_17_T3, ToValueTuple_17_T4, ToValueTuple_17_T5, ToValueTuple_17_T6, ToValueTuple_17_T7, ToValueTuple_17_T8, ToValueTuple_17_T9, ToValueTuple_17_T10, ToValueTuple_17_T11, ToValueTuple_17_T12, ToValueTuple_17_T13, ToValueTuple_17_T14, ToValueTuple_17_T15, ToValueTuple_17_T16, ToValueTuple_17_T17]: ...

        ToValueTuple_17_T1 = typing.TypeVar('ToValueTuple_17_T1')
        ToValueTuple_17_T2 = typing.TypeVar('ToValueTuple_17_T2')
        ToValueTuple_17_T3 = typing.TypeVar('ToValueTuple_17_T3')
        ToValueTuple_17_T4 = typing.TypeVar('ToValueTuple_17_T4')
        ToValueTuple_17_T5 = typing.TypeVar('ToValueTuple_17_T5')
        ToValueTuple_17_T6 = typing.TypeVar('ToValueTuple_17_T6')
        ToValueTuple_17_T7 = typing.TypeVar('ToValueTuple_17_T7')
        ToValueTuple_17_T8 = typing.TypeVar('ToValueTuple_17_T8')
        ToValueTuple_17_T9 = typing.TypeVar('ToValueTuple_17_T9')
        ToValueTuple_17_T10 = typing.TypeVar('ToValueTuple_17_T10')
        ToValueTuple_17_T11 = typing.TypeVar('ToValueTuple_17_T11')
        ToValueTuple_17_T12 = typing.TypeVar('ToValueTuple_17_T12')
        ToValueTuple_17_T13 = typing.TypeVar('ToValueTuple_17_T13')
        ToValueTuple_17_T14 = typing.TypeVar('ToValueTuple_17_T14')
        ToValueTuple_17_T15 = typing.TypeVar('ToValueTuple_17_T15')
        ToValueTuple_17_T16 = typing.TypeVar('ToValueTuple_17_T16')
        ToValueTuple_17_T17 = typing.TypeVar('ToValueTuple_17_T17')
        class ToValueTuple_17(typing.Generic[ToValueTuple_17_T1, ToValueTuple_17_T2, ToValueTuple_17_T3, ToValueTuple_17_T4, ToValueTuple_17_T5, ToValueTuple_17_T6, ToValueTuple_17_T7, ToValueTuple_17_T8, ToValueTuple_17_T9, ToValueTuple_17_T10, ToValueTuple_17_T11, ToValueTuple_17_T12, ToValueTuple_17_T13, ToValueTuple_17_T14, ToValueTuple_17_T15, ToValueTuple_17_T16, ToValueTuple_17_T17]):
            ToValueTuple_17_T1 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_17_T1
            ToValueTuple_17_T2 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_17_T2
            ToValueTuple_17_T3 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_17_T3
            ToValueTuple_17_T4 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_17_T4
            ToValueTuple_17_T5 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_17_T5
            ToValueTuple_17_T6 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_17_T6
            ToValueTuple_17_T7 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_17_T7
            ToValueTuple_17_T8 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_17_T8
            ToValueTuple_17_T9 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_17_T9
            ToValueTuple_17_T10 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_17_T10
            ToValueTuple_17_T11 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_17_T11
            ToValueTuple_17_T12 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_17_T12
            ToValueTuple_17_T13 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_17_T13
            ToValueTuple_17_T14 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_17_T14
            ToValueTuple_17_T15 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_17_T15
            ToValueTuple_17_T16 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_17_T16
            ToValueTuple_17_T17 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_17_T17
            def __call__(self, value: Tuple_8[ToValueTuple_17_T1, ToValueTuple_17_T2, ToValueTuple_17_T3, ToValueTuple_17_T4, ToValueTuple_17_T5, ToValueTuple_17_T6, ToValueTuple_17_T7, Tuple_8[ToValueTuple_17_T8, ToValueTuple_17_T9, ToValueTuple_17_T10, ToValueTuple_17_T11, ToValueTuple_17_T12, ToValueTuple_17_T13, ToValueTuple_17_T14, Tuple_3[ToValueTuple_17_T15, ToValueTuple_17_T16, ToValueTuple_17_T17]]]) -> ValueTuple_8[ToValueTuple_17_T1, ToValueTuple_17_T2, ToValueTuple_17_T3, ToValueTuple_17_T4, ToValueTuple_17_T5, ToValueTuple_17_T6, ToValueTuple_17_T7, ValueTuple_8[ToValueTuple_17_T8, ToValueTuple_17_T9, ToValueTuple_17_T10, ToValueTuple_17_T11, ToValueTuple_17_T12, ToValueTuple_17_T13, ToValueTuple_17_T14, ValueTuple_3[ToValueTuple_17_T15, ToValueTuple_17_T16, ToValueTuple_17_T17]]]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[ToValueTuple_18_T1], typing.Type[ToValueTuple_18_T2], typing.Type[ToValueTuple_18_T3], typing.Type[ToValueTuple_18_T4], typing.Type[ToValueTuple_18_T5], typing.Type[ToValueTuple_18_T6], typing.Type[ToValueTuple_18_T7], typing.Type[ToValueTuple_18_T8], typing.Type[ToValueTuple_18_T9], typing.Type[ToValueTuple_18_T10], typing.Type[ToValueTuple_18_T11], typing.Type[ToValueTuple_18_T12], typing.Type[ToValueTuple_18_T13], typing.Type[ToValueTuple_18_T14], typing.Type[ToValueTuple_18_T15], typing.Type[ToValueTuple_18_T16], typing.Type[ToValueTuple_18_T17], typing.Type[ToValueTuple_18_T18]]) -> ToValueTuple_18[ToValueTuple_18_T1, ToValueTuple_18_T2, ToValueTuple_18_T3, ToValueTuple_18_T4, ToValueTuple_18_T5, ToValueTuple_18_T6, ToValueTuple_18_T7, ToValueTuple_18_T8, ToValueTuple_18_T9, ToValueTuple_18_T10, ToValueTuple_18_T11, ToValueTuple_18_T12, ToValueTuple_18_T13, ToValueTuple_18_T14, ToValueTuple_18_T15, ToValueTuple_18_T16, ToValueTuple_18_T17, ToValueTuple_18_T18]: ...

        ToValueTuple_18_T1 = typing.TypeVar('ToValueTuple_18_T1')
        ToValueTuple_18_T2 = typing.TypeVar('ToValueTuple_18_T2')
        ToValueTuple_18_T3 = typing.TypeVar('ToValueTuple_18_T3')
        ToValueTuple_18_T4 = typing.TypeVar('ToValueTuple_18_T4')
        ToValueTuple_18_T5 = typing.TypeVar('ToValueTuple_18_T5')
        ToValueTuple_18_T6 = typing.TypeVar('ToValueTuple_18_T6')
        ToValueTuple_18_T7 = typing.TypeVar('ToValueTuple_18_T7')
        ToValueTuple_18_T8 = typing.TypeVar('ToValueTuple_18_T8')
        ToValueTuple_18_T9 = typing.TypeVar('ToValueTuple_18_T9')
        ToValueTuple_18_T10 = typing.TypeVar('ToValueTuple_18_T10')
        ToValueTuple_18_T11 = typing.TypeVar('ToValueTuple_18_T11')
        ToValueTuple_18_T12 = typing.TypeVar('ToValueTuple_18_T12')
        ToValueTuple_18_T13 = typing.TypeVar('ToValueTuple_18_T13')
        ToValueTuple_18_T14 = typing.TypeVar('ToValueTuple_18_T14')
        ToValueTuple_18_T15 = typing.TypeVar('ToValueTuple_18_T15')
        ToValueTuple_18_T16 = typing.TypeVar('ToValueTuple_18_T16')
        ToValueTuple_18_T17 = typing.TypeVar('ToValueTuple_18_T17')
        ToValueTuple_18_T18 = typing.TypeVar('ToValueTuple_18_T18')
        class ToValueTuple_18(typing.Generic[ToValueTuple_18_T1, ToValueTuple_18_T2, ToValueTuple_18_T3, ToValueTuple_18_T4, ToValueTuple_18_T5, ToValueTuple_18_T6, ToValueTuple_18_T7, ToValueTuple_18_T8, ToValueTuple_18_T9, ToValueTuple_18_T10, ToValueTuple_18_T11, ToValueTuple_18_T12, ToValueTuple_18_T13, ToValueTuple_18_T14, ToValueTuple_18_T15, ToValueTuple_18_T16, ToValueTuple_18_T17, ToValueTuple_18_T18]):
            ToValueTuple_18_T1 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_18_T1
            ToValueTuple_18_T2 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_18_T2
            ToValueTuple_18_T3 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_18_T3
            ToValueTuple_18_T4 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_18_T4
            ToValueTuple_18_T5 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_18_T5
            ToValueTuple_18_T6 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_18_T6
            ToValueTuple_18_T7 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_18_T7
            ToValueTuple_18_T8 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_18_T8
            ToValueTuple_18_T9 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_18_T9
            ToValueTuple_18_T10 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_18_T10
            ToValueTuple_18_T11 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_18_T11
            ToValueTuple_18_T12 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_18_T12
            ToValueTuple_18_T13 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_18_T13
            ToValueTuple_18_T14 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_18_T14
            ToValueTuple_18_T15 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_18_T15
            ToValueTuple_18_T16 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_18_T16
            ToValueTuple_18_T17 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_18_T17
            ToValueTuple_18_T18 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_18_T18
            def __call__(self, value: Tuple_8[ToValueTuple_18_T1, ToValueTuple_18_T2, ToValueTuple_18_T3, ToValueTuple_18_T4, ToValueTuple_18_T5, ToValueTuple_18_T6, ToValueTuple_18_T7, Tuple_8[ToValueTuple_18_T8, ToValueTuple_18_T9, ToValueTuple_18_T10, ToValueTuple_18_T11, ToValueTuple_18_T12, ToValueTuple_18_T13, ToValueTuple_18_T14, Tuple_4[ToValueTuple_18_T15, ToValueTuple_18_T16, ToValueTuple_18_T17, ToValueTuple_18_T18]]]) -> ValueTuple_8[ToValueTuple_18_T1, ToValueTuple_18_T2, ToValueTuple_18_T3, ToValueTuple_18_T4, ToValueTuple_18_T5, ToValueTuple_18_T6, ToValueTuple_18_T7, ValueTuple_8[ToValueTuple_18_T8, ToValueTuple_18_T9, ToValueTuple_18_T10, ToValueTuple_18_T11, ToValueTuple_18_T12, ToValueTuple_18_T13, ToValueTuple_18_T14, ValueTuple_4[ToValueTuple_18_T15, ToValueTuple_18_T16, ToValueTuple_18_T17, ToValueTuple_18_T18]]]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[ToValueTuple_19_T1], typing.Type[ToValueTuple_19_T2], typing.Type[ToValueTuple_19_T3], typing.Type[ToValueTuple_19_T4], typing.Type[ToValueTuple_19_T5], typing.Type[ToValueTuple_19_T6], typing.Type[ToValueTuple_19_T7], typing.Type[ToValueTuple_19_T8], typing.Type[ToValueTuple_19_T9], typing.Type[ToValueTuple_19_T10], typing.Type[ToValueTuple_19_T11], typing.Type[ToValueTuple_19_T12], typing.Type[ToValueTuple_19_T13], typing.Type[ToValueTuple_19_T14], typing.Type[ToValueTuple_19_T15], typing.Type[ToValueTuple_19_T16], typing.Type[ToValueTuple_19_T17], typing.Type[ToValueTuple_19_T18], typing.Type[ToValueTuple_19_T19]]) -> ToValueTuple_19[ToValueTuple_19_T1, ToValueTuple_19_T2, ToValueTuple_19_T3, ToValueTuple_19_T4, ToValueTuple_19_T5, ToValueTuple_19_T6, ToValueTuple_19_T7, ToValueTuple_19_T8, ToValueTuple_19_T9, ToValueTuple_19_T10, ToValueTuple_19_T11, ToValueTuple_19_T12, ToValueTuple_19_T13, ToValueTuple_19_T14, ToValueTuple_19_T15, ToValueTuple_19_T16, ToValueTuple_19_T17, ToValueTuple_19_T18, ToValueTuple_19_T19]: ...

        ToValueTuple_19_T1 = typing.TypeVar('ToValueTuple_19_T1')
        ToValueTuple_19_T2 = typing.TypeVar('ToValueTuple_19_T2')
        ToValueTuple_19_T3 = typing.TypeVar('ToValueTuple_19_T3')
        ToValueTuple_19_T4 = typing.TypeVar('ToValueTuple_19_T4')
        ToValueTuple_19_T5 = typing.TypeVar('ToValueTuple_19_T5')
        ToValueTuple_19_T6 = typing.TypeVar('ToValueTuple_19_T6')
        ToValueTuple_19_T7 = typing.TypeVar('ToValueTuple_19_T7')
        ToValueTuple_19_T8 = typing.TypeVar('ToValueTuple_19_T8')
        ToValueTuple_19_T9 = typing.TypeVar('ToValueTuple_19_T9')
        ToValueTuple_19_T10 = typing.TypeVar('ToValueTuple_19_T10')
        ToValueTuple_19_T11 = typing.TypeVar('ToValueTuple_19_T11')
        ToValueTuple_19_T12 = typing.TypeVar('ToValueTuple_19_T12')
        ToValueTuple_19_T13 = typing.TypeVar('ToValueTuple_19_T13')
        ToValueTuple_19_T14 = typing.TypeVar('ToValueTuple_19_T14')
        ToValueTuple_19_T15 = typing.TypeVar('ToValueTuple_19_T15')
        ToValueTuple_19_T16 = typing.TypeVar('ToValueTuple_19_T16')
        ToValueTuple_19_T17 = typing.TypeVar('ToValueTuple_19_T17')
        ToValueTuple_19_T18 = typing.TypeVar('ToValueTuple_19_T18')
        ToValueTuple_19_T19 = typing.TypeVar('ToValueTuple_19_T19')
        class ToValueTuple_19(typing.Generic[ToValueTuple_19_T1, ToValueTuple_19_T2, ToValueTuple_19_T3, ToValueTuple_19_T4, ToValueTuple_19_T5, ToValueTuple_19_T6, ToValueTuple_19_T7, ToValueTuple_19_T8, ToValueTuple_19_T9, ToValueTuple_19_T10, ToValueTuple_19_T11, ToValueTuple_19_T12, ToValueTuple_19_T13, ToValueTuple_19_T14, ToValueTuple_19_T15, ToValueTuple_19_T16, ToValueTuple_19_T17, ToValueTuple_19_T18, ToValueTuple_19_T19]):
            ToValueTuple_19_T1 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_19_T1
            ToValueTuple_19_T2 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_19_T2
            ToValueTuple_19_T3 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_19_T3
            ToValueTuple_19_T4 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_19_T4
            ToValueTuple_19_T5 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_19_T5
            ToValueTuple_19_T6 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_19_T6
            ToValueTuple_19_T7 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_19_T7
            ToValueTuple_19_T8 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_19_T8
            ToValueTuple_19_T9 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_19_T9
            ToValueTuple_19_T10 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_19_T10
            ToValueTuple_19_T11 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_19_T11
            ToValueTuple_19_T12 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_19_T12
            ToValueTuple_19_T13 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_19_T13
            ToValueTuple_19_T14 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_19_T14
            ToValueTuple_19_T15 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_19_T15
            ToValueTuple_19_T16 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_19_T16
            ToValueTuple_19_T17 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_19_T17
            ToValueTuple_19_T18 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_19_T18
            ToValueTuple_19_T19 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_19_T19
            def __call__(self, value: Tuple_8[ToValueTuple_19_T1, ToValueTuple_19_T2, ToValueTuple_19_T3, ToValueTuple_19_T4, ToValueTuple_19_T5, ToValueTuple_19_T6, ToValueTuple_19_T7, Tuple_8[ToValueTuple_19_T8, ToValueTuple_19_T9, ToValueTuple_19_T10, ToValueTuple_19_T11, ToValueTuple_19_T12, ToValueTuple_19_T13, ToValueTuple_19_T14, Tuple_5[ToValueTuple_19_T15, ToValueTuple_19_T16, ToValueTuple_19_T17, ToValueTuple_19_T18, ToValueTuple_19_T19]]]) -> ValueTuple_8[ToValueTuple_19_T1, ToValueTuple_19_T2, ToValueTuple_19_T3, ToValueTuple_19_T4, ToValueTuple_19_T5, ToValueTuple_19_T6, ToValueTuple_19_T7, ValueTuple_8[ToValueTuple_19_T8, ToValueTuple_19_T9, ToValueTuple_19_T10, ToValueTuple_19_T11, ToValueTuple_19_T12, ToValueTuple_19_T13, ToValueTuple_19_T14, ValueTuple_5[ToValueTuple_19_T15, ToValueTuple_19_T16, ToValueTuple_19_T17, ToValueTuple_19_T18, ToValueTuple_19_T19]]]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[ToValueTuple_20_T1], typing.Type[ToValueTuple_20_T2], typing.Type[ToValueTuple_20_T3], typing.Type[ToValueTuple_20_T4], typing.Type[ToValueTuple_20_T5], typing.Type[ToValueTuple_20_T6], typing.Type[ToValueTuple_20_T7], typing.Type[ToValueTuple_20_T8], typing.Type[ToValueTuple_20_T9], typing.Type[ToValueTuple_20_T10], typing.Type[ToValueTuple_20_T11], typing.Type[ToValueTuple_20_T12], typing.Type[ToValueTuple_20_T13], typing.Type[ToValueTuple_20_T14], typing.Type[ToValueTuple_20_T15], typing.Type[ToValueTuple_20_T16], typing.Type[ToValueTuple_20_T17], typing.Type[ToValueTuple_20_T18], typing.Type[ToValueTuple_20_T19], typing.Type[ToValueTuple_20_T20]]) -> ToValueTuple_20[ToValueTuple_20_T1, ToValueTuple_20_T2, ToValueTuple_20_T3, ToValueTuple_20_T4, ToValueTuple_20_T5, ToValueTuple_20_T6, ToValueTuple_20_T7, ToValueTuple_20_T8, ToValueTuple_20_T9, ToValueTuple_20_T10, ToValueTuple_20_T11, ToValueTuple_20_T12, ToValueTuple_20_T13, ToValueTuple_20_T14, ToValueTuple_20_T15, ToValueTuple_20_T16, ToValueTuple_20_T17, ToValueTuple_20_T18, ToValueTuple_20_T19, ToValueTuple_20_T20]: ...

        ToValueTuple_20_T1 = typing.TypeVar('ToValueTuple_20_T1')
        ToValueTuple_20_T2 = typing.TypeVar('ToValueTuple_20_T2')
        ToValueTuple_20_T3 = typing.TypeVar('ToValueTuple_20_T3')
        ToValueTuple_20_T4 = typing.TypeVar('ToValueTuple_20_T4')
        ToValueTuple_20_T5 = typing.TypeVar('ToValueTuple_20_T5')
        ToValueTuple_20_T6 = typing.TypeVar('ToValueTuple_20_T6')
        ToValueTuple_20_T7 = typing.TypeVar('ToValueTuple_20_T7')
        ToValueTuple_20_T8 = typing.TypeVar('ToValueTuple_20_T8')
        ToValueTuple_20_T9 = typing.TypeVar('ToValueTuple_20_T9')
        ToValueTuple_20_T10 = typing.TypeVar('ToValueTuple_20_T10')
        ToValueTuple_20_T11 = typing.TypeVar('ToValueTuple_20_T11')
        ToValueTuple_20_T12 = typing.TypeVar('ToValueTuple_20_T12')
        ToValueTuple_20_T13 = typing.TypeVar('ToValueTuple_20_T13')
        ToValueTuple_20_T14 = typing.TypeVar('ToValueTuple_20_T14')
        ToValueTuple_20_T15 = typing.TypeVar('ToValueTuple_20_T15')
        ToValueTuple_20_T16 = typing.TypeVar('ToValueTuple_20_T16')
        ToValueTuple_20_T17 = typing.TypeVar('ToValueTuple_20_T17')
        ToValueTuple_20_T18 = typing.TypeVar('ToValueTuple_20_T18')
        ToValueTuple_20_T19 = typing.TypeVar('ToValueTuple_20_T19')
        ToValueTuple_20_T20 = typing.TypeVar('ToValueTuple_20_T20')
        class ToValueTuple_20(typing.Generic[ToValueTuple_20_T1, ToValueTuple_20_T2, ToValueTuple_20_T3, ToValueTuple_20_T4, ToValueTuple_20_T5, ToValueTuple_20_T6, ToValueTuple_20_T7, ToValueTuple_20_T8, ToValueTuple_20_T9, ToValueTuple_20_T10, ToValueTuple_20_T11, ToValueTuple_20_T12, ToValueTuple_20_T13, ToValueTuple_20_T14, ToValueTuple_20_T15, ToValueTuple_20_T16, ToValueTuple_20_T17, ToValueTuple_20_T18, ToValueTuple_20_T19, ToValueTuple_20_T20]):
            ToValueTuple_20_T1 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_20_T1
            ToValueTuple_20_T2 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_20_T2
            ToValueTuple_20_T3 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_20_T3
            ToValueTuple_20_T4 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_20_T4
            ToValueTuple_20_T5 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_20_T5
            ToValueTuple_20_T6 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_20_T6
            ToValueTuple_20_T7 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_20_T7
            ToValueTuple_20_T8 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_20_T8
            ToValueTuple_20_T9 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_20_T9
            ToValueTuple_20_T10 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_20_T10
            ToValueTuple_20_T11 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_20_T11
            ToValueTuple_20_T12 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_20_T12
            ToValueTuple_20_T13 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_20_T13
            ToValueTuple_20_T14 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_20_T14
            ToValueTuple_20_T15 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_20_T15
            ToValueTuple_20_T16 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_20_T16
            ToValueTuple_20_T17 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_20_T17
            ToValueTuple_20_T18 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_20_T18
            ToValueTuple_20_T19 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_20_T19
            ToValueTuple_20_T20 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_20_T20
            def __call__(self, value: Tuple_8[ToValueTuple_20_T1, ToValueTuple_20_T2, ToValueTuple_20_T3, ToValueTuple_20_T4, ToValueTuple_20_T5, ToValueTuple_20_T6, ToValueTuple_20_T7, Tuple_8[ToValueTuple_20_T8, ToValueTuple_20_T9, ToValueTuple_20_T10, ToValueTuple_20_T11, ToValueTuple_20_T12, ToValueTuple_20_T13, ToValueTuple_20_T14, Tuple_6[ToValueTuple_20_T15, ToValueTuple_20_T16, ToValueTuple_20_T17, ToValueTuple_20_T18, ToValueTuple_20_T19, ToValueTuple_20_T20]]]) -> ValueTuple_8[ToValueTuple_20_T1, ToValueTuple_20_T2, ToValueTuple_20_T3, ToValueTuple_20_T4, ToValueTuple_20_T5, ToValueTuple_20_T6, ToValueTuple_20_T7, ValueTuple_8[ToValueTuple_20_T8, ToValueTuple_20_T9, ToValueTuple_20_T10, ToValueTuple_20_T11, ToValueTuple_20_T12, ToValueTuple_20_T13, ToValueTuple_20_T14, ValueTuple_6[ToValueTuple_20_T15, ToValueTuple_20_T16, ToValueTuple_20_T17, ToValueTuple_20_T18, ToValueTuple_20_T19, ToValueTuple_20_T20]]]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[ToValueTuple_21_T1], typing.Type[ToValueTuple_21_T2], typing.Type[ToValueTuple_21_T3], typing.Type[ToValueTuple_21_T4], typing.Type[ToValueTuple_21_T5], typing.Type[ToValueTuple_21_T6], typing.Type[ToValueTuple_21_T7], typing.Type[ToValueTuple_21_T8], typing.Type[ToValueTuple_21_T9], typing.Type[ToValueTuple_21_T10], typing.Type[ToValueTuple_21_T11], typing.Type[ToValueTuple_21_T12], typing.Type[ToValueTuple_21_T13], typing.Type[ToValueTuple_21_T14], typing.Type[ToValueTuple_21_T15], typing.Type[ToValueTuple_21_T16], typing.Type[ToValueTuple_21_T17], typing.Type[ToValueTuple_21_T18], typing.Type[ToValueTuple_21_T19], typing.Type[ToValueTuple_21_T20], typing.Type[ToValueTuple_21_T21]]) -> ToValueTuple_21[ToValueTuple_21_T1, ToValueTuple_21_T2, ToValueTuple_21_T3, ToValueTuple_21_T4, ToValueTuple_21_T5, ToValueTuple_21_T6, ToValueTuple_21_T7, ToValueTuple_21_T8, ToValueTuple_21_T9, ToValueTuple_21_T10, ToValueTuple_21_T11, ToValueTuple_21_T12, ToValueTuple_21_T13, ToValueTuple_21_T14, ToValueTuple_21_T15, ToValueTuple_21_T16, ToValueTuple_21_T17, ToValueTuple_21_T18, ToValueTuple_21_T19, ToValueTuple_21_T20, ToValueTuple_21_T21]: ...

        ToValueTuple_21_T1 = typing.TypeVar('ToValueTuple_21_T1')
        ToValueTuple_21_T2 = typing.TypeVar('ToValueTuple_21_T2')
        ToValueTuple_21_T3 = typing.TypeVar('ToValueTuple_21_T3')
        ToValueTuple_21_T4 = typing.TypeVar('ToValueTuple_21_T4')
        ToValueTuple_21_T5 = typing.TypeVar('ToValueTuple_21_T5')
        ToValueTuple_21_T6 = typing.TypeVar('ToValueTuple_21_T6')
        ToValueTuple_21_T7 = typing.TypeVar('ToValueTuple_21_T7')
        ToValueTuple_21_T8 = typing.TypeVar('ToValueTuple_21_T8')
        ToValueTuple_21_T9 = typing.TypeVar('ToValueTuple_21_T9')
        ToValueTuple_21_T10 = typing.TypeVar('ToValueTuple_21_T10')
        ToValueTuple_21_T11 = typing.TypeVar('ToValueTuple_21_T11')
        ToValueTuple_21_T12 = typing.TypeVar('ToValueTuple_21_T12')
        ToValueTuple_21_T13 = typing.TypeVar('ToValueTuple_21_T13')
        ToValueTuple_21_T14 = typing.TypeVar('ToValueTuple_21_T14')
        ToValueTuple_21_T15 = typing.TypeVar('ToValueTuple_21_T15')
        ToValueTuple_21_T16 = typing.TypeVar('ToValueTuple_21_T16')
        ToValueTuple_21_T17 = typing.TypeVar('ToValueTuple_21_T17')
        ToValueTuple_21_T18 = typing.TypeVar('ToValueTuple_21_T18')
        ToValueTuple_21_T19 = typing.TypeVar('ToValueTuple_21_T19')
        ToValueTuple_21_T20 = typing.TypeVar('ToValueTuple_21_T20')
        ToValueTuple_21_T21 = typing.TypeVar('ToValueTuple_21_T21')
        class ToValueTuple_21(typing.Generic[ToValueTuple_21_T1, ToValueTuple_21_T2, ToValueTuple_21_T3, ToValueTuple_21_T4, ToValueTuple_21_T5, ToValueTuple_21_T6, ToValueTuple_21_T7, ToValueTuple_21_T8, ToValueTuple_21_T9, ToValueTuple_21_T10, ToValueTuple_21_T11, ToValueTuple_21_T12, ToValueTuple_21_T13, ToValueTuple_21_T14, ToValueTuple_21_T15, ToValueTuple_21_T16, ToValueTuple_21_T17, ToValueTuple_21_T18, ToValueTuple_21_T19, ToValueTuple_21_T20, ToValueTuple_21_T21]):
            ToValueTuple_21_T1 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_21_T1
            ToValueTuple_21_T2 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_21_T2
            ToValueTuple_21_T3 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_21_T3
            ToValueTuple_21_T4 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_21_T4
            ToValueTuple_21_T5 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_21_T5
            ToValueTuple_21_T6 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_21_T6
            ToValueTuple_21_T7 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_21_T7
            ToValueTuple_21_T8 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_21_T8
            ToValueTuple_21_T9 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_21_T9
            ToValueTuple_21_T10 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_21_T10
            ToValueTuple_21_T11 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_21_T11
            ToValueTuple_21_T12 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_21_T12
            ToValueTuple_21_T13 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_21_T13
            ToValueTuple_21_T14 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_21_T14
            ToValueTuple_21_T15 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_21_T15
            ToValueTuple_21_T16 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_21_T16
            ToValueTuple_21_T17 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_21_T17
            ToValueTuple_21_T18 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_21_T18
            ToValueTuple_21_T19 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_21_T19
            ToValueTuple_21_T20 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_21_T20
            ToValueTuple_21_T21 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_21_T21
            def __call__(self, value: Tuple_8[ToValueTuple_21_T1, ToValueTuple_21_T2, ToValueTuple_21_T3, ToValueTuple_21_T4, ToValueTuple_21_T5, ToValueTuple_21_T6, ToValueTuple_21_T7, Tuple_8[ToValueTuple_21_T8, ToValueTuple_21_T9, ToValueTuple_21_T10, ToValueTuple_21_T11, ToValueTuple_21_T12, ToValueTuple_21_T13, ToValueTuple_21_T14, Tuple_7[ToValueTuple_21_T15, ToValueTuple_21_T16, ToValueTuple_21_T17, ToValueTuple_21_T18, ToValueTuple_21_T19, ToValueTuple_21_T20, ToValueTuple_21_T21]]]) -> ValueTuple_8[ToValueTuple_21_T1, ToValueTuple_21_T2, ToValueTuple_21_T3, ToValueTuple_21_T4, ToValueTuple_21_T5, ToValueTuple_21_T6, ToValueTuple_21_T7, ValueTuple_8[ToValueTuple_21_T8, ToValueTuple_21_T9, ToValueTuple_21_T10, ToValueTuple_21_T11, ToValueTuple_21_T12, ToValueTuple_21_T13, ToValueTuple_21_T14, ValueTuple_7[ToValueTuple_21_T15, ToValueTuple_21_T16, ToValueTuple_21_T17, ToValueTuple_21_T18, ToValueTuple_21_T19, ToValueTuple_21_T20, ToValueTuple_21_T21]]]:...

        @typing.overload
        def __getitem__(self, t:typing.Type[ToValueTuple_1_T1]) -> ToValueTuple_1[ToValueTuple_1_T1]: ...

        ToValueTuple_1_T1 = typing.TypeVar('ToValueTuple_1_T1')
        class ToValueTuple_1(typing.Generic[ToValueTuple_1_T1]):
            ToValueTuple_1_T1 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_1_T1
            def __call__(self, value: Tuple_1[ToValueTuple_1_T1]) -> ValueTuple_1[ToValueTuple_1_T1]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[ToValueTuple_2_T1], typing.Type[ToValueTuple_2_T2]]) -> ToValueTuple_2[ToValueTuple_2_T1, ToValueTuple_2_T2]: ...

        ToValueTuple_2_T1 = typing.TypeVar('ToValueTuple_2_T1')
        ToValueTuple_2_T2 = typing.TypeVar('ToValueTuple_2_T2')
        class ToValueTuple_2(typing.Generic[ToValueTuple_2_T1, ToValueTuple_2_T2]):
            ToValueTuple_2_T1 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_2_T1
            ToValueTuple_2_T2 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_2_T2
            def __call__(self, value: Tuple_2[ToValueTuple_2_T1, ToValueTuple_2_T2]) -> ValueTuple_2[ToValueTuple_2_T1, ToValueTuple_2_T2]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[ToValueTuple_3_T1], typing.Type[ToValueTuple_3_T2], typing.Type[ToValueTuple_3_T3]]) -> ToValueTuple_3[ToValueTuple_3_T1, ToValueTuple_3_T2, ToValueTuple_3_T3]: ...

        ToValueTuple_3_T1 = typing.TypeVar('ToValueTuple_3_T1')
        ToValueTuple_3_T2 = typing.TypeVar('ToValueTuple_3_T2')
        ToValueTuple_3_T3 = typing.TypeVar('ToValueTuple_3_T3')
        class ToValueTuple_3(typing.Generic[ToValueTuple_3_T1, ToValueTuple_3_T2, ToValueTuple_3_T3]):
            ToValueTuple_3_T1 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_3_T1
            ToValueTuple_3_T2 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_3_T2
            ToValueTuple_3_T3 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_3_T3
            def __call__(self, value: Tuple_3[ToValueTuple_3_T1, ToValueTuple_3_T2, ToValueTuple_3_T3]) -> ValueTuple_3[ToValueTuple_3_T1, ToValueTuple_3_T2, ToValueTuple_3_T3]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[ToValueTuple_4_T1], typing.Type[ToValueTuple_4_T2], typing.Type[ToValueTuple_4_T3], typing.Type[ToValueTuple_4_T4]]) -> ToValueTuple_4[ToValueTuple_4_T1, ToValueTuple_4_T2, ToValueTuple_4_T3, ToValueTuple_4_T4]: ...

        ToValueTuple_4_T1 = typing.TypeVar('ToValueTuple_4_T1')
        ToValueTuple_4_T2 = typing.TypeVar('ToValueTuple_4_T2')
        ToValueTuple_4_T3 = typing.TypeVar('ToValueTuple_4_T3')
        ToValueTuple_4_T4 = typing.TypeVar('ToValueTuple_4_T4')
        class ToValueTuple_4(typing.Generic[ToValueTuple_4_T1, ToValueTuple_4_T2, ToValueTuple_4_T3, ToValueTuple_4_T4]):
            ToValueTuple_4_T1 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_4_T1
            ToValueTuple_4_T2 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_4_T2
            ToValueTuple_4_T3 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_4_T3
            ToValueTuple_4_T4 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_4_T4
            def __call__(self, value: Tuple_4[ToValueTuple_4_T1, ToValueTuple_4_T2, ToValueTuple_4_T3, ToValueTuple_4_T4]) -> ValueTuple_4[ToValueTuple_4_T1, ToValueTuple_4_T2, ToValueTuple_4_T3, ToValueTuple_4_T4]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[ToValueTuple_5_T1], typing.Type[ToValueTuple_5_T2], typing.Type[ToValueTuple_5_T3], typing.Type[ToValueTuple_5_T4], typing.Type[ToValueTuple_5_T5]]) -> ToValueTuple_5[ToValueTuple_5_T1, ToValueTuple_5_T2, ToValueTuple_5_T3, ToValueTuple_5_T4, ToValueTuple_5_T5]: ...

        ToValueTuple_5_T1 = typing.TypeVar('ToValueTuple_5_T1')
        ToValueTuple_5_T2 = typing.TypeVar('ToValueTuple_5_T2')
        ToValueTuple_5_T3 = typing.TypeVar('ToValueTuple_5_T3')
        ToValueTuple_5_T4 = typing.TypeVar('ToValueTuple_5_T4')
        ToValueTuple_5_T5 = typing.TypeVar('ToValueTuple_5_T5')
        class ToValueTuple_5(typing.Generic[ToValueTuple_5_T1, ToValueTuple_5_T2, ToValueTuple_5_T3, ToValueTuple_5_T4, ToValueTuple_5_T5]):
            ToValueTuple_5_T1 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_5_T1
            ToValueTuple_5_T2 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_5_T2
            ToValueTuple_5_T3 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_5_T3
            ToValueTuple_5_T4 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_5_T4
            ToValueTuple_5_T5 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_5_T5
            def __call__(self, value: Tuple_5[ToValueTuple_5_T1, ToValueTuple_5_T2, ToValueTuple_5_T3, ToValueTuple_5_T4, ToValueTuple_5_T5]) -> ValueTuple_5[ToValueTuple_5_T1, ToValueTuple_5_T2, ToValueTuple_5_T3, ToValueTuple_5_T4, ToValueTuple_5_T5]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[ToValueTuple_6_T1], typing.Type[ToValueTuple_6_T2], typing.Type[ToValueTuple_6_T3], typing.Type[ToValueTuple_6_T4], typing.Type[ToValueTuple_6_T5], typing.Type[ToValueTuple_6_T6]]) -> ToValueTuple_6[ToValueTuple_6_T1, ToValueTuple_6_T2, ToValueTuple_6_T3, ToValueTuple_6_T4, ToValueTuple_6_T5, ToValueTuple_6_T6]: ...

        ToValueTuple_6_T1 = typing.TypeVar('ToValueTuple_6_T1')
        ToValueTuple_6_T2 = typing.TypeVar('ToValueTuple_6_T2')
        ToValueTuple_6_T3 = typing.TypeVar('ToValueTuple_6_T3')
        ToValueTuple_6_T4 = typing.TypeVar('ToValueTuple_6_T4')
        ToValueTuple_6_T5 = typing.TypeVar('ToValueTuple_6_T5')
        ToValueTuple_6_T6 = typing.TypeVar('ToValueTuple_6_T6')
        class ToValueTuple_6(typing.Generic[ToValueTuple_6_T1, ToValueTuple_6_T2, ToValueTuple_6_T3, ToValueTuple_6_T4, ToValueTuple_6_T5, ToValueTuple_6_T6]):
            ToValueTuple_6_T1 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_6_T1
            ToValueTuple_6_T2 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_6_T2
            ToValueTuple_6_T3 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_6_T3
            ToValueTuple_6_T4 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_6_T4
            ToValueTuple_6_T5 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_6_T5
            ToValueTuple_6_T6 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_6_T6
            def __call__(self, value: Tuple_6[ToValueTuple_6_T1, ToValueTuple_6_T2, ToValueTuple_6_T3, ToValueTuple_6_T4, ToValueTuple_6_T5, ToValueTuple_6_T6]) -> ValueTuple_6[ToValueTuple_6_T1, ToValueTuple_6_T2, ToValueTuple_6_T3, ToValueTuple_6_T4, ToValueTuple_6_T5, ToValueTuple_6_T6]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[ToValueTuple_7_T1], typing.Type[ToValueTuple_7_T2], typing.Type[ToValueTuple_7_T3], typing.Type[ToValueTuple_7_T4], typing.Type[ToValueTuple_7_T5], typing.Type[ToValueTuple_7_T6], typing.Type[ToValueTuple_7_T7]]) -> ToValueTuple_7[ToValueTuple_7_T1, ToValueTuple_7_T2, ToValueTuple_7_T3, ToValueTuple_7_T4, ToValueTuple_7_T5, ToValueTuple_7_T6, ToValueTuple_7_T7]: ...

        ToValueTuple_7_T1 = typing.TypeVar('ToValueTuple_7_T1')
        ToValueTuple_7_T2 = typing.TypeVar('ToValueTuple_7_T2')
        ToValueTuple_7_T3 = typing.TypeVar('ToValueTuple_7_T3')
        ToValueTuple_7_T4 = typing.TypeVar('ToValueTuple_7_T4')
        ToValueTuple_7_T5 = typing.TypeVar('ToValueTuple_7_T5')
        ToValueTuple_7_T6 = typing.TypeVar('ToValueTuple_7_T6')
        ToValueTuple_7_T7 = typing.TypeVar('ToValueTuple_7_T7')
        class ToValueTuple_7(typing.Generic[ToValueTuple_7_T1, ToValueTuple_7_T2, ToValueTuple_7_T3, ToValueTuple_7_T4, ToValueTuple_7_T5, ToValueTuple_7_T6, ToValueTuple_7_T7]):
            ToValueTuple_7_T1 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_7_T1
            ToValueTuple_7_T2 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_7_T2
            ToValueTuple_7_T3 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_7_T3
            ToValueTuple_7_T4 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_7_T4
            ToValueTuple_7_T5 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_7_T5
            ToValueTuple_7_T6 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_7_T6
            ToValueTuple_7_T7 = TupleExtensions.ToValueTuple_MethodGroup.ToValueTuple_7_T7
            def __call__(self, value: Tuple_7[ToValueTuple_7_T1, ToValueTuple_7_T2, ToValueTuple_7_T3, ToValueTuple_7_T4, ToValueTuple_7_T5, ToValueTuple_7_T6, ToValueTuple_7_T7]) -> ValueTuple_7[ToValueTuple_7_T1, ToValueTuple_7_T2, ToValueTuple_7_T3, ToValueTuple_7_T4, ToValueTuple_7_T5, ToValueTuple_7_T6, ToValueTuple_7_T7]:...




class Type(MemberInfo, IReflect):
    Delimiter : str
    EmptyTypes : Array_1[typing.Type[typing.Any]]
    FilterAttribute : MemberFilter
    FilterName : MemberFilter
    FilterNameIgnoreCase : MemberFilter
    Missing : typing.Any
    @property
    def Assembly(self) -> Assembly: ...
    @property
    def AssemblyQualifiedName(self) -> str: ...
    @property
    def Attributes(self) -> TypeAttributes: ...
    @property
    def BaseType(self) -> typing.Type[typing.Any]: ...
    @property
    def ContainsGenericParameters(self) -> bool: ...
    @property
    def CustomAttributes(self) -> IEnumerable_1[CustomAttributeData]: ...
    @property
    def DeclaringMethod(self) -> MethodBase: ...
    @property
    def DeclaringType(self) -> typing.Type[typing.Any]: ...
    @classmethod
    @property
    def DefaultBinder(cls) -> Binder: ...
    @property
    def FullName(self) -> str: ...
    @property
    def GenericParameterAttributes(self) -> GenericParameterAttributes: ...
    @property
    def GenericParameterPosition(self) -> int: ...
    @property
    def GenericTypeArguments(self) -> Array_1[typing.Type[typing.Any]]: ...
    @property
    def GUID(self) -> Guid: ...
    @property
    def HasElementType(self) -> bool: ...
    @property
    def IsAbstract(self) -> bool: ...
    @property
    def IsAnsiClass(self) -> bool: ...
    @property
    def IsArray(self) -> bool: ...
    @property
    def IsAutoClass(self) -> bool: ...
    @property
    def IsAutoLayout(self) -> bool: ...
    @property
    def IsByRef(self) -> bool: ...
    @property
    def IsByRefLike(self) -> bool: ...
    @property
    def IsClass(self) -> bool: ...
    @property
    def IsCollectible(self) -> bool: ...
    @property
    def IsCOMObject(self) -> bool: ...
    @property
    def IsConstructedGenericType(self) -> bool: ...
    @property
    def IsContextful(self) -> bool: ...
    @property
    def IsEnum(self) -> bool: ...
    @property
    def IsExplicitLayout(self) -> bool: ...
    @property
    def IsGenericMethodParameter(self) -> bool: ...
    @property
    def IsGenericParameter(self) -> bool: ...
    @property
    def IsGenericType(self) -> bool: ...
    @property
    def IsGenericTypeDefinition(self) -> bool: ...
    @property
    def IsGenericTypeParameter(self) -> bool: ...
    @property
    def IsImport(self) -> bool: ...
    @property
    def IsInterface(self) -> bool: ...
    @property
    def IsLayoutSequential(self) -> bool: ...
    @property
    def IsMarshalByRef(self) -> bool: ...
    @property
    def IsNested(self) -> bool: ...
    @property
    def IsNestedAssembly(self) -> bool: ...
    @property
    def IsNestedFamANDAssem(self) -> bool: ...
    @property
    def IsNestedFamily(self) -> bool: ...
    @property
    def IsNestedFamORAssem(self) -> bool: ...
    @property
    def IsNestedPrivate(self) -> bool: ...
    @property
    def IsNestedPublic(self) -> bool: ...
    @property
    def IsNotPublic(self) -> bool: ...
    @property
    def IsPointer(self) -> bool: ...
    @property
    def IsPrimitive(self) -> bool: ...
    @property
    def IsPublic(self) -> bool: ...
    @property
    def IsSealed(self) -> bool: ...
    @property
    def IsSecurityCritical(self) -> bool: ...
    @property
    def IsSecuritySafeCritical(self) -> bool: ...
    @property
    def IsSecurityTransparent(self) -> bool: ...
    @property
    def IsSerializable(self) -> bool: ...
    @property
    def IsSignatureType(self) -> bool: ...
    @property
    def IsSpecialName(self) -> bool: ...
    @property
    def IsSZArray(self) -> bool: ...
    @property
    def IsTypeDefinition(self) -> bool: ...
    @property
    def IsUnicodeClass(self) -> bool: ...
    @property
    def IsValueType(self) -> bool: ...
    @property
    def IsVariableBoundArray(self) -> bool: ...
    @property
    def IsVisible(self) -> bool: ...
    @property
    def MemberType(self) -> MemberTypes: ...
    @property
    def MetadataToken(self) -> int: ...
    @property
    def Module(self) -> Module: ...
    @property
    def Name(self) -> str: ...
    @property
    def Namespace(self) -> str: ...
    @property
    def ReflectedType(self) -> typing.Type[typing.Any]: ...
    @property
    def StructLayoutAttribute(self) -> StructLayoutAttribute: ...
    @property
    def TypeHandle(self) -> RuntimeTypeHandle: ...
    @property
    def TypeInitializer(self) -> ConstructorInfo: ...
    @property
    def UnderlyingSystemType(self) -> typing.Type[typing.Any]: ...
    def FindInterfaces(self, filter: TypeFilter, filterCriteria: typing.Any) -> Array_1[typing.Type[typing.Any]]: ...
    def FindMembers(self, memberType: MemberTypes, bindingAttr: BindingFlags, filter: MemberFilter, filterCriteria: typing.Any) -> Array_1[MemberInfo]: ...
    def GetArrayRank(self) -> int: ...
    def GetDefaultMembers(self) -> Array_1[MemberInfo]: ...
    @abc.abstractmethod
    def GetElementType(self) -> typing.Type[typing.Any]: ...
    def GetEnumName(self, value: typing.Any) -> str: ...
    def GetEnumNames(self) -> Array_1[str]: ...
    def GetEnumUnderlyingType(self) -> typing.Type[typing.Any]: ...
    def GetEnumValues(self) -> Array: ...
    def GetGenericArguments(self) -> Array_1[typing.Type[typing.Any]]: ...
    def GetGenericParameterConstraints(self) -> Array_1[typing.Type[typing.Any]]: ...
    def GetGenericTypeDefinition(self) -> typing.Type[typing.Any]: ...
    def GetHashCode(self) -> int: ...
    def GetInterfaceMap(self, interfaceType: typing.Type[typing.Any]) -> InterfaceMapping: ...
    @abc.abstractmethod
    def GetInterfaces(self) -> Array_1[typing.Type[typing.Any]]: ...
    def GetMemberWithSameMetadataDefinitionAs(self, member: MemberInfo) -> MemberInfo: ...
    @staticmethod
    def GetTypeArray(args: Array_1[typing.Any]) -> Array_1[typing.Type[typing.Any]]: ...
    @staticmethod
    def GetTypeCode(type: typing.Type[typing.Any]) -> TypeCode: ...
    @staticmethod
    def GetTypeFromHandle(handle: RuntimeTypeHandle) -> typing.Type[typing.Any]: ...
    @staticmethod
    def GetTypeHandle(o: typing.Any) -> RuntimeTypeHandle: ...
    def IsAssignableFrom(self, c: typing.Type[typing.Any]) -> bool: ...
    def IsAssignableTo(self, targetType: typing.Type[typing.Any]) -> bool: ...
    def IsEnumDefined(self, value: typing.Any) -> bool: ...
    def IsEquivalentTo(self, other: typing.Type[typing.Any]) -> bool: ...
    def IsInstanceOfType(self, o: typing.Any) -> bool: ...
    def IsSubclassOf(self, c: typing.Type[typing.Any]) -> bool: ...
    def MakeByRefType(self) -> typing.Type[typing.Any]: ...
    @staticmethod
    def MakeGenericMethodParameter(position: int) -> typing.Type[typing.Any]: ...
    @staticmethod
    def MakeGenericSignatureType(genericTypeDefinition: typing.Type[typing.Any], typeArguments: Array_1[typing.Type[typing.Any]]) -> typing.Type[typing.Any]: ...
    def MakeGenericType(self, typeArguments: Array_1[typing.Type[typing.Any]]) -> typing.Type[typing.Any]: ...
    def MakePointerType(self) -> typing.Type[typing.Any]: ...
    def __eq__(self, left: typing.Type[typing.Any], right: typing.Type[typing.Any]) -> bool: ...
    def __ne__(self, left: typing.Type[typing.Any], right: typing.Type[typing.Any]) -> bool: ...
    @staticmethod
    def ReflectionOnlyGetType(typeName: str, throwIfNotFound: bool, ignoreCase: bool) -> typing.Type[typing.Any]: ...
    def ToString(self) -> str: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, o: typing.Type[typing.Any]) -> bool:...
        @typing.overload
        def __call__(self, o: typing.Any) -> bool:...

    # Skipped GetConstructor due to it being static, abstract and generic.

    GetConstructor : GetConstructor_MethodGroup
    class GetConstructor_MethodGroup:
        @typing.overload
        def __call__(self, types: Array_1[typing.Type[typing.Any]]) -> ConstructorInfo:...
        @typing.overload
        def __call__(self, bindingAttr: BindingFlags, types: Array_1[typing.Type[typing.Any]]) -> ConstructorInfo:...
        @typing.overload
        def __call__(self, bindingAttr: BindingFlags, binder: Binder, types: Array_1[typing.Type[typing.Any]], modifiers: Array_1[ParameterModifier]) -> ConstructorInfo:...
        @typing.overload
        def __call__(self, bindingAttr: BindingFlags, binder: Binder, callConvention: CallingConventions, types: Array_1[typing.Type[typing.Any]], modifiers: Array_1[ParameterModifier]) -> ConstructorInfo:...

    # Skipped GetConstructors due to it being static, abstract and generic.

    GetConstructors : GetConstructors_MethodGroup
    class GetConstructors_MethodGroup:
        @typing.overload
        def __call__(self) -> Array_1[ConstructorInfo]:...
        @typing.overload
        def __call__(self, bindingAttr: BindingFlags) -> Array_1[ConstructorInfo]:...

    # Skipped GetEvent due to it being static, abstract and generic.

    GetEvent : GetEvent_MethodGroup
    class GetEvent_MethodGroup:
        @typing.overload
        def __call__(self, name: str) -> EventInfo:...
        @typing.overload
        def __call__(self, name: str, bindingAttr: BindingFlags) -> EventInfo:...

    # Skipped GetEvents due to it being static, abstract and generic.

    GetEvents : GetEvents_MethodGroup
    class GetEvents_MethodGroup:
        @typing.overload
        def __call__(self) -> Array_1[EventInfo]:...
        @typing.overload
        def __call__(self, bindingAttr: BindingFlags) -> Array_1[EventInfo]:...

    # Skipped GetField due to it being static, abstract and generic.

    GetField : GetField_MethodGroup
    class GetField_MethodGroup:
        @typing.overload
        def __call__(self, name: str) -> FieldInfo:...
        @typing.overload
        def __call__(self, name: str, bindingAttr: BindingFlags) -> FieldInfo:...

    # Skipped GetFields due to it being static, abstract and generic.

    GetFields : GetFields_MethodGroup
    class GetFields_MethodGroup:
        @typing.overload
        def __call__(self) -> Array_1[FieldInfo]:...
        @typing.overload
        def __call__(self, bindingAttr: BindingFlags) -> Array_1[FieldInfo]:...

    # Skipped GetInterface due to it being static, abstract and generic.

    GetInterface : GetInterface_MethodGroup
    class GetInterface_MethodGroup:
        @typing.overload
        def __call__(self, name: str) -> typing.Type[typing.Any]:...
        @typing.overload
        def __call__(self, name: str, ignoreCase: bool) -> typing.Type[typing.Any]:...

    # Skipped GetMember due to it being static, abstract and generic.

    GetMember : GetMember_MethodGroup
    class GetMember_MethodGroup:
        @typing.overload
        def __call__(self, name: str) -> Array_1[MemberInfo]:...
        @typing.overload
        def __call__(self, name: str, bindingAttr: BindingFlags) -> Array_1[MemberInfo]:...
        @typing.overload
        def __call__(self, name: str, type: MemberTypes, bindingAttr: BindingFlags) -> Array_1[MemberInfo]:...

    # Skipped GetMembers due to it being static, abstract and generic.

    GetMembers : GetMembers_MethodGroup
    class GetMembers_MethodGroup:
        @typing.overload
        def __call__(self) -> Array_1[MemberInfo]:...
        @typing.overload
        def __call__(self, bindingAttr: BindingFlags) -> Array_1[MemberInfo]:...

    # Skipped GetMethod due to it being static, abstract and generic.

    GetMethod : GetMethod_MethodGroup
    class GetMethod_MethodGroup:
        @typing.overload
        def __call__(self, name: str) -> MethodInfo:...
        @typing.overload
        def __call__(self, name: str, types: Array_1[typing.Type[typing.Any]]) -> MethodInfo:...
        @typing.overload
        def __call__(self, name: str, bindingAttr: BindingFlags) -> MethodInfo:...
        @typing.overload
        def __call__(self, name: str, genericParameterCount: int, types: Array_1[typing.Type[typing.Any]]) -> MethodInfo:...
        @typing.overload
        def __call__(self, name: str, types: Array_1[typing.Type[typing.Any]], modifiers: Array_1[ParameterModifier]) -> MethodInfo:...
        @typing.overload
        def __call__(self, name: str, bindingAttr: BindingFlags, types: Array_1[typing.Type[typing.Any]]) -> MethodInfo:...
        @typing.overload
        def __call__(self, name: str, genericParameterCount: int, types: Array_1[typing.Type[typing.Any]], modifiers: Array_1[ParameterModifier]) -> MethodInfo:...
        @typing.overload
        def __call__(self, name: str, bindingAttr: BindingFlags, binder: Binder, types: Array_1[typing.Type[typing.Any]], modifiers: Array_1[ParameterModifier]) -> MethodInfo:...
        @typing.overload
        def __call__(self, name: str, genericParameterCount: int, bindingAttr: BindingFlags, binder: Binder, types: Array_1[typing.Type[typing.Any]], modifiers: Array_1[ParameterModifier]) -> MethodInfo:...
        @typing.overload
        def __call__(self, name: str, bindingAttr: BindingFlags, binder: Binder, callConvention: CallingConventions, types: Array_1[typing.Type[typing.Any]], modifiers: Array_1[ParameterModifier]) -> MethodInfo:...
        @typing.overload
        def __call__(self, name: str, genericParameterCount: int, bindingAttr: BindingFlags, binder: Binder, callConvention: CallingConventions, types: Array_1[typing.Type[typing.Any]], modifiers: Array_1[ParameterModifier]) -> MethodInfo:...

    # Skipped GetMethods due to it being static, abstract and generic.

    GetMethods : GetMethods_MethodGroup
    class GetMethods_MethodGroup:
        @typing.overload
        def __call__(self) -> Array_1[MethodInfo]:...
        @typing.overload
        def __call__(self, bindingAttr: BindingFlags) -> Array_1[MethodInfo]:...

    # Skipped GetNestedType due to it being static, abstract and generic.

    GetNestedType : GetNestedType_MethodGroup
    class GetNestedType_MethodGroup:
        @typing.overload
        def __call__(self, name: str) -> typing.Type[typing.Any]:...
        @typing.overload
        def __call__(self, name: str, bindingAttr: BindingFlags) -> typing.Type[typing.Any]:...

    # Skipped GetNestedTypes due to it being static, abstract and generic.

    GetNestedTypes : GetNestedTypes_MethodGroup
    class GetNestedTypes_MethodGroup:
        @typing.overload
        def __call__(self) -> Array_1[typing.Type[typing.Any]]:...
        @typing.overload
        def __call__(self, bindingAttr: BindingFlags) -> Array_1[typing.Type[typing.Any]]:...

    # Skipped GetProperties due to it being static, abstract and generic.

    GetProperties : GetProperties_MethodGroup
    class GetProperties_MethodGroup:
        @typing.overload
        def __call__(self) -> Array_1[PropertyInfo]:...
        @typing.overload
        def __call__(self, bindingAttr: BindingFlags) -> Array_1[PropertyInfo]:...

    # Skipped GetProperty due to it being static, abstract and generic.

    GetProperty : GetProperty_MethodGroup
    class GetProperty_MethodGroup:
        @typing.overload
        def __call__(self, name: str) -> PropertyInfo:...
        @typing.overload
        def __call__(self, name: str, types: Array_1[typing.Type[typing.Any]]) -> PropertyInfo:...
        @typing.overload
        def __call__(self, name: str, bindingAttr: BindingFlags) -> PropertyInfo:...
        @typing.overload
        def __call__(self, name: str, returnType: typing.Type[typing.Any]) -> PropertyInfo:...
        @typing.overload
        def __call__(self, name: str, returnType: typing.Type[typing.Any], types: Array_1[typing.Type[typing.Any]]) -> PropertyInfo:...
        @typing.overload
        def __call__(self, name: str, returnType: typing.Type[typing.Any], types: Array_1[typing.Type[typing.Any]], modifiers: Array_1[ParameterModifier]) -> PropertyInfo:...
        @typing.overload
        def __call__(self, name: str, bindingAttr: BindingFlags, binder: Binder, returnType: typing.Type[typing.Any], types: Array_1[typing.Type[typing.Any]], modifiers: Array_1[ParameterModifier]) -> PropertyInfo:...

    # Skipped GetType due to it being static, abstract and generic.

    GetType : GetType_MethodGroup
    class GetType_MethodGroup:
        @typing.overload
        def __call__(self) -> typing.Type[typing.Any]:...
        @typing.overload
        def __call__(self, typeName: str) -> typing.Type[typing.Any]:...
        @typing.overload
        def __call__(self, typeName: str, throwOnError: bool) -> typing.Type[typing.Any]:...
        @typing.overload
        def __call__(self, typeName: str, assemblyResolver: Func_2[AssemblyName, Assembly], typeResolver: Func_4[Assembly, str, bool, typing.Type[typing.Any]]) -> typing.Type[typing.Any]:...
        @typing.overload
        def __call__(self, typeName: str, throwOnError: bool, ignoreCase: bool) -> typing.Type[typing.Any]:...
        @typing.overload
        def __call__(self, typeName: str, assemblyResolver: Func_2[AssemblyName, Assembly], typeResolver: Func_4[Assembly, str, bool, typing.Type[typing.Any]], throwOnError: bool) -> typing.Type[typing.Any]:...
        @typing.overload
        def __call__(self, typeName: str, assemblyResolver: Func_2[AssemblyName, Assembly], typeResolver: Func_4[Assembly, str, bool, typing.Type[typing.Any]], throwOnError: bool, ignoreCase: bool) -> typing.Type[typing.Any]:...

    # Skipped GetTypeFromCLSID due to it being static, abstract and generic.

    GetTypeFromCLSID : GetTypeFromCLSID_MethodGroup
    class GetTypeFromCLSID_MethodGroup:
        @typing.overload
        def __call__(self, clsid: Guid) -> typing.Type[typing.Any]:...
        @typing.overload
        def __call__(self, clsid: Guid, server: str) -> typing.Type[typing.Any]:...
        @typing.overload
        def __call__(self, clsid: Guid, throwOnError: bool) -> typing.Type[typing.Any]:...
        @typing.overload
        def __call__(self, clsid: Guid, server: str, throwOnError: bool) -> typing.Type[typing.Any]:...

    # Skipped GetTypeFromProgID due to it being static, abstract and generic.

    GetTypeFromProgID : GetTypeFromProgID_MethodGroup
    class GetTypeFromProgID_MethodGroup:
        @typing.overload
        def __call__(self, progID: str) -> typing.Type[typing.Any]:...
        @typing.overload
        def __call__(self, progID: str, server: str) -> typing.Type[typing.Any]:...
        @typing.overload
        def __call__(self, progID: str, throwOnError: bool) -> typing.Type[typing.Any]:...
        @typing.overload
        def __call__(self, progID: str, server: str, throwOnError: bool) -> typing.Type[typing.Any]:...

    # Skipped InvokeMember due to it being static, abstract and generic.

    InvokeMember : InvokeMember_MethodGroup
    class InvokeMember_MethodGroup:
        @typing.overload
        def __call__(self, name: str, invokeAttr: BindingFlags, binder: Binder, target: typing.Any, args: Array_1[typing.Any]) -> typing.Any:...
        @typing.overload
        def __call__(self, name: str, invokeAttr: BindingFlags, binder: Binder, target: typing.Any, args: Array_1[typing.Any], culture: CultureInfo) -> typing.Any:...
        @typing.overload
        def __call__(self, name: str, invokeAttr: BindingFlags, binder: Binder, target: typing.Any, args: Array_1[typing.Any], modifiers: Array_1[ParameterModifier], culture: CultureInfo, namedParameters: Array_1[str]) -> typing.Any:...

    # Skipped MakeArrayType due to it being static, abstract and generic.

    MakeArrayType : MakeArrayType_MethodGroup
    class MakeArrayType_MethodGroup:
        @typing.overload
        def __call__(self) -> typing.Type[typing.Any]:...
        @typing.overload
        def __call__(self, rank: int) -> typing.Type[typing.Any]:...



class TypeAccessException(TypeLoadException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, inner: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...
    @property
    def TypeName(self) -> str: ...


class TypeCode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Empty : TypeCode # 0
    Object : TypeCode # 1
    DBNull : TypeCode # 2
    Boolean : TypeCode # 3
    Char : TypeCode # 4
    SByte : TypeCode # 5
    Byte : TypeCode # 6
    Int16 : TypeCode # 7
    UInt16 : TypeCode # 8
    Int32 : TypeCode # 9
    UInt32 : TypeCode # 10
    Int64 : TypeCode # 11
    UInt64 : TypeCode # 12
    Single : TypeCode # 13
    Double : TypeCode # 14
    Decimal : TypeCode # 15
    DateTime : TypeCode # 16
    String : TypeCode # 18


class TypedReference:
    def Equals(self, o: typing.Any) -> bool: ...
    def GetHashCode(self) -> int: ...
    @staticmethod
    def GetTargetType(value: TypedReference) -> typing.Type[typing.Any]: ...
    @staticmethod
    def MakeTypedReference(target: typing.Any, flds: Array_1[FieldInfo]) -> TypedReference: ...
    @staticmethod
    def SetTypedReference(target: TypedReference, value: typing.Any) -> None: ...
    @staticmethod
    def TargetTypeToken(value: TypedReference) -> RuntimeTypeHandle: ...
    @staticmethod
    def ToObject(value: TypedReference) -> typing.Any: ...


class TypeInitializationException(SystemException):
    def __init__(self, fullTypeName: str, innerException: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...
    @property
    def TypeName(self) -> str: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...


class TypeLoadException(SystemException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, inner: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...
    @property
    def TypeName(self) -> str: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...


class TypeUnloadedException(SystemException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, innerException: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...


class UInt16(IBinaryInteger_1[int], IUnsignedNumber_1[int], IMinMaxValue_1[int], IConvertible):
    MaxValue : int
    MinValue : int
    def GetHashCode(self) -> int: ...
    def GetTypeCode(self) -> TypeCode: ...
    def TryFormat(self, destination: Span_1[str], charsWritten: clr.Reference[int], format: ReadOnlySpan_1[str] = ..., provider: IFormatProvider = ...) -> bool: ...
    # Skipped CompareTo due to it being static, abstract and generic.

    CompareTo : CompareTo_MethodGroup
    class CompareTo_MethodGroup:
        @typing.overload
        def __call__(self, value: int) -> int:...
        @typing.overload
        def __call__(self, value: typing.Any) -> int:...

    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, obj: int) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...

    # Skipped Parse due to it being static, abstract and generic.

    Parse : Parse_MethodGroup
    class Parse_MethodGroup:
        @typing.overload
        def __call__(self, s: str) -> int:...
        @typing.overload
        def __call__(self, s: str, style: NumberStyles) -> int:...
        @typing.overload
        def __call__(self, s: str, provider: IFormatProvider) -> int:...
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], style: NumberStyles = ..., provider: IFormatProvider = ...) -> int:...
        @typing.overload
        def __call__(self, s: str, style: NumberStyles, provider: IFormatProvider) -> int:...

    # Skipped ToString due to it being static, abstract and generic.

    ToString : ToString_MethodGroup
    class ToString_MethodGroup:
        @typing.overload
        def __call__(self) -> str:...
        @typing.overload
        def __call__(self, format: str) -> str:...
        @typing.overload
        def __call__(self, provider: IFormatProvider) -> str:...
        @typing.overload
        def __call__(self, format: str, provider: IFormatProvider) -> str:...

    # Skipped TryParse due to it being static, abstract and generic.

    TryParse : TryParse_MethodGroup
    class TryParse_MethodGroup:
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], result: clr.Reference[int]) -> bool:...
        @typing.overload
        def __call__(self, s: str, result: clr.Reference[int]) -> bool:...
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], style: NumberStyles, provider: IFormatProvider, result: clr.Reference[int]) -> bool:...
        @typing.overload
        def __call__(self, s: str, style: NumberStyles, provider: IFormatProvider, result: clr.Reference[int]) -> bool:...



class UInt32(IBinaryInteger_1[int], IUnsignedNumber_1[int], IMinMaxValue_1[int], IConvertible):
    MaxValue : int
    MinValue : int
    def GetHashCode(self) -> int: ...
    def GetTypeCode(self) -> TypeCode: ...
    def TryFormat(self, destination: Span_1[str], charsWritten: clr.Reference[int], format: ReadOnlySpan_1[str] = ..., provider: IFormatProvider = ...) -> bool: ...
    # Skipped CompareTo due to it being static, abstract and generic.

    CompareTo : CompareTo_MethodGroup
    class CompareTo_MethodGroup:
        @typing.overload
        def __call__(self, value: int) -> int:...
        @typing.overload
        def __call__(self, value: typing.Any) -> int:...

    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, obj: int) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...

    # Skipped Parse due to it being static, abstract and generic.

    Parse : Parse_MethodGroup
    class Parse_MethodGroup:
        @typing.overload
        def __call__(self, s: str) -> int:...
        @typing.overload
        def __call__(self, s: str, style: NumberStyles) -> int:...
        @typing.overload
        def __call__(self, s: str, provider: IFormatProvider) -> int:...
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], style: NumberStyles = ..., provider: IFormatProvider = ...) -> int:...
        @typing.overload
        def __call__(self, s: str, style: NumberStyles, provider: IFormatProvider) -> int:...

    # Skipped ToString due to it being static, abstract and generic.

    ToString : ToString_MethodGroup
    class ToString_MethodGroup:
        @typing.overload
        def __call__(self) -> str:...
        @typing.overload
        def __call__(self, format: str) -> str:...
        @typing.overload
        def __call__(self, provider: IFormatProvider) -> str:...
        @typing.overload
        def __call__(self, format: str, provider: IFormatProvider) -> str:...

    # Skipped TryParse due to it being static, abstract and generic.

    TryParse : TryParse_MethodGroup
    class TryParse_MethodGroup:
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], result: clr.Reference[int]) -> bool:...
        @typing.overload
        def __call__(self, s: str, result: clr.Reference[int]) -> bool:...
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], style: NumberStyles, provider: IFormatProvider, result: clr.Reference[int]) -> bool:...
        @typing.overload
        def __call__(self, s: str, style: NumberStyles, provider: IFormatProvider, result: clr.Reference[int]) -> bool:...



class UInt64(IBinaryInteger_1[int], IUnsignedNumber_1[int], IMinMaxValue_1[int], IConvertible):
    MaxValue : int
    MinValue : int
    def GetHashCode(self) -> int: ...
    def GetTypeCode(self) -> TypeCode: ...
    def TryFormat(self, destination: Span_1[str], charsWritten: clr.Reference[int], format: ReadOnlySpan_1[str] = ..., provider: IFormatProvider = ...) -> bool: ...
    # Skipped CompareTo due to it being static, abstract and generic.

    CompareTo : CompareTo_MethodGroup
    class CompareTo_MethodGroup:
        @typing.overload
        def __call__(self, value: int) -> int:...
        @typing.overload
        def __call__(self, value: typing.Any) -> int:...

    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, obj: int) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...

    # Skipped Parse due to it being static, abstract and generic.

    Parse : Parse_MethodGroup
    class Parse_MethodGroup:
        @typing.overload
        def __call__(self, s: str) -> int:...
        @typing.overload
        def __call__(self, s: str, style: NumberStyles) -> int:...
        @typing.overload
        def __call__(self, s: str, provider: IFormatProvider) -> int:...
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], style: NumberStyles = ..., provider: IFormatProvider = ...) -> int:...
        @typing.overload
        def __call__(self, s: str, style: NumberStyles, provider: IFormatProvider) -> int:...

    # Skipped ToString due to it being static, abstract and generic.

    ToString : ToString_MethodGroup
    class ToString_MethodGroup:
        @typing.overload
        def __call__(self) -> str:...
        @typing.overload
        def __call__(self, format: str) -> str:...
        @typing.overload
        def __call__(self, provider: IFormatProvider) -> str:...
        @typing.overload
        def __call__(self, format: str, provider: IFormatProvider) -> str:...

    # Skipped TryParse due to it being static, abstract and generic.

    TryParse : TryParse_MethodGroup
    class TryParse_MethodGroup:
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], result: clr.Reference[int]) -> bool:...
        @typing.overload
        def __call__(self, s: str, result: clr.Reference[int]) -> bool:...
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], style: NumberStyles, provider: IFormatProvider, result: clr.Reference[int]) -> bool:...
        @typing.overload
        def __call__(self, s: str, style: NumberStyles, provider: IFormatProvider, result: clr.Reference[int]) -> bool:...



class UIntPtr(IBinaryInteger_1[UIntPtr], IUnsignedNumber_1[UIntPtr], IMinMaxValue_1[UIntPtr], ISerializable):
    # Constructor .ctor(value : UInt64) was skipped since it collides with above method
    @typing.overload
    def __init__(self, value: int) -> None: ...
    @typing.overload
    def __init__(self, value: clr.Reference[None]) -> None: ...
    Zero : UIntPtr
    @classmethod
    @property
    def MaxValue(cls) -> UIntPtr: ...
    @classmethod
    @property
    def MinValue(cls) -> UIntPtr: ...
    @classmethod
    @property
    def Size(cls) -> int: ...
    @staticmethod
    def Add(pointer: UIntPtr, offset: int) -> UIntPtr: ...
    def GetHashCode(self) -> int: ...
    def __add__(self, pointer: UIntPtr, offset: int) -> UIntPtr: ...
    def __eq__(self, value1: UIntPtr, value2: UIntPtr) -> bool: ...
    # Operator not supported op_Explicit(value: UInt32)
    # Operator not supported op_Explicit(value: UInt64)
    # Operator not supported op_Explicit(value: UIntPtr)
    # Operator not supported op_Explicit(value: UIntPtr)
    # Operator not supported op_Explicit(value: UIntPtr)
    # Operator not supported op_Explicit(value: Void*)
    def __ne__(self, value1: UIntPtr, value2: UIntPtr) -> bool: ...
    def __sub__(self, pointer: UIntPtr, offset: int) -> UIntPtr: ...
    @staticmethod
    def Subtract(pointer: UIntPtr, offset: int) -> UIntPtr: ...
    def ToPointer(self) -> clr.Reference[None]: ...
    def ToUInt32(self) -> int: ...
    def ToUInt64(self) -> int: ...
    def TryFormat(self, destination: Span_1[str], charsWritten: clr.Reference[int], format: ReadOnlySpan_1[str] = ..., provider: IFormatProvider = ...) -> bool: ...
    # Skipped CompareTo due to it being static, abstract and generic.

    CompareTo : CompareTo_MethodGroup
    class CompareTo_MethodGroup:
        @typing.overload
        def __call__(self, value: UIntPtr) -> int:...
        @typing.overload
        def __call__(self, value: typing.Any) -> int:...

    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, other: UIntPtr) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...

    # Skipped Parse due to it being static, abstract and generic.

    Parse : Parse_MethodGroup
    class Parse_MethodGroup:
        @typing.overload
        def __call__(self, s: str) -> UIntPtr:...
        @typing.overload
        def __call__(self, s: str, style: NumberStyles) -> UIntPtr:...
        @typing.overload
        def __call__(self, s: str, provider: IFormatProvider) -> UIntPtr:...
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], style: NumberStyles = ..., provider: IFormatProvider = ...) -> UIntPtr:...
        @typing.overload
        def __call__(self, s: str, style: NumberStyles, provider: IFormatProvider) -> UIntPtr:...

    # Skipped ToString due to it being static, abstract and generic.

    ToString : ToString_MethodGroup
    class ToString_MethodGroup:
        @typing.overload
        def __call__(self) -> str:...
        @typing.overload
        def __call__(self, format: str) -> str:...
        @typing.overload
        def __call__(self, provider: IFormatProvider) -> str:...
        @typing.overload
        def __call__(self, format: str, provider: IFormatProvider) -> str:...

    # Skipped TryParse due to it being static, abstract and generic.

    TryParse : TryParse_MethodGroup
    class TryParse_MethodGroup:
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], result: clr.Reference[UIntPtr]) -> bool:...
        @typing.overload
        def __call__(self, s: str, result: clr.Reference[UIntPtr]) -> bool:...
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], style: NumberStyles, provider: IFormatProvider, result: clr.Reference[UIntPtr]) -> bool:...
        @typing.overload
        def __call__(self, s: str, style: NumberStyles, provider: IFormatProvider, result: clr.Reference[UIntPtr]) -> bool:...



class UnauthorizedAccessException(SystemException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, inner: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...


class UnhandledExceptionEventArgs(EventArgs):
    def __init__(self, exception: typing.Any, isTerminating: bool) -> None: ...
    @property
    def ExceptionObject(self) -> typing.Any: ...
    @property
    def IsTerminating(self) -> bool: ...


class UnhandledExceptionEventHandler(MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, sender: typing.Any, e: UnhandledExceptionEventArgs, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: typing.Any, e: UnhandledExceptionEventArgs) -> None: ...


class UnitySerializationHolder(IObjectReference, ISerializable):
    def __init__(self, info: SerializationInfo, context: StreamingContext) -> None: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...
    def GetRealObject(self, context: StreamingContext) -> typing.Any: ...


class ValueTuple_GenericClasses(abc.ABCMeta):
    Generic_ValueTuple_GenericClasses_ValueTuple_1_T1 = typing.TypeVar('Generic_ValueTuple_GenericClasses_ValueTuple_1_T1')
    @typing.overload
    def __getitem__(self, types : typing.Type[Generic_ValueTuple_GenericClasses_ValueTuple_1_T1]) -> typing.Type[ValueTuple_1[Generic_ValueTuple_GenericClasses_ValueTuple_1_T1]]: ...
    Generic_ValueTuple_GenericClasses_ValueTuple_2_T1 = typing.TypeVar('Generic_ValueTuple_GenericClasses_ValueTuple_2_T1')
    Generic_ValueTuple_GenericClasses_ValueTuple_2_T2 = typing.TypeVar('Generic_ValueTuple_GenericClasses_ValueTuple_2_T2')
    @typing.overload
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_ValueTuple_GenericClasses_ValueTuple_2_T1], typing.Type[Generic_ValueTuple_GenericClasses_ValueTuple_2_T2]]) -> typing.Type[ValueTuple_2[Generic_ValueTuple_GenericClasses_ValueTuple_2_T1, Generic_ValueTuple_GenericClasses_ValueTuple_2_T2]]: ...
    Generic_ValueTuple_GenericClasses_ValueTuple_3_T1 = typing.TypeVar('Generic_ValueTuple_GenericClasses_ValueTuple_3_T1')
    Generic_ValueTuple_GenericClasses_ValueTuple_3_T2 = typing.TypeVar('Generic_ValueTuple_GenericClasses_ValueTuple_3_T2')
    Generic_ValueTuple_GenericClasses_ValueTuple_3_T3 = typing.TypeVar('Generic_ValueTuple_GenericClasses_ValueTuple_3_T3')
    @typing.overload
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_ValueTuple_GenericClasses_ValueTuple_3_T1], typing.Type[Generic_ValueTuple_GenericClasses_ValueTuple_3_T2], typing.Type[Generic_ValueTuple_GenericClasses_ValueTuple_3_T3]]) -> typing.Type[ValueTuple_3[Generic_ValueTuple_GenericClasses_ValueTuple_3_T1, Generic_ValueTuple_GenericClasses_ValueTuple_3_T2, Generic_ValueTuple_GenericClasses_ValueTuple_3_T3]]: ...
    Generic_ValueTuple_GenericClasses_ValueTuple_4_T1 = typing.TypeVar('Generic_ValueTuple_GenericClasses_ValueTuple_4_T1')
    Generic_ValueTuple_GenericClasses_ValueTuple_4_T2 = typing.TypeVar('Generic_ValueTuple_GenericClasses_ValueTuple_4_T2')
    Generic_ValueTuple_GenericClasses_ValueTuple_4_T3 = typing.TypeVar('Generic_ValueTuple_GenericClasses_ValueTuple_4_T3')
    Generic_ValueTuple_GenericClasses_ValueTuple_4_T4 = typing.TypeVar('Generic_ValueTuple_GenericClasses_ValueTuple_4_T4')
    @typing.overload
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_ValueTuple_GenericClasses_ValueTuple_4_T1], typing.Type[Generic_ValueTuple_GenericClasses_ValueTuple_4_T2], typing.Type[Generic_ValueTuple_GenericClasses_ValueTuple_4_T3], typing.Type[Generic_ValueTuple_GenericClasses_ValueTuple_4_T4]]) -> typing.Type[ValueTuple_4[Generic_ValueTuple_GenericClasses_ValueTuple_4_T1, Generic_ValueTuple_GenericClasses_ValueTuple_4_T2, Generic_ValueTuple_GenericClasses_ValueTuple_4_T3, Generic_ValueTuple_GenericClasses_ValueTuple_4_T4]]: ...
    Generic_ValueTuple_GenericClasses_ValueTuple_5_T1 = typing.TypeVar('Generic_ValueTuple_GenericClasses_ValueTuple_5_T1')
    Generic_ValueTuple_GenericClasses_ValueTuple_5_T2 = typing.TypeVar('Generic_ValueTuple_GenericClasses_ValueTuple_5_T2')
    Generic_ValueTuple_GenericClasses_ValueTuple_5_T3 = typing.TypeVar('Generic_ValueTuple_GenericClasses_ValueTuple_5_T3')
    Generic_ValueTuple_GenericClasses_ValueTuple_5_T4 = typing.TypeVar('Generic_ValueTuple_GenericClasses_ValueTuple_5_T4')
    Generic_ValueTuple_GenericClasses_ValueTuple_5_T5 = typing.TypeVar('Generic_ValueTuple_GenericClasses_ValueTuple_5_T5')
    @typing.overload
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_ValueTuple_GenericClasses_ValueTuple_5_T1], typing.Type[Generic_ValueTuple_GenericClasses_ValueTuple_5_T2], typing.Type[Generic_ValueTuple_GenericClasses_ValueTuple_5_T3], typing.Type[Generic_ValueTuple_GenericClasses_ValueTuple_5_T4], typing.Type[Generic_ValueTuple_GenericClasses_ValueTuple_5_T5]]) -> typing.Type[ValueTuple_5[Generic_ValueTuple_GenericClasses_ValueTuple_5_T1, Generic_ValueTuple_GenericClasses_ValueTuple_5_T2, Generic_ValueTuple_GenericClasses_ValueTuple_5_T3, Generic_ValueTuple_GenericClasses_ValueTuple_5_T4, Generic_ValueTuple_GenericClasses_ValueTuple_5_T5]]: ...
    Generic_ValueTuple_GenericClasses_ValueTuple_6_T1 = typing.TypeVar('Generic_ValueTuple_GenericClasses_ValueTuple_6_T1')
    Generic_ValueTuple_GenericClasses_ValueTuple_6_T2 = typing.TypeVar('Generic_ValueTuple_GenericClasses_ValueTuple_6_T2')
    Generic_ValueTuple_GenericClasses_ValueTuple_6_T3 = typing.TypeVar('Generic_ValueTuple_GenericClasses_ValueTuple_6_T3')
    Generic_ValueTuple_GenericClasses_ValueTuple_6_T4 = typing.TypeVar('Generic_ValueTuple_GenericClasses_ValueTuple_6_T4')
    Generic_ValueTuple_GenericClasses_ValueTuple_6_T5 = typing.TypeVar('Generic_ValueTuple_GenericClasses_ValueTuple_6_T5')
    Generic_ValueTuple_GenericClasses_ValueTuple_6_T6 = typing.TypeVar('Generic_ValueTuple_GenericClasses_ValueTuple_6_T6')
    @typing.overload
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_ValueTuple_GenericClasses_ValueTuple_6_T1], typing.Type[Generic_ValueTuple_GenericClasses_ValueTuple_6_T2], typing.Type[Generic_ValueTuple_GenericClasses_ValueTuple_6_T3], typing.Type[Generic_ValueTuple_GenericClasses_ValueTuple_6_T4], typing.Type[Generic_ValueTuple_GenericClasses_ValueTuple_6_T5], typing.Type[Generic_ValueTuple_GenericClasses_ValueTuple_6_T6]]) -> typing.Type[ValueTuple_6[Generic_ValueTuple_GenericClasses_ValueTuple_6_T1, Generic_ValueTuple_GenericClasses_ValueTuple_6_T2, Generic_ValueTuple_GenericClasses_ValueTuple_6_T3, Generic_ValueTuple_GenericClasses_ValueTuple_6_T4, Generic_ValueTuple_GenericClasses_ValueTuple_6_T5, Generic_ValueTuple_GenericClasses_ValueTuple_6_T6]]: ...
    Generic_ValueTuple_GenericClasses_ValueTuple_7_T1 = typing.TypeVar('Generic_ValueTuple_GenericClasses_ValueTuple_7_T1')
    Generic_ValueTuple_GenericClasses_ValueTuple_7_T2 = typing.TypeVar('Generic_ValueTuple_GenericClasses_ValueTuple_7_T2')
    Generic_ValueTuple_GenericClasses_ValueTuple_7_T3 = typing.TypeVar('Generic_ValueTuple_GenericClasses_ValueTuple_7_T3')
    Generic_ValueTuple_GenericClasses_ValueTuple_7_T4 = typing.TypeVar('Generic_ValueTuple_GenericClasses_ValueTuple_7_T4')
    Generic_ValueTuple_GenericClasses_ValueTuple_7_T5 = typing.TypeVar('Generic_ValueTuple_GenericClasses_ValueTuple_7_T5')
    Generic_ValueTuple_GenericClasses_ValueTuple_7_T6 = typing.TypeVar('Generic_ValueTuple_GenericClasses_ValueTuple_7_T6')
    Generic_ValueTuple_GenericClasses_ValueTuple_7_T7 = typing.TypeVar('Generic_ValueTuple_GenericClasses_ValueTuple_7_T7')
    @typing.overload
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_ValueTuple_GenericClasses_ValueTuple_7_T1], typing.Type[Generic_ValueTuple_GenericClasses_ValueTuple_7_T2], typing.Type[Generic_ValueTuple_GenericClasses_ValueTuple_7_T3], typing.Type[Generic_ValueTuple_GenericClasses_ValueTuple_7_T4], typing.Type[Generic_ValueTuple_GenericClasses_ValueTuple_7_T5], typing.Type[Generic_ValueTuple_GenericClasses_ValueTuple_7_T6], typing.Type[Generic_ValueTuple_GenericClasses_ValueTuple_7_T7]]) -> typing.Type[ValueTuple_7[Generic_ValueTuple_GenericClasses_ValueTuple_7_T1, Generic_ValueTuple_GenericClasses_ValueTuple_7_T2, Generic_ValueTuple_GenericClasses_ValueTuple_7_T3, Generic_ValueTuple_GenericClasses_ValueTuple_7_T4, Generic_ValueTuple_GenericClasses_ValueTuple_7_T5, Generic_ValueTuple_GenericClasses_ValueTuple_7_T6, Generic_ValueTuple_GenericClasses_ValueTuple_7_T7]]: ...
    Generic_ValueTuple_GenericClasses_ValueTuple_8_T1 = typing.TypeVar('Generic_ValueTuple_GenericClasses_ValueTuple_8_T1')
    Generic_ValueTuple_GenericClasses_ValueTuple_8_T2 = typing.TypeVar('Generic_ValueTuple_GenericClasses_ValueTuple_8_T2')
    Generic_ValueTuple_GenericClasses_ValueTuple_8_T3 = typing.TypeVar('Generic_ValueTuple_GenericClasses_ValueTuple_8_T3')
    Generic_ValueTuple_GenericClasses_ValueTuple_8_T4 = typing.TypeVar('Generic_ValueTuple_GenericClasses_ValueTuple_8_T4')
    Generic_ValueTuple_GenericClasses_ValueTuple_8_T5 = typing.TypeVar('Generic_ValueTuple_GenericClasses_ValueTuple_8_T5')
    Generic_ValueTuple_GenericClasses_ValueTuple_8_T6 = typing.TypeVar('Generic_ValueTuple_GenericClasses_ValueTuple_8_T6')
    Generic_ValueTuple_GenericClasses_ValueTuple_8_T7 = typing.TypeVar('Generic_ValueTuple_GenericClasses_ValueTuple_8_T7')
    Generic_ValueTuple_GenericClasses_ValueTuple_8_TRest = typing.TypeVar('Generic_ValueTuple_GenericClasses_ValueTuple_8_TRest')
    @typing.overload
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_ValueTuple_GenericClasses_ValueTuple_8_T1], typing.Type[Generic_ValueTuple_GenericClasses_ValueTuple_8_T2], typing.Type[Generic_ValueTuple_GenericClasses_ValueTuple_8_T3], typing.Type[Generic_ValueTuple_GenericClasses_ValueTuple_8_T4], typing.Type[Generic_ValueTuple_GenericClasses_ValueTuple_8_T5], typing.Type[Generic_ValueTuple_GenericClasses_ValueTuple_8_T6], typing.Type[Generic_ValueTuple_GenericClasses_ValueTuple_8_T7], typing.Type[Generic_ValueTuple_GenericClasses_ValueTuple_8_TRest]]) -> typing.Type[ValueTuple_8[Generic_ValueTuple_GenericClasses_ValueTuple_8_T1, Generic_ValueTuple_GenericClasses_ValueTuple_8_T2, Generic_ValueTuple_GenericClasses_ValueTuple_8_T3, Generic_ValueTuple_GenericClasses_ValueTuple_8_T4, Generic_ValueTuple_GenericClasses_ValueTuple_8_T5, Generic_ValueTuple_GenericClasses_ValueTuple_8_T6, Generic_ValueTuple_GenericClasses_ValueTuple_8_T7, Generic_ValueTuple_GenericClasses_ValueTuple_8_TRest]]: ...

class ValueTuple(ValueTuple_0, metaclass =ValueTuple_GenericClasses): ...

class ValueTuple_0(IComparable_1[ValueTuple], IComparable_0, IStructuralComparable, IStructuralEquatable, IEquatable_1[ValueTuple]):
    def CompareTo(self, other: ValueTuple) -> int: ...
    def GetHashCode(self) -> int: ...
    def ToString(self) -> str: ...
    # Skipped Create due to it being static, abstract and generic.

    Create : Create_MethodGroup
    class Create_MethodGroup:
        @typing.overload
        def __getitem__(self, t:typing.Type[Create_1_T1]) -> Create_1[Create_1_T1]: ...

        Create_1_T1 = typing.TypeVar('Create_1_T1')
        class Create_1(typing.Generic[Create_1_T1]):
            Create_1_T1 = ValueTuple_0.Create_MethodGroup.Create_1_T1
            def __call__(self, item1: Create_1_T1) -> ValueTuple_1[Create_1_T1]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Create_2_T1], typing.Type[Create_2_T2]]) -> Create_2[Create_2_T1, Create_2_T2]: ...

        Create_2_T1 = typing.TypeVar('Create_2_T1')
        Create_2_T2 = typing.TypeVar('Create_2_T2')
        class Create_2(typing.Generic[Create_2_T1, Create_2_T2]):
            Create_2_T1 = ValueTuple_0.Create_MethodGroup.Create_2_T1
            Create_2_T2 = ValueTuple_0.Create_MethodGroup.Create_2_T2
            def __call__(self, item1: Create_2_T1, item2: Create_2_T2) -> ValueTuple_2[Create_2_T1, Create_2_T2]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Create_3_T1], typing.Type[Create_3_T2], typing.Type[Create_3_T3]]) -> Create_3[Create_3_T1, Create_3_T2, Create_3_T3]: ...

        Create_3_T1 = typing.TypeVar('Create_3_T1')
        Create_3_T2 = typing.TypeVar('Create_3_T2')
        Create_3_T3 = typing.TypeVar('Create_3_T3')
        class Create_3(typing.Generic[Create_3_T1, Create_3_T2, Create_3_T3]):
            Create_3_T1 = ValueTuple_0.Create_MethodGroup.Create_3_T1
            Create_3_T2 = ValueTuple_0.Create_MethodGroup.Create_3_T2
            Create_3_T3 = ValueTuple_0.Create_MethodGroup.Create_3_T3
            def __call__(self, item1: Create_3_T1, item2: Create_3_T2, item3: Create_3_T3) -> ValueTuple_3[Create_3_T1, Create_3_T2, Create_3_T3]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Create_4_T1], typing.Type[Create_4_T2], typing.Type[Create_4_T3], typing.Type[Create_4_T4]]) -> Create_4[Create_4_T1, Create_4_T2, Create_4_T3, Create_4_T4]: ...

        Create_4_T1 = typing.TypeVar('Create_4_T1')
        Create_4_T2 = typing.TypeVar('Create_4_T2')
        Create_4_T3 = typing.TypeVar('Create_4_T3')
        Create_4_T4 = typing.TypeVar('Create_4_T4')
        class Create_4(typing.Generic[Create_4_T1, Create_4_T2, Create_4_T3, Create_4_T4]):
            Create_4_T1 = ValueTuple_0.Create_MethodGroup.Create_4_T1
            Create_4_T2 = ValueTuple_0.Create_MethodGroup.Create_4_T2
            Create_4_T3 = ValueTuple_0.Create_MethodGroup.Create_4_T3
            Create_4_T4 = ValueTuple_0.Create_MethodGroup.Create_4_T4
            def __call__(self, item1: Create_4_T1, item2: Create_4_T2, item3: Create_4_T3, item4: Create_4_T4) -> ValueTuple_4[Create_4_T1, Create_4_T2, Create_4_T3, Create_4_T4]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Create_5_T1], typing.Type[Create_5_T2], typing.Type[Create_5_T3], typing.Type[Create_5_T4], typing.Type[Create_5_T5]]) -> Create_5[Create_5_T1, Create_5_T2, Create_5_T3, Create_5_T4, Create_5_T5]: ...

        Create_5_T1 = typing.TypeVar('Create_5_T1')
        Create_5_T2 = typing.TypeVar('Create_5_T2')
        Create_5_T3 = typing.TypeVar('Create_5_T3')
        Create_5_T4 = typing.TypeVar('Create_5_T4')
        Create_5_T5 = typing.TypeVar('Create_5_T5')
        class Create_5(typing.Generic[Create_5_T1, Create_5_T2, Create_5_T3, Create_5_T4, Create_5_T5]):
            Create_5_T1 = ValueTuple_0.Create_MethodGroup.Create_5_T1
            Create_5_T2 = ValueTuple_0.Create_MethodGroup.Create_5_T2
            Create_5_T3 = ValueTuple_0.Create_MethodGroup.Create_5_T3
            Create_5_T4 = ValueTuple_0.Create_MethodGroup.Create_5_T4
            Create_5_T5 = ValueTuple_0.Create_MethodGroup.Create_5_T5
            def __call__(self, item1: Create_5_T1, item2: Create_5_T2, item3: Create_5_T3, item4: Create_5_T4, item5: Create_5_T5) -> ValueTuple_5[Create_5_T1, Create_5_T2, Create_5_T3, Create_5_T4, Create_5_T5]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Create_6_T1], typing.Type[Create_6_T2], typing.Type[Create_6_T3], typing.Type[Create_6_T4], typing.Type[Create_6_T5], typing.Type[Create_6_T6]]) -> Create_6[Create_6_T1, Create_6_T2, Create_6_T3, Create_6_T4, Create_6_T5, Create_6_T6]: ...

        Create_6_T1 = typing.TypeVar('Create_6_T1')
        Create_6_T2 = typing.TypeVar('Create_6_T2')
        Create_6_T3 = typing.TypeVar('Create_6_T3')
        Create_6_T4 = typing.TypeVar('Create_6_T4')
        Create_6_T5 = typing.TypeVar('Create_6_T5')
        Create_6_T6 = typing.TypeVar('Create_6_T6')
        class Create_6(typing.Generic[Create_6_T1, Create_6_T2, Create_6_T3, Create_6_T4, Create_6_T5, Create_6_T6]):
            Create_6_T1 = ValueTuple_0.Create_MethodGroup.Create_6_T1
            Create_6_T2 = ValueTuple_0.Create_MethodGroup.Create_6_T2
            Create_6_T3 = ValueTuple_0.Create_MethodGroup.Create_6_T3
            Create_6_T4 = ValueTuple_0.Create_MethodGroup.Create_6_T4
            Create_6_T5 = ValueTuple_0.Create_MethodGroup.Create_6_T5
            Create_6_T6 = ValueTuple_0.Create_MethodGroup.Create_6_T6
            def __call__(self, item1: Create_6_T1, item2: Create_6_T2, item3: Create_6_T3, item4: Create_6_T4, item5: Create_6_T5, item6: Create_6_T6) -> ValueTuple_6[Create_6_T1, Create_6_T2, Create_6_T3, Create_6_T4, Create_6_T5, Create_6_T6]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Create_7_T1], typing.Type[Create_7_T2], typing.Type[Create_7_T3], typing.Type[Create_7_T4], typing.Type[Create_7_T5], typing.Type[Create_7_T6], typing.Type[Create_7_T7]]) -> Create_7[Create_7_T1, Create_7_T2, Create_7_T3, Create_7_T4, Create_7_T5, Create_7_T6, Create_7_T7]: ...

        Create_7_T1 = typing.TypeVar('Create_7_T1')
        Create_7_T2 = typing.TypeVar('Create_7_T2')
        Create_7_T3 = typing.TypeVar('Create_7_T3')
        Create_7_T4 = typing.TypeVar('Create_7_T4')
        Create_7_T5 = typing.TypeVar('Create_7_T5')
        Create_7_T6 = typing.TypeVar('Create_7_T6')
        Create_7_T7 = typing.TypeVar('Create_7_T7')
        class Create_7(typing.Generic[Create_7_T1, Create_7_T2, Create_7_T3, Create_7_T4, Create_7_T5, Create_7_T6, Create_7_T7]):
            Create_7_T1 = ValueTuple_0.Create_MethodGroup.Create_7_T1
            Create_7_T2 = ValueTuple_0.Create_MethodGroup.Create_7_T2
            Create_7_T3 = ValueTuple_0.Create_MethodGroup.Create_7_T3
            Create_7_T4 = ValueTuple_0.Create_MethodGroup.Create_7_T4
            Create_7_T5 = ValueTuple_0.Create_MethodGroup.Create_7_T5
            Create_7_T6 = ValueTuple_0.Create_MethodGroup.Create_7_T6
            Create_7_T7 = ValueTuple_0.Create_MethodGroup.Create_7_T7
            def __call__(self, item1: Create_7_T1, item2: Create_7_T2, item3: Create_7_T3, item4: Create_7_T4, item5: Create_7_T5, item6: Create_7_T6, item7: Create_7_T7) -> ValueTuple_7[Create_7_T1, Create_7_T2, Create_7_T3, Create_7_T4, Create_7_T5, Create_7_T6, Create_7_T7]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Create_8_T1], typing.Type[Create_8_T2], typing.Type[Create_8_T3], typing.Type[Create_8_T4], typing.Type[Create_8_T5], typing.Type[Create_8_T6], typing.Type[Create_8_T7], typing.Type[Create_8_T8]]) -> Create_8[Create_8_T1, Create_8_T2, Create_8_T3, Create_8_T4, Create_8_T5, Create_8_T6, Create_8_T7, Create_8_T8]: ...

        Create_8_T1 = typing.TypeVar('Create_8_T1')
        Create_8_T2 = typing.TypeVar('Create_8_T2')
        Create_8_T3 = typing.TypeVar('Create_8_T3')
        Create_8_T4 = typing.TypeVar('Create_8_T4')
        Create_8_T5 = typing.TypeVar('Create_8_T5')
        Create_8_T6 = typing.TypeVar('Create_8_T6')
        Create_8_T7 = typing.TypeVar('Create_8_T7')
        Create_8_T8 = typing.TypeVar('Create_8_T8')
        class Create_8(typing.Generic[Create_8_T1, Create_8_T2, Create_8_T3, Create_8_T4, Create_8_T5, Create_8_T6, Create_8_T7, Create_8_T8]):
            Create_8_T1 = ValueTuple_0.Create_MethodGroup.Create_8_T1
            Create_8_T2 = ValueTuple_0.Create_MethodGroup.Create_8_T2
            Create_8_T3 = ValueTuple_0.Create_MethodGroup.Create_8_T3
            Create_8_T4 = ValueTuple_0.Create_MethodGroup.Create_8_T4
            Create_8_T5 = ValueTuple_0.Create_MethodGroup.Create_8_T5
            Create_8_T6 = ValueTuple_0.Create_MethodGroup.Create_8_T6
            Create_8_T7 = ValueTuple_0.Create_MethodGroup.Create_8_T7
            Create_8_T8 = ValueTuple_0.Create_MethodGroup.Create_8_T8
            def __call__(self, item1: Create_8_T1, item2: Create_8_T2, item3: Create_8_T3, item4: Create_8_T4, item5: Create_8_T5, item6: Create_8_T6, item7: Create_8_T7, item8: Create_8_T8) -> ValueTuple_8[Create_8_T1, Create_8_T2, Create_8_T3, Create_8_T4, Create_8_T5, Create_8_T6, Create_8_T7, ValueTuple_1[Create_8_T8]]:...

        def __call__(self) -> ValueTuple:...

    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, other: ValueTuple) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...



ValueTuple_1_T1 = typing.TypeVar('ValueTuple_1_T1')
class ValueTuple_1(typing.Generic[ValueTuple_1_T1], IComparable_1[ValueTuple_1[ValueTuple_1_T1]], IComparable_0, IStructuralComparable, IStructuralEquatable, IEquatable_1[ValueTuple_1[ValueTuple_1_T1]]):
    def __init__(self, item1: ValueTuple_1_T1) -> None: ...
    Item1 : ValueTuple_1_T1
    def CompareTo(self, other: ValueTuple_1[ValueTuple_1_T1]) -> int: ...
    def GetHashCode(self) -> int: ...
    def ToString(self) -> str: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup[ValueTuple_1_T1]
    Equals_MethodGroup_ValueTuple_1_T1 = typing.TypeVar('Equals_MethodGroup_ValueTuple_1_T1')
    class Equals_MethodGroup(typing.Generic[Equals_MethodGroup_ValueTuple_1_T1]):
        Equals_MethodGroup_ValueTuple_1_T1 = ValueTuple_1.Equals_MethodGroup_ValueTuple_1_T1
        @typing.overload
        def __call__(self, other: ValueTuple_1[Equals_MethodGroup_ValueTuple_1_T1]) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...



ValueTuple_2_T1 = typing.TypeVar('ValueTuple_2_T1')
ValueTuple_2_T2 = typing.TypeVar('ValueTuple_2_T2')
class ValueTuple_2(typing.Generic[ValueTuple_2_T1, ValueTuple_2_T2], IComparable_1[ValueTuple_2[ValueTuple_2_T1, ValueTuple_2_T2]], IComparable_0, IStructuralComparable, IStructuralEquatable, IEquatable_1[ValueTuple_2[ValueTuple_2_T1, ValueTuple_2_T2]]):
    def __init__(self, item1: ValueTuple_2_T1, item2: ValueTuple_2_T2) -> None: ...
    Item1 : ValueTuple_2_T1
    Item2 : ValueTuple_2_T2
    def CompareTo(self, other: ValueTuple_2[ValueTuple_2_T1, ValueTuple_2_T2]) -> int: ...
    def GetHashCode(self) -> int: ...
    def ToString(self) -> str: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup[ValueTuple_2_T1, ValueTuple_2_T2]
    Equals_MethodGroup_ValueTuple_2_T1 = typing.TypeVar('Equals_MethodGroup_ValueTuple_2_T1')
    Equals_MethodGroup_ValueTuple_2_T2 = typing.TypeVar('Equals_MethodGroup_ValueTuple_2_T2')
    class Equals_MethodGroup(typing.Generic[Equals_MethodGroup_ValueTuple_2_T1, Equals_MethodGroup_ValueTuple_2_T2]):
        Equals_MethodGroup_ValueTuple_2_T1 = ValueTuple_2.Equals_MethodGroup_ValueTuple_2_T1
        Equals_MethodGroup_ValueTuple_2_T2 = ValueTuple_2.Equals_MethodGroup_ValueTuple_2_T2
        @typing.overload
        def __call__(self, other: ValueTuple_2[Equals_MethodGroup_ValueTuple_2_T1, Equals_MethodGroup_ValueTuple_2_T2]) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...



ValueTuple_3_T1 = typing.TypeVar('ValueTuple_3_T1')
ValueTuple_3_T2 = typing.TypeVar('ValueTuple_3_T2')
ValueTuple_3_T3 = typing.TypeVar('ValueTuple_3_T3')
class ValueTuple_3(typing.Generic[ValueTuple_3_T1, ValueTuple_3_T2, ValueTuple_3_T3], IComparable_1[ValueTuple_3[ValueTuple_3_T1, ValueTuple_3_T2, ValueTuple_3_T3]], IComparable_0, IStructuralComparable, IStructuralEquatable, IEquatable_1[ValueTuple_3[ValueTuple_3_T1, ValueTuple_3_T2, ValueTuple_3_T3]]):
    def __init__(self, item1: ValueTuple_3_T1, item2: ValueTuple_3_T2, item3: ValueTuple_3_T3) -> None: ...
    Item1 : ValueTuple_3_T1
    Item2 : ValueTuple_3_T2
    Item3 : ValueTuple_3_T3
    def CompareTo(self, other: ValueTuple_3[ValueTuple_3_T1, ValueTuple_3_T2, ValueTuple_3_T3]) -> int: ...
    def GetHashCode(self) -> int: ...
    def ToString(self) -> str: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup[ValueTuple_3_T1, ValueTuple_3_T2, ValueTuple_3_T3]
    Equals_MethodGroup_ValueTuple_3_T1 = typing.TypeVar('Equals_MethodGroup_ValueTuple_3_T1')
    Equals_MethodGroup_ValueTuple_3_T2 = typing.TypeVar('Equals_MethodGroup_ValueTuple_3_T2')
    Equals_MethodGroup_ValueTuple_3_T3 = typing.TypeVar('Equals_MethodGroup_ValueTuple_3_T3')
    class Equals_MethodGroup(typing.Generic[Equals_MethodGroup_ValueTuple_3_T1, Equals_MethodGroup_ValueTuple_3_T2, Equals_MethodGroup_ValueTuple_3_T3]):
        Equals_MethodGroup_ValueTuple_3_T1 = ValueTuple_3.Equals_MethodGroup_ValueTuple_3_T1
        Equals_MethodGroup_ValueTuple_3_T2 = ValueTuple_3.Equals_MethodGroup_ValueTuple_3_T2
        Equals_MethodGroup_ValueTuple_3_T3 = ValueTuple_3.Equals_MethodGroup_ValueTuple_3_T3
        @typing.overload
        def __call__(self, other: ValueTuple_3[Equals_MethodGroup_ValueTuple_3_T1, Equals_MethodGroup_ValueTuple_3_T2, Equals_MethodGroup_ValueTuple_3_T3]) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...



ValueTuple_4_T1 = typing.TypeVar('ValueTuple_4_T1')
ValueTuple_4_T2 = typing.TypeVar('ValueTuple_4_T2')
ValueTuple_4_T3 = typing.TypeVar('ValueTuple_4_T3')
ValueTuple_4_T4 = typing.TypeVar('ValueTuple_4_T4')
class ValueTuple_4(typing.Generic[ValueTuple_4_T1, ValueTuple_4_T2, ValueTuple_4_T3, ValueTuple_4_T4], IComparable_1[ValueTuple_4[ValueTuple_4_T1, ValueTuple_4_T2, ValueTuple_4_T3, ValueTuple_4_T4]], IComparable_0, IStructuralComparable, IStructuralEquatable, IEquatable_1[ValueTuple_4[ValueTuple_4_T1, ValueTuple_4_T2, ValueTuple_4_T3, ValueTuple_4_T4]]):
    def __init__(self, item1: ValueTuple_4_T1, item2: ValueTuple_4_T2, item3: ValueTuple_4_T3, item4: ValueTuple_4_T4) -> None: ...
    Item1 : ValueTuple_4_T1
    Item2 : ValueTuple_4_T2
    Item3 : ValueTuple_4_T3
    Item4 : ValueTuple_4_T4
    def CompareTo(self, other: ValueTuple_4[ValueTuple_4_T1, ValueTuple_4_T2, ValueTuple_4_T3, ValueTuple_4_T4]) -> int: ...
    def GetHashCode(self) -> int: ...
    def ToString(self) -> str: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup[ValueTuple_4_T1, ValueTuple_4_T2, ValueTuple_4_T3, ValueTuple_4_T4]
    Equals_MethodGroup_ValueTuple_4_T1 = typing.TypeVar('Equals_MethodGroup_ValueTuple_4_T1')
    Equals_MethodGroup_ValueTuple_4_T2 = typing.TypeVar('Equals_MethodGroup_ValueTuple_4_T2')
    Equals_MethodGroup_ValueTuple_4_T3 = typing.TypeVar('Equals_MethodGroup_ValueTuple_4_T3')
    Equals_MethodGroup_ValueTuple_4_T4 = typing.TypeVar('Equals_MethodGroup_ValueTuple_4_T4')
    class Equals_MethodGroup(typing.Generic[Equals_MethodGroup_ValueTuple_4_T1, Equals_MethodGroup_ValueTuple_4_T2, Equals_MethodGroup_ValueTuple_4_T3, Equals_MethodGroup_ValueTuple_4_T4]):
        Equals_MethodGroup_ValueTuple_4_T1 = ValueTuple_4.Equals_MethodGroup_ValueTuple_4_T1
        Equals_MethodGroup_ValueTuple_4_T2 = ValueTuple_4.Equals_MethodGroup_ValueTuple_4_T2
        Equals_MethodGroup_ValueTuple_4_T3 = ValueTuple_4.Equals_MethodGroup_ValueTuple_4_T3
        Equals_MethodGroup_ValueTuple_4_T4 = ValueTuple_4.Equals_MethodGroup_ValueTuple_4_T4
        @typing.overload
        def __call__(self, other: ValueTuple_4[Equals_MethodGroup_ValueTuple_4_T1, Equals_MethodGroup_ValueTuple_4_T2, Equals_MethodGroup_ValueTuple_4_T3, Equals_MethodGroup_ValueTuple_4_T4]) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...



ValueTuple_5_T1 = typing.TypeVar('ValueTuple_5_T1')
ValueTuple_5_T2 = typing.TypeVar('ValueTuple_5_T2')
ValueTuple_5_T3 = typing.TypeVar('ValueTuple_5_T3')
ValueTuple_5_T4 = typing.TypeVar('ValueTuple_5_T4')
ValueTuple_5_T5 = typing.TypeVar('ValueTuple_5_T5')
class ValueTuple_5(typing.Generic[ValueTuple_5_T1, ValueTuple_5_T2, ValueTuple_5_T3, ValueTuple_5_T4, ValueTuple_5_T5], IComparable_1[ValueTuple_5[ValueTuple_5_T1, ValueTuple_5_T2, ValueTuple_5_T3, ValueTuple_5_T4, ValueTuple_5_T5]], IComparable_0, IStructuralComparable, IStructuralEquatable, IEquatable_1[ValueTuple_5[ValueTuple_5_T1, ValueTuple_5_T2, ValueTuple_5_T3, ValueTuple_5_T4, ValueTuple_5_T5]]):
    def __init__(self, item1: ValueTuple_5_T1, item2: ValueTuple_5_T2, item3: ValueTuple_5_T3, item4: ValueTuple_5_T4, item5: ValueTuple_5_T5) -> None: ...
    Item1 : ValueTuple_5_T1
    Item2 : ValueTuple_5_T2
    Item3 : ValueTuple_5_T3
    Item4 : ValueTuple_5_T4
    Item5 : ValueTuple_5_T5
    def CompareTo(self, other: ValueTuple_5[ValueTuple_5_T1, ValueTuple_5_T2, ValueTuple_5_T3, ValueTuple_5_T4, ValueTuple_5_T5]) -> int: ...
    def GetHashCode(self) -> int: ...
    def ToString(self) -> str: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup[ValueTuple_5_T1, ValueTuple_5_T2, ValueTuple_5_T3, ValueTuple_5_T4, ValueTuple_5_T5]
    Equals_MethodGroup_ValueTuple_5_T1 = typing.TypeVar('Equals_MethodGroup_ValueTuple_5_T1')
    Equals_MethodGroup_ValueTuple_5_T2 = typing.TypeVar('Equals_MethodGroup_ValueTuple_5_T2')
    Equals_MethodGroup_ValueTuple_5_T3 = typing.TypeVar('Equals_MethodGroup_ValueTuple_5_T3')
    Equals_MethodGroup_ValueTuple_5_T4 = typing.TypeVar('Equals_MethodGroup_ValueTuple_5_T4')
    Equals_MethodGroup_ValueTuple_5_T5 = typing.TypeVar('Equals_MethodGroup_ValueTuple_5_T5')
    class Equals_MethodGroup(typing.Generic[Equals_MethodGroup_ValueTuple_5_T1, Equals_MethodGroup_ValueTuple_5_T2, Equals_MethodGroup_ValueTuple_5_T3, Equals_MethodGroup_ValueTuple_5_T4, Equals_MethodGroup_ValueTuple_5_T5]):
        Equals_MethodGroup_ValueTuple_5_T1 = ValueTuple_5.Equals_MethodGroup_ValueTuple_5_T1
        Equals_MethodGroup_ValueTuple_5_T2 = ValueTuple_5.Equals_MethodGroup_ValueTuple_5_T2
        Equals_MethodGroup_ValueTuple_5_T3 = ValueTuple_5.Equals_MethodGroup_ValueTuple_5_T3
        Equals_MethodGroup_ValueTuple_5_T4 = ValueTuple_5.Equals_MethodGroup_ValueTuple_5_T4
        Equals_MethodGroup_ValueTuple_5_T5 = ValueTuple_5.Equals_MethodGroup_ValueTuple_5_T5
        @typing.overload
        def __call__(self, other: ValueTuple_5[Equals_MethodGroup_ValueTuple_5_T1, Equals_MethodGroup_ValueTuple_5_T2, Equals_MethodGroup_ValueTuple_5_T3, Equals_MethodGroup_ValueTuple_5_T4, Equals_MethodGroup_ValueTuple_5_T5]) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...



ValueTuple_6_T1 = typing.TypeVar('ValueTuple_6_T1')
ValueTuple_6_T2 = typing.TypeVar('ValueTuple_6_T2')
ValueTuple_6_T3 = typing.TypeVar('ValueTuple_6_T3')
ValueTuple_6_T4 = typing.TypeVar('ValueTuple_6_T4')
ValueTuple_6_T5 = typing.TypeVar('ValueTuple_6_T5')
ValueTuple_6_T6 = typing.TypeVar('ValueTuple_6_T6')
class ValueTuple_6(typing.Generic[ValueTuple_6_T1, ValueTuple_6_T2, ValueTuple_6_T3, ValueTuple_6_T4, ValueTuple_6_T5, ValueTuple_6_T6], IComparable_1[ValueTuple_6[ValueTuple_6_T1, ValueTuple_6_T2, ValueTuple_6_T3, ValueTuple_6_T4, ValueTuple_6_T5, ValueTuple_6_T6]], IComparable_0, IStructuralComparable, IStructuralEquatable, IEquatable_1[ValueTuple_6[ValueTuple_6_T1, ValueTuple_6_T2, ValueTuple_6_T3, ValueTuple_6_T4, ValueTuple_6_T5, ValueTuple_6_T6]]):
    def __init__(self, item1: ValueTuple_6_T1, item2: ValueTuple_6_T2, item3: ValueTuple_6_T3, item4: ValueTuple_6_T4, item5: ValueTuple_6_T5, item6: ValueTuple_6_T6) -> None: ...
    Item1 : ValueTuple_6_T1
    Item2 : ValueTuple_6_T2
    Item3 : ValueTuple_6_T3
    Item4 : ValueTuple_6_T4
    Item5 : ValueTuple_6_T5
    Item6 : ValueTuple_6_T6
    def CompareTo(self, other: ValueTuple_6[ValueTuple_6_T1, ValueTuple_6_T2, ValueTuple_6_T3, ValueTuple_6_T4, ValueTuple_6_T5, ValueTuple_6_T6]) -> int: ...
    def GetHashCode(self) -> int: ...
    def ToString(self) -> str: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup[ValueTuple_6_T1, ValueTuple_6_T2, ValueTuple_6_T3, ValueTuple_6_T4, ValueTuple_6_T5, ValueTuple_6_T6]
    Equals_MethodGroup_ValueTuple_6_T1 = typing.TypeVar('Equals_MethodGroup_ValueTuple_6_T1')
    Equals_MethodGroup_ValueTuple_6_T2 = typing.TypeVar('Equals_MethodGroup_ValueTuple_6_T2')
    Equals_MethodGroup_ValueTuple_6_T3 = typing.TypeVar('Equals_MethodGroup_ValueTuple_6_T3')
    Equals_MethodGroup_ValueTuple_6_T4 = typing.TypeVar('Equals_MethodGroup_ValueTuple_6_T4')
    Equals_MethodGroup_ValueTuple_6_T5 = typing.TypeVar('Equals_MethodGroup_ValueTuple_6_T5')
    Equals_MethodGroup_ValueTuple_6_T6 = typing.TypeVar('Equals_MethodGroup_ValueTuple_6_T6')
    class Equals_MethodGroup(typing.Generic[Equals_MethodGroup_ValueTuple_6_T1, Equals_MethodGroup_ValueTuple_6_T2, Equals_MethodGroup_ValueTuple_6_T3, Equals_MethodGroup_ValueTuple_6_T4, Equals_MethodGroup_ValueTuple_6_T5, Equals_MethodGroup_ValueTuple_6_T6]):
        Equals_MethodGroup_ValueTuple_6_T1 = ValueTuple_6.Equals_MethodGroup_ValueTuple_6_T1
        Equals_MethodGroup_ValueTuple_6_T2 = ValueTuple_6.Equals_MethodGroup_ValueTuple_6_T2
        Equals_MethodGroup_ValueTuple_6_T3 = ValueTuple_6.Equals_MethodGroup_ValueTuple_6_T3
        Equals_MethodGroup_ValueTuple_6_T4 = ValueTuple_6.Equals_MethodGroup_ValueTuple_6_T4
        Equals_MethodGroup_ValueTuple_6_T5 = ValueTuple_6.Equals_MethodGroup_ValueTuple_6_T5
        Equals_MethodGroup_ValueTuple_6_T6 = ValueTuple_6.Equals_MethodGroup_ValueTuple_6_T6
        @typing.overload
        def __call__(self, other: ValueTuple_6[Equals_MethodGroup_ValueTuple_6_T1, Equals_MethodGroup_ValueTuple_6_T2, Equals_MethodGroup_ValueTuple_6_T3, Equals_MethodGroup_ValueTuple_6_T4, Equals_MethodGroup_ValueTuple_6_T5, Equals_MethodGroup_ValueTuple_6_T6]) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...



ValueTuple_7_T1 = typing.TypeVar('ValueTuple_7_T1')
ValueTuple_7_T2 = typing.TypeVar('ValueTuple_7_T2')
ValueTuple_7_T3 = typing.TypeVar('ValueTuple_7_T3')
ValueTuple_7_T4 = typing.TypeVar('ValueTuple_7_T4')
ValueTuple_7_T5 = typing.TypeVar('ValueTuple_7_T5')
ValueTuple_7_T6 = typing.TypeVar('ValueTuple_7_T6')
ValueTuple_7_T7 = typing.TypeVar('ValueTuple_7_T7')
class ValueTuple_7(typing.Generic[ValueTuple_7_T1, ValueTuple_7_T2, ValueTuple_7_T3, ValueTuple_7_T4, ValueTuple_7_T5, ValueTuple_7_T6, ValueTuple_7_T7], IComparable_1[ValueTuple_7[ValueTuple_7_T1, ValueTuple_7_T2, ValueTuple_7_T3, ValueTuple_7_T4, ValueTuple_7_T5, ValueTuple_7_T6, ValueTuple_7_T7]], IComparable_0, IStructuralComparable, IStructuralEquatable, IEquatable_1[ValueTuple_7[ValueTuple_7_T1, ValueTuple_7_T2, ValueTuple_7_T3, ValueTuple_7_T4, ValueTuple_7_T5, ValueTuple_7_T6, ValueTuple_7_T7]]):
    def __init__(self, item1: ValueTuple_7_T1, item2: ValueTuple_7_T2, item3: ValueTuple_7_T3, item4: ValueTuple_7_T4, item5: ValueTuple_7_T5, item6: ValueTuple_7_T6, item7: ValueTuple_7_T7) -> None: ...
    Item1 : ValueTuple_7_T1
    Item2 : ValueTuple_7_T2
    Item3 : ValueTuple_7_T3
    Item4 : ValueTuple_7_T4
    Item5 : ValueTuple_7_T5
    Item6 : ValueTuple_7_T6
    Item7 : ValueTuple_7_T7
    def CompareTo(self, other: ValueTuple_7[ValueTuple_7_T1, ValueTuple_7_T2, ValueTuple_7_T3, ValueTuple_7_T4, ValueTuple_7_T5, ValueTuple_7_T6, ValueTuple_7_T7]) -> int: ...
    def GetHashCode(self) -> int: ...
    def ToString(self) -> str: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup[ValueTuple_7_T1, ValueTuple_7_T2, ValueTuple_7_T3, ValueTuple_7_T4, ValueTuple_7_T5, ValueTuple_7_T6, ValueTuple_7_T7]
    Equals_MethodGroup_ValueTuple_7_T1 = typing.TypeVar('Equals_MethodGroup_ValueTuple_7_T1')
    Equals_MethodGroup_ValueTuple_7_T2 = typing.TypeVar('Equals_MethodGroup_ValueTuple_7_T2')
    Equals_MethodGroup_ValueTuple_7_T3 = typing.TypeVar('Equals_MethodGroup_ValueTuple_7_T3')
    Equals_MethodGroup_ValueTuple_7_T4 = typing.TypeVar('Equals_MethodGroup_ValueTuple_7_T4')
    Equals_MethodGroup_ValueTuple_7_T5 = typing.TypeVar('Equals_MethodGroup_ValueTuple_7_T5')
    Equals_MethodGroup_ValueTuple_7_T6 = typing.TypeVar('Equals_MethodGroup_ValueTuple_7_T6')
    Equals_MethodGroup_ValueTuple_7_T7 = typing.TypeVar('Equals_MethodGroup_ValueTuple_7_T7')
    class Equals_MethodGroup(typing.Generic[Equals_MethodGroup_ValueTuple_7_T1, Equals_MethodGroup_ValueTuple_7_T2, Equals_MethodGroup_ValueTuple_7_T3, Equals_MethodGroup_ValueTuple_7_T4, Equals_MethodGroup_ValueTuple_7_T5, Equals_MethodGroup_ValueTuple_7_T6, Equals_MethodGroup_ValueTuple_7_T7]):
        Equals_MethodGroup_ValueTuple_7_T1 = ValueTuple_7.Equals_MethodGroup_ValueTuple_7_T1
        Equals_MethodGroup_ValueTuple_7_T2 = ValueTuple_7.Equals_MethodGroup_ValueTuple_7_T2
        Equals_MethodGroup_ValueTuple_7_T3 = ValueTuple_7.Equals_MethodGroup_ValueTuple_7_T3
        Equals_MethodGroup_ValueTuple_7_T4 = ValueTuple_7.Equals_MethodGroup_ValueTuple_7_T4
        Equals_MethodGroup_ValueTuple_7_T5 = ValueTuple_7.Equals_MethodGroup_ValueTuple_7_T5
        Equals_MethodGroup_ValueTuple_7_T6 = ValueTuple_7.Equals_MethodGroup_ValueTuple_7_T6
        Equals_MethodGroup_ValueTuple_7_T7 = ValueTuple_7.Equals_MethodGroup_ValueTuple_7_T7
        @typing.overload
        def __call__(self, other: ValueTuple_7[Equals_MethodGroup_ValueTuple_7_T1, Equals_MethodGroup_ValueTuple_7_T2, Equals_MethodGroup_ValueTuple_7_T3, Equals_MethodGroup_ValueTuple_7_T4, Equals_MethodGroup_ValueTuple_7_T5, Equals_MethodGroup_ValueTuple_7_T6, Equals_MethodGroup_ValueTuple_7_T7]) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...



ValueTuple_8_T1 = typing.TypeVar('ValueTuple_8_T1')
ValueTuple_8_T2 = typing.TypeVar('ValueTuple_8_T2')
ValueTuple_8_T3 = typing.TypeVar('ValueTuple_8_T3')
ValueTuple_8_T4 = typing.TypeVar('ValueTuple_8_T4')
ValueTuple_8_T5 = typing.TypeVar('ValueTuple_8_T5')
ValueTuple_8_T6 = typing.TypeVar('ValueTuple_8_T6')
ValueTuple_8_T7 = typing.TypeVar('ValueTuple_8_T7')
ValueTuple_8_TRest = typing.TypeVar('ValueTuple_8_TRest')
class ValueTuple_8(typing.Generic[ValueTuple_8_T1, ValueTuple_8_T2, ValueTuple_8_T3, ValueTuple_8_T4, ValueTuple_8_T5, ValueTuple_8_T6, ValueTuple_8_T7, ValueTuple_8_TRest], IComparable_1[ValueTuple_8[ValueTuple_8_T1, ValueTuple_8_T2, ValueTuple_8_T3, ValueTuple_8_T4, ValueTuple_8_T5, ValueTuple_8_T6, ValueTuple_8_T7, ValueTuple_8_TRest]], IComparable_0, IStructuralComparable, IStructuralEquatable, IEquatable_1[ValueTuple_8[ValueTuple_8_T1, ValueTuple_8_T2, ValueTuple_8_T3, ValueTuple_8_T4, ValueTuple_8_T5, ValueTuple_8_T6, ValueTuple_8_T7, ValueTuple_8_TRest]]):
    def __init__(self, item1: ValueTuple_8_T1, item2: ValueTuple_8_T2, item3: ValueTuple_8_T3, item4: ValueTuple_8_T4, item5: ValueTuple_8_T5, item6: ValueTuple_8_T6, item7: ValueTuple_8_T7, rest: ValueTuple_8_TRest) -> None: ...
    Item1 : ValueTuple_8_T1
    Item2 : ValueTuple_8_T2
    Item3 : ValueTuple_8_T3
    Item4 : ValueTuple_8_T4
    Item5 : ValueTuple_8_T5
    Item6 : ValueTuple_8_T6
    Item7 : ValueTuple_8_T7
    Rest : ValueTuple_8_TRest
    def CompareTo(self, other: ValueTuple_8[ValueTuple_8_T1, ValueTuple_8_T2, ValueTuple_8_T3, ValueTuple_8_T4, ValueTuple_8_T5, ValueTuple_8_T6, ValueTuple_8_T7, ValueTuple_8_TRest]) -> int: ...
    def GetHashCode(self) -> int: ...
    def ToString(self) -> str: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup[ValueTuple_8_T1, ValueTuple_8_T2, ValueTuple_8_T3, ValueTuple_8_T4, ValueTuple_8_T5, ValueTuple_8_T6, ValueTuple_8_T7, ValueTuple_8_TRest]
    Equals_MethodGroup_ValueTuple_8_T1 = typing.TypeVar('Equals_MethodGroup_ValueTuple_8_T1')
    Equals_MethodGroup_ValueTuple_8_T2 = typing.TypeVar('Equals_MethodGroup_ValueTuple_8_T2')
    Equals_MethodGroup_ValueTuple_8_T3 = typing.TypeVar('Equals_MethodGroup_ValueTuple_8_T3')
    Equals_MethodGroup_ValueTuple_8_T4 = typing.TypeVar('Equals_MethodGroup_ValueTuple_8_T4')
    Equals_MethodGroup_ValueTuple_8_T5 = typing.TypeVar('Equals_MethodGroup_ValueTuple_8_T5')
    Equals_MethodGroup_ValueTuple_8_T6 = typing.TypeVar('Equals_MethodGroup_ValueTuple_8_T6')
    Equals_MethodGroup_ValueTuple_8_T7 = typing.TypeVar('Equals_MethodGroup_ValueTuple_8_T7')
    Equals_MethodGroup_ValueTuple_8_TRest = typing.TypeVar('Equals_MethodGroup_ValueTuple_8_TRest')
    class Equals_MethodGroup(typing.Generic[Equals_MethodGroup_ValueTuple_8_T1, Equals_MethodGroup_ValueTuple_8_T2, Equals_MethodGroup_ValueTuple_8_T3, Equals_MethodGroup_ValueTuple_8_T4, Equals_MethodGroup_ValueTuple_8_T5, Equals_MethodGroup_ValueTuple_8_T6, Equals_MethodGroup_ValueTuple_8_T7, Equals_MethodGroup_ValueTuple_8_TRest]):
        Equals_MethodGroup_ValueTuple_8_T1 = ValueTuple_8.Equals_MethodGroup_ValueTuple_8_T1
        Equals_MethodGroup_ValueTuple_8_T2 = ValueTuple_8.Equals_MethodGroup_ValueTuple_8_T2
        Equals_MethodGroup_ValueTuple_8_T3 = ValueTuple_8.Equals_MethodGroup_ValueTuple_8_T3
        Equals_MethodGroup_ValueTuple_8_T4 = ValueTuple_8.Equals_MethodGroup_ValueTuple_8_T4
        Equals_MethodGroup_ValueTuple_8_T5 = ValueTuple_8.Equals_MethodGroup_ValueTuple_8_T5
        Equals_MethodGroup_ValueTuple_8_T6 = ValueTuple_8.Equals_MethodGroup_ValueTuple_8_T6
        Equals_MethodGroup_ValueTuple_8_T7 = ValueTuple_8.Equals_MethodGroup_ValueTuple_8_T7
        Equals_MethodGroup_ValueTuple_8_TRest = ValueTuple_8.Equals_MethodGroup_ValueTuple_8_TRest
        @typing.overload
        def __call__(self, other: ValueTuple_8[Equals_MethodGroup_ValueTuple_8_T1, Equals_MethodGroup_ValueTuple_8_T2, Equals_MethodGroup_ValueTuple_8_T3, Equals_MethodGroup_ValueTuple_8_T4, Equals_MethodGroup_ValueTuple_8_T5, Equals_MethodGroup_ValueTuple_8_T6, Equals_MethodGroup_ValueTuple_8_T7, Equals_MethodGroup_ValueTuple_8_TRest]) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...



class ValueType(abc.ABC):
    def Equals(self, obj: typing.Any) -> bool: ...
    def GetHashCode(self) -> int: ...
    def ToString(self) -> str: ...


class Version(ISpanFormattable, IEquatable_1[Version], IComparable_1[Version], IComparable_0, ICloneable):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, major: int, minor: int) -> None: ...
    @typing.overload
    def __init__(self, major: int, minor: int, build: int) -> None: ...
    @typing.overload
    def __init__(self, major: int, minor: int, build: int, revision: int) -> None: ...
    @typing.overload
    def __init__(self, version: str) -> None: ...
    @property
    def Build(self) -> int: ...
    @property
    def Major(self) -> int: ...
    @property
    def MajorRevision(self) -> int: ...
    @property
    def Minor(self) -> int: ...
    @property
    def MinorRevision(self) -> int: ...
    @property
    def Revision(self) -> int: ...
    def Clone(self) -> typing.Any: ...
    def GetHashCode(self) -> int: ...
    def __eq__(self, v1: Version, v2: Version) -> bool: ...
    def __gt__(self, v1: Version, v2: Version) -> bool: ...
    def __ge__(self, v1: Version, v2: Version) -> bool: ...
    def __ne__(self, v1: Version, v2: Version) -> bool: ...
    def __lt__(self, v1: Version, v2: Version) -> bool: ...
    def __le__(self, v1: Version, v2: Version) -> bool: ...
    # Skipped CompareTo due to it being static, abstract and generic.

    CompareTo : CompareTo_MethodGroup
    class CompareTo_MethodGroup:
        @typing.overload
        def __call__(self, value: Version) -> int:...
        @typing.overload
        def __call__(self, version: typing.Any) -> int:...

    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, obj: Version) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...

    # Skipped Parse due to it being static, abstract and generic.

    Parse : Parse_MethodGroup
    class Parse_MethodGroup:
        @typing.overload
        def __call__(self, input: ReadOnlySpan_1[str]) -> Version:...
        @typing.overload
        def __call__(self, input: str) -> Version:...

    # Skipped ToString due to it being static, abstract and generic.

    ToString : ToString_MethodGroup
    class ToString_MethodGroup:
        @typing.overload
        def __call__(self) -> str:...
        @typing.overload
        def __call__(self, fieldCount: int) -> str:...

    # Skipped TryFormat due to it being static, abstract and generic.

    TryFormat : TryFormat_MethodGroup
    class TryFormat_MethodGroup:
        @typing.overload
        def __call__(self, destination: Span_1[str], charsWritten: clr.Reference[int]) -> bool:...
        @typing.overload
        def __call__(self, destination: Span_1[str], fieldCount: int, charsWritten: clr.Reference[int]) -> bool:...

    # Skipped TryParse due to it being static, abstract and generic.

    TryParse : TryParse_MethodGroup
    class TryParse_MethodGroup:
        @typing.overload
        def __call__(self, input: ReadOnlySpan_1[str], result: clr.Reference[Version]) -> bool:...
        @typing.overload
        def __call__(self, input: str, result: clr.Reference[Version]) -> bool:...



class Void:
    pass


class WeakReference_GenericClasses(abc.ABCMeta):
    Generic_WeakReference_GenericClasses_WeakReference_1_T = typing.TypeVar('Generic_WeakReference_GenericClasses_WeakReference_1_T')
    def __getitem__(self, types : typing.Type[Generic_WeakReference_GenericClasses_WeakReference_1_T]) -> typing.Type[WeakReference_1[Generic_WeakReference_GenericClasses_WeakReference_1_T]]: ...

class WeakReference(WeakReference_0, metaclass =WeakReference_GenericClasses): ...

class WeakReference_0(ISerializable):
    @typing.overload
    def __init__(self, target: typing.Any) -> None: ...
    @typing.overload
    def __init__(self, target: typing.Any, trackResurrection: bool) -> None: ...
    @property
    def IsAlive(self) -> bool: ...
    @property
    def Target(self) -> typing.Any: ...
    @Target.setter
    def Target(self, value: typing.Any) -> typing.Any: ...
    @property
    def TrackResurrection(self) -> bool: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...


WeakReference_1_T = typing.TypeVar('WeakReference_1_T')
class WeakReference_1(typing.Generic[WeakReference_1_T], ISerializable):
    @typing.overload
    def __init__(self, target: WeakReference_1_T) -> None: ...
    @typing.overload
    def __init__(self, target: WeakReference_1_T, trackResurrection: bool) -> None: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...
    def SetTarget(self, target: WeakReference_1_T) -> None: ...
    def TryGetTarget(self, target: clr.Reference[WeakReference_1_T]) -> bool: ...

