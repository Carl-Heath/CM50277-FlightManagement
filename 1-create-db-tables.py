import sqlite3


# This script creates a flight management database with five tables

# Connect to the database (will create if does not exist)
conn = sqlite3.connect("flight_mgmt.db")
c = conn.cursor()

print("Creating flight_mgmt.db database")

# Create airline table
print("Creating airline table")
c.execute('''
CREATE TABLE airline (
    airlineId INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    iataCode TEXT NOT NULL,
    icaoCode TEXT NOT NULL,
    countryOfOrigin TEXT NOT NULL,
    headquarters TEXT NOT NULL
)
''')

# Create airplane table
print("Creating airplane table")
c.execute('''
CREATE TABLE airplane (
    airplaneId INTEGER PRIMARY KEY,
    registrationNumber TEXT NOT NULL,
    model TEXT NOT NULL,
    manufacturer TEXT NOT NULL,
    capacity INTEGER NOT NULL,
    manufactureYear INTEGER NOT NULL,
    lastMaintenance DATE NOT NULL,
    airlineId INTEGER NOT NULL,
    FOREIGN KEY (airlineId) REFERENCES airline (airlineId)
)
''')

# Create pilot table
print("Creating pilot table")
c.execute('''
CREATE TABLE pilot (
    pilotId INTEGER PRIMARY KEY,
    firstName TEXT NOT NULL,
    lastName TEXT NOT NULL,
    licenseNumber TEXT NOT NULL,
    flyingHours INTEGER NOT NULL,
    licenseExpiry DATE NOT NULL,
    airlineId INTEGER NOT NULL,
    FOREIGN KEY (airlineId) REFERENCES airline (airlineId)
)
''')

# Create airport table
print("Creating airport table")
c.execute('''
CREATE TABLE airport (
    airportId INTEGER PRIMARY KEY,
    code TEXT NOT NULL,
    name TEXT NOT NULL,
    city TEXT NOT NULL,
    country TEXT NOT NULL,
    timezone TEXT NOT NULL
)
''')

# Create flight table
print("Creating flight table...")
c.execute('''
CREATE TABLE flight (
    flightId INTEGER PRIMARY KEY,
    flightNumber TEXT NOT NULL,
    departureTime DATETIME NOT NULL,
    arrivalTime DATETIME NOT NULL,
    status TEXT NOT NULL,
    terminal TEXT NOT NULL,
    gate TEXT NOT NULL,
    airplaneId INTEGER NOT NULL,
    departureAirportId INTEGER NOT NULL,
    arrivalAirportId INTEGER NOT NULL,
    pilotId INTEGER NOT NULL,
    airlineId INTEGER NOT NULL,
    FOREIGN KEY (airplaneId) REFERENCES airplane (airplaneId),
    FOREIGN KEY (departureAirportId) REFERENCES airport (airportId),
    FOREIGN KEY (arrivalAirportId) REFERENCES airport (airportId),
    FOREIGN KEY (pilotId) REFERENCES pilot (pilotId),
    FOREIGN KEY (airlineId) REFERENCES airline (airlineId)
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database created successfully!")
print("Created tables: airline, airplane, pilot, airport, flight")

