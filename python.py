Python 3.5.2 Install on CentOS7
https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-centos-7
sudo yum -y install yum-utils
sudo yum -y groupinstall development
sudo yum -y install https://centos7.iuscommunity.org/ius-release.rpm
sudo yum -y install python35u-3.5.2
sudo yum -y install python35u-pip
sudo yum -y install python35u-devel



$ yum install python-pip
$ pip install pudb 	<=debug tool
http://stackoverflow.com/questions/1623039/python-debugging-tips

#!/usr/local/python
#!/usr/local/python3.5
#!/bin/env python
If you're prone to installing python in various and interesting places on your PATH (as in $PATH in 
typical Unix shells, %PATH on typical Windows ones), using /usr/bin/env will accomodate your whim 
(well, in Unix-like environments at least) while going directly to /usr/bin/python won't. But losing 
control of what version of Python your scripts run under is no unalloyed bargain... if you look at 
my code you're more likely to see it start with, e.g., #!/usr/local/bin/python2.5 rather than with 
an open and accepting #!/usr/bin/env python -- assuming the script is important I like to ensure it's 
run with the specific version I have tested and developed it with, NOT a semi-random one;-).



Python 

1. Debugging Python Debuger
python -m pdb myscript.py
l <=list
n <=next
c <=conntinue
s <=step
w <=where
u <=up
d <=down
locals()


#!/usr/local/python3.5
print("Hello World")
def subr():
        return 5+37
x = subr
print(x)

$ python3.5 helloworld.py
$ chmod +x helloworld.py
$ ./helloworld.py

----------------------------------
x=1
print(x)
x='foo'
print(x)
x = x + "1"    <= Switch to string from integer
print(x)
y = input("Your name?")
print(y)
----------------------------------
name = input("What is your name: ")

# For Loop
for i in range (1,10):
    print("Welcome", name,"", i)
----------------------------------
# While Loop
x=0
while 1: # True:
    print (x)
    x = x + 1
    if (x == 15):
        break
----------------------------------
# For Loop using a list
myCar = ['BMW', 'Lexus', 'Ferrari']
for i in myCar:
    print(i)
----------------------------------
# Scoping
x = 0      # <=without x, error for initial value set
for i in range(1,25):
    x = i + x  
print(x)

----------------------------------
# Function
def sub(x,y):
    z = x - y
    print(z)

def add( x, y ):
    return x + y

print(add(15,4))
sub(4,3)
----------------------------------
x = int(input("Type a number:   "))
if ( x < 1):
    print ("Too small")
elif (x >= 1) and ( x <= 10 ):  #ge , le
    print("ok")
else:
    print("too high")
----------------------------------
####Call Linux host command

#!/usr/bin/python3.5
import os
from subprocess import call

print(os.getcwd())     		# same as PWD
print(os.getuid())			# 0
print(os.getenv("PATH"))	#/sbin:/bin:/usr/sbin:/usr/bin
os.system("ls -al")			# system
inp=input("Hit enter")

call(["ls", "-la"])			# sub
----------------------------------
#!/usr/bin/python3.5
import threading

# v-Object
class aThread(threading.Thread):
    def __init__(self, num, val):
        threading.Thread.__init__(self)
        self.threadNum = num
        self.loopCount = val

    def run(self):
        print("Starting run:  ", self.threadNum)
        myfunc(self.threadNum, self.loopCount)

def myfunc(num, val):
    count = 0
    while count < val:
        print(num, " : ", val * count)
        count = count + 1

t1 = aThread(1, 15)
t2 = aThread(2, 20)
t3 = aThread(3, 25)
t4 = aThread(4, 30)

t1.start()
t2.start()
t3.start()
t4.start()

threads = []
threads.append(t1)
threads.append(t2)
threads.append(t3)
threads.append(t4)

for t in threads:
    t.join()
	

### OOP ###

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year =year
        self.fuel_capacity = 20
        self.fuel_level = 0
    def fill_tank(self):
        self.fuel_level = self.fuel_capacity
        print("Fuel tank is full.")
    def drive(self):
        print("Car is moving")

my_car = Car('BMW', 'X6', 2011)
my_old_car = Car('BMW', 'M3', 1997)
my_new_car = Car('BMW', 'M6', 2020)

print(my_car.make, my_old_car.make,my_new_car.make)
print(my_car.model, my_old_car.model, my_new_car.model)
print(my_car.year, my_old_car.year, my_new_car.year)

### Output
> BMW BMW BMW
> X6 M3 M6
> 2011 1997 2020


























import random
import sys
import os

'''
Comments
Data type: number, string, list, tuple, dictionary
'''

### Print ###
print("Hello World")
name = "Albert"
print(name)

