TransactPRO Python integration
===============
[![Coverage Status](https://coveralls.io/repos/TransactPRO/transactpro-integration-python/badge.png)](https://coveralls.io/r/TransactPRO/transactpro-integration-python)
## About


**Author**: Olga Zdanchuk

**Contact**: zdanchuk@gmail.com


Library provide ability to make requests to TransactPRO Gateway API.
Library are supported by me, and not by TransactPRO. So, submit all requests, issues and questions directly here (on GitHub). Library provided as is.
You must adopt library for your projects by yourselves, I only provide basic functionality to make requests.

## Installation

Download project from Github, with downloading zip file or using
```
git clone https://github.com/pashira/transactpro-integration-python.git
```

Use pip to install requirements
```
pip install -r requirements.txt
```

## Usage
### Create gate client
| Field     | Mandatory | Type   | Description                                                          |
|-----------|-----------|--------|----------------------------------------------------------------------|
| apiUrl    | yes       | string | Api URL. Can be aquired via Integration manual.                      |
| guid      | yes       | string | Merchant GUID.                                                       |
| pwd       | yes       | string | Unecrypted password. It will be encrypted by client.                 |
| verifySSL | no        | bool   | Default: ```true```. Must be set to ```false``` for test environment |
| save_card | no        | int    | Set ```1``` to process recurrent transactions                        |

### Basic client
```python
gate_client = GateClient('http://example.com', 'AAAA-1111-1111-1111', 'mypass')
```

### Actions
GateClient instance provide number of actions, such as 'init' or 'charge'.
All data passed into action are validated and if mandatory field missed, then exception will be raised.
Please check integration manual, to get more info about required data for each action.

#### Init
```python
response = gate_client.init({
    'rs': 'AAAA',
    'merchant_transaction_id': '1212121212',
    'user_ip': '127.0.0.1',
    'description': 'Test description',
    'amount': '1000',
    'currency': 'USD',
    'name_on_card': 'Vasyly Pupkin',
    'street': 'Main street 1',
    'zip': 'LV-0000',
    'city': 'Riga',
    'country': 'LV',
    'state': 'NA',
    'email': 'email@example.lv',
    'phone': '+371 11111111',
    'card_bin': '511111',
    'bin_name': 'BANK',
    'bin_phone': '+371 11111111',
    'merchant_site_url': 'https://example.com'})
```

#### Charge
```python
response = gate_client.charge ({
    'f_extended': '5',
    'init_transaction_id': 'c811f6504791085cdd569e6a440c4f292b0f0003',
    'cc': '1111111111111111',
    'cvv': '222',
    'expire': '01/15'})
```

#### Refund
```python
response = gate_client.refund ({
    'init_transaction_id': '2250fcc6fd097e7b9df02aa9b95bf46baa7f8fea',
    'amount_to_refund': '9'})
```

#### Recount
```python
response = gate_client.charge_recurrent({
    'init_transaction_id': '2250fcc6fd097e7b9df02aa9b95bf46baa7f8fea'})
```

#### Init DMS
```python
response = gate_client.init_dms({
    'rs': 'AAAA',
    'merchant_transaction_id': '1212121212',
    'user_ip': '127.0.0.1',
    'description': 'Test description',
    'amount': '1000',
    'currency': 'USD',
    'name_on_card': 'Vasyly Pupkin',
    'street': 'Main street 1',
    'zip': 'LV-0000',
    'city': 'Riga',
    'country': 'LV',
    'state': 'NA',
    'email': 'email@example.lv',
    'phone': '+371 11111111',
    'card_bin': '511111',
    'bin_name': 'BANK',
    'bin_phone': '+371 11111111',
    'merchant_site_url': 'https://example.com'})
```

#### Make hold
```python
response = gate_client.make_hold({
    'f_extended': '5',
    'merchant_transaction_id': '1212121212',
    'cc': '1111111111111111',
    'cvv': '222',
    'expire': '01/15'})
```

#### Charge hold
```python
response = gate_client.charge_hold({
    'init_transaction_id': '2250fcc6fd097e7b9df02aa9b95bf46baa7f8fea']})
```

#### Cancel DMS
```python
response = gate_client.cancel_dms({
    'init_transaction_id':  '2250fcc6fd097e7b9df02aa9b95bf46baa7f8fea',
    'amount_to_refund': '1000'})
```

## Tests

Run the nosetests command
```
nosetests
```