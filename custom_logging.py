from colorama import Fore, init

init(strip=False)

def tag(color, tagname):
    return f"{Fore.WHITE}[{color}{tagname}{Fore.WHITE}] "

def info(m, success=False, **kwargs):
    return print(f"{tag(Fore.CYAN, 'INFO')}{m if not success else Fore.GREEN + m + Fore.RESET}", **kwargs)

def warning(m, **kwargs):
    return print(f"{tag(Fore.RED, 'WARNING')}{Fore.LIGHTRED_EX} {m}{Fore.RESET}", **kwargs)

def debug(m, **kwargs):
    return print(f"{tag(Fore.GREEN, 'DEBUG')}{Fore.RESET} {m}", **kwargs)

def error(err, **kwargs):
    print(f"{tag(Fore.RED, 'ERROR')}{Fore.LIGHTRED_EX} An error occured, please message the developer the following message{Fore.RESET}\n{Fore.RED}{err}{Fore.RESET}", **kwargs)
    exit()

def custom_input(m, **kwargs):
    print(f"{tag(Fore.LIGHTBLUE_EX, 'INPUT')}{Fore.RESET} {m}", **kwargs)
    return input()

def custom(m, color, bold = False, reset = False, **kwargs):
    b = '\033[1m'
    return print(f"{b if bold else ''}{color}{m}{Fore.RESET if reset else ''}", **kwargs)

if __name__ == "__main__":
    info("test")
    warning("test")
    debug("test")
    error("TEST ERROR MESSAGE")
    custom_input("test input")