from openerp import models, fields, api, _
from openerp.exceptions import except_orm, Warning, RedirectWarning
from openerp.tools import float_compare
import openerp.addons.decimal_precision as dp
import math
from math import modf

class summary_result(models.TransientModel):
	_name = 'summary.result'

	#date = fields.Date(string='Date',  required=True)
	year = fields.Selection( [('2015', '2015'),('2016', '2016'),('2017', '2017'),('all', "All")], string='Year'  )

	output_type = fields.Selection(
									[('pdf', 'Portable Document (pdf)'),
									('xls', 'Excel Spreadsheet (xls)')],
									string='Report format', help='Choose the format for the output', default='pdf',  required=True)

	def print_report(self, cr, uid, ids, data, context=None):

		if context is None:
			context = {}

		this = self.browse(cr, uid, ids[0], context=context)
		current_user = self.pool.get('res.users').browse(cr, uid, uid, context=context)
		#print current_user
		#print current_user.name
		#print this.year
		if this.year == 'all':
			values = {
					'type': 'ir.actions.report.xml',
					'report_name': 'summary.result.report.2', 
					'datas': {
							'output_type': this.output_type,
							'variables': {
								'this_year' : this.year,
								'username' : current_user.name,
							}
						},
					}	
		else:
			values = {
					'type': 'ir.actions.report.xml',
					'report_name': 'summary.result.report', 
					'datas': {
							'output_type': this.output_type,
							'variables': {
								'this_year' : this.year,
								'username' : current_user.name,
							}
						},
					}	
		#print values
		return values

class summary_result_v2(models.TransientModel):
	_name = 'summary.result.v2'

	#date = fields.Date(string='Date',  required=True)
	year = fields.Selection( [('2015', '2015'),('2016', '2016'),('2017', '2017'),('all', "All")], string='Year'  )

	output_type = fields.Selection(
									[('pdf', 'Portable Document (pdf)'),
									('xls', 'Excel Spreadsheet (xls)')],
									string='Report format', help='Choose the format for the output', default='pdf',  required=True)

	def print_report(self, cr, uid, ids, data, context=None):

		if context is None:
			context = {}

		this = self.browse(cr, uid, ids[0], context=context)
		current_user = self.pool.get('res.users').browse(cr, uid, uid, context=context)
		#print current_user
		#print current_user.name
		#print this.year
		if this.year == 'all':
			values = {
					'type': 'ir.actions.report.xml',
					'report_name': 'summary.result.report.v2.2', 
					'datas': {
							'output_type': this.output_type,
							'variables': {
								'this_year' : this.year,
								'username' : current_user.name,
							}
						},
					}	
		else:
			values = {
					'type': 'ir.actions.report.xml',
					'report_name': 'summary.result.report.v2', 
					'datas': {
							'output_type': this.output_type,
							'variables': {
								'this_year' : this.year,
								'username' : current_user.name,
							}
						},
					}	
		#print values
		return values

class daily_reporting(models.TransientModel):
	_name = 'daily.reporting'

	date = fields.Date(string='Date',  required=True)


	output_type = fields.Selection(
									[('pdf', 'Portable Document (pdf)')],
									string='Report format', help='Choose the format for the output', default='pdf',  required=True)

	def print_report(self, cr, uid, ids, data, context=None):

		if context is None:
			context = {}

		this = self.browse(cr, uid, ids[0], context=context)
		current_user = self.pool.get('res.users').browse(cr, uid, uid, context=context)
		print current_user
		print current_user.name


		values = {
				'type': 'ir.actions.report.xml',
				'report_name': 'daily.reporting.report', 
				'datas': {
						'output_type': this.output_type,
						'variables': {
							'date' : this.date,
							'username' : current_user.name,
						}
					},
				}	

		return values
	




