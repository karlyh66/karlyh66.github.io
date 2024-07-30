# 1166: design file system (medium)

class FileSystem(object):

    def __init__(self):
        self.path2value = defaultdict(int)
        self.path2value[''] = -1
        

    def createPath(self, path, value):
        """
        :type path: str
        :type value: int
        :rtype: bool
        """
        dirs = path.split('/')
        parent = '/'.join(dirs[:-1])
        if path in self.path2value or parent not in self.path2value:
            return False
        self.path2value[path] = value
        return True

    def get(self, path):
        """
        :type path: str
        :rtype: int
        """
        if path in self.path2value:
            return self.path2value[path]
        return -1
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
