import bs4, requests, time

# If the internet goes out, program will wait 20 seconds then try again.
def Get_HTML_Document(url,parameters):
    start_time = time.time()
    while True:
        try:
            res = requests.get(url,params = parameters)
            soup = bs4.BeautifulSoup(res.text,'lxml')
            return soup
        except:
            print('Internet has been out for %.2f minutes' % ((time.time()-start_time)/60))
            time.sleep(20)
