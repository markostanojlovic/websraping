import sys
rate = float(sys.argv[1])
lower_border = 25.2
higher_border = 25.5
if rate < lower_border or rate > higher_border:
    print 1
else: 
    print 0
