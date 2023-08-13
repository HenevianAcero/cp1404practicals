"""
CP1404 Practical 07
project.py
Estimated time: 30 min
Actual time: 28 min
"""

import datetime

class Project:
    def __init__(self, name, start_date, priority, cost, percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost = cost
        self.percentage = percentage

    def __repr__(self):
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: {self.cost}, completion: {self.percentage}"

    def complete_project(self):
        return self.percentage == 100

    def incomplete_project(self):
        return self.percentage < 100

    def __lt__(self, other_project):
        return self.priority < other_project.priority