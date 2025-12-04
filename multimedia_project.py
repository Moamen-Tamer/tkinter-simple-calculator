import tkinter as tk
from PIL import Image, ImageTk

#Dark Mode Colors
darkBgColor = "#1e1e1e"
darkButtonColor = "#333333"
darkNumbersColor = "#f5f5f5"
darkClearColor = "#ff1a1a"
darkResultColor = "#ffe4c4"

#Light Mode Colors
lightBgColor = "#f5f5f5"        
lightButtonColor = "#dedeff"    
lightNumbersColor = "#000000"   
lightClearColor = "#ff0000"  
lightResultColor = "#4d2600"    

#Fonts
buttonFont = ("Helvetica", 12)
screenFont = "jetbrains"

#Window Intialization
root = tk.Tk()
root.title("Calculator")
root.geometry("320x480")
root.config(bg = darkBgColor)

#Variables
screenText = tk.StringVar(value = "")
operators = ["+", "-", "×", "÷"]
currentTheme = "dark"

#Icons
lightModeImg = Image.open("./light.png")
lightModeImg = lightModeImg.resize((32, 32))
lightMode = ImageTk.PhotoImage(lightModeImg)

darkModeImg = Image.open("./dark.png")
darkModeImg = darkModeImg.resize((32, 32))
darkMode = ImageTk.PhotoImage(darkModeImg)

#Helper Methods
def click(choice):
    current = screenText.get()

    if (current == "0"):
        current = ""

    screenText.set(current + choice)

def clear():
    screenText.set("")

def byHundred():
    current = float(screenText.get())
    screenText.set(str(current / 100))

def backSpace():
    current = screenText.get()

    if current == "":
        return
    
    screenText.set(current[:-1])

def add(pre, post):
    return pre + post

def subtract(pre, post):
    return pre - post

def multiply(pre, post):
    return pre * post

def divide(pre, post):
    return pre / post

def calculate():
    current = screenText.get()

    if current == "" or len(current) == 1:
        return
    
    preOperator = ""
    operator = ""
    postOperator = ""
    operatorFound = False
    
    for val in current:
        if val in operators and operatorFound == False and preOperator != "":
            operator = val
            operatorFound = True
        else:
            if operatorFound == False:
                preOperator += val
            else:
                postOperator += val 

    preOperator = float(preOperator)
    postOperator = float(postOperator)

    match operator:
        case "+":
            current = add(preOperator, postOperator)
        case "-":
            current = subtract(preOperator, postOperator)
        case "×":
            current = multiply(preOperator, postOperator)
        case "÷":
            current = divide(preOperator, postOperator)

    screenText.set(current)

