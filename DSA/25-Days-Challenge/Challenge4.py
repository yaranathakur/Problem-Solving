def max_of_subarrays():
    len = int(input("Enter the length of array: "))
    sub_len = int(input("Enter the length of subarray: "))
    print("Enter the element of array: ")
    array = list(map(int, input().split()))
    for x in range(len - (sub_len - 1)):
        sub_array = array[x : x + sub_len]
        print(max(sub_array), end = " ")

max_of_subarrays()