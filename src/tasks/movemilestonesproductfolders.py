'''
    move only the millestones of the given stable version from a products folder from to another
'''
import os
import shutil
import productutils
from tasks.moveallproductsversionfolder import MoveAllProductVersionFolder

class MoveMilestonesProductFolders(MoveAllProductVersionFolder):
    def __init__(self, name, source_path, dest_path,product_filenames,stable_version):
        MoveAllProductVersionFolder.__init__(self, name, source_path, dest_path,product_filenames)
        self._stable_version = stable_version
    
    def check(self):
        return MoveAllProductVersionFolder.check(self)
        
    def run(self):
        report =[]
        
        for sf in os.listdir(self._source_path):
            folder_version = sf
            if folder_version.startswith(self._stable_version):
                dest_path = os.path.join(self._dest_path,sf)
                shutil.move(os.path.join(self._source_path,sf),dest_path)
                productutils.set_file_permissions(dest_path)
                report.append("Products {0} moved.".format(sf))
        
        #TODO change file permissions
        if len(report) == 0:
            report.append("No products to move ...")
        
        return report
                
    def name(self):
        return self._name
