# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 15:12:32 2021

@author: Nimisha
"""

s = dict()                                                                           
input_text = open('input.txt','r')                                                  

for line in input_text :                                                             
    if line != '\n':                                                                
        a = line.split(":")                                                         
        a[1] = a[1][1:]                                                             
        if a[1] != "":                                                              
            if a[1][-1] == "\n":                                                     
                a[1] = a[1][:-1]
            s[a[0]] = int(a[1])                                                                 
input_text.close()                                                                  
M = s["Number of employees"]                                                        
del s["Number of employees"]                                                       
arr = sorted(s.values())                                                            
L=len(arr)                                                                          
min = arr[-1] - arr[0]                                                              
f=0                                                                                 
for i in range((L-M)+1):                                                            
    b = arr[i+(M-1)] - arr[i]                                                       
    if b<min:                                                                       
        min=b                                                                      
        f=i                                                                                 
output_file = open('output.txt','w')                                                       
output_file.write("The goodies selected for distribution are:\n")                   
output_file.write("\n")
for i in range(f,f+M):                                                              
    for j in s.keys():                                                                                                                          
        if s[j] == arr[i]:                                                          
            output_file.write(j+": ")                                               
            output_file.write(str(s[j]))                                            
            output_file.write("\n")
            break
output_file.write("\n")
output_file.write("And the difference between the chosen goodie with highest price and the lowest price is ")
output_file.write(str(min))                                                         
output_file.close()

                  
    
    
        