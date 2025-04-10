class Node:
    def __init__(self, val, prior):
        self.val = val
        self.prior = prior
        self.color = 'RED'
        self.lft = None
        self.rght = None
        self.parent = None


class R_B_Tree_PriorQ:
    def __init__(self):
        self.NIL = Node(None, float('-inf'))
        self.NIL.color = 'BLACK'
        self.root = self.NIL

    def insert(self, val, prior):
        new_node = Node(val, prior)
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
        return (node.val, node.prior)

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
        return (node.val, node.prior) if node and node != self.NIL else None

    def inorder(self, node=None, res=None):
        if res is None:
            res = []
        if node is None:
            node = self.root
        if node != self.NIL:
            self.inorder(node.lft, res)
            res.append((node.val, node.prior))
            self.inorder(node.rght, res)
        return res

#---------------------------------------------------------------------------#


if __name__ == "__main__":
    queue = R_B_Tree_PriorQ()

    print("__prior Q__")
    print("commands:")
    print("  insrt <value> <priority>")
    print("  extrct - del from q")
    print("  peek - the max")
    print("  view - see the q")
    print("  exit")

    while True:
        command = input(">>> ").strip().split()

        if not command:
            continue

        action = command[0].lower()

        if action == "insrt" and len(command) >= 3:
            val = " ".join(command[1:-1])
            try:
                prior = int(command[-1])
                queue.insert(val, prior)
                print(f"Insrtd: {val} (prior {prior})")
            except ValueError:
                print("Inval prior (must be int)")
        elif action == "extrct":
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
            print("Q contents (by order):")
            for item in queue.inorder():
                print(f"  {item}")
        elif action == "exit":
            print("  adios  ")
            break
        else:
            print("Error")
            
# ----  cls