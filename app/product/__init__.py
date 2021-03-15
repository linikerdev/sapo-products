BASE_ROUTE = "product"

def register_routes(app, root="api"):
    from .controller import router as product_router
    
    app.include_router(product_router, prefix=f"/{root}/{BASE_ROUTE}")

