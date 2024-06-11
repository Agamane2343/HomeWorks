#same_words = ["метромОст", "Радиомост", "ДОМОстить", "батаРЕЙа", "домОСТрой"]



def single_root_words (root_word = "мост", *, other_words = 0):
    same_words = ["метромОст", "Радиомост", "ДОМОстить", "батаРЕЙа", "домОСТрой", "мастеРИТЬ", "МосТик"]
    count = 0
    result1 = []
    result2 = []

    for root_word in same_words[count].lower():
        if root_word in same_words[count]:
            result1.append(same_words[count])
            count += 1
        else:
            result2.append(same_words[count])
            count += 1
        if count == len(same_words):
            break

    print (result1)
    print (result2)

single_root_words()