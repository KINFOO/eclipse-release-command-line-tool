#!/usr/bin/python2.6
# vi: sw=4 ts=4 expandtab smarttab ai smartindent
from action.tasksaction import TasksAction
from tasks.moverepository import MoveRepository
from tasks.moveallrepositorychildren import MoveAllRepositoryChildren
from tasks.moveproductsfolder import MoveProductsFolder
from eclipsefs import EclipseFS
from tasks.moveallproductsversionfolder import MoveAllProductVersionFolder

class StableAction(TasksAction):
    def gettasks(self, args):
        efs = EclipseFS(args.directory)
        product_name = "ldt"
        stable_version = args.stableversion
        milestone_version = args.milestoneversion
        
        return[MoveAllRepositoryChildren("Archive Stable Release Repositories",
                                        efs.release_stable_composite_repository(""),
                                        efs.archive_stable_composite_repository("")),
               MoveRepository("Deliver new Stable Release Repository",
                                        efs.release_milestones_repository("", milestone_version),
                                        efs.release_stable_repository("", stable_version)),
               MoveAllRepositoryChildren("Archive milestones Release Repositories",
                                        efs.release_milestones_composite_repository(""),
                                        efs.archive_milestones_composite_repository("")),
               MoveAllProductVersionFolder("Archive Stable Products",
                                        efs.release_stable_allversion_products_directory(""),
                                        efs.archive_stable_allversion_products_directory(""),
                                        efs.products_filenames(product_name)),
               MoveProductsFolder("Deliver new Stable Products",
                                        efs.release_milestones_products_directory("", milestone_version),
                                        efs.release_stable_products_directory("", stable_version),
                                        efs.products_filenames(product_name)),
               MoveAllProductVersionFolder("Archive milestones Products",
                                        efs.release_milestones_allversion_products_directory(""),
                                        efs.archive_milestones_allversion_products_directory(""),
                                        efs.products_filenames(product_name)),] 
        
    def name(self):
        return "Stable Action"
