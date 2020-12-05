import math
import tkinter as ui
import plistlib
from _ctypes import Array
from tkinter.filedialog import askopenfilename, asksaveasfilename
import keyword

# There are variables of key and message.
global cryptKey
global message

crypted = True

# processedMessage = [] # Unused in final list
# Resulting message variable
returningMessage = ""
listOfChars = [chr(ch) for ch in (range(ord('a'), ord('z') + 1))]


def open_file():
    # Open file
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    print("File: ")
    print(filepath)
    # Putting a message from file to global variable
    global message
    with open(filepath, "r") as input_file:
        text = input_file.read()
        message = text
        print(text)


def open_key():
    # Open file
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    print("Key: ")
    print(filepath)
    # Putting a key from file to global variable
    global cryptKey
    with open(filepath, "r") as input_file:
        text = input_file.read()
        cryptKey = text
        print(text)


def cut_by_chars(text):
    for char in text:
        return char


def cut_by_blocks(key, text):
    pass


def select_vernam_char(key, text, count):
    # Set current char to variable
    processedChar = text[count].lower()

    # Linking to global variable
    global returningMessage

    # Checking char, is it alpha?
    if (text[count]).isalpha():
        if ord('z') >= ord(text[count].lower()) >= ord('a'):
            # Encrypted char = (crypted char + char of key) % size of [a..z] list
            processedChar = chr((((ord(processedChar) - 97) + (ord(key[count % len(key)]) - 97)) % 26) + 97)
            returningMessage = returningMessage + processedChar
            print(
                text[count].lower(), ord(text[count].lower()) - 97, " ",
                key[count % len(key)], ord(key[count % len(key)]) - 97, " ",
                processedChar, ord(processedChar) - 97, " ",
                count
            )
        else:
            returningMessage = returningMessage + processedChar
            return
    else:
        returningMessage = returningMessage + processedChar
        return


def select_vernam_char_inv(key, text, count):
    # Set current char to variable
    processedChar = text[count].lower()

    # Linking to global variable
    global returningMessage

    # Checking char, is it alpha?
    if (text[count]).isalpha():
        # Is alpha contained in [a..z] list? checking by ASCII codes
        if ord('z') >= ord(text[count].lower()) >= ord('a'):
            print((ord(key[count % len(key)]) - 97) % 26)

            # Encrypted char = (crypted char - char of key) % size of [a..z] list
            processedChar = chr((((ord(processedChar) - 97) - (ord(key[count % len(key)]) - 97)) % 26) + 97)
            returningMessage = returningMessage + processedChar
            print(
                text[count].lower(), ord(text[count].lower()) - 97, " ",
                key[count % len(key)], ord(key[count % len(key)]) - 97, " ",
                processedChar, ord(processedChar) - 97, " ",
                count
            )
        else:
            returningMessage = returningMessage + processedChar
            return
    else:
        returningMessage = returningMessage + processedChar
        return


def operate_and_save():
    global message
    global cryptKey

    # Now check, what should programm do
    if (crypted == False):
        # Here we're crypting message
        for i in range(len(message)):
            select_vernam_char(cryptKey, message, i)
    else:
        # Here we're performing invertion operations
        for i in range(len(message)):
            select_vernam_char_inv(cryptKey, message, i)

    # Create new file
    filepath = asksaveasfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    print("File: ")
    print(filepath)

    # Put our performed message in a file
    with open(filepath, "w") as output_file:
        global returningMessage
        output_file.write(returningMessage)
        print(returningMessage)

    # Now we should clear to not create duplication messages
    returningMessage = ""


def showClickedBTWD1():
    # It sets variable to False
    global crypted
    crypted = False
    print("We're going to crypt file.")
    return


def showClickedBTWD2():
    # It sets variable to True
    global crypted
    crypted = True
    print("We're going to encrypt file.")
    return


class mainWindow:
    # Low skills in Python don't let me use this vars.
    # It's unused block now.
    isFileSelected = False
    isKeySelected = False
    isFileCrypted = False

    # This block creates the window by methods of classes in Tkinter library.

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

    # Here we are select our method of performing message.
    # showClickedBTWDX are methods to operate on a global variable "crypted".

    btnWtWeDo1 = ui.Radiobutton(text="Crypt", variable=isFileCrypted, value=True, command=showClickedBTWD1)
    btnWtWeDo1.grid(row=0, column=2)
    btnWtWeDo2 = ui.Radiobutton(text="Encrypt", variable=isFileCrypted, value=False, command=showClickedBTWD2)
    btnWtWeDo2.grid(row=1, column=2)

    # Final button calculates our message by operate_and_save method, which is declared over this class.

    btnDo = ui.Button(text="Complete", command=operate_and_save)
    btnDo.grid(row=2, column=3)

    # lblKeyInfo.pack()
    # lblFileInfo.pack()
    window.mainloop()


if __name__ == '__main__':
    # Create an object vernamWindow by class mainWindow
    # which is declared upper lines.
    vernamWindow = mainWindow()
    print(cryptKey, message)
