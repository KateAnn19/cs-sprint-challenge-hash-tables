# Your code here
import re



def finder(files, queries):
    """
    YOUR CODE HERE
    """

    #return [str for str in files if any(sub in str for sub in queries)]
    # return [str for str in files if
    #          any(sub in str for sub in queries)] 
    # return [str for str in files  
    # if re.match(r'[^\d]+|^', str).group(0) in queries] 
     # turn queries into a dictionary
    #sub = dict.fromkeys(files, "find subs")
    sub_2 = dict.fromkeys(queries, "subs")
    # #print(sub)
    subs_list = []
    # #loop over files and see if querie exists in the files, if it does append it into a list
    # #loop over dictionary and see if queries are in the files 
    for w in files:
        split_string = w.split("/")[-1]
        if split_string in sub_2:
            subs_list.append(w)
    return subs_list


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
