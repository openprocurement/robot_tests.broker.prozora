# -*- coding: utf-8 -*-
import pytz
import dateutil.parser
import urllib

from datetime import datetime
from robot.libraries.BuiltIn import BuiltIn

def get_str(value):
    return str(value)

def get_price(initial_tender_data):
    return str(initial_tender_data.data.value.amount)

def convert_prozora_string_to_common_string(string):
    return {
        u"з ПДВ": True,
        u"без ПДВ": False,
        u"Права вимоги за кредитами": "dgfFinancialAssets",
        u"Голандський аукціон": "dgfInsider",
        u"Майно": "dgfOtherAssets",
        u"Пропозиції": "active.tendering",
        u"Відмінений": "cancelled",
        u"Не відбувся": "unsuccessful",
        u"Аукціон": "active.auction",
        u"Кваліфікація": "active.qualification",
        u"Розглянуто": "active.awarded",
        u"Завершений": "complete",
        u"грн": "UAH",
        u"Очікується завантаження підписаного переможцем протоколу аукціону": "pending.verification",
        u"Очікується оплата": "pending.payment",
        u"Учасника дискваліфікував кваліфікаційний комітет (банк)": "unsuccessful",
        u"Учасник виграв аукціон": "active",
        u"Очікує дискваліфікації": "pending.waiting",
        u"Учасник відмовився": "cancelled"
    }.get(string, string)

def convert_document_type(string):
    return {
        u"Паспорт торгів": "tenderNotice",
        u"Технічні специфікації": "technicalSpecifications",
        u"Критерії оцінки": "evaluationCriteria",
        u"Пояснення до питань заданих учасниками": "clarifications",
        u"Інформація про учасників торгів": "bidders",
        u"Іллюстрації": "illustration",
        u"Публічний паспорт активу": "x_dgfPublicAssetCertificate",
        u"Презентація": "x_presentation",
        u"Договір NDA": "x_nda",
        u"Опис активів": "x_dgfAssetFamiliarization",
        u"Віртуальна кімната для роботи з конфіденційними даними": "virtualDataRoom",
        u"Юридична Інформація Майданчиків": "x_dgfPlatformLegalDetails"
    }.get(string, string)

def get_min_step(initial_tender_data):
    return str(initial_tender_data.data.minimalStep.amount)

def get_tenderAttempts(item):
    return str(item.tenderAttempts)

def convert_ISO_DMY(isodate):
    return dateutil.parser.parse(isodate).strftime("%d.%m.%Y")

def convert_date(isodate):
    return datetime.strptime(isodate, '%d.%m.%Y').date().isoformat()

def convert_iso_to_date_time(v_date_time):
    date_obj = v_date_time.split('+')[0]
    date_obj = datetime.strptime(date_obj, "%Y-%m-%dT%H:%M:%S.%f")
    time_zone = pytz.timezone('Europe/Kiev')
    localized_date = time_zone.localize(date_obj)
    return localized_date.strftime("%d.%m.%Y %H:%M")

def convert_date_time_to_iso(v_date_time):
    date_obj = datetime.strptime(v_date_time, "%d.%m.%Y %H:%M:%S")
    time_zone = pytz.timezone('Europe/Kiev')
    localized_date = time_zone.localize(date_obj)
    return localized_date.strftime("%Y-%m-%dT%H:%M:%S.%f%z")

def is_qualified(tender_data):
    if 'qualified' in tender_data['data']:
        return  tender_data['data']['qualified']
    return False

def is_eligible(tender_data):
    if 'eligible' in tender_data['data']:
        return  tender_data['data']['eligible']
    return False

def download_file(url, file_name, output_dir):
    urllib.urlretrieve(url, ('{}/{}'.format(output_dir, file_name)))

def inc(value):
    return int(value) + 1
