# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from ..models import const

model_name = "studio.sheet"


class Sheet(models.Model):
    _name = model_name
    _description = "Sheet records"
    _inherit = ["mail.thread"]
    _rec_name = "display_name"

    # core ram
    name = fields.Char("Name", tracking=True)
    description = fields.Char("Description", tracking=True)

    # company

    # sequential
    ref = fields.Char(string="Code", default=lambda self: _("New"))

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals["ref"] = self.env["ir.sequence"].next_by_code(model_name)
        return super(Sheet, self).create(vals_list)

    @api.depends("ref")
    def _compute_display_name(self):
        for record in self:
            name = record.ref
            record.display_name = name
