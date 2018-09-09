# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from datetime import date

from odoo import api, fields, models, _


class ResPartner(models.Model):
    _inherit = "res.partner"

    birth_date = fields.Date(string="Birthdate")
    guardian = fields.Many2one(comodel_name="res.partner")
    is_underage = fields.Boolean(
        string="Is Under-Age?",
        compute="_compute_is_underage",
    )

    @api.depends('birth_date')
    @api.multi
    def _compute_is_underage(self):
        adult = 365 * 18
        for rec in self.filtered(lambda r: r.birth_date):
            rec.is_underage = (
                date.today() -
                fields.Date.from_string(rec.birth_date)).days < adult
