import threading
from item_per_receipt import get_total_items
from spending_per_receipt import get_spending

# Create thread objects
thread1 = threading.Thread(target=get_total_items,args=(3,'2019-04-01','2019-04-08'))
thread2 = threading.Thread(target=get_spending,args=(3, '2019-04-01', '2019-04-08'))

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to complete
thread1.join()
thread2.join()

print('Both threads have completed.')

# Both threads now have their results
