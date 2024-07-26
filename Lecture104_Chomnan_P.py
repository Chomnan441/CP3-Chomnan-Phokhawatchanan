class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added to " +self.name+ " " +self.lastName + "'s cart")

customer1 = Customer()
customer1.name = "Bob"
customer1.lastName = "Baby"
customer1.age = 8

customer2 = Customer()
customer2.name = "Chomnan"
customer2.lastName = "Phokhawatchanan"
customer2.age = 26

customer3 = Customer()
customer3.name = "Ning"
customer3.lastName = "Brown"
customer3.age = 24

customer4 = Customer()
customer4.name = "Pat"
customer4.lastName = "Lachinla"
customer4.age = 26

customer1.addCart()
customer2.addCart()
customer3.addCart()
customer4.addCart()