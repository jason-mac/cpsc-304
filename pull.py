#!/usr/bin/env python3

import subprocess


def main():
    """Run a hardcoded shell command and print the result."""
    command = "git pull"

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


if __name__ == "__main__":
    main()
