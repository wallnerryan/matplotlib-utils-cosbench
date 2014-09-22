import csv, sys, re
import datetime as dt
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import dates
import __main__ as main


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 2:
	print "usage: %s <filename.csv>" % main.__file__ 
        exit()
    try:
	f = open(args[1], 'rU')
    except Exception as e:
	print "could not open file, %s" % e
	exit()

#plot X-Axis  = timestamp 
#plot Y-Axis = bandwidth
x, y = [],[]

#open file
csv_r = csv.reader(f)

for line in csv_r:
    if "Timestamp" in line[0]:
        continue
    if len(line[0]) < 1:
	continue 
    x.append(dt.datetime.strptime(line[0], '%H:%M:%S'))
    y.append(long(("%.0f" % float(((float(line[5]) / 1024)) / 1024))))

fig = plt.figure(figsize=(5.5,6))
ax = fig.add_subplot(111)
ax.set_ylim(0,250)
fig.subplots_adjust(bottom=0.15)
ax.plot(x,y,'b-o')
plt.ylabel('MegaBytes per/s')
plt.xlabel("Time")
plt.xticks(rotation=45)
s = re.search(r'\/(.*)\.', args[1]).group()
fig.savefig("./figures/%s_%s.png" % (str(__file__), s))
