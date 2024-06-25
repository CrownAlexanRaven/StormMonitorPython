def retract_lines(lines):
    for _ in range(lines):
        print('\033[1A\033[2K', end='', flush=True)

def exit_and_retract(lines, status=0):
    retract_lines(lines)
    print('\nExiting...\n\033[2K')
    exit(status)