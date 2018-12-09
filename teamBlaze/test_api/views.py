from django.shortcuts import render, HttpResponse
from uber_rides.session import Session
from uber_rides.client import UberRidesClient
import requests
import googlemaps
# Create your views here.

#server token got from Lam's uber account


google_api_key = "AIzaSyCgJXyyet2ZbpKgg8d76VzMCxkEAwhiOy4"



def get_coordinate(address):
    # address = 'Plattsburgh, NY'
    # google_api_key = "AIzaSyCgJXyyet2ZbpKgg8d76VzMCxkEAwhiOy4"

    api_response = requests.get(
        'https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, google_api_key))
    api_response_dict = api_response.json()

    latitude = 0.0
    longitude = 0.0

    if api_response_dict['status'] == 'OK':
        latitude = api_response_dict['results'][0]['geometry']['location']['lat']
        longitude = api_response_dict['results'][0]['geometry']['location']['lng']

    return latitude, longitude

def get_time_distance(source, dest):
    # google_api_key = "AIzaSyCgJXyyet2ZbpKgg8d76VzMCxkEAwhiOy4"
    api_response = requests.get('https://maps.googleapis.com/maps/api/distancematrix/json?origins={0}&destinations={1}&key={2}'.format(source, dest, google_api_key))

    api_response_dict = api_response.json()

    time = 0.0
    distance = 0.0

    # if api_response_dict['status'] == 'OK':
    rows = api_response_dict['rows']
    elements = (rows[0])['elements'][0]
    #in meter
    distance = elements['distance']['value']
    #in seconds
    time = elements['duration']['value']

    # gmaps = googlemaps.Client(key="AIzaSyCgJXyyet2ZbpKgg8d76VzMCxkEAwhiOy4")
    # api_response_dict = gmaps.distance_matrix('Delhi', 'Mumbai')['rows'][0]['elements'][0]
    # distance = api_response_dict['distance']['value']
    # time = api_response_dict['duration']['value']


    return time, distance

def get_uber_price(source, destination):
    session = Session(server_token='V_89PqdPNV7zZO8_5G4C1tb3_-iVc3UXwd9h6JyU')
    client = UberRidesClient(session)
    begin_latitude, begin_longitude = get_coordinate(source)

    end_latitude, end_longitude = get_coordinate(destination)

    try:
        response = client.get_price_estimates(
            start_latitude=begin_latitude,
            start_longitude=begin_longitude,
            end_latitude=end_latitude,
            end_longitude=end_longitude,
            seat_count=2
        )

        estimate = response.json.get('prices')[0]['estimate']
        return estimate
    except:
        time, distance = get_time_distance(source, destination)
        time = time / 60

        #response = client.get_products(37.77, -122.41)
        response = client.get_products(get_coordinate(source))
        products = response.json.get('products')[6]

        price_detail = products['price_details']

        cost_per_minute = price_detail['cost_per_minute']
        cost_per_distance = price_detail['cost_per_distance']

        distance_unit = price_detail['distance_unit']
        if distance_unit == 'mile':
            distance = distance / 1609.344
        else:
            distance = distance / 1000

        service_fee = price_detail['service_fees'][0]
        booking_fee = service_fee['fee']

        uber_fee = int(cost_per_minute * time + cost_per_distance * distance + booking_fee)
        return uber_fee


def test_uber_api(request):
    # response = client.get_products(37.77, -122.41)
    # products = response.json.get('products')


    return HttpResponse('{0}'.format(get_uber_price()))

    # return HttpResponse(str(begin_latitude) + ' ' + str(begin_longitude))


    # {'destination_addresses': ['Haridwar, Uttarakhand, India'],
    #  'origin_addresses': ['Dehradun, Uttarakhand, India'],
    #  'rows':[{'elements':
    #               [{'distance': {'text': '56.3 km', 'value': 56288},
    #                 'duration': {'text': '1 hour 40 mins', 'value': 5993},
    #                 'status': 'OK'}]}],
    #  'status': 'OK'}

    # [{'upfront_fare_enabled': True, 'capacity': 4, 'product_id': '57c0ff4e-1493-4ef9-a4df-6b961525cf92',
    #   'price_details': {'service_fees': [{'fee': 2.45, 'name': 'Booking fee'}], 'cost_per_minute': 0.5,
    #                     'distance_unit': 'mile', 'minimum': 11.45, 'cost_per_distance': 2.81, 'base': 5.0,
    #                     'cancellation_fee': 5.0, 'currency_code': 'USD'},
    #   'image': 'https://d1a3f4spazzrp4.cloudfront.net/car-types/mono/mono-uberselect.png', 'cash_enabled': False,
    #   'shared': False, 'short_description': 'Select', 'display_name': 'Select', 'product_group': 'uberx',
    #   'description': 'A STEP ABOVE THE EVERY DAY'},
    #  {'upfront_fare_enabled': True, 'capacity': 6, 'product_id': '821415d8-3bd5-4e27-9604-194e4359a449',
    #   'price_details': {'service_fees': [{'fee': 2.45, 'name': 'Booking fee'}], 'cost_per_minute': 0.42,
    #                     'distance_unit': 'mile', 'minimum': 9.45, 'cost_per_distance': 1.72, 'base': 3.0,
    #                     'cancellation_fee': 5.0, 'currency_code': 'USD'},
    #   'image': 'https://d1a3f4spazzrp4.cloudfront.net/car-types/mono/mono-uberxl2.png', 'cash_enabled': False,
    #   'shared': False, 'short_description': 'UberXL', 'display_name': 'UberXL', 'product_group': 'uberxl',
    #   'description': 'LOW-COST RIDES FOR LARGE GROUPS'},
    #  {'upfront_fare_enabled': True, 'capacity': 4, 'product_id': 'd4abaae7-f4d6-4152-91cc-77523e8165a4',
    #   'price_details': {'service_fees': [], 'cost_per_minute': 0.65, 'distance_unit': 'mile', 'minimum': 15.0,
    #                     'cost_per_distance': 3.81, 'base': 8.0, 'cancellation_fee': 10.0, 'currency_code': 'USD'},
    #   'image': 'https://d1a3f4spazzrp4.cloudfront.net/car-types/mono/mono-black.png', 'cash_enabled': False,
    #   'shared': False, 'short_description': 'Black', 'display_name': 'Black', 'product_group': 'uberblack',
    #   'description': 'THE ORIGINAL UBER'},
    #  {'upfront_fare_enabled': True, 'capacity': 6, 'product_id': '8920cb5e-51a4-4fa4-acdf-dd86c5e18ae0',
    #   'price_details': {'service_fees': [], 'cost_per_minute': 0.9, 'distance_unit': 'mile', 'minimum': 25.0,
    #                     'cost_per_distance': 3.81, 'base': 15.0, 'cancellation_fee': 10.0, 'currency_code': 'USD'},
    #   'image': 'https://d1a3f4spazzrp4.cloudfront.net/car-types/mono/mono-suv.png', 'cash_enabled': False,
    #   'shared': False, 'short_description': 'Black SUV', 'display_name': 'Black SUV', 'product_group': 'suv',
    #   'description': 'ROOM FOR EVERYONE'},
    #  {'upfront_fare_enabled': True, 'capacity': 4, 'product_id': 'ff5ed8fe-6585-4803-be13-3ca541235de3',
    #   'price_details': {'service_fees': [{'fee': 2.2, 'name': 'Booking fee'}], 'cost_per_minute': 0.39,
    #                     'distance_unit': 'mile', 'minimum': 7.2, 'cost_per_distance': 0.91, 'base': 2.2,
    #                     'cancellation_fee': 5.0, 'currency_code': 'USD'},
    #   'image': 'https://d1a3f4spazzrp4.cloudfront.net/car-types/mono/mono-uberx.png', 'cash_enabled': False,
    #   'shared': False, 'short_description': 'Assist', 'display_name': 'Assist', 'product_group': 'uberx',
    #   'description': 'uberX with extra assistance'},
    #  {'upfront_fare_enabled': True, 'capacity': 4, 'product_id': '2832a1f5-cfc0-48bb-ab76-7ea7a62060e7',
    #   'price_details': {'service_fees': [{'fee': 2.2, 'name': 'Booking fee'}], 'cost_per_minute': 0.39,
    #                     'distance_unit': 'mile', 'minimum': 7.2, 'cost_per_distance': 0.91, 'base': 2.2,
    #                     'cancellation_fee': 5.0, 'currency_code': 'USD'},
    #   'image': 'https://d1a3f4spazzrp4.cloudfront.net/car-types/mono/mono-wheelchair.png', 'cash_enabled': False,
    #   'shared': False, 'short_description': 'WAV', 'display_name': 'WAV', 'product_group': 'uberx',
    #   'description': 'WHEELCHAIR ACCESSIBLE VEHICLES'},
    #  {'upfront_fare_enabled': True, 'capacity': 2, 'product_id': '26546650-e557-4a7b-86e7-6a3942445247',
    #   'price_details': {'service_fees': [{'fee': 2.2, 'name': 'Booking fee'}], 'cost_per_minute': 0.31,
    #                     'distance_unit': 'mile', 'minimum': 7.65, 'cost_per_distance': 0.81, 'base': 2.2,
    #                     'cancellation_fee': 5.0, 'currency_code': 'USD'},
    #   'image': 'https://d1a3f4spazzrp4.cloudfront.net/car-types/mono/mono-uberx.png', 'cash_enabled': False,
    #   'shared': True, 'short_description': 'Pool', 'display_name': 'UberPool', 'product_group': 'rideshare',
    #   'description': 'Shared rides, door to door'},
    #  {'upfront_fare_enabled': True, 'capacity': 4, 'product_id': 'a1111c8c-c720-46c3-8534-2fcdd730040d',
    #   'price_details': {'service_fees': [{'fee': 2.2, 'name': 'Booking fee'}], 'cost_per_minute': 0.39,
    #                     'distance_unit': 'mile', 'minimum': 7.2, 'cost_per_distance': 0.91, 'base': 2.2,
    #                     'cancellation_fee': 5.0, 'currency_code': 'USD'},
    #   'image': 'https://d1a3f4spazzrp4.cloudfront.net/car-types/mono/mono-uberx.png', 'cash_enabled': False,
    #   'shared': False, 'short_description': 'UberX', 'display_name': 'UberX', 'product_group': 'uberx',
    #   'description': 'THE LOW-COST UBER'},
    #  {'upfront_fare_enabled': False, 'capacity': 4, 'product_id': '3ab64887-4842-4c8e-9780-ccecd3a0391d',
    #   'price_details': {'service_fees': [], 'cost_per_minute': 0.55, 'distance_unit': 'mile', 'minimum': 3.5,
    #                     'cost_per_distance': 2.75, 'base': 3.5, 'cancellation_fee': 5.0, 'currency_code': 'USD'},
    #   'image': 'https://d1a3f4spazzrp4.cloudfront.net/car-types/mono/mono-taxi.png', 'cash_enabled': False,
    #   'shared': False, 'short_description': 'Taxi', 'display_name': 'Taxi', 'product_group': 'taxi',
    #   'description': 'TAXI WITHOUT THE HASSLE'}]




    # {'upfront_fare_enabled': True, 'capacity': 2, 'product_id': '26546650-e557-4a7b-86e7-6a3942445247',
    #  'price_details': {'service_fees': [{'fee': 2.2, 'name': 'Booking fee'}], 'cost_per_minute': 0.31,
    #                    'distance_unit': 'mile', 'minimum': 7.65, 'cost_per_distance': 0.81, 'base': 2.2,
    #                    'cancellation_fee': 5.0, 'currency_code': 'USD'},
    #  'image': 'https://d1a3f4spazzrp4.cloudfront.net/car-types/mono/mono-uberx.png', 'cash_enabled': False,
    #  'shared': True, 'short_description': 'Pool', 'display_name': 'UberPool', 'product_group': 'rideshare',
    #  'description': 'Shared rides, door to door'}
