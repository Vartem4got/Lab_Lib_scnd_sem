class Node:
    def __init__(self, id, name, prior):
        self.id  = id
        self.name = name
        self.prior = prior
        self.color = 'RED'
        self.lft = None
        self.rght = None
        self.parent = None


class R_B_Tree_PriorQ:
    
    def __init__(self):
        self.NIL = Node(None, None, float('-inf'))
        self.NIL.color = 'BLACK'
        self.NIL.lft = self.NIL
        self.NIL.rght = self.NIL
        self.NIL.parent = self.NIL
        self.root = self.NIL
        self.nodes_by_id = {}

    def insert(self, id, name, prior):
        if id in self.nodes_by_id:
            print(f"ID {id} already exists!")
            return
        new_node = Node(id, name, prior)
        new_node.lft = self.NIL
        new_node.rght = self.NIL
        parent = None
        current = self.root

        while current != self.NIL:
            parent = current
            if new_node.prior > current.prior:
                current = current.lft
            else:
                current = current.rght

        new_node.parent = parent

        if not parent:
            self.root = new_node
        elif new_node.prior > parent.prior:
            parent.lft = new_node
        else:
            parent.rght = new_node

        new_node.color = 'RED'
        self._fix_insert(new_node)
        self.nodes_by_id[id] = new_node

    def _fix_insert(self, node):
        while node != self.root and node.parent.color == 'RED':
            if node.parent == node.parent.parent.lft:
                uncle = node.parent.parent.rght
                if uncle.color == 'RED':
                    node.parent.color = 'BLACK'
                    uncle.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    node = node.parent.parent
                else:
                    if node == node.parent.rght:
                        node = node.parent
                        self._lft_rotate(node)
                    node.parent.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    self._rght_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.lft
                if uncle.color == 'RED':
                    node.parent.color = 'BLACK'
                    uncle.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    node = node.parent.parent
                else:
                    if node == node.parent.lft:
                        node = node.parent
                        self._rght_rotate(node)
                    node.parent.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    self._lft_rotate(node.parent.parent)

        self.root.color = 'BLACK'

    def _lft_rotate(self, x):
        y = x.rght
        x.rght = y.lft
        if y.lft != self.NIL:
            y.lft.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.lft:
            x.parent.lft = y
        else:
            x.parent.rght = y
        y.lft = x
        x.parent = y

    def _rght_rotate(self, x):
        y = x.lft
        x.lft = y.rght
        if y.rght != self.NIL:
            y.rght.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.rght:
            x.parent.rght = y
        else:
            x.parent.lft = y
        y.rght = x
        x.parent = y

    def _minimum(self, node):
        while node.lft != self.NIL:
            node = node.lft
        return node

    def extract_max(self):
        if self.root == self.NIL:
            return None
        node = self._maximum(self.root)
        self._delete_node(node)
        return (node.id, node.name, node.prior)

    def _maximum(self, node):
        while node.rght != self.NIL:
            node = node.rght
        return node 

    def _transplant(self, u, v):
        if not u.parent:
            self.root = v
        elif u == u.parent.lft:
            u.parent.lft = v
        else:
            u.parent.rght = v
        v.parent = u.parent

    def _delete_node(self, node):
        y = node
        y_original_color = y.color
        if node.lft == self.NIL:
            x = node.rght
            self._transplant(node, node.rght)
        elif node.rght == self.NIL:
            x = node.lft
            self._transplant(node, node.lft)
        else:
            y = self._minimum(node.rght)
            y_original_color = y.color
            x = y.rght
            if y.parent == node:
                x.parent = y
            else:
                self._transplant(y, y.rght)
                y.rght = node.rght
                y.rght.parent = y
            self._transplant(node, y)
            y.lft = node.lft
            y.lft.parent = y
            y.color = node.color
        if y_original_color == 'BLACK':
            self._fix_delete(x)
            
        #___________________________#  
    def delete_by_id(self, id):
        node = self.nodes_by_id.get(id)
        if not node:
            print(f"No ticket with ID {id}")
            return
        self._delete_node(node)
        del self.nodes_by_id[id]
        print(f"Deleted ticket ID {id}")
        
    def search_by_id(self, id):
        node = self.nodes_by_id.get(id)
        if node:
            print(f"Ticket ID {node.id}: {node.name} (prior {node.prior})")
        else:
            print("Not found")
        #___________________________#
        
    def _fix_delete(self, x):
        while x != self.root and x.color == 'BLACK':
            if x == x.parent.lft:
                w = x.parent.rght
                if w.color == 'RED':
                    w.color = 'BLACK'
                    x.parent.color = 'RED'
                    self._lft_rotate(x.parent)
                    w = x.parent.rght
                if w.lft.color == 'BLACK' and w.rght.color == 'BLACK':
                    w.color = 'RED'
                    x = x.parent
                else:
                    if w.rght.color == 'BLACK':
                        w.lft.color = 'BLACK'
                        w.color = 'RED'
                        self._rght_rotate(w)
                        w = x.parent.rght
                    w.color = x.parent.color
                    x.parent.color = 'BLACK'
                    w.rght.color = 'BLACK'
                    self._lft_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.lft
                if w.color == 'RED':
                    w.color = 'BLACK'
                    x.parent.color = 'RED'
                    self._rght_rotate(x.parent)
                    w = x.parent.lft
                if w.rght.color == 'BLACK' and w.lft.color == 'BLACK':
                    w.color = 'RED'
                    x = x.parent
                else:
                    if w.lft.color == 'BLACK':
                        w.rght.color = 'BLACK'
                        w.color = 'RED'
                        self._lft_rotate(w)
                        w = x.parent.lft
                    w.color = x.parent.color
                    x.parent.color = 'BLACK'
                    w.lft.color = 'BLACK'
                    self._rght_rotate(x.parent)
                    x = self.root
        x.color = 'BLACK'

    def peek(self):
        node = self._maximum(self.root)
        return (node.id, node.name, node.prior)

    def inorder(self, node=None, res=None):
        if res is None:
            res = []
        if node is None:
            node = self.root
        if node != self.NIL:
            self.inorder(node.lft, res)
            self.inorder(node.rght, res)
            res.append((node.id, node.name, node.prior))
        return res

