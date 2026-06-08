#create cash reg
class CashRegister:
    def __init__(self, discount):
        self.discount = discount
        
        self.discount = input("Enter discount percentage: ")

        if self.discount:
                self.discount = int(self.discount)
        else:
                self.discount = 0

        pass
    pass
    