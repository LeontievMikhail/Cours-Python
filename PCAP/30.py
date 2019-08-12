# Question 30
# What is the expected behavior of the following snippet?
# def gen():
#     lst = range(5)
#     for i in lst:
#         yield i*i
# for i in gen():
#     print(i, end="")
# A. It will print: <generator object gen at (some hex digits)>
# B. It will print: 014916
# C. It will print: 0 1 4 9
# 16
# D. It will cause a runtime exception/error E. It will print an empty line