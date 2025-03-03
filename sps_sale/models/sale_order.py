# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from datetime import date
import re
from markupsafe import Markup

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        credit_limits = self.env['credit.limit'].search([
            ('partner_id', '=', self.partner_id.id),
            ('state', '=', 'active')
            ])
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        if credit_limits:
            amount = sum(cl.amount for cl in credit_limits)
            if self.amount_total > amount:
                action = self.env.ref("sps_sale.action_credit_limit")
                credit_limit_url = f"{base_url}/web#action={action.id}&model=credit.limit&view_type=list&domain=[('id','in',{credit_limits.ids})]"
                msg = Markup('Credit limit is insufficient - <a href="%s" target="_blank">%s</a>') % (credit_limit_url, _("Credit Limits"))
                self.message_post(body=msg)
                return self._show_wizard_message('Credit limit is insufficient')
        partner_limit = self.partner_id.use_partner_credit_limit
        if partner_limit:
            if self.amount_total > self.partner_id.credit_limit:
                partner_limit_url = f'{base_url}/web#id={self.partner_id.id}&view_type=form&model=res.partner&menu_id=&action='
                msg = Markup('Partner limit is insufficient - <a href="%s" target="_blank">%s</a>') % (partner_limit_url, _("partner limit"))
                self.message_post(body=msg)
                return self._show_wizard_message('Partner limit is insufficient')
        
        # if not credit_limits and not partner_limit:
        sales_orders = self.env['sale.order'].search([
            ('partner_id', '=', self.partner_id.id),
            ('state', '=', 'sale')
        ])
        
        if sales_orders:
            for so in sales_orders:
                if so.invoice_ids:
                    for invoice in so.invoice_ids.filtered(lambda inv: inv.state not in ['cancel']):
                        today = date.today()
                        if invoice.invoice_date_due < today:

                            inv_url = f'{base_url}/web#id={invoice.id}&view_type=form&model=account.move&menu_id=&action='
                            msg = Markup('There is an overdue - <a href="%s" target="_blank">%s</a>') % (inv_url, (invoice.display_name))
                            self.message_post(body=msg)
                            return self._show_wizard_message('There is an overdue %s' % invoice.display_name)
                    
                    order_line = so.order_line.filtered(lambda l: l.is_downpayment and l.display_type != 'line_section')
                    if order_line:
                        for line in order_line:
                            match = re.search(r'(?<=ref: )(.*?)(?= on)', line.name)
                            if match:
                                inv_ref = match.group()
                                invoice = so.invoice_ids.filtered(lambda i: i.name == inv_ref)
                                if invoice and invoice.payment_state != 'paid':
                                    inv_url = f'{base_url}/web#id={invoice.id}&view_type=form&model=account.move&menu_id=&action='
                                    msg = Markup('There is an unpaid downpayment for <a href="%s" target="_blank">%s</a>') % (inv_url, (invoice.display_name))
                                    self.message_post(body=msg)
                                    return self._show_wizard_message('There is an unpaid downpayment for %s' % invoice.display_name)
        return super().action_confirm()

    def force_confirm(self):
        return super(SaleOrder, self).action_confirm()
    
    
    def _show_wizard_message(self, message):
        """Helper untuk memanggil wizard message."""
        return {
            'name': _('Validation Error'),
            'type': 'ir.actions.act_window',
            'res_model': 'wizard.message',
            'view_mode': 'form',
            'view_type': 'form',
            'target': 'new',
            'context': {'default_message': message}
        }