print("5 + 2 =", 5+2)
print("5 - 2 =", 5-2)
print("5 * 2 =", 5*2)
print("5 / 2 =", 5/2)
print("5 % 2 =", 5%2)
print("5 ** 2 =", 5**2)
print("5 // 2 =", 5//2)  # floor division: discard remainder 1, 14.5 =14

quote = " \"Always remember"   # \ is ignoring "
print(quote)

multi_string = quote + name
print(multi_string)
print('\n' * 1)             # 1 new lines

print("%s %s %s" % ('new type quote', quote, name))
print("I don't like ", end="")
print("newlines")


### List  ###
import random
import sys
import os

### List

grocery_list = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']
print(grocery_list)
print('Frist Item', grocery_list[0])
grocery_list[0] = "Orange Juice"        # Change to  Juice to Orange Juice
print('First Item', grocery_list[0])
print(grocery_list[1:3])
other_events = ['Wash car', 'Pickup kids', 'Cash Check']
to_do_list = [other_events, grocery_list]
print (to_do_list)
print((to_do_list[1][1]))    # 1st [] list is other_event which is 0, 2nd [] is grocery_list's 2nd item 1
grocery_list.append('Onion')
print(to_do_list)
grocery_list.insert(1, "Pickle")
print(to_do_list)
grocery_list.remove("Pickle")
print(to_do_list)
grocery_list.sort()
grocery_list.reverse()
del grocery_list[1]
print(to_do_list)
to_do_list2 = other_events + grocery_list
print(to_do_list2)
print(len(to_do_list2))
print(max(to_do_list2))
print(min(to_do_list2))


### TUPLE ###
pi_tuple = (3,1,4,1,5,9)

new_tuple = list(pi_tuple)
new_list = tuple(new_tuple)
len(tuple) min(tuple) max(tuple)

### Dictionaries ###
import random
import sys
import os

super_villains = {'Fiddler'        : 'Isaac Bowin',
                  'Captain Cold'   : 'Leonard Snart',
                  'Weather Wizard' : 'Mark Mardon',
                  'Mirror master'  : 'Sam Scudder',
                  'Pied Piper'     : 'Thomas Peterson'}

print(super_villains ['Captain Cold'])

del super_villains['Fiddler']

super_villains['Pied Piper'] = 'Hartly Rathway'

print(super_villains ['Pied Piper'])

print(super_villains.keys())

print(super_villains.values())


--------------------------------------------------------------------------------######
### Conditional ###
--------------------------------------------------------------------------------######


# if else elif    ==    !=    >    >=    <=
age =30
if age >16:
    print('You can drive')
else:
    print('You cant drive')
print('----')
if age >= 21 :
    print('You can drive')
elif age >= 16 :
    print('drive')
else :
    print ('You can\'t')

# Logical Operators: and, or, not
if ((age >= 1 ) and (age <=18)):
    print("you get a b-day")
elif ((age >= 21 ) and (age <=65)):
    print("you get a b-day")
elif not(age ==30) :
    print('No b-party')
else :
    print('B-Party')



for x in range(0,10):
    print(x, '', end="")
# a new line
print('\n')

grocery_list = [ 'juice', 'tomato', 'potatos','banaba']
for y in grocery_list:
    print(y)

for x in [2,4,6,8,10]:
    print (x)
#list in list
print('\n')

num_list = [[1,2,3],[10,20,30],[100,200,300]]
for x in range(0,3):
    for y in range(0,3):
        print(num_list[x][y])	#<=?? why
		
### While Loop

random_num = random.randrange(0,100)
while(random_num != 15):
    print(random_num)
    random_num = random.randrange(0,100)	
	

i = 0;
while(i <= 20):
    if (i%2 == 0):
        print(i)
    elif (i == 21):
        break
    else:
        i += 1    #<= Python doesn't support i++
        continue
    i += 1
	
###function

def addNumber(firstNum, lastNum):
    sumNum = firstNum + lastNum
    return sumNum
print(addNumber(1, 4))
	

### User Input ###	
import random
import sys
import os

print("What is your name?")
name = sys.stdin.readline()
print("Hello", name)

import sys
for line in sys.stdin:
    print line	

sys.stdin is a file-like object on which you can call functions read or readlines if you want to read everything or you want to read everything and split it by newline automatically. (You need to import sys for this to work.)
If you want to prompt the user for input, you can use raw_input in Python 2.X, and just input in Python 3.	
name = raw_input("Enter your name: ")   # Python 2.x	
name = input("Enter your name: ")   	# Python 3	
	
import random
import sys
import os

long_string = "I will change you if you fall = The Floor ok"
print("1st-",long_string)
	# 1st- I will change you if you fall = The Floor ok
print(long_string[:])
print(long_string[0:4]) #first 4 letters space don't count?
	# I wi
print(long_string[-5])
	# o
print(long_string[:-5])
	# I will change you if you fall = The Flo
print(long_string[:4] + " be there")
	# I wi be there
print("%c is my %s letter and my number %d number is %.5f" %
      ('X', 'favorite', 1, .14))
	# X is my favorite letter and my number 1 number is 0.14000	
	
###	
print(long_string.capitalize())
print(long_string.find("ok"))
print(long_string.isalpha())
print(long_string.isalnum())
print(long_string.replace("Floor", "Ground"))
print(long_string.strip())
print(len(long_string))
quote_list = long_string.split(" ")
print(quote_list)
###
I will change you if you fall = the floor ok
42
False
False
I will change you if you fall = The Ground ok
I will change you if you fall = The Floor ok
44
['I', 'will', 'change', 'you', 'if', 'you', 'fall', '=', 'The', 'Floor', 'ok']
###

	
	
	
	
	
	
	
	
	
	
	


Question 1

What is Python really? 
	- Python is dynamically typed, this means that you don't need to state the types of variables when you declare them 
	  or anything like that. You can do things like x=111 and then x="I'm a string" without error
	-Python is well suited to object orientated programming in that it allows the definition of classes along 
	  with composition and inheritance. Python does not have access specifiers (like C++'s public, private), 
	  the justification for this point is given as "we are all adults here"
	- In Python, functions are first-class objects. This means that they can be assigned to variables, returned from 
	  other functions and passed into functions. Classes are also first class objects
	- Writing Python code is quick but running it is often slower than compiled languages. Fortunately，Python allows 
	  the inclusion of C based extensions so bottlenecks can be optimised away and often are. The numpy package is a 
	  good example of this, it's really quite quick because a lot of the number crunching it does isn't actually done 
	  by Python
	- Python finds use in many spheres - web applications, automation, scientific modelling, big data applications 
	  and many more. It's also often used as "glue" code to get other languages and components to play nice.
	- Python makes difficult things easy so programmers can focus on overriding algorithms and structures rather 
	  than nitty-gritty low level details.
	  
### Question 2

Fill in the missing code:
###
def print_directory_contents(sPath):
    """
    This function takes the name of a directory and prints out the paths files within that 
    directory as well as any files contained in contained directories. 

    This function is similar to os.walk. Please don't use os.walk in your answer. We are interested in your 
    ability to work with nested structures. 
    """
###
	### Answer ###
###
def print_directory_contents(sPath):
    import os                                       
    for sChild in os.listdir(sPath):                
        sChildPath = os.path.join(sPath,sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)
###			
			
Pay special attention
	- be consistent with your naming conventions. If there is a naming convention evident in any sample code, 
	  stick to it. Even if it is not the naming convention you usually use
	- recursive functions need to recurse and terminate. Make sure you understand how this happens so that 
	  you avoid bottomless callstacks
	- we use the os module for interacting with the operating system in a way that is cross platform. 
	  You could say sChildPath = sPath + '/' + sChild but that wouldn't work on windows
	- familiarity with base packages is really worthwhile, but don't break your head trying to memorize 
	  everything, Google is your friend in the workplace!
	- ask questions if you don't understand what the code is supposed to do
	- KISS! Keep it Simple, Stupid!
	Why this matters:
	displays knowledge of basic operating system interaction stuff
	recursion is hella useful
	
	
### Question 3

Looking at the below code, write down the final values of A0, A1, ...An.

A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]
If you dont know what zip is don't stress out. No sane employer will expect you to memorize the standard library. Here is the output of help(zip).

zip(...)
    zip(seq1 [, seq2 [...]]) -> [(seq1[0], seq2[0] ...), (...)]

    Return a list of tuples, where each tuple contains the i-th element
    from each of the argument sequences.  The returned list is truncated
    in length to the length of the shortest argument sequence.
If that doesn't make sense then take a few minutes to figure it out however you choose to.

Answer

A0 = {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4}  # the order may vary
A1 = range(0, 10) # or [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] in python 2
A2 = []
A3 = [1, 3, 2, 5, 4]
A4 = [1, 2, 3, 4, 5]
A5 = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
A6 = [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]]	
	
	
### Question 4

