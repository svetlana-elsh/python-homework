import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from database import Base, DATABASE_URL, get_database_name


def pytest_configure(config):
    """Проверяем, что тесты запускаются на правильной БД."""
    db_name = get_database_name()

    if db_name.lower() != "qa":
        raise RuntimeError(
            f"ОПАСНО! Тесты запущены на БД '{db_name}', "
            f"а не на 'QA'. Измените DATABASE_URL!"
        )
    print(f"✓ Тесты запускаются на БД: {db_name}")


@pytest.fixture(scope="session")
def engine():
    """Создает движок подключения к БД."""
    engine = create_engine(DATABASE_URL, echo=False)

    Base.metadata.create_all(bind=engine)

    yield engine
    engine.dispose()


@pytest.fixture(scope="function")
def db_session(engine):
    """Создает сессию для каждого теста с автооткатом."""
    Session = sessionmaker(bind=engine)
    session = Session()

    session.begin()

    yield session

    session.rollback()
    session.close()


@pytest.fixture(scope="function", autouse=True)
def cleanup_test_data(db_session):
    """Автоматически очищает тестовые данные после каждого теста."""
    yield

    try:
        db_session.execute(text("""
            DELETE FROM subject
            WHERE subject_id >= 99990
        """))
        db_session.commit()
    except Exception:
        db_session.rollback()
