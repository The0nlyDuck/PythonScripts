# Reading an excel file using Python 
import xlrd, random


Answer = ["A: ", "B: ", "C: ", "D: "]
Score = 0
Check = ["A", "B", "C", "D"]
Value = [0,1,2,3,4,5,6,7,8,9]
  
# To open Workbook 
wb = xlrd.open_workbook("Quiz.xlsx") 
  
# Gets sheet data
def question(number,Index):
    print(Index.cell_value(number, 0))
    for i in range(1,5):
        print(Answer[i-1] + Index.cell_value(number, i) + "\n")
        
# Answering the Question
    correct = input("Which is correct? ")
    if correct.upper() in Check:
        if correct.upper() == Index.cell_value(number, 5):
            return True
    else:
        print("Please use the answers shown.\n")
        question(Qu, Sheet)
        
    
# Running the questions and getting the scores
for l in range(0,2):
    Sheet = wb.sheet_by_index(l)
    print("/// PART " + str(l + 1) + " ///")
    for n in range(0,5):
        Qu = random.choice(Value)
        Value.remove(Qu)
        if question(Qu, Sheet) == True:
            Score = Score + 1
        print("")
    

    
print(str(Score) + "/10")
