import os.path

from jinja2 import Environment, FileSystemLoader
import py.path

def generate_static(tmpl_path, out_path):
    jinja_env = Environment(loader=FileSystemLoader(str(tmpl_path)))
    site_path = tmpl_path.join('site')

    if os.path.exists(str(out_path)):
        out_path.remove()
    out_path.mkdir()

    for subfile in reversed(list(site_path.visit())):
        out_file_path = out_path.join(subfile.relto(site_path))

        if os.path.isdir(str(subfile)):
            out_file_path.mkdir()
            continue

        tmpl_name = str(subfile.relto(tmpl_path))
        out_file_data = jinja_env.get_template(tmpl_name).render()

        with out_file_path.open('wb') as f:
            f.write(out_file_data.encode('utf-8'))

def main():
    import sys
    tmpl_path_str, out_path_str = sys.argv[1:]
    generate_static(py.path.local(tmpl_path_str),
                    py.path.local(out_path_str))

if __name__ == '__main__':
    main()
