# import os
import subprocess
import re

DRY_RUN = False # False for no safety mode

def is_valid_username(username):
    pattern = r"^[a-z_][a-z0-9_-]{0,31}$"
    return re.fullmatch(pattern, username) is not None




def run_command(command):
    print("\nCommand:"," ".join(command))

    if DRY_RUN:
        print("Simulation mode: command was not executed.")
        return True
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True
        )

        if result.stdout:
            print(result.stdout)
        
        return True

    except subprocess.CalledProcessError as error:
        print("The command failed!")

        if error.stderr:
            print(error.stderr)
        
        return False





def get_username(message):
    while True:
        username = input(message).strip().lower()

        if is_valid_username(username):
            return username
        

        print("Invalid username.")
        print("User names can not start with hyphens or numbers , it can contain: numbers, underscores, or hyphens.")


def confirm_action(message):
    while True:
        answer = input(f"{message} (Y/N): ").strip().upper()

        if answer == "Y" or answer == "YES":
            return True
        
        if answer == "N" or answer == "NO":
            return False
        
        print("Please enter Y or N.")


def add_user():
    print("\n---Add User---")

    username = get_username(
        "Enter the name of the user to create: "
    )

    confirmed = confirm_action(
        f"Are you sure to create user '{username}'?"
    )

    if not  confirmed:
        print("User creation being cancelled.")
        return

    command = [
        "sudo",
        "useradd",
        "-m",
        username
    ]

    success = run_command(command)

    if success:
        print(f"User '{username}' was proccessed successfully.")


add_user()
