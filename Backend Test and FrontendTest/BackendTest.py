import requests

def test_status_code(url):
    "HTTP status kodunu kontrol et."
    response = requests.get(url)
    assert response.status_code == 200, f"Status kodu 200 değil, aldığımız kod: {response.status_code}"

def test_response_structure(url):
    "Response yapısını kontrol et."
    response = requests.get(url).json()
    assert 'data' in response, "Response içinde 'data' anahtarı yok"
    for flight in response['data']:
        assert all(key in flight for key in ['id', 'from', 'to', 'date']), "Flight objesi beklenen anahtarları içermiyor"

def test_content_type_header(url):
    "Content-Type header'ını kontrol et."
    response = requests.get(url)
    assert response.headers['Content-Type'] == 'application/json', f"Content-Type header'ı 'application/json' değil, değeri: {response.headers['Content-Type']}"

api_url = "https://flights-api.buraky.workers.dev/"

try:
    test_status_code(api_url)
    print("Status kodu testi başarılı.")
except AssertionError as ae:
    print(f"Status kodu testinde hata: {ae}")

try:
    test_response_structure(api_url)
    print("Response yapısı testi başarılı.")
except AssertionError as ae:
    print(f"Response yapısı testinde hata: {ae}")

try:
    test_content_type_header(api_url)
    print("Content-Type header testi başarılı.")
except AssertionError as ae:
    print(f"Content-Type header testinde hata: {ae}")