#---------------------------------------------------------------------------#


if __name__ == "__main__":
    
    try:
        print("== STARTING PROGRAM ==")
        queue = R_B_Tree_PriorQ()
        print("Queue initialized.")
    except Exception as e:
        print(f"Error during queue initialization: {e}")
        raise

    print("__prior Q__")
    print("commands:")
    print("  extrct - del from q")
    print("  peek - the max")
    print("  view - see the q")
    
    print("  add <id> <name> <priority>")
    print("  del <id>")
    print("  search <id>")
    
    print("  exit")

    while True:
        
        command = input(">>> ").strip().split()

        if not command:
            continue

        action = command[0].lower()

        if action == "extrct":
            result = queue.extract_max()
            if result:
                print(f"Extrcted: {result}")
            else:
                print("Q empty.")
        elif action == "peek":
            result = queue.peek()
            if result:
                print(f"Top element: {result}")
            else:
                print("Q empty.")
        elif action == "view":
            print("Content")
            for item in queue.inorder():
                print(f"  {item}")
        elif action == "exit":
            print("  adios  ")
            break
        
#_____________________________________________#
        elif action == "add" and len(command) >= 4:
            try:
                id = int(command[1])
                name = " ".join(command[2:-1])
                prior = int(command[-1])
                queue.insert(id, name, prior)
                print(f"Added: {name} (ID {id}, Prior {prior})")
            except ValueError:
                print("Invalid ID or priority")

        elif action == "del" and len(command) == 2:
            try:
                id = int(command[1])
                queue.delete_by_id(id)
            except ValueError:
                print("Invalid ID")

        elif action == "search" and len(command) == 2:
            try:
                id = int(command[1])
                queue.search_by_id(id)
            except ValueError:
                print("Invalid ID")
#_____________________________________________#

        else:
            print("Error??")
            
            
# ----  cls
