calls = 0
matches = (0)
def count_calls():
    global calls
    calls = calls + 1
def string_info(string):
    global calls
    weight = len(string)
    big = string.upper()
    small = string.lower()
    print(weight, big, small)
    count_calls()
def is_contains(string, list_to_search):
    d = len(list_to_search)
    global matches
    for i in range(d):
        a = string.lower()
        b = list_to_search[i]
        f = b.lower()
        if a == f:
            matches = (0)
            matches = matches + 1
            if matches >= 0:
                print(True)
                break
        else:
            print (False)
            break
    global calls
    count_calls()
string_info('Умный')
string_info('Знание')
is_contains('Smart',['smaRt', 'smat', 'soup'])
is_contains('Obscure',['ObScRe', 'core', 'One'])
print(calls)