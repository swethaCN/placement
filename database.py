# database.py
import sqlite3

class PlacementDatabase:
    def __init__(self, db_path="placement_eligibility.db"):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()

    def get_top_5_placement_ready(self):
        self.cursor.execute('''
            SELECT s.name, p.company_name, p.placement_package, p.mock_interview_score
            FROM Students s
            JOIN Placements p ON s.student_id = p.student_id
            WHERE p.placement_status = 'Placed'
            ORDER BY p.placement_package DESC
            LIMIT 5
        ''')
        return self.cursor.fetchall()

    def average_programming_per_batch(self):
        self.cursor.execute('''
            SELECT s.course_batch, AVG(pr.problems_solved), AVG(pr.assessments_completed), AVG(pr.latest_project_score)
            FROM Students s
            JOIN Programming pr ON s.student_id = pr.student_id
            GROUP BY s.course_batch
        ''')
        return self.cursor.fetchall()

    def students_with_high_mock_scores(self, threshold=80):
        self.cursor.execute('''
            SELECT s.name, p.mock_interview_score
            FROM Students s
            JOIN Placements p ON s.student_id = p.student_id
            WHERE p.mock_interview_score > ?
        ''', (threshold,))
        return self.cursor.fetchall()

    def students_with_min_internships(self, min_count=2):
        self.cursor.execute('''
            SELECT s.name, p.internships_completed
            FROM Students s
            JOIN Placements p ON s.student_id = p.student_id
            WHERE p.internships_completed >= ?
        ''', (min_count,))
        return self.cursor.fetchall()

    def students_placed_in_company(self, company_name):
        self.cursor.execute('''
            SELECT s.name, p.company_name, p.placement_package
            FROM Students s
            JOIN Placements p ON s.student_id = p.student_id
            WHERE p.company_name = ?
        ''', (company_name,))
        return self.cursor.fetchall()

    def students_with_strong_soft_skills(self, score_threshold=75):
        self.cursor.execute('''
            SELECT s.name, ss.communication, ss.teamwork, ss.leadership
            FROM Students s
            JOIN SoftSkills ss ON s.student_id = ss.student_id
            WHERE ss.communication > ? AND ss.teamwork > ? AND ss.leadership > ?
        ''', (score_threshold, score_threshold, score_threshold))
        return self.cursor.fetchall()

    def students_ready_but_not_placed(self):
        self.cursor.execute('''
            SELECT s.name, p.placement_status
            FROM Students s
            JOIN Placements p ON s.student_id = p.student_id
            WHERE p.placement_status = 'Ready'
        ''')
        return self.cursor.fetchall()

    def strong_programmers(self, min_problems=200, min_certs=2):
        self.cursor.execute('''
            SELECT s.name, pr.problems_solved, pr.certifications_earned
            FROM Students s
            JOIN Programming pr ON s.student_id = pr.student_id
            WHERE pr.problems_solved > ? AND pr.certifications_earned > ?
        ''', (min_problems, min_certs))
        return self.cursor.fetchall()

    def students_cleared_multiple_interviews(self, min_rounds=3):
        self.cursor.execute('''
            SELECT s.name, p.interview_rounds_cleared, p.company_name
            FROM Students s
            JOIN Placements p ON s.student_id = p.student_id
            WHERE p.placement_status = 'Placed' AND p.interview_rounds_cleared > ?
        ''', (min_rounds,))
        return self.cursor.fetchall()

    def graduating_unplaced_students(self, year):
        self.cursor.execute('''
            SELECT s.name, s.graduation_year, p.placement_status
            FROM Students s
            JOIN Placements p ON s.student_id = p.student_id
            WHERE s.graduation_year = ? AND p.placement_status != 'Placed'
        ''', (year,))
        return self.cursor.fetchall()

    def students_with_many_projects(self, min_projects=3):
        self.cursor.execute('''
            SELECT s.name, pr.mini_projects
            FROM Students s
            JOIN Programming pr ON s.student_id = pr.student_id
            WHERE pr.mini_projects >= ?
        ''', (min_projects,))
        return self.cursor.fetchall()

    def students_from_city_with_high_score(self, city_name="Hyderabad", min_score=85):
        self.cursor.execute('''
            SELECT s.name, s.city, p.mock_interview_score
            FROM Students s
            JOIN Placements p ON s.student_id = p.student_id
            WHERE s.city = ? AND p.mock_interview_score >= ?
        ''', (city_name, min_score))
        return self.cursor.fetchall()

    def top_certified_students(self):
        self.cursor.execute('''
            SELECT s.name, pr.certifications_earned
            FROM Students s
            JOIN Programming pr ON s.student_id = pr.student_id
            ORDER BY pr.certifications_earned DESC
            LIMIT 5
        ''')
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()
