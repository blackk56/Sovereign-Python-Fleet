# ===================================================================
# Dream house currency goal project 01 - (IF, ELIF, ELSE...) Project
# ===================================================================

User_Name: str = input("Type your name:... ")

Current_Cash = int(float(input("Type your current cash in USD: ")))

Target_Cash: float = 100000

# 1. First rule:The if statement
if User_Name != "Max":
    print("Sorry Mate, Looks like you are not Max.")

# 2. Second rule:The elif statement
elif Current_Cash >= Target_Cash and not Current_Cash < Target_Cash:
    print("Congrats Max,The cash goal is achieved")

elif Current_Cash < Target_Cash and Current_Cash >= 50000:
    print("You passed your halfway, Mashallah, You are almost there G !")

elif Current_Cash < 50000 and Current_Cash >= 10000 or Current_Cash < 10000:
    print("Pretty cool number, You always got it inshallah, dont give up G !")

# 3. Third rule:The else statement 
else:
    print("Don't worry Max, You got it inshallah, keep trying.")
