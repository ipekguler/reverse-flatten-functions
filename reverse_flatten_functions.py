def isList(element):
    if type(element) is list:
        return True
    else:
        return False

def reverse(given_list):
    result = list()
    for element in given_list:
        if isList(element):
            result.append(reverse(element))
        else:
            result.append(element)
    result.reverse()
    return result

def flatten(given_list):
    result = list()
    while given_list:
        element = given_list.pop(0)
        if isList(element):
            given_list = element + given_list
        else:
            result.append(element)
    return result


if __name__ == "__main__":
    
    list_1=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
    print(flatten(list_1))
    
    list_2=[[[1, 2], [3, 4], [5, 6, 7]]]
    print(reverse(list_2))