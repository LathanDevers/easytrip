import socketserver
from src.Server import *
from src.YamlParser import *
from functools import partial

path_to_params="params.yml"

if __name__=="__main__":
    yaml_parser=YamlParser()
    yaml_parser.read_yaml(path_to_params)
    port=yaml_parser.port
    paths=yaml_parser.paths

    Handler=partial(Server,paths)

    with socketserver.TCPServer(("", port), Handler) as httpd:
        print("serving at port", port)
        httpd.serve_forever()