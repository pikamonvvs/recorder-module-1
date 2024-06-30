import asyncio

from loguru import logger

import utils.utils as utils
from recorders.recorders import *
from recorders.recorders import recording


async def run():
    args = utils.parse_args()
    try:
        platform = globals()[args.get("platform")]
        coroutine = platform(args).start()
        await coroutine
    except (asyncio.CancelledError, KeyboardInterrupt, SystemExit):
        logger.warning("The user has interrupted the recording. Closing the live stream.")
        for stream_fd, output in recording.copy().values():
            stream_fd.close()
            output.close()


def main():
    logger.add(
        sink="logs/log_{time:YYYY-MM-DD}.log",
        rotation="00:00",
        retention="3 days",
        level="INFO",
        encoding="utf-8",
        format="[{time:YYYY-MM-DD HH:mm:ss}][{level}][{name}][{function}:{line}]{message}",
    )
    asyncio.run(run())


if __name__ == "__main__":
    main()
