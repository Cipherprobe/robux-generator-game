import tkinter as tk
from tkinter import messagebox
from playsound import playsound
import webbrowser
import os
import time

window = tk.Tk()
window.title("Robux generator working not fake 2023")
window.iconbitmap("robux.ico")
window.geometry("600x400")

robux = 0
label2 = None


entry = tk.Entry(fg="black", bg="white", width=75)
label = tk.Label(text="Enter Roblox User ID:")
id = entry.get()
label2 = tk.Label(text="Generated " + str(robux) + " Robux!")
label2.place(relx = 0.5, rely = 0.5, anchor = 'center')

def open_chrome():
    url = 'https://www.google.com/search?q=YOUR+COMPUTER+IS+GONE&sxsrf=AJOqlzWr0dnHbUu9T24DEltH2zuL2lfa3A%3A1673500491897&source=hp&ei=S5e_Y5W2NKadkPIPgPey-A4&iflsig=AK50M_UAAAAAY7-lWwGnDX93g8K9LImb5HgYDKjena_U&ved=0ahUKEwjVh-WSo8H8AhWmDkQIHYC7DO8Q4dUDCAk&uact=5&oq=YOUR+COMPUTER+IS+GONE&gs_lcp=Cgdnd3Mtd2l6EAMyBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIFCAAQhgMyBQgAEIYDMgUIABCGAzoHCCMQ6gIQJzoECCMQJzoICC4Q1AIQkQI6BAgAEEM6CggAELEDEIMBEEM6DgguEIAEELEDEMcBENEDOgcILhDUAhBDOgQILhBDOgsILhCDARCxAxCABDoLCC4QgAQQsQMQgwE6BQgAEJECOggILhCxAxCABDoKCC4QsQMQ1AIQQzoRCC4QgwEQxwEQsQMQ0QMQgAQ6EQguEIAEELEDEIMBEMcBENEDOgsIABCABBCxAxCDAToQCC4QsQMQgwEQxwEQ0QMQQzoKCC4QsQMQgwEQQzoFCC4QkQI6CAgAEIAEELEDOhkILhCABBCxAxCDARCxAxDHARDRAxDUAhAKOgUILhCABDoKCAAQgAQQsQMQCjoKCAAQsQMQgwEQCjoKCAAQgAQQhwIQFDoFCAAQgAQ6BQgAELEDOgQIABADOg4ILhCABBCxAxCDARDUAjoICAAQsQMQgwE6CAgAEBYQHhAPUO44WJJjYOZwaAZwAHgCgAGWA4gB9SOSAQo3LjExLjMuNC4xmAEAoAEBsAEK&sclient=gws-wiz'
    browser = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

    webbrowser.get(browser)
    webbrowser.open(url)

def open_roblox():
    url = "https://www.roblox.com/users/" + id + "/profile"
    browser = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

    webbrowser.get(browser)
    webbrowser.open(url)

def game():
    global robux
    robux+=1
    label2.configure(text="Generated " + str(robux) + " Robux!")
    if (robux >= 69):
        tk.messagebox.showerror("Robux Generator", "Uh oh, looks like the generator is having some problems.")
        tk.messagebox.askyesno("Robux Generator", "Do you want to proceed?")
        tk.messagebox.askyesno("Confirmation", "Are you sure?")
        playsound("audio/static.wav")
        tk.messagebox.showwarning("You shouldn't have done that.", "You shouldn't have done that.")
        window.destroy()
        playsound("audio/glitch.wav")
        path = "C:/Users/clayt/Desktop/102039912034.txt"
        with open(path, 'w') as f:
            f.write("And God made two great lights; the greater light to rule the day, and the lesser light to rule the night - Genesis 1:16")
            f.close()
        playsound("audio/scream.wav")
        for i in range(5):
            open_chrome()
            time.sleep(1)
        open_roblox()
        playsound("audio/itsybitsyspider.wav")
        user = os.getlogin()
        tk.messagebox.askyesnocancel("Question 1", "Do you believe that you are above all others, " + user + "?")
        tk.messagebox.askyesnocancel("Question 2", "Do you believe there is a God, " + user + "?")
        tk.messagebox.askyesnocancel("Question 3", "Have you ever thought about killing a loved one, " + user + "?")
        for i in range(10):
            tk.messagebox.askyesnocancel("CLOSE ME", "I will make you see, " + user)
            time.sleep(0)
        path2 = "C:/Users/clayt/Desktop/VGltZSBpcyBtYXJjaGluZyB0b3dhcmRzIG91ciBpbmV2aXRhYmxlIGRlYXRoLg==.txt"
        with open(path2, 'w') as k:
            k.write("Never gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you")
            k.close()

button = tk.Button(
    text="Generate Robux",
    width = 25,
    height = 1,
    bg = "green",
    fg = "white",
    command=game
)

label.pack()
entry.pack()
button.pack()
window.mainloop()
