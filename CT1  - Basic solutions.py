#1 Write a program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return empty string.
#example: Input: exercise, Output: exse

x = 'exercise'
a = (x[0:2])
b = (x[6:])
slicing = a+b
print(slicing)
print(len(slicing))
.................................
#2 Write a program to get a string where all the characters have been changed to '@', except the first character
#Example: Input: string, Output: s@@@@

x = "Dhaka"

for i in "Dhaka":
    print(x)
    
print("\n")

print(x.replace("haka", "@@@@"))
.................................
#3 Write a program to add "ing" at the end of the string. If the string already ends with 'ing' then add 'ly' at the end. If the string length of the given string is less than 3 then do not change it.
#Example: Input1: string, Output: stringly, Input2: strong, Output2: stronging

x = input("Enter a string: ")
#print(x)

if len(x) > 3:
    if x[-3:]=="ing":
        x+="ly"
    else:
        x+="ing"
    print(x)
else:
    print(x)
.................................
#4 Write a program to make a new string from the given string by exchanging the first and last characters.
#Example: Input: bangla, Output: aanglb

x = input("Enter a string: ")

if len(x) > 1:
    result = x[-1] + x[1:-1] + x[0]
else:
    x
print(result)
.................................
#5 Write a program to amke a string of odd length greater than 7 and then make a new string made of the middle 3 characters of the given string.
def get_middle(x):
    s_length = len(x)+1
    
    mid = str(s_length/2)
    mid_char = x.find(mid)
    mid_char2 = x[mid_char]
    return mid_char2

def main():
    print("Enter a string: ")
    x = input()
    print("The Three middle characters are: ", get_middle(x))

main()

#print("Length of the string is: ", len(x))
.................................
#6  - Write a program to take 2 string s1 and s2 then create a new tring by appending s2 in the middle of s1.

s1 = "Biplob"
s2 = "Chakma"

def append_middle(s1, s2):
    #mid index of s1
    mid = int(len(s1)/2)
    #print(mid)
    
    x = s1[:mid:] #Get character from index 0-middle from s1
    print(x)
    x = x + s2 #concatenate s2 on x1
    print(x)
    x = x + s1[mid:] #append remaining character from s1
    print("After appending: ", x)
    
    
def main():
    print("Orginal strings are: ", s1, s2)
    append_middle(s1, s2)
    
main()
.................................
#7 - Write a program to reverse a given string.

print("Enter a String: ")
x = input()
print(x[::])
print(x[:-1])
print(x[::-2])
print(x[::-1])
.................................
#8  - Write a program to split a given string on hypens into substrings and display each substring.
#Example: Input: she-is-a-student, Output: she, is, a, student

print("Enter a string with hypens: ")
x = input()

sub_string = x.split("-")
print("Each sub-strings are: ")
#print(sub_string)

for i in sub_string:
    print(i)
.................................
# 9 - Write a program to check if a given string is binary string or not
#Example: Input: 010101010, Output: YES, Input: asbsbs, Output2: No

print("Enter a string: ")
x = input()

a = {'0', '1'}  # set
t = set(x)

if t == a or t == {'0'} or t == {'1'}:
    print("Yes")
else:
    print("No")
.................................
# Write a program to convert a givven string into a lower case string

print("Enter a string with Uppler Case letter: ")
x = input()
print("Output: ", x.lower())
.................................

.................................

.................................

.................................

.................................

.................................

.................................
