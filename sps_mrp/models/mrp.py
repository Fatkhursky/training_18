# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _
from datetime import timedelta, datetime, date
from odoo.exceptions import UserError


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    def _post_labour(self):
        # Custom YP
        if not self.env.context.get('skip_backorder'):
            return
        return super()._post_labour()