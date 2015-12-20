#!/usr/bin/env python
from sb6141_timeout.pipelines import Item

PURPLE = '\033[95m'
CYAN = '\033[96m'
DARKCYAN = '\033[36m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'

for item in Item.select().order_by(Item.date.desc()):
    if 'T4' in item.message:
        msg = BOLD + RED + 'T4 timeout' + END
    elif 'T3' in item.message:
        msg = 'T3 timeout'
    else:
        msg = item.message
    print('%s - %s' % (item.date, msg))
