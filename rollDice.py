import random
import pandas as pd

faces={
    "1":0,
    "2":0,
    "3":0,
    "4":0,
    "5":0,
    "6":0
}

for i in range(1000):
    num=random.random()
    if num<1/6:
        faces["1"]+=1
    elif num<2/6:
        faces["2"]+=1
    elif num<3/6:
        faces["3"]+=1
    elif num<4/6:
        faces["4"]+=1
    elif num<5/6:
        faces["5"]+=1
    elif num<=1:
        faces["6"]+=1
        
print(faces)
face=list(faces.keys())
count=list(faces.values())

df=pd.DataFrame({"Face":face,"Count":count})
df["Percentage %"]=(df["Count"]/1000)*100
print(df)