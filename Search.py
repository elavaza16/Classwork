
Arr1 = [11,22,33,44,55,66,77,88,99]
my_key = 77
start_index = 0
end_index = len(Arr1) - 1
found = False
for i in Arr1:   ###  for i in range(len(Arr1))
    if Arr1[i] == my_key:
        print("Found")
        break
    else:
        print("Not found")

while start_index <= end_index:
    mid = (start_index+end_index) // 2
    if Arr1[mid] == my_key:
        print(" Found element at pos:", mid)
        found = True
        break
    elif my_key < Arr1[mid]:
        end_index = mid - 1
    elif my_key > Arr1[mid]:
        start_index = mid + 1

if not found:
    print(f"{my_key} not found in the list!")


    ######   USE ITERATION (RECURSION)  #######

def bs_recursive(start_imdex, emd_index):
    if start_imdex > end_index: #base case
        return -1

    mid = (start_index + end_index) // 2

    if Arr1[mid] == my_key:
        return mid
    elif my_key < Arr1[mid]: #left half - adjust edn index
        return bs_recursive(start_imdex, mid - 1)
    else:
        return bs_recursive(mid+1, end_index) #right half - adjust start index

result = bs_recursive(start_index, end_index)

if result != -1:
    print("Found at index:", result)
else:
    print(f"{my_key} not found in the list")