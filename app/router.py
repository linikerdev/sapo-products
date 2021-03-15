def register_routes(app, root="api"):
    from app.product import register_routes as attach_product

    # Add routes
    attach_product(app)
