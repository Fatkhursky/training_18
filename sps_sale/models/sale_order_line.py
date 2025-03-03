# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from datetime import date
import re
from markupsafe import Markup

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    panjang = fields.Float("Panjang(M)")
    density = fields.Float("Density")
    ketebalan = fields.Float("Ketebalan (Micron)")