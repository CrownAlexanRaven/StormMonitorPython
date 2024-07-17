def retract_lines(lines):
    for _ in range(lines):
        print('\033[2K\033[1A', end='', flush=True)
        print('\033[2K', end='', flush=True)

def exit_and_retract(lines, status=0):
    retract_lines(lines)
    print('\nExiting...\n\033[2K', flush=True)
    exit(status)
    