# Blood Bank Management System

A Python-based Blood Bank Management System with GUI and MySQL integration.  
This system allows hospitals and blood banks to manage donors, blood details, and blood requests efficiently.

---

## Features

- **Add Donor**: Enter donor details including name, age, gender, blood group, contact info, and address.  
- **Donor Details**: View the details of registered donors.  
- **Add Blood Info**: Record blood collection information including blood group and units collected.  
- **Request Blood**: Hospitals can request blood and see a list of matching donors.  
- **GUI Interface**: Interactive Tkinter-based interface for ease of use.  
- **Database Integration**: Uses MySQL to store and retrieve all data.

---

## Installation

1. Clone the repository:
   git clone https://github.com/YOUR_USERNAME/BloodBankManagementSystem.git

2. Navigate to the project directory:
cd BloodBankManagementSystem

3. Install required packages:
pip install -r requirements.txt

4. Set up MySQL database:

 CREATE DATABASE db;

CREATE TABLE donors(
    donorID INT PRIMARY KEY,
    name VARCHAR(255),
    gender VARCHAR(10),
    age INT,
    bloodgroup VARCHAR(5),
    address VARCHAR(255),
    contact BIGINT
 );

 CREATE TABLE details(
    donorID INT,
    bloodgroup VARCHAR(5),
    unit INT,
    FOREIGN KEY(donorID) REFERENCES donors(donorID)
 );

5. Run the application:
python main.py


