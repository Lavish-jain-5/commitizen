
import subprocess
import os
import re

def get_bumped_version():
    result = subprocess.run(["cz", "bump", "--check-consistency", "--changelog"], capture_output=True, text=True)
    output = result.stdout
    match = re.search(r"bump: version (\S+) → (\S+)", output)
    if match:
        bumped_version = match.group(2)
        subprocess.call(["git", "tag", bumped_version])
    else:
        return None

def main():
    # Execute your post-commit actions here
    print("Running post-commit actions...")
    get_bumped_version()