Python and multi-threading. Is it a good idea? List some ways to get some Python code to run in a parallel way.

	Python doesn't allow multi-threading in the truest sense of the word. It has a multi-threading package but 
	if you want to multi-thread to speed your code up, then it's usually not a good idea to use it. Python has 
	a construct called the Global Interpreter Lock (GIL). The GIL makes sure that only one of your 'threads' 
	can execute at any one time. A thread acquires the GIL, does a little work, then passes the GIL onto the 
	next thread. This happens very quickly so to the human eye it may seem like your threads are executing 
	in parallel, but they are really just taking turns using the same CPU core. All this GIL passing adds overhead 
	to execution. This means that if you want to make your code run faster then using the threading package often isn't a good idea.

	There are reasons to use Python's threading package. If you want to run some things simultaneously, and 
	efficiency is not a concern, then it's totally fine and convenient. Or if you are running code that needs 
	to wait for something (like some IO) then it could make a lot of sense. But the threading library wont let 
	you use extra CPU cores.

	Multi-threading can be outsourced to the operating system (by doing multi-processing), some external 
	application that calls your Python code (eg, Spark or Hadoop), or some code that your Python code calls 
	(eg: you could have your Python code call a C function that does the expensive multi-threaded stuff).

	Why this is important
	Because the GIL is an A-hole. Lots of people spend a lot of time trying to find bottlenecks in their 
	fancy Python multi-threaded code before they learn what the GIL is.	
	
	
	
### Question 6
What does this code output:
###
def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l) 
f(2)
f(3,[3,2,1])
f(3)
###

Answer
[0, 1]
[3, 2, 1, 0, 1, 4]
[0, 1, 0, 1, 4]

	The first function call should be fairly obvious, the loop appends 0 and then 1 to the empty list, l. 
	l is a name for a variable that points to a list stored in memory. 
	The second call starts off by creating a new list in a new block of memory. l then refers to this new list. 
	It then appends 0, 1 and 4 to this new list. So that's great. 
	The third function call is the weird one. It uses the original list stored in the original memory block. 
	That is why it starts off with 0 and 1.

l_mem = []

# When f(2)
l = l_mem           # the first call
for i in range(2):
    l.append(i*i)
print(l)            # [0, 1]

# When f(3, [3,2,1])
l = [3,2,1]         # the second call
for i in range(3):
    l.append(i*i)
print(l)            # [3, 2, 1, 0, 1, 4]

# when f(3)
l = l_mem           # the third call
for i in range(3):
    l.append(i*i)
print(l)            # [0, 1, 0, 1, 4]	
	
	
	
### Question 7

What is "monkey patching" and is it ever a good idea?

	Monkey patching is changing the behaviour of a function or object after it has already been defined. 
	For example:

	import datetime
	datetime.datetime.now = lambda: datetime.datetime(2012, 12, 12)

	Most of the time it's a pretty terrible idea - it is usually best if things act in a well-defined way. 
	One reason to monkey patch would be in testing. The mock package is very useful to this end.

	Why does this matter?
	It shows that you understand a bit about methodologies in unit testing. Your mention of monkey avoidance 
	will show that you aren't one of those coders who favor fancy code over maintainable code .
	And it shows that you know a little bit about how Python works on a lower level, 
	how functions are actually stored and called and suchlike.
	
	
### Question 8

What does this stuff mean: *args, **kwargs? And why would we use it?
	Use *args when we aren't sure how many arguments are going to be passed to a function, or if we want 
	to pass a stored list or tuple of arguments to a function. **kwargs is used when we dont know how many 
	keyword arguments will be passed to a function, or it can be used to pass the values of a dictionary 
	as keyword arguments. The identifiers args and kwargs are a convention, you could also use *bob and 
	**billy but that would not be wise.

e.g.

def f(*args,**kwargs): print(args, kwargs)

l = [1,2,3]
t = (4,5,6)
d = {'a':7,'b':8,'c':9}

