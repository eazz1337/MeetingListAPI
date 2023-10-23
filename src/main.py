from request_handle import RequestHandle
from config_handle import Config

def main():
    config = Config()
    request_handle = RequestHandle(config)
    cfg = config.config
    
    format = config.formats[ cfg["format"]]
    district = config.districts[ cfg["district"]]
    fields = [config.fields[field] for field in cfg["fields"]]

    request_handle.make_url(cfg["base_url"], format, district, fields)
    print(request_handle.url)

if __name__ == "__main__":
    main()
