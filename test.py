mylist = [1, 2, 3, 4, 5]

def myfun(self, *args):
    print(args[0])  # args의 첫 번째 요소를 출력합니다.
    print(len(args))  # args의 길이를 출력합니다.

myfun(mylist)