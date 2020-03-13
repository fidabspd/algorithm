jobs = [[0, 3], [1, 9], [2, 6]]
# return 9

import numpy as np
import heapq as hq
jobs = np.array(jobs)
start = hq.heapify(jobs[:, 0])
run = hq.heapify(jobs[:, 1])

now = 0

for idx in range(len(jobs)):
    now = hq.heappop(start)




import heapq as hq
now = 0
jobs = hq.heapify(jobs)
start, run = hq.heappop(jobs)