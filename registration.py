import hashlib
import json
import tkinter as tk
from tkinter import messagebox, font


def hash_voter_id(voter_id):
    return hashlib.sha256(voter_id.encode()).hexdigest()


def register_voter(voter_id):
    voter_id_hash = hash_voter_id(voter_id)

    # Check if the voter ID is already registered
    if is_voter_registered(voter_id_hash):
        messagebox.showwarning("Registration Error", "This Voter ID is already registered.")
        return

    # Create voter info dictionary
    voter_info = {
        'voter_id_hash': voter_id_hash
    }

    # Append voter info to JSON file
    with open('voter_data.json', 'a') as f:
        json.dump(voter_info, f)
        f.write('\n')
    messagebox.showinfo("Success", f"Voter ID {voter_id} registered successfully!")


def remove_voter(voter_id):
    voter_id_hash = hash_voter_id(voter_id)

    # Load existing voters
    voters = load_voter_data()

    # Check if the voter ID exists
    if voter_id_hash not in voters:
        messagebox.showwarning("Removal Error", "This Voter ID is not registered.")
        return

    # Remove the voter ID from the list
    voters.remove(voter_id_hash)

    # Write the updated list back to the JSON file
    with open('voter_data.json', 'w') as f:
        for voter in voters:
            json.dump({'voter_id_hash': voter}, f)
            f.write('\n')

    messagebox.showinfo("Success", f"Voter ID {voter_id} removed successfully!")


def is_voter_registered(voter_id_hash):
    voters = load_voter_data()
    return voter_id_hash in voters


def load_voter_data():
    voters = []
    try:
        with open('voter_data.json', 'r') as f:
            # Check if the file is empty
            if f.readable():
                f.seek(0)  # Go back to the start of the file
                for line in f:
                    if line.strip():  # Check if the line is not empty
                        voter_info = json.loads(line.strip())
                        voters.append(voter_info['voter_id_hash'])  # Append only the voter ID hash
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        messagebox.showerror("Data Error", "Voter data file is corrupted or contains invalid JSON.")
    return voters


def register():
    voter_id = id_entry.get()

    if not voter_id:
        messagebox.showwarning("Input Error", "Please fill in the Voter ID.")
    else:
        register_voter(voter_id)
        id_entry.delete(0, tk.END)


def remove():
    voter_id = id_entry.get()

    if not voter_id:
        messagebox.showwarning("Input Error", "Please fill in the Voter ID.")
    else:
        remove_voter(voter_id)
        id_entry.delete(0, tk.END)


# Set up the GUI
app = tk.Tk()
app.title("Voter Registration")
app.geometry("400x300")
app.configure(bg="#f0f0f0")

# Custom font for labels and buttons
custom_font = font.Font(family="Helvetica", size=12, weight="bold")

# Create and place widgets
tk.Label(app, text="Voter ID:", bg="#f0f0f0", font=custom_font).pack(pady=10)
id_entry = tk.Entry(app, font=custom_font)
id_entry.pack(pady=10)

register_button = tk.Button(app, text="Register", command=register, bg="#4CAF50", fg="white", font=custom_font)
register_button.pack(pady=10, padx=20, fill='x')

remove_button = tk.Button(app, text="Remove Voter ID", command=remove, bg="#f44336", fg="white", font=custom_font)
remove_button.pack(pady=10, padx=20, fill='x')

# Add a footer label
footer_label = tk.Label(app, text="Voter Registration System", bg="#f0f0f0", font=font.Font(size=10))
footer_label.pack(side="bottom", pady=15)

app.mainloop()
