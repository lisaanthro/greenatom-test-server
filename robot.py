import asyncio
import datetime


class AsyncRobot:
    def __init__(self):
        self._task = None
        self._is_running = False
        self.start_id = 0
        self.start_time = None

    async def start_loop(self, start_id: int) -> None:
        while True:
            print(start_id)
            if not self._is_running:
                break
            start_id += 1
            await asyncio.sleep(0.5)

    async def start(self, start_id: int) -> None:
        if self._is_running:
            return

        self.start_id = start_id
        self.start_time = datetime.datetime.now()
        self._task = asyncio.create_task(self.start_loop(start_id))
        self._is_running = True

    async def stop(self) -> None:
        if not self._is_running:
            return

        self._task.cancel()
        self._is_running = False
        print(f'Robot stopped!')


async_robot = AsyncRobot()
