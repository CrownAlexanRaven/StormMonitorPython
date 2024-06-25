from colorama import Fore, Style, init
import runpy, os
import functions

init()

storm_processes = [
    {
        "name": "System Information",
        "desc": "Basic infomation about your system",
        "path": "sysinfo.py",
        "colour": "GREEN",
    },
    {
        "name": "Resource Monitor",
        "desc": "A basic ",
        "path": "monitor.py",
        "colour": "BLUE",
    },
]
color_map = {
    "BLACK": Fore.LIGHTBLACK_EX,
    "RED": Fore.LIGHTRED_EX,
    "GREEN": Fore.LIGHTGREEN_EX,
    "YELLOW": Fore.LIGHTYELLOW_EX,
    "BLUE": Fore.LIGHTBLUE_EX,
    "MAGENTA": Fore.LIGHTMAGENTA_EX,
    "CYAN": Fore.LIGHTCYAN_EX,
    "WHITE": Fore.LIGHTWHITE_EX,
    "RESET": Style.RESET_ALL,
}
path = os.path.dirname(__file__)

for index, process in enumerate(storm_processes):
    print(
        f"{color_map[process['colour']]}[{index}={process['name']}]{Style.RESET_ALL} {process['desc']}{Style.RESET_ALL}"
    )

try:
    choice = int(input("Please enter your choice:"))
except Exception as failure:
    print(f"Failure: {failure}")
    exit(1)
except KeyboardInterrupt:
    functions.exit_and_retract(2, 0)
try:
    functions.retract_lines(3)
    runpy.run_path(f'{path}/{storm_processes[choice]["path"]}')
except Exception as failure:
    print(f"Failure: {failure}")
