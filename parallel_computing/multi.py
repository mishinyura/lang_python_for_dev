import itertools
import time
from multiprocessing import Process, Event, Queue, synchronize

def spin(message: str, done_event: synchronize.Event) -> None:
    for character in itertools.cycle(r"\|/-"):
        status = f"\r{character} {message}"
        print(status, end="", flush=True)
        if done_event.wait(0.1):
            break
        blanks = ' ' * (len(status) - 1)
        print(f'\r{blanks}\r', end="")

def slow_function(queue: Queue) -> None:
    time.sleep(3)
    queue.put(42)

def supervisor() -> int:
    done_event = Event()
    queue = Queue()

    spinner = Process(target=spin, args=("thinking... ", done_event))
    spinner.start()

    slow_function(queue)

    done_event.set()
    spinner.join()

    return queue.get()

def main() -> None:
    result = supervisor()
    print(f"Answer: {result}")

if __name__ == '__main__':
    main()