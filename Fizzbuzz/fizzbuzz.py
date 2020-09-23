i=int(input("Enter the number: "))
for fizzbuzz in range(1,i+1):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("FizzBuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("Fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("Buzz")
        continue
    

