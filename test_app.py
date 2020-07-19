import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from models import Students, Teachers, setup_db
from app import create_app
from models import db


class CoachingInstitutedatatest(unittest.TestCase):
    """This class represents the Coaching institute database test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = os.environ['DATABASE_URL']
        setup_db(self.app)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TEST CASES STARTS HERE
    """

    # TEST for successfully getting teachers
    def test_get_teachers(self):
        res = self.client().get("/teachers")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["Total number of teachers"] > 0)

    # #TEST for successfully getting students
    def test_get_students(self):
        res = self.client().get("/students")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["Total number of students"] > 0)

    # TEST post a new teacher details
    def test_post_new_teacherdetails(self):

        new_teacher = {
            'Name': 'Rohit Kumar',
            'age': 20,
        }

        res = self.client().post("/teachers", json=new_teacher)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['teacher added']) > 0)



    # TEST post a new student
    def test_post_new_student(self):

        new_student = {
            'name': 'Duke Stark',
            'age': 44,
            'gender': 'Male',
            'teacher_id': 2
        }

        res = self.client().post("/students", json=new_student)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['message'], "student added successfully")

    # TEST for 400 status code for missing gender of new student
    def test_400_new_student(self):

        new_student = {
            'name': 'Duke Stark',
            'age': '44',
            'teacher_id': 2
        }

        res = self.client().post("/students", json=new_student)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)


    # TEST for teacher not found while patching
    def test_400_teacher_not_present_for_patching(self):
        teacher_details = {
            'name': "Miliand",
            'age': "22"
        }

        res = self.client().patch("/teachers/5000", json=teacher_details)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)

    # TEST for change details of already present student
    def test_patch_student(self):

        patch_students = {
            'name': 'John Doe',
            'age': 24,
            'gender': 'Male',
            'teacher_id': 2
        }

        res = self.client().patch("/students/4", json=patch_students)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["message"], "update successfull")

    # TEST for student not found while patching
    def test_400_student_not_present_for_patching(self):
        patch_student = {
            'name': 'John Doe',
            'age': 24,
            'gender': 'Male',
            'teacher_id': 2
        }

        res = self.client().patch("/students/5000", json=patch_student)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)

    # TEST for deleting a specific student
    def test_delete_student(self):
        res = self.client().delete("/students/5")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)

    # TEST for getting 404 while deleting a specific student
    def test_404_delete_student(self):
        res = self.client().delete("/students/1000")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)

    # TEST for deleting a specific teacher

    def test_delete_teacher(self):
        res = self.client().delete("/teachers/9")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)

    # TEST for getting 404 while deleting a specific teacher
    def test_404_delete_teacher(self):
        res = self.client().delete("/teachers/1000")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
