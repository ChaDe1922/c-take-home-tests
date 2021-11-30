import os, sys, requests, random, re, io
# from contextlib import redirect_stdout

#method to send score to Codio
def report_score():
  url = "{0}&points={1}".format(os.environ['CODIO_PARTIAL_POINTS_URL'], score)
  requests.get(url)

score = 0
  
# get student code
with open('q1.c') as response:
  codeLines = response.readlines()
  
with open('q1.c') as response:
  answer = response.read()

#check for a loop in student code
if 'for' in answer:
  print("You implemented a `for` loop - consider using a while loop in this case.")
  score+=1
elif 'while' in answer:
  print("Nice `while` loop!")
  score+=1
else:
  print("You do not have a loop - how will the user continue to ask about leap years?")

#check for function call in student code
for i in codeLines:
  if 'isLeapYr' in i:
    line = i
    if '=' in line:
      index = line.find('=')
      line = line[index+1:]
    if 'int' not in line:
      score +=1
      print("You called the `isLeapYr` function!")
      break

# output score results to student and Codio
report_score()
print("Points Earned: %d out of 2" % score)
if score == 2:
  sys.exit(0)
else:
  sys.exit(2)