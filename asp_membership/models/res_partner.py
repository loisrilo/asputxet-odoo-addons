# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class ResPartner(models.Model):
    _inherit = "res.partner"

    iban = fields.Char(string="IBAN")
    centre_id = fields.Many2one(
        comodel_name="asp.centre",
        string="Centre",
    )
