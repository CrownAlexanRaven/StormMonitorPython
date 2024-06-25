import platform, socket, psutil, functions
from uuid import getnode as get_mac
from colorama import Fore, Style, init

init()

def get_network_info():
    hostname = socket.gethostname()
    try:
        ip_address_v4 = socket.gethostbyname(hostname)
    except socket.gaierror:
        ip_address_v4 = "Not available"
    
    try:
        ip_address_v6 = socket.getaddrinfo(hostname, None, socket.AF_INET6)[0][4][0]
    except (socket.gaierror, IndexError):
        ip_address_v6 = "Not available"
    
    return ip_address_v4, ip_address_v6

def get_mac_address():
    mac_num = get_mac()
    mac = ':'.join(('%012X' % mac_num)[i:i+2] for i in range(0, 12, 2))
    return mac
system_name = platform.node()
machine_architecture = platform.machine() if platform.machine() else "Not Found"
operating_system = platform.system() if platform.system() else "Not Found"
os_version = platform.release()
ipv4address, ipv6address = get_network_info()
mac_address = get_mac_address()
cpu_cores = psutil.cpu_count(logical=True)
cpu_usage = psutil.cpu_percent(interval=1)
memory_info = psutil.virtual_memory()
disk_info = psutil.disk_usage('/')
total_disk = disk_info.total // (1024 ** 3)
used_disk = disk_info.used // (1024 ** 3)
free_disk = disk_info.free // (1024 ** 3) 

print(f"""{Fore.GREEN}System Information
{Fore.MAGENTA}Device Name:{Style.RESET_ALL} {system_name}
{Fore.CYAN}Machine Architecture:{Style.RESET_ALL} {machine_architecture}
{Fore.BLUE}Operating System:{Style.RESET_ALL} {operating_system} {os_version}
{Fore.LIGHTRED_EX}IPv4 Address:{Style.RESET_ALL} {ipv4address}
{Fore.LIGHTRED_EX}IPv6 Address:{Style.RESET_ALL} {ipv6address}
{Fore.YELLOW}MAC Address:{Style.RESET_ALL} {mac_address}
{Fore.CYAN}Total Disk Space:{Style.RESET_ALL} {total_disk} GB
{Fore.CYAN}Used Disk Space:{Style.RESET_ALL} {used_disk} GB
{Fore.CYAN}Free Disk Space:{Style.RESET_ALL} {free_disk} GB\n\n
""")

input('Press enter to close menu.')
functions.exit_and_retract(14)
