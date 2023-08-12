import pytest
from rest_framework import status
from django.contrib.auth import get_user_model

@pytest.fixture
def create_category(api_client):
    def do_create_category(obj):
        return api_client.post('/poll/categories/', obj)
    return do_create_category


@pytest.mark.django_db
class TestCategoryModel:
    def test_if_category_is_created_returns_201(self, create_category):
        response = create_category({ 'title': 'a' })

        assert response.status_code == status.HTTP_201_CREATED

    def test_duplicate_category_returns_400(self, create_category):
        response = create_category({ 'title': 'a'})

        assert response.status_code == status.HTTP_201_CREATED

        respons = create_category({ 'title': 'a'})

        assert respons.status_code == status.HTTP_400_BAD_REQUEST

    # def test_attempt_to_delete_category_with_question_returns_409(self, api_client):
    #     pass

        
        