def themeConverter():
    global currentTheme

    if currentTheme == "dark":
        root.config(bg = lightBgColor)
        container.config(bg = lightBgColor)
        screen.config(fg = lightResultColor, bg = lightBgColor)
        buttonTheme.config(bg = lightButtonColor, image = darkMode)
        buttonAC.config(fg = lightClearColor, bg = lightButtonColor)
        buttonPercent.config(fg = lightNumbersColor, bg = lightButtonColor)
        buttonRemove.config(fg = lightClearColor, bg = lightButtonColor)
        buttonDivide.config(fg = lightNumbersColor, bg = lightButtonColor)
        buttonSeven.config(fg = lightNumbersColor, bg = lightButtonColor)
        buttonEight.config(fg = lightNumbersColor, bg = lightButtonColor)
        buttonNine.config(fg = lightNumbersColor, bg = lightButtonColor)
        buttonMultiply.config(fg = lightNumbersColor, bg = lightButtonColor)
        buttonFour.config(fg = lightNumbersColor, bg = lightButtonColor)
        buttonFive.config(fg = lightNumbersColor, bg = lightButtonColor)
        buttonSix.config(fg = lightNumbersColor, bg = lightButtonColor)
        buttonMinus.config(fg = lightNumbersColor, bg = lightButtonColor)
        buttonOne.config(fg = lightNumbersColor, bg = lightButtonColor)
        buttonTwo.config(fg = lightNumbersColor, bg = lightButtonColor)
        buttonThree.config(fg = lightNumbersColor, bg = lightButtonColor)
        buttonPlus.config(fg = lightNumbersColor, bg = lightButtonColor)
        buttonTwoZeros.config(fg = lightNumbersColor, bg = lightButtonColor)
        buttonZero.config(fg = lightNumbersColor, bg = lightButtonColor)
        buttonPoint.config(fg = lightNumbersColor, bg = lightButtonColor)
        buttonEqual.config(fg = lightResultColor, bg = lightButtonColor)

        currentTheme = "light"
    elif currentTheme == "light":
        root.config(bg = darkBgColor)
        container.config(bg = darkBgColor)
        screen.config(fg = darkResultColor, bg = darkBgColor)
        buttonTheme.config(bg = darkBgColor, image = lightMode)
        buttonAC.config(fg = darkClearColor, bg = darkBgColor)
        buttonPercent.config(fg = darkNumbersColor, bg = darkBgColor)
        buttonRemove.config(fg = darkClearColor, bg = darkBgColor)
        buttonDivide.config(fg = darkNumbersColor, bg = darkBgColor)
        buttonSeven.config(fg = darkNumbersColor, bg = darkBgColor)
        buttonEight.config(fg = darkNumbersColor, bg = darkBgColor)
        buttonNine.config(fg = darkNumbersColor, bg = darkBgColor)
        buttonMultiply.config(fg = darkNumbersColor, bg = darkBgColor)
        buttonFour.config(fg = darkNumbersColor, bg = darkBgColor)
        buttonFive.config(fg = darkNumbersColor, bg = darkBgColor)
        buttonSix.config(fg = darkNumbersColor, bg = darkBgColor)
        buttonMinus.config(fg = darkNumbersColor, bg = darkBgColor)
        buttonOne.config(fg = darkNumbersColor, bg = darkBgColor)
        buttonTwo.config(fg = darkNumbersColor, bg = darkBgColor)
        buttonThree.config(fg = darkNumbersColor, bg = darkBgColor)
        buttonPlus.config(fg = darkNumbersColor, bg = darkBgColor)
        buttonTwoZeros.config(fg = darkNumbersColor, bg = darkBgColor)
        buttonZero.config(fg = darkNumbersColor, bg = darkBgColor)
        buttonPoint.config(fg = darkNumbersColor, bg = darkBgColor)
        buttonEqual.config(fg = darkResultColor, bg = darkBgColor)

        currentTheme = "dark"

#Frame
container = tk.Frame(root, bg = darkBgColor)
container.pack(expand = True)

#Screen Displayer
screen = tk.Label(container, textvariable = screenText, font = screenFont, fg = darkResultColor, bg = darkBgColor, width = 10, anchor = "e")
screen.grid(row = 0, column = 1, columnspan = 3, sticky = "nsew",padx = 15, pady = 27)

#Theme Modification Button
buttonTheme = tk.Button(container, image = lightMode, bg = darkButtonColor, width = 5, height = 2, command = themeConverter)
buttonTheme.grid(row = 0, column = 0, sticky = "nsew", padx = 15, pady = 20)

# First Row Buttons
buttonAC = tk.Button(container, text = "AC", fg = darkClearColor, font = buttonFont, bg = darkButtonColor, width = 5, height = 2, command = clear)
buttonAC.grid(row = 1, column = 0, sticky = "nsew", padx = 13, pady = 14.5)

buttonPercent = tk.Button(container, text = "%", fg = darkNumbersColor, font = buttonFont, bg = darkButtonColor, width = 5, height = 2, command = byHundred)
buttonPercent.grid(row = 1, column = 1, sticky = "nsew", padx = 13, pady = 14.5)

buttonRemove = tk.Button(container, text = "↵", fg = darkClearColor, font = buttonFont, bg = darkButtonColor, width = 5, height = 2, command = backSpace)
buttonRemove.grid(row = 1, column = 2, sticky = "nsew", padx = 13, pady = 14.5)

buttonDivide = tk.Button(container, text = "÷", fg = darkNumbersColor, font = buttonFont, bg = darkButtonColor, width = 5, height = 2, command = lambda: click("÷"))
buttonDivide.grid(row = 1, column = 3, sticky = "nsew", padx = 13, pady = 14.5)

#Second Row Buttons
buttonSeven = tk.Button(container, text = "7", fg = darkNumbersColor, font = buttonFont, bg = darkButtonColor, width = 5, height = 2, command = lambda: click("7"))
buttonSeven.grid(row = 2, column = 0, sticky = "nsew", padx = 13, pady = 14.5)

