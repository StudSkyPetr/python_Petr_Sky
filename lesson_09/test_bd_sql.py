import os
from urllib.parse import quote_plus

import pytest
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST", "localhost")
port = os.getenv("DB_PORT", "5432")
db_name = os.getenv("DB_NAME")

db_connection_string = (
    f"postgresql://{user}:{quote_plus(password)}@{host}:{port}/{db_name}"
)
db = create_engine(db_connection_string)

TEST_USER_ID = 20002
STUDENT_DATA = {
    "user_id": TEST_USER_ID,
    "level": "Beginner",
    "education_form": "group",
    "subject_id": 1,
}


@pytest.fixture()
def test_student():
    """Добавляет тестового студента перед тестом и удаляет после."""
    with db.connect() as connection:
        # чистим старую запись, если осталась с прошлого запуска
        with connection.begin():
            connection.execute(
                text("DELETE FROM student WHERE user_id = :user_id"),
                {"user_id": TEST_USER_ID},
            )

        # добавляем свежую запись
        with connection.begin():
            connection.execute(
                text(
                    'INSERT INTO student ('
                    '"user_id", "level", "education_form", "subject_id") '
                    "VALUES (:user_id, :level, :education_form, :subject_id)"
                ),
                STUDENT_DATA,
            )

        yield

        # убираем за собой после теста
        with connection.begin():
            connection.execute(
                text("DELETE FROM student WHERE user_id = :user_id"),
                {"user_id": TEST_USER_ID},
            )


def test_select():
    # Выводим содержимое таблицы student целиком
    with db.connect() as connection:
        result = connection.execute(text("SELECT * FROM student"))
        rows = result.all()
        print(rows)


def test_select_upd(test_student):
    # Выводим содержимое только что созданного поля таблицы
    with db.connect() as connection:
        result = connection.execute(
            text("SELECT * FROM student WHERE user_id = :user_id"),
            {"user_id": TEST_USER_ID},
        )
        rows = result.all()
        print(rows)
        assert len(rows) == 1


def test_insert():
    """Добавляем запись в таблицу student: user_id 20002,
    level 'Beginner', education_form group, subject_id 1"""
    with db.connect() as connection:
        with connection.begin() as transaction:
            sql = text(
                'INSERT INTO student ('
                '"user_id", "level", "education_form", "subject_id") '
                "VALUES (:user_id, :level, :education_form, :subject_id)"
            )
            connection.execute(
                sql,
                {"user_id": 20002, "level": "Beginner",
                 "education_form": "group", "subject_id": 1},
            )
            transaction.commit()
        with db.connect() as connection:
            # Проверка, что запись создана
            resultat = connection.execute(
                text("SELECT * FROM student WHERE user_id = :user_id"),
                {"user_id": TEST_USER_ID},
            )
            rows = resultat.all()
            print(rows)
            assert len(rows) == 1


def test_update_upd(test_student):
    """Обновляем данные записи в таблице users: student: user_id 20002,
    level 'Beginner', education_form group, subject_id 1"""
    with db.connect() as connection:
        with connection.begin():
            connection.execute(
                text("UPDATE student SET level = :level"
                     " WHERE user_id = :user_id"),
                {"user_id": TEST_USER_ID, "level": "Elementary"},
            )

    # проверяем, что обновление применилось
    with db.connect() as connection:
        result = connection.execute(
            text("SELECT level FROM student WHERE user_id = :user_id"),
            {"user_id": TEST_USER_ID},
        )
        assert result.scalar() == "Elementary"


def test_delete(test_student):
    # Удаляем запись из таблицы student: user_id 20002
    # фикстура гарантирует, что запись есть перед тестом
    with db.connect() as connection:
        # Сначала удаляем
        connection.execute(
            text("DELETE FROM student WHERE user_id = :user_id"),
            {"user_id": TEST_USER_ID},
        )
        # Теперь проверяем: пытаемся получить user_id этой записи
        result = connection.scalar(
            text("SELECT user_id FROM student WHERE user_id = :user_id"),
            {"user_id": TEST_USER_ID},
        )
        # Если запись удалена, result будет None.
        # Если осталась — будет число (20002)
        assert result is None, f"Запись с user_id={TEST_USER_ID} не удалена!"
