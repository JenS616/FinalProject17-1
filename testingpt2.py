    def reset_day(self):
        self.odds_rob = random.randint(0, 10)
        self.odds_job = random.randint(0, 5)
        if self.odds_rob == 1:
            self.money_pocket = 0
            print("""YOU HAVE BEEN ROBBED OF ALL THE MONEY YOU WERE CARRYING! Better put it in the bank next time...
--------------------------------------------------------------------------------------------------
        """)
        if self.odds_job == 1:
            self.job = 'none'
            self.job_loc = 'nowhere'
            self.salary = 0
            print("""YOU HAVE LOST YOUR JOB! Go look for a new one...
--------------------------------------------------------------------------------------------------
        """)
        self.day_number += 1
        self.hours = 16
        if self.day_number != 7 or 14 or 21:
            self.day_beginning = input(f"""You are on Day {self.day_number}. You have {self.hours} hours left. You are at {self.current_loc}. Where would you like to go?
    Diner (d)
    Bank (b)
    Career Services (c)
    Education Center (e)
--------------------------------------------------------------------------------------------------
        """)
        elif self.day_number == 7 or 14 or 21:
            self.rent -= 1
            self.day_beginning = input(f"""You are on Day {self.day_number}. Today is the day that your rent is due. You should go to the bank to pay it off or you will be evicted. You have {self.hours} hours left. You are at {self.current_loc}. Where would you like to go?
    Diner (d)
    Bank (b)
    Career Services (c)
    Education Center (e)
--------------------------------------------------------------------------------------------------
        """)
        elif self.rent == -1:
            self.hours = 12
            self.day_beginning = input(f"""You are on Day {self.day_number}. You have been evicted, so you sit on the street depressed for 4 hours. You have {self.hours} hours left. You are at {self.current_loc}. Where would you like to go?
--------------------------------------------------------------------------------------------------
        """)



    def reset_day(self):
        self.odds_rob = random.randint(0, 10)
        self.odds_job = random.randint(0, 5)
        if self.odds_rob == 1:
            self.money_pocket = 0
            print("""YOU HAVE BEEN ROBBED OF ALL THE MONEY YOU WERE CARRYING! Better put it in the bank next time...
--------------------------------------------------------------------------------------------------
        """)
        if self.odds_job == 1:
            self.job = 'none'
            self.job_loc = 'nowhere'
            self.salary = 0
            print("""YOU HAVE LOST YOUR JOB! Go look for a new one...
--------------------------------------------------------------------------------------------------
        """)
        self.day_number += 1
        self.hours = 16
        self.food -= 1
        if self.food >= 0 and self.day_number != 7 or 14 or 21:
            self.day_beginning = input(f"""You are on Day {self.day_number}. You have {self.hours} hours left. You are at {self.current_loc}. Where would you like to go?
    Diner (d)
    Bank (b)
    Career Services (c)
    Education Center (e)
--------------------------------------------------------------------------------------------------
        """)
        if self.food >= 0 and self.day_number == 7 or 14 or 21:
            self.day_beginning = input(f"""You are on Day {self.day_number}. Today is the day that your rent is due. You should go to the bank to pay it off or you will be evicted. You have {self.hours} hours left. You are at {self.current_loc}. Where would you like to go?
    Diner (d)
    Bank (b)
    Career Services (c)
    Education Center (e)
--------------------------------------------------------------------------------------------------
        """)
        if self.day_number == 7 or 14 or 21:
            self.rent -= 1
        if self.food < 0 and self.day_number != 7 or 14 or 21:
            self.hours = 12
            self.food = 0
            self.day_beginning = input(f"""You are on Day {self.day_number}. You have no food, so you get sick and lose 4 hours. You have {self.hours} hours left. You are at {self.current_loc}. Where would you like to go?
    Diner (d)
    Bank (b)
    Career Services (c)
    Education Center (e)
--------------------------------------------------------------------------------------------------
        """)
        if self.food < 0 and self.day_number == 7 or 14 or 21:
            self.hours = 12
            self.food = 0
            self.day_beginning = input(f"""You are on Day {self.day_number}. You have no food, so you get sick and lose 4 hours. Also, today is the day that your rent is due. You should go to the bank to pay it off or you will be evicted. You have {self.hours} hours left. You are at {self.current_loc}. Where would you like to go?
    Diner (d)
    Bank (b)
    Career Services (c)
    Education Center (e)
--------------------------------------------------------------------------------------------------
        """)
        if self.food < 0 and self.rent == -1:
            self.hours = 10
            self.food = 0
            self.day_beginning = input(f"""You are on Day {self.day_number}. You have no food, so you get sick and lose 4 hours. You have been evicted, so you sit on the street depressed for 2 hours. You have {self.hours} hours left. You are at {self.current_loc}. Where would you like to go?
--------------------------------------------------------------------------------------------------
        """)


    # DINER PURCHASE FOOD
        if a == 'p':
            price = random.randint(20, 101)
            p = input(f"""The price of food today is {price} dollars. You have {player.money_pocket} dollars.
    Buy (b)
    Exit (e)
--------------------------------------------------------------------------------------------------
        """)
            if p == 'b':
                food_cost2 = price * 2
                food_cost3 = price * 3
                c = int(input(f"""
    How much food would you like to buy? You have {player.money_pocket} dollars.
    1: {price}
    2: {food_cost2}
    3: {food_cost3}
        """))
                if c == 1:
                    if player.money_pocket >= price:
                        player.money_pocket -= price
                        player.food += 1
                        print("""You have purchased 1 unit of food.
--------------------------------------------------------------------------------------------------
        """)
                    else:
                        print("""Sorry, you do not have enough money.
--------------------------------------------------------------------------------------------------
        """)
                elif c == 2:
                    if player.money_pocket >= food_cost2:
                        player.money_pocket -= food_cost2
                        player.food += 2
                        print("""You have purchased 2 units of food.
--------------------------------------------------------------------------------------------------
        """)
                    else:
                        print("""Sorry, you do not have enough money.
--------------------------------------------------------------------------------------------------
        """)
                elif c == 3:
                    if player.money_pocket >= food_cost3:
                        player.money_pocket -= food_cost3
                        player.food += 3
                        print("""You have purchased 3 units of food.
--------------------------------------------------------------------------------------------------
        """)
                    else:
                        print("""Sorry, you do not have enough money.
--------------------------------------------------------------------------------------------------
        """)
            if p == 'e':
                pass