'''
    add a repository to a given composite repository
'''
import repositoryutils
class PublishRepository:
    
    def __init__(self, name, source_path, dest_path,repository_name,stats_uri,feature_id):
        self._name = name
        self._source_path = source_path
        self._dest_path = dest_path
        self._repository_name = repository_name
        self._stats_uri = stats_uri
        self._feature_id = feature_id
        
    def check(self):
        # check if source is a composite repository
        if not repositoryutils.is_repository(self._source_path):
            raise Exception("source {0} is not a  repository".format(self._source_path))
        
        # check if destination is a composite repository 
        if not repositoryutils.is_composite_repository(self._dest_path):
            raise Exception("destination {0} is not a composite repository".format(self._dest_path))
        
        # check if destination does not already contains the repository to move
        if repositoryutils.composite_repository_contains(self._dest_parent_path, self._repository_name):
            raise Exception("destination {0} already contains a child {1}".format(self._dest_parent_path, self._repository_name))
        
        return ["Repo {0} will be copy to {1} with the name {2}".format(self._source_path,self._dest_path, self._repository_name),
                "Active Statistics for {0} ".format(self._repository_name)]            
        
    def run(self):
        report = []
        
        repositoryutils.add_child_to_composite_repository(self._source_path,self._dest_path, self.repository_name)
        report.append("Repo {0} added".format(self._repository_name))
        
        repositoryutils.activate_stats(self._source_path,self._stats_uri, self._feature_id)
        report.append("Statistics activated for {0}".format(self._repository_name))
        
        return report
            
    def name(self):
        return self._name