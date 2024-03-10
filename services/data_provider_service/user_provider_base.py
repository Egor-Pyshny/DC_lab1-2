from abc import abstractmethod, ABC

from schemas.schemas import UserUpdateSchema, UserAddSchema


class UserProviderBase(ABC):

    @abstractmethod
    def create_user(self, item: UserAddSchema):
        """Создание нового пользователя"""

    @abstractmethod
    def get_users(self):
        """Получение всех новостей"""

    @abstractmethod
    def get_user(self, id):
        """Получение пользователя по id"""

    @abstractmethod
    def delete_user(self, item_id):
        """Удаление пользователя по id"""

    @abstractmethod
    def update_user(self, item: UserUpdateSchema):
        """Обновление пользователя"""
