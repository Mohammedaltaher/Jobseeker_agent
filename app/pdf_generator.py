from fpdf import FPDF
from typing import Dict, Any

def generate_pdf(data: Dict[str, Any]) -> str:
    pdf = FPDF()
    pdf.add_page()

    # Add a Unicode font to support non-ASCII characters
    pdf.add_font('DejaVuSans', '', 'data/font/dejavu/ttf/DejaVuSans.ttf', uni=True)
    pdf.add_font('DejaVuSans', 'B', 'data/font/dejavu/ttf/DejaVuSans-Bold.ttf', uni=True)
    pdf.add_font('DejaVuSans', 'I', 'data/font/dejavu/ttf/DejaVuSans-Oblique.ttf', uni=True)
    pdf.add_font('DejaVuSans', 'BI', 'data/font/dejavu/ttf/DejaVuSans-BoldOblique.ttf', uni=True)
    pdf.set_font('DejaVuSans', '', 16)

    # Header with personal info
    if 'personal_info' in data and data['personal_info']:
        pdf.cell(200, 10, txt=data['personal_info'].get('name', ''), ln=True, align='C')
        pdf.set_font("DejaVuSans", 'I', 12)
        pdf.cell(200, 6, txt=data['personal_info'].get('title', ''), ln=True, align='C')
        pdf.set_font("DejaVuSans", size=10)
        pdf.cell(200, 6, txt=f"{data['personal_info'].get('location', '')} | {data['personal_info'].get('email', '')} | {data['personal_info'].get('phone', '')}", ln=True, align='C')

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

        print("Skills data:", data['skills'])  # Debugging line
        for category, skills in data['skills'].items():
            pdf.set_font("DejaVuSans", 'B', 10)
            print(f"Category: {category}, Skills: {skills}")  # Debugging line
            if skills and any(skills):
                category_width = pdf.get_string_width(f"{category.title()}:") + 2
                pdf.cell(category_width, 6, txt=f"{category.title()}:", ln=0)
                pdf.set_font("DejaVuSans", size=10)
                pdf.multi_cell(0, 6, txt=", ".join(skills))
                pdf.ln(2)

    # Professional Experience
    if 'professional_experience' in data and data['professional_experience']:
        pdf.set_font("DejaVuSans", 'B', 12)
        pdf.set_draw_color(200, 200, 200)
        pdf.set_fill_color(200, 200, 200)
        pdf.rect(x=10, y=pdf.get_y(), w=190, h=8, style='F')
        pdf.ln(1)
        pdf.cell(200, 6, txt="PROFESSIONAL EXPERIENCE", ln=True, align='C')
        pdf.ln(1)
        pdf.set_font("DejaVuSans", size=10)

        for exp in data['professional_experience']:
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
    output_path = 'static/sample_cv.pdf'
    pdf.output(output_path)
    return output_path