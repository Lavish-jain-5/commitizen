#!/usr/bin/env python3

import subprocess
import re

def tag_exists(tag):
    result = subprocess.run(["git", "tag", "--list", tag], capture_output=True, text=True)
    output = result.stdout.strip()
    return output == tag

def main():
    # Execute your post-commit actions here
    print("Running post-commit actions...")
    result = subprocess.run(["cz", "bump", "--check-consistency", "--changelog"], capture_output=True, text=True)
    output = result.stdout.strip()
    match = re.search(r"bump: version \S+ → (\S+)", output)
    if match:
        bumped_version = match.group(1)
        if not tag_exists(bumped_version):
            subprocess.run(["git", "tag", bumped_version])
            print(f"I  Tag '{bumped_version}' created successfully.")
        else:
            print(f"Really Tag '{bumped_version}' already exists.")
    else:
        print(" A Version bump not detected.")

if __name__ == "__main__":
    main()