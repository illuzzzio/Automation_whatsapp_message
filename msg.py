import pywhatkit

# Get user input
phone = input("Phone number with country code (e.g., +1234567890): ")
message = input("Enter the desired message: ")

# Specify the time to send the message
hour = int(input("Enter the hour (24-hour format) to send the message: "))
minute = int(input("Enter the minute to send the message: "))

# Send the message
pywhatkit.sendwhatmsg(phone, message, hour, minute)