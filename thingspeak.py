import httplib, urllib


def upload(value):
  params = urllib.urlencode({'field1': value,'key' : '7SZ99AFBII74WNK7'})
  headers = {"Content-typZZe":"application/x-www-form-urlencoded", "Accept": "text/plain"}
  
  conn = httplib.HTTPConnection("api.thingspeak.com:80")
  try:
    conn.request("POST", "/update", params, headers)
    response = conn.getresponse()
    print response.status, response.reason
    conn.close()

  except (httplib.HTTPException) as error:
    print "Error at httplib module: %s" % error
  except (IOError) as error:
    print "Error at urllib module: %s" %error
  except:
    print "connection failed"
  print ""
