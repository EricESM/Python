#import sys
#ys.path.append(".")
from stack_library import stack
from queue_library import queue

if __name__ == '__main__':

	op = 99
	x = 99
	print "\nWhich would you like to test:"
	print "1. Stack"
	print "2. Queue"

	op = input()

	if op == 1:

		test = stack.stack()

		while x != 8:
			print "\n Stack: "
			print "1. Push"
			print "2. pop"
			print "3. peak"
			print "4. size"
			print "5. is_empty"
			print "6. empty"
			print "7. print the stack"
			x = input()

			if x == 1: # push
				print "Please insert a character/number"
				y = input()
				test.push(y)
			if x == 2: # pop
				print test.pop(), "have been pop"
			if x == 3: # peak
				print "Top of the stack is: ",test.peak()
			if x == 4: # size
				print "Size of the stack is: ",test.size()
			if x == 5: # is_empty
				if test.is_empty() == True:
					print " Stack is empty."
				else:
					print " Stack is not empty."
			if x == 6: # empty
				test.empty()
				print "\n Stack is empty now!"
			if x == 7: # print the stack
				test.print_stack()

	elif op == 2:

		
		test = queue.queue()

		while x != 8:
			print "\n Queue: "
			print "1. Push"
			print "2. pop"
			print "3. peak"
			print "4. size"
			print "5. is_empty"
			print "6. empty"
			print "7. print the Queue"

			x = input()

			if x == 1: # push
				print "Please insert a character/number"
				y = input()
				test.push(y)

			if x == 2: # pop
				print test.pop(), "have been pop"
			if x == 3: # peak
				print "Head of the queue is: ",test.peak()
			if x == 4: # size
				print "Size of the queue is: ",test.size()
			if x == 5: # is_empty
				if test.is_empty() == True:
					print " Queue is empty."
				else:
					print " Queue is not empty."
			if x == 6: # empty
				test.empty()
				print "\n Queue is empty now!"
			if x == 7: # print the stack
				test.print_queue()		
			