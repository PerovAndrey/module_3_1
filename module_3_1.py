# a = 5
# b = 10
#
#
# def printer():
#     global a, b
#     a = 'str'
#     b = 'str2'
#     c = 15
#     d = 20
#     print(c, d, 'local')
#     print(a, b, 'global')
#
#
# print(a, b)
# printer()
# print(a, b)


calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())


def is_contains(string, list_calls):
    count_calls()
    return string.upper() in [i.upper() for i in list_calls]


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBan
print(is_contains('cycle', ['recycle', 'cyclic']))  # No matches
print(calls)
