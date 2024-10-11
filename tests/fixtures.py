import os
import pytest
from tests.utils.docker_utils import start_database_container
from sqlalchemy import create_engine
from dotenv import load_dotenv

from tests.utils.database_utils import migrate_to_db


@pytest.fixture(scope="session", autouse=True)
def db_session():
    load_dotenv()

    container = start_database_container()

    print(os.getenv("TEST_DATABASE_URL"))

    engine = create_engine(os.getenv("TEST_DATABASE_URL"))

    with engine.begin() as connection:
        migrate_to_db("migrations", "alembic.ini", connection)

    container.stop()
    container.remove()
