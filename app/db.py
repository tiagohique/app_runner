import psycopg2
from psycopg2.extras import RealDictCursor

def get_db_connection(db_name, user, password, host, port):
    conn = psycopg2.connect(
        dbname=db_name,
        user=user,
        password=password,
        host=host,
        port=port,
        cursor_factory=RealDictCursor
    )
    return conn
