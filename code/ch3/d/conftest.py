from pathlib import Path
from tempfile import TemporaryDirectory

import pytest

import cards


def db_scope(fixture_name, config):
    if config.getoption("--func-db", None):
        return "function"
    return "session"


def pytest_addoption(parser):
    parser.addoption(
        "--func-db",
        action="store_true",
        default=False,
        help="new db for each test"
    )


@pytest.fixture(scope=db_scope)
def db():
    """CardsDB object connected to temporary database"""
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db_ = cards.CardsDB(db_path)
        yield db_
        db_.close()


@pytest.fixture(scope="function")
def cards_db(db):
    """CardsDB object that's empty"""
    db.delete_all()
    return db
