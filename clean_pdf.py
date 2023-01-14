import fitz
import click
from pathlib import Path


def add_rectangle(
    document: fitz.Document, position: tuple = None, exclude: tuple = None
) -> fitz.Document:
    """Overlay a rectangle on pages of a document.

    Args:
        document (fitz.Document): Document to overlay the rectangle on.
        position (tuple): Tuple of the form (x0, y0, x1, y1) where (x0, y0) is the
            top-left corner and (x1, y1) is the bottom-right corner of the rectangle.
        exclude (tuple): Tuple of page numbers to exclude from the overlay. Defaults to
            None. Assumes first page is 0.

    Returns:
        fitz.Document: Document with the rectangle overlayed.

    """
    position = (400, 50, 420, 600) if position is None else position
    rectangle = fitz.Rect(*position)

    color = fitz.utils.getColor("white")

    exclude = [] if exclude is None else exclude
    pages_to_edit = set(range(len(document))) - set(exclude)

    for n in pages_to_edit:
        page = document[n]
        page.draw_rect(rectangle, color=color, overlay=True, fill_opacity=1, fill=color)

    return document


@click.command()
@click.argument("path", type=click.Path(exists=True))
@click.option("--new-path", type=click.Path(), default=None)
@click.option("--position", type=click.Tuple([int]), default=None)
@click.option("--exclude", type=str, default=None)
@click.option("--overwrite", is_flag=True, default=False)
def update_pdf(
    path: Path,
    new_path: Path = None,
    position: tuple = None,
    exclude: str = None,
    overwrite: bool = False,
) -> None:
    
    exclude = [int(n) for n in exclude.split(",")] if exclude is not None else None

    document = fitz.open(path)
    document = add_rectangle(document, position=position, exclude=exclude)

    if overwrite or (new_path is None and click.confirm("Overwrite original pdf?")):
        document.saveIncr()
    elif new_path is None:
        new_path = click.prompt("Path to save new pdf to")
        document.save(new_path)
    else:
        document.save(new_path)


if __name__ == "__main__":
    update_pdf()
