
# # TODO: import some code

#have to name with test underscore
# def test_():
#     pass

# expect that the enlarge function returns a larger number than the one we pass in

from app.example import enlarge, to_usd

#usually test functions don't accept any parameters
def test_enlarge():
    assert enlarge(9) == 900 #assert from within the function; invoke application functionality


# USD function should give us a rounded string back with the dollar sign

def test_to_usd():
    assert to_usd(7.1352) == "$7.14" #codifying the expectations we already have mentally to be able to run this in a test and other people can read and understand how it works
