import sqlite3

# Connect to the database
print("Connecting to database")
conn = sqlite3.connect("flight_mgmt.db")
c = conn.cursor()

# Add airlines
print("Adding airlines")
airlines = [
    (1, 'American Airlines', 'AA', 'AAL', 'United States', 'New York'),
    (2, 'Global Air', 'GA', 'GLB', 'United Kingdom', 'London'),
    (3, 'Pacific Connect', 'PC', 'PCF', 'Australia', 'Sydney'),
    (4, 'Scandinavian Airlines', 'SK', 'SAS', 'Sweden', 'Stockholm'),
    (5, 'Japan Airlines', 'JL', 'JAL', 'Japan', 'Tokyo'),
    (6, 'Maple Jet', 'MJ', 'MPL', 'Canada', 'Toronto'),
    (7, 'Iberian Sky', 'IS', 'IBK', 'Spain', 'Madrid'),
    (8, 'Emirates', 'EK', 'UAE', 'United Arab Emirates', 'Dubai'),
    (9, 'Lufthansa', 'LH', 'DLH', 'Germany', 'Frankfurt'),
    (10, 'Singapore Airlines', 'SQ', 'SIA', 'Singapore', 'Singapore')
]

# Add all airlines at once
for airline in airlines:
    try:
        c.execute("INSERT INTO airline VALUES (?, ?, ?, ?, ?, ?)", airline)
    except:
        print("Error adding airline")

# Add airports
print("Adding airports")
airports = [
    (1, 'JFK', 'John F. Kennedy International Airport', 'New York', 'United States', 'UTC-5'),
    (2, 'LHR', 'Heathrow Airport', 'London', 'United Kingdom', 'UTC+0'),
    (3, 'SYD', 'Sydney Airport', 'Sydney', 'Australia', 'UTC+10'),
    (4, 'ARN', 'Stockholm Arlanda Airport', 'Stockholm', 'Sweden', 'UTC+1'),
    (5, 'HND', 'Haneda Airport', 'Tokyo', 'Japan', 'UTC+9'),
    (6, 'LAX', 'Los Angeles International Airport', 'Los Angeles', 'United States', 'UTC-8'),
    (7, 'CDG', 'Charles de Gaulle Airport', 'Paris', 'France', 'UTC+1'),
    (8, 'DXB', 'Dubai International Airport', 'Dubai', 'United Arab Emirates', 'UTC+4'),
    (9, 'YYZ', 'Toronto Pearson International Airport', 'Toronto', 'Canada', 'UTC-5'),
    (10, 'MAD', 'Madrid-Barajas Airport', 'Madrid', 'Spain', 'UTC+1')
]

for airport in airports:
    try:
        c.execute("INSERT INTO airport VALUES (?, ?, ?, ?, ?, ?)", airport)
    except:
        print("Error adding airport")

# Add airplanes
print("Adding airplanes")
airplanes = [
    (1, 'A12345', '737-300', 'Boeing', 189, 2018, '2023-11-15', 1),
    (2, 'B67890', 'A320-100', 'Airbus', 180, 2020, '2023-12-05', 1),
    (3, 'C12345', '787-400', 'Boeing', 290, 2019, '2023-10-30', 2),
    (4, 'D67890', 'A320-200', 'Airbus', 325, 2021, '2023-11-20', 2),
    (5, 'E12345', '737-500', 'Boeing', 149, 2017, '2023-09-18', 3),
    (6, 'F67890', 'A320-300', 'Airbus', 220, 2022, '2023-12-10', 4),
    (7, 'G12345', 'A320-400', 'Boeing', 386, 2016, '2023-10-25', 5),
    (8, 'H67890', 'A320-500', 'Airbus', 160, 2021, '2023-11-05', 6),
    (9, 'I12345', 'A320-600', 'Airbus', 297, 2019, '2023-12-15', 7),
    (10, 'J67890', '737-600', 'Boeing', 302, 2015, '2023-10-10', 8)
]

for airplane in airplanes:
    try:
        c.execute("INSERT INTO airplane VALUES (?, ?, ?, ?, ?, ?, ?, ?)", airplane)
    except:
        print("Error adding airplane")

# Add pilots
print("Adding pilots")
pilots = [
    (1, 'James', 'Wilson', 'P102938', 8500, '2025-06-30', 1),
    (2, 'Sarah', 'Johnson', 'P293847', 6200, '2026-03-15', 1),
    (3, 'Michael', 'Jackson', 'P384756', 12000, '2025-09-22', 2),
    (4, 'Emma', 'Wilson', 'P475865', 5800, '2024-12-10', 2),
    (5, 'Daniel', 'Chen', 'P567894', 9400, '2025-08-05', 3),
    (6, 'Anna', 'Crow', 'P678903', 7100, '2026-01-18', 4),
    (7, 'Takashi', 'Yamamoto', 'P789012', 11000, '2025-05-12', 5),
    (8, 'Jean', 'VanDame', 'P890123', 7600, '2025-11-28', 6),
    (9, 'Roberto', 'Carlos', 'P901234', 8900, '2026-02-15', 7),
    (10, 'Mohammed', 'Khan', 'P012345', 10200, '2025-07-20', 8)
]

for pilot in pilots:
    try:
        c.execute("INSERT INTO pilot VALUES (?, ?, ?, ?, ?, ?, ?)", pilot)
    except:
        print("Error adding pilot")

# Add flights
print("Adding flights")
flights = [
    (1, 'SA101', '2025-04-05 08:00:00', '2025-04-05 11:30:00', 'Departed', 'Terminal 4', 'Gate A15', 1, 1, 2, 1, 1),
    (2, 'SA202', '2025-04-05 14:00:00', '2025-04-06 10:30:00', 'Delayed', 'Terminal 1', 'Gate C7', 2, 1, 3, 2, 1),
    (3, 'GA505', '2025-04-05 09:15:00', '2025-04-05 12:45:00', 'Departed', 'Terminal D', 'Gate B12', 3, 2, 1, 3, 2),
    (4, 'GA610', '2025-04-05 16:30:00', '2025-04-06 07:45:00', 'Scheduled', 'Terminal 3', 'Gate S5', 4, 2, 5, 4, 2),
    (5, 'PC333', '2025-04-05 22:00:00', '2025-04-06 16:30:00', 'Delayed', 'Terminal B', 'Gate 52', 5, 3, 6, 5, 3),
    (6, 'NF777', '2025-04-05 12:45:00', '2025-04-05 15:15:00', 'Scheduled', 'Terminal 2', 'Gate K10', 6, 4, 7, 6, 4),
    (7, 'EW888', '2025-04-05 10:30:00', '2025-04-05 15:45:00', 'Scheduled', 'Terminal 3', 'Gate B14', 7, 5, 8, 7, 5),
    (8, 'MJ444', '2025-04-05 13:20:00', '2025-04-05 16:45:00', 'Scheduled', 'Terminal 4', 'Gate C12', 8, 9, 1, 8, 6),
    (9, 'IS999', '2025-04-05 11:00:00', '2025-04-05 13:30:00', 'Scheduled', 'Terminal E', 'Gate K10', 9, 10, 7, 9, 7),
    (10, 'EK200', '2025-04-05 23:45:00', '2025-04-06 05:15:00', 'Scheduled', 'Terminal 5', 'Gate A15', 10, 8, 2, 10, 8)
]

for flight in flights:
    try:
        c.execute("INSERT INTO flight VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", flight)
    except:
        print("Error adding flight")

# Save changes and close connection
conn.commit()
conn.close()

print("Database populated with data")