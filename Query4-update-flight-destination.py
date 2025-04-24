import sqlite3

# Connect to database
conn = sqlite3.connect("flight_mgmt.db")
c = conn.cursor()

# View current destination of flight NF777
c.execute("""
SELECT code, name, city
FROM flight, airport
WHERE flightNumber = 'NF777'
AND arrivalAirportId = airportId
""")

current_dest = c.fetchone()
print("Flight NF777 is currently going to:", current_dest[0], "-", current_dest[2])

# Find JFK airport ID
c.execute("SELECT airportId FROM airport WHERE code = 'JFK'")
jfk_id = c.fetchone()[0]

# Update flight destination to JFK using paramaterisation 
c.execute("""
UPDATE flight
SET arrivalAirportId = ?
WHERE flightNumber = 'NF777'
""", (jfk_id,))

# Save changes
conn.commit()

# Check new destination
c.execute("""
SELECT code, name, city
FROM flight, airport
WHERE flightNumber = 'NF777'
AND arrivalAirportId = airportId
""")

new_dest = c.fetchone()
print("Flight NF777 is now going to:", new_dest[0], "-", new_dest[2])

# Close connection
conn.close()