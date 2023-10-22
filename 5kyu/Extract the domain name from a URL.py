def domain_name(url):
    resp = url.replace("http://","").replace("https://","").replace("www.","")
    resp = resp.split('.')
    return resp[0]