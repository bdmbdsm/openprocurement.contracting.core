# -*- coding: utf-8 -*-
from uuid import uuid4

from openprocurement.api.utils import get_now


test_contract_data = {
    u"items": [
        {
            u"description": u"футляри до державних нагород",
            u"classification": {
                u"scheme": u"CAV",
                u"description": u"Cartons",
                u"id": u"70122000-2"
            },
            u"additionalClassifications": [
                {
                    u"scheme": u"ДКПП",
                    u"id": u"17.21.1",
                    u"description": u"папір і картон гофровані, паперова й картонна тара"
                }
            ],
            u"deliveryAddress": {
                u"postalCode": u"79000",
                u"countryName": u"Україна",
                u"streetAddress": u"вул. Банкова 1",
                u"region": u"м. Київ",
                u"locality": u"м. Київ"
            },
            u"deliveryDate": {
                u"startDate": u"2016-03-20T18:47:47.136678+02:00",
                u"endDate": u"2016-03-23T18:47:47.136678+02:00"
            },
            u"id": u"c6c6e8ed4b1542e4bf13d3f98ec5ab59",
            u"unit": {
                u"code": u"44617100-9",
                u"name": u"item"
            },
            u"quantity": 5
        }
    ],
    u"procuringEntity": {
        u"name": u"Державне управління справами",
        u"identifier": {
            u"scheme": u"UA-EDR",
            u"id": u"00037256",
            u"uri": u"http://www.dus.gov.ua/"
        },
        u"address": {
            u"countryName": u"Україна",
            u"postalCode": u"01220",
            u"region": u"м. Київ",
            u"locality": u"м. Київ",
            u"streetAddress": u"вул. Банкова, 11, корпус 1"
        },
        u"contactPoint": {
            u"name": u"Державне управління справами",
            u"telephone": u"0440000000"
        }
    },
    u"suppliers": [
        {
            u"contactPoint": {
                u"email": u"aagt@gmail.com",
                u"telephone": u"+380 (322) 91-69-30",
                u"name": u"Андрій Олексюк"
            },
            u"identifier": {
                u"scheme": u"UA-EDR",
                u"id": u"00137226",
                u"uri": u"http://www.sc.gov.ua/"
            },
            u"name": u"ДКП «Книга»",
            u"address": {
                u"postalCode": u"79013",
                u"countryName": u"Україна",
                u"streetAddress": u"вул. Островського, 34",
                u"region": u"м. Львів",
                u"locality": u"м. Львів"
            }
        }
    ],
    u"contractNumber": u"contract #13111",
    u"period": {
        u"startDate": u"2016-03-18T18:47:47.155143+02:00",
        u"endDate": u"2017-03-18T18:47:47.155143+02:00"
    },
    u"value": {
        u"currency": u"UAH",
        u"amount": 238.0,
        u"valueAddedTaxIncluded": True
    },
    u"dateSigned": get_now().isoformat(),
    u"awardID": u"8481d7eb01694c25b18658036c236c5d",
    u"id": uuid4().hex,
    u"contractID": u"UA-2016-03-18-000001-1",
    # u"auction_id": uuid4().hex,
    # u"auction_token": uuid4().hex,
    u"owner": u"broker"
}
