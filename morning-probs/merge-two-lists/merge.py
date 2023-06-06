# Get the input
input_list1 = input().split()
input_list2 = input().split()

new_list1 = []
new_list2 = []

for i in input_list2:
    new_list2.append(i)
for index in range(len(input_list1)):
    new_list2.insert(index * 2, input_list1[index])

print(" ".join(new_list2))
