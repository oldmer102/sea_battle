from colorama import Fore
from colorama import Style




def enemy_field(masiv_enemy):
    k = 1
    for row in masiv_enemy:
        a = ''
        for element in row:
            a += element + ' '
        yield (f"""{a}{Fore.RED} {k}{Style.RESET_ALL}""")
        k += 1

def your_field(masiv_you):
    k = 1
    for row in masiv_you:
        a = ''
        for element in row:
            a += element + ' '
        yield (f"""{a}{Fore.GREEN} {k}{Style.RESET_ALL}""")
        k += 1

def start_field(masiv_you,masiv_enemy):
    n = your_field(masiv_you)
    b = enemy_field(masiv_enemy)
    print(f"""{Fore.GREEN}А Б В Г Д Е {Style.RESET_ALL}       {Fore.RED}А Б В Г Д Е {Style.RESET_ALL}""")
    try:
        while 1:
            print(n.__next__(), "   ", b.__next__())
    except StopIteration:
        pass









