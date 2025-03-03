import logging
from datetime import datetime, timedelta
from odoo import models, fields, api, _
import xlsxwriter
from io import BytesIO
import base64
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class DeadStockReport(models.TransientModel):
    _name = 'dead.stock.report'
    _description = "Dead Stock Report"

    date_from = fields.Date(required=True, default=fields.Date.today())
    date_to = fields.Date(required=True, default=fields.Date.today())            

    @api.constrains('date_from', 'date_to')
    def _check_date_range(self):
        for record in self:
            if record.date_to < record.date_from:
                raise ValidationError("Range tanggal akhir tidak boleh lebih kecil dari tanggal mulai.")
   
    def action_do_report(self):
        result = self.get_report_member(self.date_from, self.date_to)    
        return result
    
    def get_report_member(self, date_from, date_to):
        # date_report = f"{date_from} - {date_to}"
        attachment = self.report_member_xls(
            getAttachment=True,
            from_date=date_from,
            to_date=date_to,
            # summary=summary,
        )

        return {
            "type": "ir.actions.act_url",
            "url": f"/web/content/{attachment.id}?download=true",
            "target": "new",
            "nodestroy": False,
        }
    


    def report_member_xls(self, getAttachment=False, from_date=None, to_date=None):
        date_reports = f"{from_date} until {to_date}"

        excel_stream = BytesIO()
        workbook = xlsxwriter.Workbook(excel_stream)
        header_format = workbook.add_format({"bold": True, "bg_color": "orange", "align": "center", "border": 1})

        # Query SQL tetap mempertahankan logika asli, hanya menambahkan saldo akhir
        sql_query = """
        SELECT DISTINCT ON (pp.id) 
            pt.name->>'en_US' AS product,
            sl.name AS lot, 
            sml.date AS tanggal_transaksi, 
            CONCAT(slcp.name, '/', slc.name) AS location, 
            sml.quantity AS saldo_akhir -- Menggunakan quantity sebagai saldo akhir dari transaksi terakhir
        FROM product_product pp
        LEFT JOIN product_template pt ON pp.product_tmpl_id = pt.id
        LEFT JOIN stock_move_line sml ON sml.product_id = pp.id
        LEFT JOIN stock_lot sl ON sl.product_id = pp.id
        LEFT JOIN stock_location slc ON sml.location_dest_id = slc.id
        LEFT JOIN stock_location slcp ON slc.location_id = slcp.id
        WHERE sml.id NOT IN (
            SELECT sml.id
            FROM stock_move_line sml
            WHERE 
            sml.date BETWEEN %s::TIMESTAMP AND %s::TIMESTAMP + INTERVAL '1 day' - INTERVAL '1 second'
            AND
            (    -- Purchase Order tanpa Receipt (tidak ada barang diterima)
                (sml.location_dest_id IN (SELECT id FROM stock_location WHERE usage = 'internal')
                AND sml.location_id IN (SELECT id FROM stock_location WHERE usage = 'supplier'))
            OR
                -- Sale Order tanpa DO (pengiriman ke customer)
                (sml.location_dest_id IN (SELECT id FROM stock_location WHERE usage = 'supplier')
                AND sml.location_id NOT IN (SELECT id FROM stock_location WHERE usage = 'internal'))
            OR
                -- Manufacturing Order tanpa barang masuk ke produksi
                (sml.location_dest_id IN (SELECT id FROM stock_location WHERE usage = 'internal')
                AND sml.location_id NOT IN (SELECT id FROM stock_location WHERE usage = 'production'))
            OR
                -- Retur pemakaian (tidak ada barang kembali ke gudang dari produksi)
                (sml.location_id IN (SELECT id FROM stock_location WHERE complete_name = 'Virtual Locations/Production')))
            )
        AND 
        sml.id IS NOT NULL
        AND sml.date < %s
        ORDER BY pp.id, sml.date DESC
        """

        self._cr.execute(sql_query, (from_date, to_date, from_date))
        results = self._cr.fetchall()

        # Membuat sheet
        sheet = workbook.add_worksheet("Report")
        sheet.write(0, 0, "No", header_format)
        sheet.write(0, 1, "Product", header_format)
        sheet.write(0, 2, "Nomor Lot", header_format)
        sheet.write(0, 3, "Tanggal Transaksi Terakhir", header_format)
        sheet.write(0, 4, "Lokasi", header_format)
        sheet.write(0, 5, "Saldo Akhir", header_format)

        # Mengisi data ke dalam Excel
        row = 1
        for index, record in enumerate(results, start=1):
            product, lot, tanggal_transaksi, location, saldo_akhir = record

            sheet.write(row, 0, index)  # No
            sheet.write(row, 1, product)  # Product
            sheet.write(row, 2, lot or "-")  # Nomor Lot
            sheet.write(row, 3, (tanggal_transaksi + timedelta(hours=7)).strftime("%Y-%m-%d %H:%M:%S") if tanggal_transaksi else "-")  # Tanggal dan Waktu (WIB)
            sheet.write(row, 4, location or "-")  # Lokasi
            sheet.write(row, 5, saldo_akhir)  # Saldo Akhir
            
            row += 1

        workbook.close()
        excel_stream.seek(0)

        filename = f"Report Dead Stock {date_reports}.xlsx"
        datas = base64.b64encode(excel_stream.read())

        if getAttachment:
            attachment = self.env["ir.attachment"].create({"name": filename, "store_fname": filename, "datas": datas})
            return attachment

        return datas
