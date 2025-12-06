orders = []

def router(request):
    method = request.get("method")
    path = request.get("endpoint")
    data = request.get("data")

    if not method or not path:
        return {"error": "bad requestuest"}

    if method == "GET" and path == "/items":
        return {"count": len(orders), "items": orders}

    if method == "POST" and path == "/items":
        if not isinstance(data, dict):
            return {"error": "invalid payload"}

        new_order = {"id": len(orders) + 1, **data}
        orders.append(new_order)
        return {"status": "added"}

    return {"error": "invalid route"}
# request = {"method": "GET", "endpoint": "/users", "data": {"id": 101}}
request = {"method": "GET", "endpoint": "/items", "data": {"id": 101}}
print(router(request))



