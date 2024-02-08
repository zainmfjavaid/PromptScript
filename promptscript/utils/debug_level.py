from dataclasses import dataclass


@dataclass
class DebugLevel:
    DEBUG: int = 100
    INFO: int = 200
    WARNING: int = 300
    ERROR: int = 400