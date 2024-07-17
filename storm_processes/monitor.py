from colorama import Fore, Style
import psutil, time
import functions

def gb_calculation(value):
    return f"{value / (1024 ** 3):.2f}"

try:
    psutil.cpu_percent(interval=1)
    while True:
        cpu = psutil.cpu_percent(interval=0)
        ram = psutil.virtual_memory()
        swap = psutil.swap_memory()
        print(Fore.LIGHTYELLOW_EX + "Processer Load: " + Style.RESET_ALL + f'{cpu}%', flush=True)
        print(Fore.LIGHTMAGENTA_EX + "Total RAM: " + Style.RESET_ALL + f"{gb_calculation(ram.total)} GB", flush=True)
        print(Fore.LIGHTMAGENTA_EX + "Available RAM: " + Style.RESET_ALL + f"{gb_calculation(ram.available)} GB", flush=True)
        print(Fore.LIGHTMAGENTA_EX + "Used RAM: " + Style.RESET_ALL + f"{gb_calculation(ram.used)} GB", flush=True)
        print(Fore.LIGHTMAGENTA_EX + "RAM usage percentage: " + Style.RESET_ALL + f'{ram.percent}%', flush=True)
        print(Fore.LIGHTGREEN_EX + "Total Swap: " + Style.RESET_ALL + f"{gb_calculation(swap.total)} GB", flush=True)
        print(Fore.LIGHTGREEN_EX + "Used Swap: " + Style.RESET_ALL + f"{gb_calculation(swap.used)} GB", flush=True)
        print(Fore.LIGHTGREEN_EX + "Free Swap: " + Style.RESET_ALL + f"{gb_calculation(swap.free)} GB", flush=True)
        print(Fore.LIGHTGREEN_EX + "Swap usage percentage: " + Style.RESET_ALL + f"{swap.percent}%", flush=True)
        print("\nPress CMD+C or CTRL+C to exit", flush=True)
        time.sleep(1)
        functions.retract_lines(11)
except KeyboardInterrupt:
    functions.exit_and_retract(11)
except Exception as e:
     print(f"Exception has occured: {e}")

