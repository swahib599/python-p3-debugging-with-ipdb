#!/usr/bin/env python3

import ipdb

def plus_two(num):
    num = num + 2
    return num

#ipdb.set_trace()

result = plus_two(3)  # Call the function with a test value
print(result)  # Print the result to verify