from sums import timer
# from time import time

# def time_it(func):
#     start= time()
#     func(*args, **kwargs)
#     end=time()
#     print("Run time: %s" % end-start)

def seq_search(array, element):
    position = 0
    found = False
    while position < len(array) and not found:
        print("SeqS Array position: %s" % array[position])
        if array[position] == element:
            found = True
        else:
            position += 1
    return found 

def my_ordered_seq_search(array,element):
    position = 0
    found = False
    while position < len(array) and not found:
        print("MyOrdSeqS Array position: %s" % array[position])
        if array[position] > element:
            break
        if array[position] == element:
            found = True
        else:
            position += 1
    return found 

def ordered_seq_search(array, element):
    position = 0
    found = False
    stopped = False
    while position < len(array) and not found and not stopped:
        print("OrdSeqS Array position: %s" % array[position])
        if array[position] == element:
            found = True
        else:
            if array[position] > element:
                stopped = True
            position += 1
    return found 

def binary_search(arr,ele):
    first = 0
    last = len(arr)-1
    found = False
    while first <= last and not found:
        print("First: %s | Last: %s" % (first, last))
        mid = int((first+last)/2)
        print("Mid: %s" % mid)
        if arr[mid] == ele:
            found = True
        else:
            if ele < arr[mid]:
                last = mid - 1
            else:
                first = mid + 1

    return found
# @timer
def rec_binary_search(arr,ele):
    if len(arr) == 0:
        return False
    else:
        mid = int(len(arr)/2)
        print("Mid: %s" % mid)
        if arr[mid]==ele:
            return True
        else:
            if ele<arr[mid]:
                return rec_binary_search(arr[:mid],ele)
            else:
                return rec_binary_search(arr[mid+1:], ele)



if __name__ == "__main__":

    my_array = [i for i in range(1,101)]
    print(seq_search(my_array, 3.5))
    print(my_ordered_seq_search(my_array, 3.5))
    print(ordered_seq_search(my_array, 3.5))
    print(binary_search(my_array, 100))
    print(rec_binary_search(my_array, 1000))