from pytube import YouTube
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

folder_name = ""


# Choosing File
def location():
    global folder_name
    folder_name = filedialog.askdirectory()
    # Selecting Path
    if len(folder_name) > 1:
        location.config(text=folder_name, fg='green')
    else:
        location.config(text='Please Choose Path!!', fg='red')


# Downloading video
def download():
    # Checking Quality
    message.config(text="")
    try:
        if len(my_url.get()) > 1:
            if my_quality.get() == choice[0]:
                YouTube(my_url.get()).streams.filter(progressive=True).first().download(folder_name)
                message.config(text='Downloading Completed!!', fg='green')
            elif my_quality.get() == choice[1]:
                YouTube(my_url.get()).streams.get_by_resolution('360p' or '240p').download(folder_name)
                message.config(text='Downloading Completed!!', fg='green')
            elif my_quality.get() == choice[2]:
                YouTube(my_url.get()).streams.filter(progressive=True).last().download(folder_name)
                message.config(text='Downloading Completed!!', fg='green')
            else:
                message.config(text="Please Select Quality!!!", fg='red')
        else:
            message.config(text="Please Enter the Link!!", fg='red')
        link.set('')
    except:
        message.config(text='link not valid')


# Setting Root
root = Tk()

# Setting Geometry and title
root.geometry("500x500")
root.maxsize(500, 500)
root.minsize(500, 500)
root.title("Youtube Video Downloader -By Ritesh kr. Gupta")

# Setting Heading
heading = Label(root, text='Youtube Video Downloader', font=("", 16, 'bold', 'underline'), padx=120, pady=15)
heading.grid(row=1, column=0)

# Setting Entry Url
url_label = Label(root, text="Enter link here : ", font=("", 15), pady=20)
url_label.grid()

# Setting url Entry
link = StringVar()
my_url = Entry(root, width=30, font=("", 12, 'italic'), textvariable=link)
my_url.grid()

# Setting Choose path Button
my_path = Button(root, text='Choose File Location', width=20, bg='red', fg='black', font=('', 12, "bold"),
                 relief=SUNKEN, command=location)
my_path.grid(pady=20)

# Setting label to show path if selected
location = Label(root, text='', font=("", 10), pady=0)
location.grid(pady=0)

# Setting Label for Choosing Quality
quality_label = Label(root, text="Choose Quality", font=("", 15), pady=10)
quality_label.grid(pady=0)

# Setting ComboBox for selecting quality
choice = ['High', 'Medium', 'Low']
my_quality = ttk.Combobox(root, values=choice, text='Choose quality', width=30, )
my_quality.grid(pady=0)

# Setting Download button
my_button = Button(root, text='Download', width=10, bg='red', fg='black', font=('', 10, "bold"), relief=SUNKEN,
                   command=download)
my_button.grid(pady=20)

# Setting the message label for show error
message = Label(root, text="", font=("", 15), pady=20)
message.grid(pady=0)

# Mandatory thinks
root.mainloop()
