import asyncio
import time


class AsyncRobot:
    def __init__(self):
        self._task = None
        self._is_running = False

    async def start_loop(self, start_id: int):
        while True:
            print(start_id)
            start_id += 1
            await asyncio.sleep(0.5)

    async def start(self, start_id: int):
        if self._is_running:
            return
        self._task = asyncio.create_task(self.start_loop(start_id))
        self._is_running = True
        await self._task

    async def stop(self):
        self._task.cancel()
        self._is_running = False
        print(f'Robot was stopped!')


async_robot = AsyncRobot()
if __name__ == "__main__":
    asyncio.run(async_robot.start(3))
    time.sleep(4)
    asyncio.run(async_robot.stop())
