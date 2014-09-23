#!/usr/bin/python2.6
# vi: sw=4 ts=4 expandtab smarttab ai smartindent
from action.tasksaction import TasksAction
from eclipsefs import EclipseFS
from tasks.moverepository import MoveRepository
from tasks.movemilestonesrepositories import MoveMilestonesRepositories
from tasks.moveproductsfolder import MoveProductsFolder
from tasks.movemilestonesproductfolders import MoveMilestonesProductFolders

class MaintenanceStableAction(TasksAction):
    def gettasks(self, args):
        efs = EclipseFS(args.directory)
        product_name = "ldt"
        stable_version = args.stableversion
        milestone_version = args.milestoneversion
        
        return[MoveRepository("Deliver new Maintenance Stable Release Repository",
                                        efs.release_milestones_repository("", milestone_version),
                                        efs.release_stable_repository("", stable_version)),
               MoveMilestonesRepositories("Archive Maintenance Milestones Release Repositories",
                                        efs.release_milestones_composite_repository(""),
                                        efs.archive_milestones_composite_repository(""),
                                        stable_version),
               MoveProductsFolder("Deliver new Maintenance Stable Products",
                                        efs.release_milestones_products_directory("", milestone_version),
                                        efs.release_stable_products_directory("", stable_version),
                                        efs.products_filenames(product_name)),
               MoveMilestonesProductFolders("Archive Maintenance Milestones Products",
                                        efs.release_milestones_allversion_products_directory(""),
                                        efs.archive_milestones_allversion_products_directory(""),
                                        efs.products_filenames(product_name),
                                        stable_version)] 
        
    def name(self):
        return "Maintenance Stable Action"
