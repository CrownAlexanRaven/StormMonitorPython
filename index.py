# Left here for a hash/shebang letter edit in a possible setup script I might make
from colorama import Fore, Style, init
import runpy, os

init()

storm_processes = [
    {'name': 'System Information', 'desc': 'Basic infomation about your system', 'path': 'sysinfo.py', 'colour': 'GREEN'},
    {'name': 'Resource Monitor', 'desc': 'A basic ', 'path': 'monitor.py', 'colour': 'BLUE'},
]
color_map = {
    'BLACK': Fore.BLACK,
    'RED': Fore.RED,
    'GREEN': Fore.GREEN,
    'YELLOW': Fore.YELLOW,
    'BLUE': Fore.BLUE,
    'MAGENTA': Fore.MAGENTA,
    'CYAN': Fore.CYAN,
    'WHITE': Fore.WHITE,
    'RESET': Style.RESET_ALL
}
path = os.path.dirname(__file__)

for index, process in enumerate(storm_processes):
    print(f"{color_map[process['colour']]}[{index}={process['name']}]{Style.RESET_ALL} {process['desc']}{Style.RESET_ALL}")

try:
    choice = int(input('Please enter your choice:'))
except Exception as failure:
    print(f'Failure: {failure}')
    exit(1)
try:
    runpy.run_path(f'{path}/{storm_processes[choice]["path"]}')
except Exception as failure:
    print(f'Failure: {failure}')
