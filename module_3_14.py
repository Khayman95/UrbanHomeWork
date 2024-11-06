def single_root_words(root_woods, *other_words):
    same_words = []
    list_=list(other_words)
    c = len(list_)
    list_1 = ()
    d = root_woods.lower()
    for i in range(c):
        list_1 = list_[i]
        f = list_1.lower()
        if d in f or f in d:
            same_words.append(f)
    return(same_words)
    print(same_words)
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)