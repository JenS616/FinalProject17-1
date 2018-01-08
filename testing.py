import random

class User(object):
    def __init__(self, job, job_loc, salary, food, money_pocket, money_bank, education):
        self.job = job
        self.job_loc = job_loc
        self.salary = salary
        self.food = food
        self.money_pocket = money_pocket
        self.money_bank = money_bank
        self.education = education

player = User('none', 'nowhere', 0, 0, 0, 0, 'none')
hours = 16
day_number = 1

l = 'the Diner'
x = input(f"""You are on Day {day_number}. You have {hours} hours left. You are at {l}. Where would you like to go?
    Diner (D)
    Bank (B)
    Career Services (C)
    Education Center (E)
""")
while hours == 0:
    x = input(f"""You are on Day {day_number}. You have {hours} hours left. You are at {l}. Where would you like to go?
    Diner (D)
    Bank (B)
    Career Services (C)
    Education Center (E)
""")
while x == 'D':
    if l == 'the Bank':
        hours -= 1
    if l == 'Career Services':
        hours -= 1
    if l == 'the Education Center':
        hours -= 2
    l = 'the Diner'
    print(f"You have {hours} hours left. You are at {l}.")
    y = input("""What would you like to do?
    Travel (T)
    Purchase Food (P)
    Work (Wo)
""")
    if y == 'T':
        c = input(f"""You have {hours} hours left. Where would you like to go?
        Bank (B)
        Career Services (C)
        Education Center (E)
""")
        if c == 'B':
            x = 'B'
        if c == 'C':
            x = 'C'
        if c == 'E':
            x = 'E'
    if y == 'P':
        price = random.randint(20, 100)
        z = input(f"""The price of food today is {price} dollars. Type B to buy and E to go back to the Diner options.
""")
        if z == 'B':
            if player.money_pockets >= price:
                player.money_pockets -= price
            else:
                print('Sorry, you do not have enough money.')
        if z == 'E':
            x == 'D'
    if y == 'Wo':
        if player.job_loc == 'Diner' and player.job != 'none':
            a = int(input(f'You have {hours} hours left. How many hours would you like to work? '))
            hours -= a
            player.money_pocket += (a * player.salary)
        else:
            print('Sorry, you do not have a job here.')
while x == 'B':
    if l == 'the Diner':
        hours -= 1
    if l == 'Career Services':
        hours -= 2
    if l == 'the Education Center':
        hours -= 1
    l = 'the Bank'
    print(f"You have {hours} hours left. You are at {l}.")
    y = input("""What would you like to do?
    Travel (T)
    Work (Wo)
    Deposit (D)
    Withdraw (Wi)
""")
    if y == 'T':
        c = input(f"""You have {hours} hours left. Where would you like to go?
        Diner (D)
        Career Services (C)
        Education Center (E)
""")
        if c == 'D':
            x = 'D'
        if c == 'C':
            x = 'C'
        if c == 'E':
            x = 'E'
    if y == 'Wo':
        if player.job_loc == 'Bank' and player.job != 'none':
            a = int(input(f'You have {hours} hours left. How many hours would you like to work? '))
            hours -= a
            player.money_pocket += (a * player.salary)
        else:
            print('Sorry, you do not have a job here.')
    if y == 'D':
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
    if y == 'Wi':
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
while x == 'C':
    if l == 'the Diner':
        hours -= 1
    if l == 'the Bank':
        hours -= 2
    if l == 'the Education Center':
        hours -= 1
    l = 'Career Services'
    print(f"You have {hours} hours left. You are at {l}.")
    y = input("""What would you like to do?
    Travel (T)
    View Jobs (V)
""")
    if y == 'T':
        c = input(f"""You have {hours} hours left. Where would you like to go?
        Diner (D)
        Bank (B)
        Education Center (E)
""")
        if c == 'D':
            x = 'D'
        if c == 'B':
            x = 'B'
        if c == 'E':
            x = 'E'
    if y == 'V':
        d = input("""Where would you like to view jobs?
        Diner (D)
        Bank (B)
        Education Center (E)
""")
        if d == 'D':
            odds1 = random.randint(1, 3)
            odds2 = random.randint(1, 3)
            odds3 = random.randint(1, 3)
            salary_cashier = random.randint(9, 12)
            salary_cook = random.randint(11, 15)
            salary_manager = random.randint(25, 31)
            e = input(f"""You have a {player.education} education. Please indicate the job you would like to apply for.
            Cashier (Ca): ${salary_cashier} - no requirements
            Cook (Co): ${salary_cook} - must have high school education
            Manager (M): ${salary_manager} - must have college education
""")
            if e == 'Ca':
                if odds1 == 1:
                    player.job = 'Cashier'
                    player.job_loc = 'the Diner'
                    player.salary = salary_cashier
                else:
                    print('Sorry, this job is not available right now.')
            if e == 'Co':
                if player.education == 'high school' or 'college':
                    if odds2 == 1:
                        player.job = 'Cook'
                        player.job_loc = 'the Diner'
                        player.salary = salary_cook
                    if odds2 != 1:
                        print('Sorry, this job is not available right now.')
                if player.education == 'none':
                    print('Sorry, you are not qualified for this job.')
            if e == 'M':
                if player.education == 'college':
                    if odds3 == 1:
                        player.job = 'Manager'
                        player.job_loc = 'the Diner'
                        player.salary = salary_manager
                    else:
                        print('Sorry, this job is not available right now.')
                if player.education != 'college':
                    print('Sorry, you are not qualified for this job.')
        if d == 'B':
            odds1 = random.randint(1, 3)
            odds2 = random.randint(1, 3)
            odds3 = random.randint(1, 3)
            salary_guard = random.randint(11, 14)
            salary_teller = random.randint(14, 18)
            salary_manager = random.randint(25, 31)
            e = input(f"""You have a {player.education} education. Please indicate the job you would like to apply for.
            Security Guard (S): ${salary_guard} - no requirements
            Teller (T): ${salary_teller} - must have high school education
            Manager (M): ${salary_manager} - must have college education
""")
while x == 'E':
    if l == 'the Diner':
        hours -= 2
    if l == 'the Bank':
        hours -= 1
    if l == 'Career Services':
        hours -= 1
    l = 'the Education Center'
    print(f"You have {hours} hours left. You are at {l}.")
    y = input("""What would you like to do?
    Travel (T)
    Work (Wo)
    Learn (L)
""")
    if y == 'T':
        c = input(f"""You have {hours} hours left. Where would you like to go?
        Diner (D)
        Bank (B)
        Career Services (C)
""")
        if c == 'D':
            x = 'D'
        if c == 'B':
            x = 'B'
        if c == 'C':
            x = 'C'
    if y == 'Wo':
        if player.job_loc == 'Education Center' and player.job != 'none':
            a = int(input(f'You have {hours} hours left. How many hours would you like to work? '))
            hours -= a
            player.money_pocket += (a * player.salary)
        else:
            print('Sorry, you do not have a job here.')
while hours == 0:
    day_number += 1