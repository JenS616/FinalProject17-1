# Importing random
import random

class User(object):
    """Establishes player and functions"""
    def __init__(self, job, job_loc, salary, money_pocket, money_bank, money_earned, education, current_loc, hours, day_number, rent, hours_graduate, happiness, health, lottery_ticket):
        """Stats for player"""
        self.job = job
        self.job_loc = job_loc
        self.salary = salary
        self.money_pocket = money_pocket
        self.money_bank = money_bank
        self.money_earned = money_earned
        self.education = education
        self.current_loc = current_loc
        self.hours = hours
        self.day_number = day_number
        self.rent = rent
        self.hours_graduate = hours_graduate
        self.happiness = happiness
        self.health = health
        self.lottery_ticket = lottery_ticket

    def travel(self, destination):
        """Travel function, moves player from place to place and deducts appropriate number of hours"""
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
            elif self.destination == 's':
                self.hours -= 3
                self.current_loc = 'the Shopping Mall'
        if self.current_loc == 'the Bank':
            if self.destination == 'd':
                self.hours -= 1
                self.current_loc = 'the Diner'
            elif self.destination == 'c':
                self.hours -= 2
                self.current_loc = 'Career Services'
            elif self.destination == 'e':
                self.hours -= 1
                self.current_loc = 'the Education Center'
            elif self.destination == 's':
                self.hours -= 3
                self.current_loc = 'the Shopping Mall'
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
            elif self.destination == 's':
                self.hours -= 3
                self.current_loc = 'the Shopping Mall'
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
            elif self.destination == 's':
                self.hours -= 3
                self.current_loc = 'the Shopping Mall'
        if self.current_loc == 'the Shopping Mall':
            if self.destination == 'd':
                self.hours -= 3
                self.current_loc = 'the Diner'
            elif self.destination == 'b':
                self.hours -= 3
                self.current_loc = 'the Bank'
            elif self.destination == 'c':
                self.hours -= 3
                self.current_loc = 'Career Services'
            elif self.destination == 'e':
                self.hours -= 3
                self.current_loc = 'the Education Center'

    def work(self):
        """Allows player to work and adds paycheck accordingly"""
        if self.job_loc != self.current_loc:
            print("""Sorry, you do not have a job here.
--------------------------------------------------------------------------------------------------
        """)
        else:
            self.hours_work = int(input(f"""You have {self.hours} hours left. You have {self.money_pocket} dollars. Your salary is {self.salary} dollars.
    How many hours would you like to work?
--------------------------------------------------------------------------------------------------
        """))
            if self.hours >= self.hours_work:
                self.hours -= self.hours_work
                self.money_earned = self.hours_work * self.salary
                self.money_pocket += self.money_earned
                print(f"""You have earned {self.money_earned} dollars. You have {self.money_pocket} dollars.
--------------------------------------------------------------------------------------------------
        """)
            elif self.hours < self.hours_work:
                print("""Sorry, you do not have enough hours in the day.
--------------------------------------------------------------------------------------------------
        """)

    def deposit(self, money_deposit):
        """Adds user's inputted money into bank account"""
        self.money_deposit = money_deposit
        self.money_pocket -= int(money_deposit)
        self.money_bank += int(money_deposit)
        print(f"""You have deposited {self.money_deposit} dollars. You have {self.money_bank} dollars in your bank account. You are carrying {self.money_pocket} dollars.
--------------------------------------------------------------------------------------------------
        """)

    def withdraw(self, money_withdraw):
        """Withdraw user's inputted money from bank account"""
        self.money_withdraw = money_withdraw
        self.money_pocket += int(money_withdraw)
        self.money_bank -= int(money_withdraw)
        print(f"""You have withdrawn {self.money_withdraw} dollars. You have {self.money_bank} dollars in your bank account. You are carrying {self.money_pocket} dollars.
--------------------------------------------------------------------------------------------------
        """)

    def learn(self, hours_learn):
        """Subtracts hours from player's hours to graduate"""
        self.hours_learn = hours_learn
        self.hours -= hours_learn
        self.hours_graduate -= hours_learn

    def see_stats(self):
        """Displays player's stats"""
        self.days_left = 21 - self.day_number
        print(f"""
    Days Left = {self.days_left}
    Day Number = {self.day_number}
    Hours Left in Day = {self.hours}
    Happiness = {self.happiness}
    Health = {self.health}
    Job = {self.job}
    Job Location = {self.job_loc}
    Salary = {self.salary}
    Money in Pocket = {self.money_pocket}
    Money in Bank = {self.money_bank}
    Education = {self.education}
    Lottery Tickets = {self.lottery_ticket}
--------------------------------------------------------------------------------------------------
        """)

