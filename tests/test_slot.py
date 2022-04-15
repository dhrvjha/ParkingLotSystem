def test_base_slot_str(truck_slot_data, car_slot_data, *args, **kwargs):
    assert f"{truck_slot_data.id}" == str(truck_slot_data)
    assert f"{car_slot_data.id}" == str(car_slot_data)
