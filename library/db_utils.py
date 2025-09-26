import mysql.connector
import json

def get_db_connection():
    """
    db_config: dict (host, port, user, password, database)
    return: mysql.connector connection object
    """


    with open("config.json") as f:
        config = json.load(f)

    db_config = config['database']
    conn = mysql.connector.connect(**db_config)
    return conn
