from abc import ABC, abstractmethod
from datetime import date

from src.domain.entities.user import User


class IUserService(ABC):
    @abstractmethod
    async def create_user(
            self, user_id: int,
            surname: str, name: str,
            patronymic: str | None,
            region: str
    ) -> User:
        ...

    @abstractmethod
    async def is_user_exists(self, user_id: int) -> bool:
        ...

    @abstractmethod
    async def validate_fio_part(self, part: str, part_name: str) -> str:
        ...
    
    @abstractmethod
    async def get_similar_regions(self, region: str) -> list[str]:
        ...

    @abstractmethod
    async def get_region_address(self, region: str) -> str:
        ...

    @abstractmethod
    async def get_user_region(self, user_id: int) -> str:
        ...

    @abstractmethod
    async def get_all_users(self) -> list[User]:
        ...

    @abstractmethod
    async def get_region_by_prefix(self, region_prefix: str) -> str:
        ...
