from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar
from tkinter import messagebox
from tkinter import filedialog
from pytube import YouTube
from PIL import Image,ImageTk
from datetime import timedelta
import io
import requests

window=Tk()
window.title("Opening YouTube Video Downloader....")
window.geometry("650x550")

image=Image.open("youtube1.png")
resize_img=image.resize((650,550))
img=ImageTk.PhotoImage(resize_img)

limg=Label(window,image=img,bd=0)
limg.image=img
limg.place(x=0,y=0)

bar = Progressbar(window,orient=HORIZONTAL,length=650,mode="determinate")
bar.start(10)
bar.place(x=0,y=530)

def main_window():
    window.destroy()
    root=Tk()
    root.title("YouTube Video/Audio Downloader")
    root.geometry("650x550")
    root.configure(bg="old lace")
    
    def search():
        if ("youtube.com/watch" not in q.get()):
            messagebox.showinfo("Missing","Enter valid url")

        elif len(q.get()) != 0:    
            info = list()
            yt = YouTube(q.get())

            response = requests.get(yt.thumbnail_url)
            img_byte = io.BytesIO(response.content)
            i1mg = Image.open(img_byte)
            i1mg = i1mg.resize((180, 140), Image.LANCZOS)
            i1mg = ImageTk.PhotoImage(i1mg)

            thumbnail = Label(root, image= i1mg, font = ("times new roman", 15))
            thumbnail.image=i1mg
            thumbnail.place(x = 10, y = 330, width = 182, height = 154)
            
            dd1=Label(root,text="Title",font = ("Helvetica",14),bg="old lace").place(x=210,y=330)
            dd2=Label(root,text=": " + yt.title,font = ("Helvetica",14),bg="old lace").place(x=320,y=330)
            dd3=Label(root,text="Views",font = ("Helvetica",14),bg="old lace").place(x=210,y=360)
            dd4=Label(root,text=": " + str(yt.views),font = ("Helvetica",14),bg="old lace").place(x=320,y=360)

            a = timedelta(seconds=yt.length)
            dd5=Label(root,text="Duration",font = ("Helvetica",14),bg="old lace").place(x=210,y=390)
            dd6=Label(root,text=": " + str(a) + "seconds",font = ("Helvetica",14),bg="old lace").place(x=320,y=390)
            dd7=Label(root,text="Rating",font = ("Helvetica",14),bg="old lace").place(x=210,y=420)
            dd8=Label(root,text=": " + str(yt.rating),font = ("Helvetica",14),bg="old lace").place(x=320,y=420)
            cf=Label(root,text="Choose Format :",font = ("Helvetica",14),bg="old lace",fg="black")
            cf.place(x=10,y=207)

            def browse():
                dir=filedialog.askdirectory()
                path.set(dir)

            def downloader():
                choice=v.get()
                df=path.get()
        
                if len(q.get()) != 0 and df and choice == 1:
                    vid = YouTube(q.get()).streams.filter(file_extension="mp4").first()
                    vid.download(df)
                    messagebox.showinfo("Successful","Successfully Downloaded Video In\n"+df)
                    SearchBox.delete(0,END)
                    PathBox.delete(0,END)

                elif len(q.get()) != 0 and df and choice == 2:
                    audio = YouTube(q.get()).streams.filter(only_audio = True).first()
                    audio.download(df)
                    messagebox.showinfo("Successful","Successfully Downloaded Audio In\n"+df)
                    SearchBox.delete(0,END)
                    PathBox.delete(0,END)

                elif len(q.get()) != 0 and df and not choice:
                    messagebox.showinfo("Missing","Please select format")

                elif len(q.get()) != 0 and not df and not choice:
                    messagebox.showinfo("Missing","Please select format and destination")

                elif len(q.get()) != 0 and not df and choice:
                    messagebox.showinfo("Missing","Please select destination")
                    
                elif not len(q.get()) != 0 and df and not choice:
                    messagebox.showinfo("Missing","Please enter a URL and select extension")

                elif not len(q.get()) != 0 and df and choice:
                    messagebox.showinfo("Missing","Please enter a URL")

                elif not len(q.get()) != 0 and not df and choice:
                    messagebox.showinfo("Missing","Please enter a URL and select destination")

                elif not len(q.get()) != 0 and not df and not choice:
                    messagebox.showinfo("Missing","Please fill the required fields")
                    
                elif not len(q.get()) != 0 and not df:
                    messagebox.showinfo("Missing","Please enter URL and select Destination")

            v=IntVar()
            VideoRadio = Radiobutton(root, text="Video", variable=v, value=1,bg="gold",width=5)
            VideoRadio.place(x=160,y= 210)
            AudioRadio = Radiobutton(root, text="Audio", variable=v, value=2,bg="gold",width=5)
            AudioRadio.place(x=235,y= 210)

            label1=Label(root,text="Destination :",font = ("Helvetica",14),bg="old lace",fg="black")
            label1.place(x=10,y=250)

            path=StringVar()
            PathBox=Entry(root,textvariable=path,font = ("Helvetica",10),width=45,bd=9)
            PathBox.place(x=125,y=250)

            BrowseBtn=Button(root,text="Browse",font =("segoe UI",10),width =10,bg="gold",bd = 5,command=browse)
            BrowseBtn.place(x=470,y=247)

            DownloadBtn=Button(root,text="Download ↓",font = ("Verdana",10,"bold"),bg="red",fg="white",bd = 9,command = downloader)
            DownloadBtn.place(x=250,y=500)
            
    image=Image.open("youtube1.png")
    resize_img=image.resize((545,140))
    img=ImageTk.PhotoImage(resize_img)

    limg=Label(root,image=img,bd=0)
    limg.image=img
    limg.place(x=0,y=2)

    label2=Label(root,text="Video URL :",font = ("Helvetica",14),bg="old lace",fg="black")
    label2.place(x=10,y=165)

    q=StringVar()
    SearchBox=Entry(root,textvariable=q,font = ("Helvetica",10),width=45,bd = 9)
    SearchBox.place(x=125,y=165)

    SearchBtn=Button(root,text="Search",font = ("segoe UI",10),width = 10,bg="gold",bd = 5,command = search)
    SearchBtn.place(x=470,y=163)

window.after(1500,main_window)
mainloop() 
