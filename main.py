while True:
  value = int(input("Enter a number: \n"))
  if value > 8 or value <= 0:
    print("Invalid numbers\n")
  else:
    break
    
for i in range(1,value + 1):
  #space in front
  front_space = ' ' * (value - i)

  #sace between
  middle_space = ' ' * 2

  #right pyramid
  right_pyramid = '#' * i


  print(front_space + '#' * i + middle_space + right_pyramid)
 
    
