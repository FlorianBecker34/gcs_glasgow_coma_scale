# Glasgow Coma Scale Evaluator

This program is designed to assess the level of impaired consciousness in patients with brain injuries. It is based on the internationally recognized **Glasgow Coma Scale (GCS)** and allows users to classify the severity of the injury by evaluating three key responses:

- **Ocular Response**
- **Verbal Response**
- **Motoric Response**

---

## About my App:
*This is a program designed to evaluate the impaired consciousness in patients after brain injuries.  
The model on which this application is based is called the Glasgow Coma Scale.*

- **Author:** Florian Becker  
- **Date:** June 17, 2025  
- **Language:** Python  

---

##How it works:

The program prompts the user to enter the patient’s condition across the three categories above, using standardized GCS scoring. The total score determines the level of consciousness impairment:

| Total GCS Score | Interpretation               |
|------------------|------------------------------|
| 3–8              | Severe brain injury           |
| 9–12             | Moderate brain injury         |
| 13–15            | Minor brain injury            |

The maximum score is 15, and the minimum is 3 (with `0` used to indicate non-testable responses, which deviates slightly from classical GCS scoring).

---

##Input

All inputs are entered by the user

### Example Score Options:

#### Ocular Response:
- 0 = Not testable 
- 1 = Does not open eyes
- 4 = Opens eyes spontaneously

#### Verbal Response:
- 0 = Not testable (e.g., intubated)
- 1–5 = From no sounds to fully oriented

#### Motoric Response:
- 0 = Not testable (e.g., paralysis)
- 1–6 = From no movement to obeys commands





