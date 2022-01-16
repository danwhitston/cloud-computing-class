import sys
import requests

# Parse argument giving the endpoint to call
# WARNING: we carry out no verification, and assume arg's existence
endpoint = sys.argv[1]

# Get data from the endpoint, and convert to a dict
# WARNING: we do not validate incoming data format is JSON
servers_status = requests.get(endpoint).json()

# Count the servers in each category
# WARNING: we do not validate incoming data has numeric values
status_summary = {"under": 0, "over": 0}
for server_name in servers_status:
    print(f'{server_name} {servers_status[server_name]}')
    if servers_status[server_name] < 50:
        status_summary["under"] += 1
    else:
        status_summary["over"] += 1

# Print the parsed data and summary data to stdout
print(status_summary)
