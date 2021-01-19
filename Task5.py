class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}
    
    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()
        
        
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point

        suffix_arry = []

        def recurse_down(node, suffix = ''):

            if node.is_word:
                suffix_arry.append(suffix)

            for child in node.children:
                suffix += child
                child_trie = node.children[child]
                recurse_down(child_trie, suffix)

            return

        recurse_down(self)

        return suffix_arry

        


        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                current_node.insert(char)
            current_node = current_node.children[char]

        current_node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current_node = self.root

        for char in prefix:
            if char not in current_node.children:
                print ("There is no word with that prefix in the trie")
                return None
            current_node = current_node.children[char]

        return current_node


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

prefixNode = MyTrie.find('a')
print(prefixNode.suffixes())

prefixNode = MyTrie.find('') #edge case, empty string, it should return all the words in the trie
print(prefixNode.suffixes())

prefixNode = MyTrie.find('IHateCovid') #edge case, nonexistent word, it should return fail message.

