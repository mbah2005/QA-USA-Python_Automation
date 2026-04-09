import data
import helpers
from data import URBAN_ROUTES_URL
from helpers import is_url_reachable


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        if is_url_reachable(URBAN_ROUTES_URL):
            print('Connected to Urban Routes Server')
        else:
            print('Cannot connect to Urban Routes. Check the server is on and still running')

    def test_set_route(self):
        # Add in S8
        print('function created for set route')
        pass

    def test_select_plan(self):
        # Add in S8
        print('function created for set route')
        pass

    def test_fill_phone_number(self):
        # Add in S8
        print('function created for set route')
        pass

    def test_fill_card(self):
        # Add in S8
        print('function created for set route')
        pass

    def test_comment_for_driver(self):
        # Add in S8
        print('function created for set route')
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # Add in S8
        print('function created for set route')
        pass

    def test_order_2_ice_creams(self):
        number_of_ice_creams = 2
        for i in range(number_of_ice_creams):
            # Add in S8
            print('function created for set route')
        pass

    def test_car_search_model_appears(self):
        # Add in S8
        print('function created for set route')
        pass
