import requests


class YougileAPI:
    """Page Object для Yougile API v2"""

    def __init__(self, session: requests.Session):
        self.session = session

    def create_project(self, title: str, users: dict = None):
        """[POST] /api-v2/projects - Создание проекта"""
        url = f"{self.session.base_url}/projects"
        data = {"title": title}

        if users:
            data["users"] = users

        return self.session.post(url, json=data)

    def get_project(self, project_id: str):
        """[GET] /api-v2/projects/{id} - Получение проекта по ID"""
        url = f"{self.session.base_url}/projects/{project_id}"
        return self.session.get(url)

    def update_project(self, project_id: str, **kwargs):
        """[PUT] /api-v2/projects/{id} - Обновление проекта"""
        url = f"{self.session.base_url}/projects/{project_id}"
        return self.session.put(url, json=kwargs)
