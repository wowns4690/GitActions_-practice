# test_client.py

import os
import psycopg2
import pytest

@pytest.fixture
def db_connection():
    connection = psycopg2.connect(
        host=os.environ.get('POSTGRES_HOST', 'localhost'),
        port=os.environ.get('POSTGRES_PORT', '5432'),
        user=os.environ.get('POSTGRES_USER', 'test_user'),
        password=os.environ.get('POSTGRES_PASSWORD', 'test_password'),
        database=os.environ.get('POSTGRES_DB', 'test_db')
    )
    yield connection
    connection.close()

def test_database_operations(db_connection):
    cursor = db_connection.cursor()

    # 테이블 생성
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL
        );
    """)
    db_connection.commit()

    # 데이터 삽입
    cursor.execute("INSERT INTO users (name) VALUES ('Alice');")
    db_connection.commit()

    # 테이블이 존재하는지 확인
    cursor.execute("""
        SELECT EXISTS (
            SELECT FROM information_schema.tables
            WHERE table_name = 'users'
        );
    """)
    exists = cursor.fetchone()[0]
    assert exists, "테이블이 존재하지 않습니다."

    # 데이터 조회
    cursor.execute("SELECT * FROM users;")
    users = cursor.fetchall()
    assert len(users) > 0, "사용자 데이터가 없습니다."
    assert users[0][1] == 'Alice', "사용자 이름이 일치하지 않습니다."

    cursor.close()
