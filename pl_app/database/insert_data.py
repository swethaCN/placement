import pandas as pd
from db_connection import DatabaseConnection

class InsertData:
    def __init__(self):
        self.db = DatabaseConnection()
        self.db.connect()

    def insert_students(self):
        df = pd.read_csv("data/students.csv")
        df.to_sql("students", self.db.conn, if_exists="replace", index=False)

    def insert_programming(self):
        df = pd.read_csv("data/programming.csv")
        df.to_sql("programming", self.db.conn, if_exists="replace", index=False)

    def insert_soft_skills(self):
        df = pd.read_csv("data/soft_skills.csv")
        df.to_sql("soft_skills", self.db.conn, if_exists="replace", index=False)

    def insert_placements(self):
        df = pd.read_csv("data/placements.csv")
        df.to_sql("placements", self.db.conn, if_exists="replace", index=False)

    def run_all(self):
        self.insert_students()
        self.insert_programming()
        self.insert_soft_skills()
        self.insert_placements()
        print(" Data inserted into all tables")


if __name__ == "__main__":
    ins = InsertData()
    ins.run_all()