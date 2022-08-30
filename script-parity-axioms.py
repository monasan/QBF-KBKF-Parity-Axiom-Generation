#!/usr/bin/python

import sys
import math

def axiom(n):

    print("new version below:")

    lines = 2 ** n 
    variables = 2*n

    def getsign(c, v, maxvars):
        if int(c / math.pow(2, maxvars-v)) % 2 == 0:
            return 1
        return -1

    def getsignsecond(c, v, maxvars):
        v = v - maxvars
        if int(c / math.pow(2, maxvars-v)) % 2 == 0:
            s = -1
        else: s = 1
        
        if v > 0 and int(c / math.pow(2, maxvars-v+1)) % 2 == 1:
            s = -s
        return s


    for i in range(lines):
        for j in range(variables):
            #print(str(variables-j), end=' ')
            if(j < (n-1)):
                number = getsign(i, j, (n-1)) * (variables-j) 
                print(str(number), end=' ')

            if((j >= (n-1)) & (j < variables-2)):
                number = getsignsecond(i, j, (n-1)) * (variables-j) 
                print(str(number), end=' ')

            if(j >= variables-2):
                if(j% 2 == 0):
                    if(i % 2 == 0):
                        print(str(variables-j), end=' ')
                    else:
                        print("-" + str(variables-j), end=' ')


                if(j% 2 != 0):
                    if(i % 3 == 0):
                        print("-" + str(variables-j), end=' ')
                    else:
                        print(str(variables-j), end=' ')
        
        print("")

n = sys.argv[1]

axiom(int(n))

