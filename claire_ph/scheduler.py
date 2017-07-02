# -*- coding: utf-8 -*-
from openerp import models, fields, api, _
from openerp import tools
#!/usr/bin/python
import psycopg2
import urllib2
from datetime import datetime, date, timedelta


class lotto_records_grab(models.Model):
	_inherit = 'lotto.records'


	def connect_db2(self, cr, uid):
		print 'Claire:textGrabber v1 - reversed'

		lotto_records_obj = self.pool.get('lotto.records')

		x = 0
		y = 0
		found_642 = 0
		store = 0
		result =''
		#url = "http://www.pinoylottoresults.com/pcso/2017/02/02/"
		url = "http://www.pinoylottoresults.com/pcso/"
		cr.execute("SELECT (SELECT date_drawn+1 FROM lotto_records ORDER BY date_drawn ASC limit 1), CURRENT_DATE")
		data = cr.fetchone()

		print data



		start_date = datetime.strptime(data[0], "%Y-%m-%d").date()
		end_date = datetime.strptime(data[1], "%Y-%m-%d").date()

		print {'start_date':start_date,'end_date':end_date}

		for single_date in self.daterange(start_date, end_date):
			end = 0
			
			#print single_date.strftime("%Y-%m-%d")
			if single_date.strftime("%A") in ('Tuesday','Thursday','Saturday'):
				#print 'Clearing Result..'
				result =''
				print {'date':single_date.strftime("%Y-%m-%d") , 'day of the week':single_date.strftime("%A") }
				print url+str(single_date.strftime("%Y/%m/%d/") )

				try:

					response = urllib2.urlopen(url+str(single_date.strftime("%Y/%m/%d/") ) )
					print 'response ',response
				except:
					print 'No Response! on %s'%(url+str(single_date.strftime("%Y/%m/%d/") ) )
					response = ''

				
				if response:
					html = response.read()
					#print html
					#filename = wget.download(url)
					for line in html:
						if end == 0:
							#print line
							#if store == 0:
							if  found_642 == 0:
								if line[0] == '6':
									x = x + 1
								elif line[0] == '/':
									x = x + 1
								elif line[0] == '4':
									x = x + 1
								elif line[0] == '2':
									x = x + 1
								elif line[0] == '<':
									x = x + 1
								elif line[0] == '/':
									x = x + 1
								elif line[0] == 'd':
									x = x + 1
								elif line[0] == 'i':
									x = x + 1
								elif line[0] == 'v':
									x = x + 1
								elif line[0] == '>':
									x = x + 1
									#print ' x: ',x,
									if x == 10:
										print '6/42 label found'
										found_642 = 1
								else:
									#print '_'
									x = 0

							if found_642 == 1:
								if line[0] == '<':
									y = y + 1
								elif line[0] == 'p':
									y = y + 1
								elif line[0] == '>':
									y = y + 1
									#print ' y: ',y,
									if y == 25:
										print '6/42 result found'
										found_642 = 0
										x = 0
										y = 0
										store =1
								#elif line[0] == '<':
								#    y = y + 1
								elif line[0] == 'l':
									y = y + 1
								elif line[0] == 'a':
									y = y + 1
								elif line[0] == 'b':
									y = y + 1
								elif line[0] == 'e':
									y = y + 1
								elif line[0] == 'l':
									y = y + 1
								#elif line[0] == '>':
								#    y = y + 1
								elif line[0] == '9':
									y = y #+ 1
								elif line[0] == 'P':
									y = y #+ 1
								elif line[0] == 'M':
									y = y #+ 1
								elif line[0] == ' ':
									y = y + 1
								elif line[0] == '=':
									y = y + 1
								#elif line[0] == '>':
								#    y = y + 1
								#elif line[0] == ' ':
								#    y = y + 1
								#elif line[0] == '<':
								#    y = y + 1
								elif line[0] == '/':
									y = y + 1
								#elif line[0] == 'l':
								#    y = y + 1
								#elif line[0] == 'a':
								#    y = y + 1
								#elif line[0] == 'b':
								#    y = y + 1
								#elif line[0] == 'e':
								#    y = y + 1
								#elif line[0] == 'l':
								#    y = y + 1
								#elif line[0] == '>':
								#    y = y + 1
								#elif line[0] == '<':
								#    y = y + 1
								#elif line[0] == 'b':
								#    y = y + 1
								#elif line[0] == '>':
								#    y = y + 1
								elif line[0] == ':':
								    y = y + 4
								else:
									#print '_'
									y = 0


							if store == 1:
								if line != '<':
									if line != '>':
										result = result + str(line)
								else:
									store = 0
									end = 1
									print '-- End --'
									#result = result.replace('-',' - ')


					
					print 'result ',result

					if result:
						print 'str len ',len(result)
						if len(result) == 17:
							print 'Writing results in lotto_records...'
							even = 0
							odd = 0
							s_result = result.split('-')

							if (int(s_result[0]) % 2 == 0): #even
								even = even + 1
							else: #odd
								odd = odd + 1

							if (int(s_result[1]) % 2 == 0): #even
								even = even + 1
							else: #odd
								odd = odd + 1

							if (int(s_result[2]) % 2 == 0): #even
								even = even + 1
							else: #odd
								odd = odd + 1

							if (int(s_result[3]) % 2 == 0): #even
								even = even + 1
							else: #odd
								odd = odd + 1

							if (int(s_result[4]) % 2 == 0): #even
								even = even + 1
							else: #odd
								odd = odd + 1

							if (int(s_result[5]) % 2 == 0): #even
								even = even + 1
							else: #odd
								odd = odd + 1

							high = 0
							low = 0

							if int(s_result[0]) > 22:
								high = high + 1
							else:
								low = low + 1

							if int(s_result[1]) > 22:
								high = high + 1
							else:
								low = low + 1

							if int(s_result[2]) > 22:
								high = high + 1
							else:
								low = low + 1

							if int(s_result[3]) > 22:
								high = high + 1
							else:
								low = low + 1

							if int(s_result[4]) > 22:
								high = high + 1
							else:
								low = low + 1

							if int(s_result[5]) > 22:
								high = high + 1
							else:
								low = low + 1

							res_sum = int(s_result[0])+int(s_result[1])+int(s_result[2])+int(s_result[3])+int(s_result[4])+int(s_result[5])



							date_drawn = single_date.strftime("%Y-%m-%d")
							vals ={'a':int(s_result[0]),'b':int(s_result[1]),'c':int(s_result[2]),'d':int(s_result[3]),'e':int(s_result[4]),'f':int(s_result[5]),
								'x_a':s_result[0],'x_b':s_result[1],'x_c':s_result[2],'x_d':s_result[3],'x_e':s_result[4],'x_f':s_result[5],
								'date_drawn':date_drawn, 'month': datetime.strptime(date_drawn, '%Y-%m-%d').strftime("%B"), 'year': datetime.strptime(date_drawn, '%Y-%m-%d').strftime("%Y"),
								'day_of_week': datetime.strptime(date_drawn, '%Y-%m-%d').strftime("%A"), 'day': datetime.strptime(date_drawn, '%Y-%m-%d').strftime("%d"),
								'high':high, 'low':low, 'odd':odd, 'even':even, 'res_sum':res_sum,
								'name':result.replace('-',' - ') }
							print vals
							cr.execute("SELECT * FROM lotto_records WHERE date_drawn = '%s'::DATE" % (date_drawn))
							data = cr.fetchone()
							if data:
								print 'Date drawn record exist'
							else:
								print 'Record created'
								lotto_records_obj.create(cr, uid, vals, context=None)
	
	def connect_db(self, cr, uid):
		print 'Claire:textGrabber v1'

		lotto_records_obj = self.pool.get('lotto.records')

		x = 0
		y = 0
		found_642 = 0
		store = 0
		result =''
		#url = "http://www.pinoylottoresults.com/pcso/2017/02/02/"
		url = "http://www.pinoylottoresults.com/pcso/"
		cr.execute("SELECT (SELECT date_drawn+1 FROM lotto_records ORDER BY date_drawn DESC limit 1), CURRENT_DATE")
		data = cr.fetchone()

		print data



		start_date = datetime.strptime(data[0], "%Y-%m-%d").date()
		end_date = datetime.strptime(data[1], "%Y-%m-%d").date()

		print {'start_date':start_date,'end_date':end_date}

		for single_date in self.daterange(start_date, end_date):
			end = 0
			
			#print single_date.strftime("%Y-%m-%d")
			if single_date.strftime("%A") in ('Tuesday','Thursday','Saturday'):
				#print 'Clearing Result..'
				result =''
				print {'date':single_date.strftime("%Y-%m-%d") , 'day of the week':single_date.strftime("%A") }
				print url+str(single_date.strftime("%Y/%m/%d/") )

				try:

					response = urllib2.urlopen(url+str(single_date.strftime("%Y/%m/%d/") ) )
					print 'response ',response
				except:
					print 'No Response! on %s'%(url+str(single_date.strftime("%Y/%m/%d/") ) )
					response = ''

				
				if response:
					html = response.read()

					#print html
					#filename = wget.download(url)
					for line in html:
						if end == 0:
							#print line
							#if store == 0:
							if  found_642 == 0:
								if line[0] == '6':
									x = x + 1
								elif line[0] == '/':
									x = x + 1
								elif line[0] == '4':
									x = x + 1
								elif line[0] == '2':
									x = x + 1
								elif line[0] == '<':
									x = x + 1
								elif line[0] == '/':
									x = x + 1
								elif line[0] == 'd':
									x = x + 1
								elif line[0] == 'i':
									x = x + 1
								elif line[0] == 'v':
									x = x + 1
								elif line[0] == '>':
									x = x + 1
									#print ' x: ',x,
									if x == 10:
										print '6/42 label found'
										found_642 = 1
								else:
									#print '_'
									x = 0

							if found_642 == 1:
								if line[0] == '<':
									y = y + 1
								elif line[0] == 'p':
									y = y + 1
								elif line[0] == '>':
									y = y + 1
									#print ' y: ',y,
									if y == 25:
										print '6/42 result found'
										found_642 = 0
										x = 0
										y = 0
										store =1
								#elif line[0] == '<':
								#    y = y + 1
								elif line[0] == 'l':
									y = y + 1
								elif line[0] == 'a':
									y = y + 1
								elif line[0] == 'b':
									y = y + 1
								elif line[0] == 'e':
									y = y + 1
								elif line[0] == 'l':
									y = y + 1
								#elif line[0] == '>':
								#    y = y + 1
								elif line[0] == '9':
									y = y #+ 1
								elif line[0] == 'P':
									y = y #+ 1
								elif line[0] == 'M':
									y = y #+ 1
								elif line[0] == ' ':
									y = y + 1
								elif line[0] == '=':
									y = y + 1
								#elif line[0] == '>':
								#    y = y + 1
								#elif line[0] == ' ':
								#    y = y + 1
								#elif line[0] == '<':
								#    y = y + 1
								elif line[0] == '/':
									y = y + 1
								#elif line[0] == 'l':
								#    y = y + 1
								#elif line[0] == 'a':
								#    y = y + 1
								#elif line[0] == 'b':
								#    y = y + 1
								#elif line[0] == 'e':
								#    y = y + 1
								#elif line[0] == 'l':
								#    y = y + 1
								#elif line[0] == '>':
								#    y = y + 1
								#elif line[0] == '<':
								#    y = y + 1
								#elif line[0] == 'b':
								#    y = y + 1
								#elif line[0] == '>':
								#    y = y + 1
								elif line[0] == ':':
								    y = y + 4
								else:
									#print '_'
									y = 0


							if store == 1:
								if line != '<':
									if line != '>':
										result = result + str(line)
								else:
									store = 0
									end = 1
									print '-- End --'
									#result = result.replace('-',' - ')


					
					print 'result ',result

					if result:
						print 'str len ',len(result)
						if len(result) == 17:
							print 'Writing results in lotto_records...'
							even = 0
							odd = 0
							s_result = result.split('-')

							if (int(s_result[0]) % 2 == 0): #even
								even = even + 1
							else: #odd
								odd = odd + 1

							if (int(s_result[1]) % 2 == 0): #even
								even = even + 1
							else: #odd
								odd = odd + 1

							if (int(s_result[2]) % 2 == 0): #even
								even = even + 1
							else: #odd
								odd = odd + 1

							if (int(s_result[3]) % 2 == 0): #even
								even = even + 1
							else: #odd
								odd = odd + 1

							if (int(s_result[4]) % 2 == 0): #even
								even = even + 1
							else: #odd
								odd = odd + 1

							if (int(s_result[5]) % 2 == 0): #even
								even = even + 1
							else: #odd
								odd = odd + 1

							high = 0
							low = 0

							if int(s_result[0]) > 22:
								high = high + 1
							else:
								low = low + 1

							if int(s_result[1]) > 22:
								high = high + 1
							else:
								low = low + 1

							if int(s_result[2]) > 22:
								high = high + 1
							else:
								low = low + 1

							if int(s_result[3]) > 22:
								high = high + 1
							else:
								low = low + 1

							if int(s_result[4]) > 22:
								high = high + 1
							else:
								low = low + 1

							if int(s_result[5]) > 22:
								high = high + 1
							else:
								low = low + 1

							res_sum = int(s_result[0])+int(s_result[1])+int(s_result[2])+int(s_result[3])+int(s_result[4])+int(s_result[5])



							date_drawn = single_date.strftime("%Y-%m-%d")
							vals ={'a':int(s_result[0]),'b':int(s_result[1]),'c':int(s_result[2]),'d':int(s_result[3]),'e':int(s_result[4]),'f':int(s_result[5]),
								'x_a':s_result[0],'x_b':s_result[1],'x_c':s_result[2],'x_d':s_result[3],'x_e':s_result[4],'x_f':s_result[5],
								'date_drawn':date_drawn, 'month': datetime.strptime(date_drawn, '%Y-%m-%d').strftime("%B"), 'year': datetime.strptime(date_drawn, '%Y-%m-%d').strftime("%Y"),
								'day_of_week': datetime.strptime(date_drawn, '%Y-%m-%d').strftime("%A"), 'day': datetime.strptime(date_drawn, '%Y-%m-%d').strftime("%d"),
								'high':high, 'low':low, 'odd':odd, 'even':even, 'res_sum':res_sum,
								'name':result.replace('-',' - ') }
							print vals
							cr.execute("SELECT * FROM lotto_records WHERE date_drawn = '%s'::DATE" % (date_drawn))
							data = cr.fetchone()
							if data:
								print 'Date drawn record exist'
							else:
								print 'Record created'
								lotto_records_obj.create(cr, uid, vals, context=None)


	def daterange(self,start_date, end_date):
		print 'execute daterange'
		for n in range(int ((end_date - start_date).days)):
			yield start_date + timedelta(n)