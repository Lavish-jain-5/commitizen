#!/usr/bin/env python3

import subprocess
import os
import re

def get_bumped_version():
    result = subprocess.run(["cz", "bump", "--dry-run", "--check-consistency", "--changelog"], capture_output=True, text=True)
    print(result)
    output = result.stdout
    print(output)
    match = re.search(r"bump: version (\S+) → (\S+)", output)
    print(match)
    if match:
        return match.group(2)
    else:
        return None

def main():
    # Execute your post-commit actions here
    print("Running post-commit actions...")
    bumped_version = get_bumped_version()
    if bumped_version:
        subprocess.call(["git", "tag", bumped_version])  # Create the Git tag

if __name__ == "__main__":
    main()
