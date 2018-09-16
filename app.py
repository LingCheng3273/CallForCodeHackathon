import os
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

#list of all suppliers format [{'company': "company1",'contact': "company1@gmail.com" , 'comptype': "supplier", 'location':"USA", "item":"Water"}]
suppliers = [
        {'company': "company1",'contact': "company1@gmail.com" , 'comptype': "supplier", 'location':"USA", 'item':"Water"}
    ]
#list of all requesters format [{'company': "company2",'contact': "company2@gmail.com" , 'comptype': "requester" , 'location':"USA", "item":"Food"}]
requesters = [
        {'company': "company2",'contact': "company2@gmail.com" , 'comptype': "requester", 'location':"USA", 'item':"Food"}
    ]

#index page
@app.route("/")
def index():
    user = 'tommy'
    return render_template('index.html')


#list of all suppliers or requesters
@app.route("/post", methods = ['POST', 'GET'])
def post():
    # add posted people to requesters or suppliers list
    company = request.form.get('company')
    contact = request.form.get('contact')
    comptype = request.form.get('comptype')
    location = request.form.get('location')
    #add a new post for every item supplied/requested
    items = []
    if request.form.get('item1'):
        items.append(request.form.get('item1'))
    if request.form.get('item2'):
        items.append(request.form.get('item2'))
    if request.form.get('item3'):
        items.append(request.form.get('item3'))
    
    #print "company {}".format( company)
    #print "contact {}".format( contact)
    #print "comptype {}".format( comptype)
    #print "item{}".format(item)
        
    #if person is a supplier, add person to suppliers list and
    #render the page of requesters who need the supplies
    if comptype == "supplier":
        for i in items:
            if i != 0:
                item_requests= []
                suppliers.append({'company': company, 'contact': contact, 'comptype': comptype, 'location': location, 'item': i})
                for requester in requesters:
                    if requester['item'] == i:
                        item_requests.append(requester)
        return render_template('supplier.html', requesterlist= item_requests)

    #person must be a requester, so add person to requesters list and
    #render the page of suppliers who have the supplies
    for i in items:
        if i != 0:
            item_supplies= []
            requesters.append({'company': company, 'contact': contact, 'comptype': comptype, 'location': location, 'item': i})
            for supplier in suppliers:
                    if supplier['item'] == i:
                        item_supplies.append(supplier)
        return render_template('requester.html', supplierlist= item_supplies)
    #return redirect("/", code=302)



    

port=os.getenv('PORT', '5000')
if __name__=="__main__":
    app.run(host='0.0.0.0',port=int(port))
