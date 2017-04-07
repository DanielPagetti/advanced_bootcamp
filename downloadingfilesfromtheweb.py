import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
type(res)

res.status_code == requests.codes.ok
True
len(res.text)
print(res.text[:250])

res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))
res.raise_for_status()
