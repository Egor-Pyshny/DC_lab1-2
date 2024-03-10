from alembic.models.UserModel import User
from repositories.sql_repositories.user_repository import SQLUserRepository
from schemas.schemas import UserAddSchema, UserUpdateSchema, UserSchema
from services.data_provider_service.user_provider_base import UserProviderBase


class UserProvider(UserProviderBase):

    def __init__(self):
        self.repository = SQLUserRepository()

    def create_user(self, item: UserAddSchema):
        res = User(
                    login=item.login,
                    password=item.password,
                    firstname=item.firstname,
                    lastname=item.lastname,
                )
        self.repository.create(res)
        result_dto = UserSchema.model_validate(res)
        return result_dto

    def get_users(self):
        user_orm = self.repository.get_all()
        result_dtos = [UserSchema.model_validate(row) for row in user_orm]
        return result_dtos

    def get_user(self, id):
        user_orm = self.repository.get(id)
        result_dtos = [UserSchema.model_validate(row) for row in user_orm]
        return result_dtos[0]

    def delete_user(self, item_id):
        return self.repository.delete(item_id)

    def update_user(self, item: UserUpdateSchema):
        res = User(
                    id=item.id,
                    login=item.login,
                    password=item.password,
                    firstname=item.firstname,
                    lastname=item.lastname,
                )
        user_orm = self.repository.update(res)
        return UserSchema.model_validate(user_orm)
