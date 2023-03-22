from tkinter import*
from PIL import ImageTk,Image
root=Tk()

root.minsize(650,650)
root.maxsize(650,650)
 

open_img= ImageTk.PhotoImage(Image.open("file.png"))
save_img= ImageTk.PhotoImage(Image.open("save.png"))
play_img= ImageTk.PhotoImage(Image.open("Play.png"))

file_name=Label(root,text="File name :")
file_name.place(relx=0.28,rely=0.03,anchor=CENTER)

input_file_name=Entry(root,)
input_file_name.place(relx=0.46,rely=0.03,anchor=CENTER)

my_file=Text(root,height=35,width=80)
my_file.place(relx=0.5,rely=0.55,anchor=CENTER)

open_button=Button(root,image=open_img,text="Open File",command=openFile)
open_button.place(relx=0.05,rely=0.03,anchor=CENTER)

save_button=Button(root,image=open_img,text="Save File",command=saveFile)
save_button.place(relx=0.06,rely=0.03,anchor=CENTER)

play_button=Button(root,image=open_img,text="Play File",command=playFile)
play_button.place(relx=0.07,rely=0.03,anchor=CENTER)

root.mainloop()