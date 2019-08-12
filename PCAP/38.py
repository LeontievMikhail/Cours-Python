# Question 38
# Is there any difference in the error messages displayed once the two newly defined exceptions CriticalError have been raised separately?
# # Example 1
# class CriticalError(Exception):
# def __init__(self, message='ERROR MESSAGE A'):
#         Exception.__init__(self, message)
# raise CriticalError
# raise CriticalError("ERROR MESSAGE B")
# # Example 2
# class CriticalError(Exception):
# def __init__(self, message='ERROR MESSAGE A'):
#         Exception.__init__(self, message)
# raise CriticalError("ERROR MESSAGE B")
# A. No, both errors raised will display the same message: ERROR MESSAGE A
# B. No, both errors raised will display the same message: ERROR MESSAGE B
# C. No, both errors raised will display no message
# D. Yes, the first error raised will display the message ERROR MESSAGE A,
# while the second ERROR MESSAGE B
# E. Yes, the first error raised will display no message, while the second
#      ERROR MESSAGE B
# F. Yes, the first error raised will display no message, while the second
#      ERROR MESSAGE A
