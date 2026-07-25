#Classgroup.py
#مبینا شاکری
#404130813

import csv
import random
import os
import numpy as np
from collections import defaultdict
from Classteam import Team
from Classmatch import Match
#نمایش دهنده گروه جام جهانی
class Group:

    def __init__(self, name):
        self.name= name
        self.teams=[]
        self.matches=[]
    #اضافه کردن یک تیم به گروه
    def add_team( self, team):
        team.group = self.name
        self.teams.append(team)
    #انجام تمام مسابقات داخل گروه
    def play_all_matches(self):
        self.matches.clear()

        for i in range(len(self.teams)):
            for j in range(i+1, len(self.teams)):

                match= Match(self.teams[i],self.teams[j])
                match.play()
                self.matches.append(match)
    #مرتب سازی جدول گروه براساس قوانین فیفا
    def get_ranking(self):

        ranking=sorted(
            self.teams,
            key=lambda team:(
                team.points,
                team.goal_difference(),
                team.goals_for,
                random.random()
            ),
            reverse=True
        )

        return ranking
    #دو تیم صعود کننده را برمیگرداند
    def advance_team(self):
        ranking= self.get_ranking()

        return ranking[0], ranking[1]
    #چاپ جدول گروه
    def display_table(self):
        ranking =self.get_ranking()

        print("\n")
        print("*" * 70)
        print(f"Group{self.name}")
        print("*" * 70)
        print(
            f"{'Team':15}"
            f"{'MP':>4}"
            f"{'W':>4}"
            f"{'D':>4}"
            f"{'L':>4}"
            f"{'GF':>4}"
            f"{'GA':>4}"
            f"{'GD':>4}"
            f"{'Pts':>5}"
        )
        print("-" * 70)

        for team in ranking:
            print(
                f"{team.name:15}"
                f"{team.matches_played :>4}"
                f"{team.wins:>4}"
                f"{team.draws:>4}"
                f"{team.losses:>4}"
                f"{team.goals_for:>4}"
                f"{team.goals_against:>4}"
                f"{team.goal_difference():>4}"
                f"{team.points:>5}"
            )
            print("-" *70)
    #نمایش مسابقات گروه ها
    def display_matches(self):
        print(f"\n Matches of group{self.name}")
        for match in self.matches:
            match.display()
            print("-" *50)
