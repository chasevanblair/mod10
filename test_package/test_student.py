"""

Program: test_student.py

Author: Chase Van Blair

Last date modified: 7/7/20


The purpose of this program is to practice testing classes
by using the student class and checking everything works

"""
import unittest
from class_definitions.student import Student


class TestStudent(unittest.TestCase):
    def setUp(self):
        """
        create the TestStudent object
        :return:
        """
        self.student = Student(fname="dan", major="math", gpa=4.0, lname="bog")

    def tearDown(self):
        """
        delete the TestStudent object
        :return:
        """
        del self.student

    def test_object_created_required_attributes(self):
        """
        test that all required attributes have data
        :return:
        """
        self.assertEqual(self.student.first_name, "dan")
        self.assertEqual(self.student.last_name, "bog")
        self.assertEqual(self.student.major, "math")

    def test_object_created_all_attributes(self):
        """
        test that all attributes have data
        :return:
        """
        student2 = Student(fname="jeff", lname="smith", major="science", gpa=2.3)
        self.assertEqual(student2.first_name, "jeff")
        self.assertEqual(student2.last_name, "smith")
        self.assertEqual(student2.major, "science")
        self.assertEqual(student2.gpa, 2.3)

    def test_student_str(self):
        """
        test the return of ___str___ for Student
        :return:
        """
        self.assertEqual(self.student.__str__(), "bog, dan has major math with gpa: 4.0")

    def test_object_not_created_error_last_name(self):
        """
        test for a ValueError because last name has no data
        :return:
        """
        try:
            p = Student(fname="jeff", major="easy", gpa=1, lname="ssssssss")
        except ValueError:
            print("Error with last name")

    def test_object_not_created_error_first_name(self):
        """
        test for a Value error because first name has no data
        :return:
        """
        try:
            p = Student(fname="jeff", major="easy", gpa=1, lname="ssssssss")
        except ValueError:
            print("Error with first name")

    def test_object_not_created_error_major(self):
        """
        test for a Value error because major has no data
        :return:
        """
        try:
            p = Student(fname="jeff", major="easy", gpa=1, lname="ssssssss")
        except ValueError:
            print("Error with major")

    def test_object_not_created_error_gpa(self):
        """
        test for error because gpa isnt a float
        :return:
        """
        p = Student(fname="jeff", major="easy", gpa=1.1, lname="ssssssss")
        if not isinstance(p.gpa, float):
            print("Error with gpa")


