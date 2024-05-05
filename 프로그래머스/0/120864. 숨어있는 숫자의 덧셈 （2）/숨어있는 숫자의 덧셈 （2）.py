def solution(my_string):
    for x in my_string:
        if x.isalpha():
            my_string = my_string.replace(x, ' ')
    my_string = my_string.split()
    
    
    return sum(map(int, my_string))