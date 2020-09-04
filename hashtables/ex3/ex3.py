def intersection(arrays):
    """
    YOUR CODE HERE
    """
    nums_dict = {}
    nums_list = []
    # Your code here
    # loop through the first array
    for i in range(len(arrays)):
        # loop through all sub arrays
        for j in range(len(arrays[i])):
            # if number is not in the dictionary
            if arrays[i][j] not in nums_dict:
                # add the number 
                nums_dict[arrays[i][j]] = 1
            else:
                # if it is in the dictionary add 1
                nums_dict[arrays[i][j]] += 1
                # if the value of the key in the dictionary equals the length of the arrays, then append it to the list
                if nums_dict[arrays[i][j]] == len(arrays):
                    nums_list.append(arrays[i][j])
    # return the list of numbers that exist in all the lists 
    return nums_list


if __name__ == "__main__":
    arrays = []
    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

    # input is an array of arrays
    # output is a list of numbers that exist in all the lists 
