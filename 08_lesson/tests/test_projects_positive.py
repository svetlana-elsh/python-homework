from api.yougile_api import YougileAPI


def test_post_project_empty_title_fails(api_session):
    """[POST] Ошибка при пустом title"""
    api = YougileAPI(api_session)

    response = api.create_project(title="")

    assert response.status_code == 400
    assert "error" in response.json()


def test_get_nonexistent_project_fails(api_session):
    """[GET] Ошибка при несуществующем ID"""
    api = YougileAPI(api_session)

    fake_id = "00000000-0000-0000-0000-000000000000"
    response = api.get_project(fake_id)

    assert response.status_code == 404


def test_put_nonexistent_project_fails(api_session):
    """[PUT] Ошибка при обновлении несуществующего проекта"""
    api = YougileAPI(api_session)

    fake_id = "00000000-0000-0000-0000-000000000000"
    response = api.update_project(fake_id, title="Новое название")

    assert response.status_code == 404
