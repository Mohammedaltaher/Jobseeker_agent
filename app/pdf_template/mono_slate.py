from fpdf import FPDF
from typing import Dict, Any

def generate_cv(data: Dict[str, Any]) -> str:
    pdf = FPDF()
    pdf.add_page()

    # Fonts and colors
    pdf.add_font('DejaVuSans', '', 'data/font/dejavu/ttf/DejaVuSans.ttf', uni=True)
    pdf.add_font('DejaVuSans', 'B', 'data/font/dejavu/ttf/DejaVuSans-Bold.ttf', uni=True)
    pdf.add_font('DejaVuSans', 'I', 'data/font/dejavu/ttf/DejaVuSans-Oblique.ttf', uni=True)
    pdf.set_text_color(0, 0, 0)
    pdf.set_draw_color(180, 180, 180)

    # Header
    pdf.set_font('DejaVuSans', 'B', 20)
    pdf.cell(0, 10, txt=data['personal_info'].get('name', ''), ln=True, align='C')
    pdf.set_font('DejaVuSans', 'I', 12)
    pdf.cell(0, 8, txt=data['personal_info'].get('title', ''), ln=True, align='C')

    pdf.set_font('DejaVuSans', '', 10)
    contact = f"{data['personal_info'].get('location', '')} | {data['personal_info'].get('email', '')} | {data['personal_info'].get('phone', '')}"
    pdf.cell(0, 8, txt=contact, ln=True, align='C')

    pdf.ln(5)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(5)

    # Profile
    if data.get('profile'):
        pdf.set_font('DejaVuSans', 'B', 12)
        pdf.cell(0, 8, 'Professional Summary', ln=True)
        pdf.set_font('DejaVuSans', '', 10)
        pdf.multi_cell(0, 6, data['profile'])
        pdf.ln(5)

    # Skills
    if data.get('skills'):
        pdf.set_font('DejaVuSans', 'B', 12)
        pdf.cell(0, 8, 'Skills', ln=True)
        pdf.set_font('DejaVuSans', '', 10)
        for category, items in data['skills'].items():
            pdf.set_font('DejaVuSans', 'B', 10)
            pdf.cell(30, 6, f"{category.title()}:", ln=0)
            pdf.set_font('DejaVuSans', '', 10)
            pdf.multi_cell(0, 6, ", ".join(items))
        pdf.ln(5)

    # Experience
    if data.get('professional_experience'):
        pdf.set_font('DejaVuSans', 'B', 12)
        pdf.cell(0, 8, 'Professional Experience', ln=True)
        pdf.ln(2)
        for job in data['professional_experience']:
            pdf.set_font('DejaVuSans', 'B', 10)
            pdf.cell(100, 6, job.get('company', ''))
            pdf.set_font('DejaVuSans', 'I', 10)
            pdf.cell(0, 6, job.get('duration', ''), ln=True, align='R')
            pdf.set_font('DejaVuSans', 'I', 10)
            pdf.cell(100, 6, job.get('role', ''))
            pdf.cell(0, 6, job.get('location', ''), ln=True, align='R')

            if job.get('tools'):
                pdf.set_font('DejaVuSans', '', 9)
                pdf.cell(0, 5, f"Tools: {job['tools']}", ln=True)

            if job.get('description'):
                pdf.set_font('DejaVuSans', '', 10)
                pdf.multi_cell(0, 5, job['description'])

            if job.get('achievements'):
                pdf.set_font('DejaVuSans', 'B', 10)
                pdf.cell(0, 6, 'Key Achievements:', ln=True)
                pdf.set_font('DejaVuSans', '', 10)
                for ach in job['achievements']:
                    pdf.cell(5, 6, '-')
                    pdf.multi_cell(0, 6, ach)

            if job.get('projects'):
                pdf.set_font('DejaVuSans', 'B', 10)
                pdf.cell(0, 6, 'Projects:', ln=True)
                pdf.set_font('DejaVuSans', '', 10)
                for proj in job['projects']:
                    pdf.cell(5, 6, '-')
                    pdf.set_font('DejaVuSans', 'B', 10)
                    pdf.cell(30, 6, proj.get('name', '') + ':')
                    pdf.set_font('DejaVuSans', '', 10)
                    pdf.multi_cell(0, 6, proj.get('description', ''))
            pdf.ln(4)

    # Education
    if data.get('education'):
        pdf.set_font('DejaVuSans', 'B', 12)
        pdf.cell(0, 8, 'Education', ln=True)
        pdf.ln(2)
        for edu in data['education']:
            pdf.set_font('DejaVuSans', 'B', 10)
            pdf.cell(100, 6, edu.get('degree', ''))
            pdf.set_font('DejaVuSans', 'I', 10)
            pdf.cell(0, 6, edu.get('year', ''), ln=True, align='R')
            pdf.set_font('DejaVuSans', '', 10)
            pdf.cell(0, 6, f"{edu.get('institution', '')}, {edu.get('location', '')}", ln=True)
        pdf.ln(4)

    # Languages
    if data.get('languages'):
        pdf.set_font('DejaVuSans', 'B', 12)
        pdf.cell(0, 8, 'Languages', ln=True)
        pdf.set_font('DejaVuSans', '', 10)
        pdf.cell(0, 6, ", ".join(data['languages']), ln=True)

    # Output
    
    output_path = f'static/{data["personal_info"].get("name", "CV")}_mono_slate_cv.pdf'
    pdf.output(output_path)
    return output_path
