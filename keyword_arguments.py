# Document at least 3 use cases of the * and ** operators
# 1. TO ADD A SERIES OF NUMBERS
def student_scores(*args):
    return sum(args)

# print(student_scores(2,3,4))   



# ///////////////////////////////////////////////////////////////////
# 2.
def cloths(*args, **kwargs):
#   args = list(args)
    color_list = kwargs.values()
    print(color_list)
    for arg in args:
        return f"{arg} is available in {', '.join(color_list)}"


# # ///////////////////////////////////////////////////////////////////
# # 3.
def intro(**kwargs):
    for key, value in kwargs.items():
        return f"{key} is {value}"

# print(intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890))
