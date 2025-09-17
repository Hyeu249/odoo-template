{
    "name": "Gay Studio",
    "author": "Gay Studio",
    "website": "www.gay-studio.com",
    "summary": "Gay Studio",
    "depends": ["mail"],
    "data": [
        "security/role.xml",
        "security/rule.xml",
        "security/ir.model.access.csv",
        "data/sequence.xml",
        "views/menu.xml",
        "views/sheet.xml",
        "wizard/add_sheet.xml",
    ],
    "application": True,
    "assets": {
        "web.assets_backend": [
            "studio/static/src/css/**",
            "studio/static/src/js/**",
        ],
    },
}
