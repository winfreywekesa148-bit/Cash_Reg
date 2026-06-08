#create cash reg
class CashRegister:
    def __init__(self, discount):
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
        return self._total
    
    def item(self):
          return self._items

    def previous_transaction(self):
          return self._previous_transactions
    
    #method
    def add_item(self, item, price, quantity):
         self.total.append(price)
         self.total += price

         self.items.append(item)

         transaction = {
              "item" : item,
              "price" : price,
              "quantity" : quantity
         }

         self.previous_transaction.append(transaction)
    

    

    
discount = int(input("Enter discount percentage: "))
cash_register = CashRegister(discount)

print(cash_register.discount)
