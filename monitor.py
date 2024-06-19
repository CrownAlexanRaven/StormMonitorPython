from colorama import Fore, Style, init
import psutil, time

init()

def gb_calculation(value):
    return f"{value / (1024 ** 3):.2f}"

def print_stats(cpu, ram, swap):
    print(Fore.YELLOW + "Processer Load: " + Style.RESET_ALL + f'{cpu}%', flush=True)
    print(Fore.MAGENTA + "Total RAM: " + Style.RESET_ALL + f"{gb_calculation(ram.total)} GB", flush=True)
    print(Fore.MAGENTA + "Available RAM: " + Style.RESET_ALL + f"{gb_calculation(ram.available)} GB", flush=True)
    print(Fore.MAGENTA + "Used RAM: " + Style.RESET_ALL + f"{gb_calculation(ram.used)} GB", flush=True)
    print(Fore.MAGENTA + "RAM usage percentage: " + Style.RESET_ALL + f'{ram.percent}%', flush=True)
    print(Fore.GREEN + "Total Swap: " + Style.RESET_ALL + f"{gb_calculation(swap.total)} GB")
    print(Fore.GREEN + "Used Swap: " + Style.RESET_ALL + f"{gb_calculation(swap.used)} GB")
    print(Fore.GREEN + "Free Swap: " + Style.RESET_ALL + f"{gb_calculation(swap.free)} GB")
    print(Fore.GREEN + "Swap usage percentage: " + Style.RESET_ALL + f"{swap.percent}%")

try:
    psutil.cpu_percent(interval=1)
    while True:
        c = psutil.cpu_percent(interval=0)
        r = psutil.virtual_memory()
        s = psutil.swap_memory()
        print_stats(c, r, s)
        time.sleep(1)
        for _ in range(9):
            print('\033[1A\033[2K', end='', flush=True)
except KeyboardInterrupt:
    for _ in range(9):
            print('\033[1A\033[2K', end='', flush=True)
    print("\nExiting...")
except Exception as e:
     print(f"Exception has occured: {e}")

