from sqlalchemy import create_engine

from values import USER, PASSWORD, DATABASE_URL, DATABASE_NAME

config: str = 'mysql+pymysql://{}:{}@{}/{}'.format(USER,PASSWORD,DATABASE_URL,DATABASE_NAME)
engine = create_engine(config)


