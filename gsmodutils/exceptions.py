from __future__ import print_function, absolute_import, division


class ProjectNotFound(Exception):
    """ Used if no project can be found in a given directory path """
    pass


class ProjectConfigurationError(Exception):
    """ Used if project configuration is erroneous """
    pass


class DesignError(Exception):
    """ Design error occurs when their is an issue with a given design file """
    pass
