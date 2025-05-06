
mem_1 = {}

def fact(n,mem_1):
    if n == 1:
        return 1
    if n in mem_1:
        print(n, "from memory")
        return mem_1[n] 
    mem_1[n] = (n * fact(n-1,mem_1))
    return mem_1[n] 

# print(fact(5,mem_1))
# print(fact(3,mem_1))

mem = {}

def fib(n, mem):
    if n == 0 or n == 1:
        return 1
    if n in mem:
        print(n, "from memory")
        return mem[n] 
    mem[n] = (fib(n-1,mem) + fib(n-2,mem))
    return mem[n]

# print(fib(5,mem))

def fib_for(n):
    f = [0,1]
    if n == 0 or n == 1:
        return f
    for i in range(2,n+2):
        f.append(f[i-2]+f[i-1])
    return f[n+1]

# print(fib_for(5))

mem_2 = {0:1,1:1}

def fib_for_mem(n,mem_2):
    for i in range(2,n+2):
        mem_2[i]=(mem_2[i-2]+mem_2[i-1])
    return mem_2[n]

print(fib_for_mem(5,mem_2),mem_2)

    
