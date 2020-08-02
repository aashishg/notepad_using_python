# Please read README.md before starting to code and running the project

# We are making notepad using tkinter and default python OS libraries
# So we start by importing tkinter and OS libraries
import tkinter  
import os  
from tkinter import *
  
# In tkinter we have a messagebox which we will use to make editing space, that is where user
# will write text, we import that
from tkinter.messagebox import *
  
# We also have a dialogbox called filedialog which we can use for showing messages so we import that too
from tkinter.filedialog import *

# Next we add W+E+N+S to text area means that the widget should be expanded in both directions.
self.__thisTextArea.grid(sticky = N + E + S + W) 
  
# We add new file creating functionality and name it as "New" as command in the "File" option in the menu
self.__thisFileMenu.add_command(label = "New", 
                                command = self.__newFile) 
  
# We add file opening functionality and name it as "Open" as command in the "File" option in the menu
self.__thisFileMenu.add_command(label = "Open", 
                                command = self.__openFile) 
  
# We add file saving functionality and name it as "Save" as command in the "File" option in the menu
self.__thisFileMenu.add_command(label = "Save", 
                                command = self.__saveFile) 
  
# Adding a separator in the menu so we can differentiate sub option in the "File" option in the menu
self.__thisFileMenu.add_separator() 
  
# We add "Exit" functionality with same name("Exit") as command in the "File" option in the menu
self.__thisFileMenu.add_command(label = "Exit", 
                                command = self.__quitApplication) 
# Adding the "File" option that we just made as cascade to the the menu bar
self.__thisMenuBar.add_cascade(label = "File", 
                               menu = self.__thisFileMenu) 
  
# Next up, we make an edit option in the menu and add a command
self.__thisEditMenu.add_command(label = "Cut", 
                                command = self.__cut) 
  
# We will add a "Copy" command in edit menu option
self.__thisEditMenu.add_command(label = "Copy", 
                                command = self.__copy) 
  
# We will add a "Paste" command in edit menu option
self.__thisEditMenu.add_command(label = "Paste", 
                                command = self.__paste) 
  
# Same as we did for "File" option we will add "Edit" option in the menu bar as cascaded option
self.__thisMenuBar.add_cascade(label = "Edit", 
                               menu = self.__thisEditMenu) 
  
# We will add a new "Help" option in the menu and add "About Notepad" command in that option
self.__thisHelpMenu.add_command(label = "About Notepad", 
                                command = self.__showAbout) 
# Adding "Help" option as cascaded in the menu bar
self.__thisMenuBar.add_cascade(label = "Help", 
                               menu = self.__thisHelpMenu) 
# Adding Menu Bar in the root config
self.__root.config(menu = self.__thisMenuBar) 

# Adding scroll bar on the right side
self.__thisScrollBar.pack(side = RIGHT, fill = Y) 
  
# Scrollbar will adjust automatically 
# according to the content in the text area
self.__thisScrollBar.config(command = self.__thisTextArea.yview) 
self.__thisTextArea.config(yscrollcommand = self.__thisScrollBar.set) 