f()
f(1,2,3)                    # (1, 2, 3) {}
f(1,2,3,"groovy")           # (1, 2, 3, 'groovy') {}
f(a=1,b=2,c=3)              # () {'a': 1, 'c': 3, 'b': 2}
f(a=1,b=2,c=3,zzz="hi")     # () {'a': 1, 'c': 3, 'b': 2, 'zzz': 'hi'}
f(1,2,3,a=1,b=2,c=3)        # (1, 2, 3) {'a': 1, 'c': 3, 'b': 2}

f(*l,**d)                   # (1, 2, 3) {'a': 7, 'c': 9, 'b': 8}
f(*t,**d)                   # (4, 5, 6) {'a': 7, 'c': 9, 'b': 8}
f(1,2,*t)                   # (1, 2, 4, 5, 6) {}
f(q="winning",**d)          # () {'a': 7, 'q': 'winning', 'c': 9, 'b': 8}
f(1,2,*t,q="winning",**d)   # (1, 2, 4, 5, 6) {'a': 7, 'q': 'winning', 'c': 9, 'b': 8}

def f2(arg1,arg2,*args,**kwargs): print(arg1,arg2, args, kwargs)

f2(1,2,3)                       # 1 2 (3,) {}
f2(1,2,3,"groovy")              # 1 2 (3, 'groovy') {}
f2(arg1=1,arg2=2,c=3)           # 1 2 () {'c': 3}
f2(arg1=1,arg2=2,c=3,zzz="hi")  # 1 2 () {'c': 3, 'zzz': 'hi'}
f2(1,2,3,a=1,b=2,c=3)           # 1 2 (3,) {'a': 1, 'c': 3, 'b': 2}

f2(*l,**d)                   # 1 2 (3,) {'a': 7, 'c': 9, 'b': 8}
f2(*t,**d)                   # 4 5 (6,) {'a': 7, 'c': 9, 'b': 8}
f2(1,2,*t)                   # 1 2 (4, 5, 6) {}
f2(1,1,q="winning",**d)      # 1 1 () {'a': 7, 'q': 'winning', 'c': 9, 'b': 8}
f2(1,2,*t,q="winning",**d)   # 1 2 (4, 5, 6) {'a': 7, 'q': 'winning', 'c': 9, 'b': 8} 	
	
	NOte: Sometimes we will need to pass an unknown number of arguments or keyword arguments into a function. 
	Sometimes we will want to store arguments or keyword arguments for later use. Sometimes it's just a time saver.	
	
### Question 9
What do these mean to you: @classmethod, @staticmethod, @property?

	Answer Background knowledge
	These are decorators. A decorator is a special kind of function that either takes a function and returns 
	a function, or takes a class and returns a class. The @ symbol is just syntactic sugar that allows you 
	to decorate something in a way that's easy to read.
###
@my_decorator
def my_func(stuff):
    do_things
###   
   same as 
###
def my_func(stuff):
    do_things
my_func = my_decorator(my_func)
###

You can find a tutorial on how decorators in general work here.
https://www.codementor.io/python/tutorial/advanced-use-python-decorators-class-function

Actual Answer

The decorators @classmethod, @staticmethod and @property are used on functions defined within classes. Here is how they behave:

class MyClass(object):
    def __init__(self):
        self._some_property = "properties are nice"
        self._some_other_property = "VERY nice"
    def normal_method(*args,**kwargs):
        print("calling normal_method({0},{1})".format(args,kwargs))
    @classmethod
    def class_method(*args,**kwargs):
        print("calling class_method({0},{1})".format(args,kwargs))
    @staticmethod
    def static_method(*args,**kwargs):
        print("calling static_method({0},{1})".format(args,kwargs))
    @property
    def some_property(self,*args,**kwargs):
        print("calling some_property getter({0},{1},{2})".format(self,args,kwargs))
        return self._some_property
    @some_property.setter
    def some_property(self,*args,**kwargs):
        print("calling some_property setter({0},{1},{2})".format(self,args,kwargs))
        self._some_property = args[0]
    @property
    def some_other_property(self,*args,**kwargs):
        print("calling some_other_property getter({0},{1},{2})".format(self,args,kwargs))
        return self._some_other_property

o = MyClass()
# undecorated methods work like normal, they get the current instance (self) as the first argument

o.normal_method 
# <bound method MyClass.normal_method of <__main__.MyClass instance at 0x7fdd2537ea28>>

o.normal_method() 
# normal_method((<__main__.MyClass instance at 0x7fdd2537ea28>,),{})

o.normal_method(1,2,x=3,y=4) 
# normal_method((<__main__.MyClass instance at 0x7fdd2537ea28>, 1, 2),{'y': 4, 'x': 3})

# class methods always get the class as the first argument

o.class_method
# <bound method classobj.class_method of <class __main__.MyClass at 0x7fdd2536a390>>

o.class_method()
# class_method((<class __main__.MyClass at 0x7fdd2536a390>,),{})

o.class_method(1,2,x=3,y=4)
# class_method((<class __main__.MyClass at 0x7fdd2536a390>, 1, 2),{'y': 4, 'x': 3})

# static methods have no arguments except the ones you pass in when you call them

o.static_method
# <function static_method at 0x7fdd25375848>

o.static_method()
# static_method((),{})

o.static_method(1,2,x=3,y=4)
# static_method((1, 2),{'y': 4, 'x': 3})

# properties are a way of implementing getters and setters. It's an error to explicitly call them
# "read only" attributes can be specified by creating a getter without a setter (as in some_other_property)

o.some_property
# calling some_property getter(<__main__.MyClass instance at 0x7fb2b70877e8>,(),{})
# 'properties are nice'

o.some_property()
# calling some_property getter(<__main__.MyClass instance at 0x7fb2b70877e8>,(),{})
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'str' object is not callable

o.some_other_property
# calling some_other_property getter(<__main__.MyClass instance at 0x7fb2b70877e8>,(),{})
# 'VERY nice'

# o.some_other_property()
# calling some_other_property getter(<__main__.MyClass instance at 0x7fb2b70877e8>,(),{})
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'str' object is not callable

