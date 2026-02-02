# Mutability vs Immutability

x = 1
print(id(x))

y = float(5)
print (y)
print(id(y))

x = 2
print(id(x))

# Immutability there is no way to change the data that is changed at the memory address but in reality its being stored in a different place in memory
# So its a different object in memory

# So even if we do += it will create a new object in memory and assign the value of the object x+1 into the memory

# A list is mutable because the memory does not change when we append however if we add using + it does change in ID
# Whenever we do a assignment(+, - etc) it will change the value 
# But += operates like append?? Whhhhaaaat thats so weird

# Conclusion: using certain operations, we do have the ability to change the value at the original object. This is why we call lists "mutable"