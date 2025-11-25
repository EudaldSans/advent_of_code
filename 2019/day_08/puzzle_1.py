

if __name__ == '__main__':
    with open('image.txt') as file:
        image_string = file.readline()

    row_size = 25
    column_size = 6
    layer_size = row_size*column_size

    layers = [image_string[x:x + layer_size] for x in range(0, len(image_string), layer_size)]

    layer_with_fewest_zeroes = None
    min_zeroes = layer_size

    for layer in layers:
        zeroes = 0

        for character in layer:
            if character == '0':
                zeroes += 1

        if zeroes < min_zeroes:
            layer_with_fewest_zeroes = layer
            min_zeroes = zeroes

    ones = 0
    twos = 0

    for character in layer_with_fewest_zeroes:
        if character == '1':
            ones += 1
        if character == '2':
            twos += 1

    print(f'The layer with fewest zero digits ({min_zeroes}) contains {ones * twos} digits')
