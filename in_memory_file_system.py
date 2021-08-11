'''
Relax

Better to get some than None

have fun

Problem
Design an in-memory file system to simulate the following functions:

ls: Given a path in string format. If it is a file path, return a list that only contains this file’s name. If it is a directory path, return the list of file and directory names in this directory. Your output (file and directory names together) should in lexicographic order.

mkdir: Given a directory path that does not exist, you should make a new directory according to the path. If the middle directories in the path don’t exist either, you should create them as well. This function has void return type.

addContentToFile: Given a file path and file content in string format. If the file doesn’t exist, you need to create that file containing given content. If the file already exists, you need to append given content to original content. This function has void return type.

readContentFromFile: Given a file path, return its content in string format.

design
use a tree
    
'''
from typing import List
class FileSystem:
    class Node:
        def __init__(self, name, isdir):
            self.children = []
            self.content = ""
            self.isdir = isdir
            self.lookup = {}
            self.name = name
        
    def __init__(self):
        self.root = FileSystem.Node("", True)
        
    def get_node(self, names: List[str]) -> "FileSystem.Node":
        node = self.root
        for name in names:
            node = node.lookup[name]
        return node
        
    @staticmethod
    def path_to_list(path):
        '''
        in "/root/pies"
        out ["root", "pies"]        
        '''
        path = path.strip("/")
        if path == "":
            return []
        names = path.split("/")
        return names
        
    def mkdir(self, path):
        '''
        examples:
        root level -> names == []
        subdir level -> names = [a, b, c, d]
        '''
        if not path:
            raise ValueError
        names = self.path_to_list(path)
        parentnode = self.get_node(names[:len(names)-1])
        newdir = self.newchild(parentnode, names[-1], True)       
    
    def ls(self, path):
        '''
        / --> [] 
        '''
        res = []
        names = self.path_to_list(path)
        node = self.get_node(names)
        if node.isdir:
            for childnode in node.children:
                res.append(childnode.name)
        else:
            res.append(node.name)
        return path, sorted(res)
    
    def newchild(self, parentnode, childname, isdir):
        file = FileSystem.Node(childname, isdir)
        #so when get_node is called, we O(1) time get the node based on string val
        parentnode.lookup[childname] = file
        parentnode.children.append(file)
        return file
        
    def addContentToFile(self, path, content):
        '''
        path = "/root/files/f1", 
        content = "; more content for f1"
        '''
        names = self.path_to_list(path) # root, files, f1
        parentnode = self.get_node(names[:len(names)-1]) # files
        if names[-1] not in parentnode.lookup:
            file = self.newchild(parentnode, names[-1], False)
        else:
            file = parentnode.lookup[names[-1]]
        file.content += content

    def readContentFromFile(self, path):
        '''
                path = "/root/files/f1", 
        '''
        names = self.path_to_list(path)
        node = self.get_node(names)        
        return node.content
        
fs = FileSystem()

fs.mkdir("/root")
print(fs.ls("/")) # root


fs.mkdir("/root/files")
fs.mkdir("/root/pies")

print(fs.ls("/root/files/")) # f1, f2  NOT f2, f1
print(fs.ls("/root/")) # pies, files, f1, f2

fs.addContentToFile("/root/files/f1", "f1 content")
fs.addContentToFile("/root/files/f1", "; more content for f1")
fs.addContentToFile("/root/files/f2", "f2 content")
fs.mkdir("/root/files/f3-dir/")

print(fs.ls("/root/files")) # f1, f2, f3-dir
print(fs.ls("/root/files/f1")) # f1
print(fs.ls("/root/files/f2")) # f2


print(fs.readContentFromFile("/root/files/f2")) # f2 content
print(fs.readContentFromFile("/root/files/f1")) # f1 content
