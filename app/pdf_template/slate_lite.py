from datetime import datetime
from fpdf import FPDF
from typing import Dict, Any

def generate_cv(data: Dict[str, Any]) -> str:
    pdf = FPDF()
    pdf.add_page()

    # Set up fonts and base styling
    pdf.add_font('DejaVu', '', 'data/font/dejavu/ttf/DejaVuSans.ttf', uni=True)
    pdf.add_font('DejaVu', 'B', 'data/font/dejavu/ttf/DejaVuSans-Bold.ttf', uni=True)
    pdf.add_font('DejaVu', 'I', 'data/font/dejavu/ttf/DejaVuSans-Oblique.ttf', uni=True)

    pdf.set_text_color(0, 0, 0)
    pdf.set_draw_color(176, 176, 176)

    def safe_get(d, key, default="N/A"):
        value = d.get(key, default)
        if isinstance(value, str):
            return value.strip() if value.strip() else default
        return value if value else default

    # Header
    pdf.set_font('DejaVu', 'B', 20)
    pdf.cell(0, 10, safe_get(data['personal_info'], 'name'), ln=True, align='C')

    pdf.set_font('DejaVu', 'I', 12)
    pdf.cell(0, 8, safe_get(data['personal_info'], 'title'), ln=True, align='C')

    pdf.set_font('DejaVu', '', 10)
    contact_line = f" {safe_get(data['personal_info'], 'phone')}  |   {safe_get(data['personal_info'], 'email')}  |   {safe_get(data['personal_info'], 'location')}"
    pdf.cell(0, 8, contact_line, ln=True, align='C')
    visa = safe_get(data['personal_info'], 'nationality')
    if visa:
        pdf.set_font('DejaVu', 'I', 9)
        pdf.cell(0, 6, f"Nationality: {visa}", ln=True, align='C')

    pdf.ln(5)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(5)

    def section(title):
        pdf.set_font('DejaVu', 'B', 12)
        pdf.cell(0, 8, title.upper(), ln=True)
        pdf.set_font('DejaVu', '', 10)
        pdf.ln(1)

    # Profile
    profile_text = safe_get(data, 'profile')
    if profile_text:
        section("Profile")
        pdf.multi_cell(0, 6, profile_text)
        pdf.ln(4)

    # Professional Experience
    if data.get('professional_experience'):
        section("Professional Experience")
        for exp in data['professional_experience']:
            pdf.set_font('DejaVu', 'B', 10)
            pdf.cell(100, 6, safe_get(exp, 'company'))
            pdf.set_font('DejaVu', 'I', 10)
            pdf.cell(0, 6, safe_get(exp, 'duration'), ln=True, align='R')

            pdf.set_font('DejaVu', 'I', 10)
            pdf.cell(100, 6, safe_get(exp, 'role'))
            pdf.cell(0, 6, safe_get(exp, 'location'), ln=True, align='R')

            pdf.set_font('DejaVu', '', 10)
            description = exp.get('description')
            if isinstance(description, str) and description.strip():
                pdf.multi_cell(0, 6, description)

            for ach in exp.get('achievements', []):
                pdf.cell(5, 6, '-')
                pdf.multi_cell(0, 6, ach or "N/A")

            for proj in exp.get('projects', []):
                pdf.cell(5, 6, '-')
                pdf.set_font('DejaVu', 'B', 10)
                pdf.cell(30, 6, f"{safe_get(proj, 'name')}: ")
                pdf.set_font('DejaVu', '', 10)
                pdf.multi_cell(0, 6, safe_get(proj, 'description'))
            pdf.ln(3)

    # Skills
    skills = data.get('skills', {})
    if any(skills.values()):
        section("Skills")
        for category, items in skills.items():
            label = category.title() if category else "General"
            pdf.set_font('DejaVu', 'B', 10)
            pdf.cell(0, 6, f"{label}:", ln=True)
            pdf.set_font('DejaVu', '', 10)
            items_text = ", ".join([item if item else "N/A" for item in items]) or "N/A"
            pdf.multi_cell(0, 6, items_text)
        pdf.ln(3)

    # Education
    if data.get('education'):
        section("Education")
        for edu in data['education']:
            pdf.set_font('DejaVu', 'B', 10)
            pdf.cell(100, 6, safe_get(edu, 'degree'))
            pdf.set_font('DejaVu', 'I', 10)
            pdf.cell(0, 6, safe_get(edu, 'year'), ln=True, align='R')
            pdf.set_font('DejaVu', '', 10)
            pdf.cell(0, 6, f"{safe_get(edu, 'institution')}, {safe_get(edu, 'location')}", ln=True)
            pdf.ln(2)

    # Languages
    langs = data.get('languages')
    if langs:
        section("Languages")
        pdf.cell(0, 6, ", ".join([lang if lang else "N/A" for lang in langs]) or "N/A", ln=True)
        
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = f'static/{data["personal_info"].get("name", "CV")}_slate_lite_cv_{timestamp}.pdf'
    pdf.output(output_path)
    return output_path
