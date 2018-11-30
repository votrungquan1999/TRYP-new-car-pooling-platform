from django.shortcuts import render
from uber_rides.session import Session
from uber_rides.client import UberRidesClient
# Create your views here.

session = Session(server_token='V_89PqdPNV7zZO8_5G4C1tb3_-iVc3UXwd9h6JyU')
client = UberRidesClient(session)

def test_api(request):
    response = client.get_products(37.77, -122.41)
    products = response.json.get('products')

    response = client.get_price_estimates(
        start_latitude=37.770,
        start_longitude=-122.411,
        end_latitude=37.791,
        end_longitude=-122.405,
        seat_count=2
    )

    estimate = response.json.get('prices')
    return render(request, 'test_api/test_api.html', {'price' : estimate})