"""Get the data from the ICE portal about the current trip."""
import asyncio

import aiohttp

from iceportal import IcePortal


async def main():
    """Sample code to retrieve the data from the ICE portal."""
    async with aiohttp.ClientSession() as session:
        trip = IcePortal(loop, session)

        # Print details about the current rip
        await trip.get_data()

        print("Train:", trip.train)
        print("Next stop:", trip.next_stop)
        print("Track:", trip.track)
        print("Arrival time:", trip.arrival_time)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
