n = int(input("Give a number to search for: "))

l = [7, 10, 20, 15, 5]

def search(n, l):
    found = False
    for i in l:
        if i == n:
            print(f"found {l.index(i)}")
            found = True

    if found == False:
        print(f"Number not found {n}")

search(n, l)

"""
Linear = Lists, Stacks, Queues
Non-Linear = Graphs, Trees (Different Levels)

DSA = Data structures and Algorithms
            |               \> The different steps you give to complete an end goal.                   
A way to store, process or organize data in an efficient way                 

Time Complexity - The amount of iterations or time it takes to run an algorithm with different inputs
Space Complexity - The amount of memory an algorithm takes up to run and complete
"""
    
    