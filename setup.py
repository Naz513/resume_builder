from setuptools import setup, find_packages

setup(
    name='resume_builder',
    version='0.1.0',
    author='Mohd Saquib',
    author_email='nsaquib96@gmail.com',
    description='A tool to generate resumes from YAML files.',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'PyYAML',
        'Jinja2',
        'WeasyPrint',
    ],
    entry_points={
        'console_scripts': [
            'resume-builder=resume_builder.cli:main',
        ],
    },
)
