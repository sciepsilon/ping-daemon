# Ping nytimes.com every 10 seconds for a week.
# On each ping, print out the UTC time and the ping latency. 

# Run with: 
# sudo python ping.py
# Tested with python 3.7. 

import datetime
from ping3 import ping
import time

for _ in range(8640*7):
    # Output per 10s
    response = ping("nytimes.com")
    print(datetime.datetime.utcnow(), response)
    time.sleep(10)