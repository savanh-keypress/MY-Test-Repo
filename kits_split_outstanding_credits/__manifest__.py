{
    "name": "Split Outstanding Credits",
    'sequence': 1,
    "version": "16.0.1.0.2",
    "category": "Extra Tools",
    "author": "Keypress IT Services",
    "website": "https://keypress.co.in/",
    "data": [
        "security/ir.model.access.csv",
        "wizard/outstanding_credit_split_wizard_view.xml",
        "wizard/res_config_setting_invoice_view.xml",
    ],
    "assets":{
        'web.assets_backend': [
            ('replace',"account/static/src/components/account_payment_field/account_payment_field.js","kits_split_outstanding_credits/static/src/js/account_payment_field.js"),
        ],
     },

    "summary": "The tool to Fetch data",
    "description": '',
    "license": "AGPL-3",
    "application": True,
    "installable": True,
    "auto_install": False,
    "depends": ['base','account'],
}