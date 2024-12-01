from typing import List, Dict


class Terminal:
    def __init__(self):
        self.root = Directory('/', '/')
        self.current_directory = self.root
        self.directories = list()
        self.files = list()

        self.ls_results = list()
        self.expecting_ls_results = False

    def process_line(self, line):
        if line[0] != '$':
            self.ls_results.append(line)
            return

        if self.expecting_ls_results:
            self.ls(self.ls_results)
            self.ls_results = list()
            self.expecting_ls_results = False

        items = line.split(' ')
        command = items[1]

        match command:
            case 'cd':
                arg = items[2]
                self.cd(arg)

            case 'ls':
                self.expecting_ls_results = True


    def cd(self, arg: str):
        if arg[0] == '/': self.current_directory = self.root
        elif arg == '..': self.current_directory = self.current_directory.parent
        else: self.current_directory = self.current_directory.add_directory(arg)

    def ls(self, result: List):
        for item in result:
            type, name = item.split(' ')

            if type == 'dir':
                self.current_directory.add_directory(name)

            else:
                self.current_directory.add_file(name, int(type))

    def print_filesystem(self):
        self.root.print_dir(0)


class Directory:
    def __init__(self, name: str, path: str, parent: 'Directory' = None):
        self.name = name
        self.parent = parent
        self.path = path

        self.directories: Dict[str, 'Directory'] = dict()
        self.files: Dict[str, File] = dict()
        self.size = 0

    def add_file(self, name: str, size: int):
        new_file_path = f'{self.path}/{name}'
        new_file = File(name, new_file_path, size)
        if self.files.get(name) == None:
            self.files[name] = new_file

    def add_directory(self, name: str):
        new_dir_path = f'{self.path}/{name}'
        new_dir = Directory(name, new_dir_path, self)
        if self.directories.get(name) == None:
            self.directories[name] = new_dir
            return new_dir

        return self.directories.get(name)


    def print_dir(self, depth: int):
        print(f'{" " * depth * 2}- {self}')
        for directory in self.directories.values():
            directory.print_dir(depth + 1)

        depth += 1
        for file in self.files.values():
            print(f'{" " * depth * 2}- {file}')

    def __eq__(self, other: 'Directory'):
        if type(self) != type(other): return False
        return self.path == other.path

    def __str__(self):
        return f'{self.name} (dir)'

    def __repr__(self):
        return self.name

    def __hash__(self):
        return hash(self.name)

class File:
    def __init__(self, name: str, path: str, size: int):
        self.path = path
        self.size = size
        self.name = name

    def __str__(self):
        return f'{self.name} (file, size={self.size})'

    def __repr__(self):
        return self.name

    def __hash__(self):
        return hash(self.name)


def main():
    with open('example_1.txt') as terminal_output:
        lines = terminal_output.readlines()
        lines = [line.rstrip() for line in lines]

    terminal = Terminal()
    for line in lines:
        terminal.process_line(line)

    terminal.print_filesystem()

if __name__ == '__main__':
    main()