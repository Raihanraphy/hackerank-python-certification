if __name__ == '__main__':
        N = int(input())
        lst = []
        for i in range(N):
                arr = map(str, input().split())
                arr = list(arr)
                if len(arr) > 1:
                        for i in range(1,len(arr)):
                                if arr[i].isdigit():
                                        arr[i] = int(arr[i])
                if arr[0].lower() == 'insert':
                        lst.insert(arr[1],arr[2])
                elif arr[0].lower() == 'print':
                        print(lst)
                elif arr[0].lower() == 'remove':
                        lst.remove(arr[1])
                elif arr[0].lower() == 'append':
                        lst.append(arr[1])
                elif arr[0].lower() == 'sort':
                        lst.sort()
                elif arr[0].lower() == 'pop':
                        lst.pop()
                elif arr[0].lower() == 'reverse':
                        lst.reverse()