def towerOfHanoi(n, source='A', auxiliary='B', destination='C'):
    if n == 1:
        print("from", source, "to", destination)
    else:
        towerOfHanoi(n-1, source, destination, auxiliary)
        print("from", source, "to", destination)
        towerOfHanoi(n-1, auxiliary, source, destination)
