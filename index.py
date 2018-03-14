# number in python
# def main():
# 	print(88/5)
# 	print(88//5)
# 	print(88%5)
# 	print(round(9.45))
# 	print(round(9.5))
# 	print(round(9.45,1))
# 	print(round(6.45,1))
# if __name__ == '__main__':
#     main()

########################################################################

# strings in python
# def main():
# 	str1 = '    This is first '\
# 	       'type of string'
# 	str2 = "    This is second " \
# 	       "type of string"
# 	str3 = '''    This is third
# 	type of string'''
# 	str4 = """    This is forth
# 	type of string"""
# 	print(str1)
# 	print(str2)
# 	print(str3)
# 	print(str4)
#
# if __name__ == '__main__':
#     main()


# so if i write a string in a single line then all the four types will show the blank
# spaces in the output that are mentioned in the string
# but if i do it in multiline string then the difference can be seen
# only third and forth type of string will print the output in the next line but first
# two will not untill and enless i use ''\''  or ""\"" type of defining.
# for raw string use
# 	str = r"This is raw string"

# multiline comment
# '''
# This is
# multiline
# comment
# '''

# string formating- insert a variable in the string
# def main():
# 	number = 10
# 	anothernumber = 20
# 	str = "first number = {} and the second one is {}".format(number,anothernumber)
# 	print(str)
# if __name__ == '__main__':
# 	    main()


#####################################################################



# list, tuples and dictonary in python

# tuples are fixes/immutable but the list is not we can append nay value in the list
# later but same is not possible in the tuples.

# tuples:
# def main():
# 	tup = (10, 20, 30)
# 	print(tup)
# 	print("let's try to print in the different way")
# 	for i in tup:
# 		print(i)
# # 	worked as expected
# if __name__ == '__main__':
#     main()

# list:
# def main():
# 	list = [10, 20, 30]
# 	print(list)
# 	for i in list:
# 		print(i)
# 	list.append(40)
# 	list.insert(0,1)
# 	print(list)
# if __name__ == '__main__':
#     main()


#dictonary: can be called as associative array or hash
# 2 way of making the dictonary

# def main():
# 	dict1 = {"one":1, "two":2}
# 	print(dict1)
#
# 	dict2 = dict([("one",1), ("two",2)])
# 	print(dict2)
#
# 	dict3 = dict(one = 1, two = 2)
# 	print(dict3)
# 	print(dict3["two"])
# 	print(dict2["two"])
# 	print(dict1["two"])
#
# 	dict3["three"] = 3
# 	print(dict3)
#
# 	for i in dict3:
# 		print(i,"=>",dict3[i])
# if __name__ == '__main__':
#     main()




################################################################


# switch-case: it is not there in the python
# but can be implemented using another methods
#
# def main():
# 	days = dict(one = "Monday", two = "Tuesday", three = "wednesday")
# 	case = "one"
# 	print(days[case])   # but here the error will come if the case value is not
# 						# present in the days then as switch case we have to use
# 						# the default value so for that do the following
# 	case = "four"
# 	print(days.get(case,"No match"))
#
# if __name__ == '__main__':
#     main()


####################################################################



# while loop for fibonachi series

# def main():
# 	first = 0
# 	second = 1
# 	print(first,end=' ')
# 	while second<100:
# 		print(second,end=' ')
# 		first, second = second, first+second
# if __name__ == '__main__':
#     main()


#####################################################################
# for loop
#
# def main():
# 	llist = [1, 2, 3]
# 	for i in llist:
# 		print(i,end=" ")
# 	print()
# 	str = "let's try to print this"
# 	for i in str:
# 		print(i,end=" ")
# 	print()
# # 	for keeping the track of index also use enumerate
#
# 	for index, value in enumerate(str):
# 		print(index, value)
#
#
# if __name__ == '__main__': main()


####################################################################

# loop control

# def main():
# 	str = "welcome sourabh how are you feeling today?"
# 	for i in str:
# 		if(i == 'u'):
# 			break
# 		else:
# 			print(i, end=' ')
# # 			same for continue
#
#
# if __name__ == '__main__': main()



#######################################################################

# operations in python
#
# def main():
# 	print(3+2)
# 	print(4*3)
# 	print(5/4)
# 	print(5//2)
# 	print(5%3)
# 	print(divmod(5,2))
# 	x = 3
# 	x +=2
# 	print(x)
# 	print(5 == 5)
# 	print(4 < 5)
# 	a, b = 5, 5
# 	print(a == b)
# 	print(a is b)
# 	k = [3]
# 	l = [3]
# 	print(k == l)
# 	print(k is l)
#
#
# if __name__ == '__main__': main()


