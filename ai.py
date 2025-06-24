import os
from colorama import Fore

# List of suspicious keywords
bad_keywords = [
    "os.system", "eval", "exec", "subprocess", "socket",
    "base64", "requests.post", "open('/dev", "rm -rf"
]

def scan_file(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                for keyword in bad_keywords:
                    if keyword in line:
                        print(Fore.RED + f"[⚠️ ALERT] Suspicious keyword '{keyword}' found on line {i+1}")
        print(Fore.GREEN + "\n✅ Scan complete.")
    except Exception as e:
        print(Fore.YELLOW + f"[Error] Could not open the file: {e}")

print(Fore.CYAN + "🔍 Welcome! I'm DeepSeek's Friend.\n📁 Enter the filename to scan:")
target = input("> ")
scan_file(target)