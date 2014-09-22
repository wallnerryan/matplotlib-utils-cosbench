import csv, sys, re
import datetime as dt
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import dates
import __main__ as main


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

#plot X-Axis  = timestamp 
#plot Y-Axis = bandwidth
x, y = [],[]

ticks = 0
if len(args) == 3:
  try:
     ticks = int(args[2])
  except:
     print "Error setting plot-every"
     exit()

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
       x.append(dt.datetime.strptime(line[0], '%H:%M:%S'))
       print dt.datetime.strptime(line[0], '%H:%M:%S')
       y.append(long(("%.0f" % float(line[3]))))
       print long(("%.0f" % float(line[3])))
       n = n+1
    elif n == ticks:
       n = 0
    else:
       n = n+1

fig = plt.figure(figsize=(5.5,6))
ax = fig.add_subplot(111)
ax.set_ylim(0,80)
fig.subplots_adjust(bottom=0.15)
fig.subplots_adjust(left=0.15)
ax.plot(x,y,'b-o')
plt.ylabel('Average REST-Time, milliseconds')
plt.xlabel("Time")
plt.xticks(rotation=45)
s = re.search(r'(.*).', args[1]).group()
fig.savefig("./figures/%s_%s.png" % (str(__file__), s))
