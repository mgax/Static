from setuptools import setup, find_packages

setup(
    name="Static",
    packages=find_packages(),
    install_requires=['Jinja2', 'py'],
    entry_points={'console_scripts': ['static = static:main']},
)
