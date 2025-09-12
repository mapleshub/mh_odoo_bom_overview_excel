# -*- coding: utf-8 -*-
#############################################################################
#
#    Mapleshub Solutions.
#
#    Copyright (C) 2024-TODAY Mapleshub Solutions(<https://www.mapleshub.com>)
#    Author: Mapleshub Solutions(<https://www.mapleshub.com>)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
{
    'name': 'MaplesHub BoM Overview Excel Export',
    'summary': "Excel Export full BOM overview (parents, sub-BOMs, components)",
    'description': """
MaplesHub – BoM Overview → Excel Export (Odoo 18)

Export the exact data from Odoo’s BoM Overview to Excel, including parent & sub-BoMs and all component lines, 
using the same core helpers as the official PDF report.

Key Features
------------
- Flat Excel of the entire multi-level BoM (parents, sub-BoMs, components)
- No re computation: relies on report.mrp.report_bom_structure._get_bom_data
- Columns: Product, Country Codes, Qty (UoM), Lead Time (d), Route, BoM Cost, Product Cost

Notes
-----
- If no warehouse is provided via context, the first warehouse of the current companies is used.
- Users must have read access to BoM and Product.
- Tested on Odoo 18.

Built by MaplesHub
""",
    'author': "Mapleshub Solutions",
    'maintainer': 'Mapleshub Solutions',
    'company': 'Mapleshub Solutions',
    'website': "https://www.mapleshub.com",
    'support': 'service@mapleshub.com',
    'category': 'Tools',
    'version': '18.0.0.0.1',
    'sequence': 101,
    'license': 'LGPL-3',
    'depends': ['mrp'],
    'images': ["static/description/banner.png"],
    'data': [],
    'assets': {
        'web.assets_backend': [
            'mh_odoo_bom_overview_excel/static/src/bom_overview_export.xml',
        ],
    },
}
