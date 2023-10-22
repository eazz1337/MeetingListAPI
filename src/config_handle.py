import yaml
import os

class Config():

    def __init__(self,):
        
        config_dir_path = os.path.join("..", "config")
        
        formats_path = os.path.join(config_dir_path, "formats.yaml")
        districts_path = os.path.join(config_dir_path, "districts.yaml")
        fields_path = os.path.join(config_dir_path, "fields.yaml")
        config_path = os.path.join(config_dir_path, "config.yaml")

        self.formats = yaml.safe_load(open(formats_path))
        self.districts = yaml.safe_load(open(districts_path))
        self.fields = yaml.safe_load(open(fields_path))
        self.config = yaml.safe_load(open(config_path))

if __name__ == "__main__":

    config = Config()
    print(config.formats["csv"])