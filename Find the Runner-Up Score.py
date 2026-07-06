if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    if n < 2:
        print(None)
        exit()
    first=second=float('-inf')
    for num in arr:
        if num > first:
            second=first
            first=num
        elif num > second and num != first:
            second = num
    if second == float('-inf'):
        print(None)
    else:
        print(second)
        
