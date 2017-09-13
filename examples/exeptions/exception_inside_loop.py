# -*- coding: utf-8 -*-

# This section dont finish iteration
# exception is raised
#
# test = ["1", "2", "1/0", "3", "1/0"]
# for t in test:
#    print(eval(t))

# This section finish iteration

test = ["1", "2", "1/0", "3", "1/0"]
for t in teste:
    try:
        print(eval(t))
    except:
        continue

