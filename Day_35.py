from tkinter import *
from textblob import TextBlob


def mainwork():
    get_data = input_txt.get("1.0","end-1c")
    cor = TextBlob(get_data)
    data = cor.correct()
    output_txt.delete("1.0","end-1c")
    output_txt.insert("1.0",data)
root = Tk()

root.title('Spell Checker')

root.geometry("500x350")
root.minsize(500,350)
root.maxsize(500,350)

intro = Label(root, text="Spell Chacker By\n Aniruddh Tiwari",width=23,height=4,bg='light blue',relief='raised')



input_txt = Text(root, width=30,height=5, bg="light pink")

check = Button(text="CHECK",width=20, height=2, command=lambda:mainwork())

output_txt = Text(root, width=30,height=5, bg="Lavender")

intro.pack(pady=((0,20)))
input_txt.pack(pady=((0,20)))
check.pack(pady=((0,20)))
output_txt.pack(pady=((0,20)))

root.mainloop()