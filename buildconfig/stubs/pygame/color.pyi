import sys
from typing import Any, Dict, Iterator, Tuple, Union, overload

from ._common import ColorValue

if sys.version_info >= (3, 9):
    from collections.abc import Collection
else:
    from typing import Collection

THECOLORS: Dict[str, Tuple[int, int, int, int]]

# Color confirms to the Collection ABC, since it also confirms to
# Sized, Iterable and Container ABCs
class Color(Collection[int]):
    r: int
    g: int
    b: int
    a: int
    cmy: Tuple[float, float, float]
    hsva: Tuple[float, float, float, float]
    hsla: Tuple[float, float, float, float]
    i1i2i3: Tuple[float, float, float]
    __hash__: None  # type: ignore
    __array_struct__: Any
    @overload
    def __init__(self, r: int, g: int, b: int, a: int = 255) -> None: ...
    @overload
    def __init__(self, rgbvalue: ColorValue) -> None: ...
    @overload
    def __getitem__(self, i: int) -> int: ...
    @overload
    def __getitem__(self, s: slice) -> Tuple[int]: ...
    def __setitem__(self, key: int, value: int) -> None: ...
    def __iter__(self) -> Iterator[int]: ...
    def __add__(self, other: Color) -> Color: ...
    def __sub__(self, other: Color) -> Color: ...
    def __mul__(self, other: Color) -> Color: ...
    def __floordiv__(self, other: Color) -> Color: ...
    def __mod__(self, other: Color) -> Color: ...
    def __int__(self) -> int: ...
    def __float__(self) -> float: ...
    def __len__(self) -> int: ...
    def __index__(self) -> int: ...
    def __invert__(self) -> Color: ...
    def __contains__(self, other: int) -> bool: ...  # type: ignore[override]
    def __getattribute__(self, attr: str) -> Union[Color, tuple]: ...
    def __setattr__(self, attr: str, value: Union[Color, tuple]) -> None: ...
    @overload
    @classmethod
    def from_cmy(cls, object: Tuple[float, float, float]) -> Color: ...
    @overload
    @classmethod
    def from_cmy(cls, c: float, m: float, y: float) -> Color: ...
    @overload
    @classmethod
    def from_hsva(cls, object: Tuple[float, float, float, float]) -> Color: ...
    @overload
    @classmethod
    def from_hsva(cls, h: float, s: float, v: float, a: float) -> Color: ...
    @overload
    @classmethod
    def from_hsla(cls, object: Tuple[float, float, float, float]) -> Color: ...
    @overload
    @classmethod
    def from_hsla(cls, h: float, s: float, l: float, a: float) -> Color: ...
    @overload
    @classmethod
    def from_i1i2i3(cls, object: Tuple[float, float, float]) -> Color: ...
    @overload
    @classmethod
    def from_i1i2i3(cls, i1: float, i2: float, i3: float) -> Color: ...
    def normalize(self) -> Tuple[float, float, float, float]: ...
    def correct_gamma(self, gamma: float) -> Color: ...
    def set_length(self, length: int) -> None: ...
    def lerp(self, color: ColorValue, amount: float) -> Color: ...
    def premul_alpha(self) -> Color: ...
    def grayscale(self) -> Color: ...
    @overload
    def update(self, r: int, g: int, b: int, a: int = 255) -> None: ...
    @overload
    def update(self, rgbvalue: ColorValue) -> None: ...
