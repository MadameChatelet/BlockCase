from flask import Flask, escape, request, render_template
from json import loads
import requests


app = Flask(__name__) #name means this current file--> app.py
#the file represents the web application.

@app.route('/')#represents the default page
def index():
    return render_template('index.html', title = 'bloCKCs')
#,data = u,  data2 = number, data3 = actual_hash(u), data4=la_llista(8), ether = la_llista_ether(8)

@app.route('/home')#represents the default page
def home():
    return render_template('index.html', title = 'bloCKCs')


@app.route('/pat_bitcoin')
def pat_bitcoin():
    return render_template("pat_bitcoin.html" ,title = 'pat_bitcoin', data4=la_llista(8), block = number)


@app.route('/pat_ether')
def pat_ether():
    return render_template("pat_ether.html",title = 'pat_ether', ether = la_llista_ether(8), block_ether = number_ether)

 
    
@app.route('/eth_bitcoin')
def eth_bitcoin():
    return render_template("eth_bitcoin.html",title = 'eth_bitcoin', data4=la_llista(8), block = number)


@app.route('/eth_ether')
def eth_ether():
    return render_template("eth_ether.html",title = 'eth_ether', ether = la_llista_ether(8), block_ether = number_ether)



@app.route('/aboutus')
def aboutus():
    return render_template("aboutus.html",title = 'aboutus')
    
    
@app.route('/contact')
def contact():
    return render_template("contact.html",title = 'contact')


@app.route('/shop')
def shop():
    return render_template("shop.html",title = 'shop')







if __name__== "__main__":
    app.run(debug=True)




def get_block_info():

    return loads(requests.get("https://api.blockchair.com/bitcoin/blocks").content)
def get_block_ether():

    return loads(requests.get("https://api.blockchair.com/ethereum/blocks").content)

hashi = get_block_info()["data"][0]["hash"]
u = [x for x in hashi[19:]]

hashi_ether = get_block_ether()["data"][0]["hash"]
m = [x for x in hashi_ether[1:]]


number = [get_block_info()["data"][i]["id"] for i in range(0,8)] 
number_ether = [get_block_ether()["data"][i]["id"] for i in range(0,8)] 
def actual_hash(li):
    l=[]
    for x in li:
        try:
            x = int(x)
            l.append(x)
        except ValueError:
            x = ord(x)-87
            l.append(x)
    return l



def la_llista(max_number):
    llista = []
    for j in range(0,max_number):
            hashi = get_block_info()["data"][j]["hash"]
            u = [x for x in hashi[19:]]
            
            def all_numbers(li):
                l=[]
                for x in li:
                    try:
                        x = int(x)
                        l.append(x)
                    except ValueError:
                        x = ord(x)-87
                        l.append(x)
                return l
            llista.append(all_numbers(u))  
    return llista

def la_llista_ether(max_number):
    llista = []
    for j in range(0,max_number):
            hashi = get_block_ether()["data"][j]["hash"]
            u = [x for x in hashi[1:]]
            
            def all_numbers(li):
                l=[]
                for x in li:
                    try:
                        x = int(x)
                        l.append(x)
                    except ValueError:
                        x = ord(x)-87
                        l.append(x)
                return l
            llista.append(all_numbers(u))  
    return llista


    

