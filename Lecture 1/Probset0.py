import  numpy

#Collects integers and calculates the power of them
print("Please enter two values to calculate the power of them.")

#Getting the X input
x = input('Enter an X Value:')
y = input('Enter a Y value:')

#Convert the string to integer
numx = int(x)
numy = int(y)

#Print the solved value
print(pow(numx,numy))
print(numpy.log2(numx))

