'''
This is a programm designed to evaluate the impaired consciousness in patients after brain injuries.
The model on which this application is based is called the glasgow coma scale.

Author: Florian Becker
Date: 2025-10-22
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
        diaLabel1.set("Ihr Patient hat ein(e) schwere(s) Schädelhirntrauma / Bewusstseinsstörung.")
    elif score >= 9 and score <= 12:
        diaLabel1.set("Ihr Patient hat ein(e) mittelschwere(s) Schädelhirntrauma / Bewusstseinsstörung.")
    elif score >= 13 and score <= 15:
        diaLabel1.set("Ihr Patient hat ein(e) leichte(s) Schädelhirntrauma / Bewusstseinsstörung")
    else:
        diaLabel1.set("Bitte wiederholen Sie Ihre Eingabe!")

    
    
    
# ==== GUI ====
root = tk.Tk()
root.geometry("800x1200")
root.maxsize(width="800", height="1200")
root.title("===== Glasgow Coma Scale (GCS) =====")

diaPoints = tk.IntVar()
diaLabel1 = tk.StringVar()


labelOcular = tk.StringVar()
labelOcular.set("Augenreaktion: Bitte wählen Sie aus den folgenden Optionen:")
ocularLabel = tk.Label(root, textvariable=labelOcular, font=("Arial", 14, "underline"))
ocularLabel.pack(pady=15)


ocularButton_1 = ttk.Button(root, text="Keine Reaktion / nicht feststellbar", command=lambda: ocular_response(1))
ocularButton_1.pack(fill="x")

ocularButton_2 = ttk.Button(root, text="Augenöffnen nach Schmerzreiz", command=lambda: ocular_response(2))
ocularButton_2.pack(fill="x")

ocularButton_3 = ttk.Button(root, text="Augenöffnen auf Aufforderung", command=lambda: ocular_response(3))
ocularButton_3.pack(fill="x")

ocularButton_4 = ttk.Button(root, text="Spontanes Öffnen der Augen", command=lambda: ocular_response(4))
ocularButton_4.pack(fill="x")


labelVerbal = tk.StringVar()
labelVerbal.set("Verbale Reaktion: Bitte wählen Sie aus den folgenden Optionen:")
verbalLabel = tk.Label(root, textvariable=labelVerbal, font=("Arial", 14, "underline"))
verbalLabel.pack(pady=15)


verbalButton_1 = ttk.Button(root, text="Keine Reaktion / nicht feststellbar", command=lambda: verbal_response(1))
verbalButton_1.pack(fill="x")

verbalButton_2 = ttk.Button(root, text="Unverständliche Laute", command=lambda: verbal_response(2))
verbalButton_2.pack(fill="x")

verbalButton_3 = ttk.Button(root, text="Inadäquat / Wortsalat", command=lambda: verbal_response(3))
verbalButton_3.pack(fill="x")

verbalButton_4 = ttk.Button(root, text="Desorientiert", command=lambda: verbal_response(4))
verbalButton_4.pack(fill="x")

verbalButton_5 = ttk.Button(root, text="Räumlich/zeitlich orientiert", command=lambda: verbal_response(5))
verbalButton_5.pack(fill="x")


labelMotoric = tk.StringVar()
labelMotoric.set("Motorische Reaktion: Bitte wählen Sie aus den folgenden Optionen:")
motoricLabel = tk.Label(root, textvariable=labelMotoric, font=("Arial", 14, "underline"))
motoricLabel.pack(pady=20)


motoricButton_1 = ttk.Button(root, text="Keine Reaktion / nicht feststellbar", command=lambda: motoric_response(1))
motoricButton_1.pack(fill="x")

motoricButton_2 = ttk.Button(root, text="Strecksynergismen", command=lambda: motoric_response(2))
motoricButton_2.pack(fill="x")

motoricButton_3 = ttk.Button(root, text="Beugesynergismen", command=lambda: motoric_response(3))
motoricButton_3.pack(fill="x")

motoricButton_4 = ttk.Button(root, text="Ungezielte Abwehrbewegungen", command=lambda: motoric_response(4))
motoricButton_4.pack(fill="x")

motoricButton_5 = ttk.Button(root, text="Gezielte Abwehrbewegungen", command=lambda: motoric_response(5))
motoricButton_5.pack(fill="x")

motoricButton_6 = ttk.Button(root, text="Befolgt Aufforderungen", command=lambda: motoric_response(6))
motoricButton_6.pack(fill="x")


pointsDisplay = tk.Label(root, textvariable=diaPoints, font=("Arial", 16))
pointsDisplay.pack(pady=15)

diaLabel2 = tk.Label(root, textvariable=diaLabel1, font=("Arial", 14, "bold"))
diaLabel2.pack(pady=25)


diagnosis()

buttonExit = ttk.Button(root, text="Beenden", command=root.destroy)
buttonExit.pack()

root.mainloop()