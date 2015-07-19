import math
from array import array

# Furkan Kaynar 2015

# !IMPORTANT -> This is the function that will be used entire the program.
def f(x):
 	
    return 3*(float(x)**3)+4*(float(x)**2)

# func trapez -> finds the area
# @args f: the function
# @args n: the sensitivity (larger -> more sensitive)
# @args min: starting val of x
# @args max: finishing val of x

def trapez(f,n,min,max):
    h=(max-min)/float(n)
    area = (0.5)*h
    sum_y = (f(0)+f(max))
    i=min
    while i<max: 
        sum_y += 2*f(i)
        i += h
    area *= sum_y
    return area
#print "The Minimum Number of Trapez Integral?"
#a = raw_input()
#print "The Maximum Number of Trapez Integral?"
#b = raw_input()
#print trapez(f, 100000, int(a), int(b))

# func simpson -> finds the area better
# @args f: the function
# @args n: the sensitivity (larger -> more sensitive)
# @args min: starting val of x
# @args max: finishing val of x

def simpson(f,n,min,max):
    h=(max-min)/(float(n))

    sum_x = 0
    sum_y = 0
    i=min
    j=0
    while i<max: 
        if(j % 2 == 0):
        	sum_x += 2*f(i)
        else:
        	sum_y += 4*f(i)
        i += h
        j += 1
    area = (sum_y+sum_x)
    return ((max-min)/(float(n)*3))*(area+f(min)+f(max))

#print "The Minimum Number of Simpson Integral?"
#a = raw_input()
#print "The Maximum Number of Simpson Integral?"
#b = raw_input()
#print simpson(f, 1000000, int(a), int(b))
 
# func turev -> finds the derivative
# @args f: the function
# @args x: x of f(x)
# @args delta: the sensitivity of result (lesser -> more sensitive) 

def turev(f,x,delta):
	return (((f(x+delta)-f(x))/delta)+((f(x)-f(x-delta))/delta))/2
#print turev(f,2,0.000000001)
  

# func newtonRaphson -> finds the x by a given function and a result
# @args f: the function
# @args result: the result of function (to find x)
# @args delta: the sensitivity of result (lesser -> more sensitive) 
# @args x0: the starting number to check x's

def newtonRaphson(f,delta,x0,result):
	funk = f(x0)-result
	nextX = x0-((f(x0)-result)/turev(f,x0,delta))
	if(math.fabs(x0-nextX) >= delta):
		return (newtonRaphson(f,delta,nextX,result))
	else:
		return (x0)

#print "Type a number that you want to start looking."
#x = float(raw_input())
#print "f(x) = ? (A Number)"
#res = float(raw_input())
#print newtonRaphson(f,0.00000001,x,res)

# func lagrangeFunc -> creates an interpolation curve and returns an approximate value of that function
# @args neededX: the argument of function for the value you want.
# @args n: the number of values that you will input

def lagrangeFunc(neededX, n):
	xs = range(n+1)
	ys = range(n+1)
	res = 0
	n += 1
	for i in range(1,n):
		print "Type x"
		xs[i] = (float(raw_input()))
		print "Type f(x)"
		ys[i] = (float(raw_input()))

	for i in range(1,n):
		print("f("+str(xs[i])+") = "+str(ys[i])+"\n")

	for i in range(1,n):
		Lx = 1;
		for j in range(0,n):
			if(i != j):
				Lx *= (neededX-xs[j])/(xs[i]-xs[j])
		Lx *= ys[i]
		res += Lx
	return res

#print "What is the x you needed?"
#answer = float(raw_input())
#print "How Many results will you type?"
#n = int(raw_input())
#print lagrangeFunc(answer,n)
 

	