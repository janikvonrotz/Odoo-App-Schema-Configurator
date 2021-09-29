from odoo import api, fields, models, _
import logging
_logger = logging.getLogger(__name__)


class Panel(models.Model):
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _name = 'schematic_configurator.panel'
    _description = 'Schematic Configurator Panel'

    # fields
    name = fields.Char()
    slots_x = fields.Integer()
    slots_y = fields.Integer()

class PanelSlot(models.Model):
    _name = 'schematic_configurator.slot'
    _description = 'Schematic Configurator Slot'
    _rec_name = 'label'

    # fields
    label = fields.Char()
    panel_id = fields.Many2one('schematic_configurator.panel', required=True)
    postition_x = fields.Integer()
    postition_y = fields.Integer()