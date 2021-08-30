import json
from abc import ABC
from sys import exit




class Cart():

    def __init__(self):
        self.products = {}
        self.prices = {
            "tomatoes": 0.50,
            "orange": 0.75,
            "apple": 0.45,
            "melon": 1,
            "blueberries": 3,
            "banana": 0.15,
            "mango": 0.35
        }
        self.tax = 10

    def ask_if_cart(self):
        have_cart = input("Do you already have a cart?: Y/N ")
        if have_cart.lower() == "y":
            with open("productsj.json", "r") as saved_products:
                data = json.load(saved_products)
                self.products = data
            with open("productsj.json", "w") as saved_products:
                json.dump({}, saved_products)

            if len(self.products) == 0:
                print("Sorry, you have no cart in our registers")
                self.products == {}
        if have_cart.lower() == "n":
            self.products == {}

    def save(self):
        saved = input("Do you want to save your cart for later?: y/n ")
        if saved.lower() == 'y':
            if len(self.products) == 0:
                print("Your Shopping Cart is Empty.")

            else:
                with open("productsj.json", "w") as saved_products:
                    json.dump(self.products, saved_products)
                    return 1

        if saved.lower() == 'n':
            exit()

    def show(self):
        if len(self.products) == 0:
            print("Your Shopping Cart is Empty.")
        else:
            for key, values in self.products.items():
                print(f"{values}-----{key}")

    def add(self):
        item = input("What product do you want to add? : ")
        if item in self.prices:
            if item in self.products:
                self.products[item] += 1
            else:
                self.products[item] = 1

        else:
            print("We are sorry, this product is temporarily out of stock")

    def delete(self):
        # clear_output()
        if len(self.products) == 0:
            print("Your Shopping Cart is Empty.")

        else:
            self.show()
            delete = input(
                "Which product do you want to remove from your Shopping Cart? : ")
            # clear_output()
            if delete in self.products:
                amount = int(
                    input(f'How many {delete} do you want to delete: '))
                if amount > self.products[delete]:
                    print(
                        f'Sorry, you only have {self.products[delete]} {delete}')
                elif amount == self.products[delete]:
                    del self.products[delete]
                    self.show()
                else:
                    self.products[delete] -= amount
                    self.show()

            else:
                print(
                    "Sorry, it seems like you dont have this product in your Shopping Cart ")

    def clear(self):

        clear = input(
            "Are you sure you want to empty your Cart??? Y/N  ")
        if clear.lower() == "y":
            self.products.clear()

        elif clear.lower() == "n":
            pass

    def checkout(self):
        print("Please see below the total amount of your purchase")
        total = 0
        for product, quatity in self.products.items():
            total += (self.prices[product]*quatity)
            print(f'{quatity}---{product} = ${self.prices[product]*quatity}')
        print(f"Total before taxes = ${total} \n + ")

        print(f' taxes ---- {self.tax}% -- ${(total*self.tax)/100}')

        print(f'The grand total is ${((total*self.tax)/100)+total} ')


cart1 = Cart()


cart1.ask_if_cart()
while True:

    command = input(
        "Please select one option:   Show - Add - Delete - Clear - Save - Checkout - Quit  ")

    if command.lower() == "save":
        cart1.save()
        if 1:
            break
        
    if command.lower() == "quit":
        # clear_output()
        cart1.show()
        break
    elif command.lower() == "show":
        # clear_output()
        cart1.show()
    elif command.lower() == "add":
        # clear_output()
        cart1.add()
    elif command.lower() == "delete":
        # clear_output()
        cart1.delete()
    elif command.lower() == "clear":
        #     # clear_output()
        cart1.clear()
    elif command.lower() == "checkout":
        cart1.checkout()
    else:
        print("I cant understand you..")
