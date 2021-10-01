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
    
    'depends': ['contacts', 'graphql_base', 'stock', 'web_widget_numeric_step'],

    'data': [
        'security/schematic_configurator_security.xml',
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/building.xml',
        'views/level.xml',
        'views/room.xml',
        'views/installation.xml',
        'views/panel.xml',
        'views/module.xml',
    ],

    'demo': [
        'demo/demo.xml',
    ],

    'installable': True,
    'application': False,
    'auto_install': False,
}