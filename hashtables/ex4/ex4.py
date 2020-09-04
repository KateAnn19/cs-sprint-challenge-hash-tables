def has_negatives(a):
    """
    YOUR CODE HERE
    """
    nums_dict = {}
    nums_list = []
    # Your code here
    for i in a:
        pos = abs(i)
        if pos not in nums_dict:
            nums_dict[pos] = 1
        else:
            nums_dict[pos] += 1
            if pos not in nums_list:
                nums_list.append(pos)
               
    return nums_list


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))


    # input is a list
    # output is a list of positive integers that had corresponding negative numbers 

    # loop over list and check if 
