import sys
import os
import zlib

def main():
    command = sys.argv[1]
    if command == "init":
        os.mkdir(".git")
        os.mkdir(".git/objects")
        os.mkdir(".git/refs")
        with open(".git/HEAD", "w") as f:
            f.write("ref: refs/heads/main\n")
        print("Initialized git directory")

    elif command == "cat-file":
        if sys.argv[2] == "-p":
            commit_sha = sys.argv[3]
            file_path = os.path.join(os.getcwd(), '.git', 'objects', commit_sha[:2], commit_sha[2:])

            if not os.path.exists(file_path):
                raise Exception(f'Not a valid object name {commit_sha}')
            
            with open(file_path, 'rb') as f:
                raw = zlib.decompress(f.read())
                _, content = raw.split(b"\0", maxsplit=1)
                sys.stdout.write(content.decode())

    else:
        raise RuntimeError(f"Unknown command #{command}")


if __name__ == "__main__":
    main()
