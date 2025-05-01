from datetime import datetime
from fpdf import FPDF
from typing import Dict, Any
""""
 A vibrant and colorful design with bold fonts and modern layout blocks. Designed to stand out,
it's perfect for creative roles or tech-forward professionals.

"""
def generate_cv(data: Dict[str, Any]) -> str:
    pdf = FPDF()
    pdf.add_page()

    # Register fonts (assumes fonts exist in given path)
    pdf.add_font('Montserrat', '', 'data/font/montserrat/Montserrat-Regular.ttf', uni=True)
    pdf.add_font('Montserrat', 'B', 'data/font/montserrat/Montserrat-Bold.ttf', uni=True)
    pdf.add_font('Montserrat', 'I', 'data/font/montserrat/Montserrat-Italic.ttf', uni=True)

    # Define color palette
    primary_color = (30, 144, 255)  # DodgerBlue
    secondary_color = (245, 245, 245)  # LightGray background blocks
    header_color = (0, 102, 204)  # Darker Blue for headers

    # Header: Name & Title
    pdf.set_text_color(*primary_color)
    pdf.set_font('Montserrat', 'B', 20)
    pdf.cell(200, 12, txt=data['personal_info'].get('name', ''), ln=True, align='C')
    
    pdf.set_font('Montserrat', 'I', 12)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(200, 8, txt=data['personal_info'].get('title', ''), ln=True, align='C')

    pdf.set_font('Montserrat', '', 10)
    pdf.set_text_color(0, 0, 0)
    contact = f"{data['personal_info'].get('location', '')} | {data['personal_info'].get('email', '')} | {data['personal_info'].get('phone', '')}"
    pdf.cell(200, 6, txt=contact, ln=True, align='C')

    pdf.ln(6)
    pdf.set_draw_color(*primary_color)
    pdf.set_line_width(0.8)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(10)

    def section_title(title: str):
        pdf.set_fill_color(*secondary_color)
        pdf.set_draw_color(*primary_color)
        pdf.set_text_color(*header_color)
        pdf.set_font('Montserrat', 'B', 13)
        pdf.cell(190, 10, txt=title.upper(), ln=True, fill=True)

        pdf.set_text_color(0, 0, 0)
        pdf.set_font('Montserrat', '', 10)
        pdf.ln(2)

    # Profile
    if data.get('profile'):
        section_title("Profile")
        pdf.multi_cell(0, 6, txt=data['profile'])
        pdf.ln(5)

    # Skills
    if data.get('skills'):
        section_title("Skills")
        for category, skills in data['skills'].items():
            if skills:
                pdf.set_font('Montserrat', 'B', 10)
                pdf.set_text_color(*primary_color)
                pdf.cell(0, 6, txt=f"{category.title()}:", ln=True)
                pdf.set_font('Montserrat', '', 10)
                pdf.set_text_color(0, 0, 0)
                pdf.multi_cell(0, 6, txt=", ".join(skills))
                pdf.ln(1)

    # Experience
    if data.get('professional_experience'):
        section_title("Professional Experience")
        for exp in data['professional_experience']:
            pdf.set_font('Montserrat', 'B', 11)
            pdf.cell(100, 6, txt=exp.get('company', ''), ln=0)
            pdf.set_font('Montserrat', 'I', 10)
            duration = exp.get('duration', 'N/A') if exp.get('duration') else 'N/A'
            pdf.cell(90, 6, txt=duration, ln=True, align='R')

            pdf.set_font('Montserrat', 'B', 10)
            pdf.cell(100, 6, txt=exp.get('role', ''), ln=0)
            pdf.set_font('Montserrat', 'I', 10)
            location = exp.get('location', 'N/A') if exp.get('location') else 'N/A'
            pdf.cell(90, 6, txt=location, ln=True, align='R')

            if exp.get('tools'):
                pdf.set_font('Montserrat', '', 9)
                pdf.set_text_color(90, 90, 90)
                pdf.cell(0, 5, txt=f"Tools: {exp['tools']}", ln=True)
                pdf.set_text_color(0, 0, 0)

            if exp.get('description'):
                pdf.multi_cell(0, 6, txt=exp['description'])

            if exp.get('achievements'):
                pdf.set_font('Montserrat', 'B', 10)
                pdf.cell(0, 6, txt="Key Achievements:", ln=True)
                pdf.set_font('Montserrat', '', 10)
                for ach in exp['achievements']:
                    pdf.multi_cell(0, 6, txt=f"• {ach}")

            if exp.get('projects'):
                pdf.set_font('Montserrat', 'B', 10)
                pdf.cell(0, 6, txt="Projects:", ln=True)
                for proj in exp['projects']:
                    pdf.set_font('Montserrat', 'B', 10)
                    pdf.cell(30, 6, txt=f"{proj.get('name', '')}: ", ln=0)
                    pdf.set_font('Montserrat', '', 10)
                    pdf.multi_cell(0, 6, txt=proj.get('description', ''))

            pdf.ln(3)
            pdf.set_draw_color(230, 230, 230)
            pdf.set_line_width(0.5)
            pdf.line(10, pdf.get_y(), 200, pdf.get_y())
            pdf.ln(5)

    # Education
    if data.get('education'):
        section_title("Education")
        for edu in data['education']:
            pdf.set_font('Montserrat', 'B', 10)
            pdf.cell(100, 6, txt=edu.get('degree', ''), ln=0)
            pdf.set_font('Montserrat', 'I', 10)
            year = edu.get('year', 'N/A') if edu.get('year') else 'N/A'
            pdf.cell(90, 6, txt=year, ln=True, align='R')
            pdf.set_font('Montserrat', '', 10)
            pdf.cell(0, 6, txt=f"{edu.get('institution', '')}, {edu.get('location', '')}", ln=True)
            pdf.ln(2)

    # Languages
    if data.get('languages'):
        section_title("Languages")
        pdf.set_font('Montserrat', '', 10)
        pdf.cell(0, 6, txt=", ".join(data['languages']), ln=True)

    # Save
    #return the pdf with the applicant name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = f'static/{data["personal_info"].get("name", "CV")}_vivid_vision_cv_{timestamp}.pdf'
    pdf.output(output_path)
    return output_path
