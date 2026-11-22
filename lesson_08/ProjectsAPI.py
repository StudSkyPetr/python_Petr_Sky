import pytest
import requests


class ProjectsAPI:
    def __init__(self, url, login, password, company_id):
        self.url = url.rstrip('/')
        self.login = login
        self.password = password
        self.company_id = company_id
        self._token = None

    def _get_token(self):
#        Получает существующий ключ или создаёт новый
        if self._token is None:
            creds = {
                "login": self.login,
                "password": self.password,
                "companyId": self.company_id,
            }

            # пробуем получить существующие ключи
            resp = requests.post(f"{self.url}/api-v2/auth/keys/get", json=creds)
            resp.raise_for_status()
            keys = resp.json()

            if keys:
                self._token = keys[0]["key"]
            else:
                # ключей нет — создаём новый
                resp = requests.post(f"{self.url}/api-v2/auth/keys", json=creds)
                resp.raise_for_status()
                self._token = resp.json()["key"]
        return self._token

    def _headers(self):
        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self._get_token()}",
        }

    def create_project(self, title):
        resp = requests.post(
            f"{self.url}/api-v2/projects",
            json={"title": title},
            headers=self._headers(),
        )
        resp.raise_for_status()
        return resp.json()["id"]

    def create_project_response(self, title):
        resp = requests.post(
            f"{self.url}/api-v2/projects",
            json={"title": title},
            headers=self._headers(),
        )
        return resp

    def delete_project(self, project_id_for_del):
#        Удаляет проект (YouGile удаляет через PUT с флагом deleted)
        resp = requests.put(
            f"{self.url}/api-v2/projects/{project_id_for_del}",
            json={"deleted": True},
            headers=self._headers(),
        )
        resp.raise_for_status()
        return resp

    def update_project(self, project_id, new_title):
        resp = requests.put(
            f"{self.url}/api-v2/projects/{project_id}",
            json={"title": new_title},
            headers=self._headers(),
        )
        resp.raise_for_status()
        return resp.json()["id"]


    def update_project_response(self, project_id, new_title):
        resp = requests.put(
            f"{self.url}/api-v2/projects/{project_id}",
            json={"title": new_title},
            headers=self._headers(),
        )
        return resp

    def get_project_by_id(self, project_id):
        resp = requests.get(
            f"{self.url}/api-v2/projects/{project_id}",
            headers=self._headers(),
        )
        resp.raise_for_status()
        return resp.json()

    def get_project_by_id_response(self, project_id):
        resp = requests.get(
            f"{self.url}/api-v2/projects/{project_id}",
            headers=self._headers(),
        )
        return resp
