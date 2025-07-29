'''
This is a programm designed to evaluate the impaired consciousness in patients after brain injuries.
The model on which this application is based is called the glasgow coma scale.

Author: Florian Becker
Date: 2025-06-17
'''
import tkinter as tk



print("====== Glasgow Coma Scale (GCS) ======")
print("Ocular response: Please choose from the following options:")
print("0 = Not testable (severe trauma to the eyes)")
print("1 = Does not open eyes")
print("2 = Opens eyes in response to pain")
print("3 = Opens eyes in response to voice")
print("4 = Opens eyes spontaneously")

ocular_response = int(input("Enter your choice:"))

print("Verbal response: Please choose from the following options:")
print("0 = Not testable (Intubation, non-oral language disability, linguistic barrier)")
print("1 = Makes no sounds")
print("2 = Incomprehensible sounds")
print("3 = Inappropriate words")
print("4 = Confused and disoriented, but able to answer questions")
print("5 = Oriented to time, person, and place, converses normally")

verbal_response = int(input("Enter your choice: "))

print("motoric response: Please choose from the following options:")
print("0 = Not testable (acquired causes such as post-stroke, post-neurological injury; congenital/innate such as cerebral palsy)")
print("1 = Makes no movements")
print("2 = Abnormal extension")
print("3 = Abnormal flexion")
print("4 = Flexion/ Withdrawal from painful stimuli")
print("5 = Moves to localise pain")
print("6 = Obeys commands")

motoric_response = int(input("Enter your choice: "))

points_sum = ocular_response + verbal_response + motoric_response

if points_sum <= 8:
    diagnosis = "severe brain injuries"
elif points_sum >= 9 and points_sum <= 12:
    diagnosis = "moderate brain injuries"
elif points_sum >= 13:
    diagnosis = "minor brain injuries"

print(f"Your patient has {diagnosis}.")
print("====== Application closed ======")


