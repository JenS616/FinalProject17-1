import random

hours = 16

class User(object):
    def __init__(self, job, job_loc, salary, food, money_pocket, money_bank, education, current_loc):
        self.job = job
        self.job_loc = job_loc
        self.salary = salary
        self.food = food
        self.money_pocket = money_pocket
        self.money_bank = money_bank
        self.education = education
        self.current_loc = current_loc

    def travel(self, destination):
        self.destination = destination
        if self.current_loc == 'the Diner':
            if self.destination == 'b':
                hours -= 1
                self.current_loc = 'the Bank'
            elif self.destination == 'c':
                hours -= 1
                self.current_loc = 'Career Services'
            elif self.destination == 'e':
                hours -= 2
                self.current_loc = 'the Education Center'
        if self.current_loc == 'the Bank':
            if self.destination == 'd':
                hours -= 1
            elif self.destination == 'c':
                hours -= 2
                self.current_loc = 'Career Services'
            elif self.destination == 'e':
                hours -= 1
                self.current_loc = 'Education Center'
        if self.current_loc == 'Career Services':
            if self.destination == 'd':
                hours -= 1
                self.current_loc = 'the Diner'
            elif self.destination == 'b':
                hours -= 2
                self.current_loc = 'the Bank'
            elif self.destination == 'e':
                hours -= 1
                self.current_loc = 'the Education Center'
        if self.current_loc == 'the Education Center':
            if self.destination == 'd':
                hours -= 2
                self.current_loc = 'the Diner'
            elif self.destination == 'b':
                hours -= 1
                self.current_loc = 'the Bank'
            elif self.destination == 'c':
                hours -= 1
                self.current_loc = 'Career Services'


    def work(self, work_hours):
        if self.current_loc == self.job_loc:
            self.work_hours = input('How many hours would you like to work? ')

player = User('none', 'nowhere', 0, 0, 50, 0, 'none', 'the Diner')
day_number = 1
hours_to_graduate = 50

x = input(f"""You are on Day {day_number}. You have {hours} hours left. You are at {player.current_loc}. Where would you like to go?
    Diner (d)
    Bank (b)
    Career Services (c)
    Education Center (e)
""")

player.travel(x)

# DINER
while x == 'd':
    if l == 'the Bank':
        hours -= 1
    if l == 'Career Services':
        hours -= 1
    if l == 'the Education Center':
        hours -= 2
    l = 'the Diner'
    print(f"You have {hours} hours left. You are at {l}.")
    y = input("""What would you like to do?
    Travel (t)
    Purchase Food (p)
    Work (wo)
""")
    # TRAVEL
    if y == 't':
        c = input(f"""You have {hours} hours left. Where would you like to go?
        Bank (b)
        Career Services (b)
        Education Center (e)
""")
        if c == 'b':
            x = 'b'
        if c == 'c':
            x = 'c'
        if c == 'e':
            x = 'e'
    # PURCHASE
    if y == 'p':
        price = random.randint(20, 100)
        z = input(f"""The price of food today is {price} dollars. Type B to buy and E to go back to the Diner options.
""")
        if z == 'b':
            if player.money_pockets >= price:
                player.money_pockets -= price
                player.food += 1
            else:
                print('Sorry, you do not have enough money.')
        if z == 'e':
            x == 'd'
    # WORK
    if y == 'wo':
        if player.job_loc == 'Diner' and player.job != 'none':
            a = int(input(f'You have {hours} hours left. How many hours would you like to work? '))
            if a > hours:
                print('Sorry, you do not have enough hours in the day.')
            else:
                hours -= a
                player.money_pocket += (a * player.salary)
        else:
            print('Sorry, you do not have a job here.')
# BANK
while x == 'b':
    if l == 'the Diner':
        hours -= 1
    if l == 'Career Services':
        hours -= 2
    if l == 'the Education Center':
        hours -= 1
    l = 'the Bank'
    print(f"You have {hours} hours left. You are at {l}.")
    y = input("""What would you like to do?
    Travel (t)
    Work (wo)
    Deposit (d)
    Withdraw (wi)
""")
    # TRAVEL
    if y == 'T':
        c = input(f"""You have {hours} hours left. Where would you like to go?
        Diner (d)
        Career Services (c)
        Education Center (e)
""")
        if c == 'd':
            x = 'd'
        if c == 'c':
            x = 'c'
        if c == 'e':
            x = 'e'
    # WORK
    if y == 'wo':
        if player.job_loc == 'Bank' and player.job != 'none':
            a = int(input(f'You have {hours} hours left. How many hours would you like to work? '))
            hours -= a
            player.money_pocket += (a * player.salary)
        else:
            print('Sorry, you do not have a job here.')
    # DEPOSIT
    if y == 'd':
        if player.money_pocket != 0:
            a = int(input(f"""How much money would you like to deposit?
            You are carrying {player.money_pocket} dollars.
            You have {player.money_bank} dollars in your bank account.
"""))
            if player.money_pockets >= a:
                player.money_pockets -= a
                player.money_bank += a
            else:
                print('Sorry, you do not have that amount of money.')
    # WITHDRAW
    if y == 'wi':
        if player.money_bank != 0:
            a = int(input(f"""How much money would you like to withdraw?
            You have {player.money_bank} dollars in your bank account.
            You are carrying {player.money_pocket} dollars.
"""))
            if player.money_bank <= a:
                player.money_bank -= a
                player.money_pocket += a
            else:
                print('Sorry, you do not have that amount of money in the bank.')
