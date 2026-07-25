#worldcup_simulator.py
#مبینا 
#عنوان پروژه:شبیه سازی جام جهانی
#تاریخ تحویل:1405/4/27

import csv
import random
import os
import numpy as np
from collections import defaultdict
from Classteam import Team
from Classmatch import Match
from Classgroup import Group
from Classknockoutstage import knockoutstage
from Classworldcupsimulator import WorldCupSimulator

def main():
    simulator=WorldCupSimulator()
    while True:
        print("\n===== World Cup Simulator =====")
        print("1. Load teams from CSV")
        print("2. Draw groups")
        print("3. Run group stage")
        print("4. Run full tournament")
        print("5. Simulate many tournaments")            
        print("6. Display knockout bracket")
        print("7. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            filename = input("CSV file name: ")
            simulator.load_teams(filename)
        elif choice == "2":
            if len(simulator.teams) == 0:
                print("Load teams first.")
                continue
            simulator.draw_groups()
        elif choice == "3":
            if len(simulator.groups) == 0:
                print("Draw groups first.")
                continue
            simulator.play_group_stage()
        elif choice == "4":
            if len(simulator.teams) == 0:
                print("Load teams first.")
                continue
            champion = simulator.run_full_simulation()
            print("\nChampion:", champion.name)
        elif choice == "5":
            if len(simulator.teams) == 0:
                print("Load teams first.")
                continue
            number = input("Number of simulations (Default=1000): ")
            if number == "":
                number = 1000
            else:
                number = int(number)
            simulator.simulate_many(number)
        elif choice == "6":
            simulator.display_bracket()
        elif choice == "7": 
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
if __name__ == "__main__":
    main()