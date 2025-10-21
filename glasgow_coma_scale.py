'''
This is a programm designed to evaluate the impaired consciousness in patients after brain injuries.
The model on which this application is based is called the glasgow coma scale.

Author: Florian Becker
Date: 2025-10-21
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
        diaLabel1.set("Your patient has severe brain injuries!")
    elif score >= 9 and score <= 12:
        diaLabel1.set("Your patient has moderate brain injuries!")
    elif score >= 13 and score <= 15:
        diaLabel1.set("Your patient has minor brain injuries!")
    else:
        diaLabel1.set("Please start/restart your input!")

    
    
    
# ==== GUI ====
root = tk.Tk()
root.geometry("650x1200")
root.title("===== Glasgow Coma Scale (GCS) =====")

diaPoints = tk.IntVar()
diaLabel1 = tk.StringVar()


labelOcular = tk.StringVar()
labelOcular.set("Ocular response: Please choose from the following options:")
ocularLabel = tk.Label(root, textvariable=labelOcular, font=("Arial", 14, "underline"))
ocularLabel.pack(pady=20)

ocularButton_1 = ttk.Button(root, text="Not testable (severe trauma to the eyes.)", command=lambda: ocular_response(0))
ocularButton_1.pack()

ocularButton_2 = ttk.Button(root, text="Does not open eyes", command=lambda: ocular_response(1))
ocularButton_2.pack()

ocularButton_3 = ttk.Button(root, text="Opens eyes in response to pain", command=lambda: ocular_response(2))
ocularButton_3.pack()

ocularButton_4 = ttk.Button(root, text="Opens eyes in response to voice", command=lambda: ocular_response(3))
ocularButton_4.pack()

ocularButton_5 = ttk.Button(root, text="Opens eyes spontaneously", command=lambda: ocular_response(4))
ocularButton_5.pack()


labelVerbal = tk.StringVar()
labelVerbal.set("Verbal response: Please choose from the following options:")
verbalLabel = tk.Label(root, textvariable=labelVerbal, font=("Arial", 14, "underline"))
verbalLabel.pack(pady=20)

verbalButton_1 = ttk.Button(root, text="Not testable (Intubation, non-oral language disability, linguistic barrier)", command=lambda: verbal_response(0))
verbalButton_1.pack()

verbalButton_2 = ttk.Button(root, text="Makes no sounds", command=lambda: verbal_response(1))
verbalButton_2.pack()

verbalButton_3 = ttk.Button(root, text="Incomprehensible sounds", command=lambda: verbal_response(2))
verbalButton_3.pack()

verbalButton_4 = ttk.Button(root, text="Inappropriate words", command=lambda: verbal_response(3))
verbalButton_4.pack()

verbalButton_5 = ttk.Button(root, text="Confused and disoriented, but able to answer questions", command=lambda: verbal_response(4))
verbalButton_5.pack()

verbalButton_6 = ttk.Button(root, text="Oriented to time, person, and place, converses normally", command=lambda: verbal_response(5))
verbalButton_6.pack()


labelMotoric = tk.StringVar()
labelMotoric.set("Motoric response: Please choose from the following options:")
motoricLabel = tk.Label(root, textvariable=labelMotoric, font=("Arial", 14, "underline"))
motoricLabel.pack(pady=20)

motoricButton_1 = ttk.Button(root, text="Not testable (acquired causes such as post-stroke, post-neurological injury; congenital/innate such as cerebral palsy)", command=lambda: motoric_response(0))
motoricButton_1.pack()

motoricButton_2 = ttk.Button(root, text="Makes no movements", command=lambda: motoric_response(1))
motoricButton_2.pack()

motoricButton_3 = ttk.Button(root, text="Abnormal extension", command=lambda: motoric_response(2))
motoricButton_3.pack()

motoricButton_4 = ttk.Button(root, text="Abnormal flexion", command=lambda: motoric_response(3))
motoricButton_4.pack()

motoricButton_5 = ttk.Button(root, text="Flexion/ Withdrawal from painful stimuli", command=lambda: motoric_response(4))
motoricButton_5.pack()

motoricButton_6 = ttk.Button(root, text="Moves to localise pain", command=lambda: motoric_response(5))
motoricButton_6.pack()

motoricButton_7 = ttk.Button(root, text="Obeys commands", command=lambda: motoric_response(6))
motoricButton_7.pack()


pointsDisplay = tk.Label(root, textvariable=diaPoints, font=("Arial", 16))
pointsDisplay.pack(pady=20)

diaLabel2 = tk.Label(root, textvariable=diaLabel1, font=("Arial", 14, "bold"))
diaLabel2.pack(pady=20)


diagnosis()

buttonExit = ttk.Button(root, text="Exit", command=root.destroy)
buttonExit.pack(pady=20)

root.mainloop()


