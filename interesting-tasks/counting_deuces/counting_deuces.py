from timeit import timeit

def counting_deuces(num):
    count = 0
    for i in range(num+1):
        for j in str(i):
            if j == '2':
                count += 1
    return count

def counting_deuces_1(num):
    from collections import Counter
    num_str = ''
    for i in range(num+1):
        num_str += str(i)
    return Counter(num_str)['2']

def counting_deuces_2(num):
    from collections import Counter
    return Counter(''.join([str(i) for i in range(num+1)]))['2']

print(counting_deuces(1000))
print(counting_deuces_1(1000))
print(counting_deuces_2(1000))


print('counting_deuces takes:', timeit('counting_deuces(1000)', 'from __main__ import counting_deuces', number=1000), 'seconds')
print('counting_deuces1 takes:', timeit('counting_deuces_1(1000)', 'from __main__ import counting_deuces_1', number=1000), 'seconds')
print('counting_deuces2 takes:', timeit('counting_deuces_2(1000)', 'from __main__ import counting_deuces_2', number=1000), 'seconds')

print('counting_deuces takes:', timeit(lambda: counting_deuces(1000), number=10000), 'seconds')
print('counting_deuces1 takes:', timeit(lambda: counting_deuces_1(1000), number=10000), 'seconds')
print('counting_deuces2 takes:', timeit(lambda: counting_deuces_2(1000), number=10000), 'seconds')
