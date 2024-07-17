import os
from colorama import Fore, Style, init

init()

directory = input("Enter the directory path to analyze: ").strip()

if not os.path.isdir(directory):
    print(f"{Fore.RED}Error: {directory} is not a valid directory.{Style.RESET_ALL}")
    exit(1)

print(f"\n{Fore.GREEN}File Size Analyzer{Style.RESET_ALL}")
print(f"{Fore.BLUE}{'Relative Path':<80} {'Size (bytes)':>15}{Style.RESET_ALL}")
print('-' * 100)

line_count = 3  # Start with the count of initial lines printed
max_path_length = 0

for root, dirs, files in os.walk(directory):
    for name in files:
        file_path = os.path.join(root, name)
        relative_path = os.path.relpath(file_path, directory)
        file_size = os.path.getsize(file_path)

        # Update max_path_length if current path is longer
        max_path_length = max(max_path_length, len(relative_path))

        # Colorizing output with dynamic spacing
        print(f"{Fore.CYAN}{relative_path:<80}{Fore.MAGENTA} {file_size:>15}{Style.RESET_ALL}")
        line_count += 1  # Increment line count for each printed line

print(f'\n\n{Style.RESET_ALL}Complete.')