import os

class EclipseFS:
    """Representation of build.eclipse.org file system, all needed path are computed here.
    There is no file system operation performed, only the path management is performed here."""

    # List of products name
    _PRODUCT_FILENAMES = {'ldt':
                              ['org.eclipse.ldt.product-linux.gtk.x86_64.tar.gz',
                               'org.eclipse.ldt.product-macosx.cocoa.x86_64.tar.gz',
                               'org.eclipse.ldt.product-win32.win32.x86.zip',
                               'org.eclipse.ldt.product-linux.gtk.x86.tar.gz',
                               'org.eclipse.ldt.product-win32.win32.x86_64.zip']}

    _STATS_URI = {'ldt':'http://download.eclipse.org/stats/ldt'}

    _FEATURE_ID = {'ldt':'org.eclipse.ldt',
		   'remote': 'org.eclipse.ldt.remote'}

    def __init__(self, root=None):
        # root is used for test only
        if not root:
            root='/'

        # Download constant
        self.DOWNLOAD_ROOT_DIRECTORY = os.path.join(root,
            'home/data/httpd/download.eclipse.org/ldt')

        self.RELEASE_ROOT_PRODUCTS_DIRECTORY = os.path.join(
            self.DOWNLOAD_ROOT_DIRECTORY, 'products')
        self.RELEASE_STABLE_PRODUCTS_DIRECTORY = os.path.join(
            self.RELEASE_ROOT_PRODUCTS_DIRECTORY, 'stable')
        self.RELEASE_MILESTONES_PRODUCTS_DIRECTORY = os.path.join(
            self.RELEASE_ROOT_PRODUCTS_DIRECTORY, 'milestones')

        self.RELEASE_ROOT_REPOSITORY = os.path.join(
            self.DOWNLOAD_ROOT_DIRECTORY, 'releases')
        self.RELEASE_STABLE_REPOSITORY = os.path.join(
            self.RELEASE_ROOT_REPOSITORY, 'stable')
        self.RELEASE_MILESTONES_REPOSITORY = os.path.join(
            self.RELEASE_ROOT_REPOSITORY, 'milestones')

        self.NIGHTLY_REPOSITORY = os.path.join(self.DOWNLOAD_ROOT_DIRECTORY,
            'updates-nightly')
        self.NIGHTLY_MAINTENANCE_REPOSITORY = os.path.join(
            self.DOWNLOAD_ROOT_DIRECTORY, 'updates-nightly-maintenance')

        # strange case for products we search the nightly on continuous integration
        self.SHARED_LDT_FOLDER = os.path.join(root, 'shared/tools/ldt')
        self.SHARED_PRODUCTS_FOLDER = os.path.join(self.SHARED_LDT_FOLDER,
            'products')
        self.NIGHTLY_PRODUCTS_DIRECTORY = os.path.join(
            self.SHARED_PRODUCTS_FOLDER, 'nightly')
        self.NIGHTLY_MAINTENANCE_PRODUCTS_DIRECTORY = os.path.join(
            self.SHARED_PRODUCTS_FOLDER, 'nightly-maintenance')

        # Archive constant
        self.ARCHIVE_ROOT_DIRECTORY = os.path.join(root,
            'home/data/httpd/archive.eclipse.org/ldt')

        self.ARCHIVE_ROOT_PRODUCTS_DIRECTORY = os.path.join(
            self.ARCHIVE_ROOT_DIRECTORY, 'products')
        self.ARCHIVE_MILESTONES_PRODUCTS_DIRECTORY = os.path.join(
            self.ARCHIVE_ROOT_PRODUCTS_DIRECTORY, 'milestones')
        self.ARCHIVE_STABLE_PRODUCTS_DIRECTORY = os.path.join(
            self.ARCHIVE_ROOT_PRODUCTS_DIRECTORY, 'stable')

        self.ARCHIVE_ROOT_REPOSITORY = os.path.join(self.ARCHIVE_ROOT_DIRECTORY,
            'releases')
        self.ARCHIVE_STABLE_REPOSITORY = os.path.join(
            self.ARCHIVE_ROOT_REPOSITORY, 'stable')
        self.ARCHIVE_MILESTONES_REPOSITORY = os.path.join(
            self.ARCHIVE_ROOT_REPOSITORY, 'milestones')

    # products name
    ############################
    def products_filenames(self, product):
        return self._PRODUCT_FILENAMES[product]

    # statistics
    ############################
    def stats_uri(self, product):
        return self._STATS_URI[product]

    def feature_id(self, product):
        return self._FEATURE_ID[product]

    # Release paths
    ############################
    def release_stable_composite_repository(self, product=''):
        return os.path.join(self.RELEASE_STABLE_REPOSITORY, product)

    def release_stable_repository(self, product='', version=''):
        return os.path.join(self.RELEASE_STABLE_REPOSITORY, product, version)

    def release_stable_allversion_products_directory(self, product=''):
        return os.path.join(self.RELEASE_STABLE_PRODUCTS_DIRECTORY, product)

    def release_stable_products_directory(self, product='', version=''):
        return os.path.join(self.RELEASE_STABLE_PRODUCTS_DIRECTORY, product,
            version)

    def release_milestones_composite_repository(self, product=''):
        return os.path.join(self.RELEASE_MILESTONES_REPOSITORY, product)

    def release_milestones_repository(self, product='', version=''):
        return os.path.join(self.RELEASE_MILESTONES_REPOSITORY, product,
            version)

    def release_milestones_allversion_products_directory(self,product=''):
        return os.path.join(self.RELEASE_MILESTONES_PRODUCTS_DIRECTORY, product)

    def release_milestones_products_directory(self,product='', version=''):
        return os.path.join(self.RELEASE_MILESTONES_PRODUCTS_DIRECTORY, product,
            version)

    # Archive paths
    ############################
    def archive_stable_composite_repository(self, product=''):
        return os.path.join(self.ARCHIVE_STABLE_REPOSITORY, product)

    def archive_stable_repository(self, product='', version=''):
        return os.path.join(self.ARCHIVE_STABLE_REPOSITORY, product, version)

    def archive_stable_allversion_products_directory(self,product=''):
        return os.path.join(self.ARCHIVE_STABLE_PRODUCTS_DIRECTORY, product)

    def archive_stable_products_directory(self, product='', version=''):
        return os.path.join(self.ARCHIVE_STABLE_PRODUCTS_DIRECTORY, product,
            version)

    def archive_milestones_composite_repository(self, product=''):
        return os.path.join(self.ARCHIVE_MILESTONES_REPOSITORY, product)

    def archive_milestones_repository(self, product='', version=''):
        return os.path.join(self.ARCHIVE_MILESTONES_REPOSITORY, product,
            version)

    def archive_milestones_allversion_products_directory(self, product=''):
        return os.path.join(self.ARCHIVE_MILESTONES_PRODUCTS_DIRECTORY, product)

    def archive_milestones_products_directory(self, product='', version=''):
        return os.path.join(self.ARCHIVE_MILESTONES_PRODUCTS_DIRECTORY, product,
            version)

    # Nightly paths
    ############################
    def nightly_repository(self, product=''):
        return os.path.join(self.NIGHTLY_REPOSITORY, product)

    def nightly_products_directory(self, product=''):
        return os.path.join(self.NIGHTLY_PRODUCTS_DIRECTORY, product)

    def nightly_maintenance_products_directory(self, product=''):
        return os.path.join(self.NIGHTLY_MAINTENANCE_PRODUCTS_DIRECTORY,
            product)

    def nightly_maintenance_repository(self, product=''):
        return os.path.join(self.NIGHTLY_MAINTENANCE_REPOSITORY, product)
