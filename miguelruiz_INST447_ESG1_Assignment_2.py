import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

insta = pd.read_csv('InstacartOrdersByDepartment-Spring2021.csv')

orders = []
all_hours = range(24)
for num in all_hours:
    hours = insta[insta['order_hour_of_day'] == num].reset_index()
    hours = hours.drop([0,1,3,5,11,12,14,15,17,18])
    hours = hours.sort_values(by='department', ignore_index=True)
    hours = hours.drop('index', axis=1)
    hours.columns = ['order_hour_of_day', 'department', 'total_orders', 'total_dept_orders']
    col = hours.columns.tolist()
    col = ['department', 'order_hour_of_day', 'total_orders', 'total_dept_orders']
    hours = hours[col]
    orders.append(hours)
    
all_dept_orders = orders[0][['department', 'total_dept_orders']]

all_orders_long = pd.concat([orders[0],orders[1],orders[2],orders[3],orders[4],orders[5],
                    orders[6],orders[7],orders[8],orders[9],orders[10],orders[11],
                    orders[12],orders[13],orders[14],orders[15],orders[16],orders[17],
                    orders[18],orders[19],orders[20],orders[21],orders[22],orders[23]])
all_orders_long.columns = ['department', 'hours', 'total orders', 'total_dept_orders']
all_orders_long = all_orders_long.drop('total_dept_orders', axis=1).reset_index()
all_orders_long = all_orders_long.drop('index', axis=1)


fig, ax = plt.subplots(3, figsize=(15, 15))
fig.subplots_adjust(hspace=0.4)

ax[0].scatter(all_orders_long['hours'], all_orders_long['total orders'])
ax[0].set_title("All orders from midnight to eleven PM")
ax[0].set_xlabel("HOURS (24-HOUR CLOCK)")
ax[0].set_ylabel("ORDERS")

ax[1].scatter(all_orders_long['department'], all_orders_long['total orders'])
ax[1].set_title("Every order from each department")
ax[1].set_xlabel("DEPARTMENTS")
ax[1].set_ylabel("ORDERS")

ax[2].scatter(all_dept_orders['department'], all_dept_orders['total_dept_orders'])
ax[2].set_title("Total department orders")
ax[2].set_xlabel("DPARTMENTS")
ax[2].set_ylabel("TOTAL ORDERS")
plt.show()


orders06_x = all_orders_long[all_orders_long['hours'].apply(lambda x: int(x)) < 7]['hours']
orders06_y = all_orders_long[all_orders_long['hours'].apply(lambda x: int(x)) < 7]['total orders']

plt.figure(figsize=(15, 5))
plt.scatter(orders06_x, orders06_y)
plt.title("Orders between midnight and six AM")
plt.xlabel("HOURS (24-HOUR CLOCK)")
plt.ylabel("ORDERS")
plt.show()

orders126_less1k = all_orders_long[(all_orders_long['total orders'].apply(lambda x: int(x)) <= 1000) &
                                   (all_orders_long['hours'].apply(lambda x: int(x)) < 7)]

display(all_orders_long[all_orders_long['hours'].apply(lambda x: int(x)) < 7].
       groupby('department')['total orders'].agg('sum').reset_index())
display(all_orders_long[all_orders_long['hours'].apply(lambda x: int(x)) < 7].
       groupby('hours')['total orders'].agg('sum').reset_index())

grouped_orders126_hours = orders126_less1k.groupby('department')['hours'].agg('count').reset_index()

orders126_less1k[orders126_less1k['department'] == 'dairy eggs']

orders126_less1k[orders126_less1k['department'] == 'produce']

grouped_orders126_total = orders126_less1k.groupby('department')['total orders'].agg('sum').reset_index()

orders126_greater1k = all_orders_long[(all_orders_long['total orders'].apply(lambda x: int(x)) > 1000) &
                                      (all_orders_long['hours'].apply(lambda x: int(x)) < 7)]

orders126_greater1k[orders126_greater1k['department']=='dairy eggs']

orders126_greater1k[orders126_greater1k['department']=='produce']

grouped_orders126_greater1k_total = orders126_greater1k.groupby('department')['total orders'].agg('sum').reset_index()

orders715_x = all_orders_long[(all_orders_long['hours'].apply(lambda x: int(x)) > 6) &
                              (all_orders_long['hours'].apply(lambda x: int(x)) < 16)]['hours']
orders715_y = all_orders_long[(all_orders_long['hours'].apply(lambda x: int(x)) > 6) &
                              (all_orders_long['hours'].apply(lambda x: int(x)) < 16)]['total orders']

