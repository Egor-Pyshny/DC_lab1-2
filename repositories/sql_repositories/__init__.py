from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def with_session(func):
    def wrapper(self, *args, **kwargs):
        with Session() as session:
            with session.begin():
                res = func(self, session, *args, **kwargs)
        return res
    return wrapper


engine = create_engine('postgresql://postgres:postgres@localhost/distcomp')
Session = sessionmaker(bind=engine, expire_on_commit=False)
