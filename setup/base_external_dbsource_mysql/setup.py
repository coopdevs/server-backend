import setuptools

setuptools.setup(
    setup_requires=['setuptools-odoo'],
    odoo_addon={
        'external_dependencies_override': {
            'python': {

                'MySQLdb': 'mysqlclient==2.0.1',
            }
        },
    }
)
