def safe_print_integers(my_list=[], x=0):
        ret = 0
        for num in range(0, x):
            try:
                print("{:d}".format(my_list[num]), end="")
                ret += 1
            except (ValueError, TypeError):
