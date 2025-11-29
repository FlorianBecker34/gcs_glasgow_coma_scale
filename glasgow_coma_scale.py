'''
This is a programm designed to evaluate the impaired consciousness in patients after brain injuries.
The model on which this application is based is called the glasgow coma scale.

Author: Florian Becker
Date: 2025-11-29
'''
import tkinter as tk
from tkinter import ttk


sumScore = 0
ocularPoints = 0
verbalPoints = 0
motoricPoints = 0

def ocular_response(o_choice):
    global ocularPoints
    ocularPoints = o_choice
    dia_score()

    
def verbal_response(v_choice):
    global verbalPoints
    verbalPoints = v_choice
    dia_score()
        

def motoric_response(m_choice):
    global motoricPoints
    motoricPoints = m_choice
    dia_score()


def dia_score():
    global sumScore
    sumScore = ocularPoints + verbalPoints + motoricPoints
    diaPoints.set(sumScore)
    diagnosis()


def diagnosis():
    score = diaPoints.get()

    if score >= 3 and score <= 8:
        diaLabel1.set("Your patient has a severe traumatic brain injury / impaired consciousness.")
    elif score >= 9 and score <= 12:
        diaLabel1.set("Your patient has a moderate traumatic brain injury / impaired consciousness.")
    elif score >= 13 and score <= 15:
        diaLabel1.set("Your patient has a mild traumatic brain injury / impaired consciousness")
    else:
        diaLabel1.set("Please repeat your entry!")

    
    
    
# ==== GUI ====
root = tk.Tk()
root.geometry("800x1200")
root.maxsize(width="800", height="1200")
root.title("===== Glasgow Coma Scale (GCS) =====")

diaPoints = tk.IntVar()
diaLabel1 = tk.StringVar()


labelOcular = tk.StringVar()
labelOcular.set("Ocular response: Please choose from following options:")
ocularLabel = tk.Label(root, textvariable=labelOcular, font=("Arial", 14, "underline"))
ocularLabel.pack(pady=15)


ocularButton_1 = ttk.Button(root, text="No response / Not testable", command=lambda: ocular_response(1))
ocularButton_1.pack(fill="x")

ocularButton_2 = ttk.Button(root, text="Opens eyes in response to pain", command=lambda: ocular_response(2))
ocularButton_2.pack(fill="x")

ocularButton_3 = ttk.Button(root, text="Opens eyes in response to voice", command=lambda: ocular_response(3))
ocularButton_3.pack(fill="x")

ocularButton_4 = ttk.Button(root, text="Opens eyes spontaneously", command=lambda: ocular_response(4))
ocularButton_4.pack(fill="x")


labelVerbal = tk.StringVar()
labelVerbal.set("Verbal response: Please choose from the following options:")
verbalLabel = tk.Label(root, textvariable=labelVerbal, font=("Arial", 14, "underline"))
verbalLabel.pack(pady=15)


verbalButton_1 = ttk.Button(root, text="No response / Not testable", command=lambda: verbal_response(1))
verbalButton_1.pack(fill="x")

verbalButton_2 = ttk.Button(root, text="Incomprehensible sounds", command=lambda: verbal_response(2))
verbalButton_2.pack(fill="x")

verbalButton_3 = ttk.Button(root, text="Inappropriate words", command=lambda: verbal_response(3))
verbalButton_3.pack(fill="x")

verbalButton_4 = ttk.Button(root, text="Confused and disoriented, but able to answer questions", command=lambda: verbal_response(4))
verbalButton_4.pack(fill="x")

verbalButton_5 = ttk.Button(root, text="Oriented to time, person, and place, converses normally", command=lambda: verbal_response(5))
verbalButton_5.pack(fill="x")


labelMotoric = tk.StringVar()
labelMotoric.set("Motoric response: Please choose from the following options:")
motoricLabel = tk.Label(root, textvariable=labelMotoric, font=("Arial", 14, "underline"))
motoricLabel.pack(pady=20)


motoricButton_1 = ttk.Button(root, text="No response / Not testable", command=lambda: motoric_response(1))
motoricButton_1.pack(fill="x")

motoricButton_2 = ttk.Button(root, text="Stretching synergies", command=lambda: motoric_response(2))
motoricButton_2.pack(fill="x")

motoricButton_3 = ttk.Button(root, text="Flexion synergies", command=lambda: motoric_response(3))
motoricButton_3.pack(fill="x")

motoricButton_4 = ttk.Button(root, text="Indiscriminate defensive movements", command=lambda: motoric_response(4))
motoricButton_4.pack(fill="x")

motoricButton_5 = ttk.Button(root, text="Targeted defensive movements", command=lambda: motoric_response(5))
motoricButton_5.pack(fill="x")

motoricButton_6 = ttk.Button(root, text="Follows requests", command=lambda: motoric_response(6))
motoricButton_6.pack(fill="x")


pointsDisplay = tk.Label(root, textvariable=diaPoints, font=("Arial", 16))
pointsDisplay.pack(pady=15)

diaLabel2 = tk.Label(root, textvariable=diaLabel1, font=("Arial", 14, "bold"))
diaLabel2.pack(pady=25)


diagnosis()

buttonExit = ttk.Button(root, text="Exit", command=root.destroy)
buttonExit.pack()

root.mainloop()