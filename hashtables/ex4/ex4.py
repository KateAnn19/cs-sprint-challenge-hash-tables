def has_negatives(a):
    """
    YOUR CODE HERE
    """
    nums_dict = {}
    nums_list = []
    # Your code here
    # loop over every item in the arry
    for i in a:
        # take the absolute value of ever item
        pos = abs(i)
        # check to see if the number exists in the dictionary or not, if it doesn't add it
        if pos not in nums_dict:
            nums_dict[pos] = 1
        # if it does exist then add check to see if it's already in the list and if not then add to the list 
        else:
            if pos not in nums_list:
                nums_list.append(pos)
    # return the list of pos numbers containing negative numbers            
    return nums_list


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))


    # input is a list
    # output is a list of positive integers that had corresponding negative numbers 

    # loop over list and check if 
