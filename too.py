arr=[11,22,33,44,55,66,77,88,99]

my_key=99
start_index=0
end_index=len(arr)-1
found=False

for i in arr:
    if arr[i]==my_key:
        print("Found")
        break

    else:
        print("Not found")



while start_index<= end_index:

    mid=(start_index+end_index)//2
    if arr[mid]==my_key:
        print("Found element at position: ", mid)
        found=True
        break
    elif my_key <arr[mid]:
        end_index=mid-1

    elif my_key>arr[mid]:
        start_index = mid + 1

if not found:
    print(f"{my_key} not found in the list!")