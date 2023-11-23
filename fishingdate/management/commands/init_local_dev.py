from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from fishingdate.models import Category

UserModel = get_user_model()

USERS = [
    {
        'idUser': 1,
        'lastname': 'Magaud',
        'firstname': 'Guilhem',
        'birthday': '2002-05-08T00:45:00.000000Z',
        'email': 'guilhem.magaud@ynov.com',
        'phone': "0606060606",
        'address': '666 Maison du Diable',
        'zipcode': '83440',
        'city': 'Fayence',
        'languages': [
            'FR-fr',
            'EN-uk'
        ],
        'URLAvatar': 'https://www.my-sexy-pic.com/photos/69.png',
        'boatLicenseNumber': 'F4GJGF62JJ00K',
        'insuranceNumber': '001636272673',
        'status': 'Professionnel',
        'companyName': 'Ynov',
        'activity': 'Location',
        'siretNumber': 12356894100056,
        'tradeRegisterNumber': 'RCS PARIS B 517 403 572',
        'notebook': [
            {
                'idPage': 1,
                'URLFish': 'https://www.my-awesome-fish.fr/photos/3.png',
                'comment': 'Incroyable le poisson !',
                'size': 35,
                'weight': 1.5,
                'place': 'Cagnes-Sur-Mer',
                'date': '2023-06-12T11:16:54.000000Z',
                'released': 'Non'
            }
        ],
        'boatsList': [
            {
                'idBoat': 1,
                'name': 'Titan',
                'description': 'Coolest submarine of the world',
                'brand': 'OceanGate',
                'year': 2017,
                'URLBoat': 'https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Titan_submersible.jpg/300px-Titan_submersible.jpg',
                'boatLicenseType': 'Côtier',
                'boatType': 'Open',
                'equipments': [
                    'Sondeur',
                    'GPS'
                ],
                'deposit': 48000000,
                'capacity': 5,
                'bedsNumber': 5,
                'harbor': "Pearl Harbor",
                'longitude': 21.351203300630008,
                'latitude': -157.98013297318147,
                'motor': 'Hydrolic pressure',
                'horsepower': 100
            }
        ],
        'fishingExcursionsList': [
            {
                'idExcursion': 1,
                'excursionTitle': 'À la recherche du Titanic !',
                'information': 'Avis de recherche - Élu meilleur engin maritime de 2023',
                'excursionType': 'Journalière',
                'tariff': 'Par personne',
                'dateTimeList': [
                    {
                        'startDate': '2023-06-12T10:00:00.000000Z',
                        'endDate': '2023-06-20T18:00:00.000000Z'
                    }
                ],
                'numberOfPassengers': 5,
                'excursionPrice': 250000,
                'idOwner': 2,
                'idBoat': 1
            }
        ],
        'bookingsList': [
            {
                'idBooking': 1,
                'idExcursion': 1,
                'date': '2023-06-12T10:00:00.000000Z',
                'nbBookedSeats': 5,
                'totalPrice': 1250000,
                'idBooker': 2
            }
        ]
    }
]

ADMIN_ID = 'admin-oc'
ADMIN_PASSWORD = 'password-oc'


class Command(BaseCommand):

    help = 'Initialize project for local development'

    def handle(self, *args, **options):
        self.stdout.write(self.style.MIGRATE_HEADING(self.help))

        Category.objects.all().delete()

        for data_category in USERS:
            category = Category.objects.create(name=data_category['name'],
                                               active=data_category['active'])
            for data_product in data_category['products']:
                product = category.products.create(name=data_product['name'],
                                                   active=data_product['active'])
                for data_article in data_product['articles']:
                    product.articles.create(name=data_article['name'],
                                            active=data_article['active'],
                                            price=data_article['price'])

        UserModel.objects.create_superuser(ADMIN_ID, 'admin@oc.drf', ADMIN_PASSWORD)

        self.stdout.write(self.style.SUCCESS("All Done !"))
