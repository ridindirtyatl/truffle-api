from app import app

client = app.test_client()

def test_base_url():
  rsp = client.get('/')
  assert rsp.status == '200 OK'

def test_buses():
    rsp_bus = client.get('/v1/bus')
    assert rsp_bus.status == '200 OK'

def test_routes():
    rsp_routes = client.get('/v1/route')
    assert rsp_routes.status == '200 OK'
