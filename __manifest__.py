{
    'name': "gameshop",
    'version': '1.0',
    'depends': ['base'],
    'author': "blasico_rbnico",
    'category': 'Inventario',
    'description': """
    Aplicación dedicada a la administración y registro de juegos de distintas plataformas.
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/views_game.xml',
        'views/views_platform.xml',
        'views/views_genre.xml'
    ],
    'application': 'true',
    'installable': 'true',
}