```python
from odoo.tests import common

class TestBuild(common.TransactionCase):

    def setUp(self):
        super(TestBuild, self).setUp()
        self.Build = self.env['build']

    def test_create_build(self):
        """Test the creation of a build"""
        build = self.Build.create({
            'user_id': 1,
            'components': [(6, 0, [1, 2, 3])],
            'configuration': 'Test Configuration',
            'customization': 'Test Customization',
            'price': 1000.0,
        })
        self.assertEqual(build.user_id.id, 1)
        self.assertEqual(len(build.components), 3)
        self.assertEqual(build.configuration, 'Test Configuration')
        self.assertEqual(build.customization, 'Test Customization')
        self.assertEqual(build.price, 1000.0)

    def test_update_build(self):
        """Test the update of a build"""
        build = self.Build.create({
            'user_id': 1,
            'components': [(6, 0, [1, 2, 3])],
            'configuration': 'Test Configuration',
            'customization': 'Test Customization',
            'price': 1000.0,
        })
        build.write({
            'components': [(6, 0, [4, 5, 6])],
            'configuration': 'Updated Configuration',
            'customization': 'Updated Customization',
            'price': 2000.0,
        })
        self.assertEqual(len(build.components), 3)
        self.assertEqual(build.configuration, 'Updated Configuration')
        self.assertEqual(build.customization, 'Updated Customization')
        self.assertEqual(build.price, 2000.0)

    def test_delete_build(self):
        """Test the deletion of a build"""
        build = self.Build.create({
            'user_id': 1,
            'components': [(6, 0, [1, 2, 3])],
            'configuration': 'Test Configuration',
            'customization': 'Test Customization',
            'price': 1000.0,
        })
        build_id = build.id
        build.unlink()
        self.assertFalse(self.Build.search([('id', '=', build_id)]))
```