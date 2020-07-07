"""

Program: student.py

Author: Chase Van Blair

Last date modified: 7/7/20


The purpose of this program is to create a basic class
to be used for testing

"""
class Student:
    """Student class"""

    def __init__(self, lname, fname, major, gpa=0.0):
        """
        Student constructor
        :param lname: student's last name
        :param fname: student's first name
        :param major: student's major
        :param gpa: student's gpa
        """
        if not lname or not fname or not major:
            print("input error")
        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

    def __str__(self):
        """
        outputs a readable version of Student
        :return:
        """
        return self.last_name + ", " + self.first_name + " has major " + self.major + " with gpa: " + str(self.gpa)

