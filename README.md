# 🏞️ Wildlife Sanctuary Management System

## 📌 Overview
The **Wildlife Sanctuary Management System** is a Python-based program designed to manage various species of animals within a sanctuary. It tracks animal behaviors, population statistics, and endangered species status while supporting interactions with animals.

---

## 🚀 Features
- 🦁 **Animal Management**: Track different species, including mammals, birds, and reptiles.
- 🔢 **Population Tracking**: Keep a count of the total number of animals in the sanctuary.
- 🏅 **Endangered Status**: Identify and track endangered species.
- 🦅 **Flying Capabilities**: Manage and simulate the behavior of birds, including soaring and diving.
- 🎭 **Animal Interactions**: Simulate interactions like sleeping, eating, swimming, and flying.
- 🔎 **Wild Species Detection**: Identify whether an animal is considered wild.

---

## 🛠 Technologies Used
This project highlights fundamental **Python** concepts such as:
- **Object-Oriented Programming (OOP)**: Utilizes multiple classes with inheritance and encapsulation.
- **Class Methods & Static Methods**: Implements `@classmethod` and `@staticmethod` for structured logic.
- **Mixins & Multiple Inheritance**: Implements shared behavior across different classes.
- **Encapsulation & Polymorphism**: Classes override methods to provide species-specific behavior.
- **Interaction Mechanisms**: Allows interaction with animals through behaviors and status tracking.

---

## 🔹 How to Use
1️⃣ **Clone the Repository**:
   ```bash
   git clone https://github.com/dodginfeds/wildlife-sanctuary.git
   cd wildlife-sanctuary
   ```
2️⃣ **Run the Application**:
   ```bash
   python wildlife_sanctuary.py
   ```

---

## 📌 Example Usage
```python
# Creating different animals
from wildlife_sanctuary import Mammal, Reptile, EndangeredBird

dolphin = Mammal(name="Dolph", color="Blue", size="Big", species="Dolphin")
eagle = EndangeredBird(name="Rick", color="Brown and White", size="Huge", species="Eagle", endanger_status="Endangered", wing_span=4.5, length=18)
snake = Reptile(name="Sabath", color="Black and White", size="Tiny", species="Garden Snake")

# Displaying interactions
print(dolphin.describe())
print(eagle.is_soaring())
print(snake.slithering())
```

🔹 **Output:**
```
Dolph's color is Blue and it is Big.
Rick is soaring!
Sabath is slithering!
```

---

## 🔮 Future Enhancements
- 📊 **Animal Database**: Store and retrieve animal data from a structured database.
- 🎮 **Interactive GUI**: Develop a graphical interface for better user interaction.
- 🌍 **Wildlife Statistics Dashboard**: Implement visualization tools for tracking animal populations.
- 📢 **AI Behavior Simulation**: Introduce machine learning models for behavioral prediction.

---

For any inquiries, feel free to reach out via [GitHub](https://github.com/dodginfeds).
