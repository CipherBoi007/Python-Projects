
import tkinter as tk
from tkinter import messagebox, font
from BMI_Calculator import calculate_bmi

def on_calculate():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        bmi, category = calculate_bmi(weight, height)
        result_var.set(f"Your BMI is: {bmi:.1f}\nCategory: {category}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for weight and height.")



# --- Styling ---
BG_COLOR1 = "#4a90e2"  # Top color
BG_COLOR2 = "#f0f4f8"  # Bottom color
FRAME_COLOR = "#ffffff"
BTN_COLOR = "#4a90e2"
BTN_TEXT = "#ffffff"
LABEL_COLOR = "#333333"
RESULT_COLOR = "#00796b"
FONT_MAIN = ("Segoe UI", 12)
FONT_TITLE = ("Segoe UI", 16, "bold")

root = tk.Tk()
root.title("BMI Calculator GUI")
root.geometry("400x350")
root.resizable(False, False)

# Draw vertical gradient on a Canvas
canvas = tk.Canvas(root, width=400, height=350, highlightthickness=0)
canvas.pack(fill="both", expand=True)
def draw_gradient(canvas, color1, color2):
    for i in range(350):
        r1, g1, b1 = root.winfo_rgb(color1)
        r2, g2, b2 = root.winfo_rgb(color2)
        r = int(r1 + (r2 - r1) * i / 350) // 256
        g = int(g1 + (g2 - g1) * i / 350) // 256
        b = int(b1 + (b2 - b1) * i / 350) // 256
        color = f"#{r:02x}{g:02x}{b:02x}"
        canvas.create_line(0, i, 400, i, fill=color)
draw_gradient(canvas, BG_COLOR1, BG_COLOR2)

# Place the main frame on top of the gradient
frame = tk.Frame(canvas, padx=30, pady=30, bg=FRAME_COLOR, bd=2, relief="groove")
frame.place(relx=0.5, rely=0.5, anchor="center")

# Optional: Add a simple logo (emoji or text)
logo = tk.Label(frame, text="🩺", font=("Segoe UI Emoji", 32), bg=FRAME_COLOR)
logo.grid(row=0, column=0, columnspan=2, pady=(0, 5))

title = tk.Label(frame, text="BMI Calculator", font=FONT_TITLE, bg=FRAME_COLOR, fg=BTN_COLOR)
title.grid(row=1, column=0, columnspan=2, pady=(0, 15))

tk.Label(frame, text="Weight (kg):", font=FONT_MAIN, bg=FRAME_COLOR, fg=LABEL_COLOR).grid(row=2, column=0, sticky="e", pady=5)
weight_entry = tk.Entry(frame, font=FONT_MAIN, width=15, relief="solid", bd=1)
weight_entry.grid(row=2, column=1, pady=5)

tk.Label(frame, text="Height (m):", font=FONT_MAIN, bg=FRAME_COLOR, fg=LABEL_COLOR).grid(row=3, column=0, sticky="e", pady=5)
height_entry = tk.Entry(frame, font=FONT_MAIN, width=15, relief="solid", bd=1)
height_entry.grid(row=3, column=1, pady=5)

calc_btn = tk.Button(frame, text="Calculate BMI", command=on_calculate, font=FONT_MAIN, bg=BTN_COLOR, fg=BTN_TEXT, activebackground="#357ab8", activeforeground=BTN_TEXT, relief="flat", padx=10, pady=5, cursor="hand2")
calc_btn.grid(row=4, column=0, columnspan=2, pady=15)

result_var = tk.StringVar()
result_label = tk.Label(frame, textvariable=result_var, font=FONT_MAIN, fg=RESULT_COLOR, bg=FRAME_COLOR, justify="center")
result_label.grid(row=5, column=0, columnspan=2, pady=(5, 0))

root.mainloop()
