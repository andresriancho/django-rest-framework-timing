# Django REST framework timing
Minimalistic Django REST framework to test timing attacks, heavily based
on [Django REST framework quick start tutorial](http://www.django-rest-framework.org/tutorial/quickstart/).

# Installation

```bash
cd djanto-rest-framework-timing/
virtualenv venv
pip install -r requirements.txt
pip install -r client/requirements.txt
```

# Setup
The current version uses a SQLite database and Token authentication for
the REST API.

Build the docker container:

```bash
docker build -t timing .
```

The following are sorted API key / username pairs:
 
```
0375c93181e17933041886d441241188876747a0:test73
04b2b9d4cddcdc973b601a8bae519b74621310d5:test13
06e73df8a6a57a54a9d2bc6ee0de9ce3f76cb2b6:test31
070fb39e60eeea6975efff12ed1b7258c60d9d07:test4
09fce6b61993f87a647d217c8a610c0796ffc35b:test1
0d32c948f3319747704241ce0ae7f750ef76040e:test3
10c5faa0f8e18a7af0d49ce3cddcdf50282ba8de:test27
12ceb9c0a2d1ae03b559d27367b7e46fb5fc54c4:test80
15097aa62c393ada50ff2e0e927aa1034fc99816:test24
1cc3562d695b5771dbb74d577389c86894bef3f3:test61
224a93060c0dd4fb931d05083b4cb7b6a8c27df8:test78
224b543064bef6e351a84f4dc68ba43c7c8f6965:test33
24362df47101733ae530503ad5298b7ba5103bbd:test26
2852917492fac14ced26a618e38dd1c62afc632a:test17
28fcaf5342f829b67169fe0c1c0d1c824e528169:test74
2de4289d0f3206378127e5cd27dd3c32ec394247:test54
2feb69f47aa0554686723aec86e7ca134d9195d6:test23
34a9a34f6d016b8d762cc8f5f5dfb02fc99415a5:test36
37d3d73591944397f3c3d754dad8431a417ed137:test41
3af3cb0921a521a27a9663f856ffd81e6dc4fa2d:test16
3b4fdf867b841f49c8b17e6a279ec43a5ea1b428:test60
3e9f58b60c34ad6d6c04b7e92935501111c89c9f:test11
3eb993a85aa7ecd5f99ad9acb0c81f541eef38ad:test9
43d35f364f1ee0ae633db2a53b79956b66f349f2:test70
4443ee8034c7cfdd7035bf73c31eda23fb95bf98:test7
4485438af1a73e7faad413380a573e67c083aea7:test64
4588ba3b124ae372481d2c899e2bdc4d2aa3661b:test18
46fe87e523b0c7360eb02000298409e609934868:test30
4712b976fadceeb990dfd096708b8fc7fdb402f4:test5
474eb37cc4af337ee6cd919d635dd3b0781e2eed:test50
483bffb3633a08ef30d21b086928959454fd6fc0:test37
4cac130b367a8788b46cc35f5d84cfe3a3dfe860:test62
4cc340ba481b7c055d41589db67a6aa060b9fa2f:test35
4e0ba3568c67f49d28a3740debd20b2889445d9a:test75
531c837ba21c378d0301a11a7f6a59a061b7784d:test95
54866cb6399d2c73b3997f6c3b96cbaee3d63d9c:test44
5696b2fc85f4bdab15e083f5be3cce5300919b54:test87
57b35b5c0640dd2bc2d3da884dd57eeead398e04:test93
58daa8834f051a306bba1703bb74cc8f46ad1c45:test42
59990918d5e107ec092075990925847c51995139:test22
5dd7539ec147b8b1ec029816c8f75356c669568d:test52
5e1372d6c29841e09b7da0295d79c0e5c7c1889c:test68
5ebc17ba7c4cf2cb6b6648db09fe980df0e09bdd:test0
5f5c707123a471ccb10e08c986fb71719bd60fcc:test20
6ff35621c80b2a15a3269b77b2d6b81cde345c43:test94
7592f2177bae8c4586f257da368edb75762e5167:test48
76af3ffa5ca7e753c6451cbf66e80f8b98b4c2b2:test63
7766b0277a8adf9421cc6fbc91ad7ca1e39532d3:test29
7eaa82817eb1963fba8515ff1d0ddb31370b2deb:test32
856402b83fe3c6907eba7a49c962bea4180c4274:test43
884d6d0b4b1d74f50b7b7dd750b5fedb033e881b:test71
8bbcfdda293c85d0a607199f030eecdfd82d243e:test34
94d6f397b3487b7d67a64d220f5e18c6262172e9:test38
9654b0a5a45024b89c41acb25d59600dc2d10507:test69
99f6b893de5ee6fc29025f325abd4975fd8f3b57:test83
9a4490126b84e76d125f678364be41af1f30f369:test46
a2b24af57a7899651aace2e470c108a61c1716ca:test2
a3ce0422fd9def2b1e200dc4c266f155040b3666:test86
a6dabc93054940189324f7a0fd4c601d3da422c9:test90
aade89453008708bd762dc32adec5cba605bf72c:test82
adf8e3c46da05fab5ada933b48bf789a2d4cf6f0:test96
af07312fd38cad9e9a3adff43120381e6001ca08:test49
afee1ade9612e44433787dded847d8ac65a4f9d7:test84
b60e174c221bde06b36fae1bb3ebbdf95bfdf3b6:test56
b76526d26d78537dec055df82512b3fac4f071b8:test28
b798623adbe0be704df6ba8a67f053b7c7f57a77:test47
b86956c5bce188b7e2989ffb8062bc6e8b53ba66:test98
bc80e7da335f26468667cec5a330a85ec78d0618:test57
bce1cba9b2aa44e4a17f69c9a7a95432da373eec:test39
c1bc957ea1cb08b4c42c1fb9a31bd6339cc0b0f6:test12
c32b59ae197fc814cc30c7f0e886c60df5931f77:test76
c346f10f02107ce7e12386be3abbb9032d19af20:test91
ca306f5a821f810d82071391419ce15b98ed0570:test45
cad9930c29d8d1bab4673da86ef7c083204c466d:test66
cb786830b017a927a889aaeebc1ae1d313f4e492:test55
cf546b2344099678facc495ca2b7059a5a0f3e2f:test53
d12056d1803084e9d3dd9ace3db9b0ba1cf1bd7d:test97
d218e4cba8ee08d35f3ff0eb04eccdd2a7e94fdf:test92
d29e07f795d04d02c04785052c840525ad11033a:test21
d591db6b61cc1fe2606d780ca3385c6a016003df:test6
dc90906c5733e3b88dc7ec42b2fb22b86a97da71:test67
dcba6ff60bc16353a4c5532bdbc467dd9d850152:test58
de013611e6a0aa0f0f3679247d64a2a14d1dfe73:test79
df5ba347d68bdd47cb9fa3ee8d2bf592b1eabcda:test51
e18b8001f582823aab4a21a0cf7fd7289f92d323:test88
e315021e8b13dfe0445934f5f95732470f7e41e0:test25
e4d27ee8258a5a516c599a2eaeedeaf1ed7106c6:test72
e5a55f5de7a79fb4ed4d34130c9c4050dd6cb49e:test85
e64881c81f1546daf544249513a0512ea5700f6c:test14
e6dcb57875974bdfa42edd95b22baf87923625c7:test59
e905eaf59ff270b957ff18e90a86a31888f713f5:test40
ed2c572ef895305c4edb803fb55844e8c97fac4e:test77
ee003cba441e34cf61b3c254f62e9a21d8515b8d:test99
ee7ec44cc8832bc3bc4df399a8aa64bbba57952d:test10
f1638c87c400e964710204cfdcb7a639b57e100d:test65
f39347c267956d4754f27f88eb6f22927b82957d:test15
f53015edb698271dec1d6ab76045945f9c77c435:test8
f5ec26fb421a7b633f37d829481070bd722830ec:test81
f8d7eb569ef86aecfad1c10caaa9501e47de0e3f:test19
fd51bd84d556738e8d3e500eab35163222929c4c:test89
```

And were generated using this script:

```python
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

for i in xrange(100):
    username = 'test%s' % i
    new_user = User.objects.create_user(username, 'test%s@bonsai-sec.com' % i, 'password%s' % i)
    token = Token.objects.create(user=new_user)
    print('%s:%s' % (username, token.key))
```

The Django admin credentials are: `admin` / `password123`.

# Notes

## Consuming the API

Start the docker container:

```
docker run -p 8000:80 -i -t timing
```

Consume the API using a `Token`:

```
curl -X GET http://127.0.0.1:8000/users/ -H 'Authorization: Token 224a93060c0dd4fb931d05083b4cb7b6a8c27df8'
```

## Getting Timing Samples

Please note that this tool is Linux-specific due to the OS tricks implemented
in the `os_utils.py` module.

Edit the constants in `timing-collector.py` and then:

```
cd client
sudo -s -H
source venv/bin/activate
python timing-collector.py sample-name
```

## Analyzing Samples

Edit the sample input file names in `graph-results.py` and then:

```
python graph-results.py sample-name
```
