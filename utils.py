import functools
import typing as ty

def run_forever(func: ty.Callable) -> ty.Callable:
    """
    Decorator to run a function forever.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        while True:
            try:
                func(*args, **kwargs)
            except KeyboardInterrupt:
                exit(0)
            except EOFError:
                exit(0)
            except:
                print("Something went wrong:")
    return wrapper
