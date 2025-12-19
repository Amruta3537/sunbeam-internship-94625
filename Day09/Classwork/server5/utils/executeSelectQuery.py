from utils.dbConnection import getDBConnection

def executeSelectQuery(query):
    connection = getDBConnection()
    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data