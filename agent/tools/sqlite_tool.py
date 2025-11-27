import sqlite3, re

class SQLiteTool:
    def __init__(self, db_path='data/northwind.sqlite'):
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row

    def execute(self, sql):
        cur = self.conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        cols = [c[0] for c in cur.description] if cur.description else []
        return [tuple(r) for r in rows], cols

    def infer_tables_from_sql(self, sql):
        candidates = ['Orders','Order Details','Products','Customers','Categories','Suppliers']
        return [c for c in candidates if re.search(r'\b'+re.escape(c)+r'\b', sql, re.I)]

    def introspect_schema(self):
        cur = self.conn.execute("SELECT name, sql FROM sqlite_master WHERE type='table'")
        return {r['name']: r['sql'] for r in cur.fetchall()}
