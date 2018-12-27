#!/usr/bin/env python
# -*- coding: utf-8 -*-

# simon.clematide@uzh.ch
# PCL I
#

while True:
    x = raw_input('Please type in a number: ')
    try:
        float(x)
        print "from 1: "
        break
        print "from 2: "
    except ValueError:
        print "from 3: "
        pass
        print "from 4: "
    finally:
        print "from 5: "

print "The number was:", x


# Please type in a number: null
# from 3:
# from 4:
# from 5:
# Please type in a number: eins
# from 3:
# from 4:
# from 5:
# Please type in a number: 7,78
# from 3:
# from 4:
# from 5:
# Please type in a number: 90.25
# from 1:
# from 5:
# The number was: 90.25