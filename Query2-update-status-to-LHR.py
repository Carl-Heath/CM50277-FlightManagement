import sqlite3

# Connect to the database
conn = sqlite3.connect("flight_mgmt.db")
c = conn.cursor()

# Get the flight numbers that will be updated
c.execute("""
SELECT flightNumber 
FROM flight
WHERE status = 'Scheduled'
AND arrivalAirportId = (SELECT airportId FROM airport WHERE code = 'LHR')
""")

# List and store flight numbers before status update
flights_to_delay = c.fetchall()

# Update flights to LHR from Scheduled to Delayed
c.execute("""
UPDATE flight
SET status = 'Delayed'
WHERE status = 'Scheduled'
AND arrivalAirportId = (SELECT airportId FROM airport WHERE code = 'LHR')
""")

# Get number of flights updated
flights_updated = c.rowcount

# Print details of updated flights
print(flights_updated, "flights to London Heathrow (LHR) have been delayed:")
for flight in flights_to_delay:
    print("Flight", flight[0], "has been delayed")

# Save the changes
conn.commit()

# Close the connection
conn.close()