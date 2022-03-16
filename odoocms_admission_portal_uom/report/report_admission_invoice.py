import pdb
from odoo import api, fields, models, _
from odoo.exceptions import UserError
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta
from pytz import timezone, utc
import time

from odoo import http
import logging

_logger = logging.getLogger(__name__)


class AdmissionInvoice(models.AbstractModel):
    _name = 'report.odoocms_admission_portal.report_admission_invoice'
    _description = 'Admission Online Invoice'

    @api.model
    def _get_report_values(self, docsid, data=None):
        application_ids = self.env['odoocms.application'].browse(docsid)

        disciplines = 0
        discipline = 0
        prefs = self.env['odoocms.application.preference'].search([('application_id', '=', application_ids[0].id)])
        # for pref in prefs:
        #     if pref.discipline_id.id != discipline:
        #         discipline = pref.discipline_id.id
        #         disciplines = disciplines + 1

        registration_fee_international = http.request.env['ir.config_parameter'].sudo().get_param(
            'odoocms_admission_portal.registration_fee_international')
        registration_fee = http.request.env['ir.config_parameter'].sudo().get_param(
            'odoocms_admission_portal.registration_fee')
        additional_fee = http.request.env['ir.config_parameter'].sudo().get_param(
            'odoocms_admission_portal.additional_fee')

        account_payable = http.request.env['ir.config_parameter'].sudo().get_param(
            'odoocms_admission_portal.account_payable')
        account_title = http.request.env['ir.config_parameter'].sudo().get_param(
            'odoocms_admission_portal.account_title')
        account_no = http.request.env['ir.config_parameter'].sudo().get_param('odoocms_admission_portal.account_no')

        account_payable2 = http.request.env['ir.config_parameter'].sudo().get_param(
            'odoocms_admission_portal.account_payable2')
        account_title2 = http.request.env['ir.config_parameter'].sudo().get_param(
            'odoocms_admission_portal.account_title2')
        account_no2 = http.request.env['ir.config_parameter'].sudo().get_param('odoocms_admission_portal.account_no2')

        total_fee = int(float(registration_fee))
        if len(prefs) < 4:
            total_fee

        if len(prefs) >= 4 and  len(prefs) < 7:
            total_fee += 2000

        if len(prefs) >= 7 and  len(prefs) < 10:
            total_fee += 4000

        if len(prefs) >= 10 and  len(prefs) < 14:
            total_fee += 6000

        if len(prefs) >= 14 and  len(prefs) < 17:
            total_fee += 8000

        if len(prefs) >= 17 and  len(prefs) < 20:
            total_fee += 10000
        quota_numbers = len(application_ids[0].quota_ids)
        if quota_numbers > 1:
            quota_numbers = quota_numbers - 1
            total_fee += quota_numbers * 2000

        docargs = {
            'application_ids': application_ids or False,
            'account_payable': account_payable or "",
            'account_payable2': account_payable2 or "",
            'registration_fee': registration_fee or False,
            'additional_fee': additional_fee or False,
            'total_fee': str(total_fee),
            'registration_fee_international': registration_fee_international or False,
            'account_title': account_title or "",
            'account_title2': account_title2 or "",
            'account_no': account_no or "",
            'account_no2': account_no2 or "",
            'disciplines': disciplines,
            'today': date.today() or False,
        }
        return docargs
