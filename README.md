# Keylogger Script with Discord WebHook

This Python script serves as a basic keylogger, capturing keystrokes and sending them to a specified Discord channel. It uses Discord as the Command and Control (C2) server, enabling remote monitoring of captured keystrokes. To use this script, you need to set up a Discord webhook and paste the webhook URL in the designated variable within the script.

## Setting Up Discord Webhook:

1. **Create a Discord Server:**
   If you don’t have a Discord server, create one to manage your webhook.

2. **Create a Text Channel:**
   Within your server, create a new text channel where the keylogs will be sent.

3. **Create a Webhook:**
   In the channel settings, find the Webhooks section, and create a new webhook. You can customize the webhook name and avatar as desired.

4. **Copy the Webhook URL:**
   After creating the webhook, copy the generated webhook URL. This URL will be pasted into the `WEBHOOK_URL` variable in the Python script.

## Using the Python Script:

1. **Clone the Repository:**
git clone [REPO_URL]

2. **Navigate to the Script Directory:**
cd Keylogger-Discord

3. **Edit the Script:**
Open the `keylogger.py` file and paste your Discord webhook URL in the `WEBHOOK_URL` variable.

4. **Run the Script:**
python keylogger.py

## Script Explanation:

- **WEBHOOK_URL:**
Replace `'YOUR_DISCORD_WEBHOOK_URL'` with your actual Discord webhook URL.

- **send_keylogs():**
Sends captured keylogs to the specified Discord channel every 30 seconds.

- **capture_keystrokes(event):**
Callback function that captures keystrokes and adds them to the keylogs list.

- **Continuous Execution:**
The script runs indefinitely, capturing and sending keylogs with a 1-second delay between iterations.

## Important Notes:

- This script is intended for educational and ethical purposes only.
- Respect privacy and obtain proper authorization before using this script.
- Unauthorized use for malicious intent is illegal and strictly discouraged.

## Disclaimer:

The developers of this script are not responsible for any misuse or damage caused by this tool. Use it responsibly and adhere to legal regulations and ethical standards.
