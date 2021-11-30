#this script moves all functions from the student's .c code to a .c file in the secure folder for unit testing

import os, sys, requests, random, re, io #there are probably extra imports here

#get student code
with open(sys.argv[1]) as response:
  codeLines = response.readlines()
  
functionLines = []
functionLines.append('#include "' + sys.argv[2] +'"\n')

#take out main method
opened = 0
in_main = False
for i in codeLines:
  if 'main' in i:
    opened += i.count('{')
    opened -= i.count('}')
    in_main = True
  elif in_main:
    opened += i.count('{')
    opened -= i.count('}')
    if opened==0 :
      in_main = False
  else :
    functionLines.append(i)

#take out declerations in header file
headerFile = ((sys.argv[3])[:-1]) + "h" #weirdness is replacing .c extension with .h extension
with open(headerFile) as h:
  declerations = h.readlines()

for line in declerations:
  if ("#ifndef" in line) or ("#define" in line) or ("#endif" in line):
    declerations.remove(line)
    
for line in declerations:
  if line in functionLines:
    functionLines.remove(line)
    
#move functions to secure folder
with open(sys.argv[3], 'w') as f:
    for line in functionLines:
        f.write("%s" % line)