o.some_property = "groovy"
# calling some_property setter(<__main__.MyClass object at 0x7fb2b7077890>,('groovy',),{})

o.some_property
# calling some_property getter(<__main__.MyClass object at 0x7fb2b7077890>,(),{})
# 'groovy'

o.some_other_property = "very groovy"
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: can't set attribute

o.some_other_property
# calling some_other_property getter(<__main__.MyClass object at 0x7fb2b7077890>,(),{})
# 'VERY nice'
	
	
	
###	Question 10

Consider the following code, what will it output?

class A(object):
    def go(self):
        print("go A go!")
    def stop(self):
        print("stop A stop!")
    def pause(self):
        raise Exception("Not Implemented")

class B(A):
    def go(self):
        super(B, self).go()
        print("go B go!")

class C(A):
    def go(self):
        super(C, self).go()
        print("go C go!")
    def stop(self):
        super(C, self).stop()
        print("stop C stop!")

class D(B,C):
    def go(self):
        super(D, self).go()
        print("go D go!")
    def stop(self):
        super(D, self).stop()
        print("stop D stop!")
    def pause(self):
        print("wait D wait!")

class E(B,C): pass

a = A()
b = B()
c = C()
d = D()
e = E()

# specify output from here onwards

a.go()
b.go()
c.go()
d.go()
e.go()

a.stop()
b.stop()
c.stop()
d.stop()
e.stop()

a.pause()
b.pause()
c.pause()
d.pause()
e.pause()



Answer

The output is specified in the comments in the segment below:

a.go()
# go A go!

b.go()
# go A go!
# go B go!

c.go()
# go A go!
# go C go!

d.go()
# go A go!
# go C go!
# go B go!
# go D go!

e.go()
# go A go!
# go C go!
# go B go!

a.stop()
# stop A stop!

b.stop()
# stop A stop!

c.stop()
# stop A stop!
# stop C stop!

d.stop()
# stop A stop!
# stop C stop!
# stop D stop!

e.stop()
# stop A stop!

a.pause()
# ... Exception: Not Implemented

b.pause()
# ... Exception: Not Implemented

c.pause()
# ... Exception: Not Implemented

d.pause()
# wait D wait!

e.pause()
# ...Exception: Not Implemented

Why do we care?
	Because OO programming is really important. Answering this question shows your understanding of inheritance 
	and the use of Python's super function. Most of the time the order of resolution doesn't matter. 
	Sometimes it does, it depends on your application.


	
	
### Question 11

Consider the following code, what will it output?

class Node(object):
    def __init__(self,sName):
        self._lChildren = []
        self.sName = sName
    def __repr__(self):
        return "<Node '{}'>".format(self.sName)
    def append(self,*args,**kwargs):
        self._lChildren.append(*args,**kwargs)
    def print_all_1(self):
        print(self)
        for oChild in self._lChildren:
            oChild.print_all_1()
    def print_all_2(self):
        def gen(o):
            lAll = [o,]
            while lAll:
                oNext = lAll.pop(0)
                lAll.extend(oNext._lChildren)
                yield oNext
        for oNode in gen(self):
            print(oNode)

oRoot = Node("root")
oChild1 = Node("child1")
oChild2 = Node("child2")
oChild3 = Node("child3")
oChild4 = Node("child4")
oChild5 = Node("child5")
oChild6 = Node("child6")
oChild7 = Node("child7")
oChild8 = Node("child8")
oChild9 = Node("child9")
oChild10 = Node("child10")

oRoot.append(oChild1)
oRoot.append(oChild2)
oRoot.append(oChild3)
oChild1.append(oChild4)
oChild1.append(oChild5)
oChild2.append(oChild6)
oChild4.append(oChild7)
oChild3.append(oChild8)
oChild3.append(oChild9)
oChild6.append(oChild10)

# specify output from here onwards

oRoot.print_all_1()
oRoot.print_all_2()	
	
	
Answer

oRoot.print_all_1() prints:

<Node 'root'>
<Node 'child1'>
<Node 'child4'>
<Node 'child7'>
<Node 'child5'>
<Node 'child2'>
<Node 'child6'>
<Node 'child10'>
<Node 'child3'>
<Node 'child8'>
<Node 'child9'>
oRoot.print_all_2() prints:

<Node 'root'>
<Node 'child1'>
<Node 'child2'>
<Node 'child3'>
<Node 'child4'>
<Node 'child5'>
<Node 'child6'>
<Node 'child8'>
<Node 'child9'>
<Node 'child7'>
<Node 'child10'>


Why do we care?
	Because composition and object construction is what objects are all about. Objects are composed of stuff 
	and they need to be initialised somehow. This also ties up some stuff about recursion and use of generators.

	Generators are great. You could have achieved similar functionality to print_all_2 by just constructing 
	a big long list and then printing it's contents. One of the nice things about generators is that they 
	don't need to take up much space in memory.

	It is also worth pointing out that print_all_1 traverses the tree in a depth-first manner, while print_all_2 
	is width-first. Make sure you understand those terms. Sometimes one kind of traversal is more appropriate 
	than the other. But that depends very much on your application.	
	
	
### Question 12

Describe Python's garbage collection mechanism in brief.

	Python maintains a count of the number of references to each object in memory. If a reference count 
	goes to zero then the associated object is no longer live and the memory allocated to that object 
	can be freed up for something else occasionally things called "reference cycles" happen. 
	The garbage collector periodically looks for these and cleans them up. An example would be if you 
	have two objects o1 and o2 such that o1.x == o2 and o2.x == o1. If o1 and o2 are not referenced 
	by anything else then they shouldn't be live. But each of them has a reference count of 1.
	Certain heuristics are used to speed up garbage collection. For example, recently created objects 
	are more likely to be dead. As objects are created, the garbage collector assigns them to generations. 
	Each object gets one generation, and younger generations are dealt with first.
	This explanation is CPython specific.	
	
	
### Question 13

