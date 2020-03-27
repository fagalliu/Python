class CoffeeMachine:
    espresso, latte, cappuccino = [250, 0, 16, 1, 4], [350, 75, 20, 1, 7], [200, 100, 12, 1, 6]
    name_resources = ['water', 'milk', 'coffee beans', 'disposable cups', 'money']
    dictionary = {"1": espresso, "2": latte, "3": cappuccino}

    def __init__(self, water, milk, coffee, cups, money):
        self.water, self.milk, self.coffee, self.cups, self.money = water, milk, coffee, cups, money
        self.resources = [self.water, self.milk, self.coffee, self.cups, self.money]

    def fill(self):
        self.resources[0] += int(input("Write how many ml of water do you want to add "))
        self.resources[1] += int(input("Write how many ml of milk do you want to add "))
        self.resources[2] += int(input("Write how many grams of coffee beans do you want to add: "))
        self.resources[3] += int(input("Write how many disposable cups of coffee do you want to add:"))

    def buy(self):
        dic = (input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:"))
        if dic in ["1", "2", "3"]:
            for i in range(4):
                if self.resources[i - 1] < CoffeeMachine.dictionary[dic][i - 1]:
                    print("Sorry, not enough", CoffeeMachine.name_resources[i - 1], "!")
                    break
            else:
                print("I have enough resources, making you a coffee!")
                self.resources[len(CoffeeMachine.name_resources) - 1] += CoffeeMachine.dictionary[dic][4]
                for k in range(4):
                    self.resources[k] -= CoffeeMachine.dictionary[dic][k]

    def take(self):
        print("I gave you $", self.resources[4])
        self.resources[4] = 0

    def remaining(self):
        print("The coffee machine has:")
        for m in range(4):
            print(self.resources[m], "of", CoffeeMachine.name_resources[m])
        print("${} of money".format(self.resources[4]))

    def exit(self):
        global on_off
        on_off = False


answer = CoffeeMachine(400, 540, 120, 9, 550)
on_off = True
while on_off:
    dictionary_functions = {"buy": CoffeeMachine.buy, "fill": CoffeeMachine.fill,
                            "take": CoffeeMachine.take, "remaining": CoffeeMachine.remaining,
                            "exit": CoffeeMachine.exit}
    action = input("Write action (buy, fill, take, remaining, exit): ")
    dictionary_functions[action](answer)


