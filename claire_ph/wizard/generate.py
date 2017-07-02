from openerp import models, fields, api, _
from openerp.exceptions import except_orm, Warning, RedirectWarning
from openerp.tools import float_compare
import openerp.addons.decimal_precision as dp
import math
from math import modf

class overall_summary(models.Model):
	_name = 'overall.summary'
	
	date = fields.Date(string='Date')

	high = fields.Char()
	low = fields.Char()

	hl_zero_six = fields.Char()
	hl_one_five = fields.Char()
	hl_two_four = fields.Char()
	hl_three_three = fields.Char()
	hl_four_two = fields.Char()
	hl_five_one = fields.Char()
	hl_six_zero = fields.Char()

	odd = fields.Char()
	even = fields.Char()

	oe_zero_six = fields.Char()
	oe_one_five = fields.Char()
	oe_two_four = fields.Char()
	oe_three_three = fields.Char()
	oe_four_two = fields.Char()
	oe_five_one = fields.Char()
	oe_six_zero = fields.Char()

	def generate(self, cr, uid, ids, data, context=None):
		this = self.browse(cr, uid, ids[0], context=context)
		print 'Generating...'

		print 'Done!'



