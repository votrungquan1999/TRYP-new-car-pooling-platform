from django.shortcuts import render, HttpResponse
from uber_rides.session import Session
from uber_rides.client import UberRidesClient
import requests
import googlemaps
# Create your views here.

#server token got from Lam's uber account
session = Session(server_token='V_89PqdPNV7zZO8_5G4C1tb3_-iVc3UXwd9h6JyU')
client = UberRidesClient(session)

google_api_key = "AIzaSyCgJXyyet2ZbpKgg8d76VzMCxkEAwhiOy4"

gmaps = googlemaps.Client(key="AIzaSyA1PVvqJ4h3Ihl9UM2fOnXzwXfIMHuZTNQ")

def test_google_api(address):
    # address = 'Plattsburgh, NY'
    google_api_key = "AIzaSyCgJXyyet2ZbpKgg8d76VzMCxkEAwhiOy4"

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
    google_api_key = "AIzaSyCgJXyyet2ZbpKgg8d76VzMCxkEAwhiOy4"
    api_response = requests.get('https://maps.googleapis.com/maps/api/distancematrix/json?origins={0}&destinations={1}&key={2}'.format(source, dest, google_api_key))

    api_response_dict = api_response.json()

    time = 0.0
    distance = 0.0

    # if api_response_dict['status'] == 'OK':
    # rows = api_response_dict['rows']
    # elements = (rows[0])['elements']
    #
    # distance = elements['distance']['value']
    # time = elements['duration']['value']
    api_response_dict = gmaps.distance_matrix('Delhi', 'Mumbai')['rows'][0]['elements'][0]
    distance = api_response_dict['distance']['value']
    time = api_response_dict['duration']['value']
    return time, distance


def test_uber_api(request):
    # response = client.get_products(37.77, -122.41)
    # products = response.json.get('products')
    begin_latitude, begin_longitude = test_google_api('plattsburgh, NY')

    end_latitude, end_longitude = test_google_api('Burlington, Vermont')

    # try:
    # response = client.get_price_estimates(
    #     start_latitude = begin_latitude,
    #     start_longitude = begin_longitude,
    #     end_latitude = end_latitude,
    #     end_longitude = end_longitude,
    #     seat_count=2
    # )

    # estimate = response.json.get('prices')[0]['estimate']
    return HttpResponse(str(begin_latitude) + ' ' + str(begin_longitude))
    # except:
    #     time, distance = get_time_distance('plattsburgh, NY', 'new york city, NY')
    #     return HttpResponse('time:{0} distance{1}'.format(time, distance))





        # {'destination_addresses': ['Haridwar, Uttarakhand, India'],
        #  'origin_addresses': ['Dehradun, Uttarakhand, India'],
        #  'rows':[{'elements':
        #               [{'distance': {'text': '56.3 km', 'value': 56288},
        #                 'duration': {'text': '1 hour 40 mins', 'value': 5993},
        #                 'status': 'OK'}]}],
        #  'status': 'OK'}
