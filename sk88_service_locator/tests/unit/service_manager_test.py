import unittest
from sk88_service_locator.modules.service.managers.service_manager import ServiceManager
from sk88_service_locator.tests.modules.role.factories.role_manager_factory import RoleManagerFactory
from sk88_service_locator.tests.modules.role.managers.role_manager import RoleManager
from sk88_service_locator.tests.modules.user.factories.user_manager_factory import UserManagerFactory
from sk88_service_locator.tests.modules.user.managers.user_manager import UserManager


class ServiceManagerTest(unittest.TestCase):

    def setUp(self) -> None:
        self.user_manager_factory: UserManagerFactory = UserManagerFactory()
        self.role_manager_factory: RoleManagerFactory = RoleManagerFactory()

    def test_instantiates_correct_instances(self):
        service_manager = self.__get_service_manager()

        user_manager: UserManager = service_manager.get(UserManager.__name__)
        role_manager: RoleManager = service_manager.get(RoleManager.__name__)

        self.assertEqual(UserManager, type(user_manager))
        self.assertEqual(RoleManager, type(role_manager))

    def test_get_calls_factory_once_for_initiate(self):
        service_manager = self.__get_service_manager()

        user_manager: UserManager = service_manager.get(UserManager.__name__)
        role_manager: RoleManager = service_manager.get(RoleManager.__name__)

        self.assertEqual(UserManager, type(user_manager))
        self.assertEqual(RoleManager, type(role_manager))

        self.assertEqual(1, self.role_manager_factory.CALL_COUNT)

    def test_get_call_works_in_any_order(self):
        service_manager = self.__get_service_manager()

        role_manager: RoleManager = service_manager.get(RoleManager.__name__)
        user_manager: UserManager = service_manager.get(UserManager.__name__)

        self.assertEqual(UserManager, type(user_manager))
        self.assertEqual(RoleManager, type(role_manager))
        self.assertEqual(1, self.role_manager_factory.CALL_COUNT)
        self.assertEqual(1, self.user_manager_factory.CALL_COUNT)

        self.role_manager_factory.CALL_COUNT = 0
        self.user_manager_factory.CALL_COUNT = 0
        service_manager = self.__get_service_manager()

        user_manager: UserManager = service_manager.get(UserManager.__name__)
        role_manager: RoleManager = service_manager.get(RoleManager.__name__)

        self.assertEqual(UserManager, type(user_manager))
        self.assertEqual(RoleManager, type(role_manager))
        self.assertEqual(1, self.role_manager_factory.CALL_COUNT)
        self.assertEqual(1, self.user_manager_factory.CALL_COUNT)

    def __get_service_manager(self) -> ServiceManager:
        service_manager: ServiceManager = ServiceManager()
        service_manager.add({
            UserManager.__name__: self.user_manager_factory,
            RoleManager.__name__: self.role_manager_factory
        })
        return service_manager