# RESET DAY FUNCTION
def reset_day():
    """Resets the day according to number of factors"""
    # Creating odds for robbery, job loss, and lottery
    odds_rob = random.randint(0, 10)
    odds_job = random.randint(0, 5)
    odds_lottery = random.randint(1, 501)
    # Resetting day number and hours
    player.day_number += 1
    player.hours = 16
    if player.day_number != 22:
        # Robbery
        if odds_rob == 1 and player.money_pocket != 0:
            player.money_pocket = 0
            player.health -= 5
            player.happiness -= 5
            player.hours -= 4
            print("""YOU HAVE BEEN ROBBED OF ALL THE MONEY YOU WERE CARRYING!
In the fight for your money, you have LOST 5 HEALTH.
Since you're broke, your HAPPINESS DECREASES BY 5.
You lose 4 hours wallowing in self-pity. Better put it in the bank next time...
--------------------------------------------------------------------------------------------------
        """)
        # Job loss
        if odds_job == 1 and player.job != 'none':
            player.job = 'none'
            player.job_loc = 'nowhere'
            player.salary = 0
            player.happiness -= 5
            player.hours -= 2
            print("""YOU HAVE BEEN FIRED FROM YOUR JOB!
You're sad, and LOSE 5 HAPPINESS.
You lose 2 hours wallowing in self-pity. Go look for a new job...
--------------------------------------------------------------------------------------------------
        """)
        # Winning the lottery
        if odds_lottery <= player.lottery_ticket:
            player.money_pocket += 500
            player.happiness += 10
            print("""CONGRATULATIONS, YOU HAVE WON THE LOTTERY!
You GAIN 10 HAPPINESS.
$1,000 has been deposited into your bank account.
--------------------------------------------------------------------------------------------------
        """)
        # Did not win the lottery
        if player.lottery_ticket != 0 and odds_lottery > player.lottery_ticket:
            player.happiness -= 2
            player.hours -= 1
            print("""You didn't win the lottery.
You LOSE 2 HAPPINESS and 1 hour because you're sad.
--------------------------------------------------------------------------------------------------
        """)
        player.lottery_ticket = 0
        # Rent day 7
        if player.day_number == 7:
            player.rent -= 1
            day_beginning = input(f"""##################################################################################################
You are on Day {player.day_number}. Today is the day that your rent is due ($500). You should go
to the bank to pay it off or you will be evicted. You have {player.hours} hours left. You are at
{player.current_loc}.
Where would you like to go?
    Diner (d)
    Bank (b)
    Career Services (c)
    Education Center (e)
    Shopping Mall (s)
--------------------------------------------------------------------------------------------------
        """)
            player.travel(day_beginning)
        # Rent day 14
        elif player.day_number == 14:
            player.rent -= 1
            day_beginning = input(f"""##################################################################################################
You are on Day {player.day_number}. Today is the day that your rent is due ($1,000). You should go
to the bank to pay it off or you will be evicted. You have {player.hours} hours left. You are at
{player.current_loc}.
Where would you like to go?
    Diner (d)
    Bank (b)
    Career Services (c)
    Education Center (e)
    Shopping Mall (s)
--------------------------------------------------------------------------------------------------
        """)
            player.travel(day_beginning)
        # Rent day 21
        elif player.day_number == 21:
            player.rent -= 1
            day_beginning = input(f"""##################################################################################################
You are on Day {player.day_number}. Today is the day that your rent is due ($1,500). You should go
to the bank to pay it off or you will be evicted. You have {player.hours} hours left. You are at
{player.current_loc}.
Where would you like to go?
    Diner (d)
    Bank (b)
    Career Services (c)
    Education Center (e)
    Shopping Mall (s)
--------------------------------------------------------------------------------------------------
        """)
            player.travel(day_beginning)
        # Normal day beginning
        else:
            day_beginning = input(f"""##################################################################################################
You are on Day {player.day_number}. You have {player.hours} hours left. You are at {player.current_loc}.
Where would you like to go?
    Diner (d)
    Bank (b)
    Career Services (c)
    Education Center (e)
    Shopping Mall (s)
--------------------------------------------------------------------------------------------------
        """)
            player.travel(day_beginning)
        # ENDS GAME BECAUSE EVICTION
        while player.rent == -1:
            print("""YOU DID NOT PAY RENT AND YOU WERE EVICTED.
GAME OVER.
--------------------------------------------------------------------------------------------------
        """)
            break

