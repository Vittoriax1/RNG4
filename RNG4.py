import random
import time

# Obtain the current time in seconds since the epoch
current_time = int(time.time())

# Use the current time as the seed for the random number generator
random.seed(current_time)

# Generate a random integer between 1 and 99999
random_int = random.randint(1, 99999)
print(random_int)
