
# 🧾 Three-Address Code (TAC) Generator GUI

A Python GUI application that generates **Three-Address Code (TAC)** from arithmetic expressions using **Tkinter**.
The system converts infix expressions into postfix notation, then generates structured TAC instructions using temporary variables.

This project is designed as an **educational compiler tool** to visualize intermediate code generation in a simple and interactive way.

---

## ✨ Features

* 🔄 Infix ➜ Postfix conversion
* 🧠 Automatic temporary variable generation (`t1`, `t2`, `t3`, ...)
* 🧾 TAC generation format:

  ```
  t1 = a * b
  t2 = t1 + c
  x  = t2
  ```
* 🖥️ Graphical User Interface using Tkinter
* 🎨 Clean, styled UI with modern colors
* ❗ Error handling:

  * Invalid expressions
  * Mismatched parentheses
  * Invalid operator usage
* 📚 Educational structure for compiler courses

---

## 🏗️ Project Structure

```
three-address-code-generator/
│
├── main.py
└── README.md
```

---

## ⚙️ Requirements

* Python 3.x
* Tkinter (comes pre-installed with Python)

No external libraries required.

---

## ▶️ How to Run

```bash
python main.py
```

---

## 🧠 How It Works

### 1️⃣ Infix to Postfix Conversion

The system converts expressions like:

```
a + b * c
```

Into postfix:

```
a b c * +
```

### 2️⃣ TAC Generation

Postfix expression is evaluated using a stack to generate TAC:

```
t1 = b * c
t2 = a + t1
```

Each operation produces a temporary variable.

---

## 🧩 Example

### Input:

```
a + b * c
```

### Output (TAC):

```
t1 = b * c
t2 = a + t1
```

---

## 🎯 Use Cases

* Compiler Design courses
* Intermediate Code Generation
* Programming Languages labs
* Data Structures & Algorithms education
* Visual learning for stack-based parsing
* Teaching expression evaluation
* Educational software projects

---

## 🚀 Future Enhancements

* Expression parsing without space-separated tokens
* Full assignment support (`x = a + b * c`)
* Quadruple & Triple representation generation
* Syntax Tree visualization
* Export TAC to file (TXT / CSV)
* Expression history
* Dark mode UI
* Multi-expression batch processing

---

## 👩‍💻 Author

**Shereen Alaa**
Machine Learning Engineer
AI & Educational Software Developer

---

## 📄 License

Open-source project for educational and academic use.
