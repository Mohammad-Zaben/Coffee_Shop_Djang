# import threading
#
# import threading
#
# counter = 0
# lock = threading.Lock()
#
# def increment():
#     global counter
#     for _ in range(100000):
#         with lock:  # Locking the critical section
#             counter += 1
#
# # Create two threads
# thread1 = threading.Thread(target=increment)
# thread2 = threading.Thread(target=increment)
#
# # Start the threads
# thread1.start()
# thread2.start()
#
# # Wait for both threads to finish
# thread1.join()
# thread2.join()
#
# print(counter)

import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(1000000):  # Increase the number of iterations
        with lock:  # Critical section protected by the lock
            counter += 1

def increment_without_lock():
    global counter
    for _ in range(1000000):
        counter += 1

# Test without lock
counter = 0
thread1 = threading.Thread(target=increment_without_lock)
thread2 = threading.Thread(target=increment_without_lock)

thread1.start()
thread2.start()
thread1.join()
thread2.join()

print(f"Without Lock: {counter}")

# Test with lock
counter = 0
thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=increment)

thread1.start()
thread2.start()
thread1.join()
thread2.join()

print(f"With Lock: {counter}")
