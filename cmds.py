import tkinter as tk
import subprocess

def interpretar_comando():
    codigo = codigo_text.get("1.0", "end-1c")
    comandos = codigo.split("\n")

    for comando in comandos:
        palavras = comando.split()
        if len(palavras) > 0:
            if palavras[0] == "echo":
                saida_text.insert("end", " ".join(palavras[1:]) + "\n")
            elif palavras[0] == "type" and len(palavras) == 2:
                try:
                    with open(palavras[1], 'r') as arquivo:
                        texto = arquivo.read()
                        saida_text.insert("end", texto + "\n")
                except FileNotFoundError:
                    saida_text.insert("end", f"O arquivo '{palavras[1]}' não foi encontrado.\n")
            else:
                resultado = subprocess.run(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                saida_text.insert("end", resultado.stdout.decode("latin-1", errors="replace"))
                saida_text.insert("end", resultado.stderr.decode("latin-1", errors="replace"))

# Criação da janela principal
root = tk.Tk()
root.title("Interpretador de Comandos")

# Área de texto para inserção de código
codigo_text = tk.Text(root, wrap="none", width=40, height=10, bg="yellow", fg="black")
codigo_text.pack()

# Botão para interpretar o código
interpretar_button = tk.Button(root, text="Interpretar", command=interpretar_comando)
interpretar_button.pack()

# Área de texto para a saída da consola
saida_text = tk.Text(root, wrap="none", width=40, height=10 , bg="yellow", fg="black")
saida_text.pack()

root.mainloop()
