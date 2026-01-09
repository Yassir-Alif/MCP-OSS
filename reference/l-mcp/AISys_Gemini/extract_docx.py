
import docx
import sys



def extract_docx_text(path):
    try:
        doc = docx.Document(path)
        full_text = []
        
        # Access the document body elements directly to preserve order
        # This requires accessing the underlying XML structure via `doc.element.body`
        
        for element in doc.element.body:
            if element.tag.endswith('p'):  # Paragraph
                para_text = element.text.strip()
                if para_text:
                    full_text.append(para_text)
            elif element.tag.endswith('tbl'):  # Table
                # We need to find the matching table object in doc.tables to use the high-level API
                # or just parse the XML. Parsing XML is safer for raw text.
                # Let's try to simulate table structure
                table_text = []
                for row in element.findall('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tr'):
                    row_cells = []
                    for cell in row.findall('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tc'):
                        # detailed text extraction from cell
                        cell_texts = [node.text for node in cell.findall('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if node.text]
                        row_cells.append(''.join(cell_texts).strip())
                    table_text.append(" | ".join(row_cells))
                full_text.append("\n[TABLE START]\n" + "\n".join(table_text) + "\n[TABLE END]")
                
        return '\n'.join(full_text)
    except Exception as e:
        print(f"Error reading docx: {e}")
        import traceback
        traceback.print_exc()
        return None




if __name__ == "__main__":
    path = "MCP-OSS_Architektur-Modell_v1.0.docx"
    text = extract_docx_text(path)
    if text:
        with open("output.txt", "w", encoding="utf-8") as f:
            f.write(text)
        print("Written to output.txt")
    else:
        sys.exit(1)

