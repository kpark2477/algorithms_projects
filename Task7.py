# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()

    def insert(self, path_arry, handler_msg = None):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root

        for path in path_arry:
            if path not in current_node.children:
                current_node.insert(path)
            current_node = current_node.children[path]

        current_node.handler = handler_msg

    def find(self, path_arry):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root

        for path in path_arry:
            if path not in current_node.children:
                return None
            current_node = current_node.children[path]

        return current_node.handler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.handler = None
        self.children = {}

    def insert(self, path):
        # Insert the node as before
        self.children[path] = RouteTrieNode()


# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler_msg, not_found_msg = None):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route = RouteTrie()
        self.route.root.handler = root_handler_msg
        self.not_found_msg = not_found_msg

    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and lookup functions,
        # so it should be placed in a function here
        if path == '/' or path == "":
            return []
        if path[-1] == '/':
            path = path[:-1]
        if path[0] == '/':
            path = path[1:]
        path_arry = path.split("/")
        return path_arry


    def add_handler(self, path, handler_msg):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path_arry = self.split_path(path)
        self.route.insert(path_arry, handler_msg)


    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        path_arry = self.split_path(path)
        handler_output = self.route.find(path_arry)
        if handler_output == None:
            return self.not_found_msg
        else:
            return handler_output 



# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home////////about/")) #edge case, should print not found handler
print(router.lookup("")) #edge case, should return 'root handler'



