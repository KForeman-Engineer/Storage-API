import os



class File:
    def __init__(self, name, extension, size):
        self.name = name
        self.extension = extension
        self.size = size



class FileService:
    def __init__(self, Dir):
        self.Dir = Dir
        self.CurrentDir = os.getcwd()


    def UpdateCurrentDir(self, new_dir):
        self.CurrentDir = new_dir

    """
    This function returns a dictionary containing all files and folders in the directory specified by self.Dir
    """
    def GetAll(self):
        files = self.getfiles()
        folders = self.getfolders()
        return {"files": files, "folders": folders}

    """
    This function returns a list of all files in the directory specified by self.Dir
    """
    def getfiles(self, current_dir=None):
        if current_dir is None:
            current_dir = self.Dir
        files = [x for x in os.listdir(current_dir) if os.path.isfile(os.path.join(current_dir, x))]

        # -- Convert the list of files into a JSON object which lists all Files with there Names, Extensions and Sizes
        for file in files:
            name, extension = os.path.splitext(file)
            size = os.path.getsize(os.path.join(current_dir, file))
            files[files.index(file)] = File(name, extension, str(size) + " bytes").__dict__
        return files


    """
    This function returns a list of all folders in the directory specified by self.Dir
    """
    def getfolders(self):
        folders = [x for x in os.listdir(self.Dir) if os.path.isdir(os.path.join(self.Dir, x))]

        # -- Convert the list of folders into a JSON object which lists all Folders with there Names and Sizes and files if any
        for folder in folders:
            files = self.getfiles(current_dir=os.path.join(self.Dir, folder))  # Get the list of files in the current folder
            size = sum(os.path.getsize(os.path.join(self.Dir, folder,file["name"]))for file in files if file["name"] in os.listdir(os.path.join(self.CurrentDir, folder)))  # -- Loop every file provided from getfiles function mentioned above
            folders[folders.index(folder)] = {"name": folder, "size": str(size) + " bytes", "files": files}
        return folders




Fileser = FileService(os.getcwd())

print(Fileser.getfolders())