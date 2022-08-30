#!/usr/bin/python


import sys
import math

def axioms(n):
    #the first number of the new variables (after other variables)
    begin = (n * 4) + 1


    #how many output lines should be generated
    lines = begin


    counterForall = 0
    counterExists = 1
    counterExistsRest = 1
    lastForall= 3*n + 1

    for i in range(lines):
        #print("line" + str(i+1), end=' ')
        for j in range(begin):
            if(i == (j)):
                print(str(j+lines), end=' ')
            else:
                print("-" + str(j+lines), end=' ')
        
        if(i < (n*2-2)):
            if(i%2==0): #even
                print("-" + str(n + counterForall +1), end=' ')
                print("-" + str (counterExists), end=' ')
                print(str(n + (counterForall+1) +1), end=' ')
                print(str(2*n +(counterForall+1) +1), end=' ')
            else: #odd
                print("-" + str(2*n +counterForall +1), end=' ')
                print(str (counterExists), end=' ')
                print(str(n + (counterForall+1) +1), end=' ')
                print(str(2*n +(counterForall+1) +1), end=' ')

                counterForall = counterForall+1
                counterExists = counterExists+1
            

        if( (i < (n*2)) & (i >= (n*2-2))):
            if(i%2==0): #even
                print("-" + str(n + counterForall +1), end=' ')
                print("-" + str (counterExists), end=' ')
                for k in range (n): 
                    print(str(3*n + k + 1), end=' ')
            else: #odd
                print("-" + str(2*n +counterForall +1), end=' ')
                print(str (counterExists), end=' ')
                for k in range (n): 
                    print(str(3*n + k + 1), end=' ')


        if((i >= (n*2)) & (i < lines-1)):
            if(i%2==0): #even
                print("-" + str(counterExistsRest), end=' ')
                print("-" + str(lastForall), end=' ')
            else: #odd
                print(str(counterExistsRest), end=' ')
                print("-" + str(lastForall), end=' ')

                counterExistsRest = counterExistsRest+1
                lastForall = lastForall+1

        if(i==lines-1):
            print(str(counterExistsRest), end=' ')
            print( str (2*n +0 +1), end=' ')

        print("")

n = sys.argv[1]

axioms(int(n))

