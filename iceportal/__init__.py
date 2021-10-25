"""An ICE Portal API consumer."""
import asyncio
import logging
import socket
from datetime import datetime

import httpx

from . import exceptions

_LOGGER = logging.getLogger(__name__)
_PORTAL = "https://iceportal.de/api1/rs/tripInfo/trip"
_STATUS = "https://iceportal.de/api1/rs/status"


class IcePortal:
    """A class for handling connections with the ICE Portal."""

    def __init__(self):
        """Initialize the connection the ICE Portal."""
        self.data = {}
        self._track = self._arrival_time = None
        self.status = {}

    async def get_data(self):
        """Get details of the current trip."""
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(str(_PORTAL))
        except httpx.ConnectError:
            raise exceptions.IcePortalConnectionError(
                f"Connection to {_PORTAL} failed"
            )

        if response.status_code == httpx.codes.OK:
            try:
                _LOGGER.debug(response.json())
                self.data = response.json()
            except TypeError:
                _LOGGER.error("Can not load data from the ICE portal")
                raise exceptions.IcePortalError("Unable to get the data from the ICE portal")

        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(str(_STATUS))
        except httpx.ConnectError:
            raise exceptions.IcePortalConnectionError(
                f"Connection to {_STATUS} failed"
            )

        if response.status_code == httpx.codes.OK:
            _LOGGER.debug(response.json())
            try:
                self.status = response.json()
            except TypeError:
                _LOGGER.error("Can not load data from the ICE portal")
                raise exceptions.IcePortalError("Unable to get the data from the ICE portal")


    @property
    def train(self):
        """The ID of the train."""
        return f"{self.data['trip']['trainType']}{self.data['trip']['vzn']}"

    @property
    def next_stop(self):
        """The next stop."""
        stops = self.data["trip"]["stops"]
        for stop in stops:
            if stop["info"]["passed"] is False:
                self._track = stop["track"]["actual"]
                self._arrival_time = str(stop["timetable"]["actualArrivalTime"])[:-3]
                return stop["station"]["name"]

    @property
    def track(self):
        """The track of the next station."""
        return self._track

    @property
    def arrival_time(self):
        """The arrival time at the next station."""
        return datetime.utcfromtimestamp(int(self._arrival_time))

    @property
    def train_speed(self):
        """The current speed of the trains."""
        return self.status["speed"]