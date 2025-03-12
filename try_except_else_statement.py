try:
    # Code that may raise an exception
    result = 10 / 2
except ZeroDivisionError:
    # Code to handle the exception
    print("Cannot divide by zero!")
else:
    # Code to execute if no exception occurred
    print("Division was successful. Result:", result)
finally:
    # Code that will always execute
    print("This will always execute.")
