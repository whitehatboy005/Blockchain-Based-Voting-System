import hashlib
import json
import datetime
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class Block:
    def __init__(self, index, previous_hash, timestamp, data):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{json.dumps(self.data)}"
        return hashlib.sha256(block_string.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = []
        self.voters = {}
        self.candidate_votes = {}
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, '0', datetime.datetime.now(), "Genesis Block")
        self.chain.append(genesis_block)

    def add_voter(self, voter_id_hash):
        self.voters[voter_id_hash] = False  # Store the hash as a key and set voting status to False

    def cast_vote(self, voter_id, candidate):
        voter_id_hash = hashlib.sha256(voter_id.encode()).hexdigest()  # Hash the voter ID for comparison
        if voter_id_hash in self.voters:
            if self.voters[voter_id_hash]:
                raise Exception("This voter has already voted.")
            self.voters[voter_id_hash] = True  # Mark the voter as having voted
            self.candidate_votes[candidate] = self.candidate_votes.get(candidate, 0) + 1
            index = len(self.chain)
            previous_hash = self.chain[-1].hash
            timestamp = datetime.datetime.now()
            data = {
                'vote': candidate  # Only include the candidate voted for
            }
            new_block = Block(index, previous_hash, timestamp, data)
            self.chain.append(new_block)
            return
        raise Exception("Voter not registered.")

    def show_results(self):
        results = ""
        for candidate, votes in self.candidate_votes.items():
            results += f"{candidate}: {votes} votes\n"
        return results.strip() if results else "No votes cast yet."

    def get_chain_data(self):
        chain_data = []
        for block in self.chain:
            chain_data.append({
                'Index': block.index,
                'Previous Hash': block.previous_hash,
                'Timestamp': block.timestamp,
                'Data': block.data,  # Data now only contains the candidate vote
                'Hash': block.hash
            })
        return chain_data


class VotingApp:
    def __init__(self, master):
        self.master = master
        self.blockchain = Blockchain()
        self.registered_voters = self.load_voter_data()

        for voter_id_hash in self.registered_voters:
            self.blockchain.add_voter(voter_id_hash)

        # Predefined candidate names
        self.candidates = ["Candidate A", "Candidate B", "Candidate C"]

        self.master.title("Voting System")
        self.master.geometry("400x400")
        self.master.configure(bg="#f0f8ff")  # Light background color

        tk.Label(master, text="Enter your Voter ID:", bg="#f0f8ff", font=("Arial", 12)).pack(pady=10)
        self.voter_id_entry = tk.Entry(master, font=("Arial", 12), width=25)
        self.voter_id_entry.pack(pady=5)

        tk.Label(master, text="Select candidate:", bg="#f0f8ff", font=("Arial", 12)).pack(pady=10)
        self.candidate_combobox = ttk.Combobox(master, values=self.candidates, font=("Arial", 12))
        self.candidate_combobox.pack(pady=5)

        self.vote_button = tk.Button(master, text="Cast Vote", command=self.cast_vote, bg="#4CAF50", fg="white", font=("Arial", 12))
        self.vote_button.pack(pady=20)

        self.results_button = tk.Button(master, text="Show Results", command=self.show_results, bg="#2196F3", fg="white", font=("Arial", 12))
        self.results_button.pack(pady=5)

        self.view_blockchain_button = tk.Button(master, text="View Blockchain", command=self.view_blockchain, bg="#FF9800", fg="white", font=("Arial", 12))
        self.view_blockchain_button.pack(pady=5)

        self.explanation_button = tk.Button(master, text="How Blockchain Works", command=self.show_explanation, bg="#9C27B0", fg="white", font=("Arial", 12))
        self.explanation_button.pack(pady=5)

    def cast_vote(self):
        voter_id = self.voter_id_entry.get()
        candidate = self.candidate_combobox.get()

        if not voter_id or not candidate:
            messagebox.showwarning("Input Error", "Please fill in all fields.")
            return

        try:
            self.blockchain.cast_vote(voter_id, candidate)
            messagebox.showinfo("Success", "Vote cast successfully!")
            self.voter_id_entry.delete(0, tk.END)
            self.candidate_combobox.set('')  # Clear selection
        except Exception as e:
            messagebox.showwarning("Error", str(e))

    def show_results(self):
        results = self.blockchain.show_results()
        messagebox.showinfo("Voting Results", results)

    def view_blockchain(self):
        chain_data = self.blockchain.get_chain_data()
        blockchain_info = ""
        for block in chain_data:
            blockchain_info += (f"Index: {block['Index']}\n"
                                f"Previous Hash: {block['Previous Hash']}\n"
                                f"Timestamp: {block['Timestamp']}\n"
                                f"Data: {block['Data']}\n"
                                f"Hash: {block['Hash']}\n\n")
        if not blockchain_info:
            blockchain_info = "The blockchain is empty."
        messagebox.showinfo("Blockchain Information", blockchain_info)

    def show_explanation(self):
        explanation = (
            "How Blockchain Works:\n\n"
            "1. A block contains data, a timestamp, and a hash of the previous block.\n"
            "2. Each block is linked to the previous one, forming a chain.\n"
            "3. Once data is recorded in a block, it cannot be altered without changing all subsequent blocks.\n"
            "4. This structure ensures transparency and security, making it tamper-proof.\n"
            "5. In the context of voting, this means every vote is securely recorded and cannot be changed."
        )
        messagebox.showinfo("Blockchain Explanation", explanation)

    def load_voter_data(self):
        voters = []
        try:
            with open('voter_data.json', 'r') as f:
                for line in f:
                    voter_info = json.loads(line.strip())
                    voters.append(voter_info['voter_id_hash'])  # Append only the voter ID hash
        except FileNotFoundError:
            return []
        return voters


if __name__ == "__main__":
    root = tk.Tk()
    app = VotingApp(root)
    root.mainloop()
