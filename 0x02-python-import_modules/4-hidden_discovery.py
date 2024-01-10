#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_file
    for name in dict(hidden_file):
        if name[0] != '_' and name[1] != '_':
            print(name)
