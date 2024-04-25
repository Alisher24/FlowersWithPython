from dataclasses import dataclass

@dataclass(frozen=True)
class Flowers:
    id: int
    name: str   
