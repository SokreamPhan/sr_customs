# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)
{
    "name": "Cambodia Localization - Tax Invoice & Commerical Invoice",
    "summary": """
            This addon will add two new print options on Customer Invoices,
            following Cambodia's Tax Invoice and Commercial Invoice
        """,
    "version": "14.0.1.0.0",
    "author": "SokreamPhan",
    "license": "AGPL-3",
    "website": "",
    "category": "Localization / Accounting",
    "depends": ["account"],
    "data": [
        "views/res_partner_views.xml",
        "views/report_kh_tax_invoice.xml",
        "views/report_kh_commercial_invoice.xml",
    ],
    'images': ['static/description/logo.gif'],
    "installable": True,
}
