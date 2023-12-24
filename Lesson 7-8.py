import tkinter as tk

'''window = tk.Tk()
window.title("B4211")
window.geometry("600x400+400+200")
#window.resizable(True, False)
window.minsize(300, 300)
window.iconbitmap("pics/bomb.ico")

label = tk.Label(text="Hello Python",
                 font=("Cooper Black", 20, "bold"),
                 fg="DeepPink",
                 bg="yellow",
                 padx=50,
                 pady=30)
label.pack()

button = tk.Button(text="Click My", padx=30)
button.pack()

window.mainloop()'''


bomb = 100
score = 0
press_enter = True

window = tk.Tk()
window.geometry("600x600+400+100")
window.title("Bomber")
window.resizable(False, False)
window.iconbitmap("pics/bomb.ico")

label = tk.Label(text="Для початку гри натисніть [ENTER]",
                 font=("Comic Sans MS", 12, "bold"))
label.pack()

bomb_count = tk.Label(text=f"Залишок бомб {bomb}", font=("Comic Sans MS", 16, "bold"))
bomb_count.pack()

score_label = tk.Label(text=f"Набрані бали {score}", font=("Comic Sans MS", 16, "bold"))
score_label.pack()


img1 = tk.PhotoImage(file="pics/1.gif")
img2 = tk.PhotoImage(file="pics/2.gif")
img3 = tk.PhotoImage(file="pics/3.gif")
img4 = tk.PhotoImage(file="pics/4.gif")

bomb_label = tk.Label(image=img1)
bomb_label.pack()

def is_alive():
    global bomb
    if bomb <= 0:
        bomb = 0
        label.config(text="Бабах! Бабах! Бабах!", fg="red")
        return False
    else:
        return True


def update_image():
    global bomb
    global score
    if bomb >= 80:
        bomb_label.config(image=img1)
    elif 50 <= bomb < 80:
        bomb_label.config(image=img2)
    elif 0 < bomb < 50:
        bomb_label.config(image=img3)
    else:
        bomb_label.config(image=img4)

    bomb_count.config(text=f"Залишок бомб {bomb}")
    score_label.config(text=f"Набрані бали {score}")
    bomb_label.after(100, update_image)

def update_bomb():
    global bomb
    bomb -= 5
    if is_alive():
        bomb_label.after(400, update_bomb)

def update_score():
    global score
    score += 1
    if is_alive():
        score_label.after(1000, update_score)

def click():
    global bomb
    if is_alive():
        bomb += 1

def start(event):
    global press_enter
    if not press_enter:
        pass
    else:
        update_score()
        update_bomb()
        update_image()
        label.config(text="")
        press_enter = False

click_button = tk.Button(text="Тисни сюди!", font=("Comic Sans MS", 16, "bold"),
                         bg="black", fg="white", command=click, repeatinterval=100)
click_button.pack()

window.bind('<Return>', start)

window.mainloop()