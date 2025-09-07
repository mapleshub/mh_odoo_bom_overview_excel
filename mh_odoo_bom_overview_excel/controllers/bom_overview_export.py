from odoo import http
from odoo.http import request,content_disposition
import io
import xlsxwriter


class BomExportController(http.Controller):

   @http.route('/mrp/bom_overview/export', type='http', auth='user', csrf=False)
   def export_bom_overview_xlsx(self, bom_id=None, **kw):
       bom = request.env['mrp.bom'].browse(int(bom_id))
       if not bom.exists():
           return request.not_found()

       rows = self._collect_bom_rows(bom)

       output = io.BytesIO()
       workbook = xlsxwriter.Workbook(output, {'in_memory': True})
       sheet = workbook.add_worksheet('BoM Overview')

       headers = ['Product', 'Qty', 'UoM', 'Lead Time(Days)', 'Route', 'BoM Cost(CAD)', 'Product Cost(CAD)']
       for c, h in enumerate(headers):
           sheet.write(0, c, h)

       for r, line in enumerate(rows, start=1):
           sheet.write(r, 0, line['product'])
           sheet.write_number(r, 1, line['qty'])
           sheet.write(r, 2, line['qty_uom'])
           sheet.write_number(r, 3, line['lead_time_days'])
           sheet.write(r, 4, line['route'])
           sheet.write_number(r, 5, line['bom_cost'])
           sheet.write_number(r, 6, line['product_cost'])
       workbook.close()
       output.seek(0)
       fname = 'BoM_Overview_%s.xlsx' % (bom.display_name.replace('/', '_'))
       return request.make_response(
           output.getvalue(),
           headers=[
               ('Content-Type', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'),
               ('Content-Disposition', content_disposition(fname)),
           ]
       )
   def _collect_bom_rows(self, bom):
       """Flat list of BOTH BOM nodes and component rows, using BoM Overview data."""
       # Pick the product & a warehouse (you can pass warehouse via context if needed)
       product = (
               bom.product_id
               or bom.product_tmpl_id.product_variant_id
               or bom.product_tmpl_id.with_context(active_test=False).product_variant_ids[:1]
       )
       warehouse = request.env['stock.warehouse'].search(
           [('company_id', 'in', request.env.companies.ids)], limit=1
       )
       report = request.env['report.mrp.report_bom_structure']
       root = report._get_bom_data(
           bom=bom,
           warehouse=warehouse,
           product=product,
           line_qty=bom.product_qty or 1,
           level=0,
       )
       rows = []
       def _push(node):
           # Keep both: 'bom' rows (parent & sub-BOM containers) and 'component' rows
           if node.get('type') in ('bom', 'component'):
               prod = node.get('product')
               # uom_str = node.get('uom') or (
               #             node.get('product') and node['product'].uom_id and node['product'].uom_id.name) or ''
               # qty_uom = f"{qty:g} {uom_str}" if uom_str else f"{qty:g}"
               if prod:  # should be present for both
                   rows.append({
                       'product': prod.display_name,
                       'qty': node.get('quantity', 0.0),
                       'qty_uom': node.get('uom').name or '',
                       'lead_time_days': node.get('lead_time') or node.get('manufacture_delay') or 0.0,
                       'route': node.get('route_name', '') or '',
                       'bom_cost': node.get('bom_cost', 0.0),
                       'product_cost': node.get('prod_cost', 0.0),
                   })
           # Recurse into children if present (sub-BOM content)
           for child in node.get('components', []) or []:
               _push(child)
       _push(root)
       return rows
