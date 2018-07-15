from openerp import models, fields, api, _
from openerp import tools
from decimal import *
import time
import re
from openerp.exceptions import except_orm, Warning, RedirectWarning
from datetime import datetime
import random
import datetime as dt
from tempfile import TemporaryFile
import base64
import csv


def validate_date(text):
	
	try:
		print 'date_text ', text
		dt.datetime.strptime(text, '%m/%d/%Y')
		value = 'Valid data'
	except ValueError:
	
		value = "%s - Incorrect data format, should be MM/DD/YYYY"%(text)
		#raise ValueError("Incorrect data format, should be MM-DD-YYYY")

	print value
	return value
		

def validate_game(text):
	value = ''
	if text == 'Lotto 6/42':
		value = 'Valid data'

	else:
		value = "%s - Incorrect lotto game"%(text)

	print value
	return value


def validate_combinations(text):
	# Should be digit
	# Should not contain zero
	# Should not contain duplicate digit

	res = True
	if text:
		s_result = text.split('-')
		print s_result

		x = 0
		y = [0,1,2,3,4,5]
		for x in y:
			#print """x=%s %s """% (x,s_result[x])
			res = s_result[x].isdigit()

			if res == False:
				break

			if int(s_result[x]) == 0:
				res = False
				break				

			if int(s_result[x]) > 42:
				res = False
				break	

			count = x + 1
			
			if x < 5:
				while count <= 5:
					#print """%s == %s s_result[x] == s_result[count] """%(s_result[x],s_result[count])
					if s_result[x] == s_result[count]:

						res = False
						break

					count += 1

			if res == False:
				break



		# res = s_result[0].isdigit()
		if res == True:
			#print 'res ',res
			value = 'Valid data'
		else:
			#print 'res ',res
			value = "%s - Incorrect combination."%(text)
	else:
		value = "%s - Incorrect combination."%(text)

	print value
	return value


def quicksort(x):
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
		first_part = quicksort(x[:i])
		second_part = quicksort(x[i+1:])
		first_part.append(x[i])
		return first_part + second_part


def sort_name(a,b,c,d,e,f):
	#print 'sort_name'

	alist = [a,b,c,d,e,f]
	alist = quicksort(alist)

	return str(alist[0]) + ' - ' + str(alist[1]) + ' - ' + str(alist[2]) + ' - ' + str(alist[3]) + ' - ' + str(alist[4]) + ' - ' + str(alist[5])


def get_consecutives(a,b,c,d,e,f):
	print 'Get Consecutives...'
	consecutive = ''
	

	lista = []
	listb = []

	lista.append(a)
	lista.append(b)
	lista.append(c)
	lista.append(d)
	lista.append(e)
	lista.append(f)

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
			#print 'correct'

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
		consecutive = 'one_x3'
	elif lista == [1,1]:
		print 'one_x2'
		consecutive = 'one_x2'
	elif lista == [1]:
		print 'one'
		consecutive = 'one'
	elif lista == [1,2]:
		print 'one_two'
		consecutive = 'one_two'
	elif lista == [1,3]:
		print 'one'
		consecutive = 'one'
	elif lista == [2]:
		print 'two'
		consecutive = 'two'
	elif lista == [2,1]:
		print 'one_two'
		consecutive = 'one_two'
	elif lista == [2,2]:
		print 'two_x2'
		consecutive = 'two_x2'
	elif lista == [3]:
		print 'three'
		consecutive = 'three'
	elif lista == [3,1]:
		print 'three_one'
		consecutive = 'three_one'
	elif lista == [4]:
		print 'four'
		consecutive = 'four'
	elif lista == [5]:
		print 'five'
		consecutive = 'five'
	else:
		print 'zero'
		consecutive = 'zero'

	return consecutive

