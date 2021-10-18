# map, filter, zip and reduce

def callback(item):
    return item * 2


print(
    list(map(callback, [1, 2, 3, 4, 5]))
)