buttonEight = tk.Button(container, text = "8", fg = darkNumbersColor, font = buttonFont, bg = darkButtonColor, width = 5, height = 2, command = lambda: click("8"))
buttonEight.grid(row = 2, column = 1, sticky = "nsew", padx = 13, pady = 14.5)

buttonNine = tk.Button(container, text = "9", fg = darkNumbersColor, font = buttonFont, bg = darkButtonColor, width = 5, height = 2, command = lambda: click("9"))
buttonNine.grid(row = 2, column = 2, sticky = "nsew", padx = 13, pady = 14.5)

buttonMultiply = tk.Button(container, text = "×", fg = darkNumbersColor, font = buttonFont, bg = darkButtonColor, width = 5, height = 2, command = lambda: click("×"))
buttonMultiply.grid(row = 2, column = 3, sticky = "nsew", padx = 13, pady = 14.5)

#Third Row Buttons
buttonFour = tk.Button(container, text = "4", fg = darkNumbersColor, font = buttonFont, bg = darkButtonColor, width = 5, height = 2, command = lambda: click("4"))
buttonFour.grid(row = 3, column = 0, sticky = "nsew", padx = 13, pady = 14.5)

buttonFive = tk.Button(container, text = "5", fg = darkNumbersColor, font = buttonFont, bg = darkButtonColor, width = 5, height = 2, command = lambda: click("5"))
buttonFive.grid(row = 3, column = 1, sticky = "nsew", padx = 13, pady = 14.5)

buttonSix = tk.Button(container, text = "6", fg = darkNumbersColor, font = buttonFont, bg = darkButtonColor, width = 5, height = 2, command = lambda: click("6"))
buttonSix.grid(row = 3, column = 2, sticky = "nsew", padx = 13, pady = 14.5)

buttonMinus = tk.Button(container, text = "-", fg = darkNumbersColor, font = buttonFont, bg = darkButtonColor, width = 5, height = 2, command = lambda: click("-"))
buttonMinus.grid(row = 3, column = 3, sticky = "nsew", padx = 13, pady = 14.5)

#Fourth Row Buttons
buttonOne = tk.Button(container, text = "1", fg = darkNumbersColor, font = buttonFont, bg = darkButtonColor, width = 5, height = 2, command = lambda: click("1"))
buttonOne.grid(row = 4, column = 0, sticky = "nsew", padx = 13, pady = 14.5)

buttonTwo = tk.Button(container, text = "2", fg = darkNumbersColor, font = buttonFont, bg = darkButtonColor, width = 5, height = 2, command = lambda: click("2"))
buttonTwo.grid(row = 4, column = 1, sticky = "nsew", padx = 13, pady = 14.5)

buttonThree = tk.Button(container, text = "3", fg = darkNumbersColor, font = buttonFont, bg = darkButtonColor, width = 5, height = 2, command = lambda: click("3"))
buttonThree.grid(row = 4, column = 2, sticky = "nsew", padx = 13, pady = 14.5)

buttonPlus = tk.Button(container, text = "+", fg = darkNumbersColor, font = buttonFont, bg = darkButtonColor, width = 5, height = 2, command = lambda: click("+"))
buttonPlus.grid(row = 4, column = 3, sticky = "nsew", padx = 13, pady = 14.5)

#Fifth Row Buttons
buttonTwoZeros = tk.Button(container, text = "00", fg = darkNumbersColor, font = buttonFont, bg = darkButtonColor, width = 5, height = 2, command = lambda: click("00"))
buttonTwoZeros.grid(row = 5, column = 0, sticky = "nsew", padx = 13, pady = 14.5)

buttonZero = tk.Button(container, text = "0", fg = darkNumbersColor, font = buttonFont, bg = darkButtonColor, width = 5, height = 2, command = lambda: click("0"))
buttonZero.grid(row = 5, column = 1, sticky = "nsew", padx = 13, pady = 14.5)

buttonPoint = tk.Button(container, text = ".", fg = darkNumbersColor, font = buttonFont, bg = darkButtonColor, width = 5, height = 2, command = lambda: click("."))
buttonPoint.grid(row = 5, column = 2, sticky = "nsew", padx = 13, pady = 14.5)

buttonEqual = tk.Button(container, text = "=", fg = darkResultColor, font = buttonFont, bg = darkButtonColor, width = 5, height = 2, command = calculate)
buttonEqual.grid(row = 5, column = 3, sticky = "nsew", padx = 13, pady = 14.5)

#Run
root.mainloop()