plt.figure(figsize=(15,5))
plt.scatter(orders715_x, orders715_y)
plt.title("Orders between seven AM and three PM")
plt.xlabel("HOURS (24-HOUR CLOCK)")
plt.ylabel("ORDERS")
plt.show()


orders715_lesstenk = all_orders_long[(all_orders_long['total orders'].apply(lambda x: int(x)) <= 10000) &
                                     (all_orders_long['hours'].apply(lambda x: int(x)) > 6) &
                                     (all_orders_long['hours'].apply(lambda x: int(x)) < 16)]
orders715_lesstenk

display(all_orders_long[(all_orders_long['hours'].apply(lambda x: int(x)) > 6) &
                       (all_orders_long['hours'].apply(lambda x: int(x)) < 16)].
       groupby('department')['total orders'].agg('sum').reset_index())
display(all_orders_long[(all_orders_long['hours'].apply(lambda x: int(x)) > 6) &
                       (all_orders_long['hours'].apply(lambda x: int(x)) < 16)].
       groupby('hours')['total orders'].agg('sum').reset_index())

grouped_orders715_hours = orders715_lesstenk.groupby('department')['hours'].agg('count').reset_index()

orders715_lesstenk[orders715_lesstenk['department'] == 'snacks']

orders715_lesstenk[orders715_lesstenk['department'] == 'dairy eggs']

grouped_orders715_orders = orders715_lesstenk.groupby('department')['total orders'].agg('sum').reset_index()

orders715_greatertenk = all_orders_long[(all_orders_long['total orders'].apply(lambda x: int(x)) > 10000) & 
                                        (all_orders_long['hours'].apply(lambda x: int(x)) > 6) &
                                        (all_orders_long['hours'].apply(lambda x: int(x)) < 16)]

orders715_greatertenk[orders715_greatertenk['department'] == 'dairy eggs']

orders715_greatertenk[orders715_greatertenk['department'] == 'snacks']

grouped_orders715greater_orders = orders715_greatertenk.groupby('department')['total orders'].agg('sum').reset_index()

orders1623_x = all_orders_long[(all_orders_long['hours'].apply(lambda x: int(x)) > 15) &
                              (all_orders_long['hours'].apply(lambda x: int(x)) < 24)]['hours']
orders1623_y = all_orders_long[(all_orders_long['hours'].apply(lambda x: int(x)) > 15) &
                              (all_orders_long['hours'].apply(lambda x: int(x)) < 24)]['total orders']

plt.figure(figsize=(15,5))
plt.scatter(orders1623_x, orders1623_y)
plt.title("Orders between four PM and eleven PM")
plt.xlabel("HOURS (24-HOUR CLOCK)")
plt.ylabel("ORDERS")
plt.show()


orders411_lesstenk = all_orders_long[(all_orders_long['total orders'].apply(lambda x: int(x)) <= 10000) &
                                     (all_orders_long['hours'].apply(lambda x: int(x)) > 15) & 
                                     (all_orders_long['hours'].apply(lambda x: int(x)) < 24)]
orders411_lesstenk

display(all_orders_long[(all_orders_long['hours'].apply(lambda x: int(x)) > 15) &
                       (all_orders_long['hours'].apply(lambda x: int(x)) < 24)].
       groupby('department')['total orders'].agg('sum').reset_index())
display(all_orders_long[(all_orders_long['hours'].apply(lambda x: int(x)) > 15) &
                       (all_orders_long['hours'].apply(lambda x: int(x)) < 24)].
       groupby('hours')['total orders'].agg('sum').reset_index())

grouped_orders411_hours = orders411_lesstenk.groupby('department')['hours'].agg('count').reset_index()

orders411_lesstenk[orders411_lesstenk['department'] == 'dairy eggs']

orders411_lesstenk[orders411_lesstenk['department'] == 'produce']

grouped_orders411_orders = orders411_lesstenk.groupby('department')['total orders'].agg('sum').reset_index()

orders411_greatertenk = all_orders_long[(all_orders_long['total orders'].apply(lambda x: int(x)) > 10000) &
                                        (all_orders_long['hours'].apply(lambda x: int(x)) > 15) & 
                                        (all_orders_long['hours'].apply(lambda x: int(x)) < 24)]

orders411_greatertenk[orders411_greatertenk['department'] == 'produce']

orders411_greatertenk[orders411_greatertenk['department'] == 'dairy eggs']

grouped_orders411_greater = orders411_greatertenk.groupby('department')['total orders'].agg('sum').reset_index()