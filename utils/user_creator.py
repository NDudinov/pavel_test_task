from faker import Faker


class UserCreator:

    __faker = Faker()

    @classmethod
    def create_user_json(cls) -> dict:
        return {"name": cls.__faker.name(), "job": cls.__faker.job()}
