# Simple Security Information and Event Management (SIEM)

## Description
This project is a simple implementation of a Security Information and Event Management (SIEM) system that allows for the management and monitoring of security logs on a network. It enables users to read system logs, filter important events, and save them for analysis.

## Features
- Read system logs from the Event Viewer.
- Filter logs based on event types (Critical, Error).
- Save filtered logs to a text file in UTF-8 encoding.

## Installation
To run this project, ensure you have Python 3.x installed on your machine. You will also need to install the required libraries.

1. Clone the repository:
   ```bash
   git clone https://github.com/Nelzouki22/SIEM.git
   cd SIEM
Install the required libraries:
pip install wmi
Usage
Open the terminal and navigate to the project directory.

Run the script:
python event_log_reader.py
The program will read system logs and display filtered events (based on the specified event type).

The logs will be saved to event_logs.txt.

Customization
You can customize the type of events to filter by modifying the event_type variable in the main function of the script:
event_type = 'Critical'  # Change to 'Error' or None for all events
Contributing
Contributions are welcome! Please create a pull request for any improvements or bug fixes.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
For any inquiries or feedback, please contact:

LinkedIn: Nadir Elzouki
YouTube: Nadir Elzouki
GitHub: Nelzouki22

### Instructions to Add the Updated README.md
1. Replace the existing `README.md` file in your project directory with this updated content.
2. Save the changes and commit your updates.
3. Push the changes to your GitHub repository:
   ```bash
   git add README.md
   git commit -m "Update README.md with contact information"
   git push origin main  # or your branch name
