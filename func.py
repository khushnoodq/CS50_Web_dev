from squares import square
# import squares  ---> Imports entire file, funtion calls need to be scoped. See comment below

for i in range(5):
    print(f"Square of {i} is {square(i)}")
#    print(f"Square of {i} is {squares.square(i)}") ---> Scoping example


