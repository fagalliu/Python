# Define the global variable
water = 400
milk = 540
beans = 120
cups = 9
money = 550


# This function prints the maschine's state
def state():
    global water, milk, beans, cups, money
    print("\nThe coffe machine has:\n", water, 'of water\n', milk,
          'of milk\n', beans, 'of coffe beans\n', cups,
          'of disposable cups\n', money, 'of money\n')
    action()


# Buy action
def buy():
    global water, milk, beans, cups, money
    bli = str(input('\nWhat do you want to buy?\n 1-espresso\n 2-latte\n 3-cappuccino\n 4-back to main menu:\n> '))
    if bli == '1':
        if water < 250:
            print('Sorry, not enough water!')
        elif beans < 16:
            print('Sorry, not enough beans!')
        elif cups < 1:
            print('Sorry, not enough cups!')
        else:
            print('I have enough resources, making you a coffee!')
            water -= 250
            beans -= 16
            cups -= 1
            money += 4
    elif bli == '2':
        if water < 350:
            print('Sorry, not enough water!')
        elif milk < 75:
            print('Sorry, not enough milk')
        elif beans < 20:
            print('Sorry, not enough beans!')
        elif cups < 1:
            print('Sorry, not enough cups!')
        else:
            print('I have enough resources, making you a coffee!')
            water -= 350
            milk -= 75
            beans -= 20
            cups -= 1
            money += 7
    elif bli == '3':
        if water < 200:
            print('Sorry, not enough water!')
        elif milk < 100:
            print('Sorry, not enough milk')
        elif beans < 12:
            print('Sorry, not enough beans!')
        elif cups < 1:
            print('Sorry, not enough cups!')
        else:
            print('I have enough resources, making you a coffee!')
            water -= 200
            milk -= 100
            beans -= 12
            cups -= 1
            money += 6
    elif bli == 'back':
        action()
    else:
        print('Wrong number. Try again: ')
        buy()

    # state()

    # print('Do you want another cup? (type "y" for yes or any other button for no).')
    # if input() == 'y':
    #     buy()
    # else:
    #     print('Another action? ')
    #     if input() == 'y':
    #         action()
    #     else:
    #         exit()
    action()


# Fill action
def fill():
    global water, milk, beans, cups, money
    water += int(input('\nWrite how many ml of water do you want to add: '))
    milk += int(input('Write how many ml of milk do you want to add:'))
    beans += int(input('Write how many grams of coffee beans do you want to add:'))
    cups += int(input('Write how many disposable cups of coffee do you want to add:'))

    action()

    # state()
    # print('Another action? ')
    # if input() == 'y':
    #     action()
    # else:
    #     exit()


# Take action
def take():
    global money
    print('\nI gave you $' + str(money))
    money -= money

    state()

    # print('Another action? ')
    # if input() == 'y':
    #     action()
    # else:
    #     exit()


# Choose an action
def action():
    choose = input('\nWrite an action (buy, fill, take, remaining, exit):\n')
    if choose == 'buy':
        buy()
    elif choose == 'fill':
        fill()
    elif choose == 'take':
        take()
    elif choose == 'remaining':
        state()
    elif choose == 'exit':
        exit()
    else:
        print('Error! Please type buy, fill, take, remaining, exit!')
        print('Do you realy want to take an action?')
        if input() == 'y':
            action()
        else:
            exit()


# This function exit the program
#def exit():
    #print('Exited')


action()
