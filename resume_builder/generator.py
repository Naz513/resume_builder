import yaml  # For reading YAML files
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML, CSS
import os
import tempfile
import shutil

def read_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data

def render_template(data, template_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    template_dir = os.path.join(current_dir, 'templates')
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template(template_name)
    output = template.render(data)
    return output

def generate_pdf(html_content, output_path):
    # Create a temporary directory to store the HTML and CSS files
    with tempfile.TemporaryDirectory() as temp_dir:
        # Write the HTML content to a file
        html_file = os.path.join(temp_dir, 'resume.html')
        with open(html_file, 'w') as file:
            file.write(html_content)
        
        # Copy the CSS file to the temporary directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        css_source = os.path.join(current_dir, 'assets', 'styles.css')
        css_dest = os.path.join(temp_dir, 'styles.css')
        shutil.copy(css_source, css_dest)
        
        # Generate the PDF from the HTML file
        HTML(html_file).write_pdf(output_path)
