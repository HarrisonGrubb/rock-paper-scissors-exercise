import tkinter
import tkinter.messagebox

from game import *


window = tkinter.Tk()
window.title(GUI_WINDOW_TITLE)

my_message = tkinter.Message(text= WELCOME_MESSAGE, width = 2000)

my_select_label = tkinter.Label(text = GUI_PROMPT_MESSAGE)
my_select = tkinter.Listbox()
my_select.insert(1, "rock")
my_select.insert(2, 'paper')
my_select.insert(3, 'scissors')
my_select.insert(4, 'lizard spock')

