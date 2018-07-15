from openerp import models, fields, api, _
from openerp import tools
from decimal import *
import time
import re
from openerp.exceptions import except_orm, Warning, RedirectWarning
from datetime import datetime
import random


class lotto_records(models.Model):
	_name = 'lotto.records'


	game = fields.Char()

	x_a = fields.Char(string='1st Digit')
	x_b = fields.Char(string='2nd Digit')
	x_c = fields.Char(string='3rd Digit')
	x_d = fields.Char(string='4th Digit')
	x_e = fields.Char(string='5th Digit')
	x_f = fields.Char(string='6th Digit')

	a = fields.Integer(string='1st Digit')
	b = fields.Integer(string='2nd Digit')
	c = fields.Integer(string='3rd Digit')
	d = fields.Integer(string='4th Digit')
	e = fields.Integer(string='5th Digit')
	f = fields.Integer(string='6th Digit')

	name = fields.Char(string='Result')
	sorted_name = fields.Char(string='Sorted Result')

	odd = fields.Integer(default=0)
	even = fields.Integer(default=0)

	high = fields.Integer(string='High', default=0)
	low = fields.Integer(string='Low', default=0)

	res_sum = fields.Integer(string='Sum') 

	consecutive = fields.Char(help='Classification of consecutive numbers')

	date_drawn = fields.Date(string='Date')

	month = fields.Char()
	year = fields.Char()
	day = fields.Char()
	day_of_week = fields.Char()

	rel_month = fields.Char(related='month')
	rel_year = fields.Char(related='year')
	rel_day = fields.Char(related='day')
	rel_day_of_week = fields.Char(related='day_of_week')


	def init(self):
		query="""ALTER TABLE lotto_records
			ADD CONSTRAINT unique_date_drawn_in_lotto_records UNIQUE(date_drawn);"""

		try:
			self._cr.execute(query)
		except:
			print 'unique_date_drawn_in_lotto_records already exist!'

	@api.multi
	def quicksort(self,x):
		if len(x) == 1 or len(x) == 0:
			return x
		else:
			pivot = x[0]
			i = 0
			for j in range(len(x)-1):
				if x[j+1] < pivot:
					x[j+1],x[i+1] = x[i+1], x[j+1]
					i += 1
			x[0],x[i] = x[i],x[0]
			first_part = self.quicksort(x[:i])
			second_part = self.quicksort(x[i+1:])
			first_part.append(x[i])
			return first_part + second_part

	@api.multi
	def sort_name(self):
		#print 'sort_name'

		alist = [self.a,self.b,self.c,self.d,self.e,self.f]
		alist = self.quicksort(alist)
		print(alist)
		#alist = self.quicksort(alist)
		#print(alist)
		#print alist[0]
		self.sorted_name = str(alist[0]) + ' - ' + str(alist[1]) + ' - ' + str(alist[2]) + ' - ' + str(alist[3]) + ' - ' + str(alist[4]) + ' - ' + str(alist[5])


	@api.multi
	def get_consecutives(self):
		print 'Get Consecutives...'

		

		for rec in self:
			#apply quicksort in name
			rec.sort_name()

			'''
			print self.a
			print self.b
			print self.c
			print self.d 
			print self.e 
			print self.f 
			'''

			lista = []
			listb = []

			lista.append(rec.a)
			lista.append(rec.b)
			lista.append(rec.c)
			lista.append(rec.d)
			lista.append(rec.e)
			lista.append(rec.f)

			count = len(lista)

			for x in range(len(lista)):
				temp = 99
				for row in lista:
					#print row
					if row < temp:
						temp = row

				#print temp
				listb.append(temp)
				lista.remove(temp)
				#print 'lista ',lista
				#print 'listb ',listb

			temp = 99
			counter = 0
			for row in listb:
				#print {'row ':row, 'temp ':temp}
				if row == temp:
					print 'correct'

					if counter > 0:
						lista.remove(counter)

					counter += 1
					lista.append(counter)


				else:
					counter = 0
				temp = row + 1

			print lista

			if lista == [1,1,1]:
				print 'one_x3'
				rec.consecutive = 'one_x3'
			elif lista == [1,1]:
				print 'one_x2'
				rec.consecutive = 'one_x2'
			elif lista == [1]:
				print 'one'
				rec.consecutive = 'one'
			elif lista == [1,2]:
				print 'one_two'
				rec.consecutive = 'one_two'
			elif lista == [1,3]:
				print 'one'
				rec.consecutive = 'one'
			elif lista == [2]:
				print 'two'
				rec.consecutive = 'two'
			elif lista == [2,1]:
				print 'one_two'
				rec.consecutive = 'one_two'
			elif lista == [2,2]:
				print 'two_x2'
				rec.consecutive = 'two_x2'
			elif lista == [3]:
				print 'three'
				rec.consecutive = 'three'
			elif lista == [3,1]:
				print 'three_one'
				rec.consecutive = 'three_one'
			elif lista == [4]:
				print 'four'
				rec.consecutive = 'four'
			elif lista == [5]:
				print 'five'
				rec.consecutive = 'five'
			else:
				print 'zero'
				rec.consecutive = 'zero'

	@api.onchange('date_drawn')
	def  _onchange_date(self):
		print '_onchange_date '
		if self.date_drawn:
			#print self.date_drawn
			#self.month = datetime.strptime(self.date_drawn, '%Y-%m-%d').month
			self.month = datetime.strptime(self.date_drawn, '%Y-%m-%d').strftime("%B")
			self.year = datetime.strptime(self.date_drawn, '%Y-%m-%d').year
			self.day_of_week = datetime.strptime(self.date_drawn, '%Y-%m-%d').strftime("%A")
			self.day = datetime.strptime(self.date_drawn, '%Y-%m-%d').strftime("%d")

			self.get_consecutives()



	@api.onchange('x_a')
	def _filter_a(self):
		#print self.x_a

		if self.x_a:
			if re.match("[0-9]", self.x_a) != None:
				try:
					if int(self.x_a) > 42 or int(self.x_a) == 0:
						self.x_a = ''
					else:
						if self.x_a != self.x_b and self.x_a != self.x_c and self.x_a != self.x_d and self.x_a != self.x_e and self.x_a != self.x_f:
							self.a = int(self.x_a)
						else:
							self.x_a = ''
				except:
					self.x_a = ''
			else:
				self.x_a = ''

	@api.onchange('x_b')
	def _filter_b(self):
		#print self.x_b

		if self.x_b:
			if re.match("[0-9]", self.x_b) != None:
				try:
					if int(self.x_b) > 42 or int(self.x_b) == 0:
						self.x_b = ''
					else:
						if self.x_b != self.x_a and self.x_b != self.x_c and self.x_b != self.x_d and self.x_b != self.x_e and self.x_b != self.x_f:
							self.b = int(self.x_b)
						else:
							self.x_b = ''
				except:
					self.x_b = ''
			else:
				self.x_b = ''

	@api.onchange('x_c')
	def _filter_c(self):
		#print self.x_c

		if self.x_c:
			if re.match("[0-9]", self.x_c) != None:
				try:
					if int(self.x_c) > 42 or int(self.x_c) == 0:
						self.x_a = ''
					else:
						if self.x_c != self.x_a and self.x_c != self.x_b and self.x_c != self.x_d and self.x_c != self.x_e and self.x_c != self.x_f:
							self.c = int(self.x_c)
						else:
							self.x_c = ''
				except:
					self.x_c = ''
			else:
				self.x_c = ''

	@api.onchange('x_d')
	def _filter_d(self):
		#print self.x_d

		if self.x_d:
			if re.match("[0-9]", self.x_d) != None:
				try:
					if int(self.x_d) > 42 or int(self.x_d) == 0:
						self.x_d = ''
					else:
						if self.x_d != self.x_a and self.x_d != self.x_c and self.x_d != self.x_b and self.x_d != self.x_e and self.x_d != self.x_f:
							self.d = int(self.x_d)
						else:
							self.x_d = ''
				except:
					self.x_d = ''
			else:
				self.x_d = ''

	@api.onchange('x_e')
	def _filter_e(self):
		#print self.x_e

		if self.x_e:
			if re.match("[0-9]", self.x_e) != None:
				try:
					if int(self.x_e) > 42 or int(self.x_e) == 0:
						self.x_e = ''
					else:
						if self.x_e != self.x_a and self.x_e != self.x_c and self.x_e != self.x_d and self.x_e != self.x_b and self.x_e != self.x_f:
							self.e = int(self.x_e)
						else:
							self.x_e = ''
				except:
					self.x_e = ''
			else:
				self.x_e = ''

	@api.onchange('x_f')
	def _filter_f(self):
		#print self.x_f

		if self.x_f:
			if re.match("[0-9]", self.x_f) != None:
				try:
					if int(self.x_f) > 42 or int(self.x_f) == 0:
						self.x_f = ''
					else:
						if self.x_f != self.x_a and self.x_f != self.x_c and self.x_f != self.x_d and self.x_f != self.x_e and self.x_f != self.x_b:
							self.f = int(self.x_f)
						else:
							self.x_f = ''
				except:
					self.x_f = ''
			else:
				self.x_f = ''

	@api.onchange('x_a','x_b','x_c','x_d','x_e','x_f')
	def _set_name(self):
		print 'set name'

		if self.x_a:
			if self.x_b:
				if self.x_c: 
					if self.x_d: 
						if self.x_e: 
							if self.x_f:
								self.name = self.x_a+' - '+self.x_b+' - '+self.x_c+' - '+self.x_d+' - '+self.x_e+' - '+self.x_f

								even = 0
								odd = 0


								if (self.a % 2 == 0): #even
									even = even + 1
								else: #odd
									odd = odd + 1

								if (self.b % 2 == 0): #even
									even = even + 1
								else: #odd
									odd = odd + 1

								if (self.c % 2 == 0): #even
									even = even + 1
								else: #odd
									odd = odd + 1

								if (self.d % 2 == 0): #even
									even = even + 1
								else: #odd
									odd = odd + 1

								if (self.e % 2 == 0): #even
									even = even + 1
								else: #odd
									odd = odd + 1

								if (self.f % 2 == 0): #even
									even = even + 1
								else: #odd
									odd = odd + 1

								self.even = even
								self.odd = odd

								high = 0
								low = 0

								if self.a > 21:
									high = high + 1
								else:
									low = low + 1

								if self.b > 21:
									high = high + 1
								else:
									low = low + 1

								if self.c > 21:
									high = high + 1
								else:
									low = low + 1

								if self.d > 21:
									high = high + 1
								else:
									low = low + 1

								if self.e > 21:
									high = high + 1
								else:
									low = low + 1

								if self.f > 21:
									high = high + 1
								else:
									low = low + 1

								self.high = high
								self.low = low

								self.res_sum = self.a+self.b+self.c+self.d+self.e+self.f



