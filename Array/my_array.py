# play with array
'''
operations
    1) insert (start,mid,end)
    2) Delete (same 3 ops)
'''

# Basic functions
def give_array(size: int) -> list:
    return [None for _ in range(size)]

def length(li:list) -> int: 
    size = 0
    for ele in li :
        if ele != None:
            size += 1
    return size

def print_array(li:list)->None :
    if li[0] == None :
        raise ValueError("Empty array")
    for ele in li :
        if ele == None :
            print()
            break
        else :
            print(ele,end=" ") # I want felling 

# Add elements functions
def add_on_zero(array: list, value: int) -> None:
    size = length(array)

    if size == len(array):
        raise("Array is full!") # error :))
        return

    for i in range(size, 0, -1):
        array[i] = array[i-1]

    array[0] = value

def add_at_last(array: list,value:int):
    size = length(array)
    array[size] = value

def add_at_mid(array,value,idx):
    size = length(array)
    for i in range(size,idx,-1):
        array[i] = array[i-1]
    array[idx] = value

# remove elements functions
def remove_at_zero(array: list) -> None:
    size = length(array)
    for i in range(1, size):
        array[i-1] = array[i]
    array[size-1] = None

def remove_at_last(li):
    size = length(li)
    li[size-1] = None

def remove_at_mid(li,idx):
    size = length(li)
    for i in range (idx,size):
        if i+1 < size :
            li[i] = li[i+1] 
    if li[size-1] != None:
        li[size-1] = None

if __name__ =="__main__" :
    li = give_array(5)

    add_on_zero(li, 10)
    add_on_zero(li, 20)
    add_at_last(li, 30)
    add_at_mid(li,80,2)

    #add_on_zero(li, 30)

    print_array(li)

    remove_at_zero(li)
    print_array(li)

    remove_at_last(li)
    print_array(li)

    remove_at_mid(li,1)
    print_array(li)

    # remove_at_zero(li)
    # print("After removing from zero")
    # ## Expect error
    # print_array(li)
                

