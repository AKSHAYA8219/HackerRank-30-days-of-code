#!/bin/python3

n = int(input())
arr = list(map(int, input().split()))
#accessing each element of arr in reverse order
for i in arr[::-1]:
    print(i,end=" ")
