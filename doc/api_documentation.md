# API Documentation

This document provides the API documentation for the Custom PC Building Module.

## Models

### Component

- `GET /api/component`: Fetch all components
- `GET /api/component/<id>`: Fetch a specific component by its ID
- `POST /api/component`: Create a new component
- `PUT /api/component/<id>`: Update a specific component by its ID
- `DELETE /api/component/<id>`: Delete a specific component by its ID

### Build

- `GET /api/build`: Fetch all builds
- `GET /api/build/<id>`: Fetch a specific build by its ID
- `POST /api/build`: Create a new build
- `PUT /api/build/<id>`: Update a specific build by its ID
- `DELETE /api/build/<id>`: Delete a specific build by its ID

## Controllers

### Main

- `GET /api/main/component_selection`: Fetch component selection
- `GET /api/main/component_configuration`: Fetch component configuration
- `GET /api/main/component_customization`: Fetch component customization
- `GET /api/main/component_pricing`: Fetch component pricing
- `GET /api/main/build_history`: Fetch build history
- `GET /api/main/build_recommendations`: Fetch build recommendations
- `GET /api/main/build_sharing`: Fetch build sharing
- `GET /api/main/build_import_export`: Fetch build import/export
- `GET /api/main/build_analytics`: Fetch build analytics
- `GET /api/main/build_support`: Fetch build support
- `GET /api/main/visibility`: Fetch visibility settings
- `GET /api/main/comparison_price`: Fetch comparison price
- `GET /api/main/prevent_sales_zero_priced_products`: Fetch zero priced products settings
- `GET /api/main/new_menu`: Fetch new menu settings

## Security

- `GET /api/security`: Fetch security settings

## Testing

- `GET /api/testing`: Fetch testing settings

## Access Rights

- `GET /api/access_rights`: Fetch access rights

## Conclusion

This API documentation provides a comprehensive guide to the endpoints available in the Custom PC Building Module. For more detailed information on how to use these endpoints, please refer to the user documentation.