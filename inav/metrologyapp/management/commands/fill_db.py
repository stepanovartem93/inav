from django.core.management.base import BaseCommand
from metrologyapp.models import TypeOfMeasurment, MeasuringInstrument
from django.contrib.auth.models import User
from django.conf import settings


import json, os

def load_from_json(file_name):
    with open(os.path.join(settings.JSON_PATH, f'{file_name}.json'), 'r', encoding='utf-8' ) as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        types_of_measurments = load_from_json('types_of_measurment')

        TypeOfMeasurment.objects.all().delete()
        for type_of_measurment in types_of_measurments:
            new_type = TypeOfMeasurment(**type_of_measurment)
            new_type.save()

        instruments = load_from_json('measuring_instruments')

        MeasuringInstrument.objects.all().delete()
        for instrument in instruments:
            type_name = instrument['typeofmeasurment']
            #Получаем тип по имени
            _typeofmeasurment = TypeOfMeasurment.objects.get(name=type_name)
            # _typeofmeasurment = TypeOfMeasurment.objects.filter(name=type_name).first()
            #Заменяем название типа объектом
            instrument['typeofmeasurment'] = _typeofmeasurment
            new_measuring_instrument = MeasuringInstrument(**instrument)
            new_measuring_instrument.save()