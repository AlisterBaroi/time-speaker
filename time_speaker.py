# Problem from Turing Coding Challenge 2020 - The Time in Words (Challenge 7) 
# Coding challenge link: https://www.hackerrank.com/turing-coding-chalenge

# Problem Statement: ==========================================================
# Complete the 'timeInWords' function below.
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
# =============================================================================

#!/bin/python3
print("Welcome to 'Time Speaker': \nA simple program to print time in words from numeral inputs")
print("===========================================================")

h = int(input("Enter hours: "))
m = int(input("Enter minutes: "))

def timeInWords(h, m):
    # printing input data for validation
    print("Your time input: "+str(h)+":"+str(m))
    
    if h > 12:
        h = int(h % 12)
    if h == 0:
        h = 12
    if h <= -1:
        h = 1    
    if m > 60:
        h += int(m/60)
        m = int(m % 60)
    if m <= -1:
        m = 1
        
    string = str() # whole string
    hs = str() # variable to hold hour
    ms = str() # variable to hold mins
    
    # make dic to define nums from 1 to 30
    t_str = {1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"quarter",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen",20:"twenty",21:"twenty one",22:"twenty two",23:"twenty three",24:"twenty four",25:"twenty five",26:"twenty six",27:"twenty seven",28:"twenty eight",29:"twenty nine",30:"half",45:"quarter"}
    
    # set hour variable using dic indexes/keys (done)
    hs = t_str[h]
       
    # logic for 1 min (done)
    if (m==1):
        ms = t_str[m] + " minute past"
        
    # logic for mins between 0 to 30 except 15 (done)
    if (2<m<=15) or (16<m<30):
        ms = t_str[m] + " minutes past" 
        
    # logic for 15 and 30 mins (done)
    if (m==15) or (m==30):
        ms = t_str[m] + " past"
        
    # logic for 45 mins (done)
    if (m==45): 
        ms = t_str[m] + " to" 
        hs = t_str[h+1]    # set modified hours for 30+ mins (done)
           
    # logic for mins between 30 to 60 (done)
    if (31<m<=45) or (46<m<60):
        ms = t_str[(60-m)] + " minutes to"
        hs = t_str[h+1]    # set modified hours for 30+ mins (done)
    
    # setting final string (done) 
    string = str(ms + " " + hs)
    
    # logic for 0 mins (done)
    if (m==0):
        ms = " o' clock"
        string = hs + ms
    
    print("Time in Words:",  string)
    return string

timeInWords(h, m)
