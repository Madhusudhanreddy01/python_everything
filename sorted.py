def sort_arr(arr):
    start = mid = 0
    end = len(arr) - 1

    while mid < end :
        if arr[mid] == -1:
            swap(arr, start, mid)
            start += 1
        elif arr[mid] == 1:
            swap(arr, mid, end)
            end -= 1
        else:
            mid += 1

    print(id(arr))


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

abc = sort_arr

def main():
    arr = [1, 0, -1, -1, 1, 0, 1, 0] * 100_000_00
    print(id(arr))
    # [1, 0, -1, -1, 1, 0, 1, 0]  start = 0 , mid = 0, end = 8
    # [0, 0, -1, -1, 1, 0, 1, 1]  start = 0 , mid = 2, end = 7
    # [-1, -1, 0, 0, 1, 0, 1, 1]  start = 1, mid = 4, end = 7
    # [-1, -1, 0, 0, 1, 0, 1, 1]  start = 1, mid = 4, end = 6
    # [-1, -1, 0, 0, 0, 1, 1, 1]  start = 1, mid = 6, end = 6
    
    # arr = [0, 1, 0, 1, -1, 0, -1, -1] * 100
    # print(arr)
    abc(arr)
    # print(arr)

if __name__ == "__main__":
    main()



#anotherway..........
# a=[0,1,0,1,-1,0,-1,-1]
# b=[]
# c=[]
# d=[]
# for i in a:
#     if i<0:
#         b+=[i]
#     elif i==0:
#         c+=[i]
#     else:
#         d+=[i]
# print(b+c+d)


