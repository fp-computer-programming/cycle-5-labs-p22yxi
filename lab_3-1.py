# Author Yongdong Xi (Oct 25 2021)

import time
import math
start_t1 = time.process_time()
math.pow(2, 2)
end_t1 = time.process_time()
print(end_t1 - start_t1)

start_t2 = time.process_time()
(2 ** 2)
end_t2 = time.process_time()
print(end_t2 - start_t2)

print((end_t1 - start_t1) - (end_t2 - start_t2))

