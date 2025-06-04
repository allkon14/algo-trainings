N = 10
# Создание двумерного массива
myset = [[] for _ in range(N)]


def add(x):
    myset[x % N].append(x)


# Линейный поиск для нахождения
def find(x):
    for el in myset[x % N]:
        if el == x:
            return True
    return False


def delete(x):
    xlist = myset[x % N]
    for i in range(len(xlist)):
        if xlist[i] == x:
            xlist[i] = xlist[-1]
            # или swap
            # xlist[i], xlist[len(xlist) - 1] = xlist[len(xlist) - 1], xlist[i]
            xlist.pop()
            return


"""
Дана последовательность положительных чисел длиной $N$ и число $X$ 

Нужно найти два различных числа $A$ и $B$ из последовательности, таких что $A + B = X$ 
или вернуть пару $0, 0$, если такой пары чисел нет
"""
def twonumswithsumx(nums, x):
    prevnums = set()
    for nownum in nums:
        if x - nownum in prevnums:
            return (nownum, x - nownum)
        prevnums.add(nownum)
    return (0, 0)


x = 4
nums = [2, 1, 3, 4, 0, 5]
print(twonumswithsumx(nums, x))


"""
Дан словарь из $N$ слов, длина каждого не превосходит $K$ 

В записи каждого из $M$ слов текста (каждое длиной до $K$) может быть пропущена одна буква. 
Для каждого слова сказать, входит ли оно (возможно, с одной пропущенной буквой), в словарь
"""


def wordsindict(dictionary, text):
    goodwords = set(dictionary)
    for word in dictionary:
        for delpos in range(len(word)):
            goodwords.add(word[:delpos] + word[delpos + 1:])
    ans = []
    for word in text:
        ans.append(word in goodwords)
    return ans
