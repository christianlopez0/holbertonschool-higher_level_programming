#!/usr/bin/python3
class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration("No more items to iterate")

    def get_count(self):
        return self.count

# Testing
iterable = [1, 2, 3, 4, 5]
counted_iter = CountedIterator(iterable)

for item in counted_iter:
    print(item)

print("Number of items iterated:", counted_iter.get_count())
