import asyncio
import itertools

async def spin(msg: str) -> None:
    for char in itertools.cycle(r"\|/-"):
        status = f"{char} {msg}"
        print(status, end="\r")
        try:
            await asyncio.sleep(.1)
        except asyncio.CancelledError:
            break
    blanks = " " * len(status)
    print(f"{blanks}\r", end="")

async def slow_function() -> int:
    await asyncio.sleep(3)
    return 42

async def supervisor() -> int:
    spinner = asyncio.create_task(spin('thinking...'))
    print(f"spinner object: {spinner}")
    result = await slow_function()
    spinner.cancel()
    return result

def main() -> None:
    result = asyncio.run(supervisor())
    print(f"Answer: {result}")


if __name__ == '__main__':
    # main()
    a = 1
    for a in range(5):
        a += 2
        break
    print(a)
