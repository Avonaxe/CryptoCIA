import tkinter as tk
import time

# The "secure" password (for simulation purposes)
correct_password = "secure123"

# Simulates password verification with timing differences
def simulate_timing_attack():
    user_input = entry.get()
    start_time = time.time()
    
    # Check each character against the correct password
    for i in range(min(len(user_input), len(correct_password))):
        if user_input[i] != correct_password[i]:
            break
        # Introduce a small delay to simulate a timing leak
        time.sleep(0.1)  # Simulate processing time per character

    end_time = time.time()
    elapsed_time = end_time - start_time
    
    if user_input == correct_password:
        result_label.config(text="Access Granted", fg="green")
    else:
        result_label.config(text=f"Access Denied (Time: {elapsed_time:.2f}s)", fg="red")

# Set up the main application window
root = tk.Tk()
root.title("Timing Attack Simulation")
root.geometry("500x300")
root.configure(bg="#f0f0f0")

# Title label
title_label = tk.Label(root, text="Timing Attack Simulation", font=("Helvetica", 16), bg="#f0f0f0")
title_label.pack(pady=20)

# Instructions
instructions = tk.Label(root, text="Enter the password and observe the timing difference:\n(Hint: The correct password is 'secure123')", 
                        font=("Helvetica", 10), bg="#f0f0f0", fg="gray")
instructions.pack(pady=5)

# Input field for the password
entry = tk.Entry(root, width=30, font=("Helvetica", 12))
entry.pack(pady=10)

# Button to simulate the attack
attack_button = tk.Button(root, text="Submit", command=simulate_timing_attack, bg="#007bff", fg="white", font=("Helvetica", 12))
attack_button.pack(pady=10)

# Label to display the result
result_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#f0f0f0")
result_label.pack(pady=20)

# Run the application
root.mainloop()
