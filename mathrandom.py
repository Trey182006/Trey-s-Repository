import random
import time

OPERATORS = ["+", "-", "*","//"]  
# using a double divison sign is that it rounds it to a whole number
#Example 15//10=1 if it was a single division sign it would be 15/10=1.5
Min_Num = 5
Max_Num = 15
total_problems=10

def generate_problem():
    left = random.randint(Min_Num, Max_Num)
    right = random.randint(Min_Num, Max_Num)
    operator = random.choice(OPERATORS)
    expr = str(left) + " " + operator + " " + str(right)
    answer=eval(expr)
    return expr, answer
wrong=0
input("Press enter to start!")
print("----------------------")
start_time=time.time()

for i in range(total_problems):
    expr, answer=generate_problem()
    while True:
   
        guess= input("Problem #" + str (i + 1) + ": " + expr + "=")
        if guess== str(answer):
            break
        wrong=wrong+1
end_time=time.time()
total_time=round(end_time-start_time,2)
print("----------------------")
print("Good Job!, You finished in",total_time,"seconds!")