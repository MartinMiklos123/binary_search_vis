import tkinter as tk
from binary_s_alg import *

root = tk.Tk()
root.title("VS")
canvas = tk.Canvas(root, height=500, width=500)
canvas.pack()


def f_ar_sq(v, arr):
    binary_s(v, arr)


def main(arr, i=0, f=lst_mid):
    def delete():
        canvas.delete("all")

    if i > len(f) - 1:
        return

    x1 = 0
    x2 = 50
    y1 = 250
    y2 = 300
    m = f[i][1]
    l = f[i][0]
    r = f[i][2]

    canvas.create_text(50, 50, text=f"Left: {l}", font=("Halvetica", 20, "bold"), fill="black")
    canvas.create_text(52, 100, text=f"Right: {r}", font=("Halvetica", 20, "bold"), fill="black")
    canvas.create_text(52, 150, text=f"Mid: {m}", font=("Halvetica", 20, "bold"), fill="black")
    canvas.create_text(300, 150, text=f"mid = {l} + ({r} - {l})//2", font=("Halvetica", 20, "bold"),
                       fill="black")

    for j in range(0, len(arr)):

        if j == m:
            c = "red"
            w = 5

        elif j in range(l, r + 1) and j != m:
            c = "blue"
            w = 5

        else:
            c = None
            w = 1

        canvas.create_rectangle(x1, y1, x2, y2, outline=c, width=w)
        canvas.create_text(x1 + 20, y1 + 20, text=str(arr[j]), font=("Halvetica", 20, "bold"), fill="black")
        x1 += 50
        x2 += 50
    root.update_idletasks()
    canvas.after(4000, delete)
    canvas.after(4000, main, arr, i + 1)


x = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
num = 12
f_ar_sq(num, x)
main(x)

root.mainloop()
