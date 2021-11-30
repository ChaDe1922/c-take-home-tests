import os, sys, requests, random, re, io

score = 0
  
# get student code
with open('q3.c') as response:
  answer = response.read()

#check for math library import and function calls in student code
if '#include <math.h>' in answer:
  print("You imported the math library!")
  score=1
if 'pow' in answer:
  print("Nice use of the pow function")
  score=1
if 'sqrt' in answer:
  print("Good use of sqrt")
  score=1
if score==0:
  print("Your code does not import or use the math library")

# output score results to student and Codio
print("Points Earned: %d out of 1" % score)
if score == 1:
  sys.exit(0)
else:
  sys.exit(1)