"""An ICE Portal API consumer."""
import asyncio
import logging
import socket
from datetime import datetime

import aiohttp
import async_timeout

from . import exceptions

_LOGGER = logging.getLogger(__name__)
_PORTAL = "https://iceportal.de/api1/rs/tripInfo/trip"


class IcePortal:
    """A class for handling connections with the ICE Portal."""

    def __init__(self, loop, session):
        """Initialize the connection the ICE Portal."""
        self._loop = loop
        self._session = session
        self.data = {}
        self._track = self._arrival_time = None
        self.base_url = _PORTAL

    async def get_data(self):
        """Get details of the current trip."""
        try:
            async with async_timeout.timeout(5, loop=self._loop):
                response = await self._session.get(self.base_url)

            _LOGGER.info("Response from ICE Portal: %s", response.status)
            self.data = await response.json()
            _LOGGER.debug(self.data)

        except (asyncio.TimeoutError, aiohttp.ClientError, socket.gaierror):
            _LOGGER.error("Can not load data from ICE Portal")
            raise exceptions.IcePortalConnectionError

    @property
    def train(self):
        """Return the ID of the train."""
        return f"{self.data['trip']['trainType']}{self.data['trip']['vzn']}"

    @property
    def next_stop(self):
        """Return the next stop."""
        stops = self.data["trip"]["stops"]
        for stop in stops:
            if stop["info"]["passed"] is False:
                self._track = stop["track"]["actual"]
                self._arrival_time = str(stop["timetable"]["actualArrivalTime"])[:-3]
                return stop["station"]["name"]

    @property
    def track(self):
        """Return the track of the next station."""
        return self._track

    @property
    def arrival_time(self):
        """Return the arrival time at the next station."""
        return datetime.utcfromtimestamp(int(self._arrival_time))
