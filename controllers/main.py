```python
from odoo import http
from odoo.http import request

class CustomPCBuilder(http.Controller):

    @http.route('/component_selection', type='http', auth='user')
    def component_selection(self, **kwargs):
        components = request.env['component'].search([])
        return request.render('custom_pc_builder.component_selection', {'components': components})

    @http.route('/component_configuration', type='http', auth='user')
    def component_configuration(self, **kwargs):
        return request.render('custom_pc_builder.component_configuration')

    @http.route('/component_customization', type='http', auth='user')
    def component_customization(self, **kwargs):
        return request.render('custom_pc_builder.component_customization')

    @http.route('/component_pricing', type='http', auth='user')
    def component_pricing(self, **kwargs):
        return request.render('custom_pc_builder.component_pricing')

    @http.route('/build_history', type='http', auth='user')
    def build_history(self, **kwargs):
        builds = request.env['build'].search([('user_id', '=', request.uid)])
        return request.render('custom_pc_builder.build_history', {'builds': builds})

    @http.route('/build_recommendations', type='http', auth='user')
    def build_recommendations(self, **kwargs):
        return request.render('custom_pc_builder.build_recommendations')

    @http.route('/build_sharing', type='http', auth='user')
    def build_sharing(self, **kwargs):
        return request.render('custom_pc_builder.build_sharing')

    @http.route('/build_import_export', type='http', auth='user')
    def build_import_export(self, **kwargs):
        return request.render('custom_pc_builder.build_import_export')

    @http.route('/build_analytics', type='http', auth='user')
    def build_analytics(self, **kwargs):
        return request.render('custom_pc_builder.build_analytics')

    @http.route('/build_support', type='http', auth='user')
    def build_support(self, **kwargs):
        return request.render('custom_pc_builder.build_support')

    @http.route('/visibility', type='http', auth='user')
    def visibility(self, **kwargs):
        return request.render('custom_pc_builder.visibility')

    @http.route('/comparison_price', type='http', auth='user')
    def comparison_price(self, **kwargs):
        return request.render('custom_pc_builder.comparison_price')

    @http.route('/prevent_sales_zero_priced_products', type='http', auth='user')
    def prevent_sales_zero_priced_products(self, **kwargs):
        return request.render('custom_pc_builder.prevent_sales_zero_priced_products')

    @http.route('/new_menu', type='http', auth='user')
    def new_menu(self, **kwargs):
        return request.render('custom_pc_builder.new_menu')
```