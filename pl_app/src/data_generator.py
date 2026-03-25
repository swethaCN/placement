from faker import Faker
import pandas as pd
import random
import os

fake = Faker()

NUM_STUDENTS = 500

# create data folder if not exists
os.makedirs("data", exist_ok=True)

students = []
programming = []
soft_skills = []
placements = []

for i in range(1, NUM_STUDENTS + 1):

    students.append({
        "student_id": i,
        "name": fake.name(),
        "age": random.randint(18, 25),
        "gender": random.choice(["Male", "Female"]),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "enrollment_year": random.randint(2019, 2023),
        "course_batch": random.choice(["Batch A", "Batch B", "Batch C", "Batch D"]),
        "city": fake.city(),
        "graduation_year": random.randint(2023, 2026)
    })

    programming.append({
        "programming_id": i,
        "student_id": i,
        "language": random.choice(["Python", "SQL"]),
        "problems_solved": random.randint(10, 300),
        "assessments_completed": random.randint(1, 20),
        "mini_projects": random.randint(0, 10),
        "certifications_earned": random.randint(0, 5),
        "latest_project_score": random.randint(40, 100)
    })

    soft_skills.append({
        "soft_skill_id": i,
        "student_id": i,
        "communication": random.randint(40, 100),
        "teamwork": random.randint(40, 100),
        "presentation": random.randint(40, 100),
        "leadership": random.randint(40, 100),
        "critical_thinking": random.randint(40, 100),
        "interpersonal_skills": random.randint(40, 100)
    })

    placements.append({
        "placement_id": i,
        "student_id": i,
        "mock_interview_score": random.randint(40, 100),
        "internships_completed": random.randint(0, 3),
        "placement_status": random.choice(["Ready", "Not Ready", "Placed"]),
        "company_name": fake.company(),
        "placement_package": random.randint(3, 20) * 100000,
        "interview_rounds_cleared": random.randint(0, 5),
        "placement_date": fake.date()
    })

# save files
pd.DataFrame(students).to_csv("data/students.csv", index=False)
pd.DataFrame(programming).to_csv("data/programming.csv", index=False)
pd.DataFrame(soft_skills).to_csv("data/soft_skills.csv", index=False)
pd.DataFrame(placements).to_csv("data/placements.csv", index=False)

print("✅ Data generated successfully")