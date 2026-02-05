import tkinter as tk
from tkinter import messagebox

class ThreeAddressCode:
    def __init__(self):
        self.temp_count = 0  # Counter for temporary variables
        self.instructions = []  # Store the generated TAC instructions

    def new_temp(self):
        """Generate a new temporary variable."""
        self.temp_count += 1
        return f"t{self.temp_count}"

    def generate_tac(self, expression):
        """Generate TAC for an arithmetic expression."""
        stack = []  # Stack for operators and operands
        postfix = self.infix_to_postfix(expression)  # Convert to postfix notation

        for token in postfix:
            if token.isalnum():  # If operand, push to stack
                stack.append(token)
            elif token == '=':  # Assignment operator
                if len(stack) < 2:
                    raise ValueError("Invalid expression: insufficient operands for assignment.")
                rhs = stack.pop()
                lhs = stack.pop()
                self.instructions.append(f"{lhs} = {rhs}")
                stack.append(lhs)
            else:  # Binary operator
                if len(stack) < 2:
                    raise ValueError("Invalid expression: insufficient operands for binary operator.")
                op2 = stack.pop()
                op1 = stack.pop()
                temp = self.new_temp()
                self.instructions.append(f"{temp} = {op1} {token} {op2}")
                stack.append(temp)

        if len(stack) != 1:
            raise ValueError("Invalid expression: stack did not resolve to a single result.")
        return stack.pop()

    def infix_to_postfix(self, expression):
        """Convert an infix expression to postfix notation."""
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0, '=': -1}
        output = []
        operators = []

        for token in expression.split():
            if token.isalnum():  # Operand
                output.append(token)
            elif token == '(':  # Left parenthesis
                operators.append(token)
            elif token == ')':  # Right parenthesis
                while operators and operators[-1] != '(':
                    output.append(operators.pop())
                if not operators:
                    raise ValueError("Mismatched parentheses in expression.")
                operators.pop()
            else:  # Operator
                while (operators and precedence[operators[-1]] >= precedence[token]):
                    output.append(operators.pop())
                operators.append(token)

        while operators:
            if operators[-1] == '(':
                raise ValueError("Mismatched parentheses in expression.")
            output.append(operators.pop())

        return output

    def get_instructions(self):
        """Return all generated TAC instructions as a string."""
        return "\n".join(self.instructions)


# GUI Application
class TACApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Three-Address Code Generator")
        self.root.geometry("600x400")
        self.root.configure(bg="#E6E6FA")  # Lavender background color

        self.label = tk.Label(root, text="Enter Expression:", font=("Arial", 14), bg="#E6E6FA", fg="#4B0082")
        self.label.pack(pady=10)

        self.expression_entry = tk.Entry(root, font=("Arial", 14), width=50, bg="white", fg="#4B0082")
        self.expression_entry.pack(pady=10)

        self.generate_button = tk.Button(root, text="Generate TAC", font=("Arial", 14), bg="#4B0082", fg="white",
                                         command=self.generate_tac)
        self.generate_button.pack(pady=10)

        self.output_text = tk.Text(root, font=("Arial", 12), height=15, width=70, bg="white", fg="#4B0082", state=tk.DISABLED)
        self.output_text.pack(pady=10)

    def generate_tac(self):
        """Generate TAC for the entered expression."""
        expression = self.expression_entry.get()
        if not expression.strip():
            messagebox.showerror("Error", "Please enter a valid expression.")
            return

        tac_generator = ThreeAddressCode()
        try:
            tac_generator.generate_tac(expression)
            tac_instructions = tac_generator.get_instructions()
            self.output_text.config(state=tk.NORMAL)
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, tac_instructions)
            self.output_text.config(state=tk.DISABLED)
        except Exception as e:
            messagebox.showerror("Error", str(e))


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = TACApp(root)
    root.mainloop()
