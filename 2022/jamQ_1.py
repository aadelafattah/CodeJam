T = 0

def print_separator(flag,first, rest, number):
    if(flag):
        print("", first, rest*number, sep='')
    else:
        print("+", first, rest*number, sep='')

def print_line(flag,first, rest, number):
    if(flag):
        print("", first, rest*number, sep='')
    else:
        print("|", first, rest*number, sep='')


def card(r,c):
    first = True
    first_seperator = "..+"
    separator = "-+"
    first_cell = "..|"
    cell = ".|"
    for i in range(r):
        if(first):
            print_separator(first,first_seperator,separator,c-1)
            print_line(first,first_cell,cell, c-1)
            first = False
        else:
            print_separator(first,separator,separator,c-1)
            print_line(first,cell,cell, c-1)
    print_separator(first,separator,separator,c-1)


def main():
    T = int(input())
    for i in range (T):
        r , c = map(int, input().split()) 
        print("Case #", i+1, ":", sep='')
        card(r,c)


if __name__ == "__main__":
    main()