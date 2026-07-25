#Classworldcupsimulator.py
#مبینا شاکری
#404130813

import os
import csv
import random
import numpy as np
from collections import defaultdict
from Classknockoutstage import knockoutstage
from Classteam import Team
from Classgroup import Group
from Classmatch import Match
#کلاس برای مدیریت شبیه سازی جام جهانی
class WorldCupSimulator:
    def __init__(self):
        self.teams = []
        self.groups = []
        self.round16 = None
        self.quarter_finals = None
        self.semi_finals = None
        self.final = None
        self.champion = None
    #بارگذاری اطلاعات تیم ها
    def load_teams(self , filename):
        self.teams.clear()

        if not os.path.exists(filename):
            print("File not found!")
            return False
        with open(filename,"r",encoding="utf_8")as file:
            reader = csv.DictReader(file)
            for row in reader:

                team = Team(
                    row["name"],
                    row["attack"],
                    row["defense"],
                    row["rank"]
                )

                self.teams.append(team)

        if len(self.teams) != 32:
            print("CSV must contain exactly 32 teams.")
            return False
        
        print(f"{len(self.teams)} teams loaded successfully")
        return True
    #صفر کردن آمار تیم ها
    def reset_teams(self):
        for team in self.teams:
            team.reset_stats()
    #قرعه کشی گروه ها
    def draw_groups(self):
        self.groups.clear()

        group_names= ["A","B","C","D","E","F","G","H"]
        for name in group_names:
            self.groups.append(Group(name))
        self.teams.sort(key=lambda team: team.rank)

        pot1= self.teams[0:8]
        pot2= self.teams[8:16]
        pot3= self.teams[16:24]
        pot4= self.teams[24:32]

        pots =[pot1,pot2,pot3,pot4]
        for pot in pots:
            random.shuffle(pot)

            for i in range(8):
                self.groups[i].add_team(pot[i])

        print("Groups creatsd successfully.")
    #اجرای مرحله گروهی
    def play_group_stage(self):
        print("\n" + "="* 50)
        print("Group Atsge")
        print("=" *50)

        for group in self.groups:
            group.play_all_matches()
            group.display_table()
    #ساخت مرحله یک هشتم نهایی
    def create_round16(self):
        qualified= {}
        for group in self.groups:

            first,second= group.advance_team()
            qualified[group.name]= (first,second)

        teams=[
            qualified["A"][0], qualified["B"][1],
            qualified["C"][0], qualified["D"][1],

            qualified["E"][0], qualified["F"][1],
            qualified["G"][0], qualified["H"][1],

            qualified["B"][0], qualified["A"][1],
            qualified["D"][0], qualified["C"][1],

            qualified["F"][0], qualified["E"][1],
            qualified["H"][0], qualified["G"][1]
        ]    
        self.round16= knockoutstage(
            "Round of 16",
            teams
        )
    #اجرای مرحله حذفی
    def play_knockout_stage(self):

        winners= self.round16.play_stage()
        self.quarter_finals = knockoutstage(
            "Quarter Finals",
            winners
        )
        winners= self.quarter_finals.play_stage()
        self.semi_finals= knockoutstage(
            "Semi Finals",
            winners
        )
        winners=self.semi_finals.play_stage()
        self.final=knockoutstage(
            "Final",
            winners
        )
        winners= self.final.play_stage()
        self.champion= winners[0]

        print("\n ")
        print("=" *60)
        print("World cup champion")
        print("=" *60)
        print(self.champion.name)
    #اجرای کامل جام جهانی
    def run_full_simulation(self):
        self.reset_teams()
        self.draw_groups()
        self.play_group_stage()
        self.create_round16()
        self.play_knockout_stage()

        return self.champion
    #نمایش براکت مرحله حدفی
    def display_bracket(self):
        if self.round16 is None:
            print("NO tournament has been played yet.")
            return
        print("\n" + "=" * 60)
        print("Knockout Bracket")
        print("=" *60)

        self.round16.display_results()
        self.quarter_finals.display_results()
        self.semi_finals.display_results()
        self.final.display_results()
        print("\n Champion:", self.champion.name)
    #شبیه سازی جام جهانی برای چندین بار
    def simulate_many(self, num_simulations=1000):
        if num_simulations <= 0:
            print("Invalid number of simulation.")
            return
        champions = defaultdict(int)
        for _ in range(num_simulations):
            self.champion= self.run_full_simulation()
            champions[self.champion.name] += 1

        print("\n")
        print("=" * 60)
        print("Champion Statistics")
        print("=" * 60)

        for team, wins in sorted(
            champions.items(),
            key=lambda item:item[1],
            reverse=True):
            percent= wins * 100 / num_simulations

            print(
                f"{team:15}"
                f"{wins:5}"
                f"{percent:8.2f}%"
            )
