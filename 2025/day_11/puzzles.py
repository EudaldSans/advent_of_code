import re
from typing import Dict, List


def find_path(connection_dict: Dict[str, List[str]], start_node: str, end_node: str, visited: Dict[str, int]) -> int:
    nodes = connection_dict[start_node]

    result = 0
    for node in nodes:
        if node == end_node:
            return 1

        elif node == 'out':
            return 0

        elif node in visited.keys():
            result += visited[node]

        else:
            node_result = find_path(connection_dict, node, end_node, visited)
            visited[node] = node_result
            result += node_result

    return result


def main():
    with open('connection_diagram.txt', 'r') as f:
        lines = [line.rstrip('\n') for line in f]

    connection_dict = dict(map(lambda s: (s[0], s[1:]), map(lambda s: re.findall(r'\w{3}', s), lines)))

    result = find_path(connection_dict, 'you', 'out', {})
    print(result)

    svr_fft = find_path(connection_dict, "svr", "fft", {})
    fft_dac = find_path(connection_dict, "fft", "dac", {})
    dac_out = find_path(connection_dict, "dac", "out", {})

    svr_dac = find_path(connection_dict, "svr", "dac", {})
    dac_fft = find_path(connection_dict, "dac", "fft", {})
    fft_out = find_path(connection_dict, "fft", "out", {})

    print((svr_dac * dac_fft * fft_out) + (svr_fft * fft_dac * dac_out))


if __name__ == '__main__':
    main()
