from database.db_connection import DatabaseConnection


class Queries:
    def __init__(self):
        self.db = DatabaseConnection()
        self.db.connect()

    # 1️⃣ Top 5 Students Ready for Placement
    def top_5_students(self):
        query = """
        SELECT s.name, p.problems_solved, pl.mock_interview_score
        FROM students s
        JOIN programming p ON s.student_id = p.student_id
        JOIN placements pl ON s.student_id = pl.student_id
        WHERE pl.placement_status = 'Ready'
        ORDER BY p.problems_solved DESC, pl.mock_interview_score DESC
        LIMIT 5
        """
        return self.db.fetchall(query)

    # 2️⃣ Average Programming Performance per Batch
    def avg_programming_by_batch(self):
        query = """
        SELECT s.course_batch, AVG(p.problems_solved)
        FROM students s
        JOIN programming p ON s.student_id = p.student_id
        GROUP BY s.course_batch
        """
        return self.db.fetchall(query)

    # 3️⃣ Soft Skills Average Distribution
    def soft_skills_distribution(self):
        query = """
        SELECT 
            AVG(communication),
            AVG(teamwork),
            AVG(presentation),
            AVG(leadership),
            AVG(critical_thinking),
            AVG(interpersonal_skills)
        FROM soft_skills
        """
        return self.db.fetchall(query)

    # 4️⃣ Placement Status Count
    def placement_status_count(self):
        query = """
        SELECT placement_status, COUNT(*)
        FROM placements
        GROUP BY placement_status
        """
        return self.db.fetchall(query)

    # 5️⃣ Students with Internships > 1
    def students_with_internships(self):
        query = """
        SELECT s.name, pl.internships_completed
        FROM students s
        JOIN placements pl ON s.student_id = pl.student_id
        WHERE pl.internships_completed > 1
        """
        return self.db.fetchall(query)

    # 6️⃣ High Soft Skills (>80)
    def high_soft_skills(self):
        query = """
        SELECT s.name, ss.communication, ss.teamwork
        FROM students s
        JOIN soft_skills ss ON s.student_id = ss.student_id
        WHERE ss.communication > 80 AND ss.teamwork > 80
        """
        return self.db.fetchall(query)

    # 7️⃣ Low Coding but High Soft Skills
    def low_coding_high_soft(self):
        query = """
        SELECT s.name, p.problems_solved, ss.communication
        FROM students s
        JOIN programming p ON s.student_id = p.student_id
        JOIN soft_skills ss ON s.student_id = ss.student_id
        WHERE p.problems_solved < 50 AND ss.communication > 80
        """
        return self.db.fetchall(query)

    # 8️⃣ Average Interview Score
    def avg_mock_interview_score(self):
        query = """
        SELECT AVG(mock_interview_score)
        FROM placements
        """
        return self.db.fetchall(query)

    # 9️⃣ Students Placed with High Package (>10 LPA approx)
    def high_package_students(self):
        query = """
        SELECT s.name, pl.placement_package
        FROM students s
        JOIN placements pl ON s.student_id = pl.student_id
        WHERE pl.placement_package > 1000000
        """
        return self.db.fetchall(query)

    # 🔟 Top Performers (Coding + Interview)
    def top_performers(self):
        query = """
        SELECT s.name, p.problems_solved, pl.mock_interview_score
        FROM students s
        JOIN programming p ON s.student_id = p.student_id
        JOIN placements pl ON s.student_id = pl.student_id
        ORDER BY p.problems_solved DESC, pl.mock_interview_score DESC
        LIMIT 10
        """
        return self.db.fetchall(query)


# 🧪 TEST BLOCK
if __name__ == "__main__":
    q = Queries()

    print("\n1️⃣ Top 5 Students:")
    print(q.top_5_students())

    print("\n2️⃣ Avg Programming by Batch:")
    print(q.avg_programming_by_batch())

    print("\n3️⃣ Soft Skills Distribution:")
    print(q.soft_skills_distribution())

    print("\n4️⃣ Placement Status Count:")
    print(q.placement_status_count())

    print("\n5️⃣ Students with Internships > 1:")
    print(q.students_with_internships())

    print("\n6️⃣ High Soft Skills:")
    print(q.high_soft_skills())

    print("\n7️⃣ Low Coding + High Soft Skills:")
    print(q.low_coding_high_soft())

    print("\n8️⃣ Avg Interview Score:")
    print(q.avg_mock_interview_score())

    print("\n9️⃣ High Package Students:")
    print(q.high_package_students())

    print("\n🔟 Top Performers:")
    print(q.top_performers())