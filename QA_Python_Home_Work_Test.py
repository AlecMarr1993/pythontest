#1
number_list = [1, 0, -52, 3, 5, -8, 13, 21, 34, -55, 89]
number_sorted = sorted(a for a in number_list if a <= 5)
print(number_sorted)


#2
def diff(numbers_1, numbers_2):
    li_dif = [a for a in numbers_1 and numbers_2 if a in numbers_1 and a in numbers_2]
    return li_dif
numbers_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
numbers_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13];
numbers_3 = diff(numbers_1, numbers_2)
print(numbers_3)



#3
my_list = [6, 5, 9, 7, 16, 35, 73]
print("first element is" ,my_list[0])
print("last element is", my_list[-1])



#4
string_numbers = "23,45,-7,45,-6,7,8,44,0"
def convert(random_string):
    random_list = random_string.split(",")
    random_cortege = tuple(random_list)
    random_set =set(random_list)
    print(random_list)
    print(random_set)
    print(random_cortege)
convert(string_numbers)

#5
my_text = "Number of characters in this text is bigger then my))"
all_freq = {}

for i in my_text:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
print(all_freq)
print (len(my_text))

#6



#7
a_string = "Exception breakpoints: suspend the program when Exception or its subclasses are thrown.In PyCharm, you can set breakpoints for Python exceptions."
new_string = a_string.replace(" ", "_")
print(new_string)


#8
def count(string, character):
    res = 0

    for i in range(len(string)):
        if (string[i] == character):
            res = res + 1
    return res

string = "fuck my code knowledge"
character = 'e'
print(count(string, character))



#9
def isPalindrome(word):
    return word == word[::-1]
word = "kayak"
answer = isPalindrome(word)

if answer:
    print("Yes")
else:
    print("No")


#10
my_dict = {'a':234, 'b':34, 'c': 375,'d':934, 'e':5271, 'f': 1945}
my_keys = sorted(my_dict, key=my_dict.get, reverse=True)[:3]
print(my_keys)