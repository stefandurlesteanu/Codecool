
ideas = open("/home/stefan/Python/Codecool/3rd_SI_week/Idea_bank/ideas.txt", "a+")
new_idea = input("What is your new idea: ")


count = len(open("/home/stefan/Python/Codecool/3rd_SI_week/Idea_bank/ideas.txt").readlines(  ))

idea_num = str((count + 1)) + "."
ideas.write(idea_num + new_idea + "\r\n")
ideas.close()




ideas = open("/home/stefan/Python/Codecool/3rd_SI_week/Idea_bank/ideas.txt", "r")
print("\n\nYour idea bank: \n")

for idea in ideas:
    print (idea)
ideas.close()

