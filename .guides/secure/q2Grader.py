import os, sys, requests, random, re, io

score = 0
  
# get student code
with open('q2.c') as response:
  answer = response.read()

#check for a loop in student code
if 'for' in answer:
  print("You implemented a `for` loop - great work!")
  score+=1
elif 'while' in answer:
  print("You implemented a `while` loop - that's not quite right")
else:
  print("Your code does not have a loop - it needs one")

# output score results to student and Codio
print("Points Earned: %d out of 1" % score)
if score == 1:
  sys.exit(0)
else:
  sys.exit(1)