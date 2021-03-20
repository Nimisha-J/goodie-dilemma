# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 15:12:32 2021

@author: Nimisha
"""

s = dict()                                                                          #initialize a dictionary 
input_text = open('input.txt','r')                                                  #input from file

for line in input_text :                                                             #read line from input
    if line != '\n':                                                                #exclude empty lines
        a = line.split(":")                                                         #separate names of goodies and their cost
        a[1] = a[1][1:]                                                             #remove an unwanted space in cost string
        if a[1] != "":                                                              #remove lines which have no value
            if a[1][-1] == "\n":                                                    #remove endline 
                a[1] = a[1][:-1]
            s[a[0]] = int(a[1])                                                     #add the name of goodies and their cost as integer to dictionery            
input_text.close()                                                                  #close file input
M = s["Number of employees"]                                                        #extract the number of employees
del s["Number of employees"]                                                        #once extracted, key and value deleted
arr = sorted(s.values())                                                            #sort the cost in ascending order and add to a new list
L=len(arr)                                                                          #number of goodies
min = arr[-1] - arr[0]                                                              #initialise minimum for worst case
f=0                                                                                 #f is used to store the index of the goodie with the lowest cost
for i in range((L-M)+1):                                                            #traverse through the costs
    b = arr[i+(M-1)] - arr[i]                                                       #calculate difference between max and min
    if b<min:                                                                       #check if difference is lowest
        min=b                                                                      #if yes, update min value
        f=i                                                                         #also update f to store the index where min cost was found        
output_file = open('output.txt','w')                                                #write file       
output_file.write("The goodies selected for distribution are:\n")                   
output_file.write("\n")
for i in range(f,f+M):                                                              #traverse through the costs identified to come up with minimum difference
    for j in s.keys():                                                              #traverse through goodies                                                             
        if s[j] == arr[i]:                                                          #if costs match, goodies matched
            output_file.write(j+": ")                                               #print name of goodie
            output_file.write(str(s[j]))                                            #print cost of goodie
            output_file.write("\n")
            break
output_file.write("\n")
output_file.write("And the difference between the chosen goodie with highest price and the lowest price is ")
output_file.write(str(min))                                                         #print the difference between max and min
output_file.close()

                  
    
    
        