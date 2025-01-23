def local_scope():
    x = 5
    print(x)
local_scope()
# print(x), we cannot do that because x is local scope of function, and not accessible outside

x = 5
def modify_global():
    global x
    x += 15

modify_global()
print(x)