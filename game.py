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

    def work(self, hours_work):
        self.hours_work = hours_work
        self.hours -= hours_work
        self.money_earned = self.hours_work * self.salary
        self.money_pocket += self.money_earned
        if self.hours == 0:
            pass
        if self.hours != 0:
            print(f'You have earned {self.money_earned} dollars. You have {self.money_pocket} dollars and {hours} hours left.')

    def deposit(self, money_deposit):
        self.money_deposit = money_deposit
        self.money_pocket -= money_deposit
        self.money_bank += money_deposit
        print(f'You have deposited {self.money_deposit} dollars. You have {self.money_bank} dollars in your bank account. You are carrying {self.money_pocket} dollars.')

    def withdraw(self, money_withdraw):
        self.money_withdraw = money_withdraw
        self.money_pocket += money_withdraw
        self.money_bank -= money_withdraw
        print(f'You have withdrawn {self.money_withraw} dollars. You have {self.money_bank} dollars in your bank account. You are carrying {self.money_pocket} dollars.')

    def learn(self, hours_learn):
        self.hours_learn = hours_learn
        self.hours -= hours_learn
        if player.education == 'none':
            self.hours_graduate = 50
            self.hours_graduate -= hours_learn
        elif player.education == 'high school':
            self.hours_graduate = 50
            self.hours_graduate -= hours_learn


player = User('none', 'nowhere', 0, 0, 0, 0, 0, 'none', 'the Diner', 16, 1)

day_beginning = input(f"""You are on Day {player.day_number}. You have {player.hours} hours left. You are at {player.current_loc}. Where would you like to go?
    Diner (d)
    Bank (b)
    Career Services (c)
    Education Center (e)
""")

player.travel(day_beginning)

# DINER
# WITHOUT JOB
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
        player.current_loc = new_loc
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
# WITH JOB
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
        player.current_loc = new_loc
    if a == 'p':
        if player.food == 1:
            print('You cannot buy anymore food today.')
        else:
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
        hours_work = input(f"""You have {player.hours} hours left. You have {player.money_pocket} dollars. Your salary is {player.salary} dollars.
    How many hours would you like to work?
""")
        player.work(hours_work)

# BANK
# WITHOUT JOB
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
        player.current_loc = new_loc
    if a == 'd':
        if player.money_pocket > 0:
            money_deposit = int(input(f"""How much money would you like to deposit?
    You are carrying {player.money_pocket} dollars.
    You have {player.money_bank} dollars in your bank account.
"""))
            if money_deposit > player.money_pocket:
                print('Sorry, you do not have enough money.')
            else:
                player.deposit(money_deposit)
        if player.money_pocket == 0:
            print('Sorry, you have no money to deposit.')
    if a == 'wi':
        if player.money_bank > 0:
            money_withdraw = int(input(f"""How much money would you like to withdraw?
    You have {player.money_bank} dollars in your bank account.
    You are carrying {player.money_pocket} dollars.
"""))
            if money_withdraw > player.money_bank:
                print('Sorry, you do not have enough money.')
            else:
                player.withdraw(money_withdraw)
        if player.money_bank == 0:
            print('Sorry, you have no money to withdraw.')
# WITH JOB
while player.current_loc == 'the Bank' and player.job_loc == 'the Bank':
    a = input("""
    Travel (t)
    Deposit (d)
    Withdraw (wi)
    Work (wo)
""")
    if a == 't':
        new_loc = input("""Where would you like to go?
    Diner (d)
    Career Services (c)
    Education Center (e)
""")
        player.travel(new_loc)
        player.current_loc = new_loc
    if a == 'd':
        if player.money_pocket > 0:
            money_deposit = int(input(f"""How much money would you like to deposit?
    You are carrying {player.money_pocket} dollars.
    You have {player.money_bank} dollars in your bank account.
"""))
            if money_deposit > player.money_pocket:
                print('Sorry, you do not have enough money.')
            else:
                player.deposit(money_deposit)
        if player.money_pocket == 0:
            print('Sorry, you have no money to deposit.')
    if a == 'wi':
        if player.money_bank > 0:
            money_withdraw = int(input(f"""How much money would you like to withdraw?
    You have {player.money_bank} dollars in your bank account.
    You are carrying {player.money_pocket} dollars.
"""))
            if money_withdraw > player.money_bank:
                print('Sorry, you do not have enough money.')
            else:
                player.withdraw(money_withdraw)
        if player.money_bank == 0:
            print('Sorry, you have no money to withdraw.')
    if a == 'wo':
        hours_work = input(f"""You have {player.hours} hours left. You have {player.money_pocket} dollars. Your salary is {player.salary} dollars.
    How many hours would you like to work?
""")
        player.work(hours_work)

