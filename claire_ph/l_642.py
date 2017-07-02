from openerp import models, fields, api, _
from openerp import tools
from decimal import *
import time
import re
from openerp.exceptions import except_orm, Warning, RedirectWarning
from datetime import datetime

class results_analysis(models.Model):
	_name = 'results.analysis'

	name = fields.Char(string="Description")
	a_year = fields.Integer(string="Year")

	a_1 = fields.Float(string="1")
	a_2 = fields.Float(string="2")
	a_3 = fields.Float(string="3")
	a_4 = fields.Float(string="4")
	a_5 = fields.Float(string="5")

	a_6 = fields.Float(string="6")
	a_7 = fields.Float(string="7")
	a_8 = fields.Float(string="8")
	a_9 = fields.Float(string="9")
	a_10 = fields.Float(string="10")

	a_11 = fields.Float(string="11")
	a_12 = fields.Float(string="12")
	a_13 = fields.Float(string="13")
	a_14 = fields.Float(string="14")
	a_15 = fields.Float(string="15")

	a_16 = fields.Float(string="16")
	a_17 = fields.Float(string="17")
	a_18 = fields.Float(string="18")
	a_19 = fields.Float(string="19")
	a_20 = fields.Float(string="20")

	a_21 = fields.Float(string="21")
	a_22 = fields.Float(string="22")
	a_23 = fields.Float(string="23")
	a_24 = fields.Float(string="24")
	a_25 = fields.Float(string="25")

	a_26 = fields.Float(string="26")
	a_27 = fields.Float(string="27")
	a_28 = fields.Float(string="28")
	a_29 = fields.Float(string="29")
	a_30 = fields.Float(string="30")

	a_31 = fields.Float(string="31")
	a_32 = fields.Float(string="32")
	a_33 = fields.Float(string="33")
	a_34 = fields.Float(string="34")
	a_35 = fields.Float(string="35")

	a_36 = fields.Float(string="36")
	a_37 = fields.Float(string="37")
	a_38 = fields.Float(string="38")
	a_39 = fields.Float(string="39")
	a_40 = fields.Float(string="40")

	a_41 = fields.Float(string="41")
	a_42 = fields.Float(string="42")

	zero = fields.Float(string="zero")
	one = fields.Float(string="one")
	one_x2 = fields.Float(string="one_x2")
	one_x3 = fields.Float(string="one_x3")
	one_two = fields.Float(string="one_two")
	one_three = fields.Float(string="one_three")
	two = fields.Float(string="two")
	two_x2 = fields.Float(string="two_x2")
	three = fields.Float(string="three")
	three_one = fields.Float(string="three_one")
	four = fields.Float(string="four")
	five = fields.Float(string="five")

	date = fields.Date(string="Date")

	ca_line = fields.One2many('consecutive.analysis', 'ra_id' )

	@api.multi
	def generate_dated_analysis(self):
		print 'generate_analysis'

	@api.multi
	def generate_analysis(self):
		print 'generate_analysis'

		consecutive_analysis_obj = self.pool.get('consecutive.analysis')


		query=	"""
					SELECT
						lr.year,
						round((
							(SELECT count(*) FROM lotto_records WHERE year = lr.year AND consecutive = 'zero')::DECIMAL
							/
							(SELECT count(*) FROM lotto_records WHERE year = lr.year )::DECIMAL
						), 2) *100 as zero,
						round((
							(SELECT count(*) FROM lotto_records WHERE year = lr.year AND consecutive = 'one')::DECIMAL
							/
							(SELECT count(*) FROM lotto_records WHERE year = lr.year )::DECIMAL
						), 2) *100 as one,
						round((
							(SELECT count(*) FROM lotto_records WHERE year = lr.year AND consecutive like 'one_x2')::DECIMAL
							/
							(SELECT count(*) FROM lotto_records WHERE year = lr.year )::DECIMAL
						), 2) *100 as one_x2,
						round((
							(SELECT count(*) FROM lotto_records WHERE year = lr.year AND consecutive = 'one_x3')::DECIMAL
							/
							(SELECT count(*) FROM lotto_records WHERE year = lr.year )::DECIMAL
						), 2) *100 as one_x3,
						round((
							(SELECT count(*) FROM lotto_records WHERE year = lr.year AND consecutive = 'one_two')::DECIMAL
							/
							(SELECT count(*) FROM lotto_records WHERE year = lr.year )::DECIMAL
						), 2) *100 as one_two,
						round((
							(SELECT count(*) FROM lotto_records WHERE year = lr.year AND consecutive = 'one_three')::DECIMAL
							/
							(SELECT count(*) FROM lotto_records WHERE year = lr.year )::DECIMAL
						), 2) *100 as one_three,
						round((
							(SELECT count(*) FROM lotto_records WHERE year = lr.year AND consecutive = 'two')::DECIMAL
							/
							(SELECT count(*) FROM lotto_records WHERE year = lr.year )::DECIMAL
						), 2) *100 as two,
						round((
							(SELECT count(*) FROM lotto_records WHERE year = lr.year AND consecutive = 'two_x2')::DECIMAL
							/
							(SELECT count(*) FROM lotto_records WHERE year = lr.year )::DECIMAL
						), 2) *100 as two_x2,
						round((
							(SELECT count(*) FROM lotto_records WHERE year = lr.year AND consecutive = 'three')::DECIMAL
							/
							(SELECT count(*) FROM lotto_records WHERE year = lr.year )::DECIMAL
						), 2) *100 as three,
						round((
							(SELECT count(*) FROM lotto_records WHERE year = lr.year AND consecutive = 'three_one')::DECIMAL
							/
							(SELECT count(*) FROM lotto_records WHERE year = lr.year )::DECIMAL
						), 2) *100 as three_one,
						round((
							(SELECT count(*) FROM lotto_records WHERE year = lr.year AND consecutive = 'four')::DECIMAL 
							/
							(SELECT count(*) FROM lotto_records WHERE year = lr.year )::DECIMAL
						), 2) *100 as four,
						round((
							(SELECT count(*) FROM lotto_records WHERE year = lr.year AND consecutive = 'five')::DECIMAL
							/
							(SELECT count(*) FROM lotto_records WHERE year = lr.year )::DECIMAL 
						), 2) *100 as five,
						
						(SELECT count(*) FROM lotto_records WHERE year = lr.year ) as all

					FROM
						(SELECT DISTINCT year FROM lotto_records) as lr


					UNION ALL

					SELECT
						'current',
						round((
							(SELECT count(*) FROM lotto_records WHERE year = lr.year AND consecutive = 'zero')::DECIMAL
							/
							(SELECT count(*) FROM lotto_records WHERE year = lr.year )::DECIMAL
						), 2) *100 as zero,
						round((
							(SELECT count(*) FROM lotto_records WHERE year = lr.year AND consecutive = 'one')::DECIMAL
							/
							(SELECT count(*) FROM lotto_records WHERE year = lr.year )::DECIMAL
						), 2) *100 as one,
						round((
							(SELECT count(*) FROM lotto_records WHERE year = lr.year AND consecutive like 'one_x2')::DECIMAL
							/
							(SELECT count(*) FROM lotto_records WHERE year = lr.year )::DECIMAL
						), 2) *100 as one_x2,
						round((
							(SELECT count(*) FROM lotto_records WHERE year = lr.year AND consecutive = 'one_x3')::DECIMAL
							/
							(SELECT count(*) FROM lotto_records WHERE year = lr.year )::DECIMAL
						), 2) *100 as one_x3,
						round((
							(SELECT count(*) FROM lotto_records WHERE year = lr.year AND consecutive = 'one_two')::DECIMAL
							/
							(SELECT count(*) FROM lotto_records WHERE year = lr.year )::DECIMAL
						), 2) *100 as one_two,
						round((
							(SELECT count(*) FROM lotto_records WHERE year = lr.year AND consecutive = 'one_three')::DECIMAL
							/
							(SELECT count(*) FROM lotto_records WHERE year = lr.year )::DECIMAL
						), 2) *100 as one_three,
						round((
							(SELECT count(*) FROM lotto_records WHERE year = lr.year AND consecutive = 'two')::DECIMAL
							/
							(SELECT count(*) FROM lotto_records WHERE year = lr.year )::DECIMAL
						), 2) *100 as two,
						round((
							(SELECT count(*) FROM lotto_records WHERE year = lr.year AND consecutive = 'two_x2')::DECIMAL
							/
							(SELECT count(*) FROM lotto_records WHERE year = lr.year )::DECIMAL
						), 2) *100 as two_x2,
						round((
							(SELECT count(*) FROM lotto_records WHERE year = lr.year AND consecutive = 'three')::DECIMAL
							/
							(SELECT count(*) FROM lotto_records WHERE year = lr.year )::DECIMAL
						), 2) *100 as three,
						round((
							(SELECT count(*) FROM lotto_records WHERE year = lr.year AND consecutive = 'three_one')::DECIMAL
							/
							(SELECT count(*) FROM lotto_records WHERE year = lr.year )::DECIMAL
						), 2) *100 as three_one,
						round((
							(SELECT count(*) FROM lotto_records WHERE year = lr.year AND consecutive = 'four')::DECIMAL 
							/
							(SELECT count(*) FROM lotto_records WHERE year = lr.year )::DECIMAL
						), 2) *100 as four,
						round((
							(SELECT count(*) FROM lotto_records WHERE year = lr.year AND consecutive = 'five')::DECIMAL
							/
							(SELECT count(*) FROM lotto_records WHERE year = lr.year )::DECIMAL 
						), 2) *100 as five,
						
						(SELECT count(*) FROM lotto_records WHERE year = lr.year ) as all

					FROM
						(SELECT year, date_drawn FROM lotto_records limit 1) as lr WHERE lr.year::INT = extract('year' from CURRENT_DATE) AND lr.date_drawn <= CURRENT_DATE

					ORDER BY year ASC

				"""
		self._cr.execute(query)
		result = self._cr.fetchall()

		#remove existing analysis
		consecutive_analysis_ids = consecutive_analysis_obj.search(self.env.cr,self.env.uid, [('ra_id','=',self.id)], order="name desc")

		for rowx in consecutive_analysis_ids:	
			print rowx
			consecutive_analysis_obj.unlink(self.env.cr,self.env.uid, rowx, context=None)

		#create new analysis
		for row in result:		
			print row		
			val = {'ra_id':self.id,'name':row[0],'zero':row[1],'one':row[2],'one_x2':row[3],'one_x3':row[4],'one_two':row[5],'one_three':row[6],'two':row[7],'two_x2':row[8],'three':row[9],'three_one':row[10],'four':row[11],'five':row[12]}
			consecutive_analysis_obj.create(self.env.cr,self.env.uid, val, context=None)


