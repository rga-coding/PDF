from fpdf import FPDF
import pandas as pd


# orientation - Portrait, Landscape
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")
pdf.set_font(family="Times", style="B", size=12)
for index, row in df.iterrows():
    pdf.add_page()
    # Grey
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row['Topic'], align="L", ln=1)
    # margins from left to right, left top to bottom, left to right, right top to bottom
    pdf.line(10, 21, 200, 21)

    # FOOTER Add line break
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row['Topic'], align="R")

    # Add extra pages
    for _ in range(1, row['Pages']):
        pdf.add_page()
        # FOOTER
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row['Topic'], align="R")

pdf.output("output.pdf")
