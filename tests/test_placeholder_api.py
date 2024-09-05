import pytest


def test_get_all_posts(api_client_placeholder):
    response = api_client_placeholder.get_all_posts()
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 100  # Проверяем, что в ответе 100 постов


def test_get_post_by_id(api_client_placeholder):
    response = api_client_placeholder.get_post_by_id(1)
    assert response.status_code == 200
    assert 'userId' in response.json()
    assert 'id' in response.json()
    assert 'title' in response.json()
    assert 'body' in response.json()


@pytest.mark.parametrize("post_id", [1, 5, 10])
def test_get_post_by_different_ids(api_client_placeholder, post_id):
    response = api_client_placeholder.get_post_by_id(post_id)
    assert response.status_code == 200
    assert 'userId' in response.json()
    assert 'id' in response.json()
    assert 'title' in response.json()
    assert 'body' in response.json()


@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_get_comments_by_post_id(api_client_placeholder, post_id):
    response = api_client_placeholder.get_comments_by_post_id(post_id)
    assert response.status_code == 200
    comments = response.json()
    assert isinstance(comments, list)
    for comment in comments:
        assert comment['postId'] == post_id
        assert 'id' in comment
        assert 'name' in comment
        assert 'email' in comment
        assert 'body' in comment


def test_create_new_post(api_client_placeholder):
    new_post = {
        "userId": 1,
        "title": "Test Post",
        "body": "This is a test post."
    }
    response = api_client_placeholder.create_post(new_post)
    assert response.status_code == 201
    response_json = response.json()
    assert response_json['userId'] == 1
    assert response_json['title'] == "Test Post"
    assert response_json['body'] == "This is a test post."
    assert 'id' in response_json