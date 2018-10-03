BOLD = '\033[1m'
ENDC = '\033[0m'
FAIL = '\033[91m'
HEADER = '\033[95m'
OK_BLUE = '\033[94m'
OK_GREEN = '\033[92m'
UNDERLINE = '\033[4m'
WARNING = '\033[93m'


def print_bold(string):
    print(BOLD + string + ENDC)


def print_fail(string):
    print(FAIL + string + ENDC)


def print_header(string):
    print(HEADER + string + ENDC)


def print_ok_blue(string):
    print(OK_BLUE + string + ENDC)


def print_ok_green(string):
    print(OK_GREEN + string + ENDC)


def print_underline(string):
    print(UNDERLINE + string + ENDC)


def print_warning(string):
    print(WARNING + string + ENDC)


