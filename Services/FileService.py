import os



class File:
    def __init__(self, name, extension, size):
        self.name = name
        self.extension = extension
        self.size = size



class FileService:
    def __init__(self, Dir):
        self.Dir = Dir

    """
    This function returns a list of all files in the directory specified by self.Dir
    """
    def getfiles(self):
        files = [x for x in os.listdir(self.Dir) if os.path.isfile(os.path.join(self.Dir, x))]

        # -- Convert the list of files into a JSON object which lists all Files with there Names, Extensions and Sizes
        for file in files:
            name, extension = os.path.splitext(file)
            size = os.path.getsize(os.path.join(self.Dir, file))
            files[files.index(file)] = File(name, extension, str(size) + " bytes").__dict__
        return files


    """
    This function returns a list of all folders in the directory specified by self.Dir
    """
    def getfolders(self):
        folders = [x for x in os.listdir(self.Dir) if os.path.isdir(os.path.join(self.Dir, x))]

        # -- Convert the list of folders into a JSON object which lists all Folders with there Names and Sizes and files if any
        for folder in folders:
            size = sum(os.path.getsize(os.path.join(self.Dir, folder, f)) for f in os.listdir(os.path.join(self.Dir, folder)) if os.path.isfile(os.path.join(self.Dir, folder, f)))
            files = [f for f in os.listdir(os.path.join(self.Dir, folder)) if os.path.isfile(os.path.join(self.Dir, folder, f))]
            folders[folders.index(folder)] = {"name": folder, "size": str(size) + " bytes", "files": files}
        return folders




Fileser = FileService(os.getcwd())

print(Fileser.getfolders())