def game_over():
    """Ends the game"""
    # END GAME
    while player.day_number == 22:
        # WIN
        if player.money_bank >= 2000:
            money_points = (player.money_pocket + player.money_bank) / 1000
            final_score = player.happiness + player.health + money_points
            if player.education == 'none':
                final_score += 10
            elif player.education == 'high school':
                final_score += 20
            elif player.education == 'college':
                final_score += 100
            print(f"""Congratulations, you have won the game! Here are your
ending stats.
    Happiness = {self.happiness}
    Health = {self.health}
    Money in Pocket = {self.money_pocket}
    Money in Bank = {self.money_bank}
    Education = {self.education}
YOUR FINAL SCORE IS...
    {final_score} points!
Thanks for playing!
--------------------------------------------------------------------------------------------------
            """)
            break
        # LOSE
        else:
            print(f"""GAME OVER. You did not have $4,000 in your bank account.
Thanks for playing!
--------------------------------------------------------------------------------------------------
            """)
            break

# CREATE PLAYER
player = User('none', 'nowhere', 0, 0, 0, 0, 'none', 'the Diner', 16, 1, 1, 50, 10, 10, 0)

# BEGINNING OF GAME
print("""Rent is due every 7 days (Day 7: $500; Day 14: $1,000; Day 21: $1,500. If you fail to pay rent,
you will lose the game automatically. You can apply forjobs at Career Services and gain a better
education at the Education Center (a better education can give you a higher paying job). At the
Diner and Shopping Mall, you can buy items to boost your happiness and health. At the Bank, you
can access your bank account. YOU HAVE 21 DAYS TO EARN $2,000!
--------------------------------------------------------------------------------------------------
        """)
day_beginning = input(f"""You are on Day {player.day_number}. You have {player.hours} hours left. You are at {player.current_loc}.
Where would you like to go?
    Diner (d)
    Bank (b)
    Career Services (c)
    Education Center (e)
    Shopping Mall (s)
--------------------------------------------------------------------------------------------------
        """)
player.travel(day_beginning)

