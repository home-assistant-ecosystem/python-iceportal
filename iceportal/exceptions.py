"""Exceptions for ICEPortal web scraper."""


class IcePortalError(Exception):
    """General ICE Portal exception occurred."""

    pass


class IcePortalConnectionError(IcePortalError):
    """When a connection error is encountered."""

    pass


class IcePortalNoDataAvailable(IcePortalError):
    """When no data is available."""

    pass
