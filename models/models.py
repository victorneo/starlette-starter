import sqlalchemy
from .meta import metadata, database


users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("username", sqlalchemy.String(length=50)),
    sqlalchemy.Column("password", sqlalchemy.String),
)


class UserManager(object):
    async def add_user(self, username, password):
        hashed = encrypt_password(password)
        bpriv_key, bpub_key = generate_keypair()

        query = users.insert().values(
            username=username,
            password=hashed,
        )
        await database.execute(query)

    async def get_user(self, username):
        query = users.select().where(users.c.username==username)
        results = await database.fetch_one(query)
        return results


user_manager = UserManager()
