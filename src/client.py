# client.py

import os
import psycopg2

def main():
    """PostgreSQL 데이터베이스에 연결하여 간단한 CRUD 작업을 수행합니다."""
    try:
        # 환경 변수에서 데이터베이스 연결 정보 가져오기
        connection = psycopg2.connect(
            host=os.environ.get('POSTGRES_HOST', 'localhost'),
            port=os.environ.get('POSTGRES_PORT', '5432'),
            user=os.environ.get('POSTGRES_USER', 'test_user'),
            password=os.environ.get('POSTGRES_PASSWORD', 'test_password'),
            database=os.environ.get('POSTGRES_DB', 'test_db')
        )
        cursor = connection.cursor()

        # 테이블 생성
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL
            );
        """)
        connection.commit()

        # 데이터 삽입
        cursor.execute("INSERT INTO users (name) VALUES (%s);", ('Alice',))
        connection.commit()

        # 데이터 조회
        cursor.execute("SELECT * FROM users;")
        users = cursor.fetchall()
        print("Users in database:", users)

    except Exception as e:
        print("데이터베이스 작업 중 오류 발생:", e)
    finally:
        if connection:
            cursor.close()
            connection.close()

if __name__ == "__main__":
    main()
