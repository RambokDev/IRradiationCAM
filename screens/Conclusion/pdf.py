import top as top
from fpdf import FPDF, XPos, YPos


class PDF(FPDF):

    def header(self):
        # logo
        self.image('img/icam.png', 150, 5, 25)
        self.set_font('helvetica', '', 12)
        self.cell(0, 10, '{}'.format(nom1), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.cell(0, 10, '{}'.format(nom2), new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        # self.cell(0, 10, 'TP', border=False, ln=1, align='C')
        # self.set_font('helvetica', 'B', 20)
        self.ln(10)

    # def Title(self):
    #     self.set_font('helvetica', 'B', 20)
    #     self.cell(10, 10, 'TP', border=False, ln=1, align='C')
    def footer(self):
        self.set_y(-15)
        self.image('img/footer.png', 5, 260, 215)


class mainPDF:
    global nom1, nom2
    nom1 = "Gregoire BLANC"
    nom2 = "Charles GAUTHEREAU"
    # create a fpdf object
    pdf = PDF('P', 'mm', 'A4')
    pdf.set_auto_page_break(auto=True, margin=50)
    pdf.add_page()
    pdf.set_font('helvetica', '', 16)
    pdf.set_font('helvetica', 'B', 34)
    pdf.line(10, 70, 200, 70)
    pdf.cell(0, 120, "TP IR-RadiationCAM", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
    pdf.line(10, 150, 200, 150)
    pdf.image('img/image3.png', x=60, y=170, w=90, h=70, type='', link='')
    pdf.add_page()

    # Surface Observation
    pdf.set_font('helvetica', 'U', 20)
    pdf.cell(0, 20, "I - Surface Observation :  ", new_x=XPos.LMARGIN, new_y=YPos.NEXT, )






    pdf.set_font('helvetica', '', 15)
    pdf.set_text_color(255, 0, 0)
    pdf.cell(0, 10, "Not painted aluminium surface", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')

    pdf.set_font('helvetica', '', 12)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 5, "Write what do you observe?", new_x=XPos.LMARGIN, new_y=YPos.NEXT, )
    border = pdf.x
    pdf.multi_cell(150, 5, 'What is the disadvantage of such a surface for infrared measurements?\n\n', 0, 0)

    # Reset x coordinate
    pdf.x = border
    pdf.cell(0, 10, "Your answer :", new_x=XPos.LMARGIN, new_y=YPos.NEXT, )
    pdf.set_font('helvetica', 'I', 12)
    pdf.multi_cell(150, 5, 'ppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp '
                           'ppppppppppppppppppppppppppppppppppppppppppppppppppppppp\n\n\n', 0, 0)
    # Reset x coordinate
    pdf.x = border







    pdf.set_font('helvetica', '', 15)
    pdf.set_text_color(255, 0, 0)
    pdf.cell(0, 10, "Black painted aluminium surface", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')

    pdf.set_font('helvetica', '', 12)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 5, "Write what do you observe?", new_x=XPos.LMARGIN, new_y=YPos.NEXT, )

    pdf.multi_cell(170, 5, 'Explain why the measure is more realistic in comparison to the aluminum surface '
                           'temperature measurement?\n\n', 0, 0)

    # Reset x coordinate
    pdf.x = border
    pdf.cell(0, 10, "Your answer :", new_x=XPos.LMARGIN, new_y=YPos.NEXT, )
    pdf.set_font('helvetica', 'I', 12)
    pdf.multi_cell(170, 5, 'ppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp '
                           'ppppppppppppppppppppppppppppppppppppppppppppppppppppppp\n\n\n', 0, 0)
    # Reset x coordinate
    pdf.x = border







    pdf.set_font('helvetica', '', 15)
    pdf.set_text_color(255, 0, 0)
    pdf.cell(0, 10, "Glass surface", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')

    pdf.set_font('helvetica', '', 12)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 5, "Write what do you observe?", new_x=XPos.LMARGIN, new_y=YPos.NEXT, )

    pdf.multi_cell(170, 5, 'Comment on the properties of the glass in the field of the visible and infrared. Do the '
                           'same by placing this time, the thin PVC sheet. What do you observe compared to the '
                           'previous experience?\n\n', 0, 0)

    # Reset x coordinate
    pdf.x = border
    pdf.cell(0, 10, "Your answer :", new_x=XPos.LMARGIN, new_y=YPos.NEXT, )
    pdf.set_font('helvetica', 'I', 12)
    pdf.multi_cell(170, 5, 'ppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp '
                           'ppppppppppppppppppppppppppppppppppppppppppppppppppppppp\n\n\n', 0, 0)
    # Reset x coordinate
    pdf.x = border



    pdf.add_page()


    # Contact temperature calculation
    pdf.set_font('helvetica', 'U', 20)
    pdf.cell(0, 20, "II - Contact temperature calculation :  ", new_x=XPos.LMARGIN, new_y=YPos.NEXT, )

    pdf.set_font('helvetica', '', 15)
    pdf.set_text_color(255, 0, 0)
    pdf.cell(0, 20, "Watch video and record temperatures", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')

    pdf.set_font('helvetica', '', 12)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 5, "Write what do you observe?", new_x=XPos.LMARGIN, new_y=YPos.NEXT, )

    pdf.cell(0, 10, "Your answer :", new_x=XPos.LMARGIN, new_y=YPos.NEXT, )
    pdf.set_font('helvetica', 'I', 12)
    pdf.multi_cell(170, 5, 'ppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp '
                           'ppppppppppppppppppppppppppppppppppppppppppppppppppppppp\n\n\n', 0, 0)
    # Reset x coordinate
    pdf.x = border
    pdf.set_font('helvetica', '', 12)
    pdf.cell(0, 5, "IR T foam :  XXXXXXXX   °C ", new_x=XPos.LMARGIN, new_y=YPos.NEXT, )
    pdf.cell(0, 5, "IR T aluminum :   XXXXXXXXXXX   °C ", new_x=XPos.LMARGIN, new_y=YPos.NEXT, )

    pdf.multi_cell(170, 5, '\n\nUsing your documents, calculate the temperature of contact between your skin and the foam '
                           'and between your skin and the aluminum plate considering that samples are at 23 ° C and '
                           'your skin at 37 ° C.\n\n', 0, 0)

    # Reset x coordinate
    pdf.x = border
    pdf.cell(0, 5, "Your answer :", new_x=XPos.LMARGIN, new_y=YPos.NEXT, )
    pdf.cell(0, 5, "foam :  XXXXXXXX   °C ", new_x=XPos.LMARGIN, new_y=YPos.NEXT, )
    pdf.cell(0, 5, "aluminum :   XXXXXXXXXXX   °C ", new_x=XPos.LMARGIN, new_y=YPos.NEXT, )


    # Thermal approach of electric phenomena
    pdf.set_font('helvetica', 'U', 20)
    pdf.cell(0, 20, "III - Thermal approach of electric phenomena :  ", new_x=XPos.LMARGIN, new_y=YPos.NEXT, )
















    pdf.output('screens/Conclusion/pdf1.pdf')


mainPDF()
