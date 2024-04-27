import tkinter as tk
from functools import partial

root = tk.Tk()  # Создайте новый объект Tk
root.title("Калькулятор 1.0")  # Задайте заголовок окна
root.geometry("300x430")  # Установите размер окна

memory = 0
operation = ''


def actions(s):
    global memory, operation
    if s == 'C':  # clear
        display['text'] = '0'
        memory = 0
        operation = ''
    elif s == 'CE':  # clear only display
        display['text'] = '0'
    elif s in '0123456789':  # nums
        if display['text'] != '0':
            display['text'] += s
        else:
            display['text'] = s
    elif s in '÷×-+':  # set operation
        memory = float(display['text'])
        operation = s
        display['text'] = '0'
    elif s == '=':  # equals
        if operation == '+':
            display['text'] = str(memory + float(display['text']))
        elif operation == '-':
            display['text'] = str(memory - float(display['text']))
        elif operation == '×':
            display['text'] = str(memory * float(display['text']))
        elif operation == '÷' and float(display['text']) != 0:
            display['text'] = str(memory / float(display['text']))
    elif s == '.':  # dot
        if '.' not in display['text']:
            display['text'] += '.'
    elif s == '±':
        if '-' not in display['text'] and display['text'] != '0':
            display['text'] = '-' + display['text']
        else:
            display['text'] = display['text'].replace('-', '')
    elif s == '⌫':  # backspace
        if display['text'] != '0':
            if len(display['text'].replace('-', '')) > 1:
                display['text'] = display['text'][:-1]
            else:
                display['text'] = '0'
    elif s == '%':
        display['text'] = str(memory * float(display['text']) / 100)
    elif s == '1/x':
        display['text'] = str(1 / float(display['text']))
    elif s == 'x²':
        display['text'] = str(float(display['text']) ** 2)
    elif s == '√‎x':
        display['text'] = str(float(display['text']) ** 0.5)


btns_label = [['%', 'CE', 'C', '⌫'],
              ['1/x', 'x²', '√‎x', '÷'],
              '789×', '456-', '123+', '±0.=']

font = ("Arial", 22, "bold")
display = tk.Label(root, text='0', font=font, bg="yellow",
                   width=15, padx=2, pady=1, anchor="e")
display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

for row in range(len(btns_label)):
    for col in range(len(btns_label[row])):
        btn = tk.Button(root, text=btns_label[row][col], font=font, width=3,
                        command=partial(actions, btns_label[row][col]))
        btn.grid(row=row + 1, column=col)


root.mainloop()  # Запустите основной цикл
