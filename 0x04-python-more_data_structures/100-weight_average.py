#!/usr/bin/python3
def weight_average(my_list=[]):
    numerator = 0
    denominator = 0
    
    if my_list:
        for numbers_in_tuples in my_list:
            numerator += (numbers_in_tuples[0] * numbers_in_tuples[1])
            denominator += (numbers_in_tuples[1])
        return (numerator/ denominator)
    return(0)
