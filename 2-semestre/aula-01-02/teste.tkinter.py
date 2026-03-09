import tkinter as tk

def mostrar_carta_tkinter():
    root = tk.Tk()
    root.title("Carta Gigante - Tkinter")
    root.geometry("400x400")

    # O caractere (Ás de Ouros)
    carta = "\U0001F0C7"

    # DICA: Fontes específicas para renderizar símbolos/emojis
    # Windows: "Segoe UI Emoji"
    # Mac: "Apple Color Emoji"
    # Linux: "Noto Color Emoji" ou "DejaVu Sans"
    minha_fonte = tk.font.Font(family="Segoe UI Emoji", size=150)

    label = tk.Label(root, text=carta, font=minha_fonte)
    label.pack(expand=True) # Centraliza na tela

    root.mainloop()

if __name__ == "__main__":
    mostrar_carta_tkinter()