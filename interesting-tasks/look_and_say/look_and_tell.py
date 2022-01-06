def look_and_say(num):
    '''
    generates the first n numbers of the sequence
    [1, 11, 21, 1211, 111221,
    '''
    from itertools import groupby
    if num < 1:
        return
    
    #add the first member to the list     
    term = '1'
    yield term

    for i in range(num):
        term_list = []
        for value, quantity in groupby(term):
            term_list.append(str(len(list(quantity))))
            term_list.append(str(value))
        term = ''.join(term_list)
        yield term

new_a = list(look_and_say(30))
print(new_a)