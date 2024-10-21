import itertools
import time
from threading import Thread, Event

def spin(message: str, done_event: Event) -> None:
    for character in itertools.cycle(r"\|/-"):
        status = f"\r{character} {message}"
        print(status, end="", flush=True)
        if done_event.wait(0.1):
            break
        blanks = ' ' * (len(status) - 1)
        print(f'\r{blanks}\r', end="")

def slow_function() -> int:
    time.sleep(3)
    return 42

def supervisor() -> int:
    done_event = Event()
    spinner_thread = Thread(target=spin, args=("thinking... ", done_event))
    spinner_thread.start()
    result = slow_function()
    done_event.set()
    spinner_thread.join()
    return result

def main() -> None:
    result = supervisor()
    print(f"Answer: {result}")

if __name__ == '__main__':
    main()