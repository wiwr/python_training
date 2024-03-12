'''
Created on Mar 11, 2024

@author: witek
'''
def test_database_connection(db_connection):
    assert db_connection is not None
    
    cursor = db_connection.cursor()
    cursor.execute("SELECT 1")
    result = cursor.fetchone()
    
    assert result == (1,)
    
    