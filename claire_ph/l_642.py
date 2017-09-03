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

	#========================================= Analysis by Date
	x_1 = fields.Float(string="1")
	x_2 = fields.Float(string="2")
	x_3 = fields.Float(string="3")
	x_4 = fields.Float(string="4")
	x_5 = fields.Float(string="5")

	x_6 = fields.Float(string="6")
	x_7 = fields.Float(string="7")
	x_8 = fields.Float(string="8")
	x_9 = fields.Float(string="9")
	x_10 = fields.Float(string="10")

	x_11 = fields.Float(string="11")
	x_12 = fields.Float(string="12")
	x_13 = fields.Float(string="13")
	x_14 = fields.Float(string="14")
	x_15 = fields.Float(string="15")

	x_16 = fields.Float(string="16")
	x_17 = fields.Float(string="17")
	x_18 = fields.Float(string="18")
	x_19 = fields.Float(string="19")
	x_20 = fields.Float(string="20")

	x_21 = fields.Float(string="21")
	x_22 = fields.Float(string="22")
	x_23 = fields.Float(string="23")
	x_24 = fields.Float(string="24")
	x_25 = fields.Float(string="25")

	x_26 = fields.Float(string="26")
	x_27 = fields.Float(string="27")
	x_28 = fields.Float(string="28")
	x_29 = fields.Float(string="29")
	x_30 = fields.Float(string="30")

	x_31 = fields.Float(string="31")
	x_32 = fields.Float(string="32")
	x_33 = fields.Float(string="33")
	x_34 = fields.Float(string="34")
	x_35 = fields.Float(string="35")

	x_36 = fields.Float(string="36")
	x_37 = fields.Float(string="37")
	x_38 = fields.Float(string="38")
	x_39 = fields.Float(string="39")
	x_40 = fields.Float(string="40")

	x_41 = fields.Float(string="41")
	x_42 = fields.Float(string="42")

	#========================================= Prediction
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

	#========================================= Statistics
	b_1 = fields.Float(string="1")
	b_2 = fields.Float(string="2")
	b_3 = fields.Float(string="3")
	b_4 = fields.Float(string="4")
	b_5 = fields.Float(string="5")

	b_6 = fields.Float(string="6")
	b_7 = fields.Float(string="7")
	b_8 = fields.Float(string="8")
	b_9 = fields.Float(string="9")
	b_10 = fields.Float(string="10")

	b_11 = fields.Float(string="11")
	b_12 = fields.Float(string="12")
	b_13 = fields.Float(string="13")
	b_14 = fields.Float(string="14")
	b_15 = fields.Float(string="15")

	b_16 = fields.Float(string="16")
	b_17 = fields.Float(string="17")
	b_18 = fields.Float(string="18")
	b_19 = fields.Float(string="19")
	b_20 = fields.Float(string="20")

	b_21 = fields.Float(string="21")
	b_22 = fields.Float(string="22")
	b_23 = fields.Float(string="23")
	b_24 = fields.Float(string="24")
	b_25 = fields.Float(string="25")

	b_26 = fields.Float(string="26")
	b_27 = fields.Float(string="27")
	b_28 = fields.Float(string="28")
	b_29 = fields.Float(string="29")
	b_30 = fields.Float(string="30")

	b_31 = fields.Float(string="31")
	b_32 = fields.Float(string="32")
	b_33 = fields.Float(string="33")
	b_34 = fields.Float(string="34")
	b_35 = fields.Float(string="35")

	b_36 = fields.Float(string="36")
	b_37 = fields.Float(string="37")
	b_38 = fields.Float(string="38")
	b_39 = fields.Float(string="39")
	b_40 = fields.Float(string="40")

	b_41 = fields.Float(string="41")
	b_42 = fields.Float(string="42")


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


	a_zero = fields.Float(string="zero")
	a_one = fields.Float(string="one")
	a_one_x2 = fields.Float(string="one_x2")
	a_one_x3 = fields.Float(string="one_x3")
	a_one_two = fields.Float(string="one_two")
	a_one_three = fields.Float(string="one_three")
	a_two = fields.Float(string="two")
	a_two_x2 = fields.Float(string="two_x2")
	a_three = fields.Float(string="three")
	a_three_one = fields.Float(string="three_one")
	a_four = fields.Float(string="four")
	a_five = fields.Float(string="five")


	b_zero = fields.Float(string="zero")
	b_one = fields.Float(string="one")
	b_one_x2 = fields.Float(string="one_x2")
	b_one_x3 = fields.Float(string="one_x3")
	b_one_two = fields.Float(string="one_two")
	b_one_three = fields.Float(string="one_three")
	b_two = fields.Float(string="two")
	b_two_x2 = fields.Float(string="two_x2")
	b_three = fields.Float(string="three")
	b_three_one = fields.Float(string="three_one")
	b_four = fields.Float(string="four")
	b_five = fields.Float(string="five")

	date = fields.Date(string="Date")

	ca_line = fields.One2many('consecutive.analysis', 'ra_id' )

	@api.multi
	def generate_dated_analysis(self):
		print 'generate_dated_analysis'

		#======================================================================== Analysis by Date ======================================================================== 
		query="""
				SELECT
					lr.date::DATE,
					round((
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from lr.date::DATE) AND date_drawn <= lr.date::DATE AND consecutive = 'zero')::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from lr.date::DATE) AND date_drawn <= lr.date::DATE )::DECIMAL
					), 2) *100 as zero,
					round((
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from lr.date::DATE) AND date_drawn <= lr.date::DATE AND consecutive = 'one')::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from lr.date::DATE) AND date_drawn <= lr.date::DATE )::DECIMAL
					), 2) *100 as one,
					round((
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from lr.date::DATE) AND date_drawn <= lr.date::DATE AND consecutive like 'one_x2')::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from lr.date::DATE) AND date_drawn <= lr.date::DATE )::DECIMAL
					), 2) *100 as one_x2,
					round((
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from lr.date::DATE) AND date_drawn <= lr.date::DATE AND consecutive = 'one_x3')::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from lr.date::DATE) AND date_drawn <= lr.date::DATE )::DECIMAL
					), 2) *100 as one_x3,
					round((
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from lr.date::DATE) AND date_drawn <= lr.date::DATE AND consecutive = 'one_two')::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from lr.date::DATE) AND date_drawn <= lr.date::DATE )::DECIMAL
					), 2) *100 as one_two,
					round((
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from lr.date::DATE) AND date_drawn <= lr.date::DATE AND consecutive = 'one_three')::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from lr.date::DATE) AND date_drawn <= lr.date::DATE )::DECIMAL
					), 2) *100 as one_three,
					round((
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from lr.date::DATE) AND date_drawn <= lr.date::DATE AND consecutive = 'two')::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from lr.date::DATE) AND date_drawn <= lr.date::DATE )::DECIMAL
					), 2) *100 as two,
					round((
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from lr.date::DATE) AND date_drawn <= lr.date::DATE AND consecutive = 'two_x2')::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from lr.date::DATE) AND date_drawn <= lr.date::DATE )::DECIMAL
					), 2) *100 as two_x2,
					round((
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from lr.date::DATE) AND date_drawn <= lr.date::DATE AND consecutive = 'three')::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from lr.date::DATE) AND date_drawn <= lr.date::DATE )::DECIMAL
					), 2) *100 as three,
					round((
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from lr.date::DATE) AND date_drawn <= lr.date::DATE AND consecutive = 'three_one')::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from lr.date::DATE) AND date_drawn <= lr.date::DATE )::DECIMAL
					), 2) *100 as three_one,
					round((
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from lr.date::DATE) AND date_drawn <= lr.date::DATE AND consecutive = 'four')::DECIMAL 
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from lr.date::DATE) AND date_drawn <= lr.date::DATE )::DECIMAL
					), 2) *100 as four,
					round((
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from lr.date::DATE) AND date_drawn <= lr.date::DATE AND consecutive = 'five')::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from lr.date::DATE) AND date_drawn <= lr.date::DATE )::DECIMAL 
					), 2) *100 as five,
					
					(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from lr.date::DATE) AND date_drawn <= lr.date::DATE ) as all
				FROM
					(SELECT '%s'::DATE as date ) as lr
				ORDER BY lr.date::DATE ASC
		"""%self.date

		print query
		self._cr.execute(query)
		result = self._cr.dictfetchall()

		for row in result:
			print row
			self.zero = row['zero']
			self.one = row['one']
			self.one_x2 = row['one_x2']
			self.one_x3 = row['one_x3']
			self.one_two = row['one_two']
			self.one_three = row['one_three']
			self.two = row['two']
			self.two_x2 = row['two_x2']
			self.three = row['three']
			self.three_one = row['three_one']
			self.four = row['four']
			self.five = row['five']

		query="""
				SELECT
					yr.date::DATE,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 1 OR lr.b = 1 OR lr.c = 1 OR lr.d = 1 OR lr.e = 1 OR lr.f = 1) AND lr.date_drawn >= (extract('year' from yr.date::DATE)||'-01-01')::DATE AND lr.date_drawn <= yr.date::DATE)::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) AND date_drawn <= yr.date::DATE )::DECIMAL
					), 2) *100 as one,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 2 OR lr.b = 2 OR lr.c = 2 OR lr.d = 2 OR lr.e = 2 OR lr.f = 2) AND lr.date_drawn >= (extract('year' from yr.date::DATE)||'-01-01')::DATE AND lr.date_drawn <= yr.date::DATE)::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) AND date_drawn <= yr.date::DATE )::DECIMAL
					), 2) *100 as two,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 3 OR lr.b = 3 OR lr.c = 3 OR lr.d = 3 OR lr.e = 3 OR lr.f = 3) AND lr.date_drawn >= (extract('year' from yr.date::DATE)||'-01-01')::DATE AND lr.date_drawn <= yr.date::DATE)::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) AND date_drawn <= yr.date::DATE )::DECIMAL
					), 2) *100 as three,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 4 OR lr.b = 4 OR lr.c = 4 OR lr.d = 4 OR lr.e = 4 OR lr.f = 4) AND lr.date_drawn >= (extract('year' from yr.date::DATE)||'-01-01')::DATE AND lr.date_drawn <= yr.date::DATE)::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) AND date_drawn <= yr.date::DATE )::DECIMAL
					), 2) *100 as four,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 5 OR lr.b = 5 OR lr.c = 5 OR lr.d = 5 OR lr.e = 5 OR lr.f = 5) AND lr.date_drawn >= (extract('year' from yr.date::DATE)||'-01-01')::DATE AND lr.date_drawn <= yr.date::DATE)::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) AND date_drawn <= yr.date::DATE )::DECIMAL
					), 2) *100 as five,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 6 OR lr.b = 6 OR lr.c = 6 OR lr.d = 6 OR lr.e = 6 OR lr.f = 6) AND lr.date_drawn >= (extract('year' from yr.date::DATE)||'-01-01')::DATE AND lr.date_drawn <= yr.date::DATE)::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) AND date_drawn <= yr.date::DATE )::DECIMAL
					), 2) *100 as six,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 7 OR lr.b = 7 OR lr.c = 7 OR lr.d = 7 OR lr.e = 7 OR lr.f = 7) AND lr.date_drawn >= (extract('year' from yr.date::DATE)||'-01-01')::DATE AND lr.date_drawn <= yr.date::DATE)::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) AND date_drawn <= yr.date::DATE )::DECIMAL
					), 2) *100 as seven,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 8 OR lr.b = 8 OR lr.c = 8 OR lr.d = 8 OR lr.e = 8 OR lr.f = 8) AND lr.date_drawn >= (extract('year' from yr.date::DATE)||'-01-01')::DATE AND lr.date_drawn <= yr.date::DATE)::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) AND date_drawn <= yr.date::DATE )::DECIMAL
					), 2) *100 as eight,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 9 OR lr.b = 9 OR lr.c = 9 OR lr.d = 9 OR lr.e = 9 OR lr.f = 9) AND lr.date_drawn >= (extract('year' from yr.date::DATE)||'-01-01')::DATE AND lr.date_drawn <= yr.date::DATE)::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) AND date_drawn <= yr.date::DATE )::DECIMAL
					), 2) *100 as nine,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 10 OR lr.b = 10 OR lr.c = 10 OR lr.d = 10 OR lr.e = 10 OR lr.f = 10) AND lr.date_drawn >= (extract('year' from yr.date::DATE)||'-01-01')::DATE AND lr.date_drawn <= yr.date::DATE)::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) AND date_drawn <= yr.date::DATE )::DECIMAL
					), 2) *100 as ten,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 11 OR lr.b = 11 OR lr.c = 11 OR lr.d = 11 OR lr.e = 11 OR lr.f = 11) AND lr.date_drawn >= (extract('year' from yr.date::DATE)||'-01-01')::DATE AND lr.date_drawn <= yr.date::DATE)::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) AND date_drawn <= yr.date::DATE )::DECIMAL
					), 2) *100 as eleven,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 12 OR lr.b = 12 OR lr.c = 12 OR lr.d = 12 OR lr.e = 12 OR lr.f = 12) AND lr.date_drawn >= (extract('year' from yr.date::DATE)||'-01-01')::DATE AND lr.date_drawn <= yr.date::DATE)::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) AND date_drawn <= yr.date::DATE )::DECIMAL
					), 2) *100 as twelve,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 13 OR lr.b = 13 OR lr.c = 13 OR lr.d = 13 OR lr.e = 13 OR lr.f = 13) AND lr.date_drawn >= (extract('year' from yr.date::DATE)||'-01-01')::DATE AND lr.date_drawn <= yr.date::DATE)::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) AND date_drawn <= yr.date::DATE )::DECIMAL
					), 2) *100 as thirteen,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 14 OR lr.b = 14 OR lr.c = 14 OR lr.d = 14 OR lr.e = 14 OR lr.f = 14) AND lr.date_drawn >= (extract('year' from yr.date::DATE)||'-01-01')::DATE AND lr.date_drawn <= yr.date::DATE)::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) AND date_drawn <= yr.date::DATE )::DECIMAL
					), 2) *100 as fourteen,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 15 OR lr.b = 15 OR lr.c = 15 OR lr.d = 15 OR lr.e = 15 OR lr.f = 15) AND lr.date_drawn >= (extract('year' from yr.date::DATE)||'-01-01')::DATE AND lr.date_drawn <= yr.date::DATE)::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) AND date_drawn <= yr.date::DATE )::DECIMAL
					), 2) *100 as fifteen,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 16 OR lr.b = 16 OR lr.c = 16 OR lr.d = 16 OR lr.e = 16 OR lr.f = 16) AND lr.date_drawn >= (extract('year' from yr.date::DATE)||'-01-01')::DATE AND lr.date_drawn <= yr.date::DATE)::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) AND date_drawn <= yr.date::DATE )::DECIMAL
					), 2) *100 as sixteen,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 17 OR lr.b = 17 OR lr.c = 17 OR lr.d = 17 OR lr.e = 17 OR lr.f = 17) AND lr.date_drawn >= (extract('year' from yr.date::DATE)||'-01-01')::DATE AND lr.date_drawn <= yr.date::DATE)::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) AND date_drawn <= yr.date::DATE )::DECIMAL
					), 2) *100 as seventeen,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 18 OR lr.b = 18 OR lr.c = 18 OR lr.d = 18 OR lr.e = 18 OR lr.f = 18) AND lr.date_drawn >= (extract('year' from yr.date::DATE)||'-01-01')::DATE AND lr.date_drawn <= yr.date::DATE)::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) AND date_drawn <= yr.date::DATE )::DECIMAL
					), 2) *100 as eighteen,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 19 OR lr.b = 19 OR lr.c = 19 OR lr.d = 19 OR lr.e = 19 OR lr.f = 19) AND lr.date_drawn >= (extract('year' from yr.date::DATE)||'-01-01')::DATE AND lr.date_drawn <= yr.date::DATE)::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) AND date_drawn <= yr.date::DATE )::DECIMAL
					), 2) *100 as nineteen,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 20 OR lr.b = 20 OR lr.c = 20 OR lr.d = 20 OR lr.e = 20 OR lr.f = 20) AND lr.date_drawn >= (extract('year' from yr.date::DATE)||'-01-01')::DATE AND lr.date_drawn <= yr.date::DATE)::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) AND date_drawn <= yr.date::DATE )::DECIMAL
					), 2) *100 as twenty,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 21 OR lr.b = 21 OR lr.c = 21 OR lr.d = 21 OR lr.e = 21 OR lr.f = 21) AND lr.date_drawn >= (extract('year' from yr.date::DATE)||'-01-01')::DATE AND lr.date_drawn <= yr.date::DATE)::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) AND date_drawn <= yr.date::DATE )::DECIMAL
					), 2) *100 as twentyone,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 22 OR lr.b = 22 OR lr.c = 22 OR lr.d = 22 OR lr.e = 22 OR lr.f = 22) AND lr.date_drawn >= (extract('year' from yr.date::DATE)||'-01-01')::DATE AND lr.date_drawn <= yr.date::DATE)::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) AND date_drawn <= yr.date::DATE )::DECIMAL
					), 2) *100 as twentytwo,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 23 OR lr.b = 23 OR lr.c = 23 OR lr.d = 23 OR lr.e = 23 OR lr.f = 23) AND lr.date_drawn >= (extract('year' from yr.date::DATE)||'-01-01')::DATE AND lr.date_drawn <= yr.date::DATE)::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) AND date_drawn <= yr.date::DATE )::DECIMAL
					), 2) *100 as twentythree,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 24 OR lr.b = 24 OR lr.c = 24 OR lr.d = 24 OR lr.e = 24 OR lr.f = 24) AND lr.date_drawn >= (extract('year' from yr.date::DATE)||'-01-01')::DATE AND lr.date_drawn <= yr.date::DATE)::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) AND date_drawn <= yr.date::DATE )::DECIMAL
					), 2) *100 as twentyfour,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 25 OR lr.b = 25 OR lr.c = 25 OR lr.d = 25 OR lr.e = 25 OR lr.f = 25) AND lr.date_drawn >= (extract('year' from yr.date::DATE)||'-01-01')::DATE AND lr.date_drawn <= yr.date::DATE)::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) AND date_drawn <= yr.date::DATE )::DECIMAL
					), 2) *100 as twentyfive,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 26 OR lr.b = 26 OR lr.c = 26 OR lr.d = 26 OR lr.e = 26 OR lr.f = 26) AND lr.date_drawn >= (extract('year' from yr.date::DATE)||'-01-01')::DATE AND lr.date_drawn <= yr.date::DATE)::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) AND date_drawn <= yr.date::DATE )::DECIMAL
					), 2) *100 as twentysix,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 27 OR lr.b = 27 OR lr.c = 27 OR lr.d = 27 OR lr.e = 27 OR lr.f = 27) AND lr.date_drawn >= (extract('year' from yr.date::DATE)||'-01-01')::DATE AND lr.date_drawn <= yr.date::DATE)::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) AND date_drawn <= yr.date::DATE )::DECIMAL
					), 2) *100 as twentyseven,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 28 OR lr.b = 28 OR lr.c = 28 OR lr.d = 28 OR lr.e = 28 OR lr.f = 28) AND lr.date_drawn >= (extract('year' from yr.date::DATE)||'-01-01')::DATE AND lr.date_drawn <= yr.date::DATE)::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) AND date_drawn <= yr.date::DATE )::DECIMAL
					), 2) *100 as twentyeight,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 29 OR lr.b = 29 OR lr.c = 29 OR lr.d = 29 OR lr.e = 29 OR lr.f = 29) AND lr.date_drawn >= (extract('year' from yr.date::DATE)||'-01-01')::DATE AND lr.date_drawn <= yr.date::DATE)::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) AND date_drawn <= yr.date::DATE )::DECIMAL
					), 2) *100 as twentynine,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 30 OR lr.b = 30 OR lr.c = 30 OR lr.d = 30 OR lr.e = 30 OR lr.f = 30) AND lr.date_drawn >= (extract('year' from yr.date::DATE)||'-01-01')::DATE AND lr.date_drawn <= yr.date::DATE)::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) AND date_drawn <= yr.date::DATE )::DECIMAL
					), 2) *100 as thirty,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 31 OR lr.b = 31 OR lr.c = 31 OR lr.d = 31 OR lr.e = 31 OR lr.f = 31) AND lr.date_drawn >= (extract('year' from yr.date::DATE)||'-01-01')::DATE AND lr.date_drawn <= yr.date::DATE)::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) AND date_drawn <= yr.date::DATE )::DECIMAL
					), 2) *100 as thirtyone,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 32 OR lr.b = 32 OR lr.c = 32 OR lr.d = 32 OR lr.e = 32 OR lr.f = 32) AND lr.date_drawn >= (extract('year' from yr.date::DATE)||'-01-01')::DATE AND lr.date_drawn <= yr.date::DATE)::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) AND date_drawn <= yr.date::DATE )::DECIMAL
					), 2) *100 as thirtytwo,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 33 OR lr.b = 33 OR lr.c = 33 OR lr.d = 33 OR lr.e = 33 OR lr.f = 33) AND lr.date_drawn >= (extract('year' from yr.date::DATE)||'-01-01')::DATE AND lr.date_drawn <= yr.date::DATE)::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) AND date_drawn <= yr.date::DATE )::DECIMAL
					), 2) *100 as thirtythree,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 34 OR lr.b = 34 OR lr.c = 34 OR lr.d = 34 OR lr.e = 34 OR lr.f = 34) AND lr.date_drawn >= (extract('year' from yr.date::DATE)||'-01-01')::DATE AND lr.date_drawn <= yr.date::DATE)::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) AND date_drawn <= yr.date::DATE )::DECIMAL
					), 2) *100 as thirtyfour,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 35 OR lr.b = 35 OR lr.c = 35 OR lr.d = 35 OR lr.e = 35 OR lr.f = 35) AND lr.date_drawn >= (extract('year' from yr.date::DATE)||'-01-01')::DATE AND lr.date_drawn <= yr.date::DATE)::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) AND date_drawn <= yr.date::DATE )::DECIMAL
					), 2) *100 as thirtyfive,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 36 OR lr.b = 36 OR lr.c = 36 OR lr.d = 36 OR lr.e = 36 OR lr.f = 36) AND lr.date_drawn >= (extract('year' from yr.date::DATE)||'-01-01')::DATE AND lr.date_drawn <= yr.date::DATE)::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) AND date_drawn <= yr.date::DATE )::DECIMAL
					), 2) *100 as thirtysix,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 37 OR lr.b = 37 OR lr.c = 37 OR lr.d = 37 OR lr.e = 37 OR lr.f = 37) AND lr.date_drawn >= (extract('year' from yr.date::DATE)||'-01-01')::DATE AND lr.date_drawn <= yr.date::DATE)::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) AND date_drawn <= yr.date::DATE )::DECIMAL
					), 2) *100 as thirtyseven,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 38 OR lr.b = 38 OR lr.c = 38 OR lr.d = 38 OR lr.e = 38 OR lr.f = 38) AND lr.date_drawn >= (extract('year' from yr.date::DATE)||'-01-01')::DATE AND lr.date_drawn <= yr.date::DATE)::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) AND date_drawn <= yr.date::DATE )::DECIMAL
					), 2) *100 as thirtyeight,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 39 OR lr.b = 39 OR lr.c = 39 OR lr.d = 39 OR lr.e = 39 OR lr.f = 39) AND lr.date_drawn >= (extract('year' from yr.date::DATE)||'-01-01')::DATE AND lr.date_drawn <= yr.date::DATE)::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) AND date_drawn <= yr.date::DATE )::DECIMAL
					), 2) *100 as thirtynine,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 40 OR lr.b = 40 OR lr.c = 40 OR lr.d = 40 OR lr.e = 40 OR lr.f = 40) AND lr.date_drawn >= (extract('year' from yr.date::DATE)||'-01-01')::DATE AND lr.date_drawn <= yr.date::DATE)::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) AND date_drawn <= yr.date::DATE )::DECIMAL
					), 2) *100 as fourty,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 41 OR lr.b = 41 OR lr.c = 41 OR lr.d = 41 OR lr.e = 41 OR lr.f = 41) AND lr.date_drawn >= (extract('year' from yr.date::DATE)||'-01-01')::DATE AND lr.date_drawn <= yr.date::DATE)::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) AND date_drawn <= yr.date::DATE )::DECIMAL
					), 2) *100 as fourtyone,
						round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 41 OR lr.b = 41 OR lr.c = 41 OR lr.d = 41 OR lr.e = 41 OR lr.f = 41) AND lr.date_drawn >= (extract('year' from yr.date::DATE)||'-01-01')::DATE AND lr.date_drawn <= yr.date::DATE)::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) AND date_drawn <= yr.date::DATE )::DECIMAL
					), 2) *100 as fourtytwo,				


					(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) AND date_drawn <= yr.date::DATE ) as all

				FROM
					(SELECT '%s'::DATE as date ) as yr
				ORDER BY yr.date::DATE ASC
		"""%self.date

		print query
		self._cr.execute(query)
		result = self._cr.dictfetchall()

		for row in result:
			print row
			self.x_1 = row['one']
			self.x_2 = row['two']
			self.x_3 = row['three']
			self.x_4 = row['four']
			self.x_5 = row['five']
			self.x_6 = row['six']
			self.x_7 = row['seven']
			self.x_8 = row['eight']
			self.x_9 = row['nine']
			self.x_10 = row['ten']
			self.x_11 = row['eleven']
			self.x_12 = row['twelve']
			self.x_13 = row['thirteen']
			self.x_14 = row['fourteen']
			self.x_15 = row['fifteen']
			self.x_16 = row['sixteen']
			self.x_17 = row['seventeen']
			self.x_18 = row['eighteen']
			self.x_19 = row['nineteen']
			self.x_20 = row['twenty']
			self.x_21 = row['twentyone']
			self.x_22 = row['twentytwo']
			self.x_23 = row['twentythree']
			self.x_24 = row['twentyfour']
			self.x_25 = row['twentyfive']
			self.x_26 = row['twentysix']
			self.x_27 = row['twentyseven']
			self.x_28 = row['twentyeight']
			self.x_29 = row['twentynine']
			self.x_30 = row['thirty']			
			self.x_31 = row['thirtyone']
			self.x_32 = row['thirtytwo']
			self.x_33 = row['thirtythree']
			self.x_34 = row['thirtyfour']
			self.x_35 = row['thirtyfive']
			self.x_36 = row['thirtysix']
			self.x_37 = row['thirtyseven']
			self.x_38 = row['thirtyeight']
			self.x_39 = row['thirtynine']
			self.x_40 = row['fourty']
			self.x_41 = row['fourtyone']
			self.x_42 = row['fourtytwo']

		#======================================================================== Statistics ======================================================================== 
		query="""
				SELECT
					lr.date::DATE,
					round((
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from lr.date::DATE) AND consecutive = 'zero')::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from lr.date::DATE) )::DECIMAL
					), 2) *100 as zero,
					round((
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from lr.date::DATE) AND consecutive = 'one')::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from lr.date::DATE) )::DECIMAL
					), 2) *100 as one,
					round((
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from lr.date::DATE) AND consecutive like 'one_x2')::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from lr.date::DATE) )::DECIMAL
					), 2) *100 as one_x2,
					round((
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from lr.date::DATE) AND consecutive = 'one_x3')::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from lr.date::DATE) )::DECIMAL
					), 2) *100 as one_x3,
					round((
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from lr.date::DATE) AND consecutive = 'one_two')::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from lr.date::DATE) )::DECIMAL
					), 2) *100 as one_two,
					round((
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from lr.date::DATE) AND consecutive = 'one_three')::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from lr.date::DATE) )::DECIMAL
					), 2) *100 as one_three,
					round((
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from lr.date::DATE) AND consecutive = 'two')::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from lr.date::DATE) )::DECIMAL
					), 2) *100 as two,
					round((
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from lr.date::DATE) AND consecutive = 'two_x2')::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from lr.date::DATE) )::DECIMAL
					), 2) *100 as two_x2,
					round((
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from lr.date::DATE) AND consecutive = 'three')::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from lr.date::DATE) )::DECIMAL
					), 2) *100 as three,
					round((
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from lr.date::DATE) AND consecutive = 'three_one')::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from lr.date::DATE) )::DECIMAL
					), 2) *100 as three_one,
					round((
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from lr.date::DATE) AND consecutive = 'four')::DECIMAL 
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from lr.date::DATE) )::DECIMAL
					), 2) *100 as four,
					round((
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from lr.date::DATE) AND consecutive = 'five')::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from lr.date::DATE) )::DECIMAL 
					), 2) *100 as five,
					
					(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from lr.date::DATE) AND date_drawn <= lr.date::DATE ) as all

				FROM
					(SELECT '%s'::DATE as date ) as lr
				ORDER BY lr.date::DATE ASC
		"""%self.date

		print query
		self._cr.execute(query)
		result = self._cr.dictfetchall()

		for row in result:
			print row
			self.b_zero = row['zero']
			self.b_one = row['one']
			self.b_one_x2 = row['one_x2']
			self.b_one_x3 = row['one_x3']
			self.b_one_two = row['one_two']
			self.b_one_three = row['one_three']
			self.b_two = row['two']
			self.b_two_x2 = row['two_x2']
			self.b_three = row['three']
			self.b_three_one = row['three_one']
			self.b_four = row['four']
			self.b_five = row['five']

		query="""
				SELECT
					yr.date::DATE,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 1 OR lr.b = 1 OR lr.c = 1 OR lr.d = 1 OR lr.e = 1 OR lr.f = 1) AND lr.year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
					), 2) *100 as one,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 2 OR lr.b = 2 OR lr.c = 2 OR lr.d = 2 OR lr.e = 2 OR lr.f = 2) AND lr.year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
					), 2) *100 as two,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 3 OR lr.b = 3 OR lr.c = 3 OR lr.d = 3 OR lr.e = 3 OR lr.f = 3) AND lr.year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
					), 2) *100 as three,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 4 OR lr.b = 4 OR lr.c = 4 OR lr.d = 4 OR lr.e = 4 OR lr.f = 4) AND lr.year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
					), 2) *100 as four,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 5 OR lr.b = 5 OR lr.c = 5 OR lr.d = 5 OR lr.e = 5 OR lr.f = 5) AND lr.year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
					), 2) *100 as five,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 6 OR lr.b = 6 OR lr.c = 6 OR lr.d = 6 OR lr.e = 6 OR lr.f = 6) AND lr.year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
					), 2) *100 as six,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 7 OR lr.b = 7 OR lr.c = 7 OR lr.d = 7 OR lr.e = 7 OR lr.f = 7) AND lr.year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
					), 2) *100 as seven,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 8 OR lr.b = 8 OR lr.c = 8 OR lr.d = 8 OR lr.e = 8 OR lr.f = 8) AND lr.year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
					), 2) *100 as eight,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 9 OR lr.b = 9 OR lr.c = 9 OR lr.d = 9 OR lr.e = 9 OR lr.f = 9) AND lr.year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
					), 2) *100 as nine,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 10 OR lr.b = 10 OR lr.c = 10 OR lr.d = 10 OR lr.e = 10 OR lr.f = 10) AND lr.year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
					), 2) *100 as ten,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 11 OR lr.b = 11 OR lr.c = 11 OR lr.d = 11 OR lr.e = 11 OR lr.f = 11) AND lr.year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
					), 2) *100 as eleven,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 12 OR lr.b = 12 OR lr.c = 12 OR lr.d = 12 OR lr.e = 12 OR lr.f = 12) AND lr.year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
					), 2) *100 as twelve,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 13 OR lr.b = 13 OR lr.c = 13 OR lr.d = 13 OR lr.e = 13 OR lr.f = 13) AND lr.year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
					), 2) *100 as thirteen,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 14 OR lr.b = 14 OR lr.c = 14 OR lr.d = 14 OR lr.e = 14 OR lr.f = 14) AND lr.year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
					), 2) *100 as fourteen,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 15 OR lr.b = 15 OR lr.c = 15 OR lr.d = 15 OR lr.e = 15 OR lr.f = 15) AND lr.year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
					), 2) *100 as fifteen,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 16 OR lr.b = 16 OR lr.c = 16 OR lr.d = 16 OR lr.e = 16 OR lr.f = 16) AND lr.year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
					), 2) *100 as sixteen,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 17 OR lr.b = 17 OR lr.c = 17 OR lr.d = 17 OR lr.e = 17 OR lr.f = 17) AND lr.year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
					), 2) *100 as seventeen,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 18 OR lr.b = 18 OR lr.c = 18 OR lr.d = 18 OR lr.e = 18 OR lr.f = 18) AND lr.year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
					), 2) *100 as eighteen,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 19 OR lr.b = 19 OR lr.c = 19 OR lr.d = 19 OR lr.e = 19 OR lr.f = 19) AND lr.year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
					), 2) *100 as nineteen,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 20 OR lr.b = 20 OR lr.c = 20 OR lr.d = 20 OR lr.e = 20 OR lr.f = 20) AND lr.year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
					), 2) *100 as twenty,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 21 OR lr.b = 21 OR lr.c = 21 OR lr.d = 21 OR lr.e = 21 OR lr.f = 21) AND lr.year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
					), 2) *100 as twentyone,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 22 OR lr.b = 22 OR lr.c = 22 OR lr.d = 22 OR lr.e = 22 OR lr.f = 22) AND lr.year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
					), 2) *100 as twentytwo,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 23 OR lr.b = 23 OR lr.c = 23 OR lr.d = 23 OR lr.e = 23 OR lr.f = 23) AND lr.year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
					), 2) *100 as twentythree,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 24 OR lr.b = 24 OR lr.c = 24 OR lr.d = 24 OR lr.e = 24 OR lr.f = 24) AND lr.year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
					), 2) *100 as twentyfour,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 25 OR lr.b = 25 OR lr.c = 25 OR lr.d = 25 OR lr.e = 25 OR lr.f = 25) AND lr.year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
					), 2) *100 as twentyfive,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 26 OR lr.b = 26 OR lr.c = 26 OR lr.d = 26 OR lr.e = 26 OR lr.f = 26) AND lr.year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
					), 2) *100 as twentysix,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 27 OR lr.b = 27 OR lr.c = 27 OR lr.d = 27 OR lr.e = 27 OR lr.f = 27) AND lr.year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
					), 2) *100 as twentyseven,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 28 OR lr.b = 28 OR lr.c = 28 OR lr.d = 28 OR lr.e = 28 OR lr.f = 28) AND lr.year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
					), 2) *100 as twentyeight,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 29 OR lr.b = 29 OR lr.c = 29 OR lr.d = 29 OR lr.e = 29 OR lr.f = 29) AND lr.year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
					), 2) *100 as twentynine,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 30 OR lr.b = 30 OR lr.c = 30 OR lr.d = 30 OR lr.e = 30 OR lr.f = 30) AND lr.year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
					), 2) *100 as thirty,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 31 OR lr.b = 31 OR lr.c = 31 OR lr.d = 31 OR lr.e = 31 OR lr.f = 31) AND lr.year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
					), 2) *100 as thirtyone,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 32 OR lr.b = 32 OR lr.c = 32 OR lr.d = 32 OR lr.e = 32 OR lr.f = 32) AND lr.year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
					), 2) *100 as thirtytwo,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 33 OR lr.b = 33 OR lr.c = 33 OR lr.d = 33 OR lr.e = 33 OR lr.f = 33) AND lr.year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
					), 2) *100 as thirtythree,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 34 OR lr.b = 34 OR lr.c = 34 OR lr.d = 34 OR lr.e = 34 OR lr.f = 34) AND lr.year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
					), 2) *100 as thirtyfour,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 35 OR lr.b = 35 OR lr.c = 35 OR lr.d = 35 OR lr.e = 35 OR lr.f = 35) AND lr.year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
					), 2) *100 as thirtyfive,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 36 OR lr.b = 36 OR lr.c = 36 OR lr.d = 36 OR lr.e = 36 OR lr.f = 36) AND lr.year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
					), 2) *100 as thirtysix,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 37 OR lr.b = 37 OR lr.c = 37 OR lr.d = 37 OR lr.e = 37 OR lr.f = 37) AND lr.year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
					), 2) *100 as thirtyseven,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 38 OR lr.b = 38 OR lr.c = 38 OR lr.d = 38 OR lr.e = 38 OR lr.f = 38) AND lr.year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
					), 2) *100 as thirtyeight,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 39 OR lr.b = 39 OR lr.c = 39 OR lr.d = 39 OR lr.e = 39 OR lr.f = 39) AND lr.year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
					), 2) *100 as thirtynine,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 40 OR lr.b = 40 OR lr.c = 40 OR lr.d = 40 OR lr.e = 40 OR lr.f = 40) AND lr.year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
					), 2) *100 as fourty,
					round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 41 OR lr.b = 41 OR lr.c = 41 OR lr.d = 41 OR lr.e = 41 OR lr.f = 41) AND lr.year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
					), 2) *100 as fourtyone,
						round((
						(SELECT
							count(*)
						FROM
							lotto_records lr 
						WHERE (lr.a = 41 OR lr.b = 41 OR lr.c = 41 OR lr.d = 41 OR lr.e = 41 OR lr.f = 41) AND lr.year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
						/
						(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) )::DECIMAL
					), 2) *100 as fourtytwo,				


					(SELECT count(*) FROM lotto_records WHERE year::INT = EXTRACT( year from yr.date::DATE) ) as all

				FROM
					(SELECT '%s'::DATE as date ) as yr
				ORDER BY yr.date::DATE ASC
		"""%self.date

		print query
		self._cr.execute(query)
		result = self._cr.dictfetchall()

		for row in result:
			print row
			self.b_1 = row['one']
			self.b_2 = row['two']
			self.b_3 = row['three']
			self.b_4 = row['four']
			self.b_5 = row['five']
			self.b_6 = row['six']
			self.b_7 = row['seven']
			self.b_8 = row['eight']
			self.b_9 = row['nine']
			self.b_10 = row['ten']
			self.b_11 = row['eleven']
			self.b_12 = row['twelve']
			self.b_13 = row['thirteen']
			self.b_14 = row['fourteen']
			self.b_15 = row['fifteen']
			self.b_16 = row['sixteen']
			self.b_17 = row['seventeen']
			self.b_18 = row['eighteen']
			self.b_19 = row['nineteen']
			self.b_20 = row['twenty']
			self.b_21 = row['twentyone']
			self.b_22 = row['twentytwo']
			self.b_23 = row['twentythree']
			self.b_24 = row['twentyfour']
			self.b_25 = row['twentyfive']
			self.b_26 = row['twentysix']
			self.b_27 = row['twentyseven']
			self.b_28 = row['twentyeight']
			self.b_29 = row['twentynine']
			self.b_30 = row['thirty']			
			self.b_31 = row['thirtyone']
			self.b_32 = row['thirtytwo']
			self.b_33 = row['thirtythree']
			self.b_34 = row['thirtyfour']
			self.b_35 = row['thirtyfive']
			self.b_36 = row['thirtysix']
			self.b_37 = row['thirtyseven']
			self.b_38 = row['thirtyeight']
			self.b_39 = row['thirtynine']
			self.b_40 = row['fourty']
			self.b_41 = row['fourtyone']
			self.b_42 = row['fourtytwo']

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


