#!/usr/bin python3
# -*- coding: utf-8 -*-

import requests
import persons_config
import https_old_config
import json

def punch_card_batch(person_list):
    for person in person_list:
        punch_card(person)

def punch_card(person_info):
    response = requests.post(url=https_old_config.http_url,
                             headers=https_old_config.http_header,
                             data=json.dumps(person_info),
                             verify=https_old_config.http_verify)

    print(response.text)

if __name__ == "__main__":
    punch_card_batch(persons_config.person_list)