import json
import random

# TODO: According to the labs guidance, the output file needs to be saved as a
# sudoer

# Generate the servers status as a Python dict
servers_status = {}
for i in range(10):
    servers_status.update({f'server{i}': random.randint(0, 100)})

# Convert the Python dict to a JSON-encoded string
json_servers_status = json.dumps(servers_status)

# Output the string to a file
# WARNING: The output path is hardcoded, in a way that may be incompatible with
# other file systems.
with open('/var/www/html/data.json', 'x') as file:
    file.write(json_servers_status)
