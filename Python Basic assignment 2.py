#!/usr/bin/env python
# coding: utf-8



Q 1.What are the two values of the Boolean data type? How do you write them?
Soluton. The two values of boolean Data types are True & False. We will keep the first Latter of both the values Capital like: True, FalseQ 2. What are the three different types of Boolean operators?
Solution. Three differnt type of boolean operators are: "And", "Or", and "Not"Q 3. Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean values for the operator and what it evaluate ).
Solution:
And Truth table 
A	B	Q
0	0	0
0	1	0
1	0	0
1	1	1
Or Truth Table
A	B	Q
0	0	0
0	1	1
1	0	1
1	1	1
Not Truth Table
A	Q
0	1
1	0
Q 4. What are the values of the following expressions?
(5 > 4) and (3 == 5)
not (5 > 4)
(5 > 4) or (3 == 5)
not ((5 > 4) or (3 == 5))
(True and True) and (True == False)
(not False) or (not True)
Sol: False
    False
    True
    False
    False
    True
    
    Q 5. What are the six comparison operators?
Sol.   Six comparison operators are: > , < , >= , <= , === , and !== . Q 6 . How do you tell the difference between the equal to and assignment operators?Describe a condition and when you would use one.
Solution: =                                       	==
It is an assignment operator.	                    It is a relational or comparison operator.
It is used for assigning the value to a variable.	It is used for comparing two values. It returns 1                                                     if both the values are equal otherwise returns 0.
                                                    1==1 True
                                                     1==2 FaluseQ 7. Identify the three blocks in this code:
spam = 0
if spam == 10:
print('eggs')
if spam > 5:
print('bacon')
else:
print('ham')
print('spam')
print('spam')
Sol: The three blocks are everything inside the if statement and the lines print('eggs'), print('bacon') and print('ham').

spam = 10
if spam == 10:
 print('eggs')
if spam > 5:
 print('bacon')
else:
 print('ham')
 print('spam')
 print('spam')


# In[16]:


## Q 8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.
## Sol:
spam = 6
if spam==1:
    print("Hello")
elif spam==2:
    
    print("Howdy")
else:
    print("Greetings!")

 Q 9.If your programme is stuck in an endless loop, what keys you’ll press?
Solution: Ctrl+CQ 10. How can you tell the difference between break and continue?
Solution: The main difference between break and continue is that break is used for immediate termination of loop. On the other hand, 'continue' terminate the current iteration and resumes the control to the next iteration of the loop.Q 11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?
Solution: They all do the same thing. The range(10) call ranges from 0 up to (but not including) 10, range(0, 10) explicitly tells the loop to start at 0, and range(0, 10, 1) explicitly tells the loop to increase the variable by 1 on each iterationQ 12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.
Solution: 
for i in range(1,11):
    print(i)
i = 1
while i<=10:
    print(i)
    i = i+1Q 13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
Solution:  spam.bacon()

# In[ ]:





# In[ ]:




