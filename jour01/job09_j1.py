for i in range (1,101):
  # it is necessary to start with (if .. and) condition other wise it will print only fizz or buzz
  if i % 3 == 0 and i % 5 == 0  :
    print("FizzBuzz")
  elif i % 3 == 0 :
      print("Fizz")
  elif i % 5 == 0:
      print("Buzz")
  else:
    print (i)