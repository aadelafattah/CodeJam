class Module:
    def __init__(self, fun, index, visited = False, next = None, has_previous = False):
        self.fun = fun
        self.index = index
        self.visited = visited
        self.next = next
        self.has_previous = has_previous

def get_stacks(start_modules,modules):
    stacks = []
    for start in start_modules:
        stack = []
        current = start
        while(not current.next==-1):
            stack.append(current)
            current = modules[current.next]
        stack.append(current)
        stacks.append(stack)
    return stacks


def chain(stacks, modules):
    sum = 0
    for stack in stacks:
        max = 0
        while(not len(stack)==0):
            temp = stack.pop()
            if(modules[temp.index].visited == True):
                continue
            else:
                modules[temp.index].visited = True
                if(max<=temp.fun):
                    max=temp.fun
        sum+=max
    print(sum)
    

def start(modules):
    start_modules = []
    for module in modules:
        if(not module.has_previous):
            start_modules.append(module)
    stacks = get_stacks(start_modules, modules)
    stacks.sort(key=lambda x: (len(x), x[0].fun))
    chain(stacks, modules)


def main():
    T = int(input())
    for i in range (T):
        n = int(input())
        modules = []
        temp = input()
        f = list(map(int,temp.split()))
        temp = input()
        p = list(map(int,temp.split()))
        for m in range(n):
            modules.append(Module(f[m],m,next=p[m]-1, has_previous=m+1 in p))
        print("Case #", i+1, ": ",sep='', end='')
        start(modules)


if __name__ == "__main__":
    main()