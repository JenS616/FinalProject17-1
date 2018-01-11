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