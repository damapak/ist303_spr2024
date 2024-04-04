from observer import Kens
import pytest

@pytest.fixture()
def ken_instances():
  k1 = Kens(fname="Ken",lname="Masters",posts=[23,45,66])
  k2 = Kens(fname="Ken",lname="Just Ken",posts=[12,13])
  k3 = Kens(fname="Ken",lname="Obi")
  k4 = Kens(fname="Ken",lname="YouDigIt")
  return k1,k2,k3,k4

# test adding observers
def test_observer(ken_instances: tuple):
  assert len(ken_instances[0].observers) == 0 # start with 0 observers
  ken_instances[0].add_observer(ken_instances[1])
  ken_instances[0].add_observer(ken_instances[2])
  assert len(ken_instances[0].observers) == 2, f'Should have had exactly 2 observers, had {len(ken_instances[0].observers)}'

# test removing an observer
def test_observer_rmv(ken_instances: tuple):
  assert len(ken_instances[0].observers) == 0 # start with 0 observers
  ken_instances[0].add_observer(ken_instances[1])
  #ken_instances[0].remove_observer(ken_instances[1])
  assert len(ken_instances[0].observers) == 0, f'Should have had no observers, had {len(ken_instances[0].observers)}'

# test the notify_observers method to make sure it adds an event to the observers .event attribute
def test_notify(ken_instances: tuple):
  ken_instances[0].add_observer(ken_instances[1])
  assert len(ken_instances[1].events) == 0 # start with 0 subscriber events
  ken_instances[0].notify_observers("This is an Important Event!")
  assert len(ken_instances[1].events) == 1, f'Should have received one event, had {len(ken_instances[1].events)}'