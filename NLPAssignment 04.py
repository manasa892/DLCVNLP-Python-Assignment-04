# -*- coding: utf-8 -*-



#pgm 1.1 - Write a Python Program(with class concepts) to find the area of the triangle using the below
#formula. 
#area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

#Parent Class
class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]
        
    def inputSides(self):
        self.sides = [float(input("Enter side" +str(i+1)+" : ")) for i in range(self.n)]
        
    def dispSides(self):
        for i in range(self.n):
            print("Side", i+1,"is",self.sides[i])
            
#Sub Class
class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3)
        
    def findArea(self):
        a, b, c = self.sides 
        #calculate the semi-perimeter
        s = (a+b+c)/2
        area = (s*(s-a)*(s-b)*(s-c))**0.5
        print("The area of the triangle is %0.2f" %area)
        
#creating the object 
t = Triangle()  

#Invoking the functions 
t.inputSides()
t.dispSides()
t.findArea()


#pgm 1.2 - Write a function filter_long_words() that takes a list of words and an integer n and returns the list
#of words that are longer than n.

def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][1]

#Creating the object 
longest_word = find_longest_word(["dfsdfdfgdf","fdgdfgg"])

#printing the longest_word
print(longest_word)

#Pgm 2.1 - Write a Python program using function concept that maps list of words into a list of integers
#representing the lengths of the corresponding words.

wordlist = ["iff8odd","fdpifdfidf"]

def wordlength(wordlist):
    return list(map(lambda x: len(x),wordlist))

print ("word lengths in array => " +str(wordlength(wordlist)))


#Pgm 2.2 - Write a Python function which takes a character (i.e. a string of length 1) and returns True if it is
#a vowel, False otherwise.

def vowel_check(char):
    if(char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'):
        return True 
    else:
        return False
    
char = input("Enter character : ")

if(char.isalpha() == False):
     exit();

#Invoking the function 
if (vowel_check(char)):
    print(char,"is a vowel");
else:
    print(char, "is not a vowel");
