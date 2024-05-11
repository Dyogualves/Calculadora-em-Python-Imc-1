import tkinter as tk 




def calcular(): 
    peso = float(input1.get())
    altura = float(input2.get())
    calc = peso // altura ** 2
    resultado.config(text=f'Resultado: {calc}')



janela =  tk.Tk()
janela.title('Titulo')
janela.geometry('500x500')

texto = tk.Label(janela, text = 'CALCULADORA', width=20)
texto.pack()



input1 = tk.Entry(janela, width=10)
input1.pack()

input2 = tk.Entry(janela, width=10)
input2.pack()




btn1 = tk.Button(janela, text='Calcular',bg ='white', fg='black' , width = 6, height=3, command = calcular)
btn1.pack()

resultado =  tk.Label(janela, text='')
resultado.pack()


janela.mainloop()
