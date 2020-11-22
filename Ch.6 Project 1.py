import math
tolerance = 0.000001
def newton(x):
   estimate = 1.0
   while True:
       estimate = (estimate + x / estimate) / 2
       difference = abs(x - estimate ** 2)
       if difference <= tolerance:    
           break            
       return estimate    
def main():
   while True:
       x = input("Enter a positive number or enter to quit: ")
       if x == "":     
           break      
       x = float(x)
       print("The programs estimate of the square root of ", x, "is ", round(newton(x),2))
       print("Python's estimate: ", math.sqrt(x))
main()
