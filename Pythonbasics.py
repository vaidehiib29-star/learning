#1.Print Square
#num = int(input("Enter a number: "))
#print("Square =", num * num)


#2.Addition, Subtraction, Multiplication, Division
#a = int(input("Enter first number: "))
#b = int(input("Enter second number: "))

#print("Addition =", a + b)
#print("Subtraction =", a - b)
#print("Multiplication =", a *b)
#print("Division =", a / b)


#3.Even or Odd
#num = int(input("Enter a number: "))
#if num % 2 == 0:
#    print("Even")
#else:
#    print("Odd")    


#4.Cube of Number
#num = int(input("Enter a number: "))
#print("Cube =", num * num * num)


#5.Number +10 and x5
#num = int(input("Enter a number: "))

#print("Number + 10 =", num + 10)
#print("Number * 5 =", num * 5)


#Level 2: if-else

#6.Positive, Negative or Zero
#num = int(input("Enter a number: "))
#if num > 0:
#    print("Positive")
#elif num > 0:
#    print("Negative")
#else:
#    print("Zero")        


#7. Voting Eligibility
#age = int(input("Enter age: "))
#if age >= 18:
#    print("Eligible to vote")
#else:
#    print("Not eligible")    


#8.Divisible by 5
#num = int(input("Enter a number: "))
#if  num % 5 == 0:
#    print("Divisible by 5")
#else:
#    print("Not divisible by 5")    


#9.Greater Number
#a = int(input("Enter first number: "))
#b = int(input("Enter second number: "))

#if a > b:
#    print(a, "is greater")
#else:
#    print(b, "is greater")    


#10. Grade
#marks = int(input("Enter marks: "))
#if marks >= 90:
#    print("Grade A")
#elif marks >= 75:
#    print("Grade B")
#elif marks >= 50:
#    print("Grade C") 
#else:
#    print("Fail")           



#Level 3: Nested if-else

#11. Largest of Three Numbers
#a = int(input("Enter first number: "))
#b = int(input("Enter second number: "))
#c = int(input("Enter third number: "))
#if a > b:
#    if a > c:
#        print(a, "is largest")
#    else:
#        print(c, "is largest")
#else:
#    if b > c:
#        print(b, "is largest")
#    else:
#        print(c, "is largest")                


#12. Leap Year
#year = int(input("Enter year: "))
#if year % 4 == 0:
#    print("Leap Year")
#else:
#    print("Not a Leap Year")     


#13.Usernme and Password
#user = input("Enter username: ")
#password = input("Enter password: ")

#if user == "admin":
#    if passworrd == "1234":
#        print("Login Success")
#    else:
#        print("Wrong Password")
#else:
#    print("Invalid User")            


#14. Even and Divisible by 4
#num = int(input("Enter a number: "))
#if num % 2 == 0:
#    if num % 4 == 0:
#        print("Even and divisible by 4")
#    else:
#        print("Even but not divisible by 4")    


#15. Temperature Check
#temp = int(input("Enter temperature: "))
#if temp >= 40:
#    print("Very Hot")
#elif temp >= 30:
#    print("Hot")
#elif temp >= 20:
#    print("Normal")
#else:
#    print("Cold")    


#Level 4: Loops  

#16. Print 1 to 10
#for i in range(1, 11):
#    print(i)    


#17.print 10 to 1
#for i in range(10, 0, -1):
#   print(i)


#18. Multiplication Table
#num = int(input("Enter a number: "))
#for i in range(1, 11):
#    print(num, "x", i, "=", num * i)      


#19. Sum from 1 to n
#n = int(input("Enter a number: "))
#total = 0
#for i in range(1, n + 1):
#    total = total + i
#print("Sum =", total)    


#20. Count Digits
#num = int(input("Enter a number: "))
#count = 0
#while num> 0:
#    count = count + 1
#    num = num // 10
#print("Digits =", count)


#Python Loops Practice Programs
#Level 1

#1. Print 1 to 20
#for i in range(1, 21):
#    print(i)


#2. Print 20 to 1
#for i in range(20, 0, -1):
#    print(i)


#3.Print Even Numbers(1 to 50)
#for i in range(2, 51, 2):
#    print(i)


#4. Print Odd Numbers
#for i in range(1, 51, 2):
#    print(i)


#5.Print 1 to n
#n = int(input("Enter a number: "))
#for i in range(1, n, -1):
#    print(i)



#Level 2 Loops+Condition

#1. Divisible by 3
#for i in range(1, 101):
#    if i % 3 == 0:
#        print(i)


#2.Divisible by 3 and 5
#for i in range(1, 101):
#    print(i)


#3. Count Even Numbers
#count = 0
#for i in range (1, 51):
#    if i % 2 == 0:
#        count += 1
#print(count)              


#4. Count Numbers Divisible by 7
#n = int(input("Enter a number: "))
#count = 0
#for i in range(1, n + 1):
#    if i % 7 == 0:
#        count += 1
#print("Total number divisible by 7", count)        
    

#5.Numbers Not Divisible by 2
#n = int(input("Enter a number: "))
#for i in range(1, n + 1):
#    if i % 2 != 0:
#        print(i)


#Level 3: Loop + Math Logic

#1. Sum from 1 to n
#n = int(input("Enter a number: "))
#total = 0
#for i in range(1, n + 1):
#    total += 1
#print("sum=", total)    


#2.Factorial
#n = int(input("Enter a  number: "))
#factorial = 1
#for i in range(1, n + 1):
#    factorial *= i
#print("Factorial =", factorial)    


#3.Reverse Number
#n = int(input("Enter a number: "))
#reverse = 0
#while n > 0:
#    digit = n % 10
#    reverse = reverse * 10 + digit
#    n = n // 10
#print("Reverse:", reverse)    


#4. palindrome
#num = int(input("Enter a number: "))
#original = num
#reverse = 0
#while num > 0:
#    digit = num % 10
#    reverse = reverse * 10 + digit
#    num = num // 10
#if original == reverse:
#    print("Palindrome") 
#else:
#    print("Not Palindrome")       


#Sum of Digit
#num = int(input("Enter a number: "))
#total = 0
#while num > 0:
#    digit = num % 10
#    total += digit
#    num = num // 10
#print("Sum of digits:", total)    


#Level 4: Nested Loops

#1. Star Pattern 
#for i in range(1, 6):
#    print("*", i)


#2. Number Pattern 
#for i in range(1, 5):
#    for j in range(1, i + 1):
#        print(j, end="")
#    print()    


#3. Inverted Star Pattern
#for i in range(5, 0, -1):
#    print("*", i)


#4.Multiplication Tables(1-5)
#for i in range(1, 6):
#    for j in range(1, 11):
#        print(i, "*", j, "=", i * j)
#    print()    


#5. All Pairs
#for i in range(1, 4):
#    for j in range(1, 4):
#        print("(", i, ",", j, ")", sep="")




#Challenge Questions

#1. Prime Numbers(1-100)
#for num in range(2, 101):
#    is_prime = True
#    for i in range(2, num):
#        if num % i == 0:
#            is_prime = False
#            break
#        print(num)    


#2.Fibonacci Series
#n = int(input("Enter the numbers of terms:"))
#a = 0
#b = 1
#print("Fibonacci Series: ")
#for i in range(n):
#    print(a, end = "")
#    c = a + b
#    a = b
#    b = c


#3. GCD of Two Numbers
#a = int(input("Enter first Numbers: "))
#b = int(input("Enter second Number: "))
#gcd = 1
#for i in range(1, min(a, b) + 1):
#    if a % i == 0 and b % i == 0:
#        gcd = i
#print("GCD =", gcd)        