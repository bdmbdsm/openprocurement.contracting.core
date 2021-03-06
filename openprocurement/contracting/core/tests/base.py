# -*- coding: utf-8 -*-
import json
import os
from copy import deepcopy
from uuid import uuid4
from webtest import TestApp

from openprocurement.api.utils import get_now
from openprocurement.contracting.api.tests.base import (
    BaseWebTest as BaseBaseWebTest
)


class DumpsTestAppwebtest(TestApp):
    """ Class used for docs (move to common later?) """
    hostname = "api-sandbox.openprocurement.org"

    def do_request(self, req, status=None, expect_errors=None):
        req.headers.environ["HTTP_HOST"] = self.hostname
        if hasattr(self, 'file_obj') and not self.file_obj.closed:
            self.file_obj.write(req.as_bytes(True))
            self.file_obj.write("\n")
            if req.body:
                try:
                    self.file_obj.write(
                            'DATA:\n' + json.dumps(json.loads(req.body), indent=2, ensure_ascii=False).encode('utf8'))
                    self.file_obj.write("\n")
                except:
                    pass
            self.file_obj.write("\n")
        resp = super(DumpsTestAppwebtest, self).do_request(req, status=status, expect_errors=expect_errors)
        if hasattr(self, 'file_obj') and not self.file_obj.closed:
            headers = [(n.title(), v)
                       for n, v in resp.headerlist
                       if n.lower() != 'content-length']
            headers.sort()
            self.file_obj.write(str('Response: %s\n%s\n') % (
                resp.status,
                str('\n').join([str('%s: %s') % (n, v) for n, v in headers]),
            ))

            if resp.testbody:
                try:
                    self.file_obj.write(json.dumps(json.loads(resp.testbody), indent=2, ensure_ascii=False).encode('utf8'))
                except:
                    pass
            self.file_obj.write("\n\n")
        return resp


test_contract_data = {
    u"items": [
        {
        u"description": u"футляри до державних нагород",
        u"classification": {
                        u"scheme": u"CPV",
                        u"description": u"Cartons",
                        u"id": u"44617100-9"
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
    u"tender_id": uuid4().hex,
    u"tender_token": uuid4().hex,
    u"owner": u"broker"
}


test_contract_data_wo_items = deepcopy(test_contract_data)
del test_contract_data_wo_items['items']


documents = [
    {
        "title": "contract_first_document.doc",
        "url": "http://api-sandbox.openprocurement.org/api/0.12/tenders/ce536c5f46d543ec81ffa86ce4c77c8b/contracts/1359720ade994a56b488a92f2fa577b2/documents/f4f9338cda06496f9f2e588660a5203e?download=711bc63427c444d3a0638616e559996a",
        "format": "application/msword",
        "documentOf": "tender",
        "datePublished": "2016-03-18T18:48:06.238010+02:00",
        "id": "f4f9338cda06496f9f2e588660a5203e",
        "dateModified": "2016-03-18T18:48:06.238047+02:00"
        },
    {
        "title": "contract_second_document.doc",
        "url": "http://api-sandbox.openprocurement.org/api/0.12/tenders/ce536c5f46d543ec81ffa86ce4c77c8b/contracts/1359720ade994a56b488a92f2fa577b2/documents/9c8b66120d4c415cb334bbad33f94ba9?download=da839a4c3d7a41d2852d17f90aa14f47",
        "format": "application/msword",
        "documentOf": "tender",
        "datePublished": "2016-03-18T18:48:06.477792+02:00",
        "id": "9c8b66120d4c415cb334bbad33f94ba9",
        "dateModified": "2016-03-18T18:48:06.477829+02:00"
        }
]


class BaseWebTest(BaseBaseWebTest):
    """Base Web Test to test openprocurement.contractning.core.api.

    It setups the database before each test and delete it after.
    """
    relative_to = os.path.dirname(__file__)


class BaseContractWebTest(BaseWebTest):
    initial_data = test_contract_data

    def setUp(self):
        super(BaseContractWebTest, self).setUp()
        self.create_contract()

    def create_contract(self):
        data = deepcopy(self.initial_data)

        orig_auth = self.app.authorization
        self.app.authorization = ('Basic', ('contracting', ''))
        response = self.app.post_json('/contracts', {'data': data})
        self.contract = response.json['data']
        # self.contract_token = response.json['access']['token']
        self.contract_id = self.contract['id']
        self.app.authorization = orig_auth

    def tearDown(self):
        del self.db[self.contract_id]
        super(BaseContractWebTest, self).tearDown()


class BaseContractContentWebTest(BaseContractWebTest):

    def setUp(self):
        super(BaseContractContentWebTest, self).setUp()
        response = self.app.patch_json('/contracts/{}/credentials?acc_token={}'.format(
            self.contract_id, self.initial_data['tender_token']), {'data': {}})
        self.contract_token = response.json['access']['token']
