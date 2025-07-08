
import tkinter as tk
from tkinter import messagebox
from password_generator import generate_secure_password

def on_generate():
    try:
        length = int(length_entry.get())
        count = int(count_entry.get())
        count = max(1, min(20, count))
        use_upper = upper_var.get()
        use_digits = digits_var.get()
        use_special = special_var.get()
        passwords = []
        for i in range(count):
            password = generate_secure_password(length, use_upper, use_digits, use_special)
            passwords.append(f"{i+1}. {password}")
        # Dynamically set height (min 3, max 15)
        lines = max(3, min(count, 15))
        result_text.config(height=lines)
        result_text.config(state="normal")
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "\n".join(passwords))
        result_text.config(state="disabled")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for length and count.")



# --- Styling ---
BG_COLOR1 = "#ffb347"  # Top color (orange)
BG_COLOR2 = "#ffccff"  # Bottom color (light pink)
FRAME_COLOR = "#ffffff"
BTN_COLOR = "#ff9800"
BTN_TEXT = "#ffffff"
LABEL_COLOR = "#333333"
RESULT_COLOR = "#00796b"
FONT_MAIN = ("Segoe UI", 12)
FONT_TITLE = ("Segoe UI", 16, "bold")

root = tk.Tk()
root.title("Password Generator GUI")
root.geometry("540x370")
root.resizable(False, False)

# Draw vertical gradient on a Canvas
canvas = tk.Canvas(root, width=540, height=370, highlightthickness=0)
canvas.pack(fill="both", expand=True)
def draw_gradient(canvas, color1, color2):
    for i in range(370):
        r1, g1, b1 = root.winfo_rgb(color1)
        r2, g2, b2 = root.winfo_rgb(color2)
        r = int(r1 + (r2 - r1) * i / 370) // 256
        g = int(g1 + (g2 - g1) * i / 370) // 256
        b = int(b1 + (b2 - b1) * i / 370) // 256
        color = f"#{r:02x}{g:02x}{b:02x}"
        canvas.create_line(0, i, 540, i, fill=color)
draw_gradient(canvas, BG_COLOR1, BG_COLOR2)


# Place the main frame on top of the gradient
frame = tk.Frame(canvas, padx=30, pady=30, bg=FRAME_COLOR, bd=2, relief="groove")
frame.place(relx=0.5, rely=0.5, anchor="center")

# Optional: Add a simple logo (emoji or text)
logo = tk.Label(frame, text="🔒", font=("Segoe UI Emoji", 32), bg=FRAME_COLOR)
logo.grid(row=0, column=0, columnspan=2, pady=(0, 5))

title = tk.Label(frame, text="Password Generator", font=FONT_TITLE, bg=FRAME_COLOR, fg=BTN_COLOR)
title.grid(row=1, column=0, columnspan=2, pady=(0, 15))

tk.Label(frame, text="Password Length:", font=FONT_MAIN, bg=FRAME_COLOR, fg=LABEL_COLOR).grid(row=2, column=0, sticky="e", pady=5)
length_entry = tk.Entry(frame, font=FONT_MAIN, width=15, relief="solid", bd=1)
length_entry.insert(0, "12")
length_entry.grid(row=2, column=1, pady=5)

tk.Label(frame, text="How many passwords:", font=FONT_MAIN, bg=FRAME_COLOR, fg=LABEL_COLOR).grid(row=3, column=0, sticky="e", pady=5)
count_entry = tk.Entry(frame, font=FONT_MAIN, width=15, relief="solid", bd=1)
count_entry.insert(0, "1")
count_entry.grid(row=3, column=1, pady=5)

upper_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)

upper_cb = tk.Checkbutton(frame, text="Include Uppercase", variable=upper_var, font=FONT_MAIN, bg=FRAME_COLOR)
upper_cb.grid(row=4, column=0, columnspan=2, sticky="w")
digits_cb = tk.Checkbutton(frame, text="Include Digits", variable=digits_var, font=FONT_MAIN, bg=FRAME_COLOR)
digits_cb.grid(row=5, column=0, columnspan=2, sticky="w")
special_cb = tk.Checkbutton(frame, text="Include Special Chars", variable=special_var, font=FONT_MAIN, bg=FRAME_COLOR)
special_cb.grid(row=6, column=0, columnspan=2, sticky="w")

gen_btn = tk.Button(frame, text="Generate Password(s)", command=on_generate, font=FONT_MAIN, bg=BTN_COLOR, fg=BTN_TEXT, activebackground="#e65100", activeforeground=BTN_TEXT, relief="flat", padx=10, pady=5, cursor="hand2")
gen_btn.grid(row=7, column=0, columnspan=2, pady=15)


# Scrollable text box for results
result_frame = tk.Frame(frame, bg=FRAME_COLOR)
result_frame.grid(row=8, column=0, columnspan=2, pady=(5, 0), sticky="ew")
result_scroll = tk.Scrollbar(result_frame, orient="vertical")
result_text = tk.Text(result_frame, width=44, height=3, state="disabled", font=("Consolas", 14, "bold"), fg=RESULT_COLOR, bg="#f5f5f5", relief="flat", wrap="none", yscrollcommand=result_scroll.set)
result_scroll.config(command=result_text.yview)
result_text.pack(side="left", fill="both", expand=True)
result_scroll.pack(side="right", fill="y")

root.mainloop()
