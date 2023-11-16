```python
from odoo.tests import common

class TestComponent(common.TransactionCase):

    def setUp(self):
        super(TestComponent, self).setUp()
        self.Component = self.env['component']

    def test_component_creation(self):
        "Test the creation of a Component"
        component = self.Component.create({
            'name': 'Test Component',
            'category': 'CPU',
            'configuration': 'Intel i7',
            'customization': 'Black',
            'price': 300.00,
        })

        self.assertEqual(component.name, 'Test Component')
        self.assertEqual(component.category, 'CPU')
        self.assertEqual(component.configuration, 'Intel i7')
        self.assertEqual(component.customization, 'Black')
        self.assertEqual(component.price, 300.00)

    def test_component_update(self):
        "Test the update of a Component"
        component = self.Component.create({
            'name': 'Test Component',
            'category': 'CPU',
            'configuration': 'Intel i7',
            'customization': 'Black',
            'price': 300.00,
        })

        component.write({
            'name': 'Updated Component',
            'category': 'GPU',
            'configuration': 'Nvidia RTX 3080',
            'customization': 'White',
            'price': 700.00,
        })

        self.assertEqual(component.name, 'Updated Component')
        self.assertEqual(component.category, 'GPU')
        self.assertEqual(component.configuration, 'Nvidia RTX 3080')
        self.assertEqual(component.customization, 'White')
        self.assertEqual(component.price, 700.00)

    def test_component_deletion(self):
        "Test the deletion of a Component"
        component = self.Component.create({
            'name': 'Test Component',
            'category': 'CPU',
            'configuration': 'Intel i7',
            'customization': 'Black',
            'price': 300.00,
        })

        component_id = component.id
        component.unlink()

        self.assertFalse(self.Component.search([('id', '=', component_id)]))
```