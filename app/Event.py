import datetime

class Event:
    def __init__(self, date) -> None:
        self.date = date
        self.participants = []
        self.matches = []

    def update(self, date):
        pass

    def add_participant(self, participant): 
        pass

    def remove_participant(self, participant):
        pass