# CAREER SERVICES
while x == 'c':
    if l == 'the Diner':
        hours -= 1
    if l == 'the Bank':
        hours -= 2
    if l == 'the Education Center':
        hours -= 1
    l = 'Career Services'
    print(f"You have {hours} hours left. You are at {l}.")
    y = input("""What would you like to do?
    Travel (t)
    View Jobs (v)
""")
    # TRAVEL
    if y == 't':
        c = input(f"""You have {hours} hours left. Where would you like to go?
        Diner (d)
        Bank (b)
        Education Center (e)
""")
        if c == 'd':
            x = 'd'
        if c == 'b':
            x = 'b'
        if c == 'e':
            x = 'e'
    # VIEW JOBS
    if y == 'v':
        d = input("""Where would you like to view jobs?
        Diner (d)
        Bank (b)
        Education Center (e)
""")
        # DINER JOBS
        if d == 'd':
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
                else:
                    print('Sorry, this job is not available right now.')
            if e == 'co':
                if player.education != 'none':
                    if odds2 == 1:
                        player.job = 'Cook'
                        player.job_loc = 'the Diner'
                        player.salary = salary_cook
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
                    else:
                        print('Sorry, this job is not available right now.')
                if player.education != 'college':
                    print('Sorry, you are not qualified for this job.')
        # BANK JOBS
        if d == 'b':
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
                else:
                    print('Sorry, this job is not available right now.')
            if e == 't':
                if player.education != 'none':
                    if odds2 == 1:
                        player.job = 'Teller'
                        player.job_loc = 'the Bank'
                        player.salary = salary_teller
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
                    else:
                        print('Sorry, this job is not available right now.')
                if player.education != 'college':
                    print('Sorry, you are not qualified for this job.')
        # EDUCATION CENTER JOBS
        if d == 'e':
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
                else:
                    print('Sorry, this job is not available right now.')
            if e == 's':
                if player.education != 'none':
                    if odds2 == 1:
                        player.job = 'Secretary'
                        player.job_loc = 'the Education Center'
                        player.salary = salary_secretary
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
                    else:
                        print('Sorry, this job is not available right now.')
                if player.education != 'college':
                    print('Sorry, you are not qualified for this job.')
# EDUCATION CENTER
while x == 'e':
    if l == 'the Diner':
        hours -= 2
    if l == 'the Bank':
        hours -= 1
    if l == 'Career Services':
        hours -= 1
    l = 'the Education Center'
    print(f"You have {hours} hours left. You are at {l}.")
    y = input("""What would you like to do?
    Travel (t)
    Work (wo)
    Learn (l)
""")
    # TRAVEL
    if y == 't':
        c = input(f"""You have {hours} hours left. Where would you like to go?
        Diner (d)
        Bank (b)
        Career Services (c)
""")
        if c == 'd':
            x = 'd'
        if c == 'b':
            x = 'b'
        if c == 'c':
            x = 'c'
    # WORK
    if y == 'wo':
        if player.job_loc == 'Education Center' and player.job != 'none':
            a = int(input(f'You have {hours} hours left. How many hours would you like to work? '))
            hours -= a
            player.money_pocket += (a * player.salary)
        else:
            print('Sorry, you do not have a job here.')
    # LEARN
    if y == 'L':
        if player.education == 'college':
            print('You are at the highest education level. You cannot learn anymore.')
        else:
            g = int(input(f"""You have {hours} hours left. Your education level: {player.education}. You need {hours_to_graduate} more hours to graduate.
        How many hours would you like to learn?
"""))
        if g > hours:
            print('Sorry, you do not have enough hours today.')
        else:
            hours_to_graduate -= g
            hours -= g
        if hours_to_graduate == 0:
            if player.education == 'none':
                print('Congratulations, you have graduated high school!')
                player.education = 'high school'
            elif player.education == 'high school':
                print('Congratulations, you have graduated college!')
                player.education = 'college'
while hours == 0:
    day_number += 1
    x = input(f"""You are on Day {day_number}. You have {hours} hours left. You are at {l}. Where would you like to go?
    Diner (d)
    Bank (b)
    Career Services (c)
    Education Center (e)
""")