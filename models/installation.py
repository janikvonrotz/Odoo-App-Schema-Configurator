from odoo import api, fields, models, _
import logging
_logger = logging.getLogger(__name__)


class Installation(models.Model):
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _name = 'schematic_configurator.installation'
    _description = 'Schematic Configurator Installation'

    # fields
    name = fields.Char()
    room_id = fields.Many2one('schematic_configurator.room', required=True)
    amount_panels = fields.Integer()
    amount_blinds = fields.Integer()
    amount_electronic_windows = fields.Integer()
    amount_switched_sockets = fields.Integer()
    amount_lamps = fields.Integer()
    amount_dimable_lamps = fields.Integer()
