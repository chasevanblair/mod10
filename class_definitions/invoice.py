class Invoice:
    """

    Program: invoice.py

    Author: Chase Van Blair

    Last date modified: 7/5/20


    The purpose of this program is to have more practice with making classes
    and string formatting by implementing a system to print a receipt of an invoice
    for some type of store
    """
    def __init__(self, invoice_id, customer_id, lname, fname, phone, address, items_w_price={}):
        """
        constructor for Invoice obj
        :param invoice_id: Id of invoice
        :param customer_id: ID of customer
        :param lname: customer last name
        :param fname: customer first name
        :param phone: customer phone number
        :param address: customer address
        :param items_w_price: customers items purchased with their prices (optional)
        """
        self.invoice_id = invoice_id
        self.customer_id = customer_id
        self.last_name = lname
        self.first_name = fname
        self.phone_number = phone
        self.address = address
        self.items_with_price = items_w_price

    def add_item(self, item_dict):
        """
        adds purchased items with price to items_with_price
        :param item_dict: dictionary of items to be added to items_with_price
        :return:
        """
        for x, d in item_dict.items():
            self.items_with_price[x] = d

    def create_invoice(self):
        """
        creates and prints the end invoice in a readable form
        :return:
        """
        tax = 0
        total = 0
        for x, d in self.items_with_price.items():
            print(str(x) + ".........." + str(d))
            tax += self.items_with_price[x] * .06
            total += self.items_with_price[x]
        print("Tax.......%s\nTotal.........%s" % (str(round(tax, 2)), str(round(total, 2))))

    def __str__(self):
        """
        gathers all data given by customer in readable form
        :return: data as string
        """
        if len(self.items_with_price) == 0:
            items = "None"
        else:
            items = ""
            for x in self.items_with_price:
                items.join(str(x) + " : " + str(self.items_with_price[x]) + "\n")
        return (
                "Invoice ID: " + str(self.invoice_id) + "\nCustomer ID: " + str(self.customer_id) + "\nLast name: "
                + str(self.last_name) + "\nFirst name : " + str(self.first_name) + "\nPhone number: " +
                str(self.phone_number) + "\nAddress: " + str(self.address) + "\nItems with price: " + items)

    def __repr__(self):
        """
        puts all data into a list for quick access
        :return: list of customer data
        """
        if self.items_with_price == {}:
            items = "None"
        else:
            items = ""
            for x in self.items_with_price:
                items.join(str(x) + " : " + str(self.items_with_price[x]) + "\n")
        return [self.invoice_id, self.customer_id, self.last_name, self.first_name, self.phone_number,
                self.address, self.items_with_price]


if __name__ == "__main__":
    invoice = Invoice(1, 123, '1313 Disneyland Dr, Anaheim, CA 92802', 'Mouse', 'Minnie', '555-867-5309')
    invoice.add_item({'iPad': 799.99})
    invoice.add_item({'Surface': 999.99})
    invoice.create_invoice()
