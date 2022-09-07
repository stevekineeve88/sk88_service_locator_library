class FactoryInterface:
    """ Factory interface that acts as a template for factory classes
    """

    def invoke(self, service_manager):
        """ Create specified object instance
        Args:
            service_manager (ServiceManager):   Service manager for locating services
        Returns:
            Initiated Object
        """
        pass
