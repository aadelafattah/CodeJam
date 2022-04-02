import itertools
import copy

class Module:
    def __init__(self, fun, index, visited = False, next = None, has_previous = False):
        self.fun = fun
        self.index = index
        self.visited = visited
        self.next = next
        self.has_previous = has_previous

def chain(start, modules):
    stack = []
    current = start
    while(not current.next==-1 and modules[current.next].visited==False):
        stack.append(current)
        modules[current.index].visited = True
        current = modules[current.next]
    stack.append(current)
    modules[current.index].visited = True
    max = 0
    while(not len(stack)==0):
        temp = stack.pop().fun
        if(max < temp):
            max = temp
    return max

def start(modules):
    start_modules = []
    sums=[]
    for module in modules:
        if(not module.has_previous):
            start_modules.append(module)
    
    permutations = list(itertools.permutations(start_modules))
    for p in permutations:
        copy_modules = copy.deepcopy(modules)
        sum = 0
        for start in p:
            sum+=chain(start,copy_modules)
        sums.append(sum)
    return max(sums)

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
        print("Case #", i+1, ": ", start(modules),sep='')


if __name__ == "__main__":
    main()