import os
import pytest
from datetime import datetime
from dotenv import load_dotenv
from ProjectsAPI import ProjectsAPI
load_dotenv()


@pytest.fixture(scope="session")
def api():
    return ProjectsAPI(
        url="https://ru.yougile.com",
        login=os.getenv("my_login"),
        password=os.getenv("my_password"),
        company_id=os.getenv("company_id"),
    )

@pytest.fixture
def created_project(api):
#    Создаёт проект для теста и отдаёт его ID
    project_id = api.create_project("Тестовый проект")
    yield project_id
    project_id_for_del = project_id
    return project_id_for_del
    # если у API есть удаление — добавить api.delete_project(project_id)

def test_delete_project(api):
    project_id = api.create_project("Проект на удаление")
    resp = api.delete_project(project_id)
    assert resp.status_code == 200, f"Ответ: {resp.status_code} {resp.text}"
    # главный признак: проект получен и помечен как удалённый
    project = api.get_project_by_id(project_id)
    assert project.get("deleted") is True, f"Проект не помечен удалённым: {project}"


# Проверка создания проекта
def test_create_project(api):
    project_id = api.create_project("Новый проект")
    assert project_id is not None
    # созданный проект реально существует
    project = api.get_project_by_id(project_id)
    assert project["id"] == project_id

#Пробуем создавать проект с Пустым названием (негативный тест)
def test_create_project_negative_empty_title(api):
    resp = api.create_project_response("")
    assert resp.status_code == 400, f"Ожидался статус 400, но получен {resp.status_code}"
    data = resp.json()
    """ Проверяем, что в сообщении есть намёк на проблему с title 
    (название не должно быть пустым)"""
    assert "title should not be empty" in data.get("message", [])
    assert data.get("error") == "Bad Request"

# Проверка изменения проекта
def test_update_project(api, created_project):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_title = f"Изменённый проект + {timestamp} "
    api.update_project(created_project, new_title)

    project = api.get_project_by_id(created_project)
    assert project["title"] == new_title

def test_update_project_negative_empty_title(api):
    """Обновление существующего проекта пустым названием — ожидаем 400."""
    project_id = api.create_project("Проект для негативного теста")

    resp = api.update_project_response(project_id, "")

    assert resp.status_code == 400, f"Ожидали 400, получили {resp.status_code}: {resp.text}"
    assert "title should not be empty" in resp.json().get("message", [])

def test_update_project_negative_unknown_id(api):
    """Обновление несуществующего проекта — ожидаем 404."""
    fake_id = "00000000-0000-0000-0000-000000000000"

    resp = api.update_project_response(fake_id, "Новое название")

    assert resp.status_code == 404, f"Ожидали 404, получили {resp.status_code}: {resp.text}"


# Проверка получения проекта по ID
def test_get_project_id(api, created_project):
    found_project = api.get_project_by_id(created_project)
    assert found_project["id"] == created_project

def test_get_project_by_id_negative_unknown_id(api):
    """Получение несуществующего проекта — ожидаем 404."""
    fake_id = "00000000-0000-0000-0000-000000000000"

    resp = api.get_project_by_id_response(fake_id)

    assert resp.status_code == 404, f"Ожидали 404, получили {resp.status_code}: {resp.text}"
