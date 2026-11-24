import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from urllib.parse import quote_plus

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

#Выводим содержимое таблицы student
def test_select():
    with db.connect() as connection:
        result = connection.execute(text("SELECT * FROM student"))
        rows = result.all()
        print(rows)

#Добавляем запись в таблицу student: user_id 20002, level 'Beginner', education_form group, subject_id 1
def test_insert():
    with db.connect() as connection:
        with connection.begin() as transaction:
            sql = text(
                'INSERT INTO student ("user_id", "level", "education_form", "subject_id") '
                "VALUES (:user_id, :level, :education_form, :subject_id)"
            )
            connection.execute(
                sql,
                {"user_id": 20002, "level": "Beginner", "education_form": "group", "subject_id": 1},
            )
            transaction.commit()

#Обновляем данные записи в таблице users: student: user_id 20002, level 'Beginner', education_form group, subject_id 1
def test_update():
    with db.connect() as connection:
        with connection.begin() as transaction:
            sql = text(
                "UPDATE student SET level = :level WHERE user_id = :user_id"
            )
            connection.execute(sql, {"user_id": 20002, "level": "Elementary"})
            transaction.commit()

#Удаляем запись из таблицы student: user_id 20002, level 'Beginner', education_form group, subject_id 1
def test_delete():
    with db.connect() as connection:
        with connection.begin() as transaction:
            sql = text("DELETE FROM student WHERE user_id = :user_id")
            connection.execute(sql, {"user_id": 20002})
            transaction.commit()
