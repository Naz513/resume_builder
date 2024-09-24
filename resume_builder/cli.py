import argparse
from resume_builder.generator import read_yaml, render_template, generate_pdf

def main():
    parser = argparse.ArgumentParser(description='Generate a resume PDF from a YAML file.')
    parser.add_argument('yaml_file', help='Path to the YAML file containing resume data.')
    parser.add_argument('-t', '--template', default='default_template.html',
                        help='Template file to use for rendering.')
    parser.add_argument('-o', '--output', default='resume.pdf',
                        help='Output PDF file name.')
    args = parser.parse_args()

    data = read_yaml(args.yaml_file)
    html_content = render_template(data, args.template)
    generate_pdf(html_content, args.output)
    print(f'Resume generated: {args.output}')
