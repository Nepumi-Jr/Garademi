"""
    Use for print
"""

from sys import platform


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def printWarning(text):
    if platform == "linux" or platform == "linux2":
        print(f"{bcolors.WARNING}/!\\ Warnning:{text}{bcolors.ENDC}")
    elif platform == "darwin":
        print(f"{bcolors.WARNING}/!\\ Warnning:{text}{bcolors.ENDC}")
    else:
        print(f"/!\\ Warnning : {text}")

def printError(text):
    if platform == "linux" or platform == "linux2":
        print(f"{bcolors.FAIL}\a(X) Error:{text}{bcolors.ENDC}")
    elif platform == "darwin":
        print(f"{bcolors.FAIL}\a(X) Error:{text}{bcolors.ENDC}")
    else:
        print(f"\a(X) Error : {text}")

def printLog(text):
    if platform == "linux" or platform == "linux2":
        print(f"{bcolors.OKGREEN}- {text}{bcolors.ENDC}")
    elif platform == "darwin":
        print(f"{bcolors.OKGREEN}- {text}{bcolors.ENDC}")
    else:
        print(f"- {text}")

def printAnnou(text):
    if platform == "linux" or platform == "linux2":
        print(f"\n{bcolors.OKCYAN}<o> {text}{bcolors.ENDC}")
    elif platform == "darwin":
        print(f"\n{bcolors.OKCYAN}<o> {text}{bcolors.ENDC}")
    else:
        print(f"\n<o> {text}")

if __name__ == "__main__":
    printWarning("Test Warnning")
    printError("Test Error")

