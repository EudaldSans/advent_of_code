

if __name__ == '__main__':
    with open('image.txt') as file:
        image_string = file.readline()

    row_size = 25
    column_size = 6
    layer_size = row_size * column_size

    layers = [image_string[x:x + layer_size] for x in range(0, len(image_string), layer_size)]

    final_layer = ['2' for _ in range(layer_size)]

    for layer in layers:
        for pos, character in enumerate(layer):
            if final_layer[pos] != '2':
                continue

            final_layer[pos] = character

    final_image = [final_layer[x:x+row_size] for x in range(0, len(final_layer), row_size)]

    for row in final_image:
        row_str = ''
        row_str = row_str.join(row)
        row_str = row_str.replace('0', ' ')
        row_str = row_str.replace('1', '#')
        print(row_str)
