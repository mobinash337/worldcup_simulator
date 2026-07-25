#Classteam.py
#مبینا شاکری
#1080786228

import csv
import random
import os
import numpy as np
from collections import defaultdict

#کلاس نشان دهنده تیم فوتبال
class Team :

    def __init__(self, name , attack , defense , rank):
        self.name = name
        self.attack = int(attack)
        self.defense = int(defense)
        self.rank = int(rank)
        self.group = ""

        self.reset_stats()
    #صفر کردن تمام داده ها
    def reset_stats(self):
        self.matches_played = 0
        self.wins = 0
        self.points = 0
        self.draws = 0
        self.losses = 0
        self.goals_for = 0
        self.goals_against = 0
    #تفاضل گل های زده شده از گل های خورده شده
    def goal_difference(self):

        return self.goals_for - self.goals_against
    #به روز رسانی داده ها پس از یک مسابقه
    def update_stats(self, goals_for , goals_against):
        self.matches_played +=1
        self.goals_for += goals_for
        self.goals_against += goals_against

        if goals_for>goals_against:
            self.points += 3
            self.wins += 1

        elif goals_for==goals_against:
            self.points += 1
            self.draws += 1

        else:
            self.losses += 1
    
    def __str__(self):
        return self.name