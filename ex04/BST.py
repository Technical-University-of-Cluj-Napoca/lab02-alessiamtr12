import urllib.request


class Node:
    def __init__(self, word: str):
        self.word = word
        self.left = None
        self.right = None

class BST:

   def __init__(self, source: str, **kwargs):
       self.results = []
       self.root = None

       is_url = kwargs.get("url", False)
       is_file = kwargs.get("file", False)

       words = []

       if is_url:
           with urllib.request.urlopen(source) as response:
               data = response.read().decode('utf-8')
               words = data.splitlines()
       else:
           if is_file:
            with open(source, 'r', encoding='utf-8') as f:
                words = [line.strip() for line in f]

       if words:
           self.root = self.buildBST(words)

   def insert(self, word, root: Node):
       if root is None:
           root = Node(word)
           return root
       if word < root.word:
           root.left = self.insert(word, root.left)
       else:
           root.right = self.insert(word, root.right)
       return root

   def buildBST(self, words: list) -> Node:
       if not words:
           return None
       mid = len(words) // 2
       root = Node(words[mid])
       root.left = self.buildBST(words[:mid])
       root.right = self.buildBST(words[mid+1:])
       return root
   def _collect(self, node: Node, prefix: str) -> None:
       if not node:
           return

       self._collect(node.left, prefix)
       if node.word.startswith(prefix):
           self.results.append(node.word)
       self._collect(node.right, prefix)

   def autocomplete(self, prefix:str) -> list[str]:
       self.results = []
       self._collect(self.root, prefix)
       return self.results