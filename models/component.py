```python
from odoo import models, fields

class Component(models.Model):
    _name = 'component'
    _description = 'PC Component'

    name = fields.Char(string='Component Name', required=True)
    category = fields.Selection([
        ('cpu', 'CPU'),
        ('gpu', 'GPU'),
        ('ram', 'RAM'),
        ('storage', 'Storage'),
        ('power_supply', 'Power Supply'),
    ], string='Category', required=True)
    configuration = fields.Text(string='Configuration')
    customization = fields.Text(string='Customization')
    price = fields.Float(string='Price', required=True)
```