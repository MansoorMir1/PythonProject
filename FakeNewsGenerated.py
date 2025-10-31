##                     Fake News Headline Generator

# 1- import random module 
import random

# 2- Create subjects lists 
Subjects = ["Maryum ","Nawaz Sharif","Bilawal says","Virat Kholi","Election","Wifi","Robot","Moon"]

Actions = ["Drops catch","when rain comes","cuts off","join tiktok ","Postponed","take selfie","Runs for President","Discoverd to be "]

Objects = ["Says it was a 'gravity issue.'","water comes","Printer voted 'no'","and cabinet learn dance","Politician start working","claims its development project","wins by not taking","Made of cheese "]


# 3- Start Headline generation
while True:
    Subject = random.choice(Subjects)
    Action = random.choice(Actions)
    Object = random.choice(Objects)

    headline = f"Breaking News: {Subject} {Action} {Object}"
    print("\n"+ headline)

    userinput = input("\n Do you Want another News:(yes/no)").strip().lower()
    if userinput == "no":
        break
# Print GoodBye Message
print("\n Thanks for using the Fake News Headline Generator. Have a Fun Day.")
