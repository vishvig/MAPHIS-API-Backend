import psycopg2

from sqlalchemy import create_engine


from constants.configurations import PostgresDB


class PostgresDBUtil(object):
    def __init__(self):
        self.conn = psycopg2.connect(
            host=PostgresDB.host,
            database=PostgresDB.name,
            user=PostgresDB.user,
            password=PostgresDB.password
        )
        self._engine = create_engine(PostgresDB.conn_str)

    def execute(self, query):
        res = self.conn.execute(query)
        return res

    def engine(self):
        return self._engine
