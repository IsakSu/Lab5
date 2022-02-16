class Node:
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class Bintree:
    def __init__(self):
        self.root = None

    def put(self,newvalue):
        # Sorterar in newvalue i trädet
        self.root = self.putta(self.root,newvalue)

    def __contains__(self,value):
        # True om value finns i trädet, False annars
        return self.finns(self.root,value)

    def write(self):
        # Skriver ut trädet i inorder
        self.skriv(self.root)
        print("\n")

    def putta(self, node, newvalue):
        #Tar en nod och ett värde som parametrar, använder sedan rekursion för att sätta noden på rätt plats
        if (self.root == None):
            return Node(newvalue)
        else:
            if (node.value == newvalue):
                print(str(node.value) + " finns redan i trädet")
                return node
            if (newvalue < node.value):
                if (node.left == None):
                    node.left = Node(newvalue)
                    return node
                else:
                    self.putta(node.left, newvalue)
                    return node
            if (newvalue > node.value):
                if (node.right == None):
                    node.right = Node(newvalue)
                    return node
                else:
                    self.putta(node.right, newvalue)
                    return node

    def finns(self, node, value):
        #Kollar om ett värde finns i trädet
        if(node == None):
            return False

        if value == node.value:
            return True

        if(node.right == None and node.left == None):
            return False

        try:
            if node.value > value:
                if self.finns(node.left, value):
                    return True
                else:
                    return False
        except:
            return False

        try:
            if node.value < value:
                if (self.finns(node.right, value)):
                    return True
                else:
                    return False
        except:
            return False

    def skriv(self, node):
        #Metod för att skriva ut trädet, kallas av write()
        if(node == None):
            return

        if(node.right == None and node.left == None):
            print(str(node.value))
            return

        self.skriv(node.left)
        print(str(node.value))
        self.skriv(node.right)
        return

if __name__ == "__main__":
    from bintreeFile import Bintree

    def makeTree():
        tree = Bintree()
        data = input().strip()
        while data != "#":
            tree.put(data)
            data = input().strip()
        return tree

    def searches(tree):
        findme = input().strip()
        while findme != "#":
            if findme in tree:
                print(findme, "found")
            else:
                print(findme, "not found")
            findme = input().strip()

    def main():
        tree = makeTree()
        searches(tree)

    main()
