#!/usr/bin/env python3
# -*- coding: utf-8 -*-
list2 = []

# A loop that asks the user for his/hers name unless they hit return. The loop will take
# the name push it another loop that will multiply all letters and then reverse it, push
# it to a list and then print it and then clean the list.
while True:
	n = input('What\'s your name?\n')
	if n == '':
		break
	else:
		for l in n:
			b = l * 3
			list2.append(b)
		list2.reverse()
		j=''
		h= j.join(list2)
		print(h)
		list2= []
