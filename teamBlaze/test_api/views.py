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
        latitude, longitude = get_coordinate(source)
        response = client.get_products(latitude, longitude)
        try:
            products = response.json.get('products')[6]
        except:
            response = client.get_products(37.77, -122.41)
            products = response.json.get('products')[6]

        price_detail = products['price_details']

        cost_per_minute = price_detail['cost_per_minute']
        cost_per_distance = price_detail['cost_per_distance']
        # return str(cost_per_distance) + " " + str(cost_per_minute)\
        # return products

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

