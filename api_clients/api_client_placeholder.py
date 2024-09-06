import requests


class PlaceholderApiClient:

    def __init__(self, base_url="https://jsonplaceholder.typicode.com", status_code=200):
        self.session = requests.Session()
        self.base_url = base_url
        self.status_code = status_code

    def get_all_posts(self):
        response = self.session.get(url=f"{self.base_url}/posts")
        return response

    def get_post_by_id(self, post_id):
        response = self.session.get(url=f"{self.base_url}/posts/{post_id}")
        return response

    def get_comments_by_post_id(self, post_id):
        response = self.session.get(url=f"{self.base_url}/posts/{post_id}/comments")
        return response

    def create_post(self, post_data):
        response = self.session.post(url=f"{self.base_url}/posts", json=post_data)
        return response

    def update_post(self, post_id, post_data):
        response = self.session.put(url=f"{self.base_url}/posts/{post_id}", json=post_data)
        return response

    def delete_post(self, post_id):
        response = self.session.delete(url=f"{self.base_url}/posts/{post_id}")
        return response
