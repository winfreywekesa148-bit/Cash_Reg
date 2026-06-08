#create cash reg
class CashRegister:
    def __init__(self, discount):
        self.discount = discount

        if self.discount:
                self.discount = int(self.discount)
        else:
                self.discount = 0

    def total(self):
          return self.total_amount
    
    def item(self):
          items = []
          return items

    def previous_transaction(self):
          previous_transactions = []
          return previous_transactions




discount = int(input("Enter discount percentage: "))