class consucutive_analysis(models.Model): 
	_name = 'consecutive.analysis'

	year = fields.Integer(string="Year")
	name = fields.Char()
	zero = fields.Float(string="zero")
	one = fields.Float(string="one")
	one_x2 = fields.Float(string="one_x2")
	one_x3 = fields.Float(string="one_x3")
	one_two = fields.Float(string="one_two")
	one_three = fields.Float(string="one_three")
	two = fields.Float(string="two")
	two_x2 = fields.Float(string="two_x2")
	three = fields.Float(string="three")
	three_one = fields.Float(string="three_one")
	four = fields.Float(string="four")
	five = fields.Float(string="five")

	ra_id = fields.Many2one('results.analysis', 'ca_line', store = True,ondelete='cascade')


class pattern_recognition(models.TransientModel):
	_name = 'pattern.recognition'

	@api.multi
	def find_pattern_consecutive(self):#201
		print 'Execute find_pattern_consecutive'

class lotto_records(models.Model):
	_name = 'lotto.records'


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


	@api.multi
	def get_consecutives(self):
		print 'Get Consecutives...'

		for rec in self:

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

								if self.a > 22:
									high = high + 1
								else:
									low = low + 1

								if self.b > 22:
									high = high + 1
								else:
									low = low + 1

								if self.c > 22:
									high = high + 1
								else:
									low = low + 1

								if self.d > 22:
									high = high + 1
								else:
									low = low + 1

								if self.e > 22:
									high = high + 1
								else:
									low = low + 1

								if self.f > 22:
									high = high + 1
								else:
									low = low + 1

								self.high = high
								self.low = low

								self.res_sum = self.a+self.b+self.c+self.d+self.e+self.f

class lotto_records_summary(models.Model):
	_name = 'lotto.records.summary'


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
	odd = fields.Integer(default=0)
	even = fields.Integer(default=0)
	high = fields.Integer(string='High', default=0)
	low = fields.Integer(string='Low', default=0)
	res_sum = fields.Integer(string='Sum') 
	date_drawn = fields.Date(string='Date')


