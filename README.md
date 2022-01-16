# cloud-computing-class

Lab exercises for the Birkbeck MSc CompSci Cloud Computing module

Each week is separated into a different folder, labelled week1, week2 etc.

## Week 1

I've added remote SSH to my VSCode install, but I'm just using SSH directly from my WSL setup, as editing files directly on a cloud VM is uncomfortable. If I do want to use VSCode remote editing on cloud VMs, I may need to either create a new key within Windows, or pull an existing key from e.g. `\\wsl.localhost\Ubuntu\home\daniel\.ssh`.

I have $50 GCP applied to my own Google account, and can get $100 on university Azure.

Week 1 lab is manually setting up a Python script on a cloud VM, running the script to generate a JSON output file, and making that output file available through Apache webserver. Then running another Python script on local that pulls that JSON data from the VM endpoint, parses the data and prints some results to stdout. Because the VM's assigned IP is dynamic, we have to manually enter the endpoint as an argument to the local script in order for it to know where the endpoint actually is.

### Sample usage

These are the actual command line logs from a successful run. I used git to clone the repo to the cloud VM, and manually copied the VM's IP from GCP web console.

Remote VM shell:

```sh
dan@week1:~/cloud-computing-class$ sudo python3 week1/generator.py
dan@week1:~/cloud-computing-class$ ls /var/www/html/
data.json  index.html
dan@week1:~/cloud-computing-class$ cat /var/www/html/data.json
{"server0": 87, "server1": 47, "server2": 61, "server3": 38, "server4": 74, "server5": 75, "server6": 5, "server7": 5, "server8": 86, "server9": 0}
```

Local shell:

```sh
daniel@DAN-XPS-15:~/cloud-computing-class$ python3 week1/collector.py http://34.132.184.106/data.json
server0 87
server1 47
server2 61
server3 38
server4 74
server5 75
server6 5
server7 5
server8 86
server9 0
{'under': 5, 'over': 5}
```
