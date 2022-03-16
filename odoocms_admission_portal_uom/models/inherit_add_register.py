from dateutil.relativedelta import relativedelta
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError, Warning
import pdb


class OdooCMSAdmissionRegister(models.Model):
    _inherit = "odoocms.admission.register"

    prospectus = fields.Binary('Prospectus')