## ==========================================
## Project: Rust Like Team System
## Author: Meakz
## Purpose: Rust Like Management Team
## ------------------------------------------
## Version: 1.0
## Created: 09/11/2026
## ==========================================

# IMPORTS

import os
import time

red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
purple = "\033[35m"
reset = "\033[0m"

bright_black = "\033[90m"
bright_red = "\033[91m"
bright_green = "\033[92m"
bright_yellow = "\033[93m"
bright_blue = "\033[94m"
bright_purple = "\033[95m"
bright_cyan = "\033[96m"
bright_white = "\033[97m"

team_created = False
team_max = 8
team_current = 0
owner_steam = ""
steam_id = ""
team_members = []

def save_team():
    with open("STEAMIDS.txt", "w") as file:
        file.write(f"STEAM TEAM OWNER ID LOGGER: {owner_steam}\n")
        for member in team_members:
            file.write(f"STEAM ID LOGGER: {member}\n")


def owner():
    global owner_steam

    print("Whats Your Steam id?")
    owner_steam = input(">> ").strip()

    if owner_steam == "":
        print("Invalid Steam ID!")
        return False

    return True


def delete_team():
    global team_created, team_current, owner_steam, team_members

    sure = input("Are you sure? (Y/n) >> ").strip().lower()

    if sure == "y":
        team_current = 0
        team_created = False
        owner_steam = ""
        team_members = []

        with open("STEAMIDS.txt", "w") as file:
            file.write("")

        print("Deleted Team!")
        time.sleep(2)
        return

    elif sure == "n":
        return

    else:
        print("Invalid!")
        time.sleep(2)


def check_team():
    if team_created == False:
        print("Create A Team First!")
        time.sleep(2)
        return False

    return True


def check():
    if team_current >= team_max:
        print("Team Full!")
        time.sleep(2)
        return False

    return True


def create_team():
    global team_created, team_current

    if team_created == True:
        print("Team Already Created!")
        time.sleep(1.3)
        return

    if owner() == False:
        time.sleep(2)
        return

    team_created = True
    team_current = 1
    save_team()

    print("Team Created!")
    time.sleep(1.3)


def add_team_member():
    global steam_id, team_current

    if check_team() == False:
        return

    if check() == False:
        return

    print("Who Do You Want To Invite? (Steam ID)")
    steam_id = input(">> ").strip()

    if steam_id == "":
        print("Invalid Steam ID!")
        return

    if steam_id == owner_steam or steam_id in team_members:
        print("Player Already In Team!")
        time.sleep(2)
        return

    team_members.append(steam_id)
    team_current += 1
    save_team()

    print("Finished!")
    time.sleep(1)


def get_team():
    if check_team() == False:
        return

    print("\nTEAM INFORMATION")
    print(f"Owner: {owner_steam}")
    print(f"Members: {team_current}/{team_max}")

    for member in team_members:
        print(f"- {member}")

    input("\nPress Enter To Continue...")


def remove_member():
    global team_current, team_members

    if check_team() == False:
        return

    print("Which Steam ID Do You Want To Remove?")
    steam_id = input(">> ").strip()

    if steam_id == owner_steam:
        print("You Cannot Remove The Team Owner!")
        time.sleep(2)
        return

    if steam_id not in team_members:
        print("Player Not Found!")
        time.sleep(2)
        return

    team_members.remove(steam_id)
    team_current -= 1
    save_team()

    print("Player Removed!")
    time.sleep(2)


def get_player_team():
    if check_team() == False:
        return

    print("Enter Steam ID:")
    steam_id = input(">> ").strip()

    if steam_id == owner_steam:
        print("Player Is The Team Owner!")

    elif steam_id in team_members:
        print("Player Is In This Team!")

    else:
        print("Player Not Found!")

    time.sleep(2)


def main_team_ui():
    os.system("cls")

    print(f"{bright_cyan}1. Create Team{reset}")
    print(f"{bright_cyan}2. Add Team Member{reset}")
    print(f"{bright_cyan}3. View Team{reset}")
    print(f"{bright_cyan}4. Remove Team Member{reset}")
    print(f"{bright_cyan}5. Find Player Team{reset}")
    print(f"{bright_red}6. Delete Team{reset}")

    choice_main = input(">> ")

    if choice_main == "1":
        create_team()

    elif choice_main == "2":
        add_team_member()

    elif choice_main == "3":
        get_team()

    elif choice_main == "4":
        remove_member()

    elif choice_main == "5":
        get_player_team()

    elif choice_main == "6":
        delete_team()

    elif choice_main == "dev":
        print(f"|team members: {team_current} | team max: {team_max} | team created: {team_created}|")
        time.sleep(3)

    else:
        print(f"{bright_red}Invalid Input.{reset}")
        time.sleep(1)

    main_team_ui()


main_team_ui()
