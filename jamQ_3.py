def straight(sorted):
    straight = 0
    for i in range(len(sorted)):
        if(straight<sorted[i]):
            straight+=1
    return straight

def main():
    T = int(input())
    for i in range (T):
        n = int(input())
        d = input()
        s = list(map(int,d.split()))
        s.sort()
        print("Case #", i+1, ": ", straight(s),sep='')


if __name__ == "__main__":
    main()