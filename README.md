# MaplesHub – BoM Overview Excel Export (Odoo 18)

Export the exact data what see in BoM Overview (including parent & sub-BoMs and all components) straight to Excel—no recalculation, no surprises.
Built by MaplesHub.

### What it does
Mirrors Odoo’s BoM Overview output using the same internal helpers (report.mrp.report_bom_structure._get_bom_data).
Flattens the tree so parent BoM rows, sub-BoM rows, and component rows are all in one sheet. 

### Columns exported:
    Product
    Country Codes
    Qty (UoM) – combined (e.g., 4 PCS)
    Lead Time (d)
    Route
    BoM Cost
    Product Cost

### How it works
    Controller route:
    GET /mrp/bom_overview/<int:bom_id>/export_xlsx
    Returns an .xlsx built with xlsxwriter.
    Data source: exactly the same structure used by Odoo’s BoM Overview PDF. No custom recomputation.

### Installation
    Place this module in your addons path (Odoo 18).
    Update app list and install: Apps → Update Apps List → Install.

### Support
    Built & maintained by MaplesHub Solution.
    For enhancements or support, open an issue or contact your MaplesHub rep.

* License LGPL-3

