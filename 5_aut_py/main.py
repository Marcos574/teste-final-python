from weather import weather_data_processing
from api import request, create_url

def main():

    request(create_url())
    weather_data_processing()

    return 0

if __name__ == '__main__':
    main()
