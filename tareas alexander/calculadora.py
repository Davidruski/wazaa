import tkinter as tk
import math

class ScientificCalculator:
    def __init__(self, master):
        # Configuración de la ventana principal
        self.master = master
        self.master.title("Calculadora Científica")
        self.master.geometry("400x600")
        self.master.configure(bg='#f0f0f0')

        # Variable para almacenar la expresión actual
        self.current = ''
        
        # Entrada de texto para mostrar operaciones y resultados
        self.display = tk.Entry(master, width=30, font=('Arial', 20), justify='right')
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Definición de botones con sus respectivas funciones
        self.buttons = [
            ['sin', 'cos', 'tan', 'π'],
            ['√', 'x²', 'x³', 'xⁿ'],
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+'],
            ['(', ')', 'C', 'DEL']
        ]

        # Crear y posicionar los botones en la interfaz
        self.create_buttons()

    def create_buttons(self):
        """Crea y posiciona todos los botones en la calculadora"""
        for i, row in enumerate(self.buttons):
            for j, button_text in enumerate(row):
                button = tk.Button(
                    self.master,
                    text=button_text,
                    width=5,
                    height=2,
                    font=('Arial', 12),
                    command=lambda x=button_text: self.button_click(x)
                )
                button.grid(row=i+1, column=j, padx=2, pady=2)

    def button_click(self, value):
        """Maneja los eventos de click en los botones"""
        if value == '=':
            try:
                # Evaluar la expresión y mostrar el resultado
                result = self.evaluate_expression(self.current)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
                self.current = str(result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
                self.current = ''
        
        elif value == 'C':
            # Limpiar la pantalla y la expresión actual
            self.current = ''
            self.display.delete(0, tk.END)
        
        elif value == 'DEL':
            # Borrar el último carácter
            self.current = self.current[:-1]
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.current)
        
        else:
            # Procesar funciones especiales
            if value in ['sin', 'cos', 'tan']:
                self.current += value + '('
            elif value == 'π':
                self.current += str(math.pi)
            elif value == '√':
                self.current += 'sqrt('
            elif value == 'x²':
                self.current += '**2'
            elif value == 'x³':
                self.current += '**3'
            elif value == 'xⁿ':
                self.current += '**'
            else:
                self.current += value
            
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.current)

    def evaluate_expression(self, expression):
        """Evalúa la expresión matemática de manera segura"""
        # Reemplazar funciones matemáticas con sus equivalentes en math
        expression = expression.replace('sin', 'math.sin')
        expression = expression.replace('cos', 'math.cos')
        expression = expression.replace('tan', 'math.tan')
        expression = expression.replace('sqrt', 'math.sqrt')
        
        # Evaluar la expresión y retornar el resultado
        return eval(expression)

# Crear y ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Window()
    calculator = ScientificCalculator(root)
    root.mainloop()