# generate_data.py
import sqlite3
from faker import Faker
import random

fake = Faker()

conn = sqlite3.connect("placement_eligibility.db")
cursor = conn.cursor()

# Drop tables if they exist
cursor.executescript('''
DROP TABLE IF EXISTS Students;
DROP TABLE IF EXISTS Programming;
DROP TABLE IF EXISTS SoftSkills;
DROP TABLE IF EXISTS Placements;
''')

# Create tables
cursor.execute('''
CREATE TABLE Students (
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
''')

cursor.execute('''
CREATE TABLE Programming (
    programming_id INTEGER PRIMARY KEY,
    student_id INTEGER,
    language TEXT,
    problems_solved INTEGER,
    assessments_completed INTEGER,
    mini_projects INTEGER,
    certifications_earned INTEGER,
    latest_project_score REAL,
    FOREIGN KEY(student_id) REFERENCES Students(student_id)
)
''')

cursor.execute('''
CREATE TABLE SoftSkills (
    soft_skill_id INTEGER PRIMARY KEY,
    student_id INTEGER,
    communication INTEGER,
    teamwork INTEGER,
    presentation INTEGER,
    leadership INTEGER,
    critical_thinking INTEGER,
    interpersonal_skills INTEGER,
    FOREIGN KEY(student_id) REFERENCES Students(student_id)
)
''')

cursor.execute('''
CREATE TABLE Placements (
    placement_id INTEGER PRIMARY KEY,
    student_id INTEGER,
    mock_interview_score INTEGER,
    internships_completed INTEGER,
    placement_status TEXT,
    company_name TEXT,
    placement_package REAL,
    interview_rounds_cleared INTEGER,
    placement_date TEXT,
    FOREIGN KEY(student_id) REFERENCES Students(student_id)
)
''')

batches = ["Batch A", "Batch B", "Batch C", "Batch D"]
genders = ["Male", "Female", "Other"]
languages = ["Python", "Java", "C++", "SQL"]
status_options = ["Ready", "Placed", "Not Ready"]
companies = ["Infosys", "TCS", "Wipro", "Accenture", "Capgemini", None]

for i in range(500):
    name = fake.name()
    age = random.randint(20, 25)
    gender = random.choice(genders)
    email = fake.email()
    phone = fake.phone_number()
    enrollment_year = random.randint(2019, 2022)
    course_batch = random.choice(batches)
    city = fake.city()
    graduation_year = enrollment_year + 4

    cursor.execute('''
        INSERT INTO Students (name, age, gender, email, phone, enrollment_year, course_batch, city, graduation_year)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (name, age, gender, email, phone, enrollment_year, course_batch, city, graduation_year))

    student_id = cursor.lastrowid

    cursor.execute('''
        INSERT INTO Programming (student_id, language, problems_solved, assessments_completed, mini_projects, certifications_earned, latest_project_score)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        student_id,
        random.choice(languages),
        random.randint(50, 500),
        random.randint(1, 10),
        random.randint(0, 5),
        random.randint(0, 5),
        round(random.uniform(50, 100), 2)
    ))

    cursor.execute('''
        INSERT INTO SoftSkills (student_id, communication, teamwork, presentation, leadership, critical_thinking, interpersonal_skills)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        student_id,
        random.randint(40, 100),
        random.randint(40, 100),
        random.randint(40, 100),
        random.randint(40, 100),
        random.randint(40, 100),
        random.randint(40, 100)
    ))

    placed = random.choice([True, False])
    placement_status = "Placed" if placed else random.choice(["Ready", "Not Ready"])
    company = random.choice(companies) if placed else None
    package = round(random.uniform(3, 15), 2) if placed else None
    placement_date = fake.date_this_decade().isoformat() if placed else None

    cursor.execute('''
        INSERT INTO Placements (student_id, mock_interview_score, internships_completed, placement_status, company_name, placement_package, interview_rounds_cleared, placement_date)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        student_id,
        random.randint(40, 100),
        random.randint(0, 4),
        placement_status,
        company,
        package,
        random.randint(1, 5),
        placement_date
    ))

conn.commit()
conn.close()
print("Database and data generation complete.")