##################################################################
# bitwise and reange operatino in python
# and->and, or->or, &->bitwise and,
# slice operation is last value exclusive means the last value is not going to be presented in the output
# def main():
# 	list = [1, 2, 3, 4, 6, 7]
# 	print(True and False)
# 	print(list[:7])
# 	print(list[0:])
# 	print(list[0:2])
# 	print(list[0:7:2])
#
# # 	range operation: here also the last value is not going to be there in the result
# 	for i in range(0,10):
# 		print(i,end=' ')
#
# # list1[:] , : is a short hand operator
#
# 	list2 = []
# 	list2[:] = range(1, 20)
# 	print(list2)
#
#
# if __name__ == '__main__':main()




##########################################################################
# string inbuilt operations
#
# def main():
# 	lower = "i am a lower string"
# 	upper = "I AM A UPPER STRING"
# 	cash = 20
# 	print(lower.upper())
# 	print(upper.lower())
# 	print(lower.capitalize())           #only make the first leter of the string capital
# 	newstring = upper.swapcase();
# 	print(id(upper), "and the new id is ", id(newstring))
# 	print("i am string".upper())
# 	print("i got {}$".format(cash))
# 	print(lower.find("am"))
# 	print(lower.replace("am","will be"))
#
# 	str1 = "   only preceding     spaces"
# 	str2 = "only trailing spaces   "
# 	str3 = "  both   "
# 	print(str1.strip())
# 	print(str2.strip())
# 	print(str3.strip())
# 	print(str1.split(sep=None))
# 	str4 = "i amstring"
# 	str5 = '986574'
# 	print(str4.isalnum())
# 	print(str5.isspace())
# if __name__ == '__main__': main()


##################################################################

# string joins and splits
#
# def main():
# 	no = 4
# 	a = 5
# 	print("this is no = {} and this is a={}".format(no,a))
# 	print("this is no = {0} and this is a={1}".format(no,a))
# 	print("this is no = {1} and this is a={0}".format(no, a))
#
# 	str1 = "Top 10 programming languages in 2018"
# 	u = str1.split()
# 	print(u)
# 	for i in u:
# 		print(i, end='-')
# 	print()
# 	url = '-'.join(u)
#
# 	print(url, ".html")
# 	c = len(u)
# 	print("c is {}".format(c))
# 	for index, value in enumerate(u):
# 		if(index != 5):
# 			print(value,end='-')
# 		elif(index == 5):
# 			print(value)
#
#
# if __name__ == '__main__': main()


######################################################################

# list and tuples inbuilt functions
# def main():
#
# 	tup = tuple(range(20))
# 	lis = list(range(21, 40))
# 	print(tup)
# 	singletup = (1,)
# 	print(type(singletup))
# 	list2 = [1, 2, 3]
# 	list3 = list(range(1, 6))
# 	list4 = list2+list3
# 	print(list4)
#
# 	print(2 in tup)
#
# 	lis.append(200)
# 	print(lis.count(1))
#
# 	print(lis)
#
#
# if __name__ == '__main__': main()


#########################################################################

# handling ordinary file
#
# def main():
# 	# for reading the file
# 	# file = open("file.txt")
# 	# for i in file:
# 	# 	print(i,end='')
#
# # 	for writing a new file
# 	file = open("file.txt")
# 	newfile = open("newfile.txt", 'w+')
# 	for i in file:
# 		print(i, file= newfile, end='' )
#
# if __name__ == '__main__': main()


###############################################################
# handling binary files
#
# def main():
# 	file = open("icon.ico", 'rb')
# 	newicon = open("newicon.ico", 'wb')
# 	buff = 60000
# 	buffer = file.read(buff)
#
# 	while len(buffer):
# 		newicon.write(buffer)
# 		buffer = file.read(buff)                #at last it's value will be 0 so the loop gets terminated
#
#
# if __name__ == '__main__': main()



#################################################################

# try except - try exceptions in python
# when error occur then python will get freez and and statement after that won't execute
# use try except


# def main():
# 	try:
# 		file = open("filee.txt")
# 		for i in file:
# 			print(i, end="")
# 	except IOError as msg:
# 		print("couldn't open the file",msg)
#
#
# if __name__ == '__main__': main()




#####################################################################
#getting started with functions

