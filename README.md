# cloud-computing-class

Lab exercises for the Birkbeck MSc CompSci Cloud Computing module

Each week is separated into a different folder, labelled week1, week2 etc.

## Notes from week 1

I've added remote SSH to my VSCode install, but may not use it as it doesn't work well alongside my WSL setup, which has its own remote system. If I do want to use it, I may need to either create a new key within Windows, or pull an existing key from e.g. `\\wsl.localhost\Ubuntu\home\daniel\.ssh`.

I have $50 GCP applied to my own Google account, and can get $100 on university Azure.

Week 1 lab is manually setting up a Python script on a cloud VM, running the script to generate a JSON output file, and making that output file available through Apache webserver. Then running another Python script on local that pulls that JSON data from the VM endpoint, parses the data and prints some results to stdout. Because the VM's assigned IP is dynamic, we have to manually enter the IP into the local script in order for it to know where the endpoint actually is.
