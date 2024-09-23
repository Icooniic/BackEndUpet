from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Test Get Medical History By Id
def test_get_medical_history():
    # Assuming you have a valid medical_history_id
    medical_history_id = 1
    
    # Construct the URL
    url = f"/api/v1/medicalhistories/{medical_history_id}"

    # Make a request to your FastAPI endpoint
    response = client.get(url)

    
    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    # Assert that the id in the response is the same as the medical_history_id
    assert response.json().get("id") == medical_history_id

# Test Get Medical History By Id Not Found
def test_get_medical_history_not_found():
    # Assuming you have an invalid medical_history_id
    medical_history_id = 9999  # Use an ID that does not exist
    
    # Construct the URL
    url = f"/api/v1/medicalhistories/{medical_history_id}"

    # Make a request to your FastAPI endpoint
    response = client.get(url)

    # Assert that the response status code is 404 (Not Found)
    assert response.status_code == 404


#Test Get User By Id
def test_get_user_by_id():
    # Assuming you have a valid user_id
    user_id = 1
    
    # Construct the URL
    url = f"/api/v1/users/{user_id}"

    # Make a request to your FastAPI endpoint
    response = client.get(url)

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    # Assert that the id in the response is the same as the user_id
    assert response.json().get("id") == user_id

#Test Get Medical History By Pet Id
def test_get_medical_history_by_pet_id():
    # Assuming you have a valid pet_id
    pet_id = 1
    
    # Construct the URL
    url = f"/api/v1/medicalhistories/pet/{pet_id}"

    # Make a request to your FastAPI endpoint
    response = client.get(url)

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    # Assert that the petId in the response is the same as the pet_id
    assert response.json().get("petId") == pet_id


#Test Create Pet By Owner Id
def test_create_pet_by_owner_id():
    # Assuming you have a valid pet_owner_id
    pet_owner_id = 1
    
    # Construct the URL
    url = f"/api/v1/pets/{pet_owner_id}"

    # Create a sample payload
    payload = {
        "name": "Fluffy",
        "species": "Cat",
        "birthdate": "2024-09-23",
        "image_url": "string",
        "gender":"Male",
        "breed": "Siamese",
        "weight": 5.0
    }

    # Make a request to your FastAPI endpoint
    response = client.post(url, json=payload)

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 201

#Test Get Veterinarian By Id
def test_get_veterinarian_by_id():
    # Assuming you have a valid veterinarian_id
    veterinarian_id = 1
    
    # Construct the URL
    url = f"/api/v1/veterinarians/{veterinarian_id}"

    # Make a request to your FastAPI endpoint
    response = client.get(url)

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    # Assert that the id in the response is the same as the veterinarian_id
    assert response.json().get("id") == veterinarian_id

#Test Get Pet By Id
def test_get_pet_by_id():
    # Assuming you have a valid pet_id
    pet_id = 1
    
    # Construct the URL
    url = f"/api/v1/pets/pet/{pet_id}"

    # Make a request to your FastAPI endpoint
    response = client.get(url)

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    # Assert that the id in the response is the same as the pet_id
    assert response.json().get("id") == pet_id

    