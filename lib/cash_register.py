#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.discount = discount

    def add_item(self, title, price, quantity=1):
        for _ in range(quantity):
            self.total += price
            self.items.append(title)

    def apply_discount(self):
        if self.discount > 0:
            self.total -= int(self.total * (self.discount / 100))
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.items:
            last_item = self.items.pop()
            self.total -= last_item["price"]

    def void_last_transaction_with_multiples(self):
        if self.items:
            last_item = self.items[-1]  # Get the last item without removing it
            self.total -= last_item["price"]
            self.items = self.items[:-1]  # Remove the last item from the list

    def items_list_without_multiples(self):
        return self.items

    def items_list_with_multiples(self):
        items_with_multiples = []
        for item in self.items:
            if items_with_multiples and items_with_multiples[-1] == item:
                items_with_multiples.append(item)
            else:
                for _ in range(self.items.count(item)):
                    items_with_multiples.append(item)
        return items_with_multiples