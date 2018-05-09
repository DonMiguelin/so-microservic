import pytest
from op_stats.stats import Stats
from op_stats.app import app

#def test_get_cpu_percent():
#  assert 1==1


@pytest.fixture
def stats_client():
  return app.test_client()

def test_get_cpu_percent(mocker, stats_client):
  mocker.patch.object(Stats, 'get_cpu_percent', return_value=100)
  response = stats_client.get('/v1/stats/cpu')
  assert response.data.decode('utf-8')== '{"cpu_percent": 100}'
  assert response.status_code==200

def test_dummy():
  assert 1==1