# CAREER SERVICES
# WITH JOB
while player.current_loc == 'Career Services':
    a = input("""
    Travel (t)
    View Jobs (v)
""")
    if a == 't':
        new_loc = input("""Where would you like to go?
    Diner (d)
    Bank (b)
    Education Center (e)
""")
        player.travel(new_loc)
        player.current_loc = new_loc
    if a == 'v':
        b = input("""Where would you like to view jobs?
    Diner (d)
    Bank (b)
    Education Center (e)
""")
        if b == 'd':
            odds1 = random.randint(1, 3)
            odds2 = random.randint(1, 3)
            odds3 = random.randint(1, 3)
            salary_cashier = random.randint(9, 12)
            salary_cook = random.randint(11, 15)
            salary_manager = random.randint(25, 31)
            e = input(f"""You have a {player.education} education. Please indicate the job you would like to apply for.
    Cashier (ca): ${salary_cashier} - no requirements
    Cook (co): ${salary_cook} - must have high school education
    Manager (m): ${salary_manager} - must have college education
""")
            if e == 'ca':
                if odds1 == 1:
                    player.job = 'Cashier'
                    player.job_loc = 'the Diner'
                    player.salary = salary_cashier
                    print('Congratulations, you got the job!')
                else:
                    print('Sorry, this job is not available right now.')
            if e == 'co':
                if player.education != 'none':
                    if odds2 == 1:
                        player.job = 'Cook'
                        player.job_loc = 'the Diner'
                        player.salary = salary_cook
                        print('Congratulations, you got the job!')
                    if odds2 != 1:
                        print('Sorry, this job is not available right now.')
                if player.education == 'none':
                    print('Sorry, you are not qualified for this job.')
            if e == 'm':
                if player.education == 'college':
                    if odds3 == 1:
                        player.job = 'Manager'
                        player.job_loc = 'the Diner'
                        player.salary = salary_manager
                        print('Congratulations, you got the job!')
                    else:
                        print('Sorry, this job is not available right now.')
                if player.education != 'college':
                    print('Sorry, you are not qualified for this job.')
        if b == 'b':
            odds1 = random.randint(1, 3)
            odds2 = random.randint(1, 3)
            odds3 = random.randint(1, 3)
            salary_guard = random.randint(11, 14)
            salary_teller = random.randint(14, 18)
            salary_manager = random.randint(25, 31)
            e = input(f"""You have a {player.education} education. Please indicate the job you would like to apply for.
    Security Guard (s): ${salary_guard} - no requirements
    Teller (t): ${salary_teller} - must have high school education
    Manager (m): ${salary_manager} - must have college education
""")
            if e == 's':
                if odds1 == 1:
                    player.job = 'Security Guard'
                    player.job_loc = 'the Bank'
                    player.salary = salary_guard
                    print('Congratulations, you got the job!')
                else:
                    print('Sorry, this job is not available right now.')
            if e == 't':
                if player.education != 'none':
                    if odds2 == 1:
                        player.job = 'Teller'
                        player.job_loc = 'the Bank'
                        player.salary = salary_teller
                        print('Congratulations, you got the job!')
                    if odds2 != 1:
                        print('Sorry, this job is not available right now.')
                if player.education == 'none':
                    print('Sorry, you are not qualified for this job.')
            if e == 'm':
                if player.education == 'college':
                    if odds3 == 1:
                        player.job = 'Manager'
                        player.job_loc = 'the Bank'
                        player.salary = salary_manager
                        print('Congratulations, you got the job!')
                    else:
                        print('Sorry, this job is not available right now.')
                if player.education != 'college':
                    print('Sorry, you are not qualified for this job.')
        if b == 'e':
            odds1 = random.randint(1, 3)
            odds2 = random.randint(1, 3)
            odds3 = random.randint(1, 3)
            salary_janitor = random.randint(11, 15)
            salary_secretary = random.randint(17, 21)
            salary_teacher = random.randint(27, 32)
            e = input(f"""You have a {player.education} education. Please indicate the job you would like to apply for.
    Janitor (j): ${salary_janitor} - no requirements
    Secretary (s): ${salary_secretary} - must have high school education
    Teacher (t): ${salary_teacher} - must have college education
""")
            if e == 'j':
                if odds1 == 1:
                    player.job = 'Janitor'
                    player.job_loc = 'the Education Center'
                    player.salary = salary_janitor
                    print('Congratulations, you got the job!')
                else:
                    print('Sorry, this job is not available right now.')
            if e == 's':
                if player.education != 'none':
                    if odds2 == 1:
                        player.job = 'Secretary'
                        player.job_loc = 'the Education Center'
                        player.salary = salary_secretary
                        print('Congratulations, you got the job!')
                    if odds2 != 1:
                        print('Sorry, this job is not available right now.')
                if player.education == 'none':
                    print('Sorry, you are not qualified for this job.')
            if e == 't':
                if player.education == 'college':
                    if odds3 == 1:
                        player.job = 'teacher'
                        player.job_loc = 'the Education Center'
                        player.salary = salary_teacher
                        print('Congratulations, you got the job!')
                    else:
                        print('Sorry, this job is not available right now.')

                if player.education != 'college':
                    print('Sorry, you are not qualified for this job.')
# EDUCATION CENTER
# WITHOUT JOB
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
# WITH JOB
while player.current_loc == 'the Education Center' and player.job_loc == 'the Education Center':
    a = input("""
    Travel (t)
    Learn (l)
    Work (wo)
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
    if a == 'wo':
        hours_work = input(f"""You have {player.hours} hours left. You have {player.money_pocket} dollars. Your salary is {player.salary} dollars.
    How many hours would you like to work?
""")
        player.work(hours_work)