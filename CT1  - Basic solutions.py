#1
x = 'exercise'
a = (x[0:2])
b = (x[6:])
slicing = a+b
print(slicing)
print(len(slicing))
.................................
#2
x = "Dhaka"

for i in "Dhaka":
    print(x)
    
print("\n")

print(x.replace("haka", "@@@@"))
.................................
#3
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
#4
x = input("Enter a string: ")

if len(x) > 1:
    result = x[-1] + x[1:-1] + x[0]
else:
    x
print(result)
.................................
#5
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
#6  - Appending
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
#7 - Reverse String:

print("Enter a String: ")
x = input()
print(x[::])
print(x[:-1])
print(x[::-2])
print(x[::-1])
.................................
#8  - Split
print("Enter a string with hypens: ")
x = input()

sub_string = x.split("-")
print("Each sub-strings are: ")
#print(sub_string)

for i in sub_string:
    print(i)
.................................
# 9 - set - comparison

print("Enter a string: ")
x = input()

a = {'0', '1'}  # set
t = set(x)

if t == a or t == {'0'} or t == {'1'}:
    print("Yes")
else:
    print("No")
.................................
# 10

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
