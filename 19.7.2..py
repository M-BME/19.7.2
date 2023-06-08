def set_pet_photo(self, pet_id, auth_key, photo_path):
    headers = {'auth_key': auth_key['key']}
    files = {'pet_photo': open(photo_path, 'rb')}
    res = requests.delete(self.base_url + 'api/pets/' + pet_id, headers=headers, files=files)
    status = res.status_code

    result = ""
    try:
        result = res.json()
    except:
        result = res.text
    return status, result


test_pet_friends.py:


def test_set_pet_photo():
    pf = PetFriends()
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    current_dir = os.path.dirname(os.path.abspath(__file__))
    photo_path = os.path.join(current_dir, 'images', 'squirrel.jpeg')

    status, result = pf.set_pet_photo(my_pets[0]['id'], auth_key, photo_path)
    assert status == 200
    assert 'success' in result