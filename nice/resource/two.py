import one
print("Top level two.py")
one.func()


if __name__=="__main__":
    print("two.py is run directly")
else:
    print("two.py is been imported")
    
