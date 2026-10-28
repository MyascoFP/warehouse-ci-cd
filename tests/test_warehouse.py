
import pytest

from src.warehouse import Warehouse


def test_add_material():
    warehouse = Warehouse()
    warehouse.add_material("Болты", 100)

    assert warehouse.get_balance("Болты") == 100


def test_write_off():
    warehouse = Warehouse()
    warehouse.add_material("Болты", 100)
    warehouse.write_off("Болты", 30)

    assert warehouse.get_balance("Болты") == 70


def test_insufficient_balance():
    warehouse = Warehouse()
    warehouse.add_material("Болты", 10)

    with pytest.raises(ValueError):
        warehouse.write_off("Болты", 20)


def test_total_quantity():
    warehouse = Warehouse()

    warehouse.add_material("Болты", 100)
    warehouse.add_material("Гайки", 50)
    warehouse.add_material("Шайбы", 30)

    assert warehouse.get_total_quantity() == 180


def test_total_quantity_empty():
    warehouse = Warehouse()

    assert warehouse.get_total_quantity() == 0


def test_total_quantity_after_write_off():
    warehouse = Warehouse()

    warehouse.add_material("Болты", 100)
    warehouse.add_material("Гайки", 50)

    warehouse.write_off("Болты", 30)

    assert warehouse.get_total_quantity() == 120
