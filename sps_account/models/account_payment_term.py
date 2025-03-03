# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from datetime import date
import re
from markupsafe import Markup

class AccountPaymentTerm(models.Model):
    _inherit = 'account.payment.term'

    cod = fields.Boolean('COD')

