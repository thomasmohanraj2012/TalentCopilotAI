from pypdf import PdfReader


def extract_resume_text(uploaded_file):

    text = ""

    try:

        pdf_reader = PdfReader(uploaded_file)

        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"

    except Exception as e:

        return f"Error Reading Resume: {str(e)}"

    return text