# def main():
# 	myfun()
#
# def myfun():
# 	print("you are in myfunction")
# 	pincode(301001)
# 	info("sourabh")
# 	info("sourabh",20)
# 	info2("rubal")
# 	info2("rubal",20)
#
# def pincode(pin):
# 	print("my pin is {}".format(pin))
#
# def info(name, age=17):                 #in case if you want a default value then give the default value also
# 	print("my name is {} and age is {}".format(name, age))
#
# def info2(name, age=None):
# 	print("my name is {} and age is {}".format(name, age))
#
#
# if __name__ == '__main__': main()




########################################################################
# multiple arguments in python, args will work as tuples
# if i don't know that how many arguments the user will pass then use *args

# def main():
# 	myfun(1, 2, 3, 5, 4)
#
# def myfun(first, second, *args):
# 	print("first = {} second = {} and rest are {}".format(first, second, args))
#
#
# if __name__ == '__main__': main()


########################################################################
# kwargs(keyword arguments) parameters in python
# kwargs will work as dictorary

# def main():
# 	myfun(1, 3, 4, 5, 6, 7, one = "Monday", two = "Tuesday")
#
# def myfun(first, second, *args, **kwargs):
# 	print("first = {}, second = {}, rest = {}, more rest = {}".format(first, second, args, kwargs))
# 	print(type(args), type(kwargs))
#
# if __name__ == '__main__': main()




#################################################################
# returning values from functions
#
# def main():
#     a = returnFunc()
#     print(type(a))
#     print(id(a))
#     for i in a:
#         print(id(i))
#         print(i, type(i))
#
#
# def returnFunc():
#     return range(10)
#
#
# if __name__ == '__main__': main()



##########################################################################
# generators in python - to save the disk space

# at first i am going to create a sample program and after that generator fun

# def main():
#     num = [1,2,3,4]
#     print(squarelist(num))
#
# def squarelist(num):
#     result = []
#     for i in num:
#         result.append(i*i)
#     return result


# if __name__ == '__main__': main()



# This program will give the result but for large input it will use lots of memory
# and time so we will use generator functions



# generator function doesn't have return statement in it


# def main():
#     num = [1, 2, 3, 4]
#     a = squarelist(num)
#     print(a, type(a))
#     print(next(a), "here we go")
#     # after using the next the control is been passed to the next value in the
#     # generator function so if i try to loop the complete generator function
#     # i won't get the first value
#     for i in a:
#         print(i)
# def squarelist(num):
#     for i in num:
#         yield i*i
#
#
# if __name__ == '__main__': main()





# type 3rd - list comprihension:


# def main():
#     num = [1, 2, 3, 4]
#     a = returnFunc(num)
#     print(a)
#
# def returnFunc(num):
#     return [x*x for x in num]
#
#
# if __name__ == '__main__': main()
#



##################################################################
# searching and replacing with re module

# import re
# def main():
#     file = open("google.txt")
#     for i in file:
#         a = re.subn("(G|g)oogle", "******", i)
#         print(a[0], end="")
#
#
# if __name__ == '__main__': main()



####################################################################
# classes and objects in python

# classes have methods. in python functions and methods are different.
# methods have self as a argument in them but in functions it is not compulsory.
# in python classes doesn't have any public, private, protected like java
# you can use the class in any file


# class Harley:
#     def engine(self):
#         print("Harley got a big engine")
#
#     def loud(self):
#         print("Not All harley bikes makes loud noise")
#
# def main():
#     streetBob = Harley()
#     streetBob.engine()
#     streetBob.loud()
#
#
# if __name__ == '__main__': main()


# if i define the class in a seperate file and want to use it in a different file
# then use
# from filename import classname
# and then all the procedure is same



#########################################################################

#  methods and constructors:


# class Harley:
#
#     def __init__(self, value):
#         print("constructor called")
#         self._cc = value
#
#     def engine(self):
#         print("big engine", self._cc)
#
#     def loud(self):
#         print("not all are loud", self._cc)
#
# def main():
#     fatboy = Harley(1600)
#     fatboy.loud()
#
#     streetdog = Harley(1800)
#     streetdog.engine()
#
#
# if __name__ == '__main__': main()



###################################################################
# getters and setter in python

# class Harley:
#     def __init__(self, **kwargs):
#         self.features = kwargs
#
#     def engine(self):
#         print("big engine", self._cc)
#
#     def loud(self):
#         print("not all are loud", self._cc)
#
#     def setfeatures(self, k, v):
#         self.features[k] = v
#
#     def getfeatures(self, k):
#         return self.features.get(k, None)
#
# def main():
#     streetbob = Harley(one = 1)
#     streetbob.setfeatures('cc', 1600)
#     streetbob.setfeatures('color', 'blue')
#     streetbob.setfeatures('bounty', 'yes')
#     print(streetbob.features)
#
#
# if __name__ == '__main__': main()
#

