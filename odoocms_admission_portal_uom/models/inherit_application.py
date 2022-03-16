import re

from odoo import fields, models, _, api
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from odoo.tools.safe_eval import safe_eval
import pdb
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning

from odoo.http import content_disposition, Controller, request, route
import random


class OdooCMSAdmissionApplication(models.Model):
    _inherit = 'odoocms.application'

    name = fields.Char('Name')
    distance_university = fields.Integer('Distance From University (KM)')
    roll_number_lat = fields.Char('Roll Number LAT')
    marks_lat = fields.Char('LAT Marks')
    roll_number_etea = fields.Char('Roll Number ETEA')
    marks_etea = fields.Char('ETEA Marks')
    quota_ids = fields.One2many('odoocms.admission.applicant.quota', 'application_id', 'Quotas')
    quota_total = fields.Integer(compute='quota_cal', string='Total Quota Selected', store=True)
    total_amount = fields.Integer(compute='total_amount_cal', string='Total Amount System Generated', store=True)

    @api.depends('quota_ids')
    def quota_cal(self):
        self.quota_total = 0
        for rec in self.quota_ids:
            self.quota_total += 1

    @api.depends('quota_ids', 'preference_ids')
    def total_amount_cal(self):
        self.total_amount = 0
        for rec in self:
            if len(rec.preference_ids) <= 3 and len(rec.quota_ids) <= 1:
                self.total_amount = 2000
            if len(rec.preference_ids) <= 3 and len(rec.quota_ids) == 2:
                self.total_amount = 4000
            if len(rec.preference_ids) <= 3 and len(rec.quota_ids) == 3:
                self.total_amount = 6000
            if len(rec.preference_ids) <= 3 and len(rec.quota_ids) == 4:
                self.total_amount = 8000
            if len(rec.preference_ids) <= 3 and len(rec.quota_ids) == 5:
                self.total_amount = 10000
            if 3 < len(rec.preference_ids) <= 6 and len(rec.quota_ids) <= 1:
                self.total_amount = 4000
            if 3 < len(rec.preference_ids) <= 6 and len(rec.quota_ids) == 2:
                self.total_amount = 6000
            if 3 < len(rec.preference_ids) <= 6 and len(rec.quota_ids) == 3:
                self.total_amount = 8000
            if 3 < len(rec.preference_ids) <= 6 and len(rec.quota_ids) == 4:
                self.total_amount = 10000
            if 3 < len(rec.preference_ids) <= 6 and len(rec.quota_ids) == 5:
                self.total_amount = 12000

            if 6 < len(rec.preference_ids) <= 9 and len(rec.quota_ids) <= 1:
                self.total_amount = 6000
            if 6 < len(rec.preference_ids) <= 9 and len(rec.quota_ids) == 2:
                self.total_amount = 8000
            if 6 < len(rec.preference_ids) <= 9 and len(rec.quota_ids) == 3:
                self.total_amount = 10000
            if 6 < len(rec.preference_ids) <= 9 and len(rec.quota_ids) == 4:
                self.total_amount = 12000
            if 6 < len(rec.preference_ids) <= 9 and len(rec.quota_ids) == 5:
                self.total_amount = 14000

            if 9 < len(rec.preference_ids) <= 12 and len(rec.quota_ids) <= 1:
                self.total_amount = 8000
            if 9 < len(rec.preference_ids) <= 12 and len(rec.quota_ids) == 2:
                self.total_amount = 10000
            if 9 < len(rec.preference_ids) <= 12 and len(rec.quota_ids) == 3:
                self.total_amount = 12000
            if 9 < len(rec.preference_ids) <= 12 and len(rec.quota_ids) == 4:
                self.total_amount = 14000
            if 9 < len(rec.preference_ids) <= 12 and len(rec.quota_ids) == 5:
                self.total_amount = 16000

    # quota_ids = fields.Many2many('odoocms.admission.quota', 'admission_quota_rel','quota_id','application_id' , string='Apply for Quota')


class OdooCMSAdmissionQuota(models.Model):
    _inherit = 'odoocms.admission.quota'

    quota_ids = fields.One2many('odoocms.admission.applicant.quota', 'quota_id', 'Quotas')


class OdooCMSAdmissionApplicantQuota(models.Model):
    _name = 'odoocms.admission.applicant.quota'
    _rec_name = 'application_id'

    application_id = fields.Many2one('odoocms.application', string='Application')
    quota_id = fields.Many2one('odoocms.admission.quota', string='Quota')
    name = fields.Char("Quota")
    code = fields.Char("Code")


class OdooCMSAdmissionProgram(models.Model):
    _inherit = 'odoocms.program'

    test = fields.Boolean('Test Required')
    test_type = fields.Selection([('lat', 'LAT'), ('etea', 'ETEA')], string='Test type')
    matric_min = fields.Float('Matric Minimum', default=60.0, tracking=True, required=True)
    inter_min = fields.Float('Intermediate Minimum', default=45.0, tracking=True, required=True)
    a_level_min = fields.Float('A Level Minimum', default=45.0, tracking=True, required=True)
    physics_per_min = fields.Float('Physics Minimum', default=0.0, tracking=True, required=True)
    math_per_min = fields.Float('Mathematics Minimum', default=0.0, tracking=True, required=True)
    computer_per_min = fields.Float('Computer Minimum', default=0.0, tracking=True, required=True)
    chemistry_per_min = fields.Float('Chemistry Minimum', default=0.0, tracking=True, required=True)


class ResCompany(models.Model):
    _inherit = "res.company"

    short_name = fields.Char('Short Name', default='UOM')



