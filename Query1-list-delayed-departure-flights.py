import sqlite3

# Connect to database
conn = sqlite3.connect("flight_mgmt.db")
c = conn.cursor()

# Find delayed flights
c.execute("""
SELECT status, flightNumber, departureTime, code, city
FROM flight, airport 
WHERE status = 'Delayed' AND arrivalAirportId = airportId
""")

# Print each flight
for flight in c.fetchall():
    print("Status:", flight[0])
    print("Flight:", flight[1])
    print("Departure:", flight[2])
    print("Destination:", flight[3], "-", flight[4])
    print()

# Close connection
conn.close()