#######################################################################
# inheritance in python

# class Bike:
#     def seat(self):
#         print("This bike got a seat")
#
#     def tyres(self):
#         print("This bike comes with tyres")
#
# class Harley(Bike):
#     def __init__(self, **kwargs):
#         self.features = kwargs
#
#     def engine(self):
#         print("big engine", self._cc)
#
#     def loud(self):
#         print("not all are loud", self._cc)
#
#     def setfeatures(self, k, v):
#         self.features[k] = v
#
#     def getfeatures(self, k):
#         return self.features.get(k, None)
#
#     def seat(self):
#         print("This is harley's seat")
#         super().seat()                      #using super we can call the parent class function
#
# def main():
#     streetbob = Harley(one = 1)
#     streetbob.setfeatures('cc', 1600)
#     streetbob.setfeatures('color', 'blue')
#     streetbob.setfeatures('bounty', 'yes')
#     print(streetbob.features)
#     streetbob.seat()
#     streetbob.tyres()
#
# if __name__ == '__main__': main()



####################################################################
# Decorators/properties in python

# class Harley:
#     def __init__(self, **kwargs):
#         self.features = kwargs
#
#     def engine(self):
#         print("big engine", self._cc)
#
#     def loud(self):
#         print("not all are loud", self._cc)
#
#     def setfeatures(self, k, v):
#         self.features[k] = v
#
#     def getfeatures(self, k):
#         return self.features.get(k, None)
#
#     @property
#     def topspeed(self):
#         print(self.features.get('topspeed', None))
#
#     @topspeed.setter
#     def topspeed(self, ts):
#         self.features['topspeed'] = ts
#
#     @topspeed.deleter
#     def topspeed(self):
#         del self.features['topspeed']
#
# def main():
#     streetbob = Harley(one = 1)
#     streetbob.setfeatures('cc', 1600)
#     streetbob.setfeatures('color', 'blue')
#     streetbob.setfeatures('bounty', 'yes')
#     print(streetbob.features)
#
#
#     streetbob.topspeed = 450
#     streetbob.topspeed
#     del streetbob.topspeed
#     streetbob.topspeed
#
#
# if __name__ == '__main__': main()





################################################################
# python standard libraries

# import urllib.request
# import re
# def main():
#     regularexp = "(\"https.*\"|\"http.*\")"
#     web = urllib.request.urlopen("https://www.python.org/")
#     for i in web:
#         print(str(i, encoding="utf_8"), end= "")
#     web = urllib.request.urlopen("https://www.python.org/")
#     for i in web:
#         s = str(i, encoding='utf_8')
#         a = re.search(regularexp, s)
#         if a:
#             print(a.group())
#
#
# if __name__ == '__main__': main()



####################################################################
# third party modules
#
# simply download them and using cmd go in the zipped folder
# then type "python3 setup.py install"




######################################################################

# sqlite3
# import sqlite3
# def main():
#     db = sqlite3.connect('harley.db')
#     db.execute("create table bike (bike text, cc int)")
#     db.execute("insert into bike values('harley', 455)")
#     db.execute("insert into bike values('pashion', 600)")
#     db.execute("insert into bike values('yamaha', 500)")
#     db.execute("insert into bike values('streetbob', 900)")
#     db.commit()
#     cursor = db.execute("select bike, cc, rowid from bike order by cc")
#     for i in cursor:
#         print(i)
#
#
# if __name__ == '__main__': main()




######################################################################
# web scraping in python 1
# getting the title of the lco website

# import requests
# import bs4
# def main():
#     res = requests.get('https://learncodeonline.in')
#     soup = bs4.BeautifulSoup(res.text, 'lxml')
#     hi = soup.select('title')
#     print(hi[0])
#     print(hi[0].getText())
#
#
# if __name__ == '__main__': main()



######################################################################
# web scraping in python 2
# to get all the heading in the https://en.wikipedia.org/wiki/Machine_learning

import requests
import bs4
def main():
    res = requests.get('https://en.wikipedia.org/wiki/Machine_learning')
    soup = bs4.BeautifulSoup(res.text,'lxml')
    a = soup.select('title')
    print(a[0].text)
    b = soup.select('.toctext')
    c = soup.select('.tocnumber')
    for i in range(0,len(b)):
        x = c[i].text
        print(c[i].text, b[i].text)


if __name__ == '__main__': main()
