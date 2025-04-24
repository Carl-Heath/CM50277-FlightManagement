import sqlite3

# Connect to database
conn = sqlite3.connect("flight_mgmt.db")
c = conn.cursor()

# Find pilot Daniel Chen's ID
c.execute("""
SELECT pilotId 
FROM pilot 
WHERE firstName = 'Daniel' 
AND lastName = 'Chen'
""")
pilot_id = c.fetchone()[0]

# Update the flight with pilotId
c.execute("""
UPDATE flight 
SET pilotId = " + str(pilot_id) + " 
WHERE flightNumber = 'GA610'
""")

# Save changes
conn.commit()

# Get flight info
c.execute("""
SELECT departureTime, terminal, gate, code 
FROM flight, airport 
WHERE flightNumber = 'GA610' 
AND departureAirportId = airportId
""")
flight_info = c.fetchone()

# Print information
print("Flight GA610 is now assigned to pilot Daniel Chen")
print("Leaves at:", flight_info[0])
print("Terminal:", flight_info[1])
print("Gate:", flight_info[2])
print("Airport:", flight_info[3])

# Close connection
conn.close()