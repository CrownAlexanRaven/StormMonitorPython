import platform
import socket
import psutil
import functions
from uuid import getnode as get_mac
from colorama import Fore, Style, init

init()

hostname = socket.gethostname()

try:
    ipv4_address = socket.gethostbyname(hostname)
except socket.gaierror:
    ipv4_address = "Not available"

try:
    ipv6_address = socket.getaddrinfo(hostname, None, socket.AF_INET6)[0][4][0]
except (socket.gaierror, IndexError):
    ipv6_address = "Not available"

mac_num = get_mac()
mac = ':'.join(('%012X' % mac_num)[i:i+2] for i in range(0, 12, 2))

# Get system and network information
cpu_cores = psutil.cpu_count(logical=True)
disk_info = psutil.disk_usage('/')

# Print system information
print(f"""{Fore.GREEN}System Information
{Fore.MAGENTA}Device Name:{Style.RESET_ALL} {platform.node()}
{Fore.CYAN}Machine Architecture:{Style.RESET_ALL} {platform.machine() if platform.machine() else "Not Found"}
{Fore.LIGHTYELLOW_EX}CPU Cores:{Style.RESET_ALL} {cpu_cores}
{Fore.BLUE}Operating System:{Style.RESET_ALL} {platform.system() if platform.system() else "Not Found"} {platform.release()}
{Fore.LIGHTRED_EX}IPv4 Address:{Style.RESET_ALL} {ipv4_address}
{Fore.LIGHTRED_EX}IPv6 Address:{Style.RESET_ALL} {ipv6_address}
{Fore.YELLOW}MAC Address:{Style.RESET_ALL} {mac}
{Fore.CYAN}Total Disk Space:{Style.RESET_ALL} {disk_info.total // (1024 ** 3)} GB
{Fore.CYAN}Used Disk Space:{Style.RESET_ALL} {disk_info.used // (1024 ** 3)} GB
{Fore.CYAN}Free Disk Space:{Style.RESET_ALL} {disk_info.free // (1024 ** 3)} GB\n\n
""")

# Wait for user input before closing
input('Press enter to close menu.')

# Exit the program with a delay
functions.exit_and_retract(15)