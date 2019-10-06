from trie_tree.trie import Trie

if __name__ == '__main__':
    tree = Trie()
    tree.add("nivardo")
    tree.add('Nabucodonosor')
    tree.add('nação')
    tree.add("nivardox")
    tree.delete("nivardox")
    tree.add("nivardinho")
    tree.delete("nivardo")

    tree.print()