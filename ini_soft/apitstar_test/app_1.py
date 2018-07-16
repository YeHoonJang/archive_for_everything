# from apistar import App, Route, Include
# from apistar.handlers import docs_urls, static_urls
#
# def welcome(name=None):
#     if name is None:
#         return {'message': 'Welcome to API Star!'}
#     return {'message': 'Welcome to API Star, %s!' % name}
#
#
# routes = [
#     Route('/', method='GET', handler=welcome),
#     Include ( ' / docs ' , docs_urls),
#     Include ( ' / static ' , static_urls)
# ]
#
# app = App(routes=routes)
#
#


from apistar import App, Route, exceptions


USERS = {1: 'hazel', 2: 'james', 3: 'ana'}

def list_users(app: App) -> list:
    return [
        {
            'username': username,
            'url': app.reverse_url('get_user', user_id=user_id)
        } for user_id, username in USERS.items()
    ]

def get_user(app: App, user_id: int) -> dict:
    if user_id not in USERS:
        raise exceptions.NotFound()
    return {
        'username': USERS[user_id],
        'url': app.reverse_url('get_user', user_id=user_id)
    }

routes = [
    Route('/users/', method='GET', handler=list_users),
    Route('/users/{user_id}/', method='GET', handler=get_user)
]

app = App(routes=routes)

if __name__ == '__main__':
    app.serve('127.0.0.1', 5000, debug=True)
