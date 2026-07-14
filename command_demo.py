import subprocess
import sys


DRY_RUN = True


def run_command(command):
    print("\nCommand:", " ".join(command))

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
            print("Command output:")
            print(result.stdout)

        return True

    except subprocess.CalledProcessError as error:
        print("The command failed.")

        if error.stderr:
            print("Error output:")
            print(error.stderr)

        return False


# A command that succeeds
successful_command = [
    sys.executable,
    "-c",
    "print('Hello from the subprocess!')"
]

# A command that deliberately fails
failing_command = [
    sys.executable,
    "-c",
    (
        "import sys; "
        "print('This is an example error.', file=sys.stderr); "
        "sys.exit(1)"
    )
]


print("\n===== DEMONSTRATION 1: DRY RUN =====")

DRY_RUN = True
success = run_command(successful_command)
print("Returned value:", success)


print("\n===== DEMONSTRATION 2: SUCCESSFUL COMMAND =====")

DRY_RUN = False
success = run_command(successful_command)
print("Returned value:", success)


print("\n===== DEMONSTRATION 3: FAILED COMMAND =====")

success = run_command(failing_command)
print("Returned value:", success)