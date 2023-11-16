```python
from odoo import models, fields

class Build(models.Model):
    _name = 'pc.builder.build'
    _description = 'PC Build'

    user_id = fields.Many2one('res.users', string='User')
    components = fields.Many2many('pc.builder.component', string='Components')
    configuration = fields.Text(string='Configuration')
    customization = fields.Text(string='Customization')
    price = fields.Float(string='Price')
    build_history = fields.One2many('pc.builder.build.history', 'build_id', string='Build History')
    build_recommendations = fields.One2many('pc.builder.build.recommendations', 'build_id', string='Build Recommendations')
    build_sharing = fields.One2many('pc.builder.build.sharing', 'build_id', string='Build Sharing')
    build_import_export = fields.One2many('pc.builder.build.import_export', 'build_id', string='Build Import/Export')
    build_analytics = fields.One2many('pc.builder.build.analytics', 'build_id', string='Build Analytics')
    build_support = fields.One2many('pc.builder.build.support', 'build_id', string='Build Support')
```