for x in range(10):
    print(x)
else:
    print("Stops at 9 not 10")


def my_function():
    print("Hello from a function")


my_function()
my_function()
my_function()
my_function()
my_function()
my_function()
my_function()


def my_function(number):
    print(number + " 1")


my_function("1")
my_function("2")
my_function("3")


def my_function(fname, lname):
    print(fname + " " + "  " + lname)


my_function("1", "2")


def my_function(*number):
    print("The third number is " + number[2])


my_function("12", "61", "35")
