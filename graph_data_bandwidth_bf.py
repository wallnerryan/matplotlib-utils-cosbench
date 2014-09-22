import csv, sys, re
import datetime as dt
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import dates
import __main__ as main
import numpy as np
import time

if __name__ == "__main__":
    args = sys.argv
    if len(args) < 2 or len(args) > 3:
	print "usage: %s <filename.csv> <plot-every-#>" % main.__file__ 
        exit()
    try:
	f = open(args[1], 'rU')
    except Exception as e:
	print "could not open file, %s" % e
	exit()

ticks = 0
if len(args) == 3:
  try:
     ticks = int(args[2])
  except:
     print "Error setting plot-every"
     exit()

#plot X-Axis  = timestamp 
#plot Y-Axis = bandwidth
x, y = [],[]

#open file
csv_r = csv.reader(f)

n = 0
for line in csv_r:
    print line
    if ticks == 0:
       n = 0
    if "Timestamp" in line[0]:
        continue
    if len(line[0]) < 1:
	continue 
    if n == 0:
       print dt.datetime.strptime(line[0], '%H:%M:%S')
       x.append(dt.datetime.strptime(line[0], '%H:%M:%S'))
       print long(("%.0f" % float(((float(line[6]) / 1024)) / 1024)))
       y.append(long(("%.0f" % float(((float(line[6]) / 1024)) / 1024))))
       n = n+1
    elif n == ticks:
       n = 0
    else:
       n = n+1

y = np.array([np.float(i) for i in y])
x = np.array([abs(time.mktime(i.timetuple())) for i in x])
x=x[::-1]

m = np.polyfit(x,y,1)
yfit = np.polyval(m,x)
fig = plt.figure(figsize=(5.5,6))
ax = fig.add_subplot(111, xmargin=0)

#If your bandwidth is higher than 150MB, this will be an issue
# so raise 150 to a higher number.
ax.set_ylim(0,150)
fig.subplots_adjust(bottom=0.15)
ax.plot(x,y,'b-o',x, yfit, 'k')
plt.ylabel('MegaBytes per/s')
plt.xlabel("Time")
plt.xticks(rotation=45)
s = re.search('(.*).', args[1]).group()
fig.savefig("./figures/%s_%s.png" % (str(__file__), s))