class upload_lotto_reults(models.TransientModel):
	_name = 'upload.lotto.results'


	name = fields.Char('Upload File Template')
	#school_year = fields.Many2one('school.year')
	template_file = fields.Binary('Leads Upload', help="Set this CSV file as the template file")
	# temp_file = fields.Binary("File", related='data')
	data = fields.Binary(sring='CSV File')
	data_filename = fields.Char("Filename")
	#upload_grade_line = fields.One2many('course.grades.line', 'course_grades_id' )
	date_format = fields.Boolean('Date format (mm/dd/YYYY)', default=True)

	valid = fields.Boolean('Valid', default=False)

	invalid = fields.Text("Invalid Items", readonly=True) 

	upload_result_line = fields.One2many('upload.lotto.result.line', 'result_id' )

	@api.multi 
	def get_template(self):
		return {
			'type' : 'ir.actions.act_url',
			'url': '/web/binary/download_upload_leads_document',
			'target': 'self',
			}     


	def test(self):
		print 'test'

		#validate_date('01/05/2008')
		#validate_combinations('3-5-6-21-25-27') 

		print "14,16,19,28,30,32"
		#print sort_name(17,16,19,29,03,14)
		get_consecutives(14,16,19,28,30,32)

	@api.multi
	def upload_results(self):
		print 'upload_leads'
		if self.valid:

			#Loop through the line:

			for rec in self:

				temp_ids = []
				count = 0
				temp_q = ""
				so_ids = []
				inv_ids = []
				for l in rec.upload_result_line:

					#initialization
					#none

					# if l.created_date:
					# 	if self.date_format:
					# 		salesforce_date = datetime.strptime(l.created_date, "%m/%d/%Y").strftime('%Y-%m-%d')
					# 	else:
					# 		salesforce_date = datetime.strptime(l.created_date, "%d/%m/%Y").strftime('%Y-%m-%d')

					name = l.combination
					s_result = name.split('-')
					sorted_name = sort_name(s_result[0],s_result[1],s_result[2],s_result[3],s_result[4],s_result[5])

					s_result = sorted_name.split('-')

					x_a = s_result[0]
					x_b = s_result[1]
					x_c = s_result[2]
					x_d = s_result[3]
					x_e = s_result[4]
					x_f = s_result[5]

					a = int(s_result[0])
					b = int(s_result[1])
					c = int(s_result[2])
					d = int(s_result[3])
					e = int(s_result[4])
					f = int(s_result[5])


					game = l.lotto_game


					odd=0
					even=0

					if (a % 2 == 0): #even
						even = even + 1
					else: #odd
						odd = odd + 1

					if (b % 2 == 0): #even
						even = even + 1
					else: #odd
						odd = odd + 1

					if (c % 2 == 0): #even
						even = even + 1
					else: #odd
						odd = odd + 1

					if (d % 2 == 0): #even
						even = even + 1
					else: #odd
						odd = odd + 1

					if (e % 2 == 0): #even
						even = even + 1
					else: #odd
						odd = odd + 1

					if (f % 2 == 0): #even
						even = even + 1
					else: #odd
						odd = odd + 1


					high=0
					low=0

					if a > 21:
						high = high + 1
					else:
						low = low + 1

					if b > 21:
						high = high + 1
					else:
						low = low + 1

					if c > 21:
						high = high + 1
					else:
						low = low + 1

					if d > 21:
						high = high + 1
					else:
						low = low + 1

					if e > 21:
						high = high + 1
					else:
						low = low + 1

					if f > 21:
						high = high + 1
					else:
						low = low + 1


					res_sum = a+b+c+d+e+f

					consecutive = get_consecutives(a,b,c,d,e,f)

					date_drawn = l.draw_date

					month = datetime.strptime(date_drawn, '%m/%d/%Y').strftime("%B")
					year = datetime.strptime(date_drawn, '%m/%d/%Y').year
					day_of_week = datetime.strptime(date_drawn, '%m/%d/%Y').strftime("%A")
					day = datetime.strptime(date_drawn, '%m/%d/%Y').strftime("%d")

					#print 'validation ',validation


					temp = """
							INSERT INTO lotto_records 
								(x_a, x_b, x_c, x_d, x_e, x_f,
								 a, b, c, d, e, f,
								 name, sorted_name, odd, even, high, low,
								 res_sum, consecutive, date_drawn, month, year, day, 
								 day_of_week, create_uid, create_date,
								 game
								)
							VALUES 
								(
								 '%s', '%s', '%s', '%s', '%s', '%s',
								 %s, %s, %s, %s, %s, %s,
								 '%s', '%s', %s, %s, %s, %s,
								 %s, '%s', '%s', '%s', '%s', '%s',
								 '%s', '%s', NOW(),
								 '%s'
								)
							ON CONFLICT (date_drawn)
							DO
							UPDATE SET 
								x_a = '%s', x_b = %s, x_c = '%s', x_d = '%s', x_e = %s, x_f = %s,
								a = %s, b = %s, c = %s, d = %s, e = %s, f = %s,
								name = '%s', sorted_name = '%s', odd = %s, even = %s, high = %s, low = %s,
								res_sum = %s, consecutive = '%s', date_drawn = '%s', month = '%s', year = '%s', day = '%s',
								day_of_week = '%s', create_uid = '%s', create_date = NOW(),
								game = '%s'; 
							"""%(
									x_a, x_b, x_c, x_d, x_e, x_f,
									a, b, c, d, e, f,
									name, sorted_name, odd, even, high, low,
									res_sum, consecutive, date_drawn, month, year, day,
									day_of_week, rec._uid,
									game,

									x_a, x_b, x_c, x_d, x_e, x_f,
									a, b, c, d, e, f,
									name, sorted_name, odd, even, high, low,
									res_sum, consecutive, date_drawn, month, year, day,
									day_of_week, rec._uid,
									game
								)

								

					temp_q += temp
					count += 1
					if count == 500:
						tmp = ''
						self._cr.execute(temp_q.replace("'Null'", "Null"))
						#print temp_q.replace("'Null'", "Null")
						temp_q = ''
						count = 0



				#print temp_q.replace("'Null'", "Null")
				if count != 0:
					tmp = ''
					self._cr.execute(temp_q.replace("'Null'", "Null"))
					if tmp:
						temp_ids += tmp	
										



	def _validate_line(self, l, x):
		#print '_validate_line'
		res = {}
		temp = ''
		#print l
		valid = ""
		valid1 = ''
		valid2 = ''
		error = 0
		#print l
			
		if validate_game(l['lotto_game']) != 'Valid data':
			error += 1
			valid = validate_game(l['lotto_game'])

		if error == 1:
			res['is_valid'] = False
			res['valid'] = valid
		else:
			res['is_valid'] = True
			res['valid'] = "Valid"

		if validate_combinations(l['combination']) != 'Valid data':
			error += 1
			valid = validate_combinations(l['combination'])

		if error == 1:
			res['is_valid'] = False
			res['valid'] = valid
		elif error > 1:
			res['is_valid'] = False
			res['valid'] = res['valid'] +", "+valid
		else:
			res['is_valid'] = True
			res['valid'] = "Valid"

		if validate_date(l['draw_date']) != 'Valid data':
			error += 1
			valid = validate_date(l['draw_date'])

		if error == 1:
			res['is_valid'] = False
			res['valid'] = valid
		elif error > 1:
			res['is_valid'] = False
			res['valid'] = res['valid'] +", "+valid
		else:
			res['is_valid'] = True
			res['valid'] = "Valid"



		#print "res['valid'] ",res['valid']
		return res

	@api.multi
	def onchange_data(self,data):
		print 'onchange_data'
		res={}
		vals={}

		lines = []
		error = 0
		temp = ''

		print 'self.valid ',self.valid

		if data:
			print 'onchange_data if data'
			fileobj = TemporaryFile('w+') #Temporary File
			fileobj.write(base64.decodestring(data)) 
			#Check for consistency in the uploaded file
			fileobj.seek(0)

			#reader = csv.reader(open(fileobj, 'rU'), dialect=csv.excel_tab)
			reader = csv.DictReader(fileobj)
			x = 1
			for row in reader:

				x += 1
				#print 'B'
				#print {'row':row}
				vals['lotto_game'] = row['LOTTO GAME']
				vals['combination'] = row['COMBINATIONS']
				vals['draw_date'] = row['DRAW DATE']
				vals['jackpot'] = row['JACKPOT']
				vals['winners'] = row['WINNERS']


				

				v = self._validate_line(vals,x)
				#print 'v ',v
				vals['is_valid'] = v['is_valid']

				if v['valid'] != 'Valid':
					temp += """
					%s. %s"""%(x-1,v['valid'])
					vals['valid'] = temp
				if not v['is_valid']:
					error += 1

				lines.append(vals.copy())
				#print 'error ',error

			fileobj.close()

		res['upload_result_line'] = lines
		if error > 0:
			res['invalid'] = """%s Errors Encountered during loading please see lines below: 
				%s""" % (error, vals['valid'])
			res['valid'] = False
		
		if error == 0:
			res['valid'] = True
			res['invalid'] = ''
			
		
		return {'value': res}


class upload_lotto_result_lines(models.TransientModel):
	_name = 'upload.lotto.result.line'


	lotto_game = fields.Char()
	combination = fields.Char()
	draw_date = fields.Char()
	jackpot = fields.Char()
	winners = fields.Char()



	result_id = fields.Many2one('upload.lotto.results', 'upload_result_line')



