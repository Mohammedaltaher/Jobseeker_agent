from fpdf import FPDF
from typing import Dict, Any
from datetime import datetime
""""

A timeless, clean layout with a center-aligned header,minimalist dividers, and clear section separation.
Ideal for professionals in conservative industries (e.g., finance, law, admin).

"""
def generate_cv(data: Dict[str, Any]) -> str:
    pdf = FPDF()
    pdf.add_page()

    # Add a Unicode font to support non-ASCII characters
    pdf.add_font('DejaVuSans', '', 'data/font/dejavu/ttf/DejaVuSans.ttf', uni=True)
    pdf.add_font('DejaVuSans', 'B', 'data/font/dejavu/ttf/DejaVuSans-Bold.ttf', uni=True)
    pdf.add_font('DejaVuSans', 'I', 'data/font/dejavu/ttf/DejaVuSans-Oblique.ttf', uni=True)
    pdf.add_font('DejaVuSans', 'BI', 'data/font/dejavu/ttf/DejaVuSans-BoldOblique.ttf', uni=True)
    pdf.set_font('DejaVuSans', '', 16)

    # Header with personal info
    if 'personalInfo' in data and data['personalInfo']:
        pdf.cell(200, 10, txt=data['personalInfo'].get('name', ''), ln=True, align='C')
        pdf.set_font("DejaVuSans", 'I', 12)
        pdf.cell(200, 6, txt=data['personalInfo'].get('title', ''), ln=True, align='C')
        pdf.set_font("DejaVuSans", size=10)
        pdf.cell(200, 6, txt=f"{data['personalInfo'].get('location', '')} | {data['personalInfo'].get('email', '')} | {data['personalInfo'].get('phone', '')}", ln=True, align='C')

    # Add divider line
    pdf.ln(5)
    pdf.set_draw_color(200, 200, 200)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.cell(200, 0, ln=True)
    pdf.ln(8)

    # Profile section
    if 'profile' in data and data['profile']:
        pdf.set_font("DejaVuSans", 'B', 12)
        pdf.set_draw_color(200, 200, 200)
        pdf.set_fill_color(200, 200, 200)
        pdf.rect(x=10, y=pdf.get_y(), w=190, h=8, style='F')
        pdf.ln(1)
        pdf.cell(200, 6, txt="PROFILE", ln=True, align='C')
        pdf.ln(1)
        pdf.set_font("DejaVuSans", size=10)
        pdf.multi_cell(0, 6, txt=data['profile'])
        pdf.ln(5)

    # Skills section
    if 'skills' in data and data['skills']:
        pdf.set_font("DejaVuSans", 'B', 12)
        pdf.set_draw_color(200, 200, 200)
        pdf.set_fill_color(200, 200, 200)
        pdf.rect(x=10, y=pdf.get_y(), w=190, h=8, style='F')
        pdf.ln(1)
        pdf.cell(200, 6, txt="SKILLS", ln=True, align='C')
        pdf.ln(1)
        pdf.set_font("DejaVuSans", size=10)

        if 'categories' in data['skills'] and data['skills']['categories']:
            for category in data['skills']['categories']:
                pdf.set_font("DejaVuSans", 'B', 10)
                pdf.cell(0, 6, txt=category['name'], ln=True)
                pdf.set_font("DejaVuSans", size=10)
                pdf.multi_cell(0, 6, txt=", ".join(category['skills']))
                pdf.ln(2)

    # Professional Experience
    if 'professionalExperiences' in data and data['professionalExperiences']:
        pdf.set_font("DejaVuSans", 'B', 12)
        pdf.set_draw_color(200, 200, 200)
        pdf.set_fill_color(200, 200, 200)
        pdf.rect(x=10, y=pdf.get_y(), w=190, h=8, style='F')
        pdf.ln(1)
        pdf.cell(200, 6, txt="PROFESSIONAL EXPERIENCE", ln=True, align='C')
        pdf.ln(1)
        pdf.set_font("DejaVuSans", size=10)

        for exp in data['professionalExperiences']:
            pdf.set_font("DejaVuSans", 'B', 10)
            pdf.cell(100, 6, txt=f"{exp.get('company', '')}", ln=0)
            pdf.set_font("DejaVuSans", 'I', 10)
            pdf.cell(90, 6, txt=f"{exp.get('duration', '')}", ln=True, align='R')

            pdf.set_font("DejaVuSans", 'B', 10)
            pdf.cell(100, 6, txt=f"{exp.get('role', '')}", ln=0)
            pdf.set_font("DejaVuSans", 'I', 10)
            pdf.cell(90, 6, txt=f"{exp.get('location', '')}", ln=True, align='R')

            if 'tools' in exp and exp['tools']:
                pdf.set_font("DejaVuSans", size=8)
                pdf.cell(0, 4, txt=f"Tools: {exp['tools']}", ln=True)
                pdf.ln(2)

            if 'description' in exp and exp['description']:
                pdf.set_font("DejaVuSans", size=10)
                pdf.multi_cell(0, 6, txt=exp['description'])
                pdf.ln(2)

            if 'achievements' in exp and exp['achievements']:
                pdf.set_font("DejaVuSans", 'B', 10)
                pdf.cell(0, 6, txt="Key Achievements:", ln=True)
                pdf.set_font("DejaVuSans", size=10)
                for achievement in exp['achievements']:
                    pdf.cell(10, 6, txt="- ", ln=0)
                    pdf.multi_cell(0, 6, txt=achievement)
                pdf.ln(2)

            if 'projects' in exp and exp['projects']:
                pdf.set_font("DejaVuSans", 'B', 10)
                pdf.cell(0, 6, txt="Projects:", ln=True)
                pdf.set_font("DejaVuSans", size=10)
                for project in exp['projects']:
                    pdf.cell(10, 6, txt="- ", ln=0)
                    pdf.set_font("DejaVuSans", 'B', 10)
                    pdf.cell(30, 6, txt=f"{project.get('name', '')}: ", ln=0)
                    pdf.set_font("DejaVuSans", size=10)
                    pdf.multi_cell(0, 6, txt=project.get('description', ''))
                pdf.ln(2)

            pdf.ln(3)
            pdf.set_draw_color(200, 200, 200)
            pdf.cell(200, 0, ln=True)
            pdf.ln(3)

    # Education
    if 'education' in data and data['education']:
        pdf.set_font("DejaVuSans", 'B', 12)
        pdf.set_draw_color(200, 200, 200)
        pdf.set_fill_color(200, 200, 200)
        pdf.rect(x=10, y=pdf.get_y(), w=190, h=8, style='F')
        pdf.ln(1)
        pdf.cell(200, 6, txt="EDUCATION", ln=True, align='C')
        pdf.ln(1)
        pdf.set_font("DejaVuSans", size=10)

        for edu in data['education']:
            pdf.set_font("DejaVuSans", 'B', 10)
            pdf.cell(100, 6, txt=f"{edu.get('degree', '')}", ln=0)
            pdf.set_font("DejaVuSans", 'I', 10)
            pdf.cell(90, 6, txt=f"{edu.get('year', '')}", ln=True, align='R')

            pdf.set_font("DejaVuSans", size=10)
            pdf.cell(0, 6, txt=f"{edu.get('institution', '')}, {edu.get('location', '')}", ln=True)
            pdf.ln(2)

    # Languages
    if 'languages' in data and data['languages']:
        pdf.set_font("DejaVuSans", 'B', 12)
        pdf.set_draw_color(200, 200, 200)
        pdf.set_fill_color(200, 200, 200)
        pdf.rect(x=10, y=pdf.get_y(), w=190, h=8, style='F')
        pdf.ln(1)
        pdf.cell(200, 6, txt="LANGUAGES", ln=True, align='C')
        pdf.ln(1)
        pdf.set_font("DejaVuSans", size=10)
        pdf.cell(0, 6, txt=", ".join(data['languages']), ln=True)

    # Output file
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = f'static/{data["personalInfo"].get("name", "CV")}_classic_cv_{timestamp}.pdf'
    pdf.output(output_path)
    return output_path