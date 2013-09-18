#Calculate module

def Calculate(n):
    try:
        answer = eval(n)
        print answer
        return answer
    except:
        print 'Cannot calculate '+str(n)+' using eval(). Getting Wolfram Alpha to help...'
        import urllib2
        import urllib
        response = urllib2.urlopen('http://api.wolframalpha.com/v2/query?input='+str(n.replace(' ','+')+'&appid=UAGAWR-3X6Y8W777Q'))
        html = response.read()
        from xml.dom.minidom import parseString
        dom = parseString(html)
        itemlist = dom.getElementsByTagName('pod')

        for i in itemlist:
            if i.attributes['title'].value == 'Result':
                itemlist2 = i.getElementsByTagName('plaintext')
                print itemlist2[0].childNodes[0].nodeValue
                return itemlist2[0].childNodes[0].nodeValue

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Calculate stuff')
    parser.add_argument('required_arg', help='enter equation to calculate')
    
    results = parser.parse_args()
    Calculate(results.required_arg)


def test_1():
    assert abs(4. - Calculate('2**2')) < .001

def test_2():
    assert abs(8. - Calculate('2*3*4*5/3/5')) < .001

def test_3():
    assert abs(100. - Calculate('100+2-3')) > .9

def test_4():
    assert abs(1.5 - Calculate('2**.5')) <.5
               
def test_5():
    assert abs(3.14 - Calculate('22./7')) <.003
