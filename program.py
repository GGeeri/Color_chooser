import tkinter as tk
import random
import time

# Lista a színekhez
colors = ['red', 'green', 'blue', 'yellow', 'pink', 'orange', 'purple', 'brown', 'black', 'gray']
dictt={
    "red": "piros",
    "green": "zöld",
    "blue": "kék",
    "yellow":"sárga",
    "pink":"rózsaszín",
    "orange":"narancs",
    "purple":"lila",
    "brown":"barna",
    "black":"fekete",
    "gray":"szürke"
}

# Kezdő változók
best_time = float('inf')
current_color = ''
correct_answer = ''
start_time = 0
timer_running = False

# Képernyő elemek létrehozása
root = tk.Tk()
root.title("Színválasztó Játék")

label_word = tk.Label(root, font=("Helvetica", 20), width=30, height=5)
label_word.pack(pady=20)

entry = tk.Entry(root, font=("Helvetica", 20))
entry.pack(pady=10)

label_time = tk.Label(root, font=("Helvetica", 16))
label_time.pack(pady=10)

label_best_time = tk.Label(root, font=("Helvetica", 16))
label_best_time.pack(pady=10)

label_feedback = tk.Label(root, font=("Helvetica", 16))
label_feedback.pack(pady=10)

dropdown_label = tk.Label(root, text="Válaszd ki a színek számát:")
dropdown_label.pack(pady=10)

color_count_var = tk.IntVar(value=5)  # Alapértelmezett 5 szín
dropdown = tk.OptionMenu(root, color_count_var, 2, 3, 4, 5, 6, 7, 8, 9, 10)
dropdown.pack(pady=10)

# Kezdő gomb
def start_game():
    """Játék indítása és a szó színének véletlenszerű kiválasztása"""
    global current_color, correct_answer, start_time, timer_running
    entry.delete(0, tk.END)  # Töröljük a beírt szöveget
    label_feedback.config(text="")
    timer_running = True
    start_time = time.time()
    update_timer()

    # Véletlenszerűen válasszunk színt és szót
    color_count = color_count_var.get()
    current_color = random.choice(colors[:color_count])
    correct_answer = random.choice(colors[:color_count])

    # A szó a képernyőn
    label_word.config(text=correct_answer.upper(), fg=current_color)

def update_timer():
    """Az eltelt idő frissítése"""
    if timer_running:
        elapsed_time = round(time.time() - start_time, 2)
        label_time.config(text=f"Eltelt idő: {elapsed_time} másodperc")
        root.after(100, update_timer)

def check_answer(event=None):
    """A válasz ellenőrzése"""
    global best_time
    user_input = entry.get().strip().lower()

    if user_input == dictt[current_color] or user_input == current_color:
        elapsed_time = round(time.time() - start_time, 2)
        label_feedback.config(text="Helyes válasz!", fg="green")

        # Ha jobb, mint a legjobb idő, frissítjük
        if elapsed_time < best_time:
            best_time = elapsed_time
            update_best_time()

        # Új játék indítása
        start_game()

def update_best_time():
    """A legjobb idő frissítése a képernyőn"""
    if best_time == float('inf'):
        label_best_time.config(text="Legjobb eredmény: Nincs")
    else:
        label_best_time.config(text=f"Legjobb eredmény: {round(best_time, 2)} másodperc")

# Kezdés gomb
start_button = tk.Button(root, text="Játék indítása", font=("Helvetica", 14), command=start_game)
start_button.pack(pady=20)

# A legjobb idő kiírása
update_best_time()

# Beállítjuk, hogy a felhasználó válaszát a 'Return' billentyűvel is ellenőrizzük
root.bind('<Return>', check_answer)

# A Tkinter fő hurok indítása
root.mainloop()
