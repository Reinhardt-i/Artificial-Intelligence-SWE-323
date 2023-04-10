
def search(arr, to_find) :
    for i in range(len(arr)):
        if arr[i] == to_find:
            return i
    return -1

if __name__ == '__main__':
    arr = [10, 20, 30, 41, 50, 60, 71, 80]
    print(search(arr, 41))
    
    

