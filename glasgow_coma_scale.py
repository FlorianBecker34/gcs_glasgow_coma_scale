'''
This is a programm designed to evaluate the impaired consciousness in patients after brain injuries.
The model on which this application is based is called the glasgow coma scale.

Author: Florian Becker
Date: 2025-10-17
'''
import tkinter as tk
from tkinter import ttk

diaPoints = 0

def ocular_response(o_choice):
    global diaPoints
    if o_choice == 0:
        diaPoints += 0
    if o_choice == 1:
        diaPoints += 1
    if o_choice == 2:
        diaPoints +=2
    if o_choice == 3: 
        diaPoints += 3
    if o_choice == 4:
        diaPoints += 4


    return diaPoints
        

def verbal_response(v_choice):
    global diaPoints
    if v_choice == 0:
        diaPoints += 0
    if v_choice == 1:
        diaPoints += 1
    if v_choice == 2:
        diaPoints += 2
    if v_choice == 3:
        diaPoints += 3
    if v_choice == 4:
        diaPoints += 4
    if v_choice == 5:
        diaPoints += 5

    return diaPoints    


def motoric_response(m_choice):
    global diaPoints
    if m_choice == 0:
        diaPoints += 0
    if m_choice == 1:
        diaPoints += 1
    if m_choice == 2:
        diaPoints += 2
    if m_choice == 3:
        diaPoints += 3
    if m_choice == 4:
        diaPoints += 4
    if m_choice == 5:
        diaPoints += 5
    if m_choice == 6:
        diaPoints += 6

    return diaPoints


def diagnosis():
    if diaPoints <= 8:
        diaLabel1.set("Your patient has severe brain injuries!")
    if diaPoints >= 9:
        diaLabel1.set("Your patient has moderate brain injuries!")
    if diaPoints >= 13:
        diaLabel1.set("Your patient has minor brain injuries!")
    




root = tk.Tk()
root.geometry("200x400")
#root.resizable(width=False, height=False)
root.title("===== Glasgow Coma Scale (GCS) =====")


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


diaLabel1 = tk.StringVar()
diaLabel2 = tk.Label(root, textvariable=diaLabel1, font=("Arial", 14, "bold"))
diaLabel2.pack(pady=20)
diagnosis()

buttonExit = ttk.Button(root, text="Exit", command=root.destroy)
buttonExit.pack(pady=20)




root.mainloop()



# print("====== Glasgow Coma Scale (GCS) ======")
# print("Ocular response: Please choose from the following options:")
# print("0 = Not testable (severe trauma to the eyes)")
# print("1 = Does not open eyes")
# print("2 = Opens eyes in response to pain")
# print("3 = Opens eyes in response to voice")
# print("4 = Opens eyes spontaneously")

# ocular_response = int(input("Enter your choice:"))

# print("Verbal response: Please choose from the following options:")
# print("0 = Not testable (Intubation, non-oral language disability, linguistic barrier)")
# print("1 = Makes no sounds")
# print("2 = Incomprehensible sounds")
# print("3 = Inappropriate words")
# print("4 = Confused and disoriented, but able to answer questions")
# print("5 = Oriented to time, person, and place, converses normally")

# verbal_response = int(input("Enter your choice: "))

# print("motoric response: Please choose from the following options:")
# print("0 = Not testable (acquired causes such as post-stroke, post-neurological injury; congenital/innate such as cerebral palsy)")
# print("1 = Makes no movements")
# print("2 = Abnormal extension")
# print("3 = Abnormal flexion")
# print("4 = Flexion/ Withdrawal from painful stimuli")
# print("5 = Moves to localise pain")
# print("6 = Obeys commands")

# motoric_response = int(input("Enter your choice: "))

# points_sum = ocular_response + verbal_response + motoric_response

# if points_sum <= 8:
#     diagnosis = "severe brain injuries"
# elif points_sum >= 9 and points_sum <= 12:
#     diagnosis = "moderate brain injuries"
# elif points_sum >= 13:
#     diagnosis = "minor brain injuries"

# print(f"Your patient has {diagnosis}.")
# print("====== Application closed ======")


