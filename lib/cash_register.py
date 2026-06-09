#create cash reg
class CashRegister:
    def __init__(self, discount=0):
        self._discount = None
        self.discount = discount
        self._total = 0
        self._items = []
        self._previous_transactions = []

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
         self._total += price * quantity
         for _ in range(quantity):
             self._items.append(item)

         transaction = {
              "item" : item,
              "price" : price,
              "quantity" : quantity
         }

         self._previous_transactions.append(transaction)

    def apply_discount(self):
         if self._discount == 0:
              return "There is no discount to apply."
         discount_amount = self._total * (self._discount / 100)
         self._total -= discount_amount
         return f"After the discount, the total comes to ${int(self._total)}."
                   
cash_register = CashRegister()
cash_register.add_item("Coffee", 100, 2)

print(cash_register.discount)
print(cash_register.add_item("Coffee", 100, 2))
print(cash_register.apply_discount())


