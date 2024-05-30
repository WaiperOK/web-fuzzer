import random
import string
import requests


def generate_random_string(length=10):
    """Генерация случайной строки заданной длины."""
    letters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(letters) for i in range(length))


def fuzz(url, num_requests=100, param_name="input"):
    """Отправка случайных данных на указанный URL."""
    for i in range(num_requests):
        random_data = generate_random_string()
        response = requests.post(url, data={param_name: random_data})
        print(f"Request {i + 1}: Sent {random_data} - Status Code: {response.status_code}")


if __name__ == "__main__":
    target_url = input("Enter the target URL: ")
    num_requests = int(input("Enter the number of requests to send: "))
    param_name = input("Enter the parameter name to fuzz: ")

    fuzz(target_url, num_requests, param_name)
