calls = 0
matches = (0)
c = 0
def count_calls():
    global calls
    calls = calls + 1
def string_info(string):
    global calls
    count_calls()
    weight = len(string)
    big = string.upper()
    small = string.lower()
    return (weight, big, small)
def is_contains(string, list_to_search):
    global calls
    count_calls()
    d = len(list_to_search)
    global c
    for i in range(d):
        a = string.lower()
        b = list_to_search[i]
        f = b.lower()
        if a == f:
            matches = (0)
            c = matches + 1
        else:
            c = 0
    if c == 0:
        return (False)
    else:
        return (True)
    
print(string_info('Capybara'))

print(string_info('Armageddon'))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN

print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
