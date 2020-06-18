import time
import random_generated_list


def bubble_sort(l):

    for y in range(len(l)):
        for i in range(0, len(l)-1-y):
            if ord(l[i][0].lower()) > ord(l[i + 1][0].lower()):
                l[i], l[i+1] = l[i+1], l[i]

    return l


if __name__ == "__main__":
    l = random_generated_list.create()
    start = time.time()
    l = bubble_sort(l)
    dauer = time.time() - start
    print(l)
    print(dauer)
    for i in range(len(l)-1):
        assert ord(l[i][0].lower()) <= ord(l[i + 1][0].lower())
