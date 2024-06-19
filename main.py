# Error catching mechanisms
try:
    barca = {"key": "value"}
    print(barca)
    # print(barca["spsp"])
    print("barca")
except KeyError:
    print("This for the except")
else:
    print("This means the try completed.")
finally:
    print("Do this after everything")
    raise TypeError("This is a type error")

