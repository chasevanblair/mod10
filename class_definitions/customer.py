class Customer:
    """

    Program: customer.py

    Author: Chase Van Blair

    Last date modified: 7/5/20


    The purpose of this program is to get used to making classes
    and overriding built in functions

    """

    def __init__(self, id, lname, fname, phone, address):
        """
        constructor for the Customer object
        :param id: Id of customer
        :param lname: Last name of customer
        :param fname: first name of customer
        :param phone: phone number of customer
        :param address: address of customer
        """
        if not isinstance(id, int):
            raise AttributeError
        self.customer_id = str(id)
        self.last_name = lname
        self.first_name = fname
        self.phone_number = str(phone)
        self.address = address

    def __str__(self):
        """
        makes a string output of the data in Customer object
        :return: string of data
        """
        return ("ID: %s, Name: %s %s, Phone #: %s, Address: %s" % (self.customer_id, self.first_name, self.last_name,
                                                                   self.phone_number, self.address))

    def __repr__(self):
        """
        the str method but returns the variable value of the string not just a straight string
        :return: variable of string output
        """
        return ("ID: %s, Name: %s %s, Phone #: %s, Address: %s" % (self.customer_id, self.first_name, self.last_name,
                                                                   self.phone_number, self.address))

    def display(self):
        """
        prints out the string function for easy access
        :return:
        """
        print(self.__str__())


if __name__ == "__main__":
    customer1 = Customer(333, "pob", "chad", 4144141141, "333 n street st")
    customer1.display()
    customer2 = Customer("monkey", "dope", "not", 54555555555, "71628654871245 space St.")
    customer2.display()
    # constructor raised exception
