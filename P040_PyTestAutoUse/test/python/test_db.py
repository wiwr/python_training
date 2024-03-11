'''
Created on Mar 11, 2024

@author: witek
'''
import pytest
import psycopg2

@pytest.fixture(scope="module", autouse=True)
def db_data():
    db_host = "127.0.0.1"
    db_name ="testing"
    db_user = "student"
    db_password = "student"
    
    connection = psycopg2.connect(
        host=db_host,
        database=db_name,
        user=db_user,
        password=db_password
    )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM example")
    result=cursor.fetchall()
    cursor.close()
    connection.close()
    return result

def test_database_data(db_data):
    assert db_data is not None
    assert len(db_data) > 0
    for row in db_data:
        assert isinstance(row, tuple)