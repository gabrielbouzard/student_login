from Tkinter import *
import Tkinter as tk
import tkMessageBox
import urllib2
import re

try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
import webbrowser

def get_classes():
    header = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}
    # TODO: change to point to .txt file on Dropbox, Netlabs website, or somewhere else easily accessible to lab manager
    url = "https://textuploader.com/dvtg0"
    request = urllib2.Request(url, "", header)
    request.get_method = lambda: 'GET'
    response = urllib2.urlopen(request);
    # TODO: this parses HTML because the classlist is hosted on a free site that embeds the list in HTML, but if you serve a straight .txt file you will just need something like 'return response.splitlines()'
    parsed_html = BeautifulSoup(response, features="html.parser")
    return parsed_html.find("code", attrs={"class":"no-highlight"}).get_text().encode("ascii").splitlines()

def get_option(value):
    return value

def raise_above_all(window):
    window.lift()
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)

def popup_error():
    win2 = tk.Toplevel()
    raise_above_all(win2)
    win2.wm_title("You forgot something stupid!")

    l = tk.Label(win2, text="Enter name and class to continue...")
    l.pack(pady=(20,0), padx=(20,20))

    b = tk.Button(win2, text="Close", command=win2.destroy)
    b.pack(pady=(20,20))

def callback():
    if (len(entry.get()) == 0 or str(entry.get()) == "DePaul Username: " or str(get_option) == "------"):
        popup_error()
    else:
        # TODO: comment out the next line and enter DB commands here...
        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ', new=2)


win = Tk()
# win.overrideredirect(True)
win.attributes("-topmost", False)
win.resizable(width=False, height=False)
win.minsize(width=400, height=180)

window_width = 400
window_height = 180
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))


# TODO: change the window title...
win.wm_title("Salmanader is a clown!")

entry = Entry(win, state=tk.NORMAL)
entry.insert(0, "DePaul Username: ")
entry.pack(pady=(15,15))

var = StringVar(win)
var.set("------")
classes = get_classes()

options = tk.OptionMenu(win, var, *classes, command=get_option)
options.pack(pady=(0,15))

button = Button(win, text="Click Me", command=callback)
button.pack(pady=15)

mainloop()
