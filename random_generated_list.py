import random


def create():
    liste = []
    wort = ""
    for i in range(9999):
        wortlaenge = int(random.randint(5, 10))
        wort_list = []
        for j in range(wortlaenge):
            buchstabe_zahl = int(random.randint(0, 25))
            buchstabe = chr(buchstabe_zahl + 97)
            wort_list.append(buchstabe)
            wort = ""
        for k in range(len(wort_list)):
            gross = random.randint(0, 1)
            if k == 0:
                if gross == 1:
                    wort_list[k] = chr(ord(wort_list[k]) - 32)
            wort = wort + wort_list[k]
        liste.append(wort)
    return liste
