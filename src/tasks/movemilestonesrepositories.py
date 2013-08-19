'''
 task use to move only the millestones of the given stable version from a composite repository to another
'''
import repositoryutils
from tasks.moveallrepositorychildren import MoveAllRepositoryChildren

class MoveMilestonesRepositories(MoveAllRepositoryChildren):
    
    def __init__(self, name, source, dest, stable_version):
        MoveAllRepositoryChildren.__init__(self, name, source, dest)
        self._stable_version = stable_version
    
    def check(self):
        return  MoveAllRepositoryChildren.check(self)
        
    def run(self):
        report  = []
        # move all children
        for child_name in repositoryutils.composite_repository_list_child(self._source):
            folder_version = child_name
            if folder_version.startswith(self._stable_version):
                repositoryutils.move_child_from_composite_repository(self._source, self._dest, child_name,child_name)
                report.append("Repo {0} moved".format(child_name))

        if len(report) == 0:
            report.append("Nothing to do.")
            
        return report       
            
    def name(self):
        return self._name
