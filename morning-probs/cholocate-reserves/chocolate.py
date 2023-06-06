input_list = list(map(int, input().split()))
cholocate_input = []
count = 0
for k in range(input_list[1]):
    cholocate_input.append(list(map(int, input().split())))

for i in cholocate_input:
    if i[1] - i[0] >= input_list[0]:
        count += 1
print(count)



