import os
import pytest
import requests
from dotenv import load_dotenv

# Загружаем переменные из .env файла
load_dotenv()


@pytest.fixture(scope="session")
def api_session():
    """Создает авторизованную сессию для всех тестов."""
    # Читаем API ключ из .env файла
    api_key = os.getenv("YOUGILE_API_KEY")

    if not api_key:
        pytest.skip(
            "Создайте файл .env в папке 08_lesson\n"
            "с содержимым: YOUGILE_API_KEY=ваш_ключ"
        )

    # Базовый URL (общий для всех методов)
    base_url = "https://ru.yougile.com/api-v2"

    session = requests.Session()
    session.headers.update({
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    })
    session.base_url = base_url

    yield session

    session.close()


@pytest.fixture
def cleanup_project_ids():
    """Собирает ID созданных проектов для очистки."""
    ids = []
    yield ids

    # После тестов помечаем проекты как удаленные
    if not ids:
        return

    api_key = os.getenv("YOUGILE_API_KEY")
    if not api_key:
        return

    base_url = "https://ru.yougile.com/api-v2"

    session = requests.Session()
    session.headers.update({
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    })

    for project_id in ids:
        try:
            url = f"{base_url}/projects/{project_id}"
            session.put(url, json={"deleted": True})
        except Exception:
            # Игнорируем ошибки при удалении
            pass
