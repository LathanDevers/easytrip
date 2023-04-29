import yaml

class YamlParser:
    ip='localhost'
    port = 8080
    paths_html=[]
    paths_css=[]
    paths_js=[]
    paths_json=[]
    paths={}

    def __init__(self):
        pass

    def read_yaml(self,path):
        with open(path,'r') as stream:
            yf=yaml.safe_load(stream)
    
        self.paths_html=yf.get('paths').get('html')
        self.paths_html=list(map(lambda x:str(x)+".html",self.paths_html))

        self.paths_css=yf.get('paths').get('css')
        self.paths_css=list(map(lambda x:str(x)+".css",self.paths_css))

        self.paths_js=yf.get('paths').get('js')
        self.paths_js=list(map(lambda x:str(x)+".js",self.paths_js))

        self.paths_json=yf.get('paths').get('json')
        self.paths_json=list(map(lambda x:str(x)+".json",self.paths_json))

        self.ip=yf.get('ip')
        self.port=yf.get('port')

        self.paths.update({html:"html" for html in self.paths_html})
        self.paths.update({css:"css" for css in self.paths_css})
        self.paths.update({js:"js" for js in self.paths_js})
        self.paths.update({json:"json" for json in self.paths_json})
        