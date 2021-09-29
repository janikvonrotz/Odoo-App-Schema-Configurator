{
    'name': "Schematic Configurator",

    'summary': """
        Configure schematics for house installations.
    """,
    
    'author': 'Mint System GmbH, Odoo Community Association (OCA)',
    'website': 'https://www.mint-system.ch',
'category': 'Manufacturing',
    'version': '14.0.1.0.0',
    'license': 'AGPL-3',
    
    'depends': ['contacts', 'graphql_base', 'stock'],

    'data': [
        'security/schematic_configurator_security.xml',
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/building.xml',
        'views/level.xml',
        'views/room.xml',
    ],

    'demo': [
        'demo/demo.xml',
    ],

    'installable': True,
    'application': False,
    'auto_install': False,
}