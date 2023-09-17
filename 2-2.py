def sum_num(list):
    if list == []:
        return 0
    else:
        return list[0] + sum_num(list[1:])


while True:
    num = input("Enter integers separated by spaces ==>")

    try:
        if num == "done":
            print("program terminated. good bye !!")
            break
        else:
            split_num = num.split( )
            num_list = list(map(int, split_num))
            if len(num_list) == 1:
                print("must enter more than one integer")
                continue
            else:
                print(sum_num(num_list))
                continue
        
    except:
        print("must enter integers separated by spaces")
        continue