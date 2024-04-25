from dataclasses import dataclass
from Models import Florists as florists

@dataclass(frozen=True)
class Bouquet:
    id: int
    name: str
    price: int
    florist: florists.Florists