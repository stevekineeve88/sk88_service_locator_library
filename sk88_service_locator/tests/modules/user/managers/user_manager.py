from sk88_service_locator.tests.modules.role.managers.role_manager import RoleManager


class UserManager:
    def __init__(self, **kwargs):
        self.__role_manager: RoleManager = kwargs.get("role_manager")
