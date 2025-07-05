#!/usr/bin/env python3

import subprocess


def run_command(command):
    """function for pulling"""
    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            text=True,
            capture_output=True,
        )
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Command failed with exit code {e.returncode}")
        print(f"Error output:\n{e.stderr}")


def add():
    """function for adding"""
    command = "git add ."
    run_command(command)


def commit():
    """function for committing"""
    command = 'git commit -m "update"'
    run_command(command)


def push():
    """function for pushing"""
    command = "git push"
    run_command(command)


def main():
    """Run a hardcoded shell command and print the result."""
    add()
    commit()
    push()


if __name__ == "__main__":
    main()
