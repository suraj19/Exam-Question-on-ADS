#Date: 12-09-18
#ADS-1 Test
#Author: A.Suraj Kumar
'''“Nala-Paka” is well known restaurant which allows on line advance booking of tables. 
There are 2-chair table, 4-chair table and 6-chair tables. If the customer is alone, he/she can reserve only 2-chair table. 
Two customers can reserve 2-chair or 4-chairtable. All reservations can be done for the same day. 
Tables are reserved for duration of one hour and at fixed time slots. Time slots start from morning 7 O’clock to night 10 O’clock. 
The number of tables in each category is fixed and is uniquely numbered like 2T-1, 2T-2 etc. 
for 2-Chair tables and 4T-1 and 6T-1 for 4 and 6-chair tables.Owner has the provision to cancel the bookings and see the status of booking.
System should tell how many tables of various category are booked at the given time slot. There should be also a method which shows tables which are free in various category at the given time slot.'''

import ArrayQueue
two=ArrayQueue.ArrayQueue()
four=ArrayQueue.ArrayQueue()
six=ArrayQueue.ArrayQueue()
def reservation():
	table=int(input('Enter the No of people: '))
	if (table <= 2):
		cust2T1=input('Enter Name: ')
		if (two.size==len(two.data)):
			four.enqueue(cust2T1)
		else:
			two.enqueue(cust2T1)
	elif (table>2 and table<=6):
		opt=int(input('Choose the Table type(4 or 6): '))
		if (opt==4):
			cust4T1=input('Enter Name: ')
			if (four.size==len(four.data)):			
				six.enqueue(cust4T1)
				print('your booking is confirmed')
			else:
				four.enqueue(cust4T1)
				print('your booking is confirmed')
		else:
			if (six.size==len(six.data)): 
				print(' sorry We are out of capacity, we would like to see you next time')			
			else:		
				cust6T1=input('Enter Name: ')
				six.enqueue(cust6T1)
				print('your booking is confirmed')

	else:
		if (six.size==len(six.data)): 
			print(' sorry We are out of capacity, we would like to see you next time')			
		else:		
			cust6T1=input('Enter Name: ')
			six.enqueue(cust6T1)
			print('your booking is confirmed')
	ask=input('Do you want check booking slots(y/n): ')
	yes='y'
	No='n'
	if (ask==yes):
		Admin=input('Enter your Name: ')
		admin_name='Suraj'
		if (Admin==admin_name):
			choose1=input('Do you want to check reservation or cancel a slot(reservation/cancel): ')
			str1='reservation'
			str2='cancel'
			if (choose1==str1):	
				bookedslots()
			elif(shoose==str2):
				cancel()
			else:
				print('Choose proper')

	else:
		print('Thank you for choosing Nala-Paka')

def bookedslots():
	status=int(input('Booking Status of table you want to check(2 or 4 or 6) : '))
	if (status==2):
		slot=two.data.count(None)
		print('Slots vacent for Booking for 2 chaired Table: ',slot)
	elif (status==4):
		slot=four.data.count(None)
		print('Slots vacent for Booking for 4 chaired Table: ',slot)
	elif(status==6):
		slot=four.data.count(None)
		print('Slots vacent for Booking for 6 chaired Table: ',slot)
	else:
		print('You have choosen a wrong option')
def cancel():
	can=input('Do you really want to cancel your booking(Y/N): ')
	if can==Y:
		tabnum=int(input('please enter your table type allaoted(2 or 4 or 6): '))
		if (tabnum==2):
			two.dequeue()
			print('your booking has been cancelled, we would like to see you soon')
		elif(tabnum==4):
			four.dequeue()
			print('your booking has been cancelled, we would like to see you soon')
		elif(tabnum==6):
			six.dequeue()
			print('your booking has been cancelled, we would like to see you soon')
		else:
			print('please Enter the correct Table number')

print('Welcome to Nala-Paka')
choose=input('Are you a customer or Admin: ')
A='Admin'
C='customer'
if (choose==A):
	Admin=input('Enter your Name: ')
	admin_name='Suraj'
	if (Admin==admin_name):
		choose1=input('Do you want to check reservation or cancel a slot(reservation/cancel): ')
		str1='reservation'
		str2='cancel'
		if (choose1==str1):	
			bookedslots()
		elif(shoose==str2):
			cancel()
		else:
			print('Choose proper')
	else:
		print('your credentials are inncorrect')
elif(choose==C):
	customer=input('Do you want to have a reservation of Table(yes/no): ')
	str1='yes'
	str2='no'
	if (customer==str1):
		reservation()
	elif(customer==str2):
		print('we would like to serve you at our restaurant')	
	else:
		print('Please choose Y for Yes or N for No')
else:
	print('Choose Proper Credentials')
	
	
