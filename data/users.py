import dataclasses
import os


@dataclasses.dataclass
class User:
    login: str
    email: str
    password: str
    date_of_birth: [str]
    first_name: str
    last_name: str
    company: str
    address: str
    country: str
    state: str
    city: str
    zip_code: str
    mobile_number: str


admin = User(
    login='mrspock',
    email='hello113@enterprise.com',
    password=os.getenv('USER_PASSWORD'),
    date_of_birth=['13', '5', '1985'],
    first_name='Mr',
    last_name='Spock',
    company='Enterprise',
    address='Market street 13',
    country='Australia',
    state='NSW',
    city='Sydney',
    zip_code='2000',
    mobile_number='045678901'
)
