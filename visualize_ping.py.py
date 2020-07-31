# Read a file, ping-daemon.out, where each line is a UTC time followed by a 
# space followed by the ping latency at that time in seconds. 
# Show a scatter plot of the data. On the plot, a vertical red line indicates a
# failed ping.   

import matplotlib.pyplot as plt
import numpy as np

f = open("ping-daemon.out", "r")
lines = f.readlines()
pings = [float(val.split()[-1]) if val.split()[-1][1] == "." else 1.0 for val in lines]
npings = np.asarray(pings)
times = [val.split()[-2].split(".")[0] for val in lines]
timelists = [time.split(":") for time in times]
timelists = [[str((int(tl[0]) - 7) % 24), tl[1], tl[2]] for tl in timelists]
times = [":".join(tl) for tl in timelists]
tticks = [times[idx*1000] for idx in range(7)]
nticks = [idx*1000 for idx in range(7)]

plt.xticks(nticks, tticks, rotation=45)
plt.scatter(np.arange(len(npings)), npings, s=1)
for xc in np.arange(len(npings))[npings == 1.0]:
    plt.axvline(x=xc, color='red', lw=0.1)
plt.xlabel("Time (PDT)")
plt.ylabel("Ping (s)")
plt.title("Ping times for NYTimes.com, measured every 10s")
plt.show()