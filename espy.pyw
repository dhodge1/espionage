#!/usr/bin/python

from tkinter import *
from tkinter import filedialog
from sys import argv

root=Tk()
root.geometry("335x160")
#root.geometry("415x205+100+100")
root.title("Basic File Encryption/Decrytion")

encKey = {
  	'a' : 'b',
		'b' : 'c',
		'c' : 'd',
		'd' : 'e',
		'e' : 'f',
		'f' : 'g',
		'g' : 'h',
		'h' : 'i',
		'i' : 'j',
		'j' : 'k',
		'k' : 'l',
		'l' : 'm',
		'm' : 'n',
		'n' : 'o',
		'o' : 'p',
		'p' : 'q',
		'q' : 'r',
		'r' : 's',
		's' : 't',
		't' : 'u',
		'u' : 'v',
		'v' : 'w',
		'w' : 'x',
		'x' : 'y',
		'y' : 'z',
		'z' : 'a',
		',' : '.',
		' ' : '@',
		'.' : ',',
		'!' : '?',
		'?' : '!',
		'@' : ' ',
		'"' : '*',
		'*' : '"',
		'\'' : '$',
		'$' : '\'',
		'(' : ')',
		')' : '(',
		'-' : '_',
		'_' : '-',
		'+' : '=',
		'=' : '+',
		'%' : '^',
		'^' : '%',
		'#' : '>',
		'>' : '#',
		'&' : '[',
		'[' : '&',
                '1' : '2',
                '2' : '3',
                '3' : '4',
                '4' : '5',
                '5' : '6',
                '6' : '7',
                '7' : '8',
                '8' : '9',
                '9' : '0',
                '0' : '1',
                ':' : '/',
                '/' : ';',
                ';' : ':'
	 }

decKey = dict(zip(encKey.values(), encKey.keys()))

def openFile():
        global f
        filename = filedialog.askopenfilename()
        f = open(filename)
        
#outfile = "encrypted_" + argv[1]
def saveFile():
        global fout
        outfile = filedialog.asksaveasfilename(defaultextension=".txt")
        fout = open(outfile, "w")

def encrypt():
        global f
        global fout
        global encKey
        for line in f:
                lineL = line.lower()
                words = lineL.split()
                j = 0
                for word in words:
                        letters = list(word)
                        i = 0
                        for letter in letters:
                                letters[i] =  encKey[letter]
                                i = i + 1
                        word = ''.join(letters)
                        words[j] = word
                        j = j + 1
                lineL = ' '.join(words)
                fout.write(lineL)

        fout.close()
        f.close()

def decrypt():
        global f
        global fout
        global decKey
        for line in f:
                lineL = line.lower()
                words = lineL.split()
                j = 0
                for word in words:
                        letters = list(word)
                        i = 0
                        for letter in letters:
                                letters[i] =  decKey[letter]
                                i = i + 1
                        word = ''.join(letters)
                        words[j] = word
                        j = j + 1
                lineL = ' '.join(words)
                fout.write(lineL)

        fout.close()
        f.close()

menubar = Menu(root)
fileMenu = Menu(menubar)
fileMenu.add_command(label = "Open", command=openFile)
fileMenu.add_command(label = "Save as", command=saveFile)
menubar.add_cascade(label="File", menu=fileMenu)
actionMenu = Menu(menubar)
actionMenu.add_command(label = "Encrypt", command=encrypt)
actionMenu.add_command(label = "Decrypt", command=decrypt)
menubar.add_cascade(label="Actions", menu=actionMenu)

#aLab = Label(root, text="").grid(row=0, column=0, sticky=E)
bLab = Label(root, text="").grid(row=1, column=0, sticky=E)
oLab = Label(root, text="   Step 1) Choose a file to open: ").grid(row=2, column=0, sticky=W)
cLab = Label(root, text="").grid(row=3, column=0, sticky=E)
sLab = Label(root, text="   Step 2) Choose name to save file as: ").grid(row=4, column=0, sticky=W)
dLab = Label(root, text="").grid(row=5, column=0, sticky=E)
runLab = Label(root, text="   Step 3) Run process ").grid(row=6, column=0, sticky=W)

openF = Button(root, text=" Open  ", command=openFile).grid(row=2, column=1)
saveF = Button(root, text="Save as", command=saveFile).grid(row=4, column=1)
encr = Button(root, text="Encrypt", command=encrypt).grid(row=6, column=1)
eLab = Label(root, text="").grid(row=6, column=2, sticky=E)
fLab = Label(root, text="").grid(row=6, column=3, sticky=E)
decr = Button(root, text="Decrypt", command=decrypt).grid(row=6, column=4)

root.configure(menu=menubar)
root.mainloop()
	 
