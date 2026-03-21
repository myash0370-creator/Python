'''Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
and get fare information of train running under Indian Railways.'''
from random import randint

class Train:
    def __init__(self , trainNo):
        self.trainNo = trainNo

    def book(self , fro , to):
        print(f"Train is booked in train no : {self.trainNo} from {fro} to {to} ")

    def getstatus(self):
        print(f"Train no- {self.trainNo} is ruuning on time")

    def getfare(self , fro , to):
        print(f"Ticket fare in Train no- {self.trainNo} from{fro} to {to} is {randint(150 , 550)}")

t = Train(12092)
t.book("Rampur", "Dehradun")
t.getstatus()
t.getfare("Rampur",  "Dehradun")

