from sk88_service_locator.modules.service.interfaces.factory_interface import FactoryInterface
from sk88_service_locator.modules.service.managers.service_manager import ServiceManager
from sk88_service_locator.tests.modules.role.managers.role_manager import RoleManager


class RoleManagerFactory(FactoryInterface):

    CALL_COUNT = 0

    def invoke(self, service_manager: ServiceManager) -> RoleManager:
        self.CALL_COUNT += 1
        return RoleManager(
            role_data="Role Data"
        )
