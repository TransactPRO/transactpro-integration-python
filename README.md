Library provide ability to make requests to TransactPRO Gateway API (Documention 2.16).

# Installation
### Git

Download project from Github, with downloading zip file or using


### Git
Use pip to install requirements

pip install -r requirements.txt



#### Basic client
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
        'merchant_transaction_id' : '12112112323323',
        'user_ip'                 : '127.0.0.1',
        'description'             : 'Test description',
        'amount'                  : '1000',
        'currency'                : 'USD',
        'name_on_card'            : 'Vasyly Pupkin',
        'street'                  : 'Main street 1',
        'zip'                     : 'LV-0000',
        'city'                    : 'Riga',
        'country'                 : 'LV',
        'state'                   : 'NA',
        'email'                   : 'email@example.lv',
        'phone'                   : '+371 11111111',
        'card_bin'                : '511111',
        'bin_name'                : 'BANK',
        'bin_phone'               : '+371 11111111',
        'merchant_site_url'       : 'https://example.com'})
```

#### Charge
```python
response = gate_client.charge ({
        'f_extended'          : '5',
        'init_transaction_id' : transaction_id[1],
        'cc'                  : '5413330000000019',
        'cvv'                 : '589',
        'expire'              : '01/15'})
```