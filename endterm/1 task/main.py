import psycopg2
from psycopg2 import OperationalError
def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection

connection = create_connection(
 "shop_db", "postgres", "ROOT", "127.0.0.1", "5432"
)


def execute_query(connection,query):
    cursor = connection.cursor()
    result =None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except OperationalError as e:
        print(f"The error '{e}' occurred")
select_users ="SELECT * FROM blog WHERE title LIKE '%c%' AND intro LIKE '%oc%'"

users = execute_query(connection, select_users)
for user in users:
    print(user)