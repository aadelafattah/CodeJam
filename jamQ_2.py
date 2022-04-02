def printer(cyan,magenta,yellow,black):
    max_c = min(cyan)
    max_m = min(magenta)
    max_y = min(yellow)
    max_k = min(black)
    if(max_c + max_m + max_y + max_k < 1000000):
        return False
    elif(max_c + max_m + max_y + max_k == 1000000):
        print(max_c,max_m,max_y,max_k)
    else:
        max_colors = [max_c,max_m,max_y,max_k]
        sum = 0
        i = 0
        for i in range(len(max_colors)):
            remainder = 1000000 - sum
            if(max_colors[i]<=remainder):
                sum+=max_colors[i]
            else:
                sum+=remainder
                max_colors[i]=remainder
        print(max_colors[0], max_colors[1], max_colors[2], max_colors[3])
    return True


def main():
    T = int(input())
    for i in range (T):
        c1, m1, y1, k1 = map(int, input().split())
        c2, m2, y2, k2 = map(int, input().split())
        c3, m3, y3, k3 = map(int, input().split())
        cyan = [c1,c2,c3]
        magenta = [m1,m2,m3]
        yellow =[y1,y2,y3]
        black = [k1,k2,k3]
        print("Case #", i+1, ": ", sep='', end='')
        if(not printer(cyan,magenta,yellow,black)):
            print("IMPOSSIBLE")


if __name__ == "__main__":
    main()