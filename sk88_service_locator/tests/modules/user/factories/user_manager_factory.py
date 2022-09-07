from sk88_service_locator.modules.service.interfaces.factory_interface import FactoryInterface
from sk88_service_locator.modules.service.managers.service_manager import ServiceManager
from sk88_service_locator.tests.modules.role.managers.role_manager import RoleManager
from sk88_service_locator.tests.modules.user.managers.user_manager import UserManager


class UserManagerFactory(FactoryInterface):
    CALL_COUNT = 0

    def invoke(self, service_manager: ServiceManager) -> UserManager:
        self.CALL_COUNT += 1
        return UserManager(
            role_manager=service_manager.get(RoleManager.__name__)
        )