# LOOP UNTIL BROKEN BY GAME OVER FUNCTION
while player.day_number <= 21:
   # DINER
    while player.current_loc == 'the Diner':
        if player.hours <= 0:
            reset_day()
            game_over()
        if player.current_loc == 'the Diner':
            a = input(f"""You have {player.hours} hours left. You are at {player.current_loc}.
What would you like to do?
    Travel (t)
    Get Food (g)
    Work (wo)
    See Stats (s)
--------------------------------------------------------------------------------------------------
        """)
    # DINER TRAVEL
        if a == 't':
            new_loc = input("""Where would you like to go?
    Bank (b)
    Career Services (c)
    Education Center (e)
    Shopping Mall (s)
--------------------------------------------------------------------------------------------------
        """)
            player.travel(new_loc)
    # DINER GET FOOD
        if a == 'g':
            b = input("""Food costs $50. It will take you two hours to eat your food. It will increase your happiness by two. Would you like to get food?
    Yes (y)
    No (n)
--------------------------------------------------------------------------------------------------
        """)
            if b == 'y':
                if player.money_pocket >= 50:
                    player.money_pocket -= 50
                    player.happiness += 2
                    player.hours -= 2
                    print(f"""You have {player.money_pocket} dollars. Your happiness is now {player.happiness}.
--------------------------------------------------------------------------------------------------
        """)
                else:
                    print("""Sorry, you do not have enough money.
--------------------------------------------------------------------------------------------------
        """)
    # DINER WORK
        if a == 'wo':
            player.work()
    # DINER SEE STATS
        if a == 's':
            player.see_stats()


    # BANK
    while player.current_loc == 'the Bank':
        if player.hours <= 0:
            reset_day()
            game_over()
        if player.current_loc == 'the Bank':
            a = input(f"""You have {player.hours} hours left. You are at {player.current_loc}. What would you like to do?
    Travel (t)
    Deposit (d)
    Withdraw (wi)
    Work (wo)
    Pay Rent (p)
    See Stats (s)
--------------------------------------------------------------------------------------------------
        """)
    # BANK TRAVEL
        if a == 't':
            new_loc = input("""Where would you like to go?
    Diner (d)
    Career Services (c)
    Education Center (e)
    Shopping Mall (s)
--------------------------------------------------------------------------------------------------
        """)
            player.travel(new_loc)
    # BANK DEPOSIT
        if a == 'd':
            if player.money_pocket == 0:
                print("""Sorry, you have no money to deposit.
--------------------------------------------------------------------------------------------------
        """)
            if player.money_pocket > 0:
                money_deposit = int(input(f"""How much money would you like to deposit?
    You are carrying {player.money_pocket} dollars.
    You have {player.money_bank} dollars in your bank account.
--------------------------------------------------------------------------------------------------
        """))
                if money_deposit > player.money_pocket:
                    print("""Sorry, you do not have enough money.
--------------------------------------------------------------------------------------------------
        """)
                else:
                    player.deposit(money_deposit)
    # BANK WITHDRAW
        if a == 'wi':
            if player.money_bank > 0:
                money_withdraw = int(input(f"""How much money would you like to withdraw?
    You have {player.money_bank} dollars in your bank account.
    You are carrying {player.money_pocket} dollars.
--------------------------------------------------------------------------------------------------
        """))
                if money_withdraw > player.money_bank:
                    print("""Sorry, you do not have enough money.
--------------------------------------------------------------------------------------------------
        """)
                else:
                    player.withdraw(money_withdraw)
            if player.money_bank == 0:
                print("""Sorry, you have no money to withdraw.
--------------------------------------------------------------------------------------------------
        """)
    # BANK WORK
        if a == 'wo':
            player.work()
    # BANK PAY RENT
        if a == 'p':
            if player.day_number == 7 or 14 or 21:
                rent = 500
                if player.money_pocket >= rent:
                    player.rent = 1
                    player.money_pocket -= 500
                    print("""Congratulations, you have paid off your rent.
--------------------------------------------------------------------------------------------------
        """)
                else:
                    print("""Sorry, you do not have enough money on you. Please withdraw from your bank account or earn more money.
--------------------------------------------------------------------------------------------------
        """)
            else:
                if player.day_number < 7:
                    days = 7 - player.day_number
                    print("""Your rent is due in {days} days. Come back then.
--------------------------------------------------------------------------------------------------
        """)
                elif player.day_number < 14:
                    days = 14 - player.day_number
                    print("""Your rent is due in {days} days. Come back then.
--------------------------------------------------------------------------------------------------
        """)
                elif player.day_number < 21:
                    days = 21 - player.day_number
                    print("""Your rent is due in {days} days. Come back then.
--------------------------------------------------------------------------------------------------
        """)
    # BANK SEE STATS
        if a == 's':
            player.see_stats()


    # CAREER SERVICES
    while player.current_loc == 'Career Services':
        if player.hours <= 0:
            reset_day()
            game_over()
        if player.current_loc == 'Career Services':
            a = input(f"""You have {player.hours} hours left. You are at {player.current_loc}. What would you like to do?
    Travel (t)
    View Jobs (v)
    See Stats (s)
--------------------------------------------------------------------------------------------------
        """)
    # CAREER SERVICES TRAVEL
        if a == 't':
            new_loc = input("""Where would you like to go?
    Diner (d)
    Bank (b)
    Education Center (e)
    Shopping Mall (s)
--------------------------------------------------------------------------------------------------
        """)
            player.travel(new_loc)
    # CAREER SERVICES VIEW JOBS
        if a == 'v':
            b = input("""Where would you like to view jobs?
    Diner (d)
    Bank (b)
    Education Center (e)
    Shopping Mall (s)
--------------------------------------------------------------------------------------------------
        """)
            if b == 'd':
                odds1 = random.randint(0, 4)
                odds2 = random.randint(0, 4)
                odds3 = random.randint(0, 4)
                salary_cashier = 10
                salary_cook = 12
                salary_manager = 31
                e = input(f"""You have a {player.education} education. Please indicate the job you would like to apply for.
    Cashier (ca): ${salary_cashier} - no requirements
    Cook (co): ${salary_cook} - must have high school education
    Manager (m): ${salary_manager} - must have college education
--------------------------------------------------------------------------------------------------
        """)
                if e == 'ca':
                    if odds1 != 0:
                        player.job = 'Cashier'
                        player.job_loc = 'the Diner'
                        player.salary = salary_cashier
                        print("""Congratulations, you got the job!
--------------------------------------------------------------------------------------------------
        """)
                    else:
                        print("""Sorry, this job is not available right now.
--------------------------------------------------------------------------------------------------
        """)
                if e == 'co':
                    if player.education != 'none':
                        if odds2 != 0:
                            player.job = 'Cook'
                            player.job_loc = 'the Diner'
                            player.salary = salary_cook
                            print("""Congratulations, you got the job!
--------------------------------------------------------------------------------------------------
        """)
                        if odds2 == 1:
                            print("""Sorry, this job is not available right now.
--------------------------------------------------------------------------------------------------
        """)
                    if player.education == 'none':
                        print("""Sorry, you are not qualified for this job.
--------------------------------------------------------------------------------------------------
        """)
                if e == 'm':
                    if player.education == 'college':
                        if odds3 != 0:
                            player.job = 'Manager'
                            player.job_loc = 'the Diner'
                            player.salary = salary_manager
                            print("""Congratulations, you got the job!
--------------------------------------------------------------------------------------------------
        """)
                        else:
                            print("""Sorry, this job is not available right now.
--------------------------------------------------------------------------------------------------
        """)
                    if player.education != 'college':
                        print("""Sorry, you are not qualified for this job.
--------------------------------------------------------------------------------------------------
        """)
            if b == 'b':
                odds1 = random.randint(0, 4)
                odds2 = random.randint(0, 4)
                odds3 = random.randint(0, 4)
                salary_guard = 11
                salary_teller = 14
                salary_manager = 30
                e = input(f"""You have a {player.education} education. Please indicate the job you would like to apply for.
    Security Guard (s): ${salary_guard} - no requirements
    Teller (t): ${salary_teller} - must have high school education
    Manager (m): ${salary_manager} - must have college education
--------------------------------------------------------------------------------------------------
        """)
                if e == 's':
                    if odds1 != 0:
                        player.job = 'Security Guard'
                        player.job_loc = 'the Bank'
                        player.salary = salary_guard
                        print("""Congratulations, you got the job!
--------------------------------------------------------------------------------------------------
        """)
                    else:
                        print("""Sorry, this job is not available right now.
--------------------------------------------------------------------------------------------------
        """)
                if e == 't':
                    if player.education != 'none':
                        if odds2 != 0:
                            player.job = 'Teller'
                            player.job_loc = 'the Bank'
                            player.salary = salary_teller
                            print("""Congratulations, you got the job!
--------------------------------------------------------------------------------------------------
        """)
                        if odds2 == 0:
                            print("""Sorry, this job is not available right now.
--------------------------------------------------------------------------------------------------
        """)
                    if player.education == 'none':
                        print("""Sorry, you are not qualified for this job.
--------------------------------------------------------------------------------------------------
        """)
                if e == 'm':
                    if player.education == 'college':
                        if odds3 != 0:
                            player.job = 'Manager'
                            player.job_loc = 'the Bank'
                            player.salary = salary_manager
                            print("""Congratulations, you got the job!
--------------------------------------------------------------------------------------------------
        """)
                        else:
                            print("""Sorry, this job is not available right now.
--------------------------------------------------------------------------------------------------
        """)
                    if player.education != 'college':
                        print("""Sorry, you are not qualified for this job.
--------------------------------------------------------------------------------------------------
        """)
            if b == 'e':
                odds1 = random.randint(0, 4)
                odds2 = random.randint(0, 4)
                odds3 = random.randint(0, 4)
                salary_janitor = 9
                salary_secretary = 17
                salary_teacher = 33
                e = input(f"""You have a {player.education} education. Please indicate the job you would like to apply for.
    Janitor (j): ${salary_janitor} - no requirements
    Secretary (s): ${salary_secretary} - must have high school education
    Teacher (t): ${salary_teacher} - must have college education
--------------------------------------------------------------------------------------------------
        """)
                if e == 'j':
                    if odds1 != 0:
                        player.job = 'Janitor'
                        player.job_loc = 'the Education Center'
                        player.salary = salary_janitor
                        print("""Congratulations, you got the job!
--------------------------------------------------------------------------------------------------
        """)
                    else:
                        print("""Sorry, this job is not available right now.
--------------------------------------------------------------------------------------------------
        """)
                if e == 's':
                    if player.education != 'none':
                        if odds2 != 0:
                            player.job = 'Secretary'
                            player.job_loc = 'the Education Center'
                            player.salary = salary_secretary
                            print("""Congratulations, you got the job!
--------------------------------------------------------------------------------------------------
        """)
                        if odds2 == 0:
                            print("""Sorry, this job is not available right now.
--------------------------------------------------------------------------------------------------
        """)
                    if player.education == 'none':
                        print("""Sorry, you are not qualified for this job.
--------------------------------------------------------------------------------------------------
        """)
                if e == 't':
                    if player.education == 'college':
                        if odds3 != 0:
                            player.job = 'Teacher'
                            player.job_loc = 'the Education Center'
                            player.salary = salary_teacher
                            print("""Congratulations, you got the job!
--------------------------------------------------------------------------------------------------
        """)
                        else:
                            print("""Sorry, this job is not available right now.
--------------------------------------------------------------------------------------------------
        """)
                    if player.education != 'college':
                        print("""Sorry, you are not qualified for this job.
--------------------------------------------------------------------------------------------------
        """)
            if b == 's':
                odds1 = random.randint(0, 4)
                odds2 = random.randint(0, 4)
                odds3 = random.randint(0, 4)
                salary_guard = 13
                salary_retail = 16
                salary_manager = 24
                e = input(f"""You have a {player.education} education. Please indicate the job you would like to apply for.
    Security Guard (s): ${salary_guard} - no requirements
    Retail Worker (r): ${salary_retail} - must have high school education
    Manager (m): ${salary_manager} - must have college education
--------------------------------------------------------------------------------------------------
        """)
                if e == 's':
                    if odds1 != 0:
                        player.job = 'Security Guard'
                        player.job_loc = 'the Shopping Mall'
                        player.salary = salary_guard
                        print("""Congratulations, you got the job!
--------------------------------------------------------------------------------------------------
        """)
                    else:
                        print("""Sorry, this job is not available right now.
--------------------------------------------------------------------------------------------------
        """)
                if e == 'r':
                    if player.education != 'none':
                        if odds2 != 0:
                            player.job = 'Retail Worker'
                            player.job_loc = 'the Shopping Mall'
                            player.salary = salary_retail
                            print("""Congratulations, you got the job!
--------------------------------------------------------------------------------------------------
        """)
                        if odds2 == 0:
                            print("""Sorry, this job is not available right now.
--------------------------------------------------------------------------------------------------
        """)
                    if player.education == 'none':
                        print("""Sorry, you are not qualified for this job.
--------------------------------------------------------------------------------------------------
        """)
                if e == 'm':
                    if player.education == 'college':
                        if odds3 != 0:
                            player.job = 'Manager'
                            player.job_loc = 'the Shopping Mall'
                            player.salary = salary_manager
                            print("""Congratulations, you got the job!
--------------------------------------------------------------------------------------------------
        """)
                        else:
                            print("""Sorry, this job is not available right now.
--------------------------------------------------------------------------------------------------
        """)
                    if player.education != 'college':
                        print("""Sorry, you are not qualified for this job.
--------------------------------------------------------------------------------------------------
        """)
    # CAREER SERVICES SEE STATS
        if a == 's':
            player.see_stats()

    # EDUCATION CENTER
    while player.current_loc == 'the Education Center':
        if player.hours <= 0:
            reset_day()
            game_over()
        if player.current_loc == 'the Education Center':
            a = input(f"""You have {player.hours} hours left. You are at {player.current_loc}. What would you like to do?
    Travel (t)
    Learn (l)
    Work (wo)
    See Stats (s)
--------------------------------------------------------------------------------------------------
        """)
    # EDUCATION CENTER TRAVEL
        if a == 't':
            new_loc = input("""Where would you like to go?
    Diner (d)
    Bank (b)
    Career Services (c)
    Shopping Mall (s)
--------------------------------------------------------------------------------------------------
        """)
            player.travel(new_loc)
    # EDUCATION CENTER LEARN
        if a == 'l':
            if player.education == 'college':
                print(""""You are at the highest education level. You cannot learn anymore.
--------------------------------------------------------------------------------------------------
        """)
            else:
                hours_learn = int(input(f"""You have {player.hours} hours left. Your education level: {player.education}. You need {player.hours_graduate} more hours to graduate.
    How many hours would you like to learn?
--------------------------------------------------------------------------------------------------
        """))
                if hours_learn > player.hours:
                    print("""Sorry, you do not have enough hours today.
--------------------------------------------------------------------------------------------------
        """)
                else:
                    if player.education == 'none' and player.hours_graduate > 0:
                        player.learn(hours_learn)
                        if player.hours_graduate > 0:
                            print(f"""You spent {hours_learn} hours learning. You have {player.hours_graduate} left to graduate. Your education level: {player.education}.
--------------------------------------------------------------------------------------------------
        """)
                        elif player.hours_graduate <= 0:
                            print("""Congratulations, you have graduated high school! You gain 5 Happiness.
--------------------------------------------------------------------------------------------------
        """)
                            player.education = 'high school'
                            player.happiness += 5
                            player.hours_graduate = 50
                    elif player.education == 'high school' and player.hours_graduate > 0:
                        player.learn(hours_learn)
                        if player.hours_graduate > 0:
                            print(f"""You spent {hours_learn} hours learning. You have {player.hours_graduate} left to graduate. Your education level: {player.education}.
--------------------------------------------------------------------------------------------------
        """)
                        elif player.hours_graduate <= 0:
                            print("""Congratulations, you have graduated college! You gain 5 Happiness.
--------------------------------------------------------------------------------------------------
        """)
                            player.education = 'college'
                            player.happiness += 5

    # EDUCATION CENTER WORK
        if a == 'wo':
            player.work()
    # EDUCATION CENTER SEE STATS
        if a == 's':
            player.see_stats()

    # SHOPPING MALL
    while player.current_loc == 'the Shopping Mall':
        if player.hours <= 0:
            reset_day()
            game_over()
        if player.current_loc == 'the Shopping Mall':
            a = input(f"""You have {player.hours} hours left. You are at {player.current_loc}. What would you like to do?
    Travel (t)
    Go Shopping (g)
    Buy Lottery Ticket (b)
    Work (wo)
    See Stats (s)
--------------------------------------------------------------------------------------------------
        """)

    # SHOPPING MALL TRAVEL
        if a == 't':
            new_loc = input("""Where would you like to go?
    Diner (d)
    Bank (b)
    Career Services (c)
    Education Center (e)
--------------------------------------------------------------------------------------------------
        """)
            player.travel(new_loc)
    # SHOPPING MALL SHOPPING
        if a == 'g':
            b = input(f"""You have {player.happiness} happiness and {player.health} health. Would you like to view products that will boost your happiness or health?
    Happiness (ha)
    Health (he)
--------------------------------------------------------------------------------------------------
        """)
            if b == 'ha':
                c = input(f"""You have {player.happiness} happiness and {player.money_pocket} dollars. Please indicate what you would like to buy.
    Netflix (n) = $10 = +1 Happiness
    TV (tv) = $300 = +20 Happiness
--------------------------------------------------------------------------------------------------
        """)
                if c == 'n':
                    if player.money_pocket >= 10:
                        player.money_pocket -= 10
                        player.happiness += 1
                        print(f"""You have bought Netflix. You now have {player.money_pocket} dollars and {player.happiness} happiness.
--------------------------------------------------------------------------------------------------
        """)
                    else:
                        print("""Sorry, you do not have enough money.
--------------------------------------------------------------------------------------------------
        """)
                if c == 'tv':
                    if player.money_pocket >= 300:
                        player.money_pocket -= 300
                        player.happiness += 20
                        print(f"""You have bought a TV. You now have {player.money_pocket} dollars and {player.happiness} happiness.
--------------------------------------------------------------------------------------------------
        """)
                    else:
                        print("""Sorry, you do not have enough money.
--------------------------------------------------------------------------------------------------
        """)
            if b == 'he':
                c = input(f"""You have {player.health} health and {player.money_pocket} dollars. Please indicate what you would like to buy.
    Apple (a) = $2 = +1 Health
    Vitamins (v) = $15 = +3 Health
--------------------------------------------------------------------------------------------------
        """)
                if c == 'a':
                    if player.money_pocket >= 2:
                        player.money_pocket -= 2
                        player.health += 1
                        print(f"""You have bought an apple. You now have {player.money_pocket} dollars and {player.health} health.
--------------------------------------------------------------------------------------------------
        """)
                    else:
                        print("""Sorry, you do not have enough money.
--------------------------------------------------------------------------------------------------
        """)
                if c == 'v':
                    if player.money_pocket >= 15:
                        player.money_pocket -= 15
                        player.health += 3
                        print(f"""You have bought vitamins. You now have {player.money_pocket} dollars and {player.health} health.
--------------------------------------------------------------------------------------------------
        """)
                    else:
                        print("""Sorry, you do not have enough money.
--------------------------------------------------------------------------------------------------
        """)
    # SHOPPING MALL BUY LOTTERY TICKET
        if a == 'b':
            c = int(input(f"""The prize is $1,000. A lottery ticket costs $2. You have {player.money_pocket} dollars. How many tickets would you like to buy?
--------------------------------------------------------------------------------------------------
        """))
            purchase = 2 * c
            if purchase >= player.money_pocket:
                player.money_pocket -= purchase
                player.lottery_ticket += c
                print(f"""You now have {player.lottery_ticket} lottery tickets. You have {player.money_pocket} dollars.
--------------------------------------------------------------------------------------------------
        """)
    # SHOPPING MALL WORK
        if a == 'wo':
            player.work()
    # SHOPPING MALL SEE STATS
        if a == 's':
            player.see_stats()