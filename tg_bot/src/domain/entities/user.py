import enum
from dataclasses import dataclass, field
from datetime import date, datetime


class Sources(enum.Enum):
    VK = 'vk'
    TG = 'tg'
    MAX = 'max'


@dataclass
class User:
    id: int
    source: Sources
    surname: str
    name: str
    patronymic: str
    region: str
    created_at: datetime = field(default_factory=lambda: datetime.now())
