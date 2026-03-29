# SPDX-License-Identifier: 0BSD
# Author: Makkhawan Sardlah

import sqlite3

class sqlite():
    def __enter__(self):
        self.connect(self.path)
        self.conn_cursor()
        return self
    def __init__(self, path):
        self.path = path
    def create_table(self, name, data):
        pull_data = ""
        m = 0
        for i, v in data.items():
            m += 1
            pull_data = f"{pull_data}{i} "
            pull_data = f"{pull_data}{v.get("type")} "
            if v.get("kay") == True:
                pull_data = f"{pull_data} PRIMARY KEY"
            if m != len(data):
                pull_data = pull_data + ", "
        self.cursor.execute(f'''CREATE TABLE IF NOT EXISTS {name} ({pull_data})''')
        self.conn.commit()
    def add_data(self, table, data):
        pull_data = ""
        m = 0
        for i in data:
            m += 1
            pull_data = f"{pull_data}{i} "
            if m != len(data):
                pull_data = pull_data + ", "
        self.cursor.execute(f'''INSERT INTO {table} VALUES ({pull_data});''')
        self.conn.commit()
    def show_data(self, table, limit):
        self.cursor.execute(f"SELECT * FROM {table} LIMIT {limit}")
        rows = self.cursor.fetchall()
        return rows
    def search_data(self, table, csql):
        self.cursor.execute(f"SELECT * FROM {table} WHERE {csql};")
        rows = self.cursor.fetchall()
        return rows
    def conn_cursor(self):
        self.cursor = self.conn.cursor()
    def connect(self, path):
        self.conn = sqlite3.connect(path)
    def unconnect(self):
        self.conn.close()
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.unconnect()

def build_db(targetpath, sqltype):
    if sqltype == "SQLite":
        return sqlite(targetpath)
    return None