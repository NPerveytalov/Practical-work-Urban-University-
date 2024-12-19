my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
Quantity_in_list =  len(my_list)
var = 0
while var < Quantity_in_list:
    if my_list [var] == 0:
        var = var + 1
        continue
    elif my_list [var] > 0:
        print(my_list[var])
        var = var + 1
    elif my_list [var] < 0:
        break
