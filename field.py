from colorama import Fore
from colorama import Style

def enemy_field():
    X = 6
    Y = 6
    k = 1
    masiv_a = [['-'] * X for i in range(Y)]

    for row in masiv_a:
        a = ''
        for element in row:
            a += element + ' '
        yield (f"""{a}{Fore.RED} {k}{Style.RESET_ALL}""")
        k += 1



def your_field():
    X = 6
    Y = 6
    k = 1
    masiv_a = [['-'] * X for i in range(Y)]

    for row in masiv_a:
        a = ''
        for element in row:
            a += element + ' '
        yield (f"""{a}{Fore.GREEN} {k}{Style.RESET_ALL}""")
        k += 1

def start_field():
    n = your_field()
    b = enemy_field()
    print(f"""{Fore.GREEN}1 2 3 4 5 6 {Style.RESET_ALL}       {Fore.RED}1 2 3 4 5 6 {Style.RESET_ALL}""")
    try:
        while 1:
            print(n.__next__(), "   ", b.__next__())
    except StopIteration:
        pass









