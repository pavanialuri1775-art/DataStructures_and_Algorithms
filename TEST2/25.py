#137.52. Implement a generator for reading a large file line-by-line.
def generator():
    for i in range(5):
        yield i
x=generator()
print(next(x))
print(next(x))
        