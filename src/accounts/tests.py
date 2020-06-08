from django.test import TestCase, Client
from django.urls import reverse,resolve 
from django.contrib.auth import get_user_model
User = get_user_model()

class TestLoginView(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('accounts:login')
        obj1 = User.objects.create_user(
            username='test',
            email='abc@gmail.com',
            first_name='t',
            last_name='u',
            password='password'
        )
    def test_login_url(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'accounts/login.html')

    def test_redirection_on_successful_login(self):
        response = self.client.post(self.login_url,{'username':'test','password':'password'},format='text/html')
        self.assertEqual(response.status_code, 302)

    def test_redirection_on_unsuccessful_login(self):
        response = self.client.post(self.login_url,{'username':'test123','password':'password'},format='text/html')
        self.assertEqual(response.status_code, 401)

    def test_redirection_with_no_password(self):
        response = self.client.post(self.login_url,{'username':'test123','password':''},format='text/html')
        self.assertEqual(response.status_code, 401)

    def test_redirection_with_no_username(self):
        response = self.client.post(self.login_url,{'username':'','password':'test123'},format='text/html')
        self.assertEqual(response.status_code, 401)

class TestSignUpView(TestCase):
    def setUp(self):
        self.client = Client()
        self.signup_url = reverse('accounts:signup')
        obj2 = User.objects.create_user(
            username='testuserweb',
            email='testuserweb@gmail.com',
            first_name='t',
            last_name='u',
            password='qwerty@12345'
        )
    
    def test_signup_url(self):
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'accounts/signup.html')

    def test_signup_on_successful_signup(self):
        response = self.client.post(self.signup_url,{'username':'sachin','first_name':'sac','last_name':'hin','email':'sp@gmail.com','password1':'qwerty@12345', 'password2':'qwerty@12345'},format='text/html')
        self.assertEqual(response.status_code, 302)
    
    def test_signup_on_occupied_username(self):
        response = self.client.post(self.signup_url,{'username':'testuserweb','first_name':'try','last_name':'tr','email':'iot@gmail.com','password1':'qwerty@12345', 'password2':'qwerty@12345'},format='text/html')
        self.assertEqual(response.status_code,401)
        print(response.status_code)

    def test_signup_on_empty_username(self):
        response = self.client.post(self.signup_url,{'username':'','first_name':'try','last_name':'tr','email':'iot@gmail.com','password1':'qwerty@12345', 'password2':'qwerty@12345'},format='text/html')
        self.assertEqual(response.status_code,401)
    
    def test_signup_on_empty_first_name(self):
        response = self.client.post(self.signup_url,{'username':'oo','first_name':'','last_name':'tr','email':'iot@gmail.com','password1':'qwerty@12345', 'password2':'qwerty@12345'},format='text/html')
        self.assertEqual(response.status_code,401)

    def test_signup_on_invalid_first_name(self):
        response = self.client.post(self.signup_url,{'username':'oo','first_name':'$@#$#%$^','last_name':'tr','email':'iot@gmail.com','password1':'qwerty@12345', 'password2':'qwerty@12345'},format='text/html')
        self.assertEqual(response.status_code,401)

    def test_signup_on_empty_last_name(self):
        response = self.client.post(self.signup_url,{'username':'oo','first_name':'m','last_name':'','email':'iot@gmail.com','password1':'qwerty@12345', 'password2':'qwerty@12345'},format='text/html')
        self.assertEqual(response.status_code,401)

    def test_signup_on_invalid_last_name(self):
        response = self.client.post(self.signup_url,{'username':'oo','first_name':'m','last_name':'t#$%#@@^$&%','email':'iot@gmail.com','password1':'qwerty@12345', 'password2':'qwerty@12345'},format='text/html')
        self.assertEqual(response.status_code,401)

    def test_signup_on_empty_email(self):
        response = self.client.post(self.signup_url,{'username':'oo','first_name':'m','last_name':'mm','email':'','password1':'qwerty@12345', 'password2':'qwerty@12345'},format='text/html')
        self.assertEqual(response.status_code,401)

    def test_signup_on_invalid_email(self):
        response = self.client.post(self.signup_url,{'username':'oo','first_name':'m','last_name':'t#$%#@@^$&%','email':'iot#@gmail.com.com.@@gmail.com','password1':'qwerty@12345', 'password2':'qwerty@12345'},format='text/html')
        self.assertEqual(response.status_code,401)

    def test_signup_on_empty_password1(self):
        response = self.client.post(self.signup_url,{'username':'oo','first_name':'m','last_name':'mm','email':'iot@gmail.com','password1':'', 'password2':'qwerty@12345'},format='text/html')
        self.assertEqual(response.status_code,401)

    def test_signup_on_empty_password2(self):
        response = self.client.post(self.signup_url,{'username':'oo','first_name':'m','last_name':'mm','email':'iot@gmail.com','password1':'qwerty@12345', 'password2':''},format='text/html')
        self.assertEqual(response.status_code,401)

    def test_signup_on_different_password(self):
        response = self.client.post(self.signup_url,{'username':'oo','first_name':'m','last_name':'t#$%#@@^$&%','email':'iot@gmail.com','password1':'qwerty@12345', 'password2':'password1234'},format='text/html')
        self.assertEqual(response.status_code,401)