Place the following functions below in order of their efficiency. They all take in a list of numbers between 0 and 1. 
The list can be quite long. An example input list would be [random.random() for i in range(100000)]. 
How would you prove that your answer is correct?

def f1(lIn):
    l1 = sorted(lIn)
    l2 = [i for i in l1 if i<0.5]
    return [i*i for i in l2]

def f2(lIn):
    l1 = [i for i in lIn if i<0.5]
    l2 = sorted(l1)
    return [i*i for i in l2]

def f3(lIn):
    l1 = [i*i for i in lIn]
    l2 = sorted(l1)
    return [i for i in l1 if i<(0.5*0.5)]


	Most to least efficient: f2, f1, f3. To prove that this is the case, you would want to profile your code. 
	Python has a lovely profiling package that should do the trick.

import cProfile
lIn = [random.random() for i in range(100000)]
cProfile.run('f1(lIn)')
cProfile.run('f2(lIn)')
cProfile.run('f3(lIn)')
For completion's sake, here is what the above profile outputs:

>>> cProfile.run('f1(lIn)')
         4 function calls in 0.045 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.009    0.009    0.044    0.044 <stdin>:1(f1)
        1    0.001    0.001    0.045    0.045 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.035    0.035    0.035    0.035 {sorted}


>>> cProfile.run('f2(lIn)')
         4 function calls in 0.024 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.008    0.008    0.023    0.023 <stdin>:1(f2)
        1    0.001    0.001    0.024    0.024 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.016    0.016    0.016    0.016 {sorted}


>>> cProfile.run('f3(lIn)')
         4 function calls in 0.055 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.016    0.016    0.054    0.054 <stdin>:1(f3)
        1    0.001    0.001    0.055    0.055 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.038    0.038    0.038    0.038 {sorted}
	
	Note: Locating and avoiding bottlenecks is often pretty worthwhile. A lot of coding for efficiency 
	comes down to common sense - in the example above it's obviously quicker to sort a list if it's 
	a smaller list, so if you have the choice of filtering before a sort it's often a good idea. 
	The less obvious stuff can still be located through use of the proper tools. 
	It's good to know about these tools.	
	



1) What is Python? What are the benefits of using Python?

Python is a programming language with objects, modules, threads, exceptions and automatic memory management. The benefits of pythons are that it is simple and easy, portable, extensible, build-in data structure and it is an open source.

2)  What is PEP 8?

PEP 8 is a coding convention, a set of recommendation, about how to write your Python code more readable.

3) What is pickling and unpickling?

Pickle module accepts any Python object and converts it into a string representation and dumps it into a file by using dump function, this process is called pickling.  While the process of retrieving original Python objects from the stored string representation is called unpickling.

4) How Python is interpreted?

Python language is an interpreted language. Python program runs directly from the source code. It converts the source code that is written by the programmer into an intermediate language, which is again translated into machine language that has to be executed.

5) How memory is managed in Python?

Python memory is managed by Python private heap space. All Python objects and data structures are located in a private heap. The programmer does not have an access to this private heap and interpreter takes care of this Python private heap.
The allocation of Python heap space for Python objects is done by Python memory manager.  The core API gives access to some tools for the programmer to code.
Python also have an inbuilt garbage collector, which recycle all the unused memory and frees the memory and makes it available to the heap space.
python

6) What are the tools that help to find bugs or perform static analysis?

PyChecker is a static analysis tool that detects the bugs in Python source code and warns about the style and complexity of the bug. Pylint is another tool that verifies whether the module meets the coding standard.

7) What are Python decorators?

A Python decorator is a specific change that we make in Python syntax to alter functions easily.

8) What is the difference between list and tuple?

The difference between list and tuple is that list is mutable while tuple is not. Tuple can be hashed for e.g as a key for dictionaries.

9) How are arguments passed by value or by reference?

Everything in Python is an object and all variables hold references to the objects. The references values are according to the functions; as a result you cannot change the value of the references. However, you can change the objects if it is mutable.

10) What is Dict and List comprehensions are?

They are syntax constructions to ease the creation of a Dictionary or List based on existing iterable.

11) What are the built-in type does python provides?

There are mutable and Immutable types of Pythons built in types Mutable built-in types

List
Sets
Dictionaries
Immutable built-in types

Strings
Tuples
Numbers
12) What is namespace in Python?

In Python, every name introduced has a place where it lives and can be hooked for. This is known as namespace. It is like a box where a variable name is mapped to the object placed.  Whenever the variable is searched out, this box will be searched, to get corresponding object.

13) What is lambda in Python?

It is a single expression anonymous function often used as inline function.

14) Why lambda forms in python does not have statements?

A lambda form in python does not have statements as it is used to make new function object and then return them at runtime.

15) What is pass in Python?

Pass means, no-operation Python statement, or in other words it is a place holder in compound statement, where there should be a blank left and nothing has to be written there.

16) In Python what are iterators?

In Python, iterators are used to iterate a group of elements, containers like list.

17) What is unittest in Python?

A unit testing framework in Python is known as unittest.  It supports sharing of setups, automation testing, shutdown code for tests, aggregation of tests into collections etc.

18) In Python what is slicing?

A mechanism to select a range of items from sequence types like list, tuple, strings etc. is known as slicing.

19) What are generators in Python?

The way of implementing iterators are known as generators.  It is a normal function except that it yields expression in the function.

20) What is docstring in Python?

A Python documentation string is known as docstring, it is a way of documenting Python functions, modules and classes.

21)  How can you copy an object in Python?

To copy an object in Python, you can try copy.copy () or copy.deepcopy() for the general case. You cannot copy all objects but most of them.

22) What is negative index in Python?

Python sequences can be index in positive and negative numbers.   For positive index, 0 is the first index, 1 is the second index and so forth.  For negative index, (-1) is the last index and (-2) is the second last index and so forth.

23) How you can convert a number to a string?

In order to convert a number into a string, use the inbuilt function str().  If you want a octal or hexadecimal representation, use the inbuilt function oct() or hex().

24) What is the difference between Xrange and range?

Xrange returns the xrange object while range returns the list, and uses the same memory and no matter what the range size is.

25) What is module and package in Python?

In Python, module is the way to structure program. Each Python program file is a module, which imports other modules like objects and attributes.

The folder of Python program is a package of modules.  A package can have modules or subfolders.

26) Mention what are the rules for local and global variables in Python?

Local variables: If a variable is assigned a new value anywhere within the function’s body, it’s assumed to be local.

Global variables: Those variables that are only referenced inside a function are implicitly global.

27) How can you share global variables across modules?

To share global variables across modules within a single program, create a special module. Import the config module in all modules of your application. The module will be available as a global variable across modules.

28) Explain how can you make a Python Script executable on Unix?

To make a Python Script executable on Unix, you need to do two things,

Script file’s mode must be executable and
the first line must begin with # ( #!/usr/local/bin/python)
29) Explain how to delete a file in Python?

By using a command os.remove (filename) or os.unlink(filename)

30) Explain how can you generate random numbers in Python?

To generate random numbers in Python, you need to import command as

import random

random.random()

This returns a random floating point number in the range [0,1)

31) Explain how can you access a module written in Python from C?

You can access a module written in Python from C by following method,

Module =  =PyImport_ImportModule(“<modulename>”);

32) Mention the use of // operator in Python?

It is a Floor Divisionoperator , which is used for dividing two operands with the result as quotient showing only digits before the decimal point. For instance, 10//5 = 2 and 10.0//5.0 = 2.0.

33) Mention five benefits of using Python?

Python comprises of a huge standard library for most Internet platforms like Email, HTML, etc.
Python does not require explicit memory management as the interpreter itself allocates the memory to new variables and free them automatically
Provide easy readability due to use of square brackets
Easy-to-learn for beginners
Having the built-in data types saves programming time and effort from declaring variables
34) Mention the use of the split function in Python?

The use of the split function in Python is that it breaks a string into shorter strings using the defined separator. It gives a list of all words present in the string.	
	
	
	
Basic Python Programming  Interview Questions 

27) How can you copy objects in Python?

The functions used to copy objects in Python are-

1)         Copy.copy () for shallow copy

2)         Copy.deepcopy () for deep copy

However, it is not possible to copy all objects in Python using these functions.  For instance, dictionaries have a separate copy method whereas sequences in Python have to be copied by ‘Slicing’.

28) What is the difference between tuples and lists in Python?

Tuples can be used as keys for dictionaries i.e. they can be hashed. Lists are mutable whereas tuples are immutable - they cannot be changed. Tuples should be used when the order of elements in a sequence matters. For example, set of actions that need to be executed in sequence, geographic locations or list of points on a specific route.

29) What is PEP8?

PEP8 consists of coding guidelines for Python language so that programmers can write readable code making it easy to use for any other person, later on.

30) Is all the memory freed when Python exits?

No it is not, because the objects that are referenced from global namespaces of Python modules are not always de-allocated when Python exits.

31) What does _init_.py do?

_init_.py is an empty py file used for importing a module in a directory. _init_.py provides an easy way to organize the files. If there is a module maindir/subdir/module.py,_init_.py is placed in all the directories so that the module can be imported using the following command-

import  maindir.subdir.module

32) What is the different between range () and xrange () functions in Python?

range () returns a list whereas xrange () returns an object that acts like an iterator for generating numbers on demand.

33) How can you randomize the items of a list in place in Python?

Shuffle (lst) can be used for randomizing the items of a list in Python

34) What is a pass in Python?

Pass in Python signifies a no operation statement indicating that nothing is to be done.

35) If you are gives the first and last names of employees, which data type in Python will you use to store them?

You can use a list that has first name and last name included in an element or use Dictionary.

36) What happens when you execute the statement mango=banana in Python?

A name error will occur when this statement is executed in Python.

37) Write a sorting algorithm for a numerical dataset in Python. 

38) Optimize the below python code-

word = 'word'

print word.__len__ ()

Answer: print ‘word’._len_ ()

39) What is monkey patching in Python?

Monkey patching is a technique that helps the programmer to modify or extend other code at runtime. Monkey patching comes handy in testing but it is not a good practice to use it in production environment as debugging the code could become difficult.

40) Which tool in Python will you use to find bugs if any?

Pylint and Pychecker. Pylint verifies that a module satisfies all the coding standards or not. Pychecker is a static analysis tool that helps find out bugs in the course code.

 41) How are arguments passed in Python- by reference or by value?

The answer to this question is neither of these because passing semantics in Python are completely different. In all cases, Python passes arguments by value where all values are references to objects.

42) You are given a list of N numbers. Create a single list comprehension in Python to create a new list that contains only those values which have even numbers from elements of the list at even indices. For instance if list[4] has an even value the it has be included in the new output list because it has an even index but if list[5] has an even value it should not be included in the list because it is not at an even index.

[x for x in list [: 2] if x%2 == 0]

The above code will take all the numbers present at even indices and then discard the odd numbers.

43) Explain the usage of decorators.

Decorators in Python are used to modify or inject code in functions or classes. Using decorators, you can wrap a class or function method call so that a piece of code can be executed before or after the execution of the original code. Decorators can be used to check for permissions, modify or track the arguments passed to a method, logging the calls to a specific method, etc.

44) How can you check whether a pandas data frame is empty or not?

The attribute df.empty is used to check whether a data frame is empty or not.

45) What will be the output of the below Python code –

def multipliers ():

    return [lambda x: i * x for i in range (4)]

    print [m (2) for m in multipliers ()]

The output for the above code will be [6, 6,6,6]. The reason for this is that because of late binding the value of the variable i is looked up when any of the functions returned by multipliers are called.

46) What do you mean by list comprehension?

