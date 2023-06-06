# put your solution here`

input_bus_stop = int(input())
input_bus_num = list(map(int, input().split()))
bus_continue_list = []
continue_list = []
input_bus_num.sort()
is_continue = False
min_value = 0
# 1, 2, 3, 7
for i in range(1, input_bus_stop):
    if input_bus_num[i] - input_bus_num[i - 1] == 1:
        if not is_continue:
            min_value = input_bus_num[i - 1]
        else:
            is_continue = True
        bus_continue_list.extend([input_bus_num[i-1]])
        bus_continue_list.extend([input_bus_num[i]])
    else:
        val_str = str(min_value)
        min_value = 0
        is_continue = False
continue_list = list(set(bus_continue_list))
continue_list.sort()
print(continue_list)









