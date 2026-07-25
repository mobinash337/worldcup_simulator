#Classknockoutstage.py
#مبینا شاکری
#404130813

import csv
import random
import os
import numpy as np
from collections import defaultdict
from Classteam import Team
from Classmatch import Match
from Classgroup import Group
#کلاس مسئول اجرای مراحل حذفی
class knockoutstage:

    def __init__(self,stage_name,teams):
        self.stage_name= stage_name
        self.matches= []

        for i in range(0,len(teams),2):
            match= Match(
                teams[i],
                teams[i+1],
                is_knockout=True
            )
            self.matches.append(match)
    #تابع اجرا تمام مسابقات مرحله
    def play_stage(self):
        winners=[]

        print("\n" + "*" * 60)
        print(self.stage_name)
        print("*" * 60)

        for match in self.matches:
            winner = match.play()
            winners.append(winner)
            match.display()

            print("_" * 60)
        return winners

    #گرفتن لیست برندگان
    def get_winners(self):
        winners= []
        for match in self.matches:
            winners.append(match.winner)
        return winners
    #نتایج تمام بازی ها
    def display_results(self):
        print("\n" + "*" * 60)
        print(self.stage_name)
        print("*" * 60)

        for match in self.matches:
            print(
                f"{match.team1.name}"
                f"{match.goals1}-{match.goals}"
                f"{match.team2.name}"
                )
        if match.penalty is not None:
            (
                f"({match.penalty[0]}"
                f"{match.penalty[1]} penaltys)"
            )

            print("Winner:", match.winner.name)
            print("_" * 60)