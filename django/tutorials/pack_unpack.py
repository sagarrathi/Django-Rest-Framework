# *head, _,tail=[1,2,3,4,5]

# # print(head)
# # print(tail)


# users =[
#     (0,"A","b"),
#     (1,"D","b"),
#     (2,"G","b"),
#     (3,"H","b"),
#     ]

# username_mapping= {user[1]: user for user in users}

# print(username_mapping)

# def named(**args):
#     print(args)

# det={"a":1,"b":2}
# named(**det)

def both(*args, **kwargs):
    print(args)
    print(kwargs)
    print(f"Wehre are you:{__name__}")

both(1,3,5,name="bobo", age=25)