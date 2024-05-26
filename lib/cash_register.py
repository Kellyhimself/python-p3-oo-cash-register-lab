#!/usr/bin/env python3

class CashRegister:
  
  def __init__(self,discount=0):
    self.discount=discount
    self.total=0
    self.items=[]
    self.last_transaction={}

  def add_item(self,item,amount,quantity=1):
    self.total+=(amount*quantity)
    for i in range(quantity):
      self.items.append(item)
    self.last_transaction['item']=item
    self.last_transaction['amount']=amount
    self.last_transaction['quantity']=quantity

  def apply_discount(self):
    if not self.discount:
      print("There is no discount to apply.")
    else:
      self.total=self.total-self.total*(self.discount/100)
      print(f"After the discount, the total comes to ${int(self.total)}.")

  def void_last_transaction(self):
    self.items.pop()
    self.total-=self.last_transaction['amount']*self.last_transaction['quantity']