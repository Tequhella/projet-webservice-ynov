from django.contrib import admin
from fishingdate.models import User, Notebook, Boat, Excursion, Booking, DateTimeExcursion


class UserAdmin(admin.ModelAdmin):

    list_display = (
        'lastname',
        'firstname',
        'birthday',
        'email',
        'phone',
        'address',
        'zipcode',
        'city',
        'languages',
        'URLAvatar',
        'boatLicenseNumber',
        'insuranceNumber',
        'status',
        'companyName',
        'activity',
        'siretNumber',
        'tradeRegisterNumber',
        'boatList',
        'notebookPageList',
        'excursionList',
        'bookingList'
    )


class NotebookAdmin(admin.ModelAdmin):

    list_display = (
        'URLFish',
        'comment',
        'size',
        'weight',
        'place',
        'date',
        'released',
        'user'
    )

    @admin.display(description='User')
    def category(self, obj):
        return obj.notebook.user


class BoatAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'description',
        'brand',
        'year',
        'URLBoat',
        'boatLicenseType',
        'boatType',
        'equipments',
        'deposit',
        'capacity',
        'bedsNumber',
        'harbor',
        'longitude',
        'latitude',
        'motor',
        'horsepower',
        'user'
    )

    @admin.display(description='User')
    def category(self, obj):
        return obj.boatsList.user
    
    
class ExcursionAdmin(admin.ModelAdmin):

    list_display = (
        'excursionTitle',
        'information',
        'excursionType',
        'tariff',
        'dateList',
        'numberOfPassengers',
        'excursionPrice',
        'idBoat',
        'user'
    )

    @admin.display(description='User')
    def category(self, obj):
        return obj.fishingExcursionsList.user

    
class BookingAdmin(admin.ModelAdmin):

    list_display = (
        'idExcursion',
        'date',
        'nbBookedSeats',
        'totalPrice',
        'user'
    )

    @admin.display(description='User')
    def category(self, obj):
        return obj.bookingsList.user


class DateTimeExcursionAdmin(admin.ModelAdmin):

    list_display = (
        'startDate',
        'endDate'
    )

    @admin.display(description='Excursion')
    def category(self, obj):
        return obj.dateTimeList.fishingExcursionsList.user


admin.site.register(User, UserAdmin)
admin.site.register(Notebook, NotebookAdmin)
admin.site.register(Boat, BoatAdmin)
admin.site.register(Excursion, ExcursionAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(DateTimeExcursion, DateTimeExcursionAdmin)
