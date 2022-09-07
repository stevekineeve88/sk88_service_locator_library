from typing import Dict
from sk88_service_locator.modules.service.interfaces.factory_interface import FactoryInterface


class ServiceManager:
    """ Manager for locating different services
    """

    def __init__(self):
        """ Constructor for ServiceManager
        """
        self.__config: Dict[str, FactoryInterface] = {}
        self.__cached = {}

    def add(self, config: Dict[str, FactoryInterface]):
        """ Add configuration for object initialization
        Args:
            config (Dict[str, FactoryInterface]):
                key (str):                  Class name as string
                value (FactoryInterface):   Factory class for invoking and creating object
        """
        self.__config.update(config)

    def get(self, class_name: str):
        """ Get service by class name
        Args:
            class_name (str):       Class name
        Returns:
            Initialized Object
        """
        if class_name not in self.__cached:
            self.__cached[class_name] = self.__config[class_name].invoke(self)
        return self.__cached[class_name]
