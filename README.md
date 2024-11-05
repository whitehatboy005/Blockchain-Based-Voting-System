# Blockchain-based Voting System

This project is a Blockchain-based Voting System application built using Python and Tkinter. It uses blockchain technology to ensure the integrity and transparency of the voting process by securely recording each vote in a tamper-proof ledger.

## Features

1. **Blockchain Integration**  
   - Each vote is added as a block to the blockchain, containing a timestamp, candidate choice, and hash of the previous block.
   - Blockchain ensures that once recorded, a vote cannot be altered, providing transparency and immutability.

2. **Voter Registration**  
   - Unique voter IDs are hashed and stored to securely register voters and prevent duplicate votes.
   - Voter information is securely loaded from a `voter_data.json` file.

3. **Vote Casting**  
   - Users enter their Voter ID and select a candidate from predefined options.
   - The system verifies the voter's registration and voting status before allowing a vote to be cast.

4. **Results Display**  
   - After voting, results show the number of votes each candidate received.
   - Results update in real-time as votes are cast.

5. **Blockchain Viewing**  
   - View the blockchain to display each block's details, such as index, timestamp, data (candidate choice), and hash.
   - This transparency enhances trust in the voting process.

6. **Educational Section**  
   - A simple explanation of blockchain technology and its application in this system is provided.

## How to Use

1. **Setup**  
   - Ensure Python is installed along with required dependencies.
   - Run the main script to start the application.

2. **Cast Vote**  
   - Enter a valid Voter ID and choose a candidate to cast a vote.
   - Each voter can vote only once.

3. **View Results and Blockchain**  
   - Click on "Show Results" to view the voting outcomes.
   - Click on "View Blockchain" to see the chain of blocks and verify each recorded vote.

## Usage

This application serves as a prototype for secure, transparent voting systems. It highlights how blockchain technology can be leveraged to securely manage sensitive data and provide transparent voting records.

## Disclaimer

This application is a demonstration and should not be used in real elections without further security and scalability considerations.
#
## Installation
## Clone the Repository
```bash
git clone https://github.com/whitehatboy005/Blockchain-Based-Voting-System
```
## Move the file
```bash
cd Blockchain-Based-Voting-System
```
## Install Dependencies
```bash
pip install -r requirements.txt
```
## Register the voter ID
```bash
python registration.py
```
## Run the Voting Program
```bash
python voter.py
```
#
## License

This project is licensed under the terms of the [MIT license](LICENSE.md).

