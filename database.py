from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from alembic.config import Config
from alembic import command

SQLALCHEMY_DATABASE_URL = "postgresql://admin:admin123@localhost/fast-api"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

alembic_cfg = Config("alembic.ini")
alembic_cfg.set_main_option("sqlalchemy.url", SQLALCHEMY_DATABASE_URL)
command.upgrade(alembic_cfg, "head")


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
