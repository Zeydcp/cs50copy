from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # Setting font: helvetica bold 50
        self.set_font("helvetica", "B", 50)
        # Printing header:
        self.cell(0, 60, "CS50 Shirtificate", align="C", center=True)
        # Performing a line break:
        self.ln(60)

name = input("Name: ")
pdf = PDF()
pdf.add_page()
pdf.image("shirtificate.png", w=pdf.epw)
pdf.set_font("helvetica", "B", 20)
pdf.set_text_color(255, 255, 255)
pdf.set_y(135)
pdf.cell(0, 0, f"{name} took CS50", align="C", center=True)
pdf.output("shirtificate.pdf")