The process of creating a list while performing some operation on the data so that it can be accessed using an iterator is referred to as List Comprehension.

Example:

[ord (j) for j in string.ascii_uppercase]

     [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]

47)       What will be the output of the below code

word = ‘aeioubcdfg'

print word [:3] + word [3:]

The output for the above code will be: ‘aeioubcdfg'.

In string slicing when the indices of both the slices collide and a “+” operator is applied on the string it concatenates them.

48)       list= [‘a’,’e’,’i’,’o’,’u’]

print list [8:]

The output for the above code will be an empty list []. Most of the people might confuse the answer with an index error because the code is attempting to access a member in the list whose index exceeds the total number of members in the list. The reason being the code is trying to access the slice of a list at a starting index which is greater than the number of members in the list.

49)       What will be the output of the below code:

def foo (i= []):

    i.append (1)

    return i

>>> foo ()

>>> foo ()

The output for the above code will be-

[1]

[1, 1]

Argument to the function foo is evaluated only once when the function is defined. However, since it is a list, on every all the list is modified by appending a 1 to it.

50) Can the lambda forms in Python contain statements?

No, as their syntax is restrcited to single expressions and they are used for creating function objects which are returned at runtime.

This list of questions for Python interview questions and answers is not an exhaustive one and will continue to be a work in progress. Let us know in comments below if we missed out on any important question that needs to be up here.



	
	
	
	
--------------------------------------------------------------------------------
1. Calculator	
--------------------------------------------------------------------------------
#!/usr/bin/python3.5
def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def multi(x, y):
    return x * y
def div(x, y):
    return x / y

print("Select operation.")
print("1. Addition")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter a choice from 1/2/3/4: "))
# Verify choice
choice = int(input("Ente a choice from 1,2,3,4: "))
if choice == 0:
    print ("0 no option for zero")
elif choice > 4:
    print(" No option choice")
else:
    print("you have entered: ", choice )


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if   choice == '1':
    print(num1,"+",num2,"=",add(num1,num2))
elif choice == '2':
    print(num1,"-",num2,"=",sub(num1,num2))
elif choice == '3':
    print(num1,"x",num2,"=",multi(num1,num2))
elif choice == '4':
    print(num1,"x",num2,"=",div(num1,num2))
else:
    print("You put the wrong input")
--------------------------------------------------------------------------------	
2. Find the Largest Among 3 Numbers
--------------------------------------------------------------------------------
#!/usr/bin/python3.5
print("Please enter 3 numbers to find biggest number among them!")
num1 = int(input("Enter first number: "))
print("You entered: ", num1)
num2 = int(input("Enter second number: "))
print("You entered: ", num2)
num3 = int(input("Enter second number: "))
print("You entered: ", num3)

if (num1 > num2) and (num1 > num3):
    print(num1,"is the biggest")
elif (num2 > num1) and (num2 > num3):
    print(num2,"is the biggest")
else:
    print(num3, "is the biggest.")	
	
--------------------------------------------------------------------------------	
3. Sqroot
--------------------------------------------------------------------------------
# Python Program to calculate the square root

num = float(input('Enter a number: '))
num_sqrt = num ** 0.5
print('The square root of %0.3f is %0.3f'%(num ,num_sqrt))


--------------------------------------------------------------------------------	
4. # Python program to swap two variables
--------------------------------------------------------------------------------
#x = input('Enter value of x: ')
#y = input('Enter value of y: ')
x = 5
y = 10

# create a temporary variable and swap the values
change = x
x = y
y = change

# chgY = x
# chgX = y
# x = chgX
# y = chgY

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))


--------------------------------------------------------------------------------	
random
--------------------------------------------------------------------------------
import random

print(random.randint(0,9))

--------------------------------------------------------------------------------	
check if a number is positive, negative or zero
--------------------------------------------------------------------------------
num = float(input("Enter a number"))
# Using if...elif...else
if num > 0:
    print(num, " is Positive")
elif num == 0:
    print (num, " is Zero")
else:
    print(num, " is Negative Number")
print("")

# Using Nested if
if num >= 0:
    if num == 0:
        print ("Zero")
    else:
        print("Positive")
else:
    print ("Negative")

--------------------------------------------------------------------------------	
Check if a Number is Odd or Even
--------------------------------------------------------------------------------
num = int(input("Enter a number: "))

if (num % 2) == 0:
    print("Even")
else:
    print("odd")
''''------------------------------------'''
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))

--------------------------------------------------------------------------------	
Check Prime Numbers( Can't divide except 1) 2, 3, 5, 7, 11, 13, 17, 19, 23, and 29
http://www.programiz.com/python-programming/examples/prime-number
--------------------------------------------------------------------------------
num = int(input("Enter a number to check prime number: "))
if num > 1:
    for i in range(2, num):  	# e.g. 2..... 100(num)
        if ( num % i ) == 0:   	# modulo
            print(num, "is not a prime number")
            print(i, "times", num//i, "is", num)  #??
            break
#   <- indent for line because of break  
	else:
        print(num, "is a prime number")
else:
    print(num, "can't be used as a prime number!")

	#The break statement, like in C, breaks out of the smallest enclosing for or while loop.
	
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
#   |<- indent on for line, not if line 
	else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')	
	
--------------------------------------------------------------------------------	

--------------------------------------------------------------------------------


--------------------------------------------------------------------------------	

--------------------------------------------------------------------------------


--------------------------------------------------------------------------------	

--------------------------------------------------------------------------------



--------------------------------------------------------------------------------	

--------------------------------------------------------------------------------


--------------------------------------------------------------------------------	

--------------------------------------------------------------------------------

--------------------------------------------------------------------------------	

--------------------------------------------------------------------------------


--------------------------------------------------------------------------------	

--------------------------------------------------------------------------------


--------------------------------------------------------------------------------	

--------------------------------------------------------------------------------



--------------------------------------------------------------------------------	

--------------------------------------------------------------------------------
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	