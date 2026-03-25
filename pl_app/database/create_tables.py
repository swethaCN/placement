from db_connection import DatabaseConnection

class CreateTables:
    def __init__(self):
        self.db = DatabaseConnection()
        self.db.connect()

    def create_students(self):
        self.db.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            gender TEXT,
            email TEXT,
            phone TEXT,
            enrollment_year INTEGER,
            course_batch TEXT,
            city TEXT,
            graduation_year INTEGER
        )
        """)

    def create_programming(self):
        self.db.execute("""
        CREATE TABLE IF NOT EXISTS programming (
            programming_id INTEGER PRIMARY KEY,
            student_id INTEGER,
            language TEXT,
            problems_solved INTEGER,
            assessments_completed INTEGER,
            mini_projects INTEGER,
            certifications_earned INTEGER,
            latest_project_score INTEGER,
            FOREIGN KEY(student_id) REFERENCES students(student_id)
        )
        """)

    def create_soft_skills(self):
        self.db.execute("""
        CREATE TABLE IF NOT EXISTS soft_skills (
            soft_skill_id INTEGER PRIMARY KEY,
            student_id INTEGER,
            communication INTEGER,
            teamwork INTEGER,
            presentation INTEGER,
            leadership INTEGER,
            critical_thinking INTEGER,
            interpersonal_skills INTEGER,
            FOREIGN KEY(student_id) REFERENCES students(student_id)
        )
        """)

    def create_placements(self):
        self.db.execute("""
        CREATE TABLE IF NOT EXISTS placements (
            placement_id INTEGER PRIMARY KEY,
            student_id INTEGER,
            mock_interview_score INTEGER,
            internships_completed INTEGER,
            placement_status TEXT,
            company_name TEXT,
            placement_package INTEGER,
            interview_rounds_cleared INTEGER,
            placement_date TEXT,
            FOREIGN KEY(student_id) REFERENCES students(student_id)
        )
        """)

    def run_all(self):
        self.create_students()
        self.create_programming()
        self.create_soft_skills()
        self.create_placements()
        print("✅ All tables created")


if __name__ == "__main__":
    ct = CreateTables()
    ct.run_all()