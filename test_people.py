from people import People


def test_people():
    people = People()
    print(people.fetch_all())
    print(people.fetch_by_code("B"))

    person_code = "S"
    person = People(person_code)
    name = person.get_name()
    print(f"Person '{person_code}' is '{name}'")
    print(f"Person '{person_code}' was born '{person.get_date_of_birth()}'")
    assert people.get_how_many() == 6


test_people()
