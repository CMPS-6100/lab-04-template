"""
CMPS 6100  Lab 4
Author:
"""

## You don't need any imports for this lab

def unimodal_max(lst):
    # TO-DO: Implement this function
    pass # remove this instruction

def list_sum_DC(lst):
    # TO-DO: Implement this function
    pass # remove this instruction

#########    #########
### Test Functions ###
#########    #########

def test_unimodal_max():
    lst = [4, 5, 7, 6, 3, 2, 1, 0]
    assert(unimodal_max(lst) == 7)
    lst = [1, 2, 3, 4, 5, 6, 7, 8]
    assert(unimodal_max(lst) == 8)
    lst = [9, 8, 7, 6, 5, 4, 3, 2]
    assert(unimodal_max(lst) == 9)

def test_list_sum_DC():
    lst = [4, 5, 2, 6, 1, 0, 3, 7]
    assert(list_sum_DC(lst) == 28)
    lst = [i for i in range(1,101)]
    assert(list_sum_DC(lst) == 5050)