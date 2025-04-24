import sqlite3

# Connect to database
conn = sqlite3.connect("flight_mgmt.db")
c = conn.cursor()

# Find the next three airplanes due for maintenance in ascending order
c.execute("""
SELECT registrationNumber, model, manufacturer, lastMaintenance
FROM airplane
ORDER BY lastMaintenance ASC
LIMIT 3
""")

# Get the results
maintenance_due = c.fetchall()

# Print the results
print("Next three Airplanes due for maintenance:\n")

for airplane in maintenance_due:
    reg_number = airplane[0]
    model = airplane[1]
    manufacturer = airplane[2]
    last_date = airplane[3]
    
    print("Registration:", reg_number)
    print("Aircraft:", manufacturer, model)
    print("Last Maintenance:", last_date)
    print()

# Close connection
conn.close()