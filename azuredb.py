import pyodbc
import os

class AzureSQLDatabase:
    def __init__(self, server=os.getenv('SERVER'),driver=os.getenv('DRIVER'), database=os.getenv('DATABASE'), username=os.getenv('USERNAME'), password=os.getenv('PASSWORD')):
        self.connection_string = f'Driver={driver};Server=tcp:{server},1433;Database={database};Uid={username};Pwd={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = pyodbc.connect(self.connection_string)
            self.cursor = self.conn.cursor()
        except pyodbc.Error as e:
            print(f"Error connecting to database: {e}")

    def execute_query(self, query,params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.conn.commit()
            print("Query executed successfully.")
            self.close()
        except pyodbc.Error as e:
            print(f"Error executing query: {e}")
            self.close()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        print("Connection closed.")

