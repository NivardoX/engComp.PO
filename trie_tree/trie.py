from trie_tree.node import Node


class Trie():
    nodes = []
    def __init__(self):
        self.last_char = False

    def delete(self,string):
        string = string.lower()

        string = list(string)
        for node in self.nodes:
            if node.char == string[0]:
                if node.delete(string,1):
                    self.nodes.pop(self.nodes.index(node))

    def add(self,string):
        string = string.lower()
        string = list(string)
        found = False
        for node in self.nodes:
            if node.char == string[0]:
                found = True
                node.char = string[0]
                string.pop(0)
                if len(string) == 0:
                    node.last_char = True
                else:
                    node.add(string)
                break
        if not found:
            node = Node(string[0])
            self.nodes.append(node)
            string.pop(0)
            if len(string) == 1:
                node.last_char = True
            else:
                node.add(string)

    def print(self):
        for node in self.nodes:
            print("____________________________")
            if node.last_char:
                print(node.char.upper(),end=' ')
            else:
                print(node.char, end=' ')

            node.print(1)
