from api.controllers import Delivery
from django_mock_queries.query import MockSet, MockModel


def test_LotsOfItems():
    order = MockSet()
    order.add(MockModel(quantity=5))
    order.add(MockModel(quantity=5))
    order.add(MockModel(quantity=5))
    delivery_distance = 6

    cost = Delivery.calculate(order, delivery_distance)

    assert cost == 7.5


def test_MiddleOfTheRoadItems():
    order = MockSet()
    order.add(MockModel(quantity=2))
    order.add(MockModel(quantity=2))
    order.add(MockModel(quantity=2))
    delivery_distance = 4

    cost = Delivery.calculate(order, delivery_distance)

    assert cost == 5


def test_DefaultDeliveryFee():
    order = MockSet()
    order.add(MockModel(quantity=2))
    order.add(MockModel(quantity=2))
    delivery_distance = 3

    cost = Delivery.calculate(order, delivery_distance)

    assert cost == 3.50
