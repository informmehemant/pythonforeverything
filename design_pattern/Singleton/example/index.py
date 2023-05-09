import psycopg2


class DatabaseConnection:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.conn = psycopg2.connect(
                dbname="mydatabase",
                user="myuser",
                password="mypassword",
                host="localhost",
                port="5432"
            )
        return cls.__instance


db = DatabaseConnection()
cursor = db.conn.cursor()
cursor.execute("SELECT * FROM mytable")
results = cursor.fetchall()
