# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
import tkinter as ui
import plistlib
from _ctypes import Array
from tkinter.filedialog import askopenfilename
import keyword
#
# cryptKey = None
# message = None

global cryptKey
global message
processedMessage = []
# global listOfChars = []
listOfChars = [chr(ch) for ch in (range(ord('a'), ord('z')+1))]


def open_file():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    print("File: ")
    print(filepath)
    global message
    with open(filepath, "r") as input_file:
        text = input_file.read()
        message = text
        print(text)


def open_key():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    print("Key: ")
    print(filepath)
    global cryptKey
    with open(filepath, "r") as input_file:
        text = input_file.read()
        cryptKey = text
        print(text)

def cut_by_chars(text):
    for char in text:
        return char

def cut_by_blocks(key, text):
    # blocksArray[(len(text)/len(key))+1] = new Array()
    # for i in len(text):
    pass

def select_vernam_char(key, text, count):
    processedMessage
    if (text[count]).isalpha():
        if ord('z') >= ord(text[count].lower()) >= ord('a'):

            processedMessage + [text[count].lower()]
            print(processedMessage)
        else:
            return
    else:
        return


    # pass






def operate_and_save():


    global message
    # global processedMessage
    global cryptKey




    for i in range(len(message)):
        select_vernam_char(cryptKey, message, i)
    # if (object.isFileCryprted == False):
    #     print("False")
    # else:
    #     print("True")
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    print("File: ")
    print(filepath)


    with open(filepath, "w") as output_file:
        text = output_file.write()
        cryptKey = text
        print(text)

def event_handler(event):
    """Выводит символ, связанный с нажатой клавишей"""
    print(event.char)


class mainWindow:

    isFileSelected = False
    isKeySelected = False
    isFileCrypted = False

    window = ui.Tk()
    window.columnconfigure(5, weight=1, minsize=25, pad=10)
    window.rowconfigure([0, 5], weight=1, minsize=10, pad=10)
    lblKeyInfo = ui.Label(text="Put key here:")
    lblKeyInfo.grid(row=0, column=3)
    lblFileInfo = ui.Label(text="Put file here:")
    lblFileInfo.grid(row=1, column=3)

    btnKeySelect = ui.Button(text="Select Key", command=open_key)
    btnKeySelect.grid(row=0, column=4)
    btnFileSelect = ui.Button(text="Select File", command=open_file)
    btnFileSelect.grid(row=1, column=4)

    btnWtWeDo1 = ui.Radiobutton(text="Crypt", variable=isFileCrypted, value=True)
    btnWtWeDo1.grid(row=0, column=2)
    btnWtWeDo2 = ui.Radiobutton(text="Encrypt", variable=isFileCrypted, value=False)
    btnWtWeDo2.grid(row=1, column=2)

    btnDo = ui.Button(text="Complete", command=operate_and_save)
    btnDo.grid(row=2, column=3)




    # lblKeyInfo.pack()
    # lblFileInfo.pack()
    window.mainloop()

    # txt_edit.insert(ui.END, text)
    # window.title(f"Simple Text Editor - {filepath}")


if __name__ == '__main__':
    # global listOfChars
    # for i in (range(ord('a'), ord('z')+1)):
    #     listOfChars + [chr(i)]
    #     print(chr(i))
    print(len(listOfChars))
    vernamWindow = mainWindow()
    print(cryptKey, message)
    # window = ui.Tk()
    # window.mainloop()
