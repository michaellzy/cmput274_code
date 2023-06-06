n = int(input())
city_dict = {}
for i in range(n):
    # now get the two city strings for each of the first n lines
    # Hint: Consider using a dictionary here...
    # replace the pass keyword below with your code
    start, des = input().split("---")
    city_dict[start] = des
print(city_dict)
# you still have to read in the 2nd part of the input
# which consists of the value q followed by the q query lines
q = int(input())
for k in range(q):
    pass

# for each query, calculate and print the answer
