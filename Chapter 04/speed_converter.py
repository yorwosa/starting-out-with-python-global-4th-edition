# This program converts the speeds 60 kph
# through 130 kph (in 10 kph increments)
# to mph.

start_speed = 60            # Starting speed
end_speed = 131             # Ending speed
increment = 10              # Speed increment
conversion_factor = 0.6214  # Conversion factor

# Print the table headings.
print('KPH\tMPH')
print('--------------')

# Print the speeds.
for kph in range(start_speed, end_speed, increment):
    mph = kph * conversion_factor
    print(kph, '\t', format(mph, '.1f'))

