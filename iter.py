class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_lists = list_of_list

    def __iter__(self):
        self.flat_list = [x for y in self.list_of_lists for x in y]
        self.counter = -1
        return self

    def __next__(self):
        self.counter += 1
        if self.counter >= len(self.flat_list):
            raise StopIteration
        return self.flat_list[self.counter]
