######q1
#Write a method that will remove any given character from a String:
## sol:


str1 = "asdasdasd"
def rem_string(char, string):
    for letter in string:
        if letter == char:
            string = string.replace(char,"")
    print(string)
    print(len(string))## to check if the letters has been removed
    
rem_string('a', str1)


##q2
#Write a program to find all prime numbers up to a given range of numbers?
## sol:


def prime_num_checker(num):
    for n in range(2, num):
        if num % n == 0:
            return False
        else:
            return True
    

num = 7
if prime_num_checker(num):
    print("Prime number.")
else:
    print("Not a Prime number.")

##q3
#write a function that count how many the given character repeated in a given string?


str1 = "asdasdasd"
def char_counter(char, string):
    counter = 0
    for letter in string:
        if letter == char:
            counter += 1
        
    print("character ' %s ' has been repeated %d times" % (char, counter))


char_counter("a", str1)