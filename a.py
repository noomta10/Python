def UnknownFunc2(x):

    i=1

set basket 0

set flag True

while (flag=True)

set flag False

while (i <=len(x) – 1)

if (x[i] < x[i + 1])

set basket x[i]

set x[i] x[i+1]

set x[i+1] basket

set flag True

set i i+1

set i 1

print x