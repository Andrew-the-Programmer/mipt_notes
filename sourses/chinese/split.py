#!/usr/bin/env python3


import pymupdf
from pymupdf import Document


def InsertPage(self, *, docsrc, pno, rect) -> None:
    new_page = self.new_page(width=rect.width, height=rect.height)
    new_page.show_pdf_page(new_page.rect, docsrc, pno, clip=rect)


Document.InsertPage = InsertPage


def split_pdf(input_pdf, output_pdf):
    doc = pymupdf.open(input_pdf)
    new_doc = pymupdf.open()
    doc_len = len(doc)
    for page_num in range(doc_len):
        page = doc.load_page(page_num)
        rect = page.rect
        left_rect = pymupdf.Rect(rect.x0, rect.y0, rect.width / 2, rect.y1)
        right_rect = pymupdf.Rect(rect.width / 2, rect.y0, rect.x1, rect.y1)
        if page_num in [0, doc_len - 1]:
            new_doc.InsertPage(rect=rect, docsrc=doc, pno=page_num)
            continue
        if page_num == 1:
            new_doc.InsertPage(rect=right_rect, docsrc=doc, pno=page_num)
            continue
        if page_num == doc_len - 2:
            new_doc.InsertPage(rect=left_rect, docsrc=doc, pno=page_num)
            continue
        new_doc.InsertPage(rect=left_rect, docsrc=doc, pno=page_num)
        new_doc.InsertPage(rect=right_rect, docsrc=doc, pno=page_num)
    new_doc.save(output_pdf)
    new_doc.close()
    doc.close()


def main() -> None:
    # Replace with the path to your input PDF
    input_pdf = "./Chinese-Учебник_китайский_для_технических_вузов.pdf"
    output_pdf = "test.pdf"  # Replace with the path to your output PDF
    split_pdf(input_pdf, output_pdf)


if __name__ == "__main__":
    main()
