import math

n = int(input("Input n: "))
arr = [0 for i in range(int(2 + math.log(n, 2)))]
arr[1] = n
cont = True

while cont:
    cont = False
    for i in range(1, len(arr)):
        if arr[i] > 2:
            cont = True
            third = int(arr[i] / 3)
            arr[i - 1] += third * 2
            arr[i + 1] += third
            arr[i] -= third * 3
print(arr)
for i in range(len(arr) - 1, 0, -1):
    if not arr[i] == 0:
        print("Max height: " + str(i))
        print("log_3(n) + 1: " + str(int(math.log(n, 3)) + 1))
        print("log_2(n) + 1: " + str(int(math.log(n, 2)) + 1))
        break
