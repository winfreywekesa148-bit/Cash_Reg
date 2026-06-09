#create cash reg
class CashRegister:
    def __init__(self, discount=0):
        self._discount = None
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
          return self._discount
    
    @discount.setter
    def discount(self, value):
          
          if value >= 0 and value <= 100:
                self._discount = value
          else:
                raise TypeError("Not valid discount")
   

    def totals(self):
        return self.total
    
    def item(self):
          return self.items

    def previous_transaction(self):
          return self.previous_transactions
    
    #method
    def add_item(self, item, price, quantity=1):
         self.total += price * quantity
         for _ in range(quantity):
             self.items.append(item)

         transaction = {
              "item" : item,
              "price" : price,
              "quantity" : quantity
         }

         self.previous_transactions.append(transaction)

    def apply_discount(self):
         if self._discount == 0:
              print ( "There is no discount to apply.")
         discount_amount = self.total * (self._discount / 100)
         self.total -= discount_amount
         print ( f"After the discount, the total comes to ${int(self.total)}.")
                   
cash_register = CashRegister()
cash_register.add_item("Coffee", 100, 2)

print(cash_register.discount)
print(cash_register.add_item("Coffee", 100, 2))
print(cash_register.apply_discount())


