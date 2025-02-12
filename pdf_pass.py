import PyPDF2


pdf_path = ""
password = ""  

with open(pdf_path, 'rb') as file:
    pdf_reader = PyPDF2.PdfReader(file)
    
  
    if pdf_reader.is_encrypted:
      
        if pdf_reader.decrypt(password):
            print(f"PDF decrypted successfully! The document has {len(pdf_reader.pages)} pages.")
            
            # Example: Extract text from the first page
            page = pdf_reader.pages[0]
            text = page.extract_text()
            print(text)
        else:
            print("Failed to decrypt PDF with the provided password.")
    else:
        print("PDF is not encrypted.")
