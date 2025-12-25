from sqlalchemy import select
from models import Subject


def test_create_subject(db_session):
    """Тест добавления предмета (CREATE операция)."""
    test_id = 99991

    subject = Subject(
        subject_id=test_id,
        subject_title="Программирование Python"
    )
    db_session.add(subject)
    db_session.commit()

    stmt = select(Subject).where(Subject.subject_id == test_id)
    result = db_session.execute(stmt)
    saved_subject = result.scalar_one_or_none()

    assert saved_subject is not None
    assert saved_subject.subject_title == "Программирование Python"
    assert saved_subject.subject_id == test_id


def test_update_subject(db_session):
    """Тест изменения предмета (UPDATE операция)."""
    test_id = 99992

    subject = Subject(
        subject_id=test_id,
        subject_title="Базы данных"
    )
    db_session.add(subject)
    db_session.commit()

    subject.subject_title = "Базы данных: PostgreSQL"
    db_session.commit()

    stmt = select(Subject).where(Subject.subject_id == test_id)
    result = db_session.execute(stmt)
    updated_subject = result.scalar_one()

    assert updated_subject.subject_title == "Базы данных: PostgreSQL"


def test_delete_subject(db_session):
    """Тест удаления предмета (DELETE операция)."""
    test_id = 99993

    subject = Subject(
        subject_id=test_id,
        subject_title="Тестирование ПО"
    )
    db_session.add(subject)
    db_session.commit()

    db_session.delete(subject)
    db_session.commit()

    stmt = select(Subject).where(Subject.subject_id == test_id)
    result = db_session.execute(stmt)
    deleted_subject = result.scalar_one_or_none()

    assert deleted_subject is None
