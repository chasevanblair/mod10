class Employee:
    """

Program: employee.py

Author: Chase Van Blair

Last date modified: 7/3/20


The purpose of this program is to show basic understanding of oop and encapsulation

"""


    # Constructor
    def __init__(self, lname, fname, address, phone_number, salaried, start_date, salary):
        self._last_name = lname
        self._first_name = fname
        self._address = address
        self._phone_number = phone_number
        self._salaried = bool(salaried)
        self._start_date = start_date
        self._salary = salary

    def set_last_name(self, lname):
        """
        sets last name from outside class
        :param lname: last name
        :return:
        """
        self._last_name = lname

    def set_first_name(self, fname):
        """
        sets first name from outside class
        :param fname: first name
        :return:
        """
        self._first_name = fname

    def display(self):
        """
        sets up the return with all data formatted for print
        :return:
        """
        money = ""
        if self._salaried:
            money = "Salaried employee: %s/hour\n" % self._salary
        else:
            money = "Hourly employee: %s/hour\n" % self._salary

        l1 = self._first_name + " " + self._last_name + "\n"
        l2 = self._address + "\n"
        l3 = money
        l4 = "Start date: " + self._start_date
        return l1 + l2 + l3 + l4

# Driver
emp = Employee('Ruiz', 'Matthew', "123 main st. town, IA", "1234651346", False, "1/23/33", "698999999999")  # call the construtor, needs to have a first and last name in parameter
emp.set_first_name('Matt')
print(emp.display())  # display returns a str, so print the information

del emp  # clean up!
