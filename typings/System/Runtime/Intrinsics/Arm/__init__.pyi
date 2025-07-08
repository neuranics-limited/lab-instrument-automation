import typing, clr, abc
from System.Runtime.Intrinsics import Vector64_1, Vector128_1

class AdvSimd(ArmBase):
    @classmethod
    @property
    def IsSupported(cls) -> bool: ...
    @staticmethod
    def ConvertToInt32RoundAwayFromZeroScalar(value: Vector64_1[float]) -> Vector64_1[int]: ...
    @staticmethod
    def ConvertToInt32RoundToEvenScalar(value: Vector64_1[float]) -> Vector64_1[int]: ...
    @staticmethod
    def ConvertToInt32RoundToNegativeInfinityScalar(value: Vector64_1[float]) -> Vector64_1[int]: ...
    @staticmethod
    def ConvertToInt32RoundToPositiveInfinityScalar(value: Vector64_1[float]) -> Vector64_1[int]: ...
    @staticmethod
    def ConvertToInt32RoundToZeroScalar(value: Vector64_1[float]) -> Vector64_1[int]: ...
    @staticmethod
    def ConvertToUInt32RoundAwayFromZeroScalar(value: Vector64_1[float]) -> Vector64_1[int]: ...
    @staticmethod
    def ConvertToUInt32RoundToEvenScalar(value: Vector64_1[float]) -> Vector64_1[int]: ...
    @staticmethod
    def ConvertToUInt32RoundToNegativeInfinityScalar(value: Vector64_1[float]) -> Vector64_1[int]: ...
    @staticmethod
    def ConvertToUInt32RoundToPositiveInfinityScalar(value: Vector64_1[float]) -> Vector64_1[int]: ...
    @staticmethod
    def ConvertToUInt32RoundToZeroScalar(value: Vector64_1[float]) -> Vector64_1[int]: ...
    @staticmethod
    def ShiftArithmeticRoundedSaturateScalar(value: Vector64_1[int], count: Vector64_1[int]) -> Vector64_1[int]: ...
    @staticmethod
    def ShiftArithmeticRoundedScalar(value: Vector64_1[int], count: Vector64_1[int]) -> Vector64_1[int]: ...
    @staticmethod
    def ShiftArithmeticSaturateScalar(value: Vector64_1[int], count: Vector64_1[int]) -> Vector64_1[int]: ...
    @staticmethod
    def ShiftArithmeticScalar(value: Vector64_1[int], count: Vector64_1[int]) -> Vector64_1[int]: ...
    @staticmethod
    def ShiftLeftLogicalSaturateUnsignedScalar(value: Vector64_1[int], count: int) -> Vector64_1[int]: ...
    @staticmethod
    def ShiftRightArithmeticAddScalar(addend: Vector64_1[int], value: Vector64_1[int], count: int) -> Vector64_1[int]: ...
    @staticmethod
    def ShiftRightArithmeticRoundedAddScalar(addend: Vector64_1[int], value: Vector64_1[int], count: int) -> Vector64_1[int]: ...
    @staticmethod
    def ShiftRightArithmeticRoundedScalar(value: Vector64_1[int], count: int) -> Vector64_1[int]: ...
    @staticmethod
    def ShiftRightArithmeticScalar(value: Vector64_1[int], count: int) -> Vector64_1[int]: ...
    # Skipped Abs due to it being static, abstract and generic.

    Abs : Abs_MethodGroup
    class Abs_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector64_1[float]) -> Vector64_1[float]:...
        @typing.overload
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[float]:...
        # Method Abs(value : Vector64`1) was skipped since it collides with above method
        # Method Abs(value : Vector64`1) was skipped since it collides with above method
        # Method Abs(value : Vector64`1) was skipped since it collides with above method
        # Method Abs(value : Vector128`1) was skipped since it collides with above method
        # Method Abs(value : Vector128`1) was skipped since it collides with above method
        # Method Abs(value : Vector128`1) was skipped since it collides with above method

    # Skipped AbsoluteCompareGreaterThan due to it being static, abstract and generic.

    AbsoluteCompareGreaterThan : AbsoluteCompareGreaterThan_MethodGroup
    class AbsoluteCompareGreaterThan_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
        @typing.overload
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...

    # Skipped AbsoluteCompareGreaterThanOrEqual due to it being static, abstract and generic.

    AbsoluteCompareGreaterThanOrEqual : AbsoluteCompareGreaterThanOrEqual_MethodGroup
    class AbsoluteCompareGreaterThanOrEqual_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
        @typing.overload
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...

    # Skipped AbsoluteCompareLessThan due to it being static, abstract and generic.

    AbsoluteCompareLessThan : AbsoluteCompareLessThan_MethodGroup
    class AbsoluteCompareLessThan_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
        @typing.overload
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...

    # Skipped AbsoluteCompareLessThanOrEqual due to it being static, abstract and generic.

    AbsoluteCompareLessThanOrEqual : AbsoluteCompareLessThanOrEqual_MethodGroup
    class AbsoluteCompareLessThanOrEqual_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
        @typing.overload
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...

    # Skipped AbsoluteDifference due to it being static, abstract and generic.

    AbsoluteDifference : AbsoluteDifference_MethodGroup
    class AbsoluteDifference_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
        @typing.overload
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
        # Method AbsoluteDifference(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method AbsoluteDifference(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method AbsoluteDifference(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method AbsoluteDifference(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method AbsoluteDifference(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method AbsoluteDifference(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method AbsoluteDifference(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AbsoluteDifference(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AbsoluteDifference(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AbsoluteDifference(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AbsoluteDifference(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AbsoluteDifference(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped AbsoluteDifferenceAdd due to it being static, abstract and generic.

    AbsoluteDifferenceAdd : AbsoluteDifferenceAdd_MethodGroup
    class AbsoluteDifferenceAdd_MethodGroup:
        @typing.overload
        def __call__(self, addend: Vector64_1[int], left: Vector64_1[int], right: Vector64_1[int]) -> Vector64_1[int]:...
        # Method AbsoluteDifferenceAdd(addend : Vector64`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method AbsoluteDifferenceAdd(addend : Vector64`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method AbsoluteDifferenceAdd(addend : Vector64`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method AbsoluteDifferenceAdd(addend : Vector64`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method AbsoluteDifferenceAdd(addend : Vector64`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, addend: Vector128_1[int], left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
        # Method AbsoluteDifferenceAdd(addend : Vector128`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AbsoluteDifferenceAdd(addend : Vector128`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AbsoluteDifferenceAdd(addend : Vector128`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AbsoluteDifferenceAdd(addend : Vector128`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AbsoluteDifferenceAdd(addend : Vector128`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped AbsoluteDifferenceWideningLower due to it being static, abstract and generic.

    AbsoluteDifferenceWideningLower : AbsoluteDifferenceWideningLower_MethodGroup
    class AbsoluteDifferenceWideningLower_MethodGroup:
        def __call__(self, left: Vector64_1[int], right: Vector64_1[int]) -> Vector128_1[int]:...
        # Method AbsoluteDifferenceWideningLower(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method AbsoluteDifferenceWideningLower(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method AbsoluteDifferenceWideningLower(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method AbsoluteDifferenceWideningLower(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method AbsoluteDifferenceWideningLower(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

    # Skipped AbsoluteDifferenceWideningLowerAndAdd due to it being static, abstract and generic.

    AbsoluteDifferenceWideningLowerAndAdd : AbsoluteDifferenceWideningLowerAndAdd_MethodGroup
    class AbsoluteDifferenceWideningLowerAndAdd_MethodGroup:
        def __call__(self, addend: Vector128_1[int], left: Vector64_1[int], right: Vector64_1[int]) -> Vector128_1[int]:...
        # Method AbsoluteDifferenceWideningLowerAndAdd(addend : Vector128`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method AbsoluteDifferenceWideningLowerAndAdd(addend : Vector128`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method AbsoluteDifferenceWideningLowerAndAdd(addend : Vector128`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method AbsoluteDifferenceWideningLowerAndAdd(addend : Vector128`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method AbsoluteDifferenceWideningLowerAndAdd(addend : Vector128`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

    # Skipped AbsoluteDifferenceWideningUpper due to it being static, abstract and generic.

    AbsoluteDifferenceWideningUpper : AbsoluteDifferenceWideningUpper_MethodGroup
    class AbsoluteDifferenceWideningUpper_MethodGroup:
        def __call__(self, left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
        # Method AbsoluteDifferenceWideningUpper(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AbsoluteDifferenceWideningUpper(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AbsoluteDifferenceWideningUpper(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AbsoluteDifferenceWideningUpper(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AbsoluteDifferenceWideningUpper(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped AbsoluteDifferenceWideningUpperAndAdd due to it being static, abstract and generic.

    AbsoluteDifferenceWideningUpperAndAdd : AbsoluteDifferenceWideningUpperAndAdd_MethodGroup
    class AbsoluteDifferenceWideningUpperAndAdd_MethodGroup:
        def __call__(self, addend: Vector128_1[int], left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
        # Method AbsoluteDifferenceWideningUpperAndAdd(addend : Vector128`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AbsoluteDifferenceWideningUpperAndAdd(addend : Vector128`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AbsoluteDifferenceWideningUpperAndAdd(addend : Vector128`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AbsoluteDifferenceWideningUpperAndAdd(addend : Vector128`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AbsoluteDifferenceWideningUpperAndAdd(addend : Vector128`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped AbsSaturate due to it being static, abstract and generic.

    AbsSaturate : AbsSaturate_MethodGroup
    class AbsSaturate_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector64_1[int]) -> Vector64_1[int]:...
        # Method AbsSaturate(value : Vector64`1) was skipped since it collides with above method
        # Method AbsSaturate(value : Vector64`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector128_1[int]) -> Vector128_1[int]:...
        # Method AbsSaturate(value : Vector128`1) was skipped since it collides with above method
        # Method AbsSaturate(value : Vector128`1) was skipped since it collides with above method

    # Skipped AbsScalar due to it being static, abstract and generic.

    AbsScalar : AbsScalar_MethodGroup
    class AbsScalar_MethodGroup:
        def __call__(self, value: Vector64_1[float]) -> Vector64_1[float]:...
        # Method AbsScalar(value : Vector64`1) was skipped since it collides with above method

    # Skipped Add due to it being static, abstract and generic.

    Add : Add_MethodGroup
    class Add_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
        @typing.overload
        def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
        # Method Add(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Add(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Add(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Add(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Add(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Add(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method Add(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method Add(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method Add(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method Add(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method Add(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method Add(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Add(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Add(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped AddHighNarrowingLower due to it being static, abstract and generic.

    AddHighNarrowingLower : AddHighNarrowingLower_MethodGroup
    class AddHighNarrowingLower_MethodGroup:
        def __call__(self, left: Vector128_1[int], right: Vector128_1[int]) -> Vector64_1[int]:...
        # Method AddHighNarrowingLower(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AddHighNarrowingLower(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AddHighNarrowingLower(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AddHighNarrowingLower(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AddHighNarrowingLower(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped AddHighNarrowingUpper due to it being static, abstract and generic.

    AddHighNarrowingUpper : AddHighNarrowingUpper_MethodGroup
    class AddHighNarrowingUpper_MethodGroup:
        def __call__(self, lower: Vector64_1[int], left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
        # Method AddHighNarrowingUpper(lower : Vector64`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AddHighNarrowingUpper(lower : Vector64`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AddHighNarrowingUpper(lower : Vector64`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AddHighNarrowingUpper(lower : Vector64`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AddHighNarrowingUpper(lower : Vector64`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped AddPairwise due to it being static, abstract and generic.

    AddPairwise : AddPairwise_MethodGroup
    class AddPairwise_MethodGroup:
        def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
        # Method AddPairwise(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method AddPairwise(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method AddPairwise(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method AddPairwise(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method AddPairwise(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method AddPairwise(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

    # Skipped AddPairwiseWidening due to it being static, abstract and generic.

    AddPairwiseWidening : AddPairwiseWidening_MethodGroup
    class AddPairwiseWidening_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector64_1[int]) -> Vector64_1[int]:...
        # Method AddPairwiseWidening(value : Vector64`1) was skipped since it collides with above method
        # Method AddPairwiseWidening(value : Vector64`1) was skipped since it collides with above method
        # Method AddPairwiseWidening(value : Vector64`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector128_1[int]) -> Vector128_1[int]:...
        # Method AddPairwiseWidening(value : Vector128`1) was skipped since it collides with above method
        # Method AddPairwiseWidening(value : Vector128`1) was skipped since it collides with above method
        # Method AddPairwiseWidening(value : Vector128`1) was skipped since it collides with above method
        # Method AddPairwiseWidening(value : Vector128`1) was skipped since it collides with above method
        # Method AddPairwiseWidening(value : Vector128`1) was skipped since it collides with above method

    # Skipped AddPairwiseWideningAndAdd due to it being static, abstract and generic.

    AddPairwiseWideningAndAdd : AddPairwiseWideningAndAdd_MethodGroup
    class AddPairwiseWideningAndAdd_MethodGroup:
        @typing.overload
        def __call__(self, addend: Vector64_1[int], value: Vector64_1[int]) -> Vector64_1[int]:...
        # Method AddPairwiseWideningAndAdd(addend : Vector64`1, value : Vector64`1) was skipped since it collides with above method
        # Method AddPairwiseWideningAndAdd(addend : Vector64`1, value : Vector64`1) was skipped since it collides with above method
        # Method AddPairwiseWideningAndAdd(addend : Vector64`1, value : Vector64`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, addend: Vector128_1[int], value: Vector128_1[int]) -> Vector128_1[int]:...
        # Method AddPairwiseWideningAndAdd(addend : Vector128`1, value : Vector128`1) was skipped since it collides with above method
        # Method AddPairwiseWideningAndAdd(addend : Vector128`1, value : Vector128`1) was skipped since it collides with above method
        # Method AddPairwiseWideningAndAdd(addend : Vector128`1, value : Vector128`1) was skipped since it collides with above method
        # Method AddPairwiseWideningAndAdd(addend : Vector128`1, value : Vector128`1) was skipped since it collides with above method
        # Method AddPairwiseWideningAndAdd(addend : Vector128`1, value : Vector128`1) was skipped since it collides with above method

    # Skipped AddPairwiseWideningAndAddScalar due to it being static, abstract and generic.

    AddPairwiseWideningAndAddScalar : AddPairwiseWideningAndAddScalar_MethodGroup
    class AddPairwiseWideningAndAddScalar_MethodGroup:
        def __call__(self, addend: Vector64_1[int], value: Vector64_1[int]) -> Vector64_1[int]:...
        # Method AddPairwiseWideningAndAddScalar(addend : Vector64`1, value : Vector64`1) was skipped since it collides with above method

    # Skipped AddPairwiseWideningScalar due to it being static, abstract and generic.

    AddPairwiseWideningScalar : AddPairwiseWideningScalar_MethodGroup
    class AddPairwiseWideningScalar_MethodGroup:
        def __call__(self, value: Vector64_1[int]) -> Vector64_1[int]:...
        # Method AddPairwiseWideningScalar(value : Vector64`1) was skipped since it collides with above method

    # Skipped AddRoundedHighNarrowingLower due to it being static, abstract and generic.

    AddRoundedHighNarrowingLower : AddRoundedHighNarrowingLower_MethodGroup
    class AddRoundedHighNarrowingLower_MethodGroup:
        def __call__(self, left: Vector128_1[int], right: Vector128_1[int]) -> Vector64_1[int]:...
        # Method AddRoundedHighNarrowingLower(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AddRoundedHighNarrowingLower(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AddRoundedHighNarrowingLower(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AddRoundedHighNarrowingLower(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AddRoundedHighNarrowingLower(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped AddRoundedHighNarrowingUpper due to it being static, abstract and generic.

    AddRoundedHighNarrowingUpper : AddRoundedHighNarrowingUpper_MethodGroup
    class AddRoundedHighNarrowingUpper_MethodGroup:
        def __call__(self, lower: Vector64_1[int], left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
        # Method AddRoundedHighNarrowingUpper(lower : Vector64`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AddRoundedHighNarrowingUpper(lower : Vector64`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AddRoundedHighNarrowingUpper(lower : Vector64`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AddRoundedHighNarrowingUpper(lower : Vector64`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AddRoundedHighNarrowingUpper(lower : Vector64`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped AddSaturate due to it being static, abstract and generic.

    AddSaturate : AddSaturate_MethodGroup
    class AddSaturate_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector64_1[int], right: Vector64_1[int]) -> Vector64_1[int]:...
        # Method AddSaturate(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method AddSaturate(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method AddSaturate(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method AddSaturate(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method AddSaturate(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
        # Method AddSaturate(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AddSaturate(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AddSaturate(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AddSaturate(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AddSaturate(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AddSaturate(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AddSaturate(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped AddSaturateScalar due to it being static, abstract and generic.

    AddSaturateScalar : AddSaturateScalar_MethodGroup
    class AddSaturateScalar_MethodGroup:
        def __call__(self, left: Vector64_1[int], right: Vector64_1[int]) -> Vector64_1[int]:...
        # Method AddSaturateScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

    # Skipped AddScalar due to it being static, abstract and generic.

    AddScalar : AddScalar_MethodGroup
    class AddScalar_MethodGroup:
        def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
        # Method AddScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method AddScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method AddScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

    # Skipped AddWideningLower due to it being static, abstract and generic.

    AddWideningLower : AddWideningLower_MethodGroup
    class AddWideningLower_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector64_1[int], right: Vector64_1[int]) -> Vector128_1[int]:...
        # Method AddWideningLower(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, left: Vector128_1[int], right: Vector64_1[int]) -> Vector128_1[int]:...
        # Method AddWideningLower(left : Vector128`1, right : Vector64`1) was skipped since it collides with above method
        # Method AddWideningLower(left : Vector128`1, right : Vector64`1) was skipped since it collides with above method
        # Method AddWideningLower(left : Vector128`1, right : Vector64`1) was skipped since it collides with above method
        # Method AddWideningLower(left : Vector128`1, right : Vector64`1) was skipped since it collides with above method
        # Method AddWideningLower(left : Vector128`1, right : Vector64`1) was skipped since it collides with above method
        # Method AddWideningLower(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method AddWideningLower(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method AddWideningLower(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method AddWideningLower(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

    # Skipped AddWideningUpper due to it being static, abstract and generic.

    AddWideningUpper : AddWideningUpper_MethodGroup
    class AddWideningUpper_MethodGroup:
        def __call__(self, left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
        # Method AddWideningUpper(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AddWideningUpper(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AddWideningUpper(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AddWideningUpper(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AddWideningUpper(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AddWideningUpper(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AddWideningUpper(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AddWideningUpper(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AddWideningUpper(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AddWideningUpper(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AddWideningUpper(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped And due to it being static, abstract and generic.

    And : And_MethodGroup
    class And_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
        # Method And(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
        # Method And(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method And(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method And(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method And(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method And(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method And(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method And(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method And(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method And(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method And(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method And(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method And(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method And(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method And(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method And(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method And(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method And(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped BitwiseClear due to it being static, abstract and generic.

    BitwiseClear : BitwiseClear_MethodGroup
    class BitwiseClear_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector64_1[float], mask: Vector64_1[float]) -> Vector64_1[float]:...
        # Method BitwiseClear(value : Vector64`1, mask : Vector64`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector128_1[float], mask: Vector128_1[float]) -> Vector128_1[float]:...
        # Method BitwiseClear(value : Vector128`1, mask : Vector128`1) was skipped since it collides with above method
        # Method BitwiseClear(value : Vector64`1, mask : Vector64`1) was skipped since it collides with above method
        # Method BitwiseClear(value : Vector64`1, mask : Vector64`1) was skipped since it collides with above method
        # Method BitwiseClear(value : Vector64`1, mask : Vector64`1) was skipped since it collides with above method
        # Method BitwiseClear(value : Vector64`1, mask : Vector64`1) was skipped since it collides with above method
        # Method BitwiseClear(value : Vector64`1, mask : Vector64`1) was skipped since it collides with above method
        # Method BitwiseClear(value : Vector64`1, mask : Vector64`1) was skipped since it collides with above method
        # Method BitwiseClear(value : Vector64`1, mask : Vector64`1) was skipped since it collides with above method
        # Method BitwiseClear(value : Vector64`1, mask : Vector64`1) was skipped since it collides with above method
        # Method BitwiseClear(value : Vector128`1, mask : Vector128`1) was skipped since it collides with above method
        # Method BitwiseClear(value : Vector128`1, mask : Vector128`1) was skipped since it collides with above method
        # Method BitwiseClear(value : Vector128`1, mask : Vector128`1) was skipped since it collides with above method
        # Method BitwiseClear(value : Vector128`1, mask : Vector128`1) was skipped since it collides with above method
        # Method BitwiseClear(value : Vector128`1, mask : Vector128`1) was skipped since it collides with above method
        # Method BitwiseClear(value : Vector128`1, mask : Vector128`1) was skipped since it collides with above method
        # Method BitwiseClear(value : Vector128`1, mask : Vector128`1) was skipped since it collides with above method
        # Method BitwiseClear(value : Vector128`1, mask : Vector128`1) was skipped since it collides with above method

    # Skipped BitwiseSelect due to it being static, abstract and generic.

    BitwiseSelect : BitwiseSelect_MethodGroup
    class BitwiseSelect_MethodGroup:
        @typing.overload
        def __call__(self, select: Vector64_1[float], left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
        # Method BitwiseSelect(select : Vector64`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, select: Vector128_1[float], left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
        # Method BitwiseSelect(select : Vector128`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method BitwiseSelect(select : Vector64`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method BitwiseSelect(select : Vector64`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method BitwiseSelect(select : Vector64`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method BitwiseSelect(select : Vector64`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method BitwiseSelect(select : Vector64`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method BitwiseSelect(select : Vector64`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method BitwiseSelect(select : Vector64`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method BitwiseSelect(select : Vector64`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method BitwiseSelect(select : Vector128`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method BitwiseSelect(select : Vector128`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method BitwiseSelect(select : Vector128`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method BitwiseSelect(select : Vector128`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method BitwiseSelect(select : Vector128`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method BitwiseSelect(select : Vector128`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method BitwiseSelect(select : Vector128`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method BitwiseSelect(select : Vector128`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped Ceiling due to it being static, abstract and generic.

    Ceiling : Ceiling_MethodGroup
    class Ceiling_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector64_1[float]) -> Vector64_1[float]:...
        @typing.overload
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[float]:...

    # Skipped CeilingScalar due to it being static, abstract and generic.

    CeilingScalar : CeilingScalar_MethodGroup
    class CeilingScalar_MethodGroup:
        def __call__(self, value: Vector64_1[float]) -> Vector64_1[float]:...
        # Method CeilingScalar(value : Vector64`1) was skipped since it collides with above method

    # Skipped CompareEqual due to it being static, abstract and generic.

    CompareEqual : CompareEqual_MethodGroup
    class CompareEqual_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
        @typing.overload
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
        # Method CompareEqual(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method CompareEqual(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method CompareEqual(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method CompareEqual(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method CompareEqual(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method CompareEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareEqual(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

    # Skipped CompareGreaterThan due to it being static, abstract and generic.

    CompareGreaterThan : CompareGreaterThan_MethodGroup
    class CompareGreaterThan_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
        @typing.overload
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
        # Method CompareGreaterThan(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method CompareGreaterThan(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method CompareGreaterThan(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method CompareGreaterThan(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method CompareGreaterThan(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method CompareGreaterThan(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method CompareGreaterThan(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareGreaterThan(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareGreaterThan(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareGreaterThan(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareGreaterThan(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareGreaterThan(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped CompareGreaterThanOrEqual due to it being static, abstract and generic.

    CompareGreaterThanOrEqual : CompareGreaterThanOrEqual_MethodGroup
    class CompareGreaterThanOrEqual_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
        @typing.overload
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
        # Method CompareGreaterThanOrEqual(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method CompareGreaterThanOrEqual(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method CompareGreaterThanOrEqual(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method CompareGreaterThanOrEqual(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method CompareGreaterThanOrEqual(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method CompareGreaterThanOrEqual(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method CompareGreaterThanOrEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareGreaterThanOrEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareGreaterThanOrEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareGreaterThanOrEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareGreaterThanOrEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareGreaterThanOrEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped CompareLessThan due to it being static, abstract and generic.

    CompareLessThan : CompareLessThan_MethodGroup
    class CompareLessThan_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
        @typing.overload
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
        # Method CompareLessThan(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method CompareLessThan(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method CompareLessThan(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method CompareLessThan(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method CompareLessThan(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method CompareLessThan(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method CompareLessThan(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareLessThan(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareLessThan(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareLessThan(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareLessThan(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareLessThan(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped CompareLessThanOrEqual due to it being static, abstract and generic.

    CompareLessThanOrEqual : CompareLessThanOrEqual_MethodGroup
    class CompareLessThanOrEqual_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
        @typing.overload
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
        # Method CompareLessThanOrEqual(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method CompareLessThanOrEqual(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method CompareLessThanOrEqual(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method CompareLessThanOrEqual(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method CompareLessThanOrEqual(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method CompareLessThanOrEqual(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method CompareLessThanOrEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareLessThanOrEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareLessThanOrEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareLessThanOrEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareLessThanOrEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareLessThanOrEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped CompareTest due to it being static, abstract and generic.

    CompareTest : CompareTest_MethodGroup
    class CompareTest_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
        @typing.overload
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
        # Method CompareTest(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method CompareTest(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method CompareTest(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method CompareTest(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method CompareTest(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method CompareTest(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method CompareTest(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareTest(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareTest(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareTest(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareTest(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareTest(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped ConvertToInt32RoundAwayFromZero due to it being static, abstract and generic.

    ConvertToInt32RoundAwayFromZero : ConvertToInt32RoundAwayFromZero_MethodGroup
    class ConvertToInt32RoundAwayFromZero_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector64_1[float]) -> Vector64_1[int]:...
        @typing.overload
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[int]:...

    # Skipped ConvertToInt32RoundToEven due to it being static, abstract and generic.

    ConvertToInt32RoundToEven : ConvertToInt32RoundToEven_MethodGroup
    class ConvertToInt32RoundToEven_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector64_1[float]) -> Vector64_1[int]:...
        @typing.overload
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[int]:...

    # Skipped ConvertToInt32RoundToNegativeInfinity due to it being static, abstract and generic.

    ConvertToInt32RoundToNegativeInfinity : ConvertToInt32RoundToNegativeInfinity_MethodGroup
    class ConvertToInt32RoundToNegativeInfinity_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector64_1[float]) -> Vector64_1[int]:...
        @typing.overload
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[int]:...

    # Skipped ConvertToInt32RoundToPositiveInfinity due to it being static, abstract and generic.

    ConvertToInt32RoundToPositiveInfinity : ConvertToInt32RoundToPositiveInfinity_MethodGroup
    class ConvertToInt32RoundToPositiveInfinity_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector64_1[float]) -> Vector64_1[int]:...
        @typing.overload
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[int]:...

    # Skipped ConvertToInt32RoundToZero due to it being static, abstract and generic.

    ConvertToInt32RoundToZero : ConvertToInt32RoundToZero_MethodGroup
    class ConvertToInt32RoundToZero_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector64_1[float]) -> Vector64_1[int]:...
        @typing.overload
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[int]:...

    # Skipped ConvertToSingle due to it being static, abstract and generic.

    ConvertToSingle : ConvertToSingle_MethodGroup
    class ConvertToSingle_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector64_1[int]) -> Vector64_1[float]:...
        # Method ConvertToSingle(value : Vector64`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector128_1[int]) -> Vector128_1[float]:...
        # Method ConvertToSingle(value : Vector128`1) was skipped since it collides with above method

    # Skipped ConvertToSingleScalar due to it being static, abstract and generic.

    ConvertToSingleScalar : ConvertToSingleScalar_MethodGroup
    class ConvertToSingleScalar_MethodGroup:
        def __call__(self, value: Vector64_1[int]) -> Vector64_1[float]:...
        # Method ConvertToSingleScalar(value : Vector64`1) was skipped since it collides with above method

    # Skipped ConvertToUInt32RoundAwayFromZero due to it being static, abstract and generic.

    ConvertToUInt32RoundAwayFromZero : ConvertToUInt32RoundAwayFromZero_MethodGroup
    class ConvertToUInt32RoundAwayFromZero_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector64_1[float]) -> Vector64_1[int]:...
        @typing.overload
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[int]:...

    # Skipped ConvertToUInt32RoundToEven due to it being static, abstract and generic.

    ConvertToUInt32RoundToEven : ConvertToUInt32RoundToEven_MethodGroup
    class ConvertToUInt32RoundToEven_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector64_1[float]) -> Vector64_1[int]:...
        @typing.overload
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[int]:...

    # Skipped ConvertToUInt32RoundToNegativeInfinity due to it being static, abstract and generic.

    ConvertToUInt32RoundToNegativeInfinity : ConvertToUInt32RoundToNegativeInfinity_MethodGroup
    class ConvertToUInt32RoundToNegativeInfinity_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector64_1[float]) -> Vector64_1[int]:...
        @typing.overload
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[int]:...

    # Skipped ConvertToUInt32RoundToPositiveInfinity due to it being static, abstract and generic.

    ConvertToUInt32RoundToPositiveInfinity : ConvertToUInt32RoundToPositiveInfinity_MethodGroup
    class ConvertToUInt32RoundToPositiveInfinity_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector64_1[float]) -> Vector64_1[int]:...
        @typing.overload
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[int]:...

    # Skipped ConvertToUInt32RoundToZero due to it being static, abstract and generic.

    ConvertToUInt32RoundToZero : ConvertToUInt32RoundToZero_MethodGroup
    class ConvertToUInt32RoundToZero_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector64_1[float]) -> Vector64_1[int]:...
        @typing.overload
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[int]:...

    # Skipped DivideScalar due to it being static, abstract and generic.

    DivideScalar : DivideScalar_MethodGroup
    class DivideScalar_MethodGroup:
        def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
        # Method DivideScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

    # Skipped DuplicateSelectedScalarToVector128 due to it being static, abstract and generic.

    DuplicateSelectedScalarToVector128 : DuplicateSelectedScalarToVector128_MethodGroup
    class DuplicateSelectedScalarToVector128_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector64_1[float], index: int) -> Vector128_1[float]:...
        @typing.overload
        def __call__(self, value: Vector128_1[float], index: int) -> Vector128_1[float]:...
        # Method DuplicateSelectedScalarToVector128(value : Vector64`1, index : Byte) was skipped since it collides with above method
        # Method DuplicateSelectedScalarToVector128(value : Vector64`1, index : Byte) was skipped since it collides with above method
        # Method DuplicateSelectedScalarToVector128(value : Vector64`1, index : Byte) was skipped since it collides with above method
        # Method DuplicateSelectedScalarToVector128(value : Vector64`1, index : Byte) was skipped since it collides with above method
        # Method DuplicateSelectedScalarToVector128(value : Vector64`1, index : Byte) was skipped since it collides with above method
        # Method DuplicateSelectedScalarToVector128(value : Vector64`1, index : Byte) was skipped since it collides with above method
        # Method DuplicateSelectedScalarToVector128(value : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method DuplicateSelectedScalarToVector128(value : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method DuplicateSelectedScalarToVector128(value : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method DuplicateSelectedScalarToVector128(value : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method DuplicateSelectedScalarToVector128(value : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method DuplicateSelectedScalarToVector128(value : Vector128`1, index : Byte) was skipped since it collides with above method

    # Skipped DuplicateSelectedScalarToVector64 due to it being static, abstract and generic.

    DuplicateSelectedScalarToVector64 : DuplicateSelectedScalarToVector64_MethodGroup
    class DuplicateSelectedScalarToVector64_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector64_1[float], index: int) -> Vector64_1[float]:...
        @typing.overload
        def __call__(self, value: Vector128_1[float], index: int) -> Vector64_1[float]:...
        # Method DuplicateSelectedScalarToVector64(value : Vector64`1, index : Byte) was skipped since it collides with above method
        # Method DuplicateSelectedScalarToVector64(value : Vector64`1, index : Byte) was skipped since it collides with above method
        # Method DuplicateSelectedScalarToVector64(value : Vector64`1, index : Byte) was skipped since it collides with above method
        # Method DuplicateSelectedScalarToVector64(value : Vector64`1, index : Byte) was skipped since it collides with above method
        # Method DuplicateSelectedScalarToVector64(value : Vector64`1, index : Byte) was skipped since it collides with above method
        # Method DuplicateSelectedScalarToVector64(value : Vector64`1, index : Byte) was skipped since it collides with above method
        # Method DuplicateSelectedScalarToVector64(value : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method DuplicateSelectedScalarToVector64(value : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method DuplicateSelectedScalarToVector64(value : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method DuplicateSelectedScalarToVector64(value : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method DuplicateSelectedScalarToVector64(value : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method DuplicateSelectedScalarToVector64(value : Vector128`1, index : Byte) was skipped since it collides with above method

    # Skipped DuplicateToVector128 due to it being static, abstract and generic.

    DuplicateToVector128 : DuplicateToVector128_MethodGroup
    class DuplicateToVector128_MethodGroup:
        def __call__(self, value: float) -> Vector128_1[float]:...
        # Method DuplicateToVector128(value : Byte) was skipped since it collides with above method
        # Method DuplicateToVector128(value : Int16) was skipped since it collides with above method
        # Method DuplicateToVector128(value : Int32) was skipped since it collides with above method
        # Method DuplicateToVector128(value : SByte) was skipped since it collides with above method
        # Method DuplicateToVector128(value : UInt16) was skipped since it collides with above method
        # Method DuplicateToVector128(value : UInt32) was skipped since it collides with above method

    # Skipped DuplicateToVector64 due to it being static, abstract and generic.

    DuplicateToVector64 : DuplicateToVector64_MethodGroup
    class DuplicateToVector64_MethodGroup:
        def __call__(self, value: float) -> Vector64_1[float]:...
        # Method DuplicateToVector64(value : Byte) was skipped since it collides with above method
        # Method DuplicateToVector64(value : Int16) was skipped since it collides with above method
        # Method DuplicateToVector64(value : Int32) was skipped since it collides with above method
        # Method DuplicateToVector64(value : SByte) was skipped since it collides with above method
        # Method DuplicateToVector64(value : UInt16) was skipped since it collides with above method
        # Method DuplicateToVector64(value : UInt32) was skipped since it collides with above method

    # Skipped Extract due to it being static, abstract and generic.

    Extract : Extract_MethodGroup
    class Extract_MethodGroup:
        @typing.overload
        def __call__(self, vector: Vector128_1[float], index: int) -> float:...
        # Method Extract(vector : Vector128`1, index : Byte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, vector: Vector64_1[float], index: int) -> float:...
        # Method Extract(vector : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method Extract(vector : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method Extract(vector : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method Extract(vector : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method Extract(vector : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method Extract(vector : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method Extract(vector : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method Extract(vector : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method Extract(vector : Vector64`1, index : Byte) was skipped since it collides with above method
        # Method Extract(vector : Vector64`1, index : Byte) was skipped since it collides with above method
        # Method Extract(vector : Vector64`1, index : Byte) was skipped since it collides with above method
        # Method Extract(vector : Vector64`1, index : Byte) was skipped since it collides with above method
        # Method Extract(vector : Vector64`1, index : Byte) was skipped since it collides with above method
        # Method Extract(vector : Vector64`1, index : Byte) was skipped since it collides with above method

    # Skipped ExtractNarrowingLower due to it being static, abstract and generic.

    ExtractNarrowingLower : ExtractNarrowingLower_MethodGroup
    class ExtractNarrowingLower_MethodGroup:
        def __call__(self, value: Vector128_1[int]) -> Vector64_1[int]:...
        # Method ExtractNarrowingLower(value : Vector128`1) was skipped since it collides with above method
        # Method ExtractNarrowingLower(value : Vector128`1) was skipped since it collides with above method
        # Method ExtractNarrowingLower(value : Vector128`1) was skipped since it collides with above method
        # Method ExtractNarrowingLower(value : Vector128`1) was skipped since it collides with above method
        # Method ExtractNarrowingLower(value : Vector128`1) was skipped since it collides with above method

    # Skipped ExtractNarrowingSaturateLower due to it being static, abstract and generic.

    ExtractNarrowingSaturateLower : ExtractNarrowingSaturateLower_MethodGroup
    class ExtractNarrowingSaturateLower_MethodGroup:
        def __call__(self, value: Vector128_1[int]) -> Vector64_1[int]:...
        # Method ExtractNarrowingSaturateLower(value : Vector128`1) was skipped since it collides with above method
        # Method ExtractNarrowingSaturateLower(value : Vector128`1) was skipped since it collides with above method
        # Method ExtractNarrowingSaturateLower(value : Vector128`1) was skipped since it collides with above method
        # Method ExtractNarrowingSaturateLower(value : Vector128`1) was skipped since it collides with above method
        # Method ExtractNarrowingSaturateLower(value : Vector128`1) was skipped since it collides with above method

    # Skipped ExtractNarrowingSaturateUnsignedLower due to it being static, abstract and generic.

    ExtractNarrowingSaturateUnsignedLower : ExtractNarrowingSaturateUnsignedLower_MethodGroup
    class ExtractNarrowingSaturateUnsignedLower_MethodGroup:
        def __call__(self, value: Vector128_1[int]) -> Vector64_1[int]:...
        # Method ExtractNarrowingSaturateUnsignedLower(value : Vector128`1) was skipped since it collides with above method
        # Method ExtractNarrowingSaturateUnsignedLower(value : Vector128`1) was skipped since it collides with above method

    # Skipped ExtractNarrowingSaturateUnsignedUpper due to it being static, abstract and generic.

    ExtractNarrowingSaturateUnsignedUpper : ExtractNarrowingSaturateUnsignedUpper_MethodGroup
    class ExtractNarrowingSaturateUnsignedUpper_MethodGroup:
        def __call__(self, lower: Vector64_1[int], value: Vector128_1[int]) -> Vector128_1[int]:...
        # Method ExtractNarrowingSaturateUnsignedUpper(lower : Vector64`1, value : Vector128`1) was skipped since it collides with above method
        # Method ExtractNarrowingSaturateUnsignedUpper(lower : Vector64`1, value : Vector128`1) was skipped since it collides with above method

    # Skipped ExtractNarrowingSaturateUpper due to it being static, abstract and generic.

    ExtractNarrowingSaturateUpper : ExtractNarrowingSaturateUpper_MethodGroup
    class ExtractNarrowingSaturateUpper_MethodGroup:
        def __call__(self, lower: Vector64_1[int], value: Vector128_1[int]) -> Vector128_1[int]:...
        # Method ExtractNarrowingSaturateUpper(lower : Vector64`1, value : Vector128`1) was skipped since it collides with above method
        # Method ExtractNarrowingSaturateUpper(lower : Vector64`1, value : Vector128`1) was skipped since it collides with above method
        # Method ExtractNarrowingSaturateUpper(lower : Vector64`1, value : Vector128`1) was skipped since it collides with above method
        # Method ExtractNarrowingSaturateUpper(lower : Vector64`1, value : Vector128`1) was skipped since it collides with above method
        # Method ExtractNarrowingSaturateUpper(lower : Vector64`1, value : Vector128`1) was skipped since it collides with above method

    # Skipped ExtractNarrowingUpper due to it being static, abstract and generic.

    ExtractNarrowingUpper : ExtractNarrowingUpper_MethodGroup
    class ExtractNarrowingUpper_MethodGroup:
        def __call__(self, lower: Vector64_1[int], value: Vector128_1[int]) -> Vector128_1[int]:...
        # Method ExtractNarrowingUpper(lower : Vector64`1, value : Vector128`1) was skipped since it collides with above method
        # Method ExtractNarrowingUpper(lower : Vector64`1, value : Vector128`1) was skipped since it collides with above method
        # Method ExtractNarrowingUpper(lower : Vector64`1, value : Vector128`1) was skipped since it collides with above method
        # Method ExtractNarrowingUpper(lower : Vector64`1, value : Vector128`1) was skipped since it collides with above method
        # Method ExtractNarrowingUpper(lower : Vector64`1, value : Vector128`1) was skipped since it collides with above method

    # Skipped ExtractVector128 due to it being static, abstract and generic.

    ExtractVector128 : ExtractVector128_MethodGroup
    class ExtractVector128_MethodGroup:
        def __call__(self, upper: Vector128_1[float], lower: Vector128_1[float], index: int) -> Vector128_1[float]:...
        # Method ExtractVector128(upper : Vector128`1, lower : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method ExtractVector128(upper : Vector128`1, lower : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method ExtractVector128(upper : Vector128`1, lower : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method ExtractVector128(upper : Vector128`1, lower : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method ExtractVector128(upper : Vector128`1, lower : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method ExtractVector128(upper : Vector128`1, lower : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method ExtractVector128(upper : Vector128`1, lower : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method ExtractVector128(upper : Vector128`1, lower : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method ExtractVector128(upper : Vector128`1, lower : Vector128`1, index : Byte) was skipped since it collides with above method

    # Skipped ExtractVector64 due to it being static, abstract and generic.

    ExtractVector64 : ExtractVector64_MethodGroup
    class ExtractVector64_MethodGroup:
        def __call__(self, upper: Vector64_1[float], lower: Vector64_1[float], index: int) -> Vector64_1[float]:...
        # Method ExtractVector64(upper : Vector64`1, lower : Vector64`1, index : Byte) was skipped since it collides with above method
        # Method ExtractVector64(upper : Vector64`1, lower : Vector64`1, index : Byte) was skipped since it collides with above method
        # Method ExtractVector64(upper : Vector64`1, lower : Vector64`1, index : Byte) was skipped since it collides with above method
        # Method ExtractVector64(upper : Vector64`1, lower : Vector64`1, index : Byte) was skipped since it collides with above method
        # Method ExtractVector64(upper : Vector64`1, lower : Vector64`1, index : Byte) was skipped since it collides with above method
        # Method ExtractVector64(upper : Vector64`1, lower : Vector64`1, index : Byte) was skipped since it collides with above method

    # Skipped Floor due to it being static, abstract and generic.

    Floor : Floor_MethodGroup
    class Floor_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector64_1[float]) -> Vector64_1[float]:...
        @typing.overload
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[float]:...

    # Skipped FloorScalar due to it being static, abstract and generic.

    FloorScalar : FloorScalar_MethodGroup
    class FloorScalar_MethodGroup:
        def __call__(self, value: Vector64_1[float]) -> Vector64_1[float]:...
        # Method FloorScalar(value : Vector64`1) was skipped since it collides with above method

    # Skipped FusedAddHalving due to it being static, abstract and generic.

    FusedAddHalving : FusedAddHalving_MethodGroup
    class FusedAddHalving_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector64_1[int], right: Vector64_1[int]) -> Vector64_1[int]:...
        # Method FusedAddHalving(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method FusedAddHalving(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method FusedAddHalving(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method FusedAddHalving(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method FusedAddHalving(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
        # Method FusedAddHalving(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method FusedAddHalving(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method FusedAddHalving(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method FusedAddHalving(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method FusedAddHalving(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped FusedAddRoundedHalving due to it being static, abstract and generic.

    FusedAddRoundedHalving : FusedAddRoundedHalving_MethodGroup
    class FusedAddRoundedHalving_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector64_1[int], right: Vector64_1[int]) -> Vector64_1[int]:...
        # Method FusedAddRoundedHalving(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method FusedAddRoundedHalving(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method FusedAddRoundedHalving(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method FusedAddRoundedHalving(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method FusedAddRoundedHalving(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
        # Method FusedAddRoundedHalving(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method FusedAddRoundedHalving(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method FusedAddRoundedHalving(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method FusedAddRoundedHalving(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method FusedAddRoundedHalving(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped FusedMultiplyAdd due to it being static, abstract and generic.

    FusedMultiplyAdd : FusedMultiplyAdd_MethodGroup
    class FusedMultiplyAdd_MethodGroup:
        @typing.overload
        def __call__(self, addend: Vector64_1[float], left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
        @typing.overload
        def __call__(self, addend: Vector128_1[float], left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...

    # Skipped FusedMultiplyAddNegatedScalar due to it being static, abstract and generic.

    FusedMultiplyAddNegatedScalar : FusedMultiplyAddNegatedScalar_MethodGroup
    class FusedMultiplyAddNegatedScalar_MethodGroup:
        def __call__(self, addend: Vector64_1[float], left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
        # Method FusedMultiplyAddNegatedScalar(addend : Vector64`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

    # Skipped FusedMultiplyAddScalar due to it being static, abstract and generic.

    FusedMultiplyAddScalar : FusedMultiplyAddScalar_MethodGroup
    class FusedMultiplyAddScalar_MethodGroup:
        def __call__(self, addend: Vector64_1[float], left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
        # Method FusedMultiplyAddScalar(addend : Vector64`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

    # Skipped FusedMultiplySubtract due to it being static, abstract and generic.

    FusedMultiplySubtract : FusedMultiplySubtract_MethodGroup
    class FusedMultiplySubtract_MethodGroup:
        @typing.overload
        def __call__(self, minuend: Vector64_1[float], left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
        @typing.overload
        def __call__(self, minuend: Vector128_1[float], left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...

    # Skipped FusedMultiplySubtractNegatedScalar due to it being static, abstract and generic.

    FusedMultiplySubtractNegatedScalar : FusedMultiplySubtractNegatedScalar_MethodGroup
    class FusedMultiplySubtractNegatedScalar_MethodGroup:
        def __call__(self, minuend: Vector64_1[float], left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
        # Method FusedMultiplySubtractNegatedScalar(minuend : Vector64`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

    # Skipped FusedMultiplySubtractScalar due to it being static, abstract and generic.

    FusedMultiplySubtractScalar : FusedMultiplySubtractScalar_MethodGroup
    class FusedMultiplySubtractScalar_MethodGroup:
        def __call__(self, minuend: Vector64_1[float], left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
        # Method FusedMultiplySubtractScalar(minuend : Vector64`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

    # Skipped FusedSubtractHalving due to it being static, abstract and generic.

    FusedSubtractHalving : FusedSubtractHalving_MethodGroup
    class FusedSubtractHalving_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector64_1[int], right: Vector64_1[int]) -> Vector64_1[int]:...
        # Method FusedSubtractHalving(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method FusedSubtractHalving(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method FusedSubtractHalving(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method FusedSubtractHalving(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method FusedSubtractHalving(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
        # Method FusedSubtractHalving(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method FusedSubtractHalving(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method FusedSubtractHalving(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method FusedSubtractHalving(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method FusedSubtractHalving(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped Insert due to it being static, abstract and generic.

    Insert : Insert_MethodGroup
    class Insert_MethodGroup:
        @typing.overload
        def __call__(self, vector: Vector64_1[float], index: int, data: float) -> Vector64_1[float]:...
        @typing.overload
        def __call__(self, vector: Vector128_1[float], index: int, data: float) -> Vector128_1[float]:...
        # Method Insert(vector : Vector128`1, index : Byte, data : Single) was skipped since it collides with above method
        # Method Insert(vector : Vector64`1, index : Byte, data : Byte) was skipped since it collides with above method
        # Method Insert(vector : Vector64`1, index : Byte, data : Int16) was skipped since it collides with above method
        # Method Insert(vector : Vector64`1, index : Byte, data : Int32) was skipped since it collides with above method
        # Method Insert(vector : Vector64`1, index : Byte, data : SByte) was skipped since it collides with above method
        # Method Insert(vector : Vector64`1, index : Byte, data : UInt16) was skipped since it collides with above method
        # Method Insert(vector : Vector64`1, index : Byte, data : UInt32) was skipped since it collides with above method
        # Method Insert(vector : Vector128`1, index : Byte, data : Byte) was skipped since it collides with above method
        # Method Insert(vector : Vector128`1, index : Byte, data : Int16) was skipped since it collides with above method
        # Method Insert(vector : Vector128`1, index : Byte, data : Int32) was skipped since it collides with above method
        # Method Insert(vector : Vector128`1, index : Byte, data : Int64) was skipped since it collides with above method
        # Method Insert(vector : Vector128`1, index : Byte, data : SByte) was skipped since it collides with above method
        # Method Insert(vector : Vector128`1, index : Byte, data : UInt16) was skipped since it collides with above method
        # Method Insert(vector : Vector128`1, index : Byte, data : UInt32) was skipped since it collides with above method
        # Method Insert(vector : Vector128`1, index : Byte, data : UInt64) was skipped since it collides with above method

    # Skipped InsertScalar due to it being static, abstract and generic.

    InsertScalar : InsertScalar_MethodGroup
    class InsertScalar_MethodGroup:
        def __call__(self, result: Vector128_1[float], resultIndex: int, value: Vector64_1[float]) -> Vector128_1[float]:...
        # Method InsertScalar(result : Vector128`1, resultIndex : Byte, value : Vector64`1) was skipped since it collides with above method
        # Method InsertScalar(result : Vector128`1, resultIndex : Byte, value : Vector64`1) was skipped since it collides with above method

    # Skipped LeadingSignCount due to it being static, abstract and generic.

    LeadingSignCount : LeadingSignCount_MethodGroup
    class LeadingSignCount_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector64_1[int]) -> Vector64_1[int]:...
        # Method LeadingSignCount(value : Vector64`1) was skipped since it collides with above method
        # Method LeadingSignCount(value : Vector64`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector128_1[int]) -> Vector128_1[int]:...
        # Method LeadingSignCount(value : Vector128`1) was skipped since it collides with above method
        # Method LeadingSignCount(value : Vector128`1) was skipped since it collides with above method

    # Skipped LeadingZeroCount due to it being static, abstract and generic.

    LeadingZeroCount : LeadingZeroCount_MethodGroup
    class LeadingZeroCount_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector64_1[int]) -> Vector64_1[int]:...
        # Method LeadingZeroCount(value : Vector64`1) was skipped since it collides with above method
        # Method LeadingZeroCount(value : Vector64`1) was skipped since it collides with above method
        # Method LeadingZeroCount(value : Vector64`1) was skipped since it collides with above method
        # Method LeadingZeroCount(value : Vector64`1) was skipped since it collides with above method
        # Method LeadingZeroCount(value : Vector64`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector128_1[int]) -> Vector128_1[int]:...
        # Method LeadingZeroCount(value : Vector128`1) was skipped since it collides with above method
        # Method LeadingZeroCount(value : Vector128`1) was skipped since it collides with above method
        # Method LeadingZeroCount(value : Vector128`1) was skipped since it collides with above method
        # Method LeadingZeroCount(value : Vector128`1) was skipped since it collides with above method
        # Method LeadingZeroCount(value : Vector128`1) was skipped since it collides with above method

    # Skipped LoadAndInsertScalar due to it being static, abstract and generic.

    LoadAndInsertScalar : LoadAndInsertScalar_MethodGroup
    class LoadAndInsertScalar_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector64_1[float], index: int, address: clr.Reference[float]) -> Vector64_1[float]:...
        @typing.overload
        def __call__(self, value: Vector128_1[float], index: int, address: clr.Reference[float]) -> Vector128_1[float]:...
        # Method LoadAndInsertScalar(value : Vector128`1, index : Byte, address : Single*) was skipped since it collides with above method
        # Method LoadAndInsertScalar(value : Vector64`1, index : Byte, address : Byte*) was skipped since it collides with above method
        # Method LoadAndInsertScalar(value : Vector64`1, index : Byte, address : Int16*) was skipped since it collides with above method
        # Method LoadAndInsertScalar(value : Vector64`1, index : Byte, address : Int32*) was skipped since it collides with above method
        # Method LoadAndInsertScalar(value : Vector64`1, index : Byte, address : SByte*) was skipped since it collides with above method
        # Method LoadAndInsertScalar(value : Vector64`1, index : Byte, address : UInt16*) was skipped since it collides with above method
        # Method LoadAndInsertScalar(value : Vector64`1, index : Byte, address : UInt32*) was skipped since it collides with above method
        # Method LoadAndInsertScalar(value : Vector128`1, index : Byte, address : Byte*) was skipped since it collides with above method
        # Method LoadAndInsertScalar(value : Vector128`1, index : Byte, address : Int16*) was skipped since it collides with above method
        # Method LoadAndInsertScalar(value : Vector128`1, index : Byte, address : Int32*) was skipped since it collides with above method
        # Method LoadAndInsertScalar(value : Vector128`1, index : Byte, address : Int64*) was skipped since it collides with above method
        # Method LoadAndInsertScalar(value : Vector128`1, index : Byte, address : SByte*) was skipped since it collides with above method
        # Method LoadAndInsertScalar(value : Vector128`1, index : Byte, address : UInt16*) was skipped since it collides with above method
        # Method LoadAndInsertScalar(value : Vector128`1, index : Byte, address : UInt32*) was skipped since it collides with above method
        # Method LoadAndInsertScalar(value : Vector128`1, index : Byte, address : UInt64*) was skipped since it collides with above method

    # Skipped LoadAndReplicateToVector128 due to it being static, abstract and generic.

    LoadAndReplicateToVector128 : LoadAndReplicateToVector128_MethodGroup
    class LoadAndReplicateToVector128_MethodGroup:
        def __call__(self, address: clr.Reference[float]) -> Vector128_1[float]:...
        # Method LoadAndReplicateToVector128(address : Byte*) was skipped since it collides with above method
        # Method LoadAndReplicateToVector128(address : Int16*) was skipped since it collides with above method
        # Method LoadAndReplicateToVector128(address : Int32*) was skipped since it collides with above method
        # Method LoadAndReplicateToVector128(address : SByte*) was skipped since it collides with above method
        # Method LoadAndReplicateToVector128(address : UInt16*) was skipped since it collides with above method
        # Method LoadAndReplicateToVector128(address : UInt32*) was skipped since it collides with above method

    # Skipped LoadAndReplicateToVector64 due to it being static, abstract and generic.

    LoadAndReplicateToVector64 : LoadAndReplicateToVector64_MethodGroup
    class LoadAndReplicateToVector64_MethodGroup:
        def __call__(self, address: clr.Reference[float]) -> Vector64_1[float]:...
        # Method LoadAndReplicateToVector64(address : UInt32*) was skipped since it collides with above method
        # Method LoadAndReplicateToVector64(address : Byte*) was skipped since it collides with above method
        # Method LoadAndReplicateToVector64(address : Int16*) was skipped since it collides with above method
        # Method LoadAndReplicateToVector64(address : Int32*) was skipped since it collides with above method
        # Method LoadAndReplicateToVector64(address : SByte*) was skipped since it collides with above method
        # Method LoadAndReplicateToVector64(address : UInt16*) was skipped since it collides with above method

    # Skipped LoadVector128 due to it being static, abstract and generic.

    LoadVector128 : LoadVector128_MethodGroup
    class LoadVector128_MethodGroup:
        def __call__(self, address: clr.Reference[float]) -> Vector128_1[float]:...
        # Method LoadVector128(address : Single*) was skipped since it collides with above method
        # Method LoadVector128(address : Byte*) was skipped since it collides with above method
        # Method LoadVector128(address : Int16*) was skipped since it collides with above method
        # Method LoadVector128(address : Int32*) was skipped since it collides with above method
        # Method LoadVector128(address : Int64*) was skipped since it collides with above method
        # Method LoadVector128(address : SByte*) was skipped since it collides with above method
        # Method LoadVector128(address : UInt16*) was skipped since it collides with above method
        # Method LoadVector128(address : UInt32*) was skipped since it collides with above method
        # Method LoadVector128(address : UInt64*) was skipped since it collides with above method

    # Skipped LoadVector64 due to it being static, abstract and generic.

    LoadVector64 : LoadVector64_MethodGroup
    class LoadVector64_MethodGroup:
        def __call__(self, address: clr.Reference[float]) -> Vector64_1[float]:...
        # Method LoadVector64(address : Single*) was skipped since it collides with above method
        # Method LoadVector64(address : Byte*) was skipped since it collides with above method
        # Method LoadVector64(address : Int16*) was skipped since it collides with above method
        # Method LoadVector64(address : Int32*) was skipped since it collides with above method
        # Method LoadVector64(address : Int64*) was skipped since it collides with above method
        # Method LoadVector64(address : SByte*) was skipped since it collides with above method
        # Method LoadVector64(address : UInt16*) was skipped since it collides with above method
        # Method LoadVector64(address : UInt32*) was skipped since it collides with above method
        # Method LoadVector64(address : UInt64*) was skipped since it collides with above method

    # Skipped Max due to it being static, abstract and generic.

    Max : Max_MethodGroup
    class Max_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
        @typing.overload
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
        # Method Max(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method Max(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method Max(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method Max(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method Max(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method Max(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method Max(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Max(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Max(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Max(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Max(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Max(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped MaxNumber due to it being static, abstract and generic.

    MaxNumber : MaxNumber_MethodGroup
    class MaxNumber_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
        @typing.overload
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...

    # Skipped MaxNumberScalar due to it being static, abstract and generic.

    MaxNumberScalar : MaxNumberScalar_MethodGroup
    class MaxNumberScalar_MethodGroup:
        def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
        # Method MaxNumberScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

    # Skipped MaxPairwise due to it being static, abstract and generic.

    MaxPairwise : MaxPairwise_MethodGroup
    class MaxPairwise_MethodGroup:
        def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
        # Method MaxPairwise(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method MaxPairwise(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method MaxPairwise(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method MaxPairwise(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method MaxPairwise(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method MaxPairwise(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

    # Skipped Min due to it being static, abstract and generic.

    Min : Min_MethodGroup
    class Min_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
        @typing.overload
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
        # Method Min(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method Min(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method Min(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method Min(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method Min(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method Min(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method Min(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Min(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Min(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Min(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Min(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Min(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped MinNumber due to it being static, abstract and generic.

    MinNumber : MinNumber_MethodGroup
    class MinNumber_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
        @typing.overload
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...

    # Skipped MinNumberScalar due to it being static, abstract and generic.

    MinNumberScalar : MinNumberScalar_MethodGroup
    class MinNumberScalar_MethodGroup:
        def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
        # Method MinNumberScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

    # Skipped MinPairwise due to it being static, abstract and generic.

    MinPairwise : MinPairwise_MethodGroup
    class MinPairwise_MethodGroup:
        def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
        # Method MinPairwise(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method MinPairwise(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method MinPairwise(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method MinPairwise(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method MinPairwise(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method MinPairwise(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

    # Skipped Multiply due to it being static, abstract and generic.

    Multiply : Multiply_MethodGroup
    class Multiply_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
        @typing.overload
        def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
        # Method Multiply(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Multiply(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Multiply(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Multiply(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Multiply(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Multiply(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Multiply(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method Multiply(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method Multiply(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method Multiply(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method Multiply(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method Multiply(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

    # Skipped MultiplyAdd due to it being static, abstract and generic.

    MultiplyAdd : MultiplyAdd_MethodGroup
    class MultiplyAdd_MethodGroup:
        @typing.overload
        def __call__(self, addend: Vector64_1[int], left: Vector64_1[int], right: Vector64_1[int]) -> Vector64_1[int]:...
        # Method MultiplyAdd(addend : Vector64`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method MultiplyAdd(addend : Vector64`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method MultiplyAdd(addend : Vector64`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method MultiplyAdd(addend : Vector64`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method MultiplyAdd(addend : Vector64`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, addend: Vector128_1[int], left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
        # Method MultiplyAdd(addend : Vector128`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method MultiplyAdd(addend : Vector128`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method MultiplyAdd(addend : Vector128`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method MultiplyAdd(addend : Vector128`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method MultiplyAdd(addend : Vector128`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped MultiplyAddByScalar due to it being static, abstract and generic.

    MultiplyAddByScalar : MultiplyAddByScalar_MethodGroup
    class MultiplyAddByScalar_MethodGroup:
        @typing.overload
        def __call__(self, addend: Vector64_1[int], left: Vector64_1[int], right: Vector64_1[int]) -> Vector64_1[int]:...
        # Method MultiplyAddByScalar(addend : Vector64`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method MultiplyAddByScalar(addend : Vector64`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method MultiplyAddByScalar(addend : Vector64`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, addend: Vector128_1[int], left: Vector128_1[int], right: Vector64_1[int]) -> Vector128_1[int]:...
        # Method MultiplyAddByScalar(addend : Vector128`1, left : Vector128`1, right : Vector64`1) was skipped since it collides with above method
        # Method MultiplyAddByScalar(addend : Vector128`1, left : Vector128`1, right : Vector64`1) was skipped since it collides with above method
        # Method MultiplyAddByScalar(addend : Vector128`1, left : Vector128`1, right : Vector64`1) was skipped since it collides with above method

    # Skipped MultiplyAddBySelectedScalar due to it being static, abstract and generic.

    MultiplyAddBySelectedScalar : MultiplyAddBySelectedScalar_MethodGroup
    class MultiplyAddBySelectedScalar_MethodGroup:
        @typing.overload
        def __call__(self, addend: Vector64_1[int], left: Vector64_1[int], right: Vector64_1[int], rightIndex: int) -> Vector64_1[int]:...
        @typing.overload
        def __call__(self, addend: Vector64_1[int], left: Vector64_1[int], right: Vector128_1[int], rightIndex: int) -> Vector64_1[int]:...
        # Method MultiplyAddBySelectedScalar(addend : Vector64`1, left : Vector64`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyAddBySelectedScalar(addend : Vector64`1, left : Vector64`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyAddBySelectedScalar(addend : Vector64`1, left : Vector64`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyAddBySelectedScalar(addend : Vector64`1, left : Vector64`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyAddBySelectedScalar(addend : Vector64`1, left : Vector64`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyAddBySelectedScalar(addend : Vector64`1, left : Vector64`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, addend: Vector128_1[int], left: Vector128_1[int], right: Vector64_1[int], rightIndex: int) -> Vector128_1[int]:...
        @typing.overload
        def __call__(self, addend: Vector128_1[int], left: Vector128_1[int], right: Vector128_1[int], rightIndex: int) -> Vector128_1[int]:...
        # Method MultiplyAddBySelectedScalar(addend : Vector128`1, left : Vector128`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyAddBySelectedScalar(addend : Vector128`1, left : Vector128`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyAddBySelectedScalar(addend : Vector128`1, left : Vector128`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyAddBySelectedScalar(addend : Vector128`1, left : Vector128`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyAddBySelectedScalar(addend : Vector128`1, left : Vector128`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyAddBySelectedScalar(addend : Vector128`1, left : Vector128`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method

    # Skipped MultiplyByScalar due to it being static, abstract and generic.

    MultiplyByScalar : MultiplyByScalar_MethodGroup
    class MultiplyByScalar_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector128_1[float], right: Vector64_1[float]) -> Vector128_1[float]:...
        @typing.overload
        def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
        # Method MultiplyByScalar(left : Vector128`1, right : Vector64`1) was skipped since it collides with above method
        # Method MultiplyByScalar(left : Vector128`1, right : Vector64`1) was skipped since it collides with above method
        # Method MultiplyByScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method MultiplyByScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method MultiplyByScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method MultiplyByScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method MultiplyByScalar(left : Vector128`1, right : Vector64`1) was skipped since it collides with above method
        # Method MultiplyByScalar(left : Vector128`1, right : Vector64`1) was skipped since it collides with above method

    # Skipped MultiplyBySelectedScalar due to it being static, abstract and generic.

    MultiplyBySelectedScalar : MultiplyBySelectedScalar_MethodGroup
    class MultiplyBySelectedScalar_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector64_1[float], right: Vector64_1[float], rightIndex: int) -> Vector64_1[float]:...
        @typing.overload
        def __call__(self, left: Vector64_1[float], right: Vector128_1[float], rightIndex: int) -> Vector64_1[float]:...
        @typing.overload
        def __call__(self, left: Vector128_1[float], right: Vector64_1[float], rightIndex: int) -> Vector128_1[float]:...
        @typing.overload
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float], rightIndex: int) -> Vector128_1[float]:...
        # Method MultiplyBySelectedScalar(left : Vector64`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyBySelectedScalar(left : Vector64`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyBySelectedScalar(left : Vector64`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyBySelectedScalar(left : Vector64`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyBySelectedScalar(left : Vector64`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyBySelectedScalar(left : Vector64`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyBySelectedScalar(left : Vector64`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyBySelectedScalar(left : Vector64`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyBySelectedScalar(left : Vector128`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyBySelectedScalar(left : Vector128`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyBySelectedScalar(left : Vector128`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyBySelectedScalar(left : Vector128`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyBySelectedScalar(left : Vector128`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyBySelectedScalar(left : Vector128`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyBySelectedScalar(left : Vector128`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyBySelectedScalar(left : Vector128`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method

    # Skipped MultiplyBySelectedScalarWideningLower due to it being static, abstract and generic.

    MultiplyBySelectedScalarWideningLower : MultiplyBySelectedScalarWideningLower_MethodGroup
    class MultiplyBySelectedScalarWideningLower_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector64_1[int], right: Vector64_1[int], rightIndex: int) -> Vector128_1[int]:...
        @typing.overload
        def __call__(self, left: Vector64_1[int], right: Vector128_1[int], rightIndex: int) -> Vector128_1[int]:...
        # Method MultiplyBySelectedScalarWideningLower(left : Vector64`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyBySelectedScalarWideningLower(left : Vector64`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyBySelectedScalarWideningLower(left : Vector64`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyBySelectedScalarWideningLower(left : Vector64`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyBySelectedScalarWideningLower(left : Vector64`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyBySelectedScalarWideningLower(left : Vector64`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method

    # Skipped MultiplyBySelectedScalarWideningLowerAndAdd due to it being static, abstract and generic.

    MultiplyBySelectedScalarWideningLowerAndAdd : MultiplyBySelectedScalarWideningLowerAndAdd_MethodGroup
    class MultiplyBySelectedScalarWideningLowerAndAdd_MethodGroup:
        @typing.overload
        def __call__(self, addend: Vector128_1[int], left: Vector64_1[int], right: Vector64_1[int], rightIndex: int) -> Vector128_1[int]:...
        @typing.overload
        def __call__(self, addend: Vector128_1[int], left: Vector64_1[int], right: Vector128_1[int], rightIndex: int) -> Vector128_1[int]:...
        # Method MultiplyBySelectedScalarWideningLowerAndAdd(addend : Vector128`1, left : Vector64`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyBySelectedScalarWideningLowerAndAdd(addend : Vector128`1, left : Vector64`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyBySelectedScalarWideningLowerAndAdd(addend : Vector128`1, left : Vector64`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyBySelectedScalarWideningLowerAndAdd(addend : Vector128`1, left : Vector64`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyBySelectedScalarWideningLowerAndAdd(addend : Vector128`1, left : Vector64`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyBySelectedScalarWideningLowerAndAdd(addend : Vector128`1, left : Vector64`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method

    # Skipped MultiplyBySelectedScalarWideningLowerAndSubtract due to it being static, abstract and generic.

    MultiplyBySelectedScalarWideningLowerAndSubtract : MultiplyBySelectedScalarWideningLowerAndSubtract_MethodGroup
    class MultiplyBySelectedScalarWideningLowerAndSubtract_MethodGroup:
        @typing.overload
        def __call__(self, minuend: Vector128_1[int], left: Vector64_1[int], right: Vector64_1[int], rightIndex: int) -> Vector128_1[int]:...
        @typing.overload
        def __call__(self, minuend: Vector128_1[int], left: Vector64_1[int], right: Vector128_1[int], rightIndex: int) -> Vector128_1[int]:...
        # Method MultiplyBySelectedScalarWideningLowerAndSubtract(minuend : Vector128`1, left : Vector64`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyBySelectedScalarWideningLowerAndSubtract(minuend : Vector128`1, left : Vector64`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyBySelectedScalarWideningLowerAndSubtract(minuend : Vector128`1, left : Vector64`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyBySelectedScalarWideningLowerAndSubtract(minuend : Vector128`1, left : Vector64`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyBySelectedScalarWideningLowerAndSubtract(minuend : Vector128`1, left : Vector64`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyBySelectedScalarWideningLowerAndSubtract(minuend : Vector128`1, left : Vector64`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method

    # Skipped MultiplyBySelectedScalarWideningUpper due to it being static, abstract and generic.

    MultiplyBySelectedScalarWideningUpper : MultiplyBySelectedScalarWideningUpper_MethodGroup
    class MultiplyBySelectedScalarWideningUpper_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector128_1[int], right: Vector64_1[int], rightIndex: int) -> Vector128_1[int]:...
        @typing.overload
        def __call__(self, left: Vector128_1[int], right: Vector128_1[int], rightIndex: int) -> Vector128_1[int]:...
        # Method MultiplyBySelectedScalarWideningUpper(left : Vector128`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyBySelectedScalarWideningUpper(left : Vector128`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyBySelectedScalarWideningUpper(left : Vector128`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyBySelectedScalarWideningUpper(left : Vector128`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyBySelectedScalarWideningUpper(left : Vector128`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyBySelectedScalarWideningUpper(left : Vector128`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method

    # Skipped MultiplyBySelectedScalarWideningUpperAndAdd due to it being static, abstract and generic.

    MultiplyBySelectedScalarWideningUpperAndAdd : MultiplyBySelectedScalarWideningUpperAndAdd_MethodGroup
    class MultiplyBySelectedScalarWideningUpperAndAdd_MethodGroup:
        @typing.overload
        def __call__(self, addend: Vector128_1[int], left: Vector128_1[int], right: Vector64_1[int], rightIndex: int) -> Vector128_1[int]:...
        @typing.overload
        def __call__(self, addend: Vector128_1[int], left: Vector128_1[int], right: Vector128_1[int], rightIndex: int) -> Vector128_1[int]:...
        # Method MultiplyBySelectedScalarWideningUpperAndAdd(addend : Vector128`1, left : Vector128`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyBySelectedScalarWideningUpperAndAdd(addend : Vector128`1, left : Vector128`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyBySelectedScalarWideningUpperAndAdd(addend : Vector128`1, left : Vector128`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyBySelectedScalarWideningUpperAndAdd(addend : Vector128`1, left : Vector128`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyBySelectedScalarWideningUpperAndAdd(addend : Vector128`1, left : Vector128`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyBySelectedScalarWideningUpperAndAdd(addend : Vector128`1, left : Vector128`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method

    # Skipped MultiplyBySelectedScalarWideningUpperAndSubtract due to it being static, abstract and generic.

    MultiplyBySelectedScalarWideningUpperAndSubtract : MultiplyBySelectedScalarWideningUpperAndSubtract_MethodGroup
    class MultiplyBySelectedScalarWideningUpperAndSubtract_MethodGroup:
        @typing.overload
        def __call__(self, minuend: Vector128_1[int], left: Vector128_1[int], right: Vector64_1[int], rightIndex: int) -> Vector128_1[int]:...
        @typing.overload
        def __call__(self, minuend: Vector128_1[int], left: Vector128_1[int], right: Vector128_1[int], rightIndex: int) -> Vector128_1[int]:...
        # Method MultiplyBySelectedScalarWideningUpperAndSubtract(minuend : Vector128`1, left : Vector128`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyBySelectedScalarWideningUpperAndSubtract(minuend : Vector128`1, left : Vector128`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyBySelectedScalarWideningUpperAndSubtract(minuend : Vector128`1, left : Vector128`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyBySelectedScalarWideningUpperAndSubtract(minuend : Vector128`1, left : Vector128`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyBySelectedScalarWideningUpperAndSubtract(minuend : Vector128`1, left : Vector128`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyBySelectedScalarWideningUpperAndSubtract(minuend : Vector128`1, left : Vector128`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method

    # Skipped MultiplyDoublingByScalarSaturateHigh due to it being static, abstract and generic.

    MultiplyDoublingByScalarSaturateHigh : MultiplyDoublingByScalarSaturateHigh_MethodGroup
    class MultiplyDoublingByScalarSaturateHigh_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector64_1[int], right: Vector64_1[int]) -> Vector64_1[int]:...
        # Method MultiplyDoublingByScalarSaturateHigh(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, left: Vector128_1[int], right: Vector64_1[int]) -> Vector128_1[int]:...
        # Method MultiplyDoublingByScalarSaturateHigh(left : Vector128`1, right : Vector64`1) was skipped since it collides with above method

    # Skipped MultiplyDoublingBySelectedScalarSaturateHigh due to it being static, abstract and generic.

    MultiplyDoublingBySelectedScalarSaturateHigh : MultiplyDoublingBySelectedScalarSaturateHigh_MethodGroup
    class MultiplyDoublingBySelectedScalarSaturateHigh_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector64_1[int], right: Vector64_1[int], rightIndex: int) -> Vector64_1[int]:...
        @typing.overload
        def __call__(self, left: Vector64_1[int], right: Vector128_1[int], rightIndex: int) -> Vector64_1[int]:...
        # Method MultiplyDoublingBySelectedScalarSaturateHigh(left : Vector64`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyDoublingBySelectedScalarSaturateHigh(left : Vector64`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, left: Vector128_1[int], right: Vector64_1[int], rightIndex: int) -> Vector128_1[int]:...
        @typing.overload
        def __call__(self, left: Vector128_1[int], right: Vector128_1[int], rightIndex: int) -> Vector128_1[int]:...
        # Method MultiplyDoublingBySelectedScalarSaturateHigh(left : Vector128`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyDoublingBySelectedScalarSaturateHigh(left : Vector128`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method

    # Skipped MultiplyDoublingSaturateHigh due to it being static, abstract and generic.

    MultiplyDoublingSaturateHigh : MultiplyDoublingSaturateHigh_MethodGroup
    class MultiplyDoublingSaturateHigh_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
        # Method MultiplyDoublingSaturateHigh(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, left: Vector64_1[int], right: Vector64_1[int]) -> Vector64_1[int]:...
        # Method MultiplyDoublingSaturateHigh(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

    # Skipped MultiplyDoublingWideningLowerAndAddSaturate due to it being static, abstract and generic.

    MultiplyDoublingWideningLowerAndAddSaturate : MultiplyDoublingWideningLowerAndAddSaturate_MethodGroup
    class MultiplyDoublingWideningLowerAndAddSaturate_MethodGroup:
        def __call__(self, addend: Vector128_1[int], left: Vector64_1[int], right: Vector64_1[int]) -> Vector128_1[int]:...
        # Method MultiplyDoublingWideningLowerAndAddSaturate(addend : Vector128`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

    # Skipped MultiplyDoublingWideningLowerAndSubtractSaturate due to it being static, abstract and generic.

    MultiplyDoublingWideningLowerAndSubtractSaturate : MultiplyDoublingWideningLowerAndSubtractSaturate_MethodGroup
    class MultiplyDoublingWideningLowerAndSubtractSaturate_MethodGroup:
        def __call__(self, minuend: Vector128_1[int], left: Vector64_1[int], right: Vector64_1[int]) -> Vector128_1[int]:...
        # Method MultiplyDoublingWideningLowerAndSubtractSaturate(minuend : Vector128`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

    # Skipped MultiplyDoublingWideningLowerByScalarAndAddSaturate due to it being static, abstract and generic.

    MultiplyDoublingWideningLowerByScalarAndAddSaturate : MultiplyDoublingWideningLowerByScalarAndAddSaturate_MethodGroup
    class MultiplyDoublingWideningLowerByScalarAndAddSaturate_MethodGroup:
        def __call__(self, addend: Vector128_1[int], left: Vector64_1[int], right: Vector64_1[int]) -> Vector128_1[int]:...
        # Method MultiplyDoublingWideningLowerByScalarAndAddSaturate(addend : Vector128`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

    # Skipped MultiplyDoublingWideningLowerByScalarAndSubtractSaturate due to it being static, abstract and generic.

    MultiplyDoublingWideningLowerByScalarAndSubtractSaturate : MultiplyDoublingWideningLowerByScalarAndSubtractSaturate_MethodGroup
    class MultiplyDoublingWideningLowerByScalarAndSubtractSaturate_MethodGroup:
        def __call__(self, minuend: Vector128_1[int], left: Vector64_1[int], right: Vector64_1[int]) -> Vector128_1[int]:...
        # Method MultiplyDoublingWideningLowerByScalarAndSubtractSaturate(minuend : Vector128`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

    # Skipped MultiplyDoublingWideningLowerBySelectedScalarAndAddSaturate due to it being static, abstract and generic.

    MultiplyDoublingWideningLowerBySelectedScalarAndAddSaturate : MultiplyDoublingWideningLowerBySelectedScalarAndAddSaturate_MethodGroup
    class MultiplyDoublingWideningLowerBySelectedScalarAndAddSaturate_MethodGroup:
        @typing.overload
        def __call__(self, addend: Vector128_1[int], left: Vector64_1[int], right: Vector64_1[int], rightIndex: int) -> Vector128_1[int]:...
        @typing.overload
        def __call__(self, addend: Vector128_1[int], left: Vector64_1[int], right: Vector128_1[int], rightIndex: int) -> Vector128_1[int]:...
        # Method MultiplyDoublingWideningLowerBySelectedScalarAndAddSaturate(addend : Vector128`1, left : Vector64`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyDoublingWideningLowerBySelectedScalarAndAddSaturate(addend : Vector128`1, left : Vector64`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method

    # Skipped MultiplyDoublingWideningLowerBySelectedScalarAndSubtractSaturate due to it being static, abstract and generic.

    MultiplyDoublingWideningLowerBySelectedScalarAndSubtractSaturate : MultiplyDoublingWideningLowerBySelectedScalarAndSubtractSaturate_MethodGroup
    class MultiplyDoublingWideningLowerBySelectedScalarAndSubtractSaturate_MethodGroup:
        @typing.overload
        def __call__(self, minuend: Vector128_1[int], left: Vector64_1[int], right: Vector64_1[int], rightIndex: int) -> Vector128_1[int]:...
        @typing.overload
        def __call__(self, minuend: Vector128_1[int], left: Vector64_1[int], right: Vector128_1[int], rightIndex: int) -> Vector128_1[int]:...
        # Method MultiplyDoublingWideningLowerBySelectedScalarAndSubtractSaturate(minuend : Vector128`1, left : Vector64`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyDoublingWideningLowerBySelectedScalarAndSubtractSaturate(minuend : Vector128`1, left : Vector64`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method

    # Skipped MultiplyDoublingWideningSaturateLower due to it being static, abstract and generic.

    MultiplyDoublingWideningSaturateLower : MultiplyDoublingWideningSaturateLower_MethodGroup
    class MultiplyDoublingWideningSaturateLower_MethodGroup:
        def __call__(self, left: Vector64_1[int], right: Vector64_1[int]) -> Vector128_1[int]:...
        # Method MultiplyDoublingWideningSaturateLower(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

    # Skipped MultiplyDoublingWideningSaturateLowerByScalar due to it being static, abstract and generic.

    MultiplyDoublingWideningSaturateLowerByScalar : MultiplyDoublingWideningSaturateLowerByScalar_MethodGroup
    class MultiplyDoublingWideningSaturateLowerByScalar_MethodGroup:
        def __call__(self, left: Vector64_1[int], right: Vector64_1[int]) -> Vector128_1[int]:...
        # Method MultiplyDoublingWideningSaturateLowerByScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

    # Skipped MultiplyDoublingWideningSaturateLowerBySelectedScalar due to it being static, abstract and generic.

    MultiplyDoublingWideningSaturateLowerBySelectedScalar : MultiplyDoublingWideningSaturateLowerBySelectedScalar_MethodGroup
    class MultiplyDoublingWideningSaturateLowerBySelectedScalar_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector64_1[int], right: Vector64_1[int], rightIndex: int) -> Vector128_1[int]:...
        @typing.overload
        def __call__(self, left: Vector64_1[int], right: Vector128_1[int], rightIndex: int) -> Vector128_1[int]:...
        # Method MultiplyDoublingWideningSaturateLowerBySelectedScalar(left : Vector64`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyDoublingWideningSaturateLowerBySelectedScalar(left : Vector64`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method

    # Skipped MultiplyDoublingWideningSaturateUpper due to it being static, abstract and generic.

    MultiplyDoublingWideningSaturateUpper : MultiplyDoublingWideningSaturateUpper_MethodGroup
    class MultiplyDoublingWideningSaturateUpper_MethodGroup:
        def __call__(self, left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
        # Method MultiplyDoublingWideningSaturateUpper(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped MultiplyDoublingWideningSaturateUpperByScalar due to it being static, abstract and generic.

    MultiplyDoublingWideningSaturateUpperByScalar : MultiplyDoublingWideningSaturateUpperByScalar_MethodGroup
    class MultiplyDoublingWideningSaturateUpperByScalar_MethodGroup:
        def __call__(self, left: Vector128_1[int], right: Vector64_1[int]) -> Vector128_1[int]:...
        # Method MultiplyDoublingWideningSaturateUpperByScalar(left : Vector128`1, right : Vector64`1) was skipped since it collides with above method

    # Skipped MultiplyDoublingWideningSaturateUpperBySelectedScalar due to it being static, abstract and generic.

    MultiplyDoublingWideningSaturateUpperBySelectedScalar : MultiplyDoublingWideningSaturateUpperBySelectedScalar_MethodGroup
    class MultiplyDoublingWideningSaturateUpperBySelectedScalar_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector128_1[int], right: Vector64_1[int], rightIndex: int) -> Vector128_1[int]:...
        @typing.overload
        def __call__(self, left: Vector128_1[int], right: Vector128_1[int], rightIndex: int) -> Vector128_1[int]:...
        # Method MultiplyDoublingWideningSaturateUpperBySelectedScalar(left : Vector128`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyDoublingWideningSaturateUpperBySelectedScalar(left : Vector128`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method

    # Skipped MultiplyDoublingWideningUpperAndAddSaturate due to it being static, abstract and generic.

    MultiplyDoublingWideningUpperAndAddSaturate : MultiplyDoublingWideningUpperAndAddSaturate_MethodGroup
    class MultiplyDoublingWideningUpperAndAddSaturate_MethodGroup:
        def __call__(self, addend: Vector128_1[int], left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
        # Method MultiplyDoublingWideningUpperAndAddSaturate(addend : Vector128`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped MultiplyDoublingWideningUpperAndSubtractSaturate due to it being static, abstract and generic.

    MultiplyDoublingWideningUpperAndSubtractSaturate : MultiplyDoublingWideningUpperAndSubtractSaturate_MethodGroup
    class MultiplyDoublingWideningUpperAndSubtractSaturate_MethodGroup:
        def __call__(self, minuend: Vector128_1[int], left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
        # Method MultiplyDoublingWideningUpperAndSubtractSaturate(minuend : Vector128`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped MultiplyDoublingWideningUpperByScalarAndAddSaturate due to it being static, abstract and generic.

    MultiplyDoublingWideningUpperByScalarAndAddSaturate : MultiplyDoublingWideningUpperByScalarAndAddSaturate_MethodGroup
    class MultiplyDoublingWideningUpperByScalarAndAddSaturate_MethodGroup:
        def __call__(self, addend: Vector128_1[int], left: Vector128_1[int], right: Vector64_1[int]) -> Vector128_1[int]:...
        # Method MultiplyDoublingWideningUpperByScalarAndAddSaturate(addend : Vector128`1, left : Vector128`1, right : Vector64`1) was skipped since it collides with above method

    # Skipped MultiplyDoublingWideningUpperByScalarAndSubtractSaturate due to it being static, abstract and generic.

    MultiplyDoublingWideningUpperByScalarAndSubtractSaturate : MultiplyDoublingWideningUpperByScalarAndSubtractSaturate_MethodGroup
    class MultiplyDoublingWideningUpperByScalarAndSubtractSaturate_MethodGroup:
        def __call__(self, minuend: Vector128_1[int], left: Vector128_1[int], right: Vector64_1[int]) -> Vector128_1[int]:...
        # Method MultiplyDoublingWideningUpperByScalarAndSubtractSaturate(minuend : Vector128`1, left : Vector128`1, right : Vector64`1) was skipped since it collides with above method

    # Skipped MultiplyDoublingWideningUpperBySelectedScalarAndAddSaturate due to it being static, abstract and generic.

    MultiplyDoublingWideningUpperBySelectedScalarAndAddSaturate : MultiplyDoublingWideningUpperBySelectedScalarAndAddSaturate_MethodGroup
    class MultiplyDoublingWideningUpperBySelectedScalarAndAddSaturate_MethodGroup:
        @typing.overload
        def __call__(self, addend: Vector128_1[int], left: Vector128_1[int], right: Vector64_1[int], rightIndex: int) -> Vector128_1[int]:...
        @typing.overload
        def __call__(self, addend: Vector128_1[int], left: Vector128_1[int], right: Vector128_1[int], rightIndex: int) -> Vector128_1[int]:...
        # Method MultiplyDoublingWideningUpperBySelectedScalarAndAddSaturate(addend : Vector128`1, left : Vector128`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyDoublingWideningUpperBySelectedScalarAndAddSaturate(addend : Vector128`1, left : Vector128`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method

    # Skipped MultiplyDoublingWideningUpperBySelectedScalarAndSubtractSaturate due to it being static, abstract and generic.

    MultiplyDoublingWideningUpperBySelectedScalarAndSubtractSaturate : MultiplyDoublingWideningUpperBySelectedScalarAndSubtractSaturate_MethodGroup
    class MultiplyDoublingWideningUpperBySelectedScalarAndSubtractSaturate_MethodGroup:
        @typing.overload
        def __call__(self, minuend: Vector128_1[int], left: Vector128_1[int], right: Vector64_1[int], rightIndex: int) -> Vector128_1[int]:...
        @typing.overload
        def __call__(self, minuend: Vector128_1[int], left: Vector128_1[int], right: Vector128_1[int], rightIndex: int) -> Vector128_1[int]:...
        # Method MultiplyDoublingWideningUpperBySelectedScalarAndSubtractSaturate(minuend : Vector128`1, left : Vector128`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyDoublingWideningUpperBySelectedScalarAndSubtractSaturate(minuend : Vector128`1, left : Vector128`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method

    # Skipped MultiplyRoundedDoublingByScalarSaturateHigh due to it being static, abstract and generic.

    MultiplyRoundedDoublingByScalarSaturateHigh : MultiplyRoundedDoublingByScalarSaturateHigh_MethodGroup
    class MultiplyRoundedDoublingByScalarSaturateHigh_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector64_1[int], right: Vector64_1[int]) -> Vector64_1[int]:...
        # Method MultiplyRoundedDoublingByScalarSaturateHigh(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, left: Vector128_1[int], right: Vector64_1[int]) -> Vector128_1[int]:...
        # Method MultiplyRoundedDoublingByScalarSaturateHigh(left : Vector128`1, right : Vector64`1) was skipped since it collides with above method

    # Skipped MultiplyRoundedDoublingBySelectedScalarSaturateHigh due to it being static, abstract and generic.

    MultiplyRoundedDoublingBySelectedScalarSaturateHigh : MultiplyRoundedDoublingBySelectedScalarSaturateHigh_MethodGroup
    class MultiplyRoundedDoublingBySelectedScalarSaturateHigh_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector64_1[int], right: Vector64_1[int], rightIndex: int) -> Vector64_1[int]:...
        @typing.overload
        def __call__(self, left: Vector64_1[int], right: Vector128_1[int], rightIndex: int) -> Vector64_1[int]:...
        # Method MultiplyRoundedDoublingBySelectedScalarSaturateHigh(left : Vector64`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyRoundedDoublingBySelectedScalarSaturateHigh(left : Vector64`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, left: Vector128_1[int], right: Vector64_1[int], rightIndex: int) -> Vector128_1[int]:...
        @typing.overload
        def __call__(self, left: Vector128_1[int], right: Vector128_1[int], rightIndex: int) -> Vector128_1[int]:...
        # Method MultiplyRoundedDoublingBySelectedScalarSaturateHigh(left : Vector128`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyRoundedDoublingBySelectedScalarSaturateHigh(left : Vector128`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method

    # Skipped MultiplyRoundedDoublingSaturateHigh due to it being static, abstract and generic.

    MultiplyRoundedDoublingSaturateHigh : MultiplyRoundedDoublingSaturateHigh_MethodGroup
    class MultiplyRoundedDoublingSaturateHigh_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector64_1[int], right: Vector64_1[int]) -> Vector64_1[int]:...
        # Method MultiplyRoundedDoublingSaturateHigh(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
        # Method MultiplyRoundedDoublingSaturateHigh(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped MultiplyScalar due to it being static, abstract and generic.

    MultiplyScalar : MultiplyScalar_MethodGroup
    class MultiplyScalar_MethodGroup:
        def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
        # Method MultiplyScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

    # Skipped MultiplyScalarBySelectedScalar due to it being static, abstract and generic.

    MultiplyScalarBySelectedScalar : MultiplyScalarBySelectedScalar_MethodGroup
    class MultiplyScalarBySelectedScalar_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector64_1[float], right: Vector64_1[float], rightIndex: int) -> Vector64_1[float]:...
        @typing.overload
        def __call__(self, left: Vector64_1[float], right: Vector128_1[float], rightIndex: int) -> Vector64_1[float]:...

    # Skipped MultiplySubtract due to it being static, abstract and generic.

    MultiplySubtract : MultiplySubtract_MethodGroup
    class MultiplySubtract_MethodGroup:
        @typing.overload
        def __call__(self, minuend: Vector64_1[int], left: Vector64_1[int], right: Vector64_1[int]) -> Vector64_1[int]:...
        # Method MultiplySubtract(minuend : Vector64`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method MultiplySubtract(minuend : Vector64`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method MultiplySubtract(minuend : Vector64`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method MultiplySubtract(minuend : Vector64`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method MultiplySubtract(minuend : Vector64`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, minuend: Vector128_1[int], left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
        # Method MultiplySubtract(minuend : Vector128`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method MultiplySubtract(minuend : Vector128`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method MultiplySubtract(minuend : Vector128`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method MultiplySubtract(minuend : Vector128`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method MultiplySubtract(minuend : Vector128`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped MultiplySubtractByScalar due to it being static, abstract and generic.

    MultiplySubtractByScalar : MultiplySubtractByScalar_MethodGroup
    class MultiplySubtractByScalar_MethodGroup:
        @typing.overload
        def __call__(self, minuend: Vector64_1[int], left: Vector64_1[int], right: Vector64_1[int]) -> Vector64_1[int]:...
        @typing.overload
        def __call__(self, minuend: Vector128_1[int], left: Vector128_1[int], right: Vector64_1[int]) -> Vector128_1[int]:...
        # Method MultiplySubtractByScalar(minuend : Vector128`1, left : Vector128`1, right : Vector64`1) was skipped since it collides with above method
        # Method MultiplySubtractByScalar(minuend : Vector128`1, left : Vector128`1, right : Vector64`1) was skipped since it collides with above method
        # Method MultiplySubtractByScalar(minuend : Vector128`1, left : Vector128`1, right : Vector64`1) was skipped since it collides with above method
        # Method MultiplySubtractByScalar(minuend : Vector64`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method MultiplySubtractByScalar(minuend : Vector64`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method MultiplySubtractByScalar(minuend : Vector64`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

    # Skipped MultiplySubtractBySelectedScalar due to it being static, abstract and generic.

    MultiplySubtractBySelectedScalar : MultiplySubtractBySelectedScalar_MethodGroup
    class MultiplySubtractBySelectedScalar_MethodGroup:
        @typing.overload
        def __call__(self, minuend: Vector64_1[int], left: Vector64_1[int], right: Vector64_1[int], rightIndex: int) -> Vector64_1[int]:...
        @typing.overload
        def __call__(self, minuend: Vector64_1[int], left: Vector64_1[int], right: Vector128_1[int], rightIndex: int) -> Vector64_1[int]:...
        # Method MultiplySubtractBySelectedScalar(minuend : Vector64`1, left : Vector64`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplySubtractBySelectedScalar(minuend : Vector64`1, left : Vector64`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplySubtractBySelectedScalar(minuend : Vector64`1, left : Vector64`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplySubtractBySelectedScalar(minuend : Vector64`1, left : Vector64`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplySubtractBySelectedScalar(minuend : Vector64`1, left : Vector64`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplySubtractBySelectedScalar(minuend : Vector64`1, left : Vector64`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, minuend: Vector128_1[int], left: Vector128_1[int], right: Vector64_1[int], rightIndex: int) -> Vector128_1[int]:...
        @typing.overload
        def __call__(self, minuend: Vector128_1[int], left: Vector128_1[int], right: Vector128_1[int], rightIndex: int) -> Vector128_1[int]:...
        # Method MultiplySubtractBySelectedScalar(minuend : Vector128`1, left : Vector128`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplySubtractBySelectedScalar(minuend : Vector128`1, left : Vector128`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplySubtractBySelectedScalar(minuend : Vector128`1, left : Vector128`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplySubtractBySelectedScalar(minuend : Vector128`1, left : Vector128`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplySubtractBySelectedScalar(minuend : Vector128`1, left : Vector128`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplySubtractBySelectedScalar(minuend : Vector128`1, left : Vector128`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method

    # Skipped MultiplyWideningLower due to it being static, abstract and generic.

    MultiplyWideningLower : MultiplyWideningLower_MethodGroup
    class MultiplyWideningLower_MethodGroup:
        def __call__(self, left: Vector64_1[int], right: Vector64_1[int]) -> Vector128_1[int]:...
        # Method MultiplyWideningLower(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method MultiplyWideningLower(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method MultiplyWideningLower(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method MultiplyWideningLower(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method MultiplyWideningLower(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

    # Skipped MultiplyWideningLowerAndAdd due to it being static, abstract and generic.

    MultiplyWideningLowerAndAdd : MultiplyWideningLowerAndAdd_MethodGroup
    class MultiplyWideningLowerAndAdd_MethodGroup:
        def __call__(self, addend: Vector128_1[int], left: Vector64_1[int], right: Vector64_1[int]) -> Vector128_1[int]:...
        # Method MultiplyWideningLowerAndAdd(addend : Vector128`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method MultiplyWideningLowerAndAdd(addend : Vector128`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method MultiplyWideningLowerAndAdd(addend : Vector128`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method MultiplyWideningLowerAndAdd(addend : Vector128`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method MultiplyWideningLowerAndAdd(addend : Vector128`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

    # Skipped MultiplyWideningLowerAndSubtract due to it being static, abstract and generic.

    MultiplyWideningLowerAndSubtract : MultiplyWideningLowerAndSubtract_MethodGroup
    class MultiplyWideningLowerAndSubtract_MethodGroup:
        def __call__(self, minuend: Vector128_1[int], left: Vector64_1[int], right: Vector64_1[int]) -> Vector128_1[int]:...
        # Method MultiplyWideningLowerAndSubtract(minuend : Vector128`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method MultiplyWideningLowerAndSubtract(minuend : Vector128`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method MultiplyWideningLowerAndSubtract(minuend : Vector128`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method MultiplyWideningLowerAndSubtract(minuend : Vector128`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method MultiplyWideningLowerAndSubtract(minuend : Vector128`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

    # Skipped MultiplyWideningUpper due to it being static, abstract and generic.

    MultiplyWideningUpper : MultiplyWideningUpper_MethodGroup
    class MultiplyWideningUpper_MethodGroup:
        def __call__(self, left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
        # Method MultiplyWideningUpper(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method MultiplyWideningUpper(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method MultiplyWideningUpper(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method MultiplyWideningUpper(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method MultiplyWideningUpper(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped MultiplyWideningUpperAndAdd due to it being static, abstract and generic.

    MultiplyWideningUpperAndAdd : MultiplyWideningUpperAndAdd_MethodGroup
    class MultiplyWideningUpperAndAdd_MethodGroup:
        def __call__(self, addend: Vector128_1[int], left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
        # Method MultiplyWideningUpperAndAdd(addend : Vector128`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method MultiplyWideningUpperAndAdd(addend : Vector128`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method MultiplyWideningUpperAndAdd(addend : Vector128`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method MultiplyWideningUpperAndAdd(addend : Vector128`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method MultiplyWideningUpperAndAdd(addend : Vector128`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped MultiplyWideningUpperAndSubtract due to it being static, abstract and generic.

    MultiplyWideningUpperAndSubtract : MultiplyWideningUpperAndSubtract_MethodGroup
    class MultiplyWideningUpperAndSubtract_MethodGroup:
        def __call__(self, minuend: Vector128_1[int], left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
        # Method MultiplyWideningUpperAndSubtract(minuend : Vector128`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method MultiplyWideningUpperAndSubtract(minuend : Vector128`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method MultiplyWideningUpperAndSubtract(minuend : Vector128`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method MultiplyWideningUpperAndSubtract(minuend : Vector128`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method MultiplyWideningUpperAndSubtract(minuend : Vector128`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped Negate due to it being static, abstract and generic.

    Negate : Negate_MethodGroup
    class Negate_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector64_1[float]) -> Vector64_1[float]:...
        @typing.overload
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[float]:...
        # Method Negate(value : Vector64`1) was skipped since it collides with above method
        # Method Negate(value : Vector64`1) was skipped since it collides with above method
        # Method Negate(value : Vector64`1) was skipped since it collides with above method
        # Method Negate(value : Vector128`1) was skipped since it collides with above method
        # Method Negate(value : Vector128`1) was skipped since it collides with above method
        # Method Negate(value : Vector128`1) was skipped since it collides with above method

    # Skipped NegateSaturate due to it being static, abstract and generic.

    NegateSaturate : NegateSaturate_MethodGroup
    class NegateSaturate_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector64_1[int]) -> Vector64_1[int]:...
        # Method NegateSaturate(value : Vector64`1) was skipped since it collides with above method
        # Method NegateSaturate(value : Vector64`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector128_1[int]) -> Vector128_1[int]:...
        # Method NegateSaturate(value : Vector128`1) was skipped since it collides with above method
        # Method NegateSaturate(value : Vector128`1) was skipped since it collides with above method

    # Skipped NegateScalar due to it being static, abstract and generic.

    NegateScalar : NegateScalar_MethodGroup
    class NegateScalar_MethodGroup:
        def __call__(self, value: Vector64_1[float]) -> Vector64_1[float]:...
        # Method NegateScalar(value : Vector64`1) was skipped since it collides with above method

    # Skipped Not due to it being static, abstract and generic.

    Not : Not_MethodGroup
    class Not_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[float]:...
        @typing.overload
        def __call__(self, value: Vector64_1[float]) -> Vector64_1[float]:...
        # Method Not(value : Vector64`1) was skipped since it collides with above method
        # Method Not(value : Vector128`1) was skipped since it collides with above method
        # Method Not(value : Vector128`1) was skipped since it collides with above method
        # Method Not(value : Vector128`1) was skipped since it collides with above method
        # Method Not(value : Vector128`1) was skipped since it collides with above method
        # Method Not(value : Vector128`1) was skipped since it collides with above method
        # Method Not(value : Vector128`1) was skipped since it collides with above method
        # Method Not(value : Vector128`1) was skipped since it collides with above method
        # Method Not(value : Vector128`1) was skipped since it collides with above method
        # Method Not(value : Vector64`1) was skipped since it collides with above method
        # Method Not(value : Vector64`1) was skipped since it collides with above method
        # Method Not(value : Vector64`1) was skipped since it collides with above method
        # Method Not(value : Vector64`1) was skipped since it collides with above method
        # Method Not(value : Vector64`1) was skipped since it collides with above method
        # Method Not(value : Vector64`1) was skipped since it collides with above method
        # Method Not(value : Vector64`1) was skipped since it collides with above method
        # Method Not(value : Vector64`1) was skipped since it collides with above method
        # Method Not(value : Vector128`1) was skipped since it collides with above method

    # Skipped Or due to it being static, abstract and generic.

    Or : Or_MethodGroup
    class Or_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
        # Method Or(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
        # Method Or(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Or(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method Or(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method Or(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method Or(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method Or(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method Or(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method Or(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method Or(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method Or(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Or(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Or(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Or(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Or(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Or(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Or(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Or(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped OrNot due to it being static, abstract and generic.

    OrNot : OrNot_MethodGroup
    class OrNot_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
        # Method OrNot(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
        # Method OrNot(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method OrNot(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method OrNot(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method OrNot(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method OrNot(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method OrNot(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method OrNot(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method OrNot(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method OrNot(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method OrNot(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method OrNot(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method OrNot(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method OrNot(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method OrNot(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method OrNot(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method OrNot(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method OrNot(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped PolynomialMultiply due to it being static, abstract and generic.

    PolynomialMultiply : PolynomialMultiply_MethodGroup
    class PolynomialMultiply_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector64_1[int], right: Vector64_1[int]) -> Vector64_1[int]:...
        # Method PolynomialMultiply(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
        # Method PolynomialMultiply(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped PolynomialMultiplyWideningLower due to it being static, abstract and generic.

    PolynomialMultiplyWideningLower : PolynomialMultiplyWideningLower_MethodGroup
    class PolynomialMultiplyWideningLower_MethodGroup:
        def __call__(self, left: Vector64_1[int], right: Vector64_1[int]) -> Vector128_1[int]:...
        # Method PolynomialMultiplyWideningLower(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

    # Skipped PolynomialMultiplyWideningUpper due to it being static, abstract and generic.

    PolynomialMultiplyWideningUpper : PolynomialMultiplyWideningUpper_MethodGroup
    class PolynomialMultiplyWideningUpper_MethodGroup:
        def __call__(self, left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
        # Method PolynomialMultiplyWideningUpper(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped PopCount due to it being static, abstract and generic.

    PopCount : PopCount_MethodGroup
    class PopCount_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector64_1[int]) -> Vector64_1[int]:...
        # Method PopCount(value : Vector64`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector128_1[int]) -> Vector128_1[int]:...
        # Method PopCount(value : Vector128`1) was skipped since it collides with above method

    # Skipped ReciprocalEstimate due to it being static, abstract and generic.

    ReciprocalEstimate : ReciprocalEstimate_MethodGroup
    class ReciprocalEstimate_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector64_1[float]) -> Vector64_1[float]:...
        @typing.overload
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[float]:...
        # Method ReciprocalEstimate(value : Vector64`1) was skipped since it collides with above method
        # Method ReciprocalEstimate(value : Vector128`1) was skipped since it collides with above method

    # Skipped ReciprocalSquareRootEstimate due to it being static, abstract and generic.

    ReciprocalSquareRootEstimate : ReciprocalSquareRootEstimate_MethodGroup
    class ReciprocalSquareRootEstimate_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector64_1[float]) -> Vector64_1[float]:...
        @typing.overload
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[float]:...
        # Method ReciprocalSquareRootEstimate(value : Vector64`1) was skipped since it collides with above method
        # Method ReciprocalSquareRootEstimate(value : Vector128`1) was skipped since it collides with above method

    # Skipped ReciprocalSquareRootStep due to it being static, abstract and generic.

    ReciprocalSquareRootStep : ReciprocalSquareRootStep_MethodGroup
    class ReciprocalSquareRootStep_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
        @typing.overload
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...

    # Skipped ReciprocalStep due to it being static, abstract and generic.

    ReciprocalStep : ReciprocalStep_MethodGroup
    class ReciprocalStep_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
        @typing.overload
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...

    # Skipped ReverseElement16 due to it being static, abstract and generic.

    ReverseElement16 : ReverseElement16_MethodGroup
    class ReverseElement16_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector64_1[int]) -> Vector64_1[int]:...
        # Method ReverseElement16(value : Vector64`1) was skipped since it collides with above method
        # Method ReverseElement16(value : Vector64`1) was skipped since it collides with above method
        # Method ReverseElement16(value : Vector64`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector128_1[int]) -> Vector128_1[int]:...
        # Method ReverseElement16(value : Vector128`1) was skipped since it collides with above method
        # Method ReverseElement16(value : Vector128`1) was skipped since it collides with above method
        # Method ReverseElement16(value : Vector128`1) was skipped since it collides with above method

    # Skipped ReverseElement32 due to it being static, abstract and generic.

    ReverseElement32 : ReverseElement32_MethodGroup
    class ReverseElement32_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector64_1[int]) -> Vector64_1[int]:...
        # Method ReverseElement32(value : Vector64`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector128_1[int]) -> Vector128_1[int]:...
        # Method ReverseElement32(value : Vector128`1) was skipped since it collides with above method

    # Skipped ReverseElement8 due to it being static, abstract and generic.

    ReverseElement8 : ReverseElement8_MethodGroup
    class ReverseElement8_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector64_1[int]) -> Vector64_1[int]:...
        # Method ReverseElement8(value : Vector64`1) was skipped since it collides with above method
        # Method ReverseElement8(value : Vector64`1) was skipped since it collides with above method
        # Method ReverseElement8(value : Vector64`1) was skipped since it collides with above method
        # Method ReverseElement8(value : Vector64`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector128_1[int]) -> Vector128_1[int]:...
        # Method ReverseElement8(value : Vector128`1) was skipped since it collides with above method
        # Method ReverseElement8(value : Vector128`1) was skipped since it collides with above method
        # Method ReverseElement8(value : Vector128`1) was skipped since it collides with above method
        # Method ReverseElement8(value : Vector128`1) was skipped since it collides with above method
        # Method ReverseElement8(value : Vector128`1) was skipped since it collides with above method
        # Method ReverseElement8(value : Vector64`1) was skipped since it collides with above method

    # Skipped RoundAwayFromZero due to it being static, abstract and generic.

    RoundAwayFromZero : RoundAwayFromZero_MethodGroup
    class RoundAwayFromZero_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector64_1[float]) -> Vector64_1[float]:...
        @typing.overload
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[float]:...

    # Skipped RoundAwayFromZeroScalar due to it being static, abstract and generic.

    RoundAwayFromZeroScalar : RoundAwayFromZeroScalar_MethodGroup
    class RoundAwayFromZeroScalar_MethodGroup:
        def __call__(self, value: Vector64_1[float]) -> Vector64_1[float]:...
        # Method RoundAwayFromZeroScalar(value : Vector64`1) was skipped since it collides with above method

    # Skipped RoundToNearest due to it being static, abstract and generic.

    RoundToNearest : RoundToNearest_MethodGroup
    class RoundToNearest_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector64_1[float]) -> Vector64_1[float]:...
        @typing.overload
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[float]:...

    # Skipped RoundToNearestScalar due to it being static, abstract and generic.

    RoundToNearestScalar : RoundToNearestScalar_MethodGroup
    class RoundToNearestScalar_MethodGroup:
        def __call__(self, value: Vector64_1[float]) -> Vector64_1[float]:...
        # Method RoundToNearestScalar(value : Vector64`1) was skipped since it collides with above method

    # Skipped RoundToNegativeInfinity due to it being static, abstract and generic.

    RoundToNegativeInfinity : RoundToNegativeInfinity_MethodGroup
    class RoundToNegativeInfinity_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector64_1[float]) -> Vector64_1[float]:...
        @typing.overload
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[float]:...

    # Skipped RoundToNegativeInfinityScalar due to it being static, abstract and generic.

    RoundToNegativeInfinityScalar : RoundToNegativeInfinityScalar_MethodGroup
    class RoundToNegativeInfinityScalar_MethodGroup:
        def __call__(self, value: Vector64_1[float]) -> Vector64_1[float]:...
        # Method RoundToNegativeInfinityScalar(value : Vector64`1) was skipped since it collides with above method

    # Skipped RoundToPositiveInfinity due to it being static, abstract and generic.

    RoundToPositiveInfinity : RoundToPositiveInfinity_MethodGroup
    class RoundToPositiveInfinity_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector64_1[float]) -> Vector64_1[float]:...
        @typing.overload
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[float]:...

    # Skipped RoundToPositiveInfinityScalar due to it being static, abstract and generic.

    RoundToPositiveInfinityScalar : RoundToPositiveInfinityScalar_MethodGroup
    class RoundToPositiveInfinityScalar_MethodGroup:
        def __call__(self, value: Vector64_1[float]) -> Vector64_1[float]:...
        # Method RoundToPositiveInfinityScalar(value : Vector64`1) was skipped since it collides with above method

    # Skipped RoundToZero due to it being static, abstract and generic.

    RoundToZero : RoundToZero_MethodGroup
    class RoundToZero_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector64_1[float]) -> Vector64_1[float]:...
        @typing.overload
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[float]:...

    # Skipped RoundToZeroScalar due to it being static, abstract and generic.

    RoundToZeroScalar : RoundToZeroScalar_MethodGroup
    class RoundToZeroScalar_MethodGroup:
        def __call__(self, value: Vector64_1[float]) -> Vector64_1[float]:...
        # Method RoundToZeroScalar(value : Vector64`1) was skipped since it collides with above method

    # Skipped ShiftArithmetic due to it being static, abstract and generic.

    ShiftArithmetic : ShiftArithmetic_MethodGroup
    class ShiftArithmetic_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector64_1[int], count: Vector64_1[int]) -> Vector64_1[int]:...
        # Method ShiftArithmetic(value : Vector64`1, count : Vector64`1) was skipped since it collides with above method
        # Method ShiftArithmetic(value : Vector64`1, count : Vector64`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector128_1[int], count: Vector128_1[int]) -> Vector128_1[int]:...
        # Method ShiftArithmetic(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method
        # Method ShiftArithmetic(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method
        # Method ShiftArithmetic(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method

    # Skipped ShiftArithmeticRounded due to it being static, abstract and generic.

    ShiftArithmeticRounded : ShiftArithmeticRounded_MethodGroup
    class ShiftArithmeticRounded_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector64_1[int], count: Vector64_1[int]) -> Vector64_1[int]:...
        # Method ShiftArithmeticRounded(value : Vector64`1, count : Vector64`1) was skipped since it collides with above method
        # Method ShiftArithmeticRounded(value : Vector64`1, count : Vector64`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector128_1[int], count: Vector128_1[int]) -> Vector128_1[int]:...
        # Method ShiftArithmeticRounded(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method
        # Method ShiftArithmeticRounded(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method
        # Method ShiftArithmeticRounded(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method

    # Skipped ShiftArithmeticRoundedSaturate due to it being static, abstract and generic.

    ShiftArithmeticRoundedSaturate : ShiftArithmeticRoundedSaturate_MethodGroup
    class ShiftArithmeticRoundedSaturate_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector64_1[int], count: Vector64_1[int]) -> Vector64_1[int]:...
        # Method ShiftArithmeticRoundedSaturate(value : Vector64`1, count : Vector64`1) was skipped since it collides with above method
        # Method ShiftArithmeticRoundedSaturate(value : Vector64`1, count : Vector64`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector128_1[int], count: Vector128_1[int]) -> Vector128_1[int]:...
        # Method ShiftArithmeticRoundedSaturate(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method
        # Method ShiftArithmeticRoundedSaturate(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method
        # Method ShiftArithmeticRoundedSaturate(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method

    # Skipped ShiftArithmeticSaturate due to it being static, abstract and generic.

    ShiftArithmeticSaturate : ShiftArithmeticSaturate_MethodGroup
    class ShiftArithmeticSaturate_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector64_1[int], count: Vector64_1[int]) -> Vector64_1[int]:...
        # Method ShiftArithmeticSaturate(value : Vector64`1, count : Vector64`1) was skipped since it collides with above method
        # Method ShiftArithmeticSaturate(value : Vector64`1, count : Vector64`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector128_1[int], count: Vector128_1[int]) -> Vector128_1[int]:...
        # Method ShiftArithmeticSaturate(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method
        # Method ShiftArithmeticSaturate(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method
        # Method ShiftArithmeticSaturate(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method

    # Skipped ShiftLeftAndInsert due to it being static, abstract and generic.

    ShiftLeftAndInsert : ShiftLeftAndInsert_MethodGroup
    class ShiftLeftAndInsert_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector64_1[int], right: Vector64_1[int], shift: int) -> Vector64_1[int]:...
        # Method ShiftLeftAndInsert(left : Vector64`1, right : Vector64`1, shift : Byte) was skipped since it collides with above method
        # Method ShiftLeftAndInsert(left : Vector64`1, right : Vector64`1, shift : Byte) was skipped since it collides with above method
        # Method ShiftLeftAndInsert(left : Vector64`1, right : Vector64`1, shift : Byte) was skipped since it collides with above method
        # Method ShiftLeftAndInsert(left : Vector64`1, right : Vector64`1, shift : Byte) was skipped since it collides with above method
        # Method ShiftLeftAndInsert(left : Vector64`1, right : Vector64`1, shift : Byte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, left: Vector128_1[int], right: Vector128_1[int], shift: int) -> Vector128_1[int]:...
        # Method ShiftLeftAndInsert(left : Vector128`1, right : Vector128`1, shift : Byte) was skipped since it collides with above method
        # Method ShiftLeftAndInsert(left : Vector128`1, right : Vector128`1, shift : Byte) was skipped since it collides with above method
        # Method ShiftLeftAndInsert(left : Vector128`1, right : Vector128`1, shift : Byte) was skipped since it collides with above method
        # Method ShiftLeftAndInsert(left : Vector128`1, right : Vector128`1, shift : Byte) was skipped since it collides with above method
        # Method ShiftLeftAndInsert(left : Vector128`1, right : Vector128`1, shift : Byte) was skipped since it collides with above method
        # Method ShiftLeftAndInsert(left : Vector128`1, right : Vector128`1, shift : Byte) was skipped since it collides with above method
        # Method ShiftLeftAndInsert(left : Vector128`1, right : Vector128`1, shift : Byte) was skipped since it collides with above method

    # Skipped ShiftLeftAndInsertScalar due to it being static, abstract and generic.

    ShiftLeftAndInsertScalar : ShiftLeftAndInsertScalar_MethodGroup
    class ShiftLeftAndInsertScalar_MethodGroup:
        def __call__(self, left: Vector64_1[int], right: Vector64_1[int], shift: int) -> Vector64_1[int]:...
        # Method ShiftLeftAndInsertScalar(left : Vector64`1, right : Vector64`1, shift : Byte) was skipped since it collides with above method

    # Skipped ShiftLeftLogical due to it being static, abstract and generic.

    ShiftLeftLogical : ShiftLeftLogical_MethodGroup
    class ShiftLeftLogical_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector128_1[int], count: int) -> Vector128_1[int]:...
        # Method ShiftLeftLogical(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftLeftLogical(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftLeftLogical(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftLeftLogical(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftLeftLogical(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftLeftLogical(value : Vector128`1, count : Byte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector64_1[int], count: int) -> Vector64_1[int]:...
        # Method ShiftLeftLogical(value : Vector64`1, count : Byte) was skipped since it collides with above method
        # Method ShiftLeftLogical(value : Vector64`1, count : Byte) was skipped since it collides with above method
        # Method ShiftLeftLogical(value : Vector64`1, count : Byte) was skipped since it collides with above method
        # Method ShiftLeftLogical(value : Vector64`1, count : Byte) was skipped since it collides with above method
        # Method ShiftLeftLogical(value : Vector64`1, count : Byte) was skipped since it collides with above method

    # Skipped ShiftLeftLogicalSaturate due to it being static, abstract and generic.

    ShiftLeftLogicalSaturate : ShiftLeftLogicalSaturate_MethodGroup
    class ShiftLeftLogicalSaturate_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector64_1[int], count: int) -> Vector64_1[int]:...
        # Method ShiftLeftLogicalSaturate(value : Vector64`1, count : Byte) was skipped since it collides with above method
        # Method ShiftLeftLogicalSaturate(value : Vector64`1, count : Byte) was skipped since it collides with above method
        # Method ShiftLeftLogicalSaturate(value : Vector64`1, count : Byte) was skipped since it collides with above method
        # Method ShiftLeftLogicalSaturate(value : Vector64`1, count : Byte) was skipped since it collides with above method
        # Method ShiftLeftLogicalSaturate(value : Vector64`1, count : Byte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector128_1[int], count: int) -> Vector128_1[int]:...
        # Method ShiftLeftLogicalSaturate(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftLeftLogicalSaturate(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftLeftLogicalSaturate(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftLeftLogicalSaturate(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftLeftLogicalSaturate(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftLeftLogicalSaturate(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftLeftLogicalSaturate(value : Vector128`1, count : Byte) was skipped since it collides with above method

    # Skipped ShiftLeftLogicalSaturateScalar due to it being static, abstract and generic.

    ShiftLeftLogicalSaturateScalar : ShiftLeftLogicalSaturateScalar_MethodGroup
    class ShiftLeftLogicalSaturateScalar_MethodGroup:
        def __call__(self, value: Vector64_1[int], count: int) -> Vector64_1[int]:...
        # Method ShiftLeftLogicalSaturateScalar(value : Vector64`1, count : Byte) was skipped since it collides with above method

    # Skipped ShiftLeftLogicalSaturateUnsigned due to it being static, abstract and generic.

    ShiftLeftLogicalSaturateUnsigned : ShiftLeftLogicalSaturateUnsigned_MethodGroup
    class ShiftLeftLogicalSaturateUnsigned_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector64_1[int], count: int) -> Vector64_1[int]:...
        # Method ShiftLeftLogicalSaturateUnsigned(value : Vector64`1, count : Byte) was skipped since it collides with above method
        # Method ShiftLeftLogicalSaturateUnsigned(value : Vector64`1, count : Byte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector128_1[int], count: int) -> Vector128_1[int]:...
        # Method ShiftLeftLogicalSaturateUnsigned(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftLeftLogicalSaturateUnsigned(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftLeftLogicalSaturateUnsigned(value : Vector128`1, count : Byte) was skipped since it collides with above method

    # Skipped ShiftLeftLogicalScalar due to it being static, abstract and generic.

    ShiftLeftLogicalScalar : ShiftLeftLogicalScalar_MethodGroup
    class ShiftLeftLogicalScalar_MethodGroup:
        def __call__(self, value: Vector64_1[int], count: int) -> Vector64_1[int]:...
        # Method ShiftLeftLogicalScalar(value : Vector64`1, count : Byte) was skipped since it collides with above method

    # Skipped ShiftLeftLogicalWideningLower due to it being static, abstract and generic.

    ShiftLeftLogicalWideningLower : ShiftLeftLogicalWideningLower_MethodGroup
    class ShiftLeftLogicalWideningLower_MethodGroup:
        def __call__(self, value: Vector64_1[int], count: int) -> Vector128_1[int]:...
        # Method ShiftLeftLogicalWideningLower(value : Vector64`1, count : Byte) was skipped since it collides with above method
        # Method ShiftLeftLogicalWideningLower(value : Vector64`1, count : Byte) was skipped since it collides with above method
        # Method ShiftLeftLogicalWideningLower(value : Vector64`1, count : Byte) was skipped since it collides with above method
        # Method ShiftLeftLogicalWideningLower(value : Vector64`1, count : Byte) was skipped since it collides with above method
        # Method ShiftLeftLogicalWideningLower(value : Vector64`1, count : Byte) was skipped since it collides with above method

    # Skipped ShiftLeftLogicalWideningUpper due to it being static, abstract and generic.

    ShiftLeftLogicalWideningUpper : ShiftLeftLogicalWideningUpper_MethodGroup
    class ShiftLeftLogicalWideningUpper_MethodGroup:
        def __call__(self, value: Vector128_1[int], count: int) -> Vector128_1[int]:...
        # Method ShiftLeftLogicalWideningUpper(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftLeftLogicalWideningUpper(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftLeftLogicalWideningUpper(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftLeftLogicalWideningUpper(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftLeftLogicalWideningUpper(value : Vector128`1, count : Byte) was skipped since it collides with above method

    # Skipped ShiftLogical due to it being static, abstract and generic.

    ShiftLogical : ShiftLogical_MethodGroup
    class ShiftLogical_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector64_1[int], count: Vector64_1[int]) -> Vector64_1[int]:...
        # Method ShiftLogical(value : Vector64`1, count : Vector64`1) was skipped since it collides with above method
        # Method ShiftLogical(value : Vector64`1, count : Vector64`1) was skipped since it collides with above method
        # Method ShiftLogical(value : Vector64`1, count : Vector64`1) was skipped since it collides with above method
        # Method ShiftLogical(value : Vector64`1, count : Vector64`1) was skipped since it collides with above method
        # Method ShiftLogical(value : Vector64`1, count : Vector64`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector128_1[int], count: Vector128_1[int]) -> Vector128_1[int]:...
        # Method ShiftLogical(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method
        # Method ShiftLogical(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method
        # Method ShiftLogical(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method
        # Method ShiftLogical(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method
        # Method ShiftLogical(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method
        # Method ShiftLogical(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method
        # Method ShiftLogical(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method

    # Skipped ShiftLogicalRounded due to it being static, abstract and generic.

    ShiftLogicalRounded : ShiftLogicalRounded_MethodGroup
    class ShiftLogicalRounded_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector64_1[int], count: Vector64_1[int]) -> Vector64_1[int]:...
        # Method ShiftLogicalRounded(value : Vector64`1, count : Vector64`1) was skipped since it collides with above method
        # Method ShiftLogicalRounded(value : Vector64`1, count : Vector64`1) was skipped since it collides with above method
        # Method ShiftLogicalRounded(value : Vector64`1, count : Vector64`1) was skipped since it collides with above method
        # Method ShiftLogicalRounded(value : Vector64`1, count : Vector64`1) was skipped since it collides with above method
        # Method ShiftLogicalRounded(value : Vector64`1, count : Vector64`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector128_1[int], count: Vector128_1[int]) -> Vector128_1[int]:...
        # Method ShiftLogicalRounded(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method
        # Method ShiftLogicalRounded(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method
        # Method ShiftLogicalRounded(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method
        # Method ShiftLogicalRounded(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method
        # Method ShiftLogicalRounded(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method
        # Method ShiftLogicalRounded(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method
        # Method ShiftLogicalRounded(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method

    # Skipped ShiftLogicalRoundedSaturate due to it being static, abstract and generic.

    ShiftLogicalRoundedSaturate : ShiftLogicalRoundedSaturate_MethodGroup
    class ShiftLogicalRoundedSaturate_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector128_1[int], count: Vector128_1[int]) -> Vector128_1[int]:...
        # Method ShiftLogicalRoundedSaturate(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector64_1[int], count: Vector64_1[int]) -> Vector64_1[int]:...
        # Method ShiftLogicalRoundedSaturate(value : Vector64`1, count : Vector64`1) was skipped since it collides with above method
        # Method ShiftLogicalRoundedSaturate(value : Vector64`1, count : Vector64`1) was skipped since it collides with above method
        # Method ShiftLogicalRoundedSaturate(value : Vector64`1, count : Vector64`1) was skipped since it collides with above method
        # Method ShiftLogicalRoundedSaturate(value : Vector64`1, count : Vector64`1) was skipped since it collides with above method
        # Method ShiftLogicalRoundedSaturate(value : Vector64`1, count : Vector64`1) was skipped since it collides with above method
        # Method ShiftLogicalRoundedSaturate(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method
        # Method ShiftLogicalRoundedSaturate(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method
        # Method ShiftLogicalRoundedSaturate(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method
        # Method ShiftLogicalRoundedSaturate(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method
        # Method ShiftLogicalRoundedSaturate(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method
        # Method ShiftLogicalRoundedSaturate(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method

    # Skipped ShiftLogicalRoundedSaturateScalar due to it being static, abstract and generic.

    ShiftLogicalRoundedSaturateScalar : ShiftLogicalRoundedSaturateScalar_MethodGroup
    class ShiftLogicalRoundedSaturateScalar_MethodGroup:
        def __call__(self, value: Vector64_1[int], count: Vector64_1[int]) -> Vector64_1[int]:...
        # Method ShiftLogicalRoundedSaturateScalar(value : Vector64`1, count : Vector64`1) was skipped since it collides with above method

    # Skipped ShiftLogicalRoundedScalar due to it being static, abstract and generic.

    ShiftLogicalRoundedScalar : ShiftLogicalRoundedScalar_MethodGroup
    class ShiftLogicalRoundedScalar_MethodGroup:
        def __call__(self, value: Vector64_1[int], count: Vector64_1[int]) -> Vector64_1[int]:...
        # Method ShiftLogicalRoundedScalar(value : Vector64`1, count : Vector64`1) was skipped since it collides with above method

    # Skipped ShiftLogicalSaturate due to it being static, abstract and generic.

    ShiftLogicalSaturate : ShiftLogicalSaturate_MethodGroup
    class ShiftLogicalSaturate_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector64_1[int], count: Vector64_1[int]) -> Vector64_1[int]:...
        # Method ShiftLogicalSaturate(value : Vector64`1, count : Vector64`1) was skipped since it collides with above method
        # Method ShiftLogicalSaturate(value : Vector64`1, count : Vector64`1) was skipped since it collides with above method
        # Method ShiftLogicalSaturate(value : Vector64`1, count : Vector64`1) was skipped since it collides with above method
        # Method ShiftLogicalSaturate(value : Vector64`1, count : Vector64`1) was skipped since it collides with above method
        # Method ShiftLogicalSaturate(value : Vector64`1, count : Vector64`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector128_1[int], count: Vector128_1[int]) -> Vector128_1[int]:...
        # Method ShiftLogicalSaturate(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method
        # Method ShiftLogicalSaturate(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method
        # Method ShiftLogicalSaturate(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method
        # Method ShiftLogicalSaturate(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method
        # Method ShiftLogicalSaturate(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method
        # Method ShiftLogicalSaturate(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method
        # Method ShiftLogicalSaturate(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method

    # Skipped ShiftLogicalSaturateScalar due to it being static, abstract and generic.

    ShiftLogicalSaturateScalar : ShiftLogicalSaturateScalar_MethodGroup
    class ShiftLogicalSaturateScalar_MethodGroup:
        def __call__(self, value: Vector64_1[int], count: Vector64_1[int]) -> Vector64_1[int]:...
        # Method ShiftLogicalSaturateScalar(value : Vector64`1, count : Vector64`1) was skipped since it collides with above method

    # Skipped ShiftLogicalScalar due to it being static, abstract and generic.

    ShiftLogicalScalar : ShiftLogicalScalar_MethodGroup
    class ShiftLogicalScalar_MethodGroup:
        def __call__(self, value: Vector64_1[int], count: Vector64_1[int]) -> Vector64_1[int]:...
        # Method ShiftLogicalScalar(value : Vector64`1, count : Vector64`1) was skipped since it collides with above method

    # Skipped ShiftRightAndInsert due to it being static, abstract and generic.

    ShiftRightAndInsert : ShiftRightAndInsert_MethodGroup
    class ShiftRightAndInsert_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector64_1[int], right: Vector64_1[int], shift: int) -> Vector64_1[int]:...
        # Method ShiftRightAndInsert(left : Vector64`1, right : Vector64`1, shift : Byte) was skipped since it collides with above method
        # Method ShiftRightAndInsert(left : Vector64`1, right : Vector64`1, shift : Byte) was skipped since it collides with above method
        # Method ShiftRightAndInsert(left : Vector64`1, right : Vector64`1, shift : Byte) was skipped since it collides with above method
        # Method ShiftRightAndInsert(left : Vector64`1, right : Vector64`1, shift : Byte) was skipped since it collides with above method
        # Method ShiftRightAndInsert(left : Vector64`1, right : Vector64`1, shift : Byte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, left: Vector128_1[int], right: Vector128_1[int], shift: int) -> Vector128_1[int]:...
        # Method ShiftRightAndInsert(left : Vector128`1, right : Vector128`1, shift : Byte) was skipped since it collides with above method
        # Method ShiftRightAndInsert(left : Vector128`1, right : Vector128`1, shift : Byte) was skipped since it collides with above method
        # Method ShiftRightAndInsert(left : Vector128`1, right : Vector128`1, shift : Byte) was skipped since it collides with above method
        # Method ShiftRightAndInsert(left : Vector128`1, right : Vector128`1, shift : Byte) was skipped since it collides with above method
        # Method ShiftRightAndInsert(left : Vector128`1, right : Vector128`1, shift : Byte) was skipped since it collides with above method
        # Method ShiftRightAndInsert(left : Vector128`1, right : Vector128`1, shift : Byte) was skipped since it collides with above method
        # Method ShiftRightAndInsert(left : Vector128`1, right : Vector128`1, shift : Byte) was skipped since it collides with above method

    # Skipped ShiftRightAndInsertScalar due to it being static, abstract and generic.

    ShiftRightAndInsertScalar : ShiftRightAndInsertScalar_MethodGroup
    class ShiftRightAndInsertScalar_MethodGroup:
        def __call__(self, left: Vector64_1[int], right: Vector64_1[int], shift: int) -> Vector64_1[int]:...
        # Method ShiftRightAndInsertScalar(left : Vector64`1, right : Vector64`1, shift : Byte) was skipped since it collides with above method

    # Skipped ShiftRightArithmetic due to it being static, abstract and generic.

    ShiftRightArithmetic : ShiftRightArithmetic_MethodGroup
    class ShiftRightArithmetic_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector64_1[int], count: int) -> Vector64_1[int]:...
        # Method ShiftRightArithmetic(value : Vector64`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightArithmetic(value : Vector64`1, count : Byte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector128_1[int], count: int) -> Vector128_1[int]:...
        # Method ShiftRightArithmetic(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightArithmetic(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightArithmetic(value : Vector128`1, count : Byte) was skipped since it collides with above method

    # Skipped ShiftRightArithmeticAdd due to it being static, abstract and generic.

    ShiftRightArithmeticAdd : ShiftRightArithmeticAdd_MethodGroup
    class ShiftRightArithmeticAdd_MethodGroup:
        @typing.overload
        def __call__(self, addend: Vector64_1[int], value: Vector64_1[int], count: int) -> Vector64_1[int]:...
        # Method ShiftRightArithmeticAdd(addend : Vector64`1, value : Vector64`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightArithmeticAdd(addend : Vector64`1, value : Vector64`1, count : Byte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, addend: Vector128_1[int], value: Vector128_1[int], count: int) -> Vector128_1[int]:...
        # Method ShiftRightArithmeticAdd(addend : Vector128`1, value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightArithmeticAdd(addend : Vector128`1, value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightArithmeticAdd(addend : Vector128`1, value : Vector128`1, count : Byte) was skipped since it collides with above method

    # Skipped ShiftRightArithmeticNarrowingSaturateLower due to it being static, abstract and generic.

    ShiftRightArithmeticNarrowingSaturateLower : ShiftRightArithmeticNarrowingSaturateLower_MethodGroup
    class ShiftRightArithmeticNarrowingSaturateLower_MethodGroup:
        def __call__(self, value: Vector128_1[int], count: int) -> Vector64_1[int]:...
        # Method ShiftRightArithmeticNarrowingSaturateLower(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightArithmeticNarrowingSaturateLower(value : Vector128`1, count : Byte) was skipped since it collides with above method

    # Skipped ShiftRightArithmeticNarrowingSaturateUnsignedLower due to it being static, abstract and generic.

    ShiftRightArithmeticNarrowingSaturateUnsignedLower : ShiftRightArithmeticNarrowingSaturateUnsignedLower_MethodGroup
    class ShiftRightArithmeticNarrowingSaturateUnsignedLower_MethodGroup:
        def __call__(self, value: Vector128_1[int], count: int) -> Vector64_1[int]:...
        # Method ShiftRightArithmeticNarrowingSaturateUnsignedLower(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightArithmeticNarrowingSaturateUnsignedLower(value : Vector128`1, count : Byte) was skipped since it collides with above method

    # Skipped ShiftRightArithmeticNarrowingSaturateUnsignedUpper due to it being static, abstract and generic.

    ShiftRightArithmeticNarrowingSaturateUnsignedUpper : ShiftRightArithmeticNarrowingSaturateUnsignedUpper_MethodGroup
    class ShiftRightArithmeticNarrowingSaturateUnsignedUpper_MethodGroup:
        def __call__(self, lower: Vector64_1[int], value: Vector128_1[int], count: int) -> Vector128_1[int]:...
        # Method ShiftRightArithmeticNarrowingSaturateUnsignedUpper(lower : Vector64`1, value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightArithmeticNarrowingSaturateUnsignedUpper(lower : Vector64`1, value : Vector128`1, count : Byte) was skipped since it collides with above method

    # Skipped ShiftRightArithmeticNarrowingSaturateUpper due to it being static, abstract and generic.

    ShiftRightArithmeticNarrowingSaturateUpper : ShiftRightArithmeticNarrowingSaturateUpper_MethodGroup
    class ShiftRightArithmeticNarrowingSaturateUpper_MethodGroup:
        def __call__(self, lower: Vector64_1[int], value: Vector128_1[int], count: int) -> Vector128_1[int]:...
        # Method ShiftRightArithmeticNarrowingSaturateUpper(lower : Vector64`1, value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightArithmeticNarrowingSaturateUpper(lower : Vector64`1, value : Vector128`1, count : Byte) was skipped since it collides with above method

    # Skipped ShiftRightArithmeticRounded due to it being static, abstract and generic.

    ShiftRightArithmeticRounded : ShiftRightArithmeticRounded_MethodGroup
    class ShiftRightArithmeticRounded_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector64_1[int], count: int) -> Vector64_1[int]:...
        # Method ShiftRightArithmeticRounded(value : Vector64`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightArithmeticRounded(value : Vector64`1, count : Byte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector128_1[int], count: int) -> Vector128_1[int]:...
        # Method ShiftRightArithmeticRounded(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightArithmeticRounded(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightArithmeticRounded(value : Vector128`1, count : Byte) was skipped since it collides with above method

    # Skipped ShiftRightArithmeticRoundedAdd due to it being static, abstract and generic.

    ShiftRightArithmeticRoundedAdd : ShiftRightArithmeticRoundedAdd_MethodGroup
    class ShiftRightArithmeticRoundedAdd_MethodGroup:
        @typing.overload
        def __call__(self, addend: Vector64_1[int], value: Vector64_1[int], count: int) -> Vector64_1[int]:...
        # Method ShiftRightArithmeticRoundedAdd(addend : Vector64`1, value : Vector64`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightArithmeticRoundedAdd(addend : Vector64`1, value : Vector64`1, count : Byte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, addend: Vector128_1[int], value: Vector128_1[int], count: int) -> Vector128_1[int]:...
        # Method ShiftRightArithmeticRoundedAdd(addend : Vector128`1, value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightArithmeticRoundedAdd(addend : Vector128`1, value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightArithmeticRoundedAdd(addend : Vector128`1, value : Vector128`1, count : Byte) was skipped since it collides with above method

    # Skipped ShiftRightArithmeticRoundedNarrowingSaturateLower due to it being static, abstract and generic.

    ShiftRightArithmeticRoundedNarrowingSaturateLower : ShiftRightArithmeticRoundedNarrowingSaturateLower_MethodGroup
    class ShiftRightArithmeticRoundedNarrowingSaturateLower_MethodGroup:
        def __call__(self, value: Vector128_1[int], count: int) -> Vector64_1[int]:...
        # Method ShiftRightArithmeticRoundedNarrowingSaturateLower(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightArithmeticRoundedNarrowingSaturateLower(value : Vector128`1, count : Byte) was skipped since it collides with above method

    # Skipped ShiftRightArithmeticRoundedNarrowingSaturateUnsignedLower due to it being static, abstract and generic.

    ShiftRightArithmeticRoundedNarrowingSaturateUnsignedLower : ShiftRightArithmeticRoundedNarrowingSaturateUnsignedLower_MethodGroup
    class ShiftRightArithmeticRoundedNarrowingSaturateUnsignedLower_MethodGroup:
        def __call__(self, value: Vector128_1[int], count: int) -> Vector64_1[int]:...
        # Method ShiftRightArithmeticRoundedNarrowingSaturateUnsignedLower(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightArithmeticRoundedNarrowingSaturateUnsignedLower(value : Vector128`1, count : Byte) was skipped since it collides with above method

    # Skipped ShiftRightArithmeticRoundedNarrowingSaturateUnsignedUpper due to it being static, abstract and generic.

    ShiftRightArithmeticRoundedNarrowingSaturateUnsignedUpper : ShiftRightArithmeticRoundedNarrowingSaturateUnsignedUpper_MethodGroup
    class ShiftRightArithmeticRoundedNarrowingSaturateUnsignedUpper_MethodGroup:
        def __call__(self, lower: Vector64_1[int], value: Vector128_1[int], count: int) -> Vector128_1[int]:...
        # Method ShiftRightArithmeticRoundedNarrowingSaturateUnsignedUpper(lower : Vector64`1, value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightArithmeticRoundedNarrowingSaturateUnsignedUpper(lower : Vector64`1, value : Vector128`1, count : Byte) was skipped since it collides with above method

    # Skipped ShiftRightArithmeticRoundedNarrowingSaturateUpper due to it being static, abstract and generic.

    ShiftRightArithmeticRoundedNarrowingSaturateUpper : ShiftRightArithmeticRoundedNarrowingSaturateUpper_MethodGroup
    class ShiftRightArithmeticRoundedNarrowingSaturateUpper_MethodGroup:
        def __call__(self, lower: Vector64_1[int], value: Vector128_1[int], count: int) -> Vector128_1[int]:...
        # Method ShiftRightArithmeticRoundedNarrowingSaturateUpper(lower : Vector64`1, value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightArithmeticRoundedNarrowingSaturateUpper(lower : Vector64`1, value : Vector128`1, count : Byte) was skipped since it collides with above method

    # Skipped ShiftRightLogical due to it being static, abstract and generic.

    ShiftRightLogical : ShiftRightLogical_MethodGroup
    class ShiftRightLogical_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector64_1[int], count: int) -> Vector64_1[int]:...
        # Method ShiftRightLogical(value : Vector64`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogical(value : Vector64`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogical(value : Vector64`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogical(value : Vector64`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogical(value : Vector64`1, count : Byte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector128_1[int], count: int) -> Vector128_1[int]:...
        # Method ShiftRightLogical(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogical(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogical(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogical(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogical(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogical(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogical(value : Vector128`1, count : Byte) was skipped since it collides with above method

    # Skipped ShiftRightLogicalAdd due to it being static, abstract and generic.

    ShiftRightLogicalAdd : ShiftRightLogicalAdd_MethodGroup
    class ShiftRightLogicalAdd_MethodGroup:
        @typing.overload
        def __call__(self, addend: Vector64_1[int], value: Vector64_1[int], count: int) -> Vector64_1[int]:...
        # Method ShiftRightLogicalAdd(addend : Vector64`1, value : Vector64`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalAdd(addend : Vector64`1, value : Vector64`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalAdd(addend : Vector64`1, value : Vector64`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalAdd(addend : Vector64`1, value : Vector64`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalAdd(addend : Vector64`1, value : Vector64`1, count : Byte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, addend: Vector128_1[int], value: Vector128_1[int], count: int) -> Vector128_1[int]:...
        # Method ShiftRightLogicalAdd(addend : Vector128`1, value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalAdd(addend : Vector128`1, value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalAdd(addend : Vector128`1, value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalAdd(addend : Vector128`1, value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalAdd(addend : Vector128`1, value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalAdd(addend : Vector128`1, value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalAdd(addend : Vector128`1, value : Vector128`1, count : Byte) was skipped since it collides with above method

    # Skipped ShiftRightLogicalAddScalar due to it being static, abstract and generic.

    ShiftRightLogicalAddScalar : ShiftRightLogicalAddScalar_MethodGroup
    class ShiftRightLogicalAddScalar_MethodGroup:
        def __call__(self, addend: Vector64_1[int], value: Vector64_1[int], count: int) -> Vector64_1[int]:...
        # Method ShiftRightLogicalAddScalar(addend : Vector64`1, value : Vector64`1, count : Byte) was skipped since it collides with above method

    # Skipped ShiftRightLogicalNarrowingLower due to it being static, abstract and generic.

    ShiftRightLogicalNarrowingLower : ShiftRightLogicalNarrowingLower_MethodGroup
    class ShiftRightLogicalNarrowingLower_MethodGroup:
        def __call__(self, value: Vector128_1[int], count: int) -> Vector64_1[int]:...
        # Method ShiftRightLogicalNarrowingLower(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalNarrowingLower(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalNarrowingLower(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalNarrowingLower(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalNarrowingLower(value : Vector128`1, count : Byte) was skipped since it collides with above method

    # Skipped ShiftRightLogicalNarrowingSaturateLower due to it being static, abstract and generic.

    ShiftRightLogicalNarrowingSaturateLower : ShiftRightLogicalNarrowingSaturateLower_MethodGroup
    class ShiftRightLogicalNarrowingSaturateLower_MethodGroup:
        def __call__(self, value: Vector128_1[int], count: int) -> Vector64_1[int]:...
        # Method ShiftRightLogicalNarrowingSaturateLower(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalNarrowingSaturateLower(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalNarrowingSaturateLower(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalNarrowingSaturateLower(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalNarrowingSaturateLower(value : Vector128`1, count : Byte) was skipped since it collides with above method

    # Skipped ShiftRightLogicalNarrowingSaturateUpper due to it being static, abstract and generic.

    ShiftRightLogicalNarrowingSaturateUpper : ShiftRightLogicalNarrowingSaturateUpper_MethodGroup
    class ShiftRightLogicalNarrowingSaturateUpper_MethodGroup:
        def __call__(self, lower: Vector64_1[int], value: Vector128_1[int], count: int) -> Vector128_1[int]:...
        # Method ShiftRightLogicalNarrowingSaturateUpper(lower : Vector64`1, value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalNarrowingSaturateUpper(lower : Vector64`1, value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalNarrowingSaturateUpper(lower : Vector64`1, value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalNarrowingSaturateUpper(lower : Vector64`1, value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalNarrowingSaturateUpper(lower : Vector64`1, value : Vector128`1, count : Byte) was skipped since it collides with above method

    # Skipped ShiftRightLogicalNarrowingUpper due to it being static, abstract and generic.

    ShiftRightLogicalNarrowingUpper : ShiftRightLogicalNarrowingUpper_MethodGroup
    class ShiftRightLogicalNarrowingUpper_MethodGroup:
        def __call__(self, lower: Vector64_1[int], value: Vector128_1[int], count: int) -> Vector128_1[int]:...
        # Method ShiftRightLogicalNarrowingUpper(lower : Vector64`1, value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalNarrowingUpper(lower : Vector64`1, value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalNarrowingUpper(lower : Vector64`1, value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalNarrowingUpper(lower : Vector64`1, value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalNarrowingUpper(lower : Vector64`1, value : Vector128`1, count : Byte) was skipped since it collides with above method

    # Skipped ShiftRightLogicalRounded due to it being static, abstract and generic.

    ShiftRightLogicalRounded : ShiftRightLogicalRounded_MethodGroup
    class ShiftRightLogicalRounded_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector64_1[int], count: int) -> Vector64_1[int]:...
        # Method ShiftRightLogicalRounded(value : Vector64`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalRounded(value : Vector64`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalRounded(value : Vector64`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalRounded(value : Vector64`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalRounded(value : Vector64`1, count : Byte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector128_1[int], count: int) -> Vector128_1[int]:...
        # Method ShiftRightLogicalRounded(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalRounded(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalRounded(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalRounded(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalRounded(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalRounded(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalRounded(value : Vector128`1, count : Byte) was skipped since it collides with above method

    # Skipped ShiftRightLogicalRoundedAdd due to it being static, abstract and generic.

    ShiftRightLogicalRoundedAdd : ShiftRightLogicalRoundedAdd_MethodGroup
    class ShiftRightLogicalRoundedAdd_MethodGroup:
        @typing.overload
        def __call__(self, addend: Vector128_1[int], value: Vector128_1[int], count: int) -> Vector128_1[int]:...
        # Method ShiftRightLogicalRoundedAdd(addend : Vector128`1, value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalRoundedAdd(addend : Vector128`1, value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalRoundedAdd(addend : Vector128`1, value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalRoundedAdd(addend : Vector128`1, value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalRoundedAdd(addend : Vector128`1, value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalRoundedAdd(addend : Vector128`1, value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalRoundedAdd(addend : Vector128`1, value : Vector128`1, count : Byte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, addend: Vector64_1[int], value: Vector64_1[int], count: int) -> Vector64_1[int]:...
        # Method ShiftRightLogicalRoundedAdd(addend : Vector64`1, value : Vector64`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalRoundedAdd(addend : Vector64`1, value : Vector64`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalRoundedAdd(addend : Vector64`1, value : Vector64`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalRoundedAdd(addend : Vector64`1, value : Vector64`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalRoundedAdd(addend : Vector64`1, value : Vector64`1, count : Byte) was skipped since it collides with above method

    # Skipped ShiftRightLogicalRoundedAddScalar due to it being static, abstract and generic.

    ShiftRightLogicalRoundedAddScalar : ShiftRightLogicalRoundedAddScalar_MethodGroup
    class ShiftRightLogicalRoundedAddScalar_MethodGroup:
        def __call__(self, addend: Vector64_1[int], value: Vector64_1[int], count: int) -> Vector64_1[int]:...
        # Method ShiftRightLogicalRoundedAddScalar(addend : Vector64`1, value : Vector64`1, count : Byte) was skipped since it collides with above method

    # Skipped ShiftRightLogicalRoundedNarrowingLower due to it being static, abstract and generic.

    ShiftRightLogicalRoundedNarrowingLower : ShiftRightLogicalRoundedNarrowingLower_MethodGroup
    class ShiftRightLogicalRoundedNarrowingLower_MethodGroup:
        def __call__(self, value: Vector128_1[int], count: int) -> Vector64_1[int]:...
        # Method ShiftRightLogicalRoundedNarrowingLower(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalRoundedNarrowingLower(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalRoundedNarrowingLower(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalRoundedNarrowingLower(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalRoundedNarrowingLower(value : Vector128`1, count : Byte) was skipped since it collides with above method

    # Skipped ShiftRightLogicalRoundedNarrowingSaturateLower due to it being static, abstract and generic.

    ShiftRightLogicalRoundedNarrowingSaturateLower : ShiftRightLogicalRoundedNarrowingSaturateLower_MethodGroup
    class ShiftRightLogicalRoundedNarrowingSaturateLower_MethodGroup:
        def __call__(self, value: Vector128_1[int], count: int) -> Vector64_1[int]:...
        # Method ShiftRightLogicalRoundedNarrowingSaturateLower(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalRoundedNarrowingSaturateLower(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalRoundedNarrowingSaturateLower(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalRoundedNarrowingSaturateLower(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalRoundedNarrowingSaturateLower(value : Vector128`1, count : Byte) was skipped since it collides with above method

    # Skipped ShiftRightLogicalRoundedNarrowingSaturateUpper due to it being static, abstract and generic.

    ShiftRightLogicalRoundedNarrowingSaturateUpper : ShiftRightLogicalRoundedNarrowingSaturateUpper_MethodGroup
    class ShiftRightLogicalRoundedNarrowingSaturateUpper_MethodGroup:
        def __call__(self, lower: Vector64_1[int], value: Vector128_1[int], count: int) -> Vector128_1[int]:...
        # Method ShiftRightLogicalRoundedNarrowingSaturateUpper(lower : Vector64`1, value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalRoundedNarrowingSaturateUpper(lower : Vector64`1, value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalRoundedNarrowingSaturateUpper(lower : Vector64`1, value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalRoundedNarrowingSaturateUpper(lower : Vector64`1, value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalRoundedNarrowingSaturateUpper(lower : Vector64`1, value : Vector128`1, count : Byte) was skipped since it collides with above method

    # Skipped ShiftRightLogicalRoundedNarrowingUpper due to it being static, abstract and generic.

    ShiftRightLogicalRoundedNarrowingUpper : ShiftRightLogicalRoundedNarrowingUpper_MethodGroup
    class ShiftRightLogicalRoundedNarrowingUpper_MethodGroup:
        def __call__(self, lower: Vector64_1[int], value: Vector128_1[int], count: int) -> Vector128_1[int]:...
        # Method ShiftRightLogicalRoundedNarrowingUpper(lower : Vector64`1, value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalRoundedNarrowingUpper(lower : Vector64`1, value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalRoundedNarrowingUpper(lower : Vector64`1, value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalRoundedNarrowingUpper(lower : Vector64`1, value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogicalRoundedNarrowingUpper(lower : Vector64`1, value : Vector128`1, count : Byte) was skipped since it collides with above method

    # Skipped ShiftRightLogicalRoundedScalar due to it being static, abstract and generic.

    ShiftRightLogicalRoundedScalar : ShiftRightLogicalRoundedScalar_MethodGroup
    class ShiftRightLogicalRoundedScalar_MethodGroup:
        def __call__(self, value: Vector64_1[int], count: int) -> Vector64_1[int]:...
        # Method ShiftRightLogicalRoundedScalar(value : Vector64`1, count : Byte) was skipped since it collides with above method

    # Skipped ShiftRightLogicalScalar due to it being static, abstract and generic.

    ShiftRightLogicalScalar : ShiftRightLogicalScalar_MethodGroup
    class ShiftRightLogicalScalar_MethodGroup:
        def __call__(self, value: Vector64_1[int], count: int) -> Vector64_1[int]:...
        # Method ShiftRightLogicalScalar(value : Vector64`1, count : Byte) was skipped since it collides with above method

    # Skipped SignExtendWideningLower due to it being static, abstract and generic.

    SignExtendWideningLower : SignExtendWideningLower_MethodGroup
    class SignExtendWideningLower_MethodGroup:
        def __call__(self, value: Vector64_1[int]) -> Vector128_1[int]:...
        # Method SignExtendWideningLower(value : Vector64`1) was skipped since it collides with above method
        # Method SignExtendWideningLower(value : Vector64`1) was skipped since it collides with above method

    # Skipped SignExtendWideningUpper due to it being static, abstract and generic.

    SignExtendWideningUpper : SignExtendWideningUpper_MethodGroup
    class SignExtendWideningUpper_MethodGroup:
        def __call__(self, value: Vector128_1[int]) -> Vector128_1[int]:...
        # Method SignExtendWideningUpper(value : Vector128`1) was skipped since it collides with above method
        # Method SignExtendWideningUpper(value : Vector128`1) was skipped since it collides with above method

    # Skipped SqrtScalar due to it being static, abstract and generic.

    SqrtScalar : SqrtScalar_MethodGroup
    class SqrtScalar_MethodGroup:
        def __call__(self, value: Vector64_1[float]) -> Vector64_1[float]:...
        # Method SqrtScalar(value : Vector64`1) was skipped since it collides with above method

    # Skipped Store due to it being static, abstract and generic.

    Store : Store_MethodGroup
    class Store_MethodGroup:
        @typing.overload
        def __call__(self, address: clr.Reference[float], source: Vector64_1[float]) -> None:...
        # Method Store(address : Single*, source : Vector64`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, address: clr.Reference[float], source: Vector128_1[float]) -> None:...
        # Method Store(address : Single*, source : Vector128`1) was skipped since it collides with above method
        # Method Store(address : Byte*, source : Vector64`1) was skipped since it collides with above method
        # Method Store(address : Int16*, source : Vector64`1) was skipped since it collides with above method
        # Method Store(address : Int32*, source : Vector64`1) was skipped since it collides with above method
        # Method Store(address : Int64*, source : Vector64`1) was skipped since it collides with above method
        # Method Store(address : SByte*, source : Vector64`1) was skipped since it collides with above method
        # Method Store(address : UInt16*, source : Vector64`1) was skipped since it collides with above method
        # Method Store(address : UInt32*, source : Vector64`1) was skipped since it collides with above method
        # Method Store(address : UInt64*, source : Vector64`1) was skipped since it collides with above method
        # Method Store(address : Byte*, source : Vector128`1) was skipped since it collides with above method
        # Method Store(address : Int16*, source : Vector128`1) was skipped since it collides with above method
        # Method Store(address : Int32*, source : Vector128`1) was skipped since it collides with above method
        # Method Store(address : Int64*, source : Vector128`1) was skipped since it collides with above method
        # Method Store(address : SByte*, source : Vector128`1) was skipped since it collides with above method
        # Method Store(address : UInt16*, source : Vector128`1) was skipped since it collides with above method
        # Method Store(address : UInt32*, source : Vector128`1) was skipped since it collides with above method
        # Method Store(address : UInt64*, source : Vector128`1) was skipped since it collides with above method

    # Skipped StoreSelectedScalar due to it being static, abstract and generic.

    StoreSelectedScalar : StoreSelectedScalar_MethodGroup
    class StoreSelectedScalar_MethodGroup:
        @typing.overload
        def __call__(self, address: clr.Reference[float], value: Vector64_1[float], index: int) -> None:...
        @typing.overload
        def __call__(self, address: clr.Reference[float], value: Vector128_1[float], index: int) -> None:...
        # Method StoreSelectedScalar(address : Single*, value : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method StoreSelectedScalar(address : Byte*, value : Vector64`1, index : Byte) was skipped since it collides with above method
        # Method StoreSelectedScalar(address : Int16*, value : Vector64`1, index : Byte) was skipped since it collides with above method
        # Method StoreSelectedScalar(address : Int32*, value : Vector64`1, index : Byte) was skipped since it collides with above method
        # Method StoreSelectedScalar(address : SByte*, value : Vector64`1, index : Byte) was skipped since it collides with above method
        # Method StoreSelectedScalar(address : UInt16*, value : Vector64`1, index : Byte) was skipped since it collides with above method
        # Method StoreSelectedScalar(address : UInt32*, value : Vector64`1, index : Byte) was skipped since it collides with above method
        # Method StoreSelectedScalar(address : Byte*, value : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method StoreSelectedScalar(address : Int16*, value : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method StoreSelectedScalar(address : Int32*, value : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method StoreSelectedScalar(address : Int64*, value : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method StoreSelectedScalar(address : SByte*, value : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method StoreSelectedScalar(address : UInt16*, value : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method StoreSelectedScalar(address : UInt32*, value : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method StoreSelectedScalar(address : UInt64*, value : Vector128`1, index : Byte) was skipped since it collides with above method

    # Skipped Subtract due to it being static, abstract and generic.

    Subtract : Subtract_MethodGroup
    class Subtract_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
        @typing.overload
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
        # Method Subtract(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method Subtract(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method Subtract(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method Subtract(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method Subtract(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Subtract(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Subtract(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Subtract(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Subtract(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Subtract(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Subtract(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Subtract(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Subtract(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method Subtract(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

    # Skipped SubtractHighNarrowingLower due to it being static, abstract and generic.

    SubtractHighNarrowingLower : SubtractHighNarrowingLower_MethodGroup
    class SubtractHighNarrowingLower_MethodGroup:
        def __call__(self, left: Vector128_1[int], right: Vector128_1[int]) -> Vector64_1[int]:...
        # Method SubtractHighNarrowingLower(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method SubtractHighNarrowingLower(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method SubtractHighNarrowingLower(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method SubtractHighNarrowingLower(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method SubtractHighNarrowingLower(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped SubtractHighNarrowingUpper due to it being static, abstract and generic.

    SubtractHighNarrowingUpper : SubtractHighNarrowingUpper_MethodGroup
    class SubtractHighNarrowingUpper_MethodGroup:
        def __call__(self, lower: Vector64_1[int], left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
        # Method SubtractHighNarrowingUpper(lower : Vector64`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method SubtractHighNarrowingUpper(lower : Vector64`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method SubtractHighNarrowingUpper(lower : Vector64`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method SubtractHighNarrowingUpper(lower : Vector64`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method SubtractHighNarrowingUpper(lower : Vector64`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped SubtractRoundedHighNarrowingLower due to it being static, abstract and generic.

    SubtractRoundedHighNarrowingLower : SubtractRoundedHighNarrowingLower_MethodGroup
    class SubtractRoundedHighNarrowingLower_MethodGroup:
        def __call__(self, left: Vector128_1[int], right: Vector128_1[int]) -> Vector64_1[int]:...
        # Method SubtractRoundedHighNarrowingLower(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method SubtractRoundedHighNarrowingLower(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method SubtractRoundedHighNarrowingLower(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method SubtractRoundedHighNarrowingLower(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method SubtractRoundedHighNarrowingLower(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped SubtractRoundedHighNarrowingUpper due to it being static, abstract and generic.

    SubtractRoundedHighNarrowingUpper : SubtractRoundedHighNarrowingUpper_MethodGroup
    class SubtractRoundedHighNarrowingUpper_MethodGroup:
        def __call__(self, lower: Vector64_1[int], left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
        # Method SubtractRoundedHighNarrowingUpper(lower : Vector64`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method SubtractRoundedHighNarrowingUpper(lower : Vector64`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method SubtractRoundedHighNarrowingUpper(lower : Vector64`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method SubtractRoundedHighNarrowingUpper(lower : Vector64`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method SubtractRoundedHighNarrowingUpper(lower : Vector64`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped SubtractSaturate due to it being static, abstract and generic.

    SubtractSaturate : SubtractSaturate_MethodGroup
    class SubtractSaturate_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector64_1[int], right: Vector64_1[int]) -> Vector64_1[int]:...
        # Method SubtractSaturate(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method SubtractSaturate(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method SubtractSaturate(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method SubtractSaturate(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method SubtractSaturate(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
        # Method SubtractSaturate(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method SubtractSaturate(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method SubtractSaturate(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method SubtractSaturate(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method SubtractSaturate(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method SubtractSaturate(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method SubtractSaturate(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped SubtractSaturateScalar due to it being static, abstract and generic.

    SubtractSaturateScalar : SubtractSaturateScalar_MethodGroup
    class SubtractSaturateScalar_MethodGroup:
        def __call__(self, left: Vector64_1[int], right: Vector64_1[int]) -> Vector64_1[int]:...
        # Method SubtractSaturateScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

    # Skipped SubtractScalar due to it being static, abstract and generic.

    SubtractScalar : SubtractScalar_MethodGroup
    class SubtractScalar_MethodGroup:
        def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
        # Method SubtractScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method SubtractScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method SubtractScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

    # Skipped SubtractWideningLower due to it being static, abstract and generic.

    SubtractWideningLower : SubtractWideningLower_MethodGroup
    class SubtractWideningLower_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector64_1[int], right: Vector64_1[int]) -> Vector128_1[int]:...
        # Method SubtractWideningLower(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method SubtractWideningLower(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method SubtractWideningLower(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method SubtractWideningLower(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method SubtractWideningLower(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, left: Vector128_1[int], right: Vector64_1[int]) -> Vector128_1[int]:...
        # Method SubtractWideningLower(left : Vector128`1, right : Vector64`1) was skipped since it collides with above method
        # Method SubtractWideningLower(left : Vector128`1, right : Vector64`1) was skipped since it collides with above method
        # Method SubtractWideningLower(left : Vector128`1, right : Vector64`1) was skipped since it collides with above method
        # Method SubtractWideningLower(left : Vector128`1, right : Vector64`1) was skipped since it collides with above method
        # Method SubtractWideningLower(left : Vector128`1, right : Vector64`1) was skipped since it collides with above method

    # Skipped SubtractWideningUpper due to it being static, abstract and generic.

    SubtractWideningUpper : SubtractWideningUpper_MethodGroup
    class SubtractWideningUpper_MethodGroup:
        def __call__(self, left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
        # Method SubtractWideningUpper(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method SubtractWideningUpper(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method SubtractWideningUpper(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method SubtractWideningUpper(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method SubtractWideningUpper(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method SubtractWideningUpper(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method SubtractWideningUpper(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method SubtractWideningUpper(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method SubtractWideningUpper(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method SubtractWideningUpper(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method SubtractWideningUpper(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped VectorTableLookup due to it being static, abstract and generic.

    VectorTableLookup : VectorTableLookup_MethodGroup
    class VectorTableLookup_MethodGroup:
        def __call__(self, table: Vector128_1[int], byteIndexes: Vector64_1[int]) -> Vector64_1[int]:...
        # Method VectorTableLookup(table : Vector128`1, byteIndexes : Vector64`1) was skipped since it collides with above method

    # Skipped VectorTableLookupExtension due to it being static, abstract and generic.

    VectorTableLookupExtension : VectorTableLookupExtension_MethodGroup
    class VectorTableLookupExtension_MethodGroup:
        def __call__(self, defaultValues: Vector64_1[int], table: Vector128_1[int], byteIndexes: Vector64_1[int]) -> Vector64_1[int]:...
        # Method VectorTableLookupExtension(defaultValues : Vector64`1, table : Vector128`1, byteIndexes : Vector64`1) was skipped since it collides with above method

    # Skipped Xor due to it being static, abstract and generic.

    Xor : Xor_MethodGroup
    class Xor_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
        # Method Xor(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
        # Method Xor(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Xor(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method Xor(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method Xor(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method Xor(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method Xor(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method Xor(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method Xor(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method Xor(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        # Method Xor(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Xor(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Xor(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Xor(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Xor(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Xor(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Xor(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Xor(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped ZeroExtendWideningLower due to it being static, abstract and generic.

    ZeroExtendWideningLower : ZeroExtendWideningLower_MethodGroup
    class ZeroExtendWideningLower_MethodGroup:
        def __call__(self, value: Vector64_1[int]) -> Vector128_1[int]:...
        # Method ZeroExtendWideningLower(value : Vector64`1) was skipped since it collides with above method
        # Method ZeroExtendWideningLower(value : Vector64`1) was skipped since it collides with above method
        # Method ZeroExtendWideningLower(value : Vector64`1) was skipped since it collides with above method
        # Method ZeroExtendWideningLower(value : Vector64`1) was skipped since it collides with above method
        # Method ZeroExtendWideningLower(value : Vector64`1) was skipped since it collides with above method

    # Skipped ZeroExtendWideningUpper due to it being static, abstract and generic.

    ZeroExtendWideningUpper : ZeroExtendWideningUpper_MethodGroup
    class ZeroExtendWideningUpper_MethodGroup:
        def __call__(self, value: Vector128_1[int]) -> Vector128_1[int]:...
        # Method ZeroExtendWideningUpper(value : Vector128`1) was skipped since it collides with above method
        # Method ZeroExtendWideningUpper(value : Vector128`1) was skipped since it collides with above method
        # Method ZeroExtendWideningUpper(value : Vector128`1) was skipped since it collides with above method
        # Method ZeroExtendWideningUpper(value : Vector128`1) was skipped since it collides with above method
        # Method ZeroExtendWideningUpper(value : Vector128`1) was skipped since it collides with above method


    class Arm64(ArmBase.Arm64):
        @classmethod
        @property
        def IsSupported(cls) -> bool: ...
        @staticmethod
        def AbsoluteCompareGreaterThan(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
        @staticmethod
        def AbsoluteCompareGreaterThanOrEqual(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
        @staticmethod
        def AbsoluteCompareLessThan(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
        @staticmethod
        def AbsoluteCompareLessThanOrEqual(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
        @staticmethod
        def AbsoluteDifference(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
        @staticmethod
        def AbsSaturate(value: Vector128_1[int]) -> Vector128_1[int]: ...
        @staticmethod
        def AbsScalar(value: Vector64_1[int]) -> Vector64_1[int]: ...
        @staticmethod
        def Add(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
        @staticmethod
        def Ceiling(value: Vector128_1[float]) -> Vector128_1[float]: ...
        @staticmethod
        def ConvertToDoubleUpper(value: Vector128_1[float]) -> Vector128_1[float]: ...
        @staticmethod
        def ConvertToInt64RoundAwayFromZero(value: Vector128_1[float]) -> Vector128_1[int]: ...
        @staticmethod
        def ConvertToInt64RoundAwayFromZeroScalar(value: Vector64_1[float]) -> Vector64_1[int]: ...
        @staticmethod
        def ConvertToInt64RoundToEven(value: Vector128_1[float]) -> Vector128_1[int]: ...
        @staticmethod
        def ConvertToInt64RoundToEvenScalar(value: Vector64_1[float]) -> Vector64_1[int]: ...
        @staticmethod
        def ConvertToInt64RoundToNegativeInfinity(value: Vector128_1[float]) -> Vector128_1[int]: ...
        @staticmethod
        def ConvertToInt64RoundToNegativeInfinityScalar(value: Vector64_1[float]) -> Vector64_1[int]: ...
        @staticmethod
        def ConvertToInt64RoundToPositiveInfinity(value: Vector128_1[float]) -> Vector128_1[int]: ...
        @staticmethod
        def ConvertToInt64RoundToPositiveInfinityScalar(value: Vector64_1[float]) -> Vector64_1[int]: ...
        @staticmethod
        def ConvertToInt64RoundToZero(value: Vector128_1[float]) -> Vector128_1[int]: ...
        @staticmethod
        def ConvertToInt64RoundToZeroScalar(value: Vector64_1[float]) -> Vector64_1[int]: ...
        @staticmethod
        def ConvertToSingleLower(value: Vector128_1[float]) -> Vector64_1[float]: ...
        @staticmethod
        def ConvertToSingleRoundToOddLower(value: Vector128_1[float]) -> Vector64_1[float]: ...
        @staticmethod
        def ConvertToSingleRoundToOddUpper(lower: Vector64_1[float], value: Vector128_1[float]) -> Vector128_1[float]: ...
        @staticmethod
        def ConvertToSingleUpper(lower: Vector64_1[float], value: Vector128_1[float]) -> Vector128_1[float]: ...
        @staticmethod
        def ConvertToUInt64RoundAwayFromZero(value: Vector128_1[float]) -> Vector128_1[int]: ...
        @staticmethod
        def ConvertToUInt64RoundAwayFromZeroScalar(value: Vector64_1[float]) -> Vector64_1[int]: ...
        @staticmethod
        def ConvertToUInt64RoundToEven(value: Vector128_1[float]) -> Vector128_1[int]: ...
        @staticmethod
        def ConvertToUInt64RoundToEvenScalar(value: Vector64_1[float]) -> Vector64_1[int]: ...
        @staticmethod
        def ConvertToUInt64RoundToNegativeInfinity(value: Vector128_1[float]) -> Vector128_1[int]: ...
        @staticmethod
        def ConvertToUInt64RoundToNegativeInfinityScalar(value: Vector64_1[float]) -> Vector64_1[int]: ...
        @staticmethod
        def ConvertToUInt64RoundToPositiveInfinity(value: Vector128_1[float]) -> Vector128_1[int]: ...
        @staticmethod
        def ConvertToUInt64RoundToPositiveInfinityScalar(value: Vector64_1[float]) -> Vector64_1[int]: ...
        @staticmethod
        def ConvertToUInt64RoundToZero(value: Vector128_1[float]) -> Vector128_1[int]: ...
        @staticmethod
        def ConvertToUInt64RoundToZeroScalar(value: Vector64_1[float]) -> Vector64_1[int]: ...
        @staticmethod
        def Floor(value: Vector128_1[float]) -> Vector128_1[float]: ...
        @staticmethod
        def FusedMultiplyAdd(addend: Vector128_1[float], left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
        @staticmethod
        def FusedMultiplySubtract(minuend: Vector128_1[float], left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
        @staticmethod
        def Max(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
        @staticmethod
        def MaxNumber(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
        @staticmethod
        def MaxNumberAcross(value: Vector128_1[float]) -> Vector64_1[float]: ...
        @staticmethod
        def Min(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
        @staticmethod
        def MinNumber(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
        @staticmethod
        def MinNumberAcross(value: Vector128_1[float]) -> Vector64_1[float]: ...
        @staticmethod
        def Multiply(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
        @staticmethod
        def MultiplyByScalar(left: Vector128_1[float], right: Vector64_1[float]) -> Vector128_1[float]: ...
        @staticmethod
        def MultiplyBySelectedScalar(left: Vector128_1[float], right: Vector128_1[float], rightIndex: int) -> Vector128_1[float]: ...
        @staticmethod
        def MultiplyExtendedByScalar(left: Vector128_1[float], right: Vector64_1[float]) -> Vector128_1[float]: ...
        @staticmethod
        def MultiplyScalarBySelectedScalar(left: Vector64_1[float], right: Vector128_1[float], rightIndex: int) -> Vector64_1[float]: ...
        @staticmethod
        def NegateSaturate(value: Vector128_1[int]) -> Vector128_1[int]: ...
        @staticmethod
        def NegateScalar(value: Vector64_1[int]) -> Vector64_1[int]: ...
        @staticmethod
        def ReciprocalEstimate(value: Vector128_1[float]) -> Vector128_1[float]: ...
        @staticmethod
        def ReciprocalSquareRootEstimate(value: Vector128_1[float]) -> Vector128_1[float]: ...
        @staticmethod
        def ReciprocalSquareRootStep(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
        @staticmethod
        def ReciprocalStep(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
        @staticmethod
        def RoundAwayFromZero(value: Vector128_1[float]) -> Vector128_1[float]: ...
        @staticmethod
        def RoundToNearest(value: Vector128_1[float]) -> Vector128_1[float]: ...
        @staticmethod
        def RoundToNegativeInfinity(value: Vector128_1[float]) -> Vector128_1[float]: ...
        @staticmethod
        def RoundToPositiveInfinity(value: Vector128_1[float]) -> Vector128_1[float]: ...
        @staticmethod
        def RoundToZero(value: Vector128_1[float]) -> Vector128_1[float]: ...
        @staticmethod
        def Subtract(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
        # Skipped Abs due to it being static, abstract and generic.

        Abs : Abs_MethodGroup
        class Abs_MethodGroup:
            def __call__(self, value: Vector128_1[float]) -> Vector128_1[float]:...
            # Method Abs(value : Vector128`1) was skipped since it collides with above method

        # Skipped AbsoluteCompareGreaterThanOrEqualScalar due to it being static, abstract and generic.

        AbsoluteCompareGreaterThanOrEqualScalar : AbsoluteCompareGreaterThanOrEqualScalar_MethodGroup
        class AbsoluteCompareGreaterThanOrEqualScalar_MethodGroup:
            def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
            # Method AbsoluteCompareGreaterThanOrEqualScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

        # Skipped AbsoluteCompareGreaterThanScalar due to it being static, abstract and generic.

        AbsoluteCompareGreaterThanScalar : AbsoluteCompareGreaterThanScalar_MethodGroup
        class AbsoluteCompareGreaterThanScalar_MethodGroup:
            def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
            # Method AbsoluteCompareGreaterThanScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

        # Skipped AbsoluteCompareLessThanOrEqualScalar due to it being static, abstract and generic.

        AbsoluteCompareLessThanOrEqualScalar : AbsoluteCompareLessThanOrEqualScalar_MethodGroup
        class AbsoluteCompareLessThanOrEqualScalar_MethodGroup:
            def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
            # Method AbsoluteCompareLessThanOrEqualScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

        # Skipped AbsoluteCompareLessThanScalar due to it being static, abstract and generic.

        AbsoluteCompareLessThanScalar : AbsoluteCompareLessThanScalar_MethodGroup
        class AbsoluteCompareLessThanScalar_MethodGroup:
            def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
            # Method AbsoluteCompareLessThanScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

        # Skipped AbsoluteDifferenceScalar due to it being static, abstract and generic.

        AbsoluteDifferenceScalar : AbsoluteDifferenceScalar_MethodGroup
        class AbsoluteDifferenceScalar_MethodGroup:
            def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
            # Method AbsoluteDifferenceScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

        # Skipped AbsSaturateScalar due to it being static, abstract and generic.

        AbsSaturateScalar : AbsSaturateScalar_MethodGroup
        class AbsSaturateScalar_MethodGroup:
            def __call__(self, value: Vector64_1[int]) -> Vector64_1[int]:...
            # Method AbsSaturateScalar(value : Vector64`1) was skipped since it collides with above method
            # Method AbsSaturateScalar(value : Vector64`1) was skipped since it collides with above method
            # Method AbsSaturateScalar(value : Vector64`1) was skipped since it collides with above method

        # Skipped AddAcross due to it being static, abstract and generic.

        AddAcross : AddAcross_MethodGroup
        class AddAcross_MethodGroup:
            @typing.overload
            def __call__(self, value: Vector64_1[int]) -> Vector64_1[int]:...
            # Method AddAcross(value : Vector64`1) was skipped since it collides with above method
            # Method AddAcross(value : Vector64`1) was skipped since it collides with above method
            # Method AddAcross(value : Vector64`1) was skipped since it collides with above method
            @typing.overload
            def __call__(self, value: Vector128_1[int]) -> Vector64_1[int]:...
            # Method AddAcross(value : Vector128`1) was skipped since it collides with above method
            # Method AddAcross(value : Vector128`1) was skipped since it collides with above method
            # Method AddAcross(value : Vector128`1) was skipped since it collides with above method
            # Method AddAcross(value : Vector128`1) was skipped since it collides with above method
            # Method AddAcross(value : Vector128`1) was skipped since it collides with above method

        # Skipped AddAcrossWidening due to it being static, abstract and generic.

        AddAcrossWidening : AddAcrossWidening_MethodGroup
        class AddAcrossWidening_MethodGroup:
            @typing.overload
            def __call__(self, value: Vector64_1[int]) -> Vector64_1[int]:...
            # Method AddAcrossWidening(value : Vector64`1) was skipped since it collides with above method
            # Method AddAcrossWidening(value : Vector64`1) was skipped since it collides with above method
            # Method AddAcrossWidening(value : Vector64`1) was skipped since it collides with above method
            @typing.overload
            def __call__(self, value: Vector128_1[int]) -> Vector64_1[int]:...
            # Method AddAcrossWidening(value : Vector128`1) was skipped since it collides with above method
            # Method AddAcrossWidening(value : Vector128`1) was skipped since it collides with above method
            # Method AddAcrossWidening(value : Vector128`1) was skipped since it collides with above method
            # Method AddAcrossWidening(value : Vector128`1) was skipped since it collides with above method
            # Method AddAcrossWidening(value : Vector128`1) was skipped since it collides with above method

        # Skipped AddPairwise due to it being static, abstract and generic.

        AddPairwise : AddPairwise_MethodGroup
        class AddPairwise_MethodGroup:
            def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
            # Method AddPairwise(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method AddPairwise(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method AddPairwise(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method AddPairwise(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method AddPairwise(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method AddPairwise(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method AddPairwise(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method AddPairwise(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method AddPairwise(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

        # Skipped AddPairwiseScalar due to it being static, abstract and generic.

        AddPairwiseScalar : AddPairwiseScalar_MethodGroup
        class AddPairwiseScalar_MethodGroup:
            @typing.overload
            def __call__(self, value: Vector64_1[float]) -> Vector64_1[float]:...
            @typing.overload
            def __call__(self, value: Vector128_1[float]) -> Vector64_1[float]:...
            # Method AddPairwiseScalar(value : Vector128`1) was skipped since it collides with above method
            # Method AddPairwiseScalar(value : Vector128`1) was skipped since it collides with above method

        # Skipped AddSaturate due to it being static, abstract and generic.

        AddSaturate : AddSaturate_MethodGroup
        class AddSaturate_MethodGroup:
            @typing.overload
            def __call__(self, left: Vector64_1[int], right: Vector64_1[int]) -> Vector64_1[int]:...
            # Method AddSaturate(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method AddSaturate(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method AddSaturate(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method AddSaturate(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method AddSaturate(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            @typing.overload
            def __call__(self, left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
            # Method AddSaturate(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method AddSaturate(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method AddSaturate(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method AddSaturate(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method AddSaturate(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method AddSaturate(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method AddSaturate(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

        # Skipped AddSaturateScalar due to it being static, abstract and generic.

        AddSaturateScalar : AddSaturateScalar_MethodGroup
        class AddSaturateScalar_MethodGroup:
            def __call__(self, left: Vector64_1[int], right: Vector64_1[int]) -> Vector64_1[int]:...
            # Method AddSaturateScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method AddSaturateScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method AddSaturateScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method AddSaturateScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method AddSaturateScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method AddSaturateScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method AddSaturateScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method AddSaturateScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method AddSaturateScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method AddSaturateScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method AddSaturateScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method AddSaturateScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method AddSaturateScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

        # Skipped CompareEqual due to it being static, abstract and generic.

        CompareEqual : CompareEqual_MethodGroup
        class CompareEqual_MethodGroup:
            def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
            # Method CompareEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method CompareEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

        # Skipped CompareEqualScalar due to it being static, abstract and generic.

        CompareEqualScalar : CompareEqualScalar_MethodGroup
        class CompareEqualScalar_MethodGroup:
            def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
            # Method CompareEqualScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method CompareEqualScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method CompareEqualScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

        # Skipped CompareGreaterThan due to it being static, abstract and generic.

        CompareGreaterThan : CompareGreaterThan_MethodGroup
        class CompareGreaterThan_MethodGroup:
            def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
            # Method CompareGreaterThan(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method CompareGreaterThan(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

        # Skipped CompareGreaterThanOrEqual due to it being static, abstract and generic.

        CompareGreaterThanOrEqual : CompareGreaterThanOrEqual_MethodGroup
        class CompareGreaterThanOrEqual_MethodGroup:
            def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
            # Method CompareGreaterThanOrEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method CompareGreaterThanOrEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

        # Skipped CompareGreaterThanOrEqualScalar due to it being static, abstract and generic.

        CompareGreaterThanOrEqualScalar : CompareGreaterThanOrEqualScalar_MethodGroup
        class CompareGreaterThanOrEqualScalar_MethodGroup:
            def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
            # Method CompareGreaterThanOrEqualScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method CompareGreaterThanOrEqualScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method CompareGreaterThanOrEqualScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

        # Skipped CompareGreaterThanScalar due to it being static, abstract and generic.

        CompareGreaterThanScalar : CompareGreaterThanScalar_MethodGroup
        class CompareGreaterThanScalar_MethodGroup:
            def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
            # Method CompareGreaterThanScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method CompareGreaterThanScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method CompareGreaterThanScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

        # Skipped CompareLessThan due to it being static, abstract and generic.

        CompareLessThan : CompareLessThan_MethodGroup
        class CompareLessThan_MethodGroup:
            def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
            # Method CompareLessThan(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method CompareLessThan(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

        # Skipped CompareLessThanOrEqual due to it being static, abstract and generic.

        CompareLessThanOrEqual : CompareLessThanOrEqual_MethodGroup
        class CompareLessThanOrEqual_MethodGroup:
            def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
            # Method CompareLessThanOrEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method CompareLessThanOrEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

        # Skipped CompareLessThanOrEqualScalar due to it being static, abstract and generic.

        CompareLessThanOrEqualScalar : CompareLessThanOrEqualScalar_MethodGroup
        class CompareLessThanOrEqualScalar_MethodGroup:
            def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
            # Method CompareLessThanOrEqualScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method CompareLessThanOrEqualScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method CompareLessThanOrEqualScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

        # Skipped CompareLessThanScalar due to it being static, abstract and generic.

        CompareLessThanScalar : CompareLessThanScalar_MethodGroup
        class CompareLessThanScalar_MethodGroup:
            def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
            # Method CompareLessThanScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method CompareLessThanScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method CompareLessThanScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

        # Skipped CompareTest due to it being static, abstract and generic.

        CompareTest : CompareTest_MethodGroup
        class CompareTest_MethodGroup:
            def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
            # Method CompareTest(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method CompareTest(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

        # Skipped CompareTestScalar due to it being static, abstract and generic.

        CompareTestScalar : CompareTestScalar_MethodGroup
        class CompareTestScalar_MethodGroup:
            def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
            # Method CompareTestScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method CompareTestScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

        # Skipped ConvertToDouble due to it being static, abstract and generic.

        ConvertToDouble : ConvertToDouble_MethodGroup
        class ConvertToDouble_MethodGroup:
            @typing.overload
            def __call__(self, value: Vector64_1[float]) -> Vector128_1[float]:...
            @typing.overload
            def __call__(self, value: Vector128_1[int]) -> Vector128_1[float]:...
            # Method ConvertToDouble(value : Vector128`1) was skipped since it collides with above method

        # Skipped ConvertToDoubleScalar due to it being static, abstract and generic.

        ConvertToDoubleScalar : ConvertToDoubleScalar_MethodGroup
        class ConvertToDoubleScalar_MethodGroup:
            def __call__(self, value: Vector64_1[int]) -> Vector64_1[float]:...
            # Method ConvertToDoubleScalar(value : Vector64`1) was skipped since it collides with above method

        # Skipped Divide due to it being static, abstract and generic.

        Divide : Divide_MethodGroup
        class Divide_MethodGroup:
            @typing.overload
            def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
            @typing.overload
            def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
            # Method Divide(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

        # Skipped DuplicateSelectedScalarToVector128 due to it being static, abstract and generic.

        DuplicateSelectedScalarToVector128 : DuplicateSelectedScalarToVector128_MethodGroup
        class DuplicateSelectedScalarToVector128_MethodGroup:
            def __call__(self, value: Vector128_1[float], index: int) -> Vector128_1[float]:...
            # Method DuplicateSelectedScalarToVector128(value : Vector128`1, index : Byte) was skipped since it collides with above method
            # Method DuplicateSelectedScalarToVector128(value : Vector128`1, index : Byte) was skipped since it collides with above method

        # Skipped DuplicateToVector128 due to it being static, abstract and generic.

        DuplicateToVector128 : DuplicateToVector128_MethodGroup
        class DuplicateToVector128_MethodGroup:
            def __call__(self, value: float) -> Vector128_1[float]:...
            # Method DuplicateToVector128(value : Int64) was skipped since it collides with above method
            # Method DuplicateToVector128(value : UInt64) was skipped since it collides with above method

        # Skipped ExtractNarrowingSaturateScalar due to it being static, abstract and generic.

        ExtractNarrowingSaturateScalar : ExtractNarrowingSaturateScalar_MethodGroup
        class ExtractNarrowingSaturateScalar_MethodGroup:
            def __call__(self, value: Vector64_1[int]) -> Vector64_1[int]:...
            # Method ExtractNarrowingSaturateScalar(value : Vector64`1) was skipped since it collides with above method
            # Method ExtractNarrowingSaturateScalar(value : Vector64`1) was skipped since it collides with above method
            # Method ExtractNarrowingSaturateScalar(value : Vector64`1) was skipped since it collides with above method
            # Method ExtractNarrowingSaturateScalar(value : Vector64`1) was skipped since it collides with above method
            # Method ExtractNarrowingSaturateScalar(value : Vector64`1) was skipped since it collides with above method

        # Skipped ExtractNarrowingSaturateUnsignedScalar due to it being static, abstract and generic.

        ExtractNarrowingSaturateUnsignedScalar : ExtractNarrowingSaturateUnsignedScalar_MethodGroup
        class ExtractNarrowingSaturateUnsignedScalar_MethodGroup:
            def __call__(self, value: Vector64_1[int]) -> Vector64_1[int]:...
            # Method ExtractNarrowingSaturateUnsignedScalar(value : Vector64`1) was skipped since it collides with above method
            # Method ExtractNarrowingSaturateUnsignedScalar(value : Vector64`1) was skipped since it collides with above method

        # Skipped FusedMultiplyAddByScalar due to it being static, abstract and generic.

        FusedMultiplyAddByScalar : FusedMultiplyAddByScalar_MethodGroup
        class FusedMultiplyAddByScalar_MethodGroup:
            @typing.overload
            def __call__(self, addend: Vector64_1[float], left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
            @typing.overload
            def __call__(self, addend: Vector128_1[float], left: Vector128_1[float], right: Vector64_1[float]) -> Vector128_1[float]:...
            # Method FusedMultiplyAddByScalar(addend : Vector128`1, left : Vector128`1, right : Vector64`1) was skipped since it collides with above method

        # Skipped FusedMultiplyAddBySelectedScalar due to it being static, abstract and generic.

        FusedMultiplyAddBySelectedScalar : FusedMultiplyAddBySelectedScalar_MethodGroup
        class FusedMultiplyAddBySelectedScalar_MethodGroup:
            @typing.overload
            def __call__(self, addend: Vector64_1[float], left: Vector64_1[float], right: Vector64_1[float], rightIndex: int) -> Vector64_1[float]:...
            @typing.overload
            def __call__(self, addend: Vector64_1[float], left: Vector64_1[float], right: Vector128_1[float], rightIndex: int) -> Vector64_1[float]:...
            @typing.overload
            def __call__(self, addend: Vector128_1[float], left: Vector128_1[float], right: Vector128_1[float], rightIndex: int) -> Vector128_1[float]:...
            @typing.overload
            def __call__(self, addend: Vector128_1[float], left: Vector128_1[float], right: Vector64_1[float], rightIndex: int) -> Vector128_1[float]:...
            # Method FusedMultiplyAddBySelectedScalar(addend : Vector128`1, left : Vector128`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method

        # Skipped FusedMultiplyAddScalarBySelectedScalar due to it being static, abstract and generic.

        FusedMultiplyAddScalarBySelectedScalar : FusedMultiplyAddScalarBySelectedScalar_MethodGroup
        class FusedMultiplyAddScalarBySelectedScalar_MethodGroup:
            @typing.overload
            def __call__(self, addend: Vector64_1[float], left: Vector64_1[float], right: Vector128_1[float], rightIndex: int) -> Vector64_1[float]:...
            @typing.overload
            def __call__(self, addend: Vector64_1[float], left: Vector64_1[float], right: Vector64_1[float], rightIndex: int) -> Vector64_1[float]:...
            # Method FusedMultiplyAddScalarBySelectedScalar(addend : Vector64`1, left : Vector64`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method

        # Skipped FusedMultiplySubtractByScalar due to it being static, abstract and generic.

        FusedMultiplySubtractByScalar : FusedMultiplySubtractByScalar_MethodGroup
        class FusedMultiplySubtractByScalar_MethodGroup:
            @typing.overload
            def __call__(self, minuend: Vector64_1[float], left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
            @typing.overload
            def __call__(self, minuend: Vector128_1[float], left: Vector128_1[float], right: Vector64_1[float]) -> Vector128_1[float]:...
            # Method FusedMultiplySubtractByScalar(minuend : Vector128`1, left : Vector128`1, right : Vector64`1) was skipped since it collides with above method

        # Skipped FusedMultiplySubtractBySelectedScalar due to it being static, abstract and generic.

        FusedMultiplySubtractBySelectedScalar : FusedMultiplySubtractBySelectedScalar_MethodGroup
        class FusedMultiplySubtractBySelectedScalar_MethodGroup:
            @typing.overload
            def __call__(self, minuend: Vector64_1[float], left: Vector64_1[float], right: Vector64_1[float], rightIndex: int) -> Vector64_1[float]:...
            @typing.overload
            def __call__(self, minuend: Vector64_1[float], left: Vector64_1[float], right: Vector128_1[float], rightIndex: int) -> Vector64_1[float]:...
            @typing.overload
            def __call__(self, minuend: Vector128_1[float], left: Vector128_1[float], right: Vector128_1[float], rightIndex: int) -> Vector128_1[float]:...
            @typing.overload
            def __call__(self, minuend: Vector128_1[float], left: Vector128_1[float], right: Vector64_1[float], rightIndex: int) -> Vector128_1[float]:...
            # Method FusedMultiplySubtractBySelectedScalar(minuend : Vector128`1, left : Vector128`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method

        # Skipped FusedMultiplySubtractScalarBySelectedScalar due to it being static, abstract and generic.

        FusedMultiplySubtractScalarBySelectedScalar : FusedMultiplySubtractScalarBySelectedScalar_MethodGroup
        class FusedMultiplySubtractScalarBySelectedScalar_MethodGroup:
            @typing.overload
            def __call__(self, minuend: Vector64_1[float], left: Vector64_1[float], right: Vector128_1[float], rightIndex: int) -> Vector64_1[float]:...
            @typing.overload
            def __call__(self, minuend: Vector64_1[float], left: Vector64_1[float], right: Vector64_1[float], rightIndex: int) -> Vector64_1[float]:...
            # Method FusedMultiplySubtractScalarBySelectedScalar(minuend : Vector64`1, left : Vector64`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method

        # Skipped InsertSelectedScalar due to it being static, abstract and generic.

        InsertSelectedScalar : InsertSelectedScalar_MethodGroup
        class InsertSelectedScalar_MethodGroup:
            @typing.overload
            def __call__(self, result: Vector64_1[float], resultIndex: int, value: Vector64_1[float], valueIndex: int) -> Vector64_1[float]:...
            @typing.overload
            def __call__(self, result: Vector64_1[float], resultIndex: int, value: Vector128_1[float], valueIndex: int) -> Vector64_1[float]:...
            @typing.overload
            def __call__(self, result: Vector128_1[float], resultIndex: int, value: Vector128_1[float], valueIndex: int) -> Vector128_1[float]:...
            @typing.overload
            def __call__(self, result: Vector128_1[float], resultIndex: int, value: Vector64_1[float], valueIndex: int) -> Vector128_1[float]:...
            # Method InsertSelectedScalar(result : Vector128`1, resultIndex : Byte, value : Vector128`1, valueIndex : Byte) was skipped since it collides with above method
            # Method InsertSelectedScalar(result : Vector64`1, resultIndex : Byte, value : Vector64`1, valueIndex : Byte) was skipped since it collides with above method
            # Method InsertSelectedScalar(result : Vector64`1, resultIndex : Byte, value : Vector128`1, valueIndex : Byte) was skipped since it collides with above method
            # Method InsertSelectedScalar(result : Vector64`1, resultIndex : Byte, value : Vector64`1, valueIndex : Byte) was skipped since it collides with above method
            # Method InsertSelectedScalar(result : Vector64`1, resultIndex : Byte, value : Vector128`1, valueIndex : Byte) was skipped since it collides with above method
            # Method InsertSelectedScalar(result : Vector64`1, resultIndex : Byte, value : Vector64`1, valueIndex : Byte) was skipped since it collides with above method
            # Method InsertSelectedScalar(result : Vector64`1, resultIndex : Byte, value : Vector128`1, valueIndex : Byte) was skipped since it collides with above method
            # Method InsertSelectedScalar(result : Vector64`1, resultIndex : Byte, value : Vector64`1, valueIndex : Byte) was skipped since it collides with above method
            # Method InsertSelectedScalar(result : Vector64`1, resultIndex : Byte, value : Vector128`1, valueIndex : Byte) was skipped since it collides with above method
            # Method InsertSelectedScalar(result : Vector64`1, resultIndex : Byte, value : Vector64`1, valueIndex : Byte) was skipped since it collides with above method
            # Method InsertSelectedScalar(result : Vector64`1, resultIndex : Byte, value : Vector128`1, valueIndex : Byte) was skipped since it collides with above method
            # Method InsertSelectedScalar(result : Vector64`1, resultIndex : Byte, value : Vector64`1, valueIndex : Byte) was skipped since it collides with above method
            # Method InsertSelectedScalar(result : Vector64`1, resultIndex : Byte, value : Vector128`1, valueIndex : Byte) was skipped since it collides with above method
            # Method InsertSelectedScalar(result : Vector128`1, resultIndex : Byte, value : Vector64`1, valueIndex : Byte) was skipped since it collides with above method
            # Method InsertSelectedScalar(result : Vector128`1, resultIndex : Byte, value : Vector128`1, valueIndex : Byte) was skipped since it collides with above method
            # Method InsertSelectedScalar(result : Vector128`1, resultIndex : Byte, value : Vector64`1, valueIndex : Byte) was skipped since it collides with above method
            # Method InsertSelectedScalar(result : Vector128`1, resultIndex : Byte, value : Vector128`1, valueIndex : Byte) was skipped since it collides with above method
            # Method InsertSelectedScalar(result : Vector128`1, resultIndex : Byte, value : Vector64`1, valueIndex : Byte) was skipped since it collides with above method
            # Method InsertSelectedScalar(result : Vector128`1, resultIndex : Byte, value : Vector128`1, valueIndex : Byte) was skipped since it collides with above method
            # Method InsertSelectedScalar(result : Vector128`1, resultIndex : Byte, value : Vector128`1, valueIndex : Byte) was skipped since it collides with above method
            # Method InsertSelectedScalar(result : Vector128`1, resultIndex : Byte, value : Vector64`1, valueIndex : Byte) was skipped since it collides with above method
            # Method InsertSelectedScalar(result : Vector128`1, resultIndex : Byte, value : Vector128`1, valueIndex : Byte) was skipped since it collides with above method
            # Method InsertSelectedScalar(result : Vector128`1, resultIndex : Byte, value : Vector64`1, valueIndex : Byte) was skipped since it collides with above method
            # Method InsertSelectedScalar(result : Vector128`1, resultIndex : Byte, value : Vector128`1, valueIndex : Byte) was skipped since it collides with above method
            # Method InsertSelectedScalar(result : Vector128`1, resultIndex : Byte, value : Vector64`1, valueIndex : Byte) was skipped since it collides with above method
            # Method InsertSelectedScalar(result : Vector128`1, resultIndex : Byte, value : Vector128`1, valueIndex : Byte) was skipped since it collides with above method
            # Method InsertSelectedScalar(result : Vector128`1, resultIndex : Byte, value : Vector128`1, valueIndex : Byte) was skipped since it collides with above method

        # Skipped LoadAndReplicateToVector128 due to it being static, abstract and generic.

        LoadAndReplicateToVector128 : LoadAndReplicateToVector128_MethodGroup
        class LoadAndReplicateToVector128_MethodGroup:
            def __call__(self, address: clr.Reference[float]) -> Vector128_1[float]:...
            # Method LoadAndReplicateToVector128(address : Int64*) was skipped since it collides with above method
            # Method LoadAndReplicateToVector128(address : UInt64*) was skipped since it collides with above method

        # Skipped MaxAcross due to it being static, abstract and generic.

        MaxAcross : MaxAcross_MethodGroup
        class MaxAcross_MethodGroup:
            @typing.overload
            def __call__(self, value: Vector128_1[float]) -> Vector64_1[float]:...
            @typing.overload
            def __call__(self, value: Vector64_1[int]) -> Vector64_1[int]:...
            # Method MaxAcross(value : Vector64`1) was skipped since it collides with above method
            # Method MaxAcross(value : Vector64`1) was skipped since it collides with above method
            # Method MaxAcross(value : Vector64`1) was skipped since it collides with above method
            # Method MaxAcross(value : Vector128`1) was skipped since it collides with above method
            # Method MaxAcross(value : Vector128`1) was skipped since it collides with above method
            # Method MaxAcross(value : Vector128`1) was skipped since it collides with above method
            # Method MaxAcross(value : Vector128`1) was skipped since it collides with above method
            # Method MaxAcross(value : Vector128`1) was skipped since it collides with above method
            # Method MaxAcross(value : Vector128`1) was skipped since it collides with above method

        # Skipped MaxNumberPairwise due to it being static, abstract and generic.

        MaxNumberPairwise : MaxNumberPairwise_MethodGroup
        class MaxNumberPairwise_MethodGroup:
            @typing.overload
            def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
            @typing.overload
            def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
            # Method MaxNumberPairwise(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

        # Skipped MaxNumberPairwiseScalar due to it being static, abstract and generic.

        MaxNumberPairwiseScalar : MaxNumberPairwiseScalar_MethodGroup
        class MaxNumberPairwiseScalar_MethodGroup:
            @typing.overload
            def __call__(self, value: Vector64_1[float]) -> Vector64_1[float]:...
            @typing.overload
            def __call__(self, value: Vector128_1[float]) -> Vector64_1[float]:...

        # Skipped MaxPairwise due to it being static, abstract and generic.

        MaxPairwise : MaxPairwise_MethodGroup
        class MaxPairwise_MethodGroup:
            def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
            # Method MaxPairwise(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method MaxPairwise(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method MaxPairwise(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method MaxPairwise(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method MaxPairwise(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method MaxPairwise(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method MaxPairwise(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

        # Skipped MaxPairwiseScalar due to it being static, abstract and generic.

        MaxPairwiseScalar : MaxPairwiseScalar_MethodGroup
        class MaxPairwiseScalar_MethodGroup:
            @typing.overload
            def __call__(self, value: Vector64_1[float]) -> Vector64_1[float]:...
            @typing.overload
            def __call__(self, value: Vector128_1[float]) -> Vector64_1[float]:...

        # Skipped MaxScalar due to it being static, abstract and generic.

        MaxScalar : MaxScalar_MethodGroup
        class MaxScalar_MethodGroup:
            def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
            # Method MaxScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

        # Skipped MinAcross due to it being static, abstract and generic.

        MinAcross : MinAcross_MethodGroup
        class MinAcross_MethodGroup:
            @typing.overload
            def __call__(self, value: Vector128_1[float]) -> Vector64_1[float]:...
            @typing.overload
            def __call__(self, value: Vector64_1[int]) -> Vector64_1[int]:...
            # Method MinAcross(value : Vector64`1) was skipped since it collides with above method
            # Method MinAcross(value : Vector64`1) was skipped since it collides with above method
            # Method MinAcross(value : Vector64`1) was skipped since it collides with above method
            # Method MinAcross(value : Vector128`1) was skipped since it collides with above method
            # Method MinAcross(value : Vector128`1) was skipped since it collides with above method
            # Method MinAcross(value : Vector128`1) was skipped since it collides with above method
            # Method MinAcross(value : Vector128`1) was skipped since it collides with above method
            # Method MinAcross(value : Vector128`1) was skipped since it collides with above method
            # Method MinAcross(value : Vector128`1) was skipped since it collides with above method

        # Skipped MinNumberPairwise due to it being static, abstract and generic.

        MinNumberPairwise : MinNumberPairwise_MethodGroup
        class MinNumberPairwise_MethodGroup:
            @typing.overload
            def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
            @typing.overload
            def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
            # Method MinNumberPairwise(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

        # Skipped MinNumberPairwiseScalar due to it being static, abstract and generic.

        MinNumberPairwiseScalar : MinNumberPairwiseScalar_MethodGroup
        class MinNumberPairwiseScalar_MethodGroup:
            @typing.overload
            def __call__(self, value: Vector64_1[float]) -> Vector64_1[float]:...
            @typing.overload
            def __call__(self, value: Vector128_1[float]) -> Vector64_1[float]:...

        # Skipped MinPairwise due to it being static, abstract and generic.

        MinPairwise : MinPairwise_MethodGroup
        class MinPairwise_MethodGroup:
            def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
            # Method MinPairwise(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method MinPairwise(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method MinPairwise(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method MinPairwise(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method MinPairwise(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method MinPairwise(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method MinPairwise(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

        # Skipped MinPairwiseScalar due to it being static, abstract and generic.

        MinPairwiseScalar : MinPairwiseScalar_MethodGroup
        class MinPairwiseScalar_MethodGroup:
            @typing.overload
            def __call__(self, value: Vector64_1[float]) -> Vector64_1[float]:...
            @typing.overload
            def __call__(self, value: Vector128_1[float]) -> Vector64_1[float]:...

        # Skipped MinScalar due to it being static, abstract and generic.

        MinScalar : MinScalar_MethodGroup
        class MinScalar_MethodGroup:
            def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
            # Method MinScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

        # Skipped MultiplyDoublingSaturateHighScalar due to it being static, abstract and generic.

        MultiplyDoublingSaturateHighScalar : MultiplyDoublingSaturateHighScalar_MethodGroup
        class MultiplyDoublingSaturateHighScalar_MethodGroup:
            def __call__(self, left: Vector64_1[int], right: Vector64_1[int]) -> Vector64_1[int]:...
            # Method MultiplyDoublingSaturateHighScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

        # Skipped MultiplyDoublingScalarBySelectedScalarSaturateHigh due to it being static, abstract and generic.

        MultiplyDoublingScalarBySelectedScalarSaturateHigh : MultiplyDoublingScalarBySelectedScalarSaturateHigh_MethodGroup
        class MultiplyDoublingScalarBySelectedScalarSaturateHigh_MethodGroup:
            @typing.overload
            def __call__(self, left: Vector64_1[int], right: Vector64_1[int], rightIndex: int) -> Vector64_1[int]:...
            @typing.overload
            def __call__(self, left: Vector64_1[int], right: Vector128_1[int], rightIndex: int) -> Vector64_1[int]:...
            # Method MultiplyDoublingScalarBySelectedScalarSaturateHigh(left : Vector64`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
            # Method MultiplyDoublingScalarBySelectedScalarSaturateHigh(left : Vector64`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method

        # Skipped MultiplyDoublingWideningAndAddSaturateScalar due to it being static, abstract and generic.

        MultiplyDoublingWideningAndAddSaturateScalar : MultiplyDoublingWideningAndAddSaturateScalar_MethodGroup
        class MultiplyDoublingWideningAndAddSaturateScalar_MethodGroup:
            def __call__(self, addend: Vector64_1[int], left: Vector64_1[int], right: Vector64_1[int]) -> Vector64_1[int]:...
            # Method MultiplyDoublingWideningAndAddSaturateScalar(addend : Vector64`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

        # Skipped MultiplyDoublingWideningAndSubtractSaturateScalar due to it being static, abstract and generic.

        MultiplyDoublingWideningAndSubtractSaturateScalar : MultiplyDoublingWideningAndSubtractSaturateScalar_MethodGroup
        class MultiplyDoublingWideningAndSubtractSaturateScalar_MethodGroup:
            def __call__(self, minuend: Vector64_1[int], left: Vector64_1[int], right: Vector64_1[int]) -> Vector64_1[int]:...
            # Method MultiplyDoublingWideningAndSubtractSaturateScalar(minuend : Vector64`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

        # Skipped MultiplyDoublingWideningSaturateScalar due to it being static, abstract and generic.

        MultiplyDoublingWideningSaturateScalar : MultiplyDoublingWideningSaturateScalar_MethodGroup
        class MultiplyDoublingWideningSaturateScalar_MethodGroup:
            def __call__(self, left: Vector64_1[int], right: Vector64_1[int]) -> Vector64_1[int]:...
            # Method MultiplyDoublingWideningSaturateScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

        # Skipped MultiplyDoublingWideningSaturateScalarBySelectedScalar due to it being static, abstract and generic.

        MultiplyDoublingWideningSaturateScalarBySelectedScalar : MultiplyDoublingWideningSaturateScalarBySelectedScalar_MethodGroup
        class MultiplyDoublingWideningSaturateScalarBySelectedScalar_MethodGroup:
            @typing.overload
            def __call__(self, left: Vector64_1[int], right: Vector64_1[int], rightIndex: int) -> Vector64_1[int]:...
            @typing.overload
            def __call__(self, left: Vector64_1[int], right: Vector128_1[int], rightIndex: int) -> Vector64_1[int]:...
            # Method MultiplyDoublingWideningSaturateScalarBySelectedScalar(left : Vector64`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
            # Method MultiplyDoublingWideningSaturateScalarBySelectedScalar(left : Vector64`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method

        # Skipped MultiplyDoublingWideningScalarBySelectedScalarAndAddSaturate due to it being static, abstract and generic.

        MultiplyDoublingWideningScalarBySelectedScalarAndAddSaturate : MultiplyDoublingWideningScalarBySelectedScalarAndAddSaturate_MethodGroup
        class MultiplyDoublingWideningScalarBySelectedScalarAndAddSaturate_MethodGroup:
            @typing.overload
            def __call__(self, addend: Vector64_1[int], left: Vector64_1[int], right: Vector64_1[int], rightIndex: int) -> Vector64_1[int]:...
            @typing.overload
            def __call__(self, addend: Vector64_1[int], left: Vector64_1[int], right: Vector128_1[int], rightIndex: int) -> Vector64_1[int]:...
            # Method MultiplyDoublingWideningScalarBySelectedScalarAndAddSaturate(addend : Vector64`1, left : Vector64`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
            # Method MultiplyDoublingWideningScalarBySelectedScalarAndAddSaturate(addend : Vector64`1, left : Vector64`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method

        # Skipped MultiplyDoublingWideningScalarBySelectedScalarAndSubtractSaturate due to it being static, abstract and generic.

        MultiplyDoublingWideningScalarBySelectedScalarAndSubtractSaturate : MultiplyDoublingWideningScalarBySelectedScalarAndSubtractSaturate_MethodGroup
        class MultiplyDoublingWideningScalarBySelectedScalarAndSubtractSaturate_MethodGroup:
            @typing.overload
            def __call__(self, minuend: Vector64_1[int], left: Vector64_1[int], right: Vector64_1[int], rightIndex: int) -> Vector64_1[int]:...
            @typing.overload
            def __call__(self, minuend: Vector64_1[int], left: Vector64_1[int], right: Vector128_1[int], rightIndex: int) -> Vector64_1[int]:...
            # Method MultiplyDoublingWideningScalarBySelectedScalarAndSubtractSaturate(minuend : Vector64`1, left : Vector64`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
            # Method MultiplyDoublingWideningScalarBySelectedScalarAndSubtractSaturate(minuend : Vector64`1, left : Vector64`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method

        # Skipped MultiplyExtended due to it being static, abstract and generic.

        MultiplyExtended : MultiplyExtended_MethodGroup
        class MultiplyExtended_MethodGroup:
            @typing.overload
            def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
            @typing.overload
            def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
            # Method MultiplyExtended(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

        # Skipped MultiplyExtendedBySelectedScalar due to it being static, abstract and generic.

        MultiplyExtendedBySelectedScalar : MultiplyExtendedBySelectedScalar_MethodGroup
        class MultiplyExtendedBySelectedScalar_MethodGroup:
            @typing.overload
            def __call__(self, left: Vector64_1[float], right: Vector64_1[float], rightIndex: int) -> Vector64_1[float]:...
            @typing.overload
            def __call__(self, left: Vector64_1[float], right: Vector128_1[float], rightIndex: int) -> Vector64_1[float]:...
            @typing.overload
            def __call__(self, left: Vector128_1[float], right: Vector128_1[float], rightIndex: int) -> Vector128_1[float]:...
            @typing.overload
            def __call__(self, left: Vector128_1[float], right: Vector64_1[float], rightIndex: int) -> Vector128_1[float]:...
            # Method MultiplyExtendedBySelectedScalar(left : Vector128`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method

        # Skipped MultiplyExtendedScalar due to it being static, abstract and generic.

        MultiplyExtendedScalar : MultiplyExtendedScalar_MethodGroup
        class MultiplyExtendedScalar_MethodGroup:
            def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
            # Method MultiplyExtendedScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

        # Skipped MultiplyExtendedScalarBySelectedScalar due to it being static, abstract and generic.

        MultiplyExtendedScalarBySelectedScalar : MultiplyExtendedScalarBySelectedScalar_MethodGroup
        class MultiplyExtendedScalarBySelectedScalar_MethodGroup:
            @typing.overload
            def __call__(self, left: Vector64_1[float], right: Vector128_1[float], rightIndex: int) -> Vector64_1[float]:...
            @typing.overload
            def __call__(self, left: Vector64_1[float], right: Vector64_1[float], rightIndex: int) -> Vector64_1[float]:...
            # Method MultiplyExtendedScalarBySelectedScalar(left : Vector64`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method

        # Skipped MultiplyRoundedDoublingSaturateHighScalar due to it being static, abstract and generic.

        MultiplyRoundedDoublingSaturateHighScalar : MultiplyRoundedDoublingSaturateHighScalar_MethodGroup
        class MultiplyRoundedDoublingSaturateHighScalar_MethodGroup:
            def __call__(self, left: Vector64_1[int], right: Vector64_1[int]) -> Vector64_1[int]:...
            # Method MultiplyRoundedDoublingSaturateHighScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

        # Skipped MultiplyRoundedDoublingScalarBySelectedScalarSaturateHigh due to it being static, abstract and generic.

        MultiplyRoundedDoublingScalarBySelectedScalarSaturateHigh : MultiplyRoundedDoublingScalarBySelectedScalarSaturateHigh_MethodGroup
        class MultiplyRoundedDoublingScalarBySelectedScalarSaturateHigh_MethodGroup:
            @typing.overload
            def __call__(self, left: Vector64_1[int], right: Vector64_1[int], rightIndex: int) -> Vector64_1[int]:...
            @typing.overload
            def __call__(self, left: Vector64_1[int], right: Vector128_1[int], rightIndex: int) -> Vector64_1[int]:...
            # Method MultiplyRoundedDoublingScalarBySelectedScalarSaturateHigh(left : Vector64`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
            # Method MultiplyRoundedDoublingScalarBySelectedScalarSaturateHigh(left : Vector64`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method

        # Skipped Negate due to it being static, abstract and generic.

        Negate : Negate_MethodGroup
        class Negate_MethodGroup:
            def __call__(self, value: Vector128_1[float]) -> Vector128_1[float]:...
            # Method Negate(value : Vector128`1) was skipped since it collides with above method

        # Skipped NegateSaturateScalar due to it being static, abstract and generic.

        NegateSaturateScalar : NegateSaturateScalar_MethodGroup
        class NegateSaturateScalar_MethodGroup:
            def __call__(self, value: Vector64_1[int]) -> Vector64_1[int]:...
            # Method NegateSaturateScalar(value : Vector64`1) was skipped since it collides with above method
            # Method NegateSaturateScalar(value : Vector64`1) was skipped since it collides with above method
            # Method NegateSaturateScalar(value : Vector64`1) was skipped since it collides with above method

        # Skipped ReciprocalEstimateScalar due to it being static, abstract and generic.

        ReciprocalEstimateScalar : ReciprocalEstimateScalar_MethodGroup
        class ReciprocalEstimateScalar_MethodGroup:
            def __call__(self, value: Vector64_1[float]) -> Vector64_1[float]:...
            # Method ReciprocalEstimateScalar(value : Vector64`1) was skipped since it collides with above method

        # Skipped ReciprocalExponentScalar due to it being static, abstract and generic.

        ReciprocalExponentScalar : ReciprocalExponentScalar_MethodGroup
        class ReciprocalExponentScalar_MethodGroup:
            def __call__(self, value: Vector64_1[float]) -> Vector64_1[float]:...
            # Method ReciprocalExponentScalar(value : Vector64`1) was skipped since it collides with above method

        # Skipped ReciprocalSquareRootEstimateScalar due to it being static, abstract and generic.

        ReciprocalSquareRootEstimateScalar : ReciprocalSquareRootEstimateScalar_MethodGroup
        class ReciprocalSquareRootEstimateScalar_MethodGroup:
            def __call__(self, value: Vector64_1[float]) -> Vector64_1[float]:...
            # Method ReciprocalSquareRootEstimateScalar(value : Vector64`1) was skipped since it collides with above method

        # Skipped ReciprocalSquareRootStepScalar due to it being static, abstract and generic.

        ReciprocalSquareRootStepScalar : ReciprocalSquareRootStepScalar_MethodGroup
        class ReciprocalSquareRootStepScalar_MethodGroup:
            def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
            # Method ReciprocalSquareRootStepScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

        # Skipped ReciprocalStepScalar due to it being static, abstract and generic.

        ReciprocalStepScalar : ReciprocalStepScalar_MethodGroup
        class ReciprocalStepScalar_MethodGroup:
            def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
            # Method ReciprocalStepScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

        # Skipped ReverseElementBits due to it being static, abstract and generic.

        ReverseElementBits : ReverseElementBits_MethodGroup
        class ReverseElementBits_MethodGroup:
            @typing.overload
            def __call__(self, value: Vector64_1[int]) -> Vector64_1[int]:...
            # Method ReverseElementBits(value : Vector64`1) was skipped since it collides with above method
            @typing.overload
            def __call__(self, value: Vector128_1[int]) -> Vector128_1[int]:...
            # Method ReverseElementBits(value : Vector128`1) was skipped since it collides with above method

        # Skipped ShiftArithmeticRoundedSaturateScalar due to it being static, abstract and generic.

        ShiftArithmeticRoundedSaturateScalar : ShiftArithmeticRoundedSaturateScalar_MethodGroup
        class ShiftArithmeticRoundedSaturateScalar_MethodGroup:
            def __call__(self, value: Vector64_1[int], count: Vector64_1[int]) -> Vector64_1[int]:...
            # Method ShiftArithmeticRoundedSaturateScalar(value : Vector64`1, count : Vector64`1) was skipped since it collides with above method
            # Method ShiftArithmeticRoundedSaturateScalar(value : Vector64`1, count : Vector64`1) was skipped since it collides with above method

        # Skipped ShiftArithmeticSaturateScalar due to it being static, abstract and generic.

        ShiftArithmeticSaturateScalar : ShiftArithmeticSaturateScalar_MethodGroup
        class ShiftArithmeticSaturateScalar_MethodGroup:
            def __call__(self, value: Vector64_1[int], count: Vector64_1[int]) -> Vector64_1[int]:...
            # Method ShiftArithmeticSaturateScalar(value : Vector64`1, count : Vector64`1) was skipped since it collides with above method
            # Method ShiftArithmeticSaturateScalar(value : Vector64`1, count : Vector64`1) was skipped since it collides with above method

        # Skipped ShiftLeftLogicalSaturateScalar due to it being static, abstract and generic.

        ShiftLeftLogicalSaturateScalar : ShiftLeftLogicalSaturateScalar_MethodGroup
        class ShiftLeftLogicalSaturateScalar_MethodGroup:
            def __call__(self, value: Vector64_1[int], count: int) -> Vector64_1[int]:...
            # Method ShiftLeftLogicalSaturateScalar(value : Vector64`1, count : Byte) was skipped since it collides with above method
            # Method ShiftLeftLogicalSaturateScalar(value : Vector64`1, count : Byte) was skipped since it collides with above method
            # Method ShiftLeftLogicalSaturateScalar(value : Vector64`1, count : Byte) was skipped since it collides with above method
            # Method ShiftLeftLogicalSaturateScalar(value : Vector64`1, count : Byte) was skipped since it collides with above method
            # Method ShiftLeftLogicalSaturateScalar(value : Vector64`1, count : Byte) was skipped since it collides with above method

        # Skipped ShiftLeftLogicalSaturateUnsignedScalar due to it being static, abstract and generic.

        ShiftLeftLogicalSaturateUnsignedScalar : ShiftLeftLogicalSaturateUnsignedScalar_MethodGroup
        class ShiftLeftLogicalSaturateUnsignedScalar_MethodGroup:
            def __call__(self, value: Vector64_1[int], count: int) -> Vector64_1[int]:...
            # Method ShiftLeftLogicalSaturateUnsignedScalar(value : Vector64`1, count : Byte) was skipped since it collides with above method
            # Method ShiftLeftLogicalSaturateUnsignedScalar(value : Vector64`1, count : Byte) was skipped since it collides with above method

        # Skipped ShiftLogicalRoundedSaturateScalar due to it being static, abstract and generic.

        ShiftLogicalRoundedSaturateScalar : ShiftLogicalRoundedSaturateScalar_MethodGroup
        class ShiftLogicalRoundedSaturateScalar_MethodGroup:
            def __call__(self, value: Vector64_1[int], count: Vector64_1[int]) -> Vector64_1[int]:...
            # Method ShiftLogicalRoundedSaturateScalar(value : Vector64`1, count : Vector64`1) was skipped since it collides with above method
            # Method ShiftLogicalRoundedSaturateScalar(value : Vector64`1, count : Vector64`1) was skipped since it collides with above method
            # Method ShiftLogicalRoundedSaturateScalar(value : Vector64`1, count : Vector64`1) was skipped since it collides with above method
            # Method ShiftLogicalRoundedSaturateScalar(value : Vector64`1, count : Vector64`1) was skipped since it collides with above method
            # Method ShiftLogicalRoundedSaturateScalar(value : Vector64`1, count : Vector64`1) was skipped since it collides with above method

        # Skipped ShiftLogicalSaturateScalar due to it being static, abstract and generic.

        ShiftLogicalSaturateScalar : ShiftLogicalSaturateScalar_MethodGroup
        class ShiftLogicalSaturateScalar_MethodGroup:
            def __call__(self, value: Vector64_1[int], count: Vector64_1[int]) -> Vector64_1[int]:...
            # Method ShiftLogicalSaturateScalar(value : Vector64`1, count : Vector64`1) was skipped since it collides with above method
            # Method ShiftLogicalSaturateScalar(value : Vector64`1, count : Vector64`1) was skipped since it collides with above method
            # Method ShiftLogicalSaturateScalar(value : Vector64`1, count : Vector64`1) was skipped since it collides with above method
            # Method ShiftLogicalSaturateScalar(value : Vector64`1, count : Vector64`1) was skipped since it collides with above method
            # Method ShiftLogicalSaturateScalar(value : Vector64`1, count : Vector64`1) was skipped since it collides with above method

        # Skipped ShiftRightArithmeticNarrowingSaturateScalar due to it being static, abstract and generic.

        ShiftRightArithmeticNarrowingSaturateScalar : ShiftRightArithmeticNarrowingSaturateScalar_MethodGroup
        class ShiftRightArithmeticNarrowingSaturateScalar_MethodGroup:
            def __call__(self, value: Vector64_1[int], count: int) -> Vector64_1[int]:...
            # Method ShiftRightArithmeticNarrowingSaturateScalar(value : Vector64`1, count : Byte) was skipped since it collides with above method
            # Method ShiftRightArithmeticNarrowingSaturateScalar(value : Vector64`1, count : Byte) was skipped since it collides with above method

        # Skipped ShiftRightArithmeticNarrowingSaturateUnsignedScalar due to it being static, abstract and generic.

        ShiftRightArithmeticNarrowingSaturateUnsignedScalar : ShiftRightArithmeticNarrowingSaturateUnsignedScalar_MethodGroup
        class ShiftRightArithmeticNarrowingSaturateUnsignedScalar_MethodGroup:
            def __call__(self, value: Vector64_1[int], count: int) -> Vector64_1[int]:...
            # Method ShiftRightArithmeticNarrowingSaturateUnsignedScalar(value : Vector64`1, count : Byte) was skipped since it collides with above method
            # Method ShiftRightArithmeticNarrowingSaturateUnsignedScalar(value : Vector64`1, count : Byte) was skipped since it collides with above method

        # Skipped ShiftRightArithmeticRoundedNarrowingSaturateScalar due to it being static, abstract and generic.

        ShiftRightArithmeticRoundedNarrowingSaturateScalar : ShiftRightArithmeticRoundedNarrowingSaturateScalar_MethodGroup
        class ShiftRightArithmeticRoundedNarrowingSaturateScalar_MethodGroup:
            def __call__(self, value: Vector64_1[int], count: int) -> Vector64_1[int]:...
            # Method ShiftRightArithmeticRoundedNarrowingSaturateScalar(value : Vector64`1, count : Byte) was skipped since it collides with above method
            # Method ShiftRightArithmeticRoundedNarrowingSaturateScalar(value : Vector64`1, count : Byte) was skipped since it collides with above method

        # Skipped ShiftRightArithmeticRoundedNarrowingSaturateUnsignedScalar due to it being static, abstract and generic.

        ShiftRightArithmeticRoundedNarrowingSaturateUnsignedScalar : ShiftRightArithmeticRoundedNarrowingSaturateUnsignedScalar_MethodGroup
        class ShiftRightArithmeticRoundedNarrowingSaturateUnsignedScalar_MethodGroup:
            def __call__(self, value: Vector64_1[int], count: int) -> Vector64_1[int]:...
            # Method ShiftRightArithmeticRoundedNarrowingSaturateUnsignedScalar(value : Vector64`1, count : Byte) was skipped since it collides with above method
            # Method ShiftRightArithmeticRoundedNarrowingSaturateUnsignedScalar(value : Vector64`1, count : Byte) was skipped since it collides with above method

        # Skipped ShiftRightLogicalNarrowingSaturateScalar due to it being static, abstract and generic.

        ShiftRightLogicalNarrowingSaturateScalar : ShiftRightLogicalNarrowingSaturateScalar_MethodGroup
        class ShiftRightLogicalNarrowingSaturateScalar_MethodGroup:
            def __call__(self, value: Vector64_1[int], count: int) -> Vector64_1[int]:...
            # Method ShiftRightLogicalNarrowingSaturateScalar(value : Vector64`1, count : Byte) was skipped since it collides with above method
            # Method ShiftRightLogicalNarrowingSaturateScalar(value : Vector64`1, count : Byte) was skipped since it collides with above method
            # Method ShiftRightLogicalNarrowingSaturateScalar(value : Vector64`1, count : Byte) was skipped since it collides with above method
            # Method ShiftRightLogicalNarrowingSaturateScalar(value : Vector64`1, count : Byte) was skipped since it collides with above method
            # Method ShiftRightLogicalNarrowingSaturateScalar(value : Vector64`1, count : Byte) was skipped since it collides with above method

        # Skipped ShiftRightLogicalRoundedNarrowingSaturateScalar due to it being static, abstract and generic.

        ShiftRightLogicalRoundedNarrowingSaturateScalar : ShiftRightLogicalRoundedNarrowingSaturateScalar_MethodGroup
        class ShiftRightLogicalRoundedNarrowingSaturateScalar_MethodGroup:
            def __call__(self, value: Vector64_1[int], count: int) -> Vector64_1[int]:...
            # Method ShiftRightLogicalRoundedNarrowingSaturateScalar(value : Vector64`1, count : Byte) was skipped since it collides with above method
            # Method ShiftRightLogicalRoundedNarrowingSaturateScalar(value : Vector64`1, count : Byte) was skipped since it collides with above method
            # Method ShiftRightLogicalRoundedNarrowingSaturateScalar(value : Vector64`1, count : Byte) was skipped since it collides with above method
            # Method ShiftRightLogicalRoundedNarrowingSaturateScalar(value : Vector64`1, count : Byte) was skipped since it collides with above method
            # Method ShiftRightLogicalRoundedNarrowingSaturateScalar(value : Vector64`1, count : Byte) was skipped since it collides with above method

        # Skipped Sqrt due to it being static, abstract and generic.

        Sqrt : Sqrt_MethodGroup
        class Sqrt_MethodGroup:
            @typing.overload
            def __call__(self, value: Vector128_1[float]) -> Vector128_1[float]:...
            # Method Sqrt(value : Vector128`1) was skipped since it collides with above method
            @typing.overload
            def __call__(self, value: Vector64_1[float]) -> Vector64_1[float]:...

        # Skipped StorePair due to it being static, abstract and generic.

        StorePair : StorePair_MethodGroup
        class StorePair_MethodGroup:
            @typing.overload
            def __call__(self, address: clr.Reference[float], value1: Vector64_1[float], value2: Vector64_1[float]) -> None:...
            # Method StorePair(address : Single*, value1 : Vector64`1, value2 : Vector64`1) was skipped since it collides with above method
            @typing.overload
            def __call__(self, address: clr.Reference[float], value1: Vector128_1[float], value2: Vector128_1[float]) -> None:...
            # Method StorePair(address : Single*, value1 : Vector128`1, value2 : Vector128`1) was skipped since it collides with above method
            # Method StorePair(address : Byte*, value1 : Vector64`1, value2 : Vector64`1) was skipped since it collides with above method
            # Method StorePair(address : Int16*, value1 : Vector64`1, value2 : Vector64`1) was skipped since it collides with above method
            # Method StorePair(address : Int32*, value1 : Vector64`1, value2 : Vector64`1) was skipped since it collides with above method
            # Method StorePair(address : Int64*, value1 : Vector64`1, value2 : Vector64`1) was skipped since it collides with above method
            # Method StorePair(address : SByte*, value1 : Vector64`1, value2 : Vector64`1) was skipped since it collides with above method
            # Method StorePair(address : UInt16*, value1 : Vector64`1, value2 : Vector64`1) was skipped since it collides with above method
            # Method StorePair(address : UInt32*, value1 : Vector64`1, value2 : Vector64`1) was skipped since it collides with above method
            # Method StorePair(address : UInt64*, value1 : Vector64`1, value2 : Vector64`1) was skipped since it collides with above method
            # Method StorePair(address : Byte*, value1 : Vector128`1, value2 : Vector128`1) was skipped since it collides with above method
            # Method StorePair(address : Int16*, value1 : Vector128`1, value2 : Vector128`1) was skipped since it collides with above method
            # Method StorePair(address : Int32*, value1 : Vector128`1, value2 : Vector128`1) was skipped since it collides with above method
            # Method StorePair(address : Int64*, value1 : Vector128`1, value2 : Vector128`1) was skipped since it collides with above method
            # Method StorePair(address : SByte*, value1 : Vector128`1, value2 : Vector128`1) was skipped since it collides with above method
            # Method StorePair(address : UInt16*, value1 : Vector128`1, value2 : Vector128`1) was skipped since it collides with above method
            # Method StorePair(address : UInt32*, value1 : Vector128`1, value2 : Vector128`1) was skipped since it collides with above method
            # Method StorePair(address : UInt64*, value1 : Vector128`1, value2 : Vector128`1) was skipped since it collides with above method

        # Skipped StorePairNonTemporal due to it being static, abstract and generic.

        StorePairNonTemporal : StorePairNonTemporal_MethodGroup
        class StorePairNonTemporal_MethodGroup:
            @typing.overload
            def __call__(self, address: clr.Reference[float], value1: Vector64_1[float], value2: Vector64_1[float]) -> None:...
            # Method StorePairNonTemporal(address : Single*, value1 : Vector64`1, value2 : Vector64`1) was skipped since it collides with above method
            @typing.overload
            def __call__(self, address: clr.Reference[float], value1: Vector128_1[float], value2: Vector128_1[float]) -> None:...
            # Method StorePairNonTemporal(address : Single*, value1 : Vector128`1, value2 : Vector128`1) was skipped since it collides with above method
            # Method StorePairNonTemporal(address : Byte*, value1 : Vector64`1, value2 : Vector64`1) was skipped since it collides with above method
            # Method StorePairNonTemporal(address : Int16*, value1 : Vector64`1, value2 : Vector64`1) was skipped since it collides with above method
            # Method StorePairNonTemporal(address : Int32*, value1 : Vector64`1, value2 : Vector64`1) was skipped since it collides with above method
            # Method StorePairNonTemporal(address : Int64*, value1 : Vector64`1, value2 : Vector64`1) was skipped since it collides with above method
            # Method StorePairNonTemporal(address : SByte*, value1 : Vector64`1, value2 : Vector64`1) was skipped since it collides with above method
            # Method StorePairNonTemporal(address : UInt16*, value1 : Vector64`1, value2 : Vector64`1) was skipped since it collides with above method
            # Method StorePairNonTemporal(address : UInt32*, value1 : Vector64`1, value2 : Vector64`1) was skipped since it collides with above method
            # Method StorePairNonTemporal(address : UInt64*, value1 : Vector64`1, value2 : Vector64`1) was skipped since it collides with above method
            # Method StorePairNonTemporal(address : Byte*, value1 : Vector128`1, value2 : Vector128`1) was skipped since it collides with above method
            # Method StorePairNonTemporal(address : Int16*, value1 : Vector128`1, value2 : Vector128`1) was skipped since it collides with above method
            # Method StorePairNonTemporal(address : Int32*, value1 : Vector128`1, value2 : Vector128`1) was skipped since it collides with above method
            # Method StorePairNonTemporal(address : Int64*, value1 : Vector128`1, value2 : Vector128`1) was skipped since it collides with above method
            # Method StorePairNonTemporal(address : SByte*, value1 : Vector128`1, value2 : Vector128`1) was skipped since it collides with above method
            # Method StorePairNonTemporal(address : UInt16*, value1 : Vector128`1, value2 : Vector128`1) was skipped since it collides with above method
            # Method StorePairNonTemporal(address : UInt32*, value1 : Vector128`1, value2 : Vector128`1) was skipped since it collides with above method
            # Method StorePairNonTemporal(address : UInt64*, value1 : Vector128`1, value2 : Vector128`1) was skipped since it collides with above method

        # Skipped StorePairScalar due to it being static, abstract and generic.

        StorePairScalar : StorePairScalar_MethodGroup
        class StorePairScalar_MethodGroup:
            def __call__(self, address: clr.Reference[float], value1: Vector64_1[float], value2: Vector64_1[float]) -> None:...
            # Method StorePairScalar(address : Int32*, value1 : Vector64`1, value2 : Vector64`1) was skipped since it collides with above method
            # Method StorePairScalar(address : UInt32*, value1 : Vector64`1, value2 : Vector64`1) was skipped since it collides with above method

        # Skipped StorePairScalarNonTemporal due to it being static, abstract and generic.

        StorePairScalarNonTemporal : StorePairScalarNonTemporal_MethodGroup
        class StorePairScalarNonTemporal_MethodGroup:
            def __call__(self, address: clr.Reference[float], value1: Vector64_1[float], value2: Vector64_1[float]) -> None:...
            # Method StorePairScalarNonTemporal(address : Int32*, value1 : Vector64`1, value2 : Vector64`1) was skipped since it collides with above method
            # Method StorePairScalarNonTemporal(address : UInt32*, value1 : Vector64`1, value2 : Vector64`1) was skipped since it collides with above method

        # Skipped SubtractSaturateScalar due to it being static, abstract and generic.

        SubtractSaturateScalar : SubtractSaturateScalar_MethodGroup
        class SubtractSaturateScalar_MethodGroup:
            def __call__(self, left: Vector64_1[int], right: Vector64_1[int]) -> Vector64_1[int]:...
            # Method SubtractSaturateScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method SubtractSaturateScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method SubtractSaturateScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method SubtractSaturateScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method SubtractSaturateScalar(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

        # Skipped TransposeEven due to it being static, abstract and generic.

        TransposeEven : TransposeEven_MethodGroup
        class TransposeEven_MethodGroup:
            @typing.overload
            def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
            @typing.overload
            def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
            # Method TransposeEven(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method TransposeEven(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method TransposeEven(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method TransposeEven(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method TransposeEven(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method TransposeEven(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method TransposeEven(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method TransposeEven(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method TransposeEven(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method TransposeEven(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method TransposeEven(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method TransposeEven(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method TransposeEven(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method TransposeEven(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method TransposeEven(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

        # Skipped TransposeOdd due to it being static, abstract and generic.

        TransposeOdd : TransposeOdd_MethodGroup
        class TransposeOdd_MethodGroup:
            @typing.overload
            def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
            @typing.overload
            def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
            # Method TransposeOdd(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method TransposeOdd(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method TransposeOdd(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method TransposeOdd(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method TransposeOdd(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method TransposeOdd(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method TransposeOdd(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method TransposeOdd(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method TransposeOdd(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method TransposeOdd(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method TransposeOdd(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method TransposeOdd(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method TransposeOdd(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method TransposeOdd(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method TransposeOdd(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

        # Skipped UnzipEven due to it being static, abstract and generic.

        UnzipEven : UnzipEven_MethodGroup
        class UnzipEven_MethodGroup:
            @typing.overload
            def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
            @typing.overload
            def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
            # Method UnzipEven(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method UnzipEven(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method UnzipEven(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method UnzipEven(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method UnzipEven(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method UnzipEven(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method UnzipEven(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method UnzipEven(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method UnzipEven(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method UnzipEven(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method UnzipEven(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method UnzipEven(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method UnzipEven(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method UnzipEven(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method UnzipEven(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

        # Skipped UnzipOdd due to it being static, abstract and generic.

        UnzipOdd : UnzipOdd_MethodGroup
        class UnzipOdd_MethodGroup:
            @typing.overload
            def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
            @typing.overload
            def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
            # Method UnzipOdd(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method UnzipOdd(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method UnzipOdd(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method UnzipOdd(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method UnzipOdd(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method UnzipOdd(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method UnzipOdd(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method UnzipOdd(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method UnzipOdd(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method UnzipOdd(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method UnzipOdd(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method UnzipOdd(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method UnzipOdd(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method UnzipOdd(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method UnzipOdd(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

        # Skipped VectorTableLookup due to it being static, abstract and generic.

        VectorTableLookup : VectorTableLookup_MethodGroup
        class VectorTableLookup_MethodGroup:
            def __call__(self, table: Vector128_1[int], byteIndexes: Vector128_1[int]) -> Vector128_1[int]:...
            # Method VectorTableLookup(table : Vector128`1, byteIndexes : Vector128`1) was skipped since it collides with above method

        # Skipped VectorTableLookupExtension due to it being static, abstract and generic.

        VectorTableLookupExtension : VectorTableLookupExtension_MethodGroup
        class VectorTableLookupExtension_MethodGroup:
            def __call__(self, defaultValues: Vector128_1[int], table: Vector128_1[int], byteIndexes: Vector128_1[int]) -> Vector128_1[int]:...
            # Method VectorTableLookupExtension(defaultValues : Vector128`1, table : Vector128`1, byteIndexes : Vector128`1) was skipped since it collides with above method

        # Skipped ZipHigh due to it being static, abstract and generic.

        ZipHigh : ZipHigh_MethodGroup
        class ZipHigh_MethodGroup:
            @typing.overload
            def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
            @typing.overload
            def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
            # Method ZipHigh(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method ZipHigh(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method ZipHigh(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method ZipHigh(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method ZipHigh(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method ZipHigh(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method ZipHigh(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method ZipHigh(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method ZipHigh(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method ZipHigh(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method ZipHigh(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method ZipHigh(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method ZipHigh(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method ZipHigh(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method ZipHigh(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

        # Skipped ZipLow due to it being static, abstract and generic.

        ZipLow : ZipLow_MethodGroup
        class ZipLow_MethodGroup:
            @typing.overload
            def __call__(self, left: Vector64_1[float], right: Vector64_1[float]) -> Vector64_1[float]:...
            @typing.overload
            def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
            # Method ZipLow(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method ZipLow(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method ZipLow(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method ZipLow(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method ZipLow(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method ZipLow(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method ZipLow(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
            # Method ZipLow(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method ZipLow(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method ZipLow(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method ZipLow(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method ZipLow(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method ZipLow(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method ZipLow(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method ZipLow(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method




class Aes(ArmBase):
    @classmethod
    @property
    def IsSupported(cls) -> bool: ...
    @staticmethod
    def Decrypt(value: Vector128_1[int], roundKey: Vector128_1[int]) -> Vector128_1[int]: ...
    @staticmethod
    def Encrypt(value: Vector128_1[int], roundKey: Vector128_1[int]) -> Vector128_1[int]: ...
    @staticmethod
    def InverseMixColumns(value: Vector128_1[int]) -> Vector128_1[int]: ...
    @staticmethod
    def MixColumns(value: Vector128_1[int]) -> Vector128_1[int]: ...
    # Skipped PolynomialMultiplyWideningLower due to it being static, abstract and generic.

    PolynomialMultiplyWideningLower : PolynomialMultiplyWideningLower_MethodGroup
    class PolynomialMultiplyWideningLower_MethodGroup:
        def __call__(self, left: Vector64_1[int], right: Vector64_1[int]) -> Vector128_1[int]:...
        # Method PolynomialMultiplyWideningLower(left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

    # Skipped PolynomialMultiplyWideningUpper due to it being static, abstract and generic.

    PolynomialMultiplyWideningUpper : PolynomialMultiplyWideningUpper_MethodGroup
    class PolynomialMultiplyWideningUpper_MethodGroup:
        def __call__(self, left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
        # Method PolynomialMultiplyWideningUpper(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method


    class Arm64(ArmBase.Arm64):
        @classmethod
        @property
        def IsSupported(cls) -> bool: ...



class ArmBase(abc.ABC):
    @classmethod
    @property
    def IsSupported(cls) -> bool: ...
    # Skipped LeadingZeroCount due to it being static, abstract and generic.

    LeadingZeroCount : LeadingZeroCount_MethodGroup
    class LeadingZeroCount_MethodGroup:
        def __call__(self, value: int) -> int:...
        # Method LeadingZeroCount(value : UInt32) was skipped since it collides with above method

    # Skipped ReverseElementBits due to it being static, abstract and generic.

    ReverseElementBits : ReverseElementBits_MethodGroup
    class ReverseElementBits_MethodGroup:
        def __call__(self, value: int) -> int:...
        # Method ReverseElementBits(value : UInt32) was skipped since it collides with above method


    class Arm64(abc.ABC):
        @classmethod
        @property
        def IsSupported(cls) -> bool: ...
        # Skipped LeadingSignCount due to it being static, abstract and generic.

        LeadingSignCount : LeadingSignCount_MethodGroup
        class LeadingSignCount_MethodGroup:
            def __call__(self, value: int) -> int:...
            # Method LeadingSignCount(value : Int64) was skipped since it collides with above method

        # Skipped LeadingZeroCount due to it being static, abstract and generic.

        LeadingZeroCount : LeadingZeroCount_MethodGroup
        class LeadingZeroCount_MethodGroup:
            def __call__(self, value: int) -> int:...
            # Method LeadingZeroCount(value : UInt64) was skipped since it collides with above method

        # Skipped MultiplyHigh due to it being static, abstract and generic.

        MultiplyHigh : MultiplyHigh_MethodGroup
        class MultiplyHigh_MethodGroup:
            def __call__(self, left: int, right: int) -> int:...
            # Method MultiplyHigh(left : UInt64, right : UInt64) was skipped since it collides with above method

        # Skipped ReverseElementBits due to it being static, abstract and generic.

        ReverseElementBits : ReverseElementBits_MethodGroup
        class ReverseElementBits_MethodGroup:
            def __call__(self, value: int) -> int:...
            # Method ReverseElementBits(value : UInt64) was skipped since it collides with above method




class Crc32(ArmBase):
    @classmethod
    @property
    def IsSupported(cls) -> bool: ...
    # Skipped ComputeCrc32 due to it being static, abstract and generic.

    ComputeCrc32 : ComputeCrc32_MethodGroup
    class ComputeCrc32_MethodGroup:
        def __call__(self, crc: int, data: int) -> int:...
        # Method ComputeCrc32(crc : UInt32, data : UInt16) was skipped since it collides with above method
        # Method ComputeCrc32(crc : UInt32, data : UInt32) was skipped since it collides with above method

    # Skipped ComputeCrc32C due to it being static, abstract and generic.

    ComputeCrc32C : ComputeCrc32C_MethodGroup
    class ComputeCrc32C_MethodGroup:
        def __call__(self, crc: int, data: int) -> int:...
        # Method ComputeCrc32C(crc : UInt32, data : UInt16) was skipped since it collides with above method
        # Method ComputeCrc32C(crc : UInt32, data : UInt32) was skipped since it collides with above method


    class Arm64(ArmBase.Arm64):
        @classmethod
        @property
        def IsSupported(cls) -> bool: ...
        @staticmethod
        def ComputeCrc32(crc: int, data: int) -> int: ...
        @staticmethod
        def ComputeCrc32C(crc: int, data: int) -> int: ...



class Dp(AdvSimd):
    @classmethod
    @property
    def IsSupported(cls) -> bool: ...
    # Skipped DotProduct due to it being static, abstract and generic.

    DotProduct : DotProduct_MethodGroup
    class DotProduct_MethodGroup:
        @typing.overload
        def __call__(self, addend: Vector64_1[int], left: Vector64_1[int], right: Vector64_1[int]) -> Vector64_1[int]:...
        # Method DotProduct(addend : Vector64`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, addend: Vector128_1[int], left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
        # Method DotProduct(addend : Vector128`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped DotProductBySelectedQuadruplet due to it being static, abstract and generic.

    DotProductBySelectedQuadruplet : DotProductBySelectedQuadruplet_MethodGroup
    class DotProductBySelectedQuadruplet_MethodGroup:
        @typing.overload
        def __call__(self, addend: Vector64_1[int], left: Vector64_1[int], right: Vector64_1[int], rightScaledIndex: int) -> Vector64_1[int]:...
        @typing.overload
        def __call__(self, addend: Vector64_1[int], left: Vector64_1[int], right: Vector128_1[int], rightScaledIndex: int) -> Vector64_1[int]:...
        # Method DotProductBySelectedQuadruplet(addend : Vector64`1, left : Vector64`1, right : Vector64`1, rightScaledIndex : Byte) was skipped since it collides with above method
        # Method DotProductBySelectedQuadruplet(addend : Vector64`1, left : Vector64`1, right : Vector128`1, rightScaledIndex : Byte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, addend: Vector128_1[int], left: Vector128_1[int], right: Vector128_1[int], rightScaledIndex: int) -> Vector128_1[int]:...
        @typing.overload
        def __call__(self, addend: Vector128_1[int], left: Vector128_1[int], right: Vector64_1[int], rightScaledIndex: int) -> Vector128_1[int]:...
        # Method DotProductBySelectedQuadruplet(addend : Vector128`1, left : Vector128`1, right : Vector128`1, rightScaledIndex : Byte) was skipped since it collides with above method
        # Method DotProductBySelectedQuadruplet(addend : Vector128`1, left : Vector128`1, right : Vector64`1, rightScaledIndex : Byte) was skipped since it collides with above method


    class Arm64(AdvSimd.Arm64):
        @classmethod
        @property
        def IsSupported(cls) -> bool: ...



class Rdm(AdvSimd):
    @classmethod
    @property
    def IsSupported(cls) -> bool: ...
    # Skipped MultiplyRoundedDoublingAndAddSaturateHigh due to it being static, abstract and generic.

    MultiplyRoundedDoublingAndAddSaturateHigh : MultiplyRoundedDoublingAndAddSaturateHigh_MethodGroup
    class MultiplyRoundedDoublingAndAddSaturateHigh_MethodGroup:
        @typing.overload
        def __call__(self, addend: Vector64_1[int], left: Vector64_1[int], right: Vector64_1[int]) -> Vector64_1[int]:...
        # Method MultiplyRoundedDoublingAndAddSaturateHigh(addend : Vector64`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, addend: Vector128_1[int], left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
        # Method MultiplyRoundedDoublingAndAddSaturateHigh(addend : Vector128`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped MultiplyRoundedDoublingAndSubtractSaturateHigh due to it being static, abstract and generic.

    MultiplyRoundedDoublingAndSubtractSaturateHigh : MultiplyRoundedDoublingAndSubtractSaturateHigh_MethodGroup
    class MultiplyRoundedDoublingAndSubtractSaturateHigh_MethodGroup:
        @typing.overload
        def __call__(self, minuend: Vector64_1[int], left: Vector64_1[int], right: Vector64_1[int]) -> Vector64_1[int]:...
        # Method MultiplyRoundedDoublingAndSubtractSaturateHigh(minuend : Vector64`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, minuend: Vector128_1[int], left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
        # Method MultiplyRoundedDoublingAndSubtractSaturateHigh(minuend : Vector128`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped MultiplyRoundedDoublingBySelectedScalarAndAddSaturateHigh due to it being static, abstract and generic.

    MultiplyRoundedDoublingBySelectedScalarAndAddSaturateHigh : MultiplyRoundedDoublingBySelectedScalarAndAddSaturateHigh_MethodGroup
    class MultiplyRoundedDoublingBySelectedScalarAndAddSaturateHigh_MethodGroup:
        @typing.overload
        def __call__(self, addend: Vector64_1[int], left: Vector64_1[int], right: Vector64_1[int], rightIndex: int) -> Vector64_1[int]:...
        @typing.overload
        def __call__(self, addend: Vector64_1[int], left: Vector64_1[int], right: Vector128_1[int], rightIndex: int) -> Vector64_1[int]:...
        # Method MultiplyRoundedDoublingBySelectedScalarAndAddSaturateHigh(addend : Vector64`1, left : Vector64`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyRoundedDoublingBySelectedScalarAndAddSaturateHigh(addend : Vector64`1, left : Vector64`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, addend: Vector128_1[int], left: Vector128_1[int], right: Vector64_1[int], rightIndex: int) -> Vector128_1[int]:...
        @typing.overload
        def __call__(self, addend: Vector128_1[int], left: Vector128_1[int], right: Vector128_1[int], rightIndex: int) -> Vector128_1[int]:...
        # Method MultiplyRoundedDoublingBySelectedScalarAndAddSaturateHigh(addend : Vector128`1, left : Vector128`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyRoundedDoublingBySelectedScalarAndAddSaturateHigh(addend : Vector128`1, left : Vector128`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method

    # Skipped MultiplyRoundedDoublingBySelectedScalarAndSubtractSaturateHigh due to it being static, abstract and generic.

    MultiplyRoundedDoublingBySelectedScalarAndSubtractSaturateHigh : MultiplyRoundedDoublingBySelectedScalarAndSubtractSaturateHigh_MethodGroup
    class MultiplyRoundedDoublingBySelectedScalarAndSubtractSaturateHigh_MethodGroup:
        @typing.overload
        def __call__(self, minuend: Vector64_1[int], left: Vector64_1[int], right: Vector64_1[int], rightIndex: int) -> Vector64_1[int]:...
        @typing.overload
        def __call__(self, minuend: Vector64_1[int], left: Vector64_1[int], right: Vector128_1[int], rightIndex: int) -> Vector64_1[int]:...
        # Method MultiplyRoundedDoublingBySelectedScalarAndSubtractSaturateHigh(minuend : Vector64`1, left : Vector64`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyRoundedDoublingBySelectedScalarAndSubtractSaturateHigh(minuend : Vector64`1, left : Vector64`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, minuend: Vector128_1[int], left: Vector128_1[int], right: Vector64_1[int], rightIndex: int) -> Vector128_1[int]:...
        @typing.overload
        def __call__(self, minuend: Vector128_1[int], left: Vector128_1[int], right: Vector128_1[int], rightIndex: int) -> Vector128_1[int]:...
        # Method MultiplyRoundedDoublingBySelectedScalarAndSubtractSaturateHigh(minuend : Vector128`1, left : Vector128`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
        # Method MultiplyRoundedDoublingBySelectedScalarAndSubtractSaturateHigh(minuend : Vector128`1, left : Vector128`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method


    class Arm64(AdvSimd.Arm64):
        @classmethod
        @property
        def IsSupported(cls) -> bool: ...
        # Skipped MultiplyRoundedDoublingAndAddSaturateHighScalar due to it being static, abstract and generic.

        MultiplyRoundedDoublingAndAddSaturateHighScalar : MultiplyRoundedDoublingAndAddSaturateHighScalar_MethodGroup
        class MultiplyRoundedDoublingAndAddSaturateHighScalar_MethodGroup:
            def __call__(self, addend: Vector64_1[int], left: Vector64_1[int], right: Vector64_1[int]) -> Vector64_1[int]:...
            # Method MultiplyRoundedDoublingAndAddSaturateHighScalar(addend : Vector64`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

        # Skipped MultiplyRoundedDoublingAndSubtractSaturateHighScalar due to it being static, abstract and generic.

        MultiplyRoundedDoublingAndSubtractSaturateHighScalar : MultiplyRoundedDoublingAndSubtractSaturateHighScalar_MethodGroup
        class MultiplyRoundedDoublingAndSubtractSaturateHighScalar_MethodGroup:
            def __call__(self, addend: Vector64_1[int], left: Vector64_1[int], right: Vector64_1[int]) -> Vector64_1[int]:...
            # Method MultiplyRoundedDoublingAndSubtractSaturateHighScalar(addend : Vector64`1, left : Vector64`1, right : Vector64`1) was skipped since it collides with above method

        # Skipped MultiplyRoundedDoublingScalarBySelectedScalarAndAddSaturateHigh due to it being static, abstract and generic.

        MultiplyRoundedDoublingScalarBySelectedScalarAndAddSaturateHigh : MultiplyRoundedDoublingScalarBySelectedScalarAndAddSaturateHigh_MethodGroup
        class MultiplyRoundedDoublingScalarBySelectedScalarAndAddSaturateHigh_MethodGroup:
            @typing.overload
            def __call__(self, addend: Vector64_1[int], left: Vector64_1[int], right: Vector64_1[int], rightIndex: int) -> Vector64_1[int]:...
            @typing.overload
            def __call__(self, addend: Vector64_1[int], left: Vector64_1[int], right: Vector128_1[int], rightIndex: int) -> Vector64_1[int]:...
            # Method MultiplyRoundedDoublingScalarBySelectedScalarAndAddSaturateHigh(addend : Vector64`1, left : Vector64`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
            # Method MultiplyRoundedDoublingScalarBySelectedScalarAndAddSaturateHigh(addend : Vector64`1, left : Vector64`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method

        # Skipped MultiplyRoundedDoublingScalarBySelectedScalarAndSubtractSaturateHigh due to it being static, abstract and generic.

        MultiplyRoundedDoublingScalarBySelectedScalarAndSubtractSaturateHigh : MultiplyRoundedDoublingScalarBySelectedScalarAndSubtractSaturateHigh_MethodGroup
        class MultiplyRoundedDoublingScalarBySelectedScalarAndSubtractSaturateHigh_MethodGroup:
            @typing.overload
            def __call__(self, minuend: Vector64_1[int], left: Vector64_1[int], right: Vector64_1[int], rightIndex: int) -> Vector64_1[int]:...
            @typing.overload
            def __call__(self, minuend: Vector64_1[int], left: Vector64_1[int], right: Vector128_1[int], rightIndex: int) -> Vector64_1[int]:...
            # Method MultiplyRoundedDoublingScalarBySelectedScalarAndSubtractSaturateHigh(minuend : Vector64`1, left : Vector64`1, right : Vector64`1, rightIndex : Byte) was skipped since it collides with above method
            # Method MultiplyRoundedDoublingScalarBySelectedScalarAndSubtractSaturateHigh(minuend : Vector64`1, left : Vector64`1, right : Vector128`1, rightIndex : Byte) was skipped since it collides with above method




class Sha1(ArmBase):
    @classmethod
    @property
    def IsSupported(cls) -> bool: ...
    @staticmethod
    def FixedRotate(hash_e: Vector64_1[int]) -> Vector64_1[int]: ...
    @staticmethod
    def HashUpdateChoose(hash_abcd: Vector128_1[int], hash_e: Vector64_1[int], wk: Vector128_1[int]) -> Vector128_1[int]: ...
    @staticmethod
    def HashUpdateMajority(hash_abcd: Vector128_1[int], hash_e: Vector64_1[int], wk: Vector128_1[int]) -> Vector128_1[int]: ...
    @staticmethod
    def HashUpdateParity(hash_abcd: Vector128_1[int], hash_e: Vector64_1[int], wk: Vector128_1[int]) -> Vector128_1[int]: ...
    @staticmethod
    def ScheduleUpdate0(w0_3: Vector128_1[int], w4_7: Vector128_1[int], w8_11: Vector128_1[int]) -> Vector128_1[int]: ...
    @staticmethod
    def ScheduleUpdate1(tw0_3: Vector128_1[int], w12_15: Vector128_1[int]) -> Vector128_1[int]: ...

    class Arm64(ArmBase.Arm64):
        @classmethod
        @property
        def IsSupported(cls) -> bool: ...



class Sha256(ArmBase):
    @classmethod
    @property
    def IsSupported(cls) -> bool: ...
    @staticmethod
    def HashUpdate1(hash_abcd: Vector128_1[int], hash_efgh: Vector128_1[int], wk: Vector128_1[int]) -> Vector128_1[int]: ...
    @staticmethod
    def HashUpdate2(hash_efgh: Vector128_1[int], hash_abcd: Vector128_1[int], wk: Vector128_1[int]) -> Vector128_1[int]: ...
    @staticmethod
    def ScheduleUpdate0(w0_3: Vector128_1[int], w4_7: Vector128_1[int]) -> Vector128_1[int]: ...
    @staticmethod
    def ScheduleUpdate1(w0_3: Vector128_1[int], w8_11: Vector128_1[int], w12_15: Vector128_1[int]) -> Vector128_1[int]: ...

    class Arm64(ArmBase.Arm64):
        @classmethod
        @property
        def IsSupported(cls) -> bool: ...


