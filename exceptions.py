try:
    int("a")
except ValueError as error:
    print("Oops you can't do that! The error is: ", error)

print("other code")
