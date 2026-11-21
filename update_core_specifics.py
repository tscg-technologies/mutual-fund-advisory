"""
Update Core Pages with Specific Dedicated Image Placeholders
"""
from templates import render_html_page, make_placeholder

def update_core():
    # Load and update
    from make_core_pages import build_core_pages
    build_core_pages()

if __name__ == "__main__":
    update_core()
