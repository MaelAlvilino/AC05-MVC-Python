from resource.users import *

from resource.users import UserResource
class View():
    def routes(api):
        api.add_resource(UserResource,"/users")