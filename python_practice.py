list = ([num for num in range(1,5)]);

[num*20 for num in [1,2,3,4,5,6]]

list = ["Elie","Tim","Matt"] 

[val[0] for val in ["Elie","Tim","Matt"]]

{val[0]:val[1] for val in [("name", "Elie"), ("job", "Instringuctor")]}

l1 = ["CA", "NJ", "RI"]
l2 = ["California", "New Jersey", "Rhode Island"]

{l1[i]:l2[i] for i in range(len(l1))}

[num for num in [1,2,3,4,5,6] if num % 2 == 0]

[num for num in [1,2,3,4] if [3,4,5,6].count(num) != 0]

[val for val in ["Elie","Matt","Tim"] if len(val) > 3]

len([val for val in ["Elie", "Tim", "Matt"] if val.find("M") != -1 or val.find("m") != -1])
len([val for val in ["Elie", "Tim", "Matt"] if val.lower().find('m') > -1])

{val:0 for val in "aeiou"}

[char for char in "awesome"]

len([char for char in "awesome" if char.lower() == 'e'])

len([char for char in "awesome" if char.lower() in 'aeiou'])

[val[::-1].lower() for val in ["Elie", "Tim", "Matt"] ]

nested = [[1,2,3],[4,5,6],[7,8,9]]

[ [val*10 for val in sub_array] for sub_array in nested]

[char for char in "first" if "third".find(char) > -1]

[num for num in range(1,101) if num % 12 == 0]

[char for char in "amazong" if char not in "aeiou"]

[[num for num in range(3)] for outer in range(3)]

[[num for num in range(10)] for outer in range(11)]

def sequence_nums(begin_number, end_number, step):
	return sum(range(begin_number, end_number + 1, step))

l1 = [('name', 'Elie'), ('job', 'Instringuctor')]
{val[0]:val[1] for val in l1}

l1 = ["CA", "NJ", "RI"] 
l2 = ["California", "New Jersey", "Rhode Island"]
{l1[i]:l2[i] for i in range(len(l1))}

{key: "O" for key in ["a","e","i","o","u"]}

numbers = [num for num in range(1,27)]
letters = [chr(char) for char in range(65,91)]
{numbers[i]:letters[i] for i in range(26)}

{(i+1):chr(i+65) for i in range(26)}

string = "awesome sauce"

{vowel: "awesome sauce".count(vowel) for vowel in "aeiou"}

def difference(a,b):
	"""this function takes in two parameters and returns the difference between the two"""
	return max(a,b) - min(a,b)

def product(a,b):
	"""this function takes in two parameters and returns the product of the two"""
	return a * b

def print_day(num):
	"""this function takes in one parameter (a number from 1-7)
	 and returns the day of the week (1 is Sunday, 2 is Monday, 3 is Tuesday etc.).
	  If the number is less than 1 or greater than 7, the function should return None"""
	week = {1:"Sunday",2:"Monday",3:"Tuesday",4:"Wednesday",
	5:"Thursday",6:"Friday", 7: "Saturday"}
	if num not in list(range(1,8)):
		return None
	else:
		return week[num];

def last_element(list):
	"""this function takes in one parameter (a list) and returns 
	the last value in the list. It should return None if the list is empty."""
	if len(list) < 1:
		return None
	return list[-1]

def number_compare(a,b):
	"""this function takes in two parameters (both numbers). If the first is 
	greater than the second, this function returns "First is greater." If the second
	 number is greater than the first, the function returns "Second is greater." 
	 Otherwise the function returns "Numbers are equal."""
	if a > b:
	 	return "First is greater"
	elif b > a:
	 	return "Second is greater"
	else:
	 	return "Numbers are equal"

def single_letter_count(string1,string2):
	"""this function takes in two parameters (two stringings). The first parameter 
	should be a word and the second should be a letter. The function returns the 
	number of times that letter appears in the word. The function should be case 
	insensitive (does not matter if the input is lowercase or uppercase). If the 
	letter is not found in the word, the function should return 0."""
	return string1.lower().count(string2.lower())

def multiple_letter_count(string):
	return {letter:string.count(letter) for letter in string}

def list_manipulation(list,cmd,idx=0,val=0):
	if cmd is 'add':
		if idx is 'beginning':
			list.insert(0,val)
			return list
		elif idx is 'end':
			list.append(val)
			return list
	if cmd is 'remove':
		if idx is 'beginning':
			return list.pop(0)
		if idx is 'end':
			return list.pop()
		
def is_palindrome(string):
	return string.lower() == string.lower()[::-1]

def frequency(list, search_term):
	return list.count(search_term)

def flip_case(string, search_term):
	return "".join([char.swapcase() if char.lower() == search_term.lower() else 
		char for char in [letter for letter in string]])
	# swaps = [idx for idx,val in enumerate(chars) if val.lower() == search_term.lower()]
	# for idx in swaps:
	# 	chars[idx] = chars[idx].swapcase()
	# return "".join(chars)
	###########
		# ans = ""
	# for char in string:
	# 	if char.lower() == search_term.lower():
	# 		ans += char.swapcase()
	# 	else:
	# 		ans += char
	# return ans;

def multiply_even_numbers(list):
	ans = 1
	for num in ([num for num in list if num % 2 == 0]):
		ans *= num
	return ans

def mode(lst):
	mode, freq = 0,0
	d = {val:lst.count(val) for val in set(lst)}
	for val in d.items():
		if val[1] > freq:
			mode, freq = val[0], val[1]
	return mode

	# ans = 0
	# s = set(lst)
	# for val in s:
	# 	if lst.count(val) > ans:
	# 		ans = val
	# return ans

def captalize(string):
	return string[0].upper() + string[1:]

def compact(lst):
	return [val for val in lst if bool(val)]

def intersection(lst1, lst2):
	set1 = set(lst1)
	set2 = set(lst2)
	return list(set1.intersection(set2))
	# ans_list = []
	# for val in lst1:
	# 	if val in lst2:
	# 		ans_list.append(val)
	# return ans_list

def partition(lst, callback):
	t = [val for val in lst if callback(val)]
	f = [val for val in lst if not callback(val)]
	return [t,f]

def once(callback):
	def inner(*args):
		if callback.count == True:
			print("This is done")
			return None
		else:
			callback.count = True
			return callback(*args)
	callback.count = False
	callback.callback = callback
	return inner

# call @once
# 	callback definition(args)

{val[0]:val[1] for val in [("name", "Elie"), ("job", "Instringuctor")]}



class Student():
	#instance info, set on every instance
	def __init__(self,fname,lname):
		self.fname = fname
		self.lname = lname
	# instance method, on every instance
	def full_name(self):
		return "My name is {} {}".format(self.fname, self.lname)
	#whatever goes under here will be "decorated" by what is above
	#is on the class constructor itself, not each instance
	@classmethod
	def hello(cls):
		return "Hello from the Student class, {}".format(cls) 
	@staticmethod
	def hi():
		return "Static hi from the Student Class"

