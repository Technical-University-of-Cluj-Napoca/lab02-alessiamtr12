import sys
from BST import BST
from search_engine import search_loop


def main():

    source = sys.argv[1]
    kwargs = {}
    if source.startswith("http://") or source.startswith("https://"):
        kwargs['url'] = True
    else:
        kwargs['file'] = True

    search_tree = BST(source, **kwargs)
    search_loop(search_tree)
if __name__ == "__main__":
    main()

