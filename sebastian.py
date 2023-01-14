import fitz
from pathlib import Path


def update_pdf(path: Path, new_path: Path = None) -> None:

    doc = fitz.open(path)
    rect = fitz.Rect(50, 100, 300, 400)
    text = """This text will only appear in the rectangle. Depending on width, new lines are generated as required.\n<- This forced line break will also appear.\tNow a very long word: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.\nIt will be broken into pieces."""
    
    for n in range(len(doc)):
        page = doc[n]
        page.insert_textbox(rect, text, fontsize = 12,
                           fontname = "Times-Roman",
                           fontfile = None,
                           align = 0)
    
    if new_path is None:
        doc.saveIncr()
    else:
        doc.save(new_path)


if __name__ == "__main__":
    path = Path("Hazell2022_QJE.pdf")
    update_pdf(path)