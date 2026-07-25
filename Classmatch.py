#classmatch.py
#مبینا شاکری
#404130813

import csv
import random
import os
import numpy as np
from collections import defaultdict
from Classteam import Team

#تابع شبیه سازی ضربات پنالتی
def penalty_shoot(team1 , team2):
    score1 = 0
    score2 = 0

    p1 = 0.75 + (team1.attack - team2.defense)/ 250
    p2 = 0.75 + (team2.attack - team1.defense)/ 250

    p1= max(0.6, min(0.9 , p1))
    p2= max(0.6, min(0.9 , p2)) 

    for i in range(5):
        if random.random() < p1 :
            score1 += 1
        if random.random() < p2:
            score2 += 1

    while score1==score2 :
        if random.random() < p1 :
            score1 +=1
        if random.random() < p2 :
            score2 += 1
    if score1>score2:
        winner = team1
    else:
        winner = team2

    return winner,score1, score2
#تابع محاسبه lam
def calculate_lambda(team , opponent):

    lam=((team.attack /100) * 1.5 + (1- opponent.defense /100) * 0.8)

    return max(lam, 0.1)

#شبیه سازی تعداد گل های یک تیم در مسابقه
def simulate_goals(team1, team2, extra_time=False):
    lam = calculate_lambda (team1, team2)

    if extra_time:
        lam *= 0.33

    return np.random.poisson(lam)
#برگزاری یک مسابقه بین دو تیم
class Match:

    def __init__(self, team1, team2, is_knockout=False):
        self.team1 = team1
        self.team2 = team2
        self.is_knockout = is_knockout
        self.goals1 = 0
        self.goals2 = 0
        self.penalty = None
        self.winner = None
    #تابع انجام مسابقه
    def play(self):
        self.goals1 = simulate_goals(self.team1, self.team2)
        self.goals2 = simulate_goals(self.team2, self.team1)

        self.team1.update_stats(self.goals1,self.goals2)
        self.team2.update_stats(self.goals2,self.goals1)

        if not self.is_knockout:
            if self.goals1> self.goals2:
                self.winner = self.team1
            elif self.goals2> self.goals1:
                self.winner = self.team2
            else:
                self.winner= None

            return self.winner
        #مرحله حذفی
        if self.goals1> self.goals2:
            self.winner = self.team1
            return self.winner
        if self.goals2> self.goals1:
            self.winner= self.team2
            return self.winner
        #وقت اضافه
        extra1 = simulate_goals(
            self.team1,
            self.team2,
            extra_time=True
        )
        extra2 = simulate_goals(
            self.team2,
            self.team1,
            extra_time=True
        )
        self.goals1 += extra1
        self.goals2 +=extra2

        if self.goals1>self.goals2:
            self.winner= self.team1
            return self.winner
        if self.goals2> self.goals1:
            self.winner= self.team2
            return self.winner
        #پنالتی
        self.winner,p1,p2= penalty_shoot(
            self.team1,
            self.team2
        )
        self.penalty=(p1,p2)
        self.winner= self.winner
        return self.winner
    #نتایج مسابقه انجام شده
    def display(self):
        print("-"* 60)
        print(
            f"{self.team1.name}"
            f"{self.goals1}-{self.goals2}"
            f"{self.team2.name}"
        )
        if self.penalty is not None:
            print(
                f"({self.penalty[0]}-{self.penalty[1]} penaltys)"
            )
        if self.winner is not None:
            print("winner:",self.winner.name)

        print("-"* 60)