from pecanrest.controllers import v1
from pecanrest.controllers.api import api

class RootController(object):
    v1 = v1.VersionController()
    api = api.ApiController()

