def product_except_index(my_list):
    prod_list = []
    temp_list = []

    temp_list = list(my_list)
    # look into copy and deepcopy

    if len(my_list) > 0:
        # print("This is my original list: %s" % my_list)
        for num in my_list:
            # print("number being used is: %s" % num)
            # print("temp_list before pop is: %s" % temp_list)
            # print("temp_list will pop: %s " % temp_list[0])
            temp_list.pop(0)
            # print("temp_list after pop is: %s " % temp_list)
            # print("my_list is: %s" % my_list)
            result = 1
            # print("declared result to be 1 ")
            for x in temp_list:
                result = result * x
                # print("Result variable = %s " % result)
            prod_list.append(result)
            temp_list.append(num)
            # print("Prod_list: %s " % prod_list)
    print("Final solution: %s " % prod_list)


if __name__ == "__main__":
    product_except_index([10,20,30,40,50,60,70,80,90,100])
