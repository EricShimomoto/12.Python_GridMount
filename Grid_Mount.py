import tkinter as tk
import pandas as pd
from tkinter import Canvas

df = pd.read_csv('ipas_chg.csv')
        
# print(df.to_string()) 

app = tk.Tk()
app.title("Canvas")
app.geometry("1000x1000")
canvas = Canvas(app,width=1000, height=1000)
canvas.pack()

for i in range(len(df)):
    # if df.iloc[i,4] == "Line":
    #     canvas.create_line(df.iloc[i,0], df.iloc[i,1], df.iloc[i,2], df.iloc[i,3])
    if df.iloc[i,4] == "Box":
        canvas.create_rectangle(df.iloc[i,0], df.iloc[i,1], df.iloc[i,2], df.iloc[i,3])
    # if df.iloc[i,4] == "Retangle":
    #     canvas.create_rectangle(df.iloc[i,0], df.iloc[i,1], df.iloc[i,2], df.iloc[i,3])    
        
    print(i)
    app.update()
    
# for ind in df.index:
#     if df['Type'][ind] == "Line":
#         canvas.create_line(df['x1'][ind], df['y1'][ind],df['x2'][ind], df['y2'][ind])
 



app.mainloop()