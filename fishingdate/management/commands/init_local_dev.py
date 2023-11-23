from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from fishingdate.models import User, Notebook, Boat, Excursion, Booking

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
    },
{
        'idUser': 2,
        'lastname': 'Chardon',
        'firstname': 'Lilian',
        'birthday': '2000-05-19T00:45:00.000000Z',
        'email': 'lilian.chardon@ynov.com',
        'phone': "0707070707",
        'address': '69 Maison du Plaisir',
        'zipcode': '06600',
        'city': 'Antibes',
        'languages': [
            'FR-fr'
        ],
        'URLAvatar': 'https://www.unicorn-fans.com/photos/5.png',
        'boatLicenseNumber': 'F1BPLF62JJ69Q',
        'insuranceNumber': '101695272243',
        'status': 'Professionnel',
        'companyName': 'Ynov',
        'activity': 'Guide de pêche',
        'siretNumber': 49685234100746,
        'tradeRegisterNumber': 'SNK NICE D 998 254 576',
        'notebook': [
            {
                'idPage': 1,
                'URLFish': 'https://www.my-awesome-fish.fr/photos/9.png',
                'comment': 'Le poisson est beau !',
                'size': 25,
                'weight': 0.95,
                'place': 'Cagnes-Sur-Mer',
                'date': '2023-06-12T13:37:12.000000Z',
                'released': 'Oui'
            }
        ],
        'boatsList': [],
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

        User.objects.all().delete()

        for data_user in USERS:
            user = User.objects.create(
                lastname=data_user['lastname'],
                firstname=data_user['firstname'],
                birthday=data_user['birthday'],
                email=data_user['email'],
                phone=data_user['phone'],
                address=data_user['address'],
                zipcode=data_user['zipcode'],
                city=data_user['city'],
                languages=data_user['languages'],
                URLAvatar=data_user['URLAvatar'],
                boatLicenseNumber=data_user['boatLicenseNumber'],
                insuranceNumber=data_user['insuranceNumber'],
                status=data_user['status'],
                companyName=data_user['companyName'],
                activity=data_user['activity'],
                siretNumber=data_user['siretNumber'],
                tradeRegisterNumber=data_user['tradeRegisterNumber']
            )

            for data_notebook in data_user['notebook']:
                notebook = user.notebook.create(
                    URLFish=data_notebook['URLFish'],
                    comment=data_notebook['comment'],
                    size=data_notebook['size'],
                    weight=data_notebook['weight'],
                    place=data_notebook['place'],
                    date=data_notebook['date'],
                    released=data_notebook['released']
                )

            for data_boat in data_user['boatsList']:
                boat = user.boatsList.create(
                    name=data_boat['name'],
                    description=data_boat['description'],
                    brand=data_boat['brand'],
                    year=data_boat['year'],
                    URLBoat=data_boat['URLBoat'],
                    boatLicenseType=data_boat['boatLicenseType'],
                    boatType=data_boat['boatType'],
                    equipments=data_boat['equipments'],
                    deposit=data_boat['deposit'],
                    capacity=data_boat['capacity'],
                    bedsNumber=data_boat['bedsNumber'],
                    harbor=data_boat['harbor'],
                    longitude=data_boat['longitude'],
                    latitude=data_boat['latitude'],
                    motor=data_boat['motor'],
                    horsepower=data_boat['horsepower']
                )

            for data_excursion in data_user['fishingExcursionsList']:
                excursion = user.fishingExcursionsList.create(
                    excursionTitle=data_excursion['excursionTitle'],
                    information=data_excursion['information'],
                    excursionType=data_excursion['excursionType'],
                    tariff=data_excursion['tariff'],
                    dateTimeList=data_excursion['dateTimeList'],
                    numberOfPassengers=data_excursion['numberOfPassengers'],
                    excursionPrice=data_excursion['excursionPrice'],
                    idOwner=data_excursion['idOwner'],
                    idBoat=data_excursion['idBoat']
                )

            for data_booking in data_user['bookingsList']:
                booking = user.bookingsList.create(
                    idExcursion=data_booking['idExcursion'],
                    date=data_booking['date'],
                    nbBookedSeats=data_booking['nbBookedSeats'],
                    totalPrice=data_booking['totalPrice'],
                    idBooker=data_booking['idBooker']
                )

        UserModel.objects.create_superuser(ADMIN_ID, 'admin@oc.drf', ADMIN_PASSWORD)

        self.stdout.write(self.style.SUCCESS("All Done !"))
