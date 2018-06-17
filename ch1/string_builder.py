# https://stackoverflow.com/questions/476772/python-string-join-performance

def join_strings(string_list):
    string_accumulator = ""
    for string in string_list:
        string_accumulator += string
    # using + creates new strings for string_accumulator
    # every single pass, a lot of memory allocation and
    # copy operations involved.
    return string_accumulator

def join_strings2(string_list):
    '''
    Using the string builder method.
    '''
    string_accumulator = []
    asdf = 'aasdfasdfasfd'
    for string in string_list:
        for c in string:
            string_accumulator.append(c)
    # appending to a resizable array is probably faster
    # than recreating the string every time
    # stackover claims that concatenation is done
    # on one pass, copying the string only once
    # when using the .join() method.
    return "".join(string_accumulator)


assert(join_strings(["a", "b"]) == "ab")
assert(join_strings2(["a", "b"]) == "ab")

with open('words_alpha.txt') as file:
    word_list = file.read().splitlines()
file.close()

# import tracemalloc
import time

# tracemalloc.start()
t1 = time.time()
# snapshot1 = tracemalloc.take_snapshot()
join_strings(word_list)
t2 = time.time()
# snapshot2 = tracemalloc.take_snapshot()
# stats = snapshot2.compare_to(snapshot1, 'lineno')
print(t2 - t1)
# print("join_strings")
# for stat in stats[:10]:
    # print(stat)

# tracemalloc.clear_traces()
# tracemalloc.stop()
# 
# tracemalloc.start()
t3 = time.time()
# snapshot3 = tracemalloc.take_snapshot()
join_strings(word_list)
t4 = time.time()
# snapshot4 = tracemalloc.take_snapshot()
# stats = snapshot4.compare_to(snapshot3, 'lineno')
print(t4 - t3)
# print("join_strings2")
# for stat in stats[:10]:
#     print(stat)
    
# Don't really know how to understand tracemalloc info, but it seems
# that both methods are yielding the same memory/time requirements...
# The concat operator is probably optimised now.
