import mysql.connector
import pandas as pd


class Connector:
    def __init__(self,server="localhost",port=3306,
                 database="salesdatabase",
                 username="root",password="Maiquynh@210406"):
        self.server=server
        self.port=port
        self.database=database
        self.username=username
        self.password=password

    def connect(self):
        self.conn = mysql.connector.connect(
            host=self.server,
            port=self.port,
            database=self.database,
            user=self.username,
            password=self.password,
            use_pure=True
        )
        return self.conn

    def queryDataset(self, sql, val=None):
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql, val)
            return pd.DataFrame(
                cursor.fetchall(),
                columns=cursor.column_names
            )
        finally:
            cursor.close()

