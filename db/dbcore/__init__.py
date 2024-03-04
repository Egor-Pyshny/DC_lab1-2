from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('postgresql://postgres:postgres@localhost/distcomp')
Session = sessionmaker(bind=engine)
