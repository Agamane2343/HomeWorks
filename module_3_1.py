calls = 0

def count_calls():
    global calls
    calls += 1


def string_info(n):
    count_calls()
    return len(n), n.upper(), n.lower()

def is_contains(string, list_to_search):
    count_calls()
    for i in list_to_search:
        if i.lower() == string.lower():
            return True
    return False


#Str1 = string_info('Галя тащила саквояж')
#Str2 = is_contains("УрБан", ["урбан", "город", "деревня"])
#print(Str1)
#print(Str2)


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)