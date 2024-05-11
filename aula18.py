import tkinter as tk 

imc = peso / altura ** 2


def somar(): 
    n1 = float(input1.get())
    n2 = float(input2.get())
    soma = n1 + n2 
    resultado.config(text=f'Resultado {soma}')


def subtrair():
    n1 = float(input1.get())
    n2 = float(input2.get())
    sub = n1 - n2
    resultado.config(text=f'Resultado {sub}')

def multiplicacao():
    n1 = float(input1.get())
    n2 = float(input2.get())
    mul = n1 * n2
    resultado.config(text=f'Resultado {mul}')


def divisao():
    n1 = float(input1.get())
    n2 = float(input2.get())
    div = n1 / n2
    resultado.config(text=f'Resultado {div}')







janela =  tk.Tk()
janela.title('Titulo')
janela.geometry('500x500')

texto = tk.Label(janela, text = 'CALCULADORA', width=20)
texto.pack()



input1 = tk.Entry(janela, width=10)
input1.pack()

input2 = tk.Entry(janela, width=10)
input2.pack()




btn1 = tk.Button(janela, text='+',bg ='white', fg='black' , width = 3, height=2, command = somar)
btn1.pack()
btn2 = tk.Button(janela, text='-',bg ='white', fg='black' , width = 3, height=2, command = subtrair)
btn2.pack()
btn3 = tk.Button(janela, text='*',bg ='white', fg='black' , width = 3, height=2, command = multiplicacao)
btn3.pack()
btn4 = tk.Button(janela, text='/',bg ='white', fg='black' , width = 3, height=2, command = divisao)
btn4.pack()


resultado =  tk.Label(janela, text='')
resultado.pack()


janela.mainloop()

