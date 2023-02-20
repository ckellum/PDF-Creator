from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")
for index, item in df.iterrows():
    space = 21
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=item["Topic"], align="L", ln=1, border=0)
    for s in range(30):
        pdf.line(10, space, 200, space)
        space += 10

    pdf.ln(260)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=item["Topic"], align="R")

    for x in range(item["Pages"] - 1):
        space = 21
        pdf.add_page()
        for s in range(30):
            pdf.line(10, space, 200, space)
            space += 10
        pdf.ln(272)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=item["Topic"], align="R")

pdf.output("output.pdf")
