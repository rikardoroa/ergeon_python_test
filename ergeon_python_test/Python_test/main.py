#script by rikardoroa
#just python it!!
import datetime
import time


class calendar_yield:

    def __init__(self, current=str, initial=str, primenumbers=[]):
        self.current = current
        self.initial = initial
        self.primenumbers = primenumbers

    def response_time(function):
        def wrapper(self, *args, **kwargs):
            start = time.time()
            result = function(self, *args, **kwargs)
            execution = (time.time() - start) * 1000
            print(f"total time of execution for {function.__name__} was:", round(execution, 2), "ms")
            return result

        return wrapper

    def range_days(self):
        while True:

            try:

                # capturing initial date
                self.initial = input("please enter a date in format yyyy-mm-dd:")
                self.initial = datetime.datetime.strptime(self.initial, "%Y-%m-%d")

                # capturing current date (today)
                self.current = str(datetime.date.today())
                self.current = datetime.datetime.strptime(self.current, "%Y-%m-%d")

                # days between initial and current date
                self.initial = self.initial - datetime.timedelta(1)
                days = int((self.current - self.initial).days)

                # creating de dates generator between dates and taking days as input
                # to calculate actual date
                dates = []
                for i in range(days):
                    today = yield self.initial + datetime.timedelta(i + 1)
                    dates.append(today)
                return dates
            except ValueError:
                print("please write the correct format")

    @response_time
    def show_dates(self):

        # creating and iterator for printing the dates
        iter_ = iter(self.range_days())
        while True:
            try:
                X = next(iter_)
                print(X)
            except StopIteration:
                break

    @response_time
    def twins_prime(self, s, f):
        #looping al numbers between the range
        for num in range(s, f):
            if num > 2:
                #validating all the numbers that are not primes
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    #capturing al prime numbers
                    self.primenumbers.append(num)
        twins = []
        #creating the tuples with all twin prime numbers
        for index, item in enumerate(self.primenumbers):
            i = self.primenumbers[index]
            j = self.primenumbers[(index + 1) % len(self.primenumbers)]
            if j - 2 == i:
                twins.append((i, j))
        print(twins)


if __name__ == '__main__':
    yield_cal = calendar_yield()
    yield_cal.range_days()
    yield_cal.show_dates()
    yield_cal.twins_prime(1, 100000)
