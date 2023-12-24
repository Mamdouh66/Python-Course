import time

class TimeFunction:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {self.func.__name__} took {end_time - start_time} seconds to execute.")
        return result

@TimeFunction
def evenFun(x, y):
    return sum(i for i in range(x, y+1) if i % 2 == 0)

if __name__ == "__main__":
    evenFun(1, 10)
