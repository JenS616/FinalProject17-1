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
                print(f'You have {self.hours} hours left. You are at {self.current_loc}. What would you like to do?')
            elif self.destination == 'c':
                self.hours -= 1
                self.current_loc = 'Career Services'
                print(f'You have {self.hours} hours left. You are at {self.current_loc}. What would you like to do?')
            elif self.destination == 'e':
                self.hours -= 2
                self.current_loc = 'the Education Center'
                print(f'You have {self.hours} hours left. You are at {self.current_loc}. What would you like to do?')
        if self.current_loc == 'the Bank':
            if self.destination == 'd':
                self.hours -= 1
                self.current_loc = 'the Diner'
                print(f'You have {self.hours} hours left. You are at {self.current_loc}. What would you like to do?')
            elif self.destination == 'c':
                self.hours -= 2
                self.current_loc = 'Career Services'
                print(f'You have {self.hours} hours left. You are at {self.current_loc}. What would you like to do?')
            elif self.destination == 'e':
                self.hours -= 1
                self.current_loc = 'Education Center'
                print(f'You have {self.hours} hours left. You are at {self.current_loc}. What would you like to do?')
        if self.current_loc == 'Career Services':
            if self.destination == 'd':
                self.hours -= 1
                self.current_loc = 'the Diner'
                print(f'You have {self.hours} hours left. You are at {self.current_loc}. What would you like to do?')
            elif self.destination == 'b':
                self.hours -= 2
                self.current_loc = 'the Bank'
                print(f'You have {self.hours} hours left. You are at {self.current_loc}. What would you like to do?')
            elif self.destination == 'e':
                self.hours -= 1
                self.current_loc = 'the Education Center'
                print(f'You have {self.hours} hours left. You are at {self.current_loc}. What would you like to do?')
        if self.current_loc == 'the Education Center':
            if self.destination == 'd':
                self.hours -= 2
                self.current_loc = 'the Diner'
                print(f'You have {self.hours} hours left. You are at {self.current_loc}. What would you like to do?')
            elif self.destination == 'b':
                self.hours -= 1
                self.current_loc = 'the Bank'
                print(f'You have {self.hours} hours left. You are at {self.current_loc}. What would you like to do?')
            elif self.destination == 'c':
                self.hours -= 1
                self.current_loc = 'Career Services'
                print(f'You have {self.hours} hours left. You are at {self.current_loc}. What would you like to do?')

player = User('none', 'nowhere', 0, 0, 0, 0, 0, 'none', 'the Diner', 16, 1)

day_beginning = input(f"""You are on Day {player.day_number}. You have {player.hours} hours left. You are at {player.current_loc}. Where would you like to go?
    Diner (d)
    Bank (b)
    Career Services (c)
    Education Center (e)
""")

player.travel(day_beginning)

   # DINER
while player.current_loc == 'the Diner':
        a = input(f"""You have {player.hours} hours left. You are at {player.current_loc}. What would you like to do?
    Travel (t)
    Purchase Food (p)
    Work (wo)
--------------------------------------------------------------------------------------------------
        """)
    # DINER TRAVEL
        if a == 't':
            new_loc = input("""Where would you like to go?
    Bank (b)
    Career Services (c)
    Education Center (e)
--------------------------------------------------------------------------------------------------
        """)
            player.travel(new_loc)
    # DINER PURCHASE FOOD
        if a == 'p':
            if player.food == 1:
                print("""You cannot buy anymore food today.
--------------------------------------------------------------------------------------------------
        """)
            else:
                price = random.randint(20, 101)
                p = input(f"""The price of food today is {price} dollars. You have {player.money_pocket} dollars.
    Buy (b)
    Exit (e)
--------------------------------------------------------------------------------------------------
        """)
                if p == 'b':
                    if player.money_pocket >= price:
                        player.money_pocket -= price
                        player.food += 1
                    else:
                        print("""Sorry, you do not have enough money.
--------------------------------------------------------------------------------------------------
        """)
                if p == 'e':
                    pass
        if a == 'wo':
            if player.job_loc != 'the Diner':
                print("""Sorry, you do not have a job here.
--------------------------------------------------------------------------------------------------
        """)
            else:
                hours_work = int(input(f"""You have {player.hours} hours left. You have {player.money_pocket} dollars. Your salary is {player.salary} dollars.
        How many hours would you like to work?
--------------------------------------------------------------------------------------------------
        """)
                player.work(hours_work)


#EDUCATION
while player.current_loc == 'the Education Center' and player.job_loc != 'the Education Center':
    a = input("""
    Travel (t)
    Learn (l)
""")
    if a == 't':
        new_loc = input("""Where would you like to go?
    Diner (d)
    Bank (b)
    Career Services (c)
""")
        player.travel(new_loc)
    if a == 'l':
        if player.education == 'college':
            print('You are at the highest education level. You cannot learn anymore.')
        else:
            hours_learn = int(input(f"""You have {player.hours} hours left. Your education level: {player.education}. You need {player.hours_graduate}.
    How many hours would you like to learn?
"""))
            if hours_learn > player.hours:
                print('Sorry, you do not have enough hours today.')
            else:
                player.learn(hours_learn)
                print(f'You spent {hours_learn} hours learning. You have {player.hours_graduate} left to graduate. Your education level: {player.education}.')
                if player.hours_to_graduate == 0:
                    if player.education == 'none':
                        print('Congratulations, you have graduated high school!')
                        player.education = 'high school'
                    elif player.education == 'high school':
                        print('Congratulations, you have graduated college!')
                        player.education = 'college'