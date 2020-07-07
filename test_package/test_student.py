import unittest
from class_definitions.student import Student


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student(fname="dan", major="math", gpa=4.0, lname="bog")

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.first_name, "dan")
        self.assertEqual(self.student.last_name, "bog")
        self.assertEqual(self.student.major, "math")

    def test_object_created_all_attributes(self):
        student2 = Student(fname="jeff", lname="smith", major="science", gpa=2.3)
        self.assertEqual(student2.first_name, "jeff")
        self.assertEqual(student2.last_name, "smith")
        self.assertEqual(student2.major, "science")
        self.assertEqual(student2.gpa, 2.3)

    def test_student_str(self):
        self.assertEqual(self.student.__str__(), "bog, dan has major math with gpa: 4.0")

    def test_object_not_created_error_last_name(self):
        try:
            p = Student(fname="jeff", major="easy", gpa=1, lname="ssssssss")
        except ValueError:
            print("Error with last name")

    def test_object_not_created_error_first_name(self):
        try:
            p = Student(fname="jeff", major="easy", gpa=1, lname="ssssssss")
        except ValueError:
            print("Error with first name")

    def test_object_not_created_error_major(self):
        try:
            p = Student(fname="jeff", major="easy", gpa=1, lname="ssssssss")
        except ValueError:
            print("Error with major")

    def test_object_not_created_error_gpa(self):
        p = Student(fname="jeff", major="easy", gpa=1, lname="ssssssss")
        if not isinstance(p.gpa, float):
            print("Error with gpa")


