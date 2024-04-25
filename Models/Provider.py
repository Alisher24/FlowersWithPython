from dataclasses import dataclass

@dataclass(frozen=True)
class Provider:
    
    id: int
    name: str