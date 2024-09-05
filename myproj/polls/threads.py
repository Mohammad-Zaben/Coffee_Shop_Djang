import threading

from myproj.polls.controllers.most_selling_item import selling_item
from myproj.polls.controllers.peek_houres import peek_houres
from myproj.polls.controllers.sales import logic_type

start_date = '2019-04-01'
end_date = '2019-04-18'
sales_outlet_id = 3
t = threading.Thread(target=logic_type, args=(start_date, end_date, sales_outlet_id))
t.start()

t1 = threading.Thread(target=peek_houres, args=(sales_outlet_id,))
t1.start()

t2 = threading.Thread(target=selling_item)
t2.start()


