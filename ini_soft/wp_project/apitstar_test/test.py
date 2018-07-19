from apistar import typesystem
from apistar import Include, Route
from apistar.frameworks.asyncio import ASyncIOAPP as App
from apistar.handlers import docs_urls, static_urls


class Product(typesystem.Object):
    properties = {
    'name': Name,
    "in_stock" : typesystem.Boolean,
    }
def welcome(data: Product):
    return data

routes = [
Route('/', 'POST', welcome)
]

app = App(routes=routes)

if __name__ == '__main__':
    app.main()
