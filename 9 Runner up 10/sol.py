# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    mx=max(arr)
    runner_up=0
    for i in arr:
        if i!=mx:
            runner_up=i
    print(runner_up)
