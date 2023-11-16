# System Architecture Documentation

## Overview

The system architecture for the Custom PC Building Module is designed to provide a comprehensive and user-friendly way for users to build custom PCs on an e-commerce website. The system is built on the Odoo V16 CE platform and uses Python for backend development and Odoo's UI framework for frontend development.

## System Components

The system is composed of several components, each responsible for a specific functionality in the Custom PC Building Module.

### Models

The system uses two main models, `Component` and `Build`. The `Component` model represents the individual components that users can select and customize for their PC build. The `Build` model represents the user's custom PC build.

Refer to `models/component.py` and `models/build.py` for the implementation of these models.

### Controllers

The system uses a main controller to handle requests from the frontend and interact with the models. The main controller handles component selection, configuration, customization, pricing, build history, build recommendations, build sharing, build import/export, build analytics, build support, visibility, comparison price, prevent sales of zero priced products, and new menu.

Refer to `controllers/main.py` for the implementation of the main controller.

### Views

The system uses Odoo's UI framework to create the user interface. The views define the layout and presentation of the user interface.

Refer to `views/*.xml` for the implementation of the views.

### Tests

The system includes unit tests, integration tests, and end-to-end tests to ensure that all components are working as expected.

Refer to `tests/*.py` for the implementation of the tests.

### Security

The system implements secure component selection and configuration. It protects against common web vulnerabilities such as SQL injection and cross-site scripting and uses HTTPS for secure communication.

Refer to `security/ir.model.access.csv` for the implementation of the access rights.

## Data Flow

The data in the system flows from the frontend to the backend. When a user interacts with the frontend, the main controller receives the request, interacts with the models, and sends a response back to the frontend.

## Conclusion

The system architecture for the Custom PC Building Module is designed to provide a comprehensive and user-friendly way for users to build custom PCs on an e-commerce website. The system is built on the Odoo V16 CE platform and uses Python for backend development and Odoo's UI framework for frontend development.