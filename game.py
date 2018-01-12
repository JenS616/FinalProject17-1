import random

class User(object):
    def __init__(self, job, job_loc, salary, food, money_pocket, money_bank, money_earned, education, current_loc, hours, day_number):
        self.job = job
        self.job_loc = job_loc
        self.salary = salary
        self.food = food
        self.money_pocket = money_pocket
        self.money_bank = money_bank
        self.money_earned = money_earned
        self.education = education
        self.current_loc = current_loc
        self.hours = hours
        self.day_number = day_number

    def travel(self, destination):
        self.destination = destination
        if self.current_loc == 'the Diner':
            if self.destination == 'b':
                self.hours -= 1
                self.current_loc = 'the Bank'
            elif self.destination == 'c':
                self.hours -= 1
                self.current_loc = 'Career Services'
            elif self.destination == 'e':
                self.hours -= 2
                self.current_loc = 'the Education Center'
        if self.current_loc == 'the Bank':
            if self.destination == 'd':
                self.hours -= 1
            elif self.destination == 'c':
                self.hours -= 2
                self.current_loc = 'Career Services'
            elif self.destination == 'e':
                self.hours -= 1
                self.current_loc = 'Education Center'
        if self.current_loc == 'Career Services':
            if self.destination == 'd':
                self.hours -= 1
                self.current_loc = 'the Diner'
            elif self.destination == 'b':
                self.hours -= 2
                self.current_loc = 'the Bank'
            elif self.destination == 'e':
                self.hours -= 1
                self.current_loc = 'the Education Center'
        if self.current_loc == 'the Education Center':
            if self.destination == 'd':
                self.hours -= 2
                self.current_loc = 'the Diner'
            elif self.destination == 'b':
                self.hours -= 1
                self.current_loc = 'the Bank'
            elif self.destination == 'c':
                self.hours -= 1
                self.current_loc = 'Career Services'

    def work(self, hours_work):
        self.hours_work = hours_work
        self.hours -= hours_work
        self.money_earned = self.hours_work * self.salary
        self.money_pocket += self.money_earned
        if self.hours == 0:
            pass
        if self.hours != 0:
            print(f'You have earned {self.money_earned}. You have {self.money_pocket} and {hours} hours left.')

    def deposit(self, money_deposit):
        self.money_deposit = money_deposit



player = User('none', 'nowhere', 0, 0, 0, 0, 0, 'none', 'the Diner', 16, 1)

day_beginning = input(f"""You are on Day {player.day_number}. You have {player.hours} left. You are at {player.current_loc}. Where would you like to go?
    Diner (d)
    Bank (b)
    Career Services (c)
    Education Center (e)
""")

player.travel(day_beginning)

print(f'You have {player.hours} hours left. You are at {player.current_loc}. What would you like to do?')

# DINER
while player.current_loc == 'the Diner' and player.job_loc != 'the Diner':
    a = input("""
    Travel (t)
    Purchase Food (p)
""")
    if a == 't':
        new_loc = input("""Where would you like to go?
    Bank (b)
    Career Services (c)
    Education Center (e)
""")
        player.travel(new_loc)
    if a == 'p':
        price = random.randint(20, 101)
        p = input(f"""The price of food today is {price} dollars. You have {player.money_pocket}.
    Buy (b)
    Exit (e)
    """)
        if p == 'b':
            if player.money_pocket >= price:
                player.money_pocket -= price
                player.food += 1
            else:
                print('Sorry, you do not have enough money.')
        if p == 'e':
            pass
while player.current_loc == 'the Diner' and player.job_loc == 'the Diner':
    a = input("""
    Travel (t)
    Purchase Food (p)
    Work (wo)
""")
    if a == 't':
        new_loc = input("""Where would you like to go?
    Bank (b)
    Career Services (c)
    Education Center (e)
""")
        player.travel(new_loc)
    if a == 'p':
        price = random.randint(20, 101)
        p = input(f"""The price of food today is {price} dollars. You have {player.money_pocket} dollars.
    Buy (b)
    Exit (e)
""")
        if p == 'b':
            if player.money_pocket >= price:
                player.money_pocket -= price
                player.food += 1
            else:
                print('Sorry, you do not have enough money.')
        if p == 'e':
            pass
    if a == 'wo':
        hours_work = input(f"""You have {player.hours} hours left. You have {player.money_pocket} dollars.
    How many hours would you like to work?
""")
        player.work(hours_work)

# BANK
while player.current_loc == 'the Bank' and player.job_loc != 'the Bank':
    a = input("""
    Travel (t)
    Deposit (d)
    Withdraw (wi)
""")
    if a == 't':
        new_loc = input("""Where would you like to go?
    Diner (d)
    Career Services (c)
    Education Center (e)
""")
        player.travel(new_loc)
    if a == 'd':
        if player.money_pocket != 0:
            b = int(input(f"""How much money would you like to deposit?
            You are carrying {player.money_pocket} dollars.
            You have {player.money_bank} dollars in your bank account.
"""))
            if player.money_pockets >= b:
                player.money_pockets -= a
                player.money_bank += a
            else:
                print('Sorry, you do not have that amount of money.')