# 🧑‍💻 Fun Programming Path for a 7-Year-Old  
_Using Python first, then Go_

This plan introduces programming in a fun, visual, and interactive way.  
It starts with **Python Turtle** (drawing), moves to **Pygame Zero** (games), explores **creative coding**, and finally transitions into **Go with Ebiten**.  

---

## 🎨 Stage 1: Fun with Python Turtle (Weeks 1–3)  
**Goal:** Learn loops, functions, and coordinates by drawing.

- **Week 1: First Steps**
  - Install Python + simple editor (Thonny or Mu).
  - Use `turtle.forward()`, `.right()`, `.left()`.
  - Draw a **square** and a **triangle**.
  - **Challenge:** “Make a house shape (square + triangle roof).”

- **Week 2: Colors & Loops**
  - Introduce loops:  
    ```python
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)
    ```
  - Add `turtle.color("blue")`, `turtle.pensize(3)`.
  - **Challenge:** “Draw a rainbow spiral.”

- **Week 3: Functions**
  - Teach `def draw_star(size): ...`.
  - **Challenge:** “Make a field of stars (loop calling your function).”
  - Creative twist: let him design a **night sky** with stars, moon, etc.

---

## 🎮 Stage 2: Games with Pygame Zero (Weeks 4–6)  
**Goal:** Learn sprites, events, and game loops.

- **Week 4: Sprites & Movement**
  - Load an image: `alien = Actor("alien")`.
  - Move alien with arrow keys.
  - **Challenge:** “Make the alien move around the screen.”

- **Week 5: Animation**
  - Add bouncing ball that hits screen edges.
  - **Challenge:** “Can you make 5 balls bouncing?”

- **Week 6: A Simple Game**
  - Make a game where alien catches falling apples.
  - Add score counter.
  - Let him choose graphics/sounds.

---

## 🖌️ Stage 3: Creative Coding (Weeks 7–8)  
**Goal:** Mix art + code to keep things fresh.

- **Week 7: p5py (Processing in Python)**
  - Draw shapes with `ellipse()`, `rect()`.
  - Animate shapes (moving circle).
  - **Challenge:** “Make a bouncing smiley face.”

- **Week 8: Interactive Art**
  - React to mouse clicks and key presses.
  - **Challenge:** “Draw fireworks on mouse click.”

---

## 🌀 Stage 4: Transition to Go with Ebiten (Weeks 9–12)  
**Goal:** Show that the *same coding ideas* work in another language.

- **Week 9: Hello Go**
  - Show how `package main` works.
  - Print text, then move to graphics with **Ebiten**.
  - Draw a red rectangle on screen.

- **Week 10: Movement**
  - Move rectangle with arrow keys.
  - **Challenge:** “Make a character walk.”

- **Week 11: Collision**
  - Add another object (e.g., treasure).
  - **Challenge:** “Collect the treasure when touched.”

- **Week 12: First Go Game**
  - Put it together: simple “collect coins” game.
  - Show score counter.
  - Let him design sprites.

---

## 🚀 Beyond
Once comfortable, start building “real projects” together:
- **Python:** Drawing app, quiz game, math trainer.
- **Go:** Flappy Bird clone, racing game, or exporting to WebAssembly to play in the browser.

---

## 📌 Teaching Tips
- **Gamify challenges** (stickers, points, high-scores).  
- Keep lessons short (30–40 mins max).  
- Always end with something *he created himself* (even silly).  
- Celebrate small wins with screenshots or saving his “art gallery.”  
