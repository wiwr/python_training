import pytest
import psycopg2

@pytest.fixture(scope="module")
def db_connection():
    db_host = "127.0.0.1"
    db_name = "testing"
    db_user = "student"
    db_password = "student"
    
    connection = psycopg2.connect(
        host = db_host,
        database=db_name,
        user=db_user,
        password=db_password
    )
    
    yield connection
    connection.close()