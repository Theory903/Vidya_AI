import warnings
warnings.filterwarnings('ignore')
from filetype import guess

def detect_document_type(document_path):
    
    guess_file = guess(document_path)
    file_type = ""
    image_types = ['jpg', 'jpeg', 'png', 'gif']
    
    if(guess_file.extension.lower() == "pdf"):
        file_type = "pdf"
        
    elif(guess_file.extension.lower() in image_types):
        file_type = "image"
        
    else:
        file_type = "unkown"
        
    return file_type
research_paper_path = "Model/Snap_ai/doc.pdf"
print(f"Research Paper Type: {detect_document_type(research_paper_path)}")
from langchain.document_loaders.image import UnstructuredImageLoader
from langchain.document_loaders import UnstructuredFileLoader

"""
YOU CAN UNCOMMENT THE CODE BELOW TO UNDERSTAND THE LOGIC OF THE FUNCTIONS
"""

def extract_text_from_pdf(pdf_file):
    
    loader = UnstructuredFileLoader(pdf_file)
    documents = loader.load()
    pdf_pages_content = '\n'.join(doc.page_content for doc in documents)
    
    return pdf_pages_content

def extract_file_content(file_path):
    
    file_type = detect_document_type(file_path)
    
    if(file_type == "pdf"):
        loader = UnstructuredFileLoader(file_path)
        
    elif(file_type == "image"):
        loader = UnstructuredImageLoader(file_path)
        
    documents = loader.load()
    documents_content = '\n'.join(doc.page_content for doc in documents)
    
    return documents_content

#research_paper_content = extract_text_from_pdf(research_paper_path)
#article_information_content = extract_text_from_image(article_information_path)


research_paper_content = extract_file_content(research_paper_path)
print(research_paper_content)