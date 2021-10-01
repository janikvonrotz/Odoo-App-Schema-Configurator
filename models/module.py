from odoo import api, fields, models, _
import logging
_logger = logging.getLogger(__name__)


class Module(models.Model):
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _name = 'schematic_configurator.module'
    _description = 'Schematic Configurator Module'
    _rec_name = 'label'
    _order = 'sequence'

    # fields
    sequence = fields.Integer()
    label = fields.Char(required=True)
    slot_id = fields.Many2one('schematic_configurator.panel.slot', required=True)
    panel_id = fields.Many2one(related='slot_id.panel_id')
    product_id = fields.Many2one('product.template', required=True)
    image = fields.Image(related='product_id.image_1920')

    def action_show_details(self):
        self.ensure_one()
        view = self.env.ref('schematic_configurator.module_form')
        return {
            'name': _('%s') % self.label,
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'res_model': 'schematic_configurator.module',
            'views': [(view.id, 'form')],
            'view_id': view.id,
            'target': 'new',
            'res_id': self.id,
            'context': dict(self.env.context),
        }