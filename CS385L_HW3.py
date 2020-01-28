#CS 385L – Python Programming Language
#Instructor: Dr. Vidhyacharan Bhaskar
#Homework 2A | Carlos Valero

#1______________________________________
def sqr_root(sqr):
  sqr = float(sqr)
  num_iterations = 0
  close_enough = 0.1 #how acurate u want it
  guess = 1.0 #never use 0.0
  avg = sqr/guess
  while (abs((guess**2) - sqr) >= close_enough) and guess <= sqr:  #abs is need
    num_iterations += 1
    guess = (avg + guess)/2
    #print("Iteration",num_iterations," -->",guess) #tracing print
    avg = sqr/guess
  print(guess)
sqr_root(280)
sqr_root(179)
sqr_root(321)

#2______________________________________
def cube_root(cube):
  cube = float(cube)
  epsilon = 0.1
  guess = 0.0
  increment = 0.01
  num_guesses= 0
  while abs(guess**3 - cube) >= epsilon and guess <= cube:
    guess += increment
    num_guesses+= 1
  print('num_guesses=', num_guesses)
  if abs(guess**3 -cube) >= epsilon:
    print('Failed on cube root of', cube)
  else:
    print(guess, 'is close to the cube root of', cube)
cube_root(280) 
cube_root(-179) 
cube_root(-321)

#3______________________________________
def comp_str():
  a = input("Insert first word: ")
  b = input("Insert second word: ")
  for i in range(len(a)):  #we analize letter by letter
    if a[i] < b[i]:
      return str(a) + ", goes first on dictionary"
    elif b[i] > a[i]:
      return str(b) + " goes first on dictionary"
  return ("the words are the same.")
comp_str()

#4______________________________________
def bisection(cube):
  epsilon = 0.01
  sign = 1   #quick fixing for include negative inputs
  if cube < 0: 
    sign *= -1
    cube *= -1
  num_guesses= 0
  low = 0
  high = cube
  guess = (high + low)/2.0
  while abs(guess**3 -cube) >= epsilon:
    if guess**3 < cube :
      low = guess
    else:
      high = guess
    guess = (high + low)/2.0
    num_guesses+= 1
  print('num_guesses=', num_guesses)
  print(guess*sign, 'is close to the cube root of', cube*sign) #quite close
bisection(-380)
bisection(-147)
bisection(261) 

#5______________________________________
def animals():
  lst = ["dog", "huron", "rabbit", "guinea pig"]
  for i in lst:  #going through the list
    print("A",i.title(), "could be a great pet")
  print("\nAll this animals are mammals")
animals()

#6______________________________________
def million():
  lst = []
  for i in range(1,1000001): #from 1 to 1000000
    lst.append(i)
  print("Min list value:",min(lst))
  print("Max list value:",max(lst))
  print("Sum of all list values:",sum(lst))
million()

#7______________________________________
def food():
  food = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream'] #original list
  print("First three items:",food[:3])
  print("Middle three items:",food[1:4])
  print("Last three items:",food[2:5])
food()

#8______________________________________
def restaurant():
  menu = ("Lomo Saltado", "Cebiche", "Jalea Marina", "Arroz con pato", "Caja china")
  for i in menu:
    print(i)
  try:
    menu[0] = "Pollo a la brasa"  #super error
  except:
    print("\n--------->ERROR: Tuple is inmutable. Do you even code?<--------\n")
  new_menu = ("Pollo a la brasa", ) + menu[1:4] + ("Pachamanca",) #rewriting tuple
  for j in new_menu:
    print(j)
restaurant()
