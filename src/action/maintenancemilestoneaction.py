#!/usr/bin/python2.6
from action.tasksaction import TasksAction
from eclipsefs import EclipseFS
from tasks.publishrepository import PublishRepository
from tasks.copyproductsfolder import CopyProductsFolder

class MaintenanceMilestoneAction(TasksAction):
    def gettasks(self,args):

        efs = EclipseFS(args.directory)
        milestone_version = args.milestoneversion
        project_name = "ldt"
        product_name = "ldt"
        remote_name = "remote"

        return[PublishRepository("Publish new Maintenance Milestones Release Repositories",
                                        efs.nightly_maintenance_repository(),
                                        efs.release_milestones_composite_repository(),
                                        milestone_version,
                                        efs.stats_uri(project_name),
                                        [efs.feature_id(product_name),efs.feature_id(remote_name)]
                                        ),
               CopyProductsFolder("Deliver new Maintenance Milestones Products",
                                        efs.nightly_maintenance_products_directory(),
                                        efs.release_milestones_products_directory("", milestone_version),
                                        efs.products_filenames(product_name))]

    def name(self):
        return "Maintenance Milestone Action"
