import random

class Fruitquiz :
    def __init__(self) :
        self.fruits = {'apple':'red' ,
                    'orange':'orange' ,
                    'watermelon':'green',
                    'banana':'yellow'}
        
    def quiz(self):
            while(True):

              fruit,color = random.choice(list(self.fruits.items())) 
              print("what is the color of" , fruit)
              user_answer = input()
              if(user_answer.lower()== color):
                  print("corect answer") 
              else:
                  print("wrong answer") 

              option = (input("enter 0 , if you want to play again otherwise enter 1:"))
              if (option=='0') :
                continue
              else:
                break
              
print("welcome to the fruit quiz")
fruit = Fruitquiz ()
fruit.quiz()
