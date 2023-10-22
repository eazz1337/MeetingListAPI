from request_handle import RequestHandle
from config_handle import Config

def main():
    config = Config()
    request_handle = RequestHandle(config)
    print(type(config.config))

if __name__ == "__main__":
    main()
