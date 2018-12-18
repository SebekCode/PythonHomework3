#!/usr/bin/env python3


class Cuboid:
    def __init__(self, side_length, name):
        self.side_length = side_length
        self.name = name

    def __eq__(self, other):
        print("Comparision type: {} == {}".format(self.name, other.name))
        return self.side_length == other.side_length

    def __lt__(self, other):
        print("Comparision type: {} < {}".format(self.name, other.name))
        return self.side_length < other.side_length

    def __gt__(self, other):
        print("Comparision type: {} > {}".format(self.name, other.name))
        return self.side_length > other.side_length

    def __le__(self, other):
        print("Comparision type: {} <= {}".format(self.name, other.name))
        return self.side_length <= other.side_length

    def __ge__(self, other):
        print("Comparision type: {} >= {}".format(self.name, other.name))
        return self.side_length >= other.side_length

    def __ne__(self, other):
        print("Comparision type: {} != {}".format(self.name, other.name))
        return self.side_length != other.side_length


a = Cuboid(4, "A")
b = Cuboid(5, "B")
h = Cuboid(7, "H")

print(a == h)
print(a >= h)
print(a <= h)
print(a != h)
print(a > h)
print(a < h)
