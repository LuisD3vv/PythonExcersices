def FizzBuzz(numbers):
  for n in numbers:
    if n %2 == 0 and n %3 == 0:
      #print("Fizzbuzz")
    elif n %3 == 0:
      #print("Fizz")
    elif n %2 == 0:
      #print("buzz")

rango = range(1,99)

FizzBuzz(rango)
