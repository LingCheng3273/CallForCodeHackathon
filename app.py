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
    return render_template('home.html')


@app.route("/index", methods = ['POST'])
def index_page():
    return render_template('index.html')

@app.route("/browse_index", methods = ['GET'])
def browse_index():
    return render_template('browse_index.html')

@app.route("/browse", methods = ['POST'])
def browse():
    comptype = request.form.get('comptype')

    items = []
    for i in range(3):
        i = i+1   # form numbers start at 1
        if request.form.get('item' + str(i)):
            items.append(request.form.get('item' + str(i)))

    if comptype == "requests":
        item_requests = []
        for i in items:
            if i != 0:
                for requester in requesters:
                    if requester['item'] == i:
                        if not requester in item_requests:
                            item_requests.append(requester)
        return render_template('browse.html', a_list= item_requests, result= "Requesters")
    else:
        item_supplies = []
        for i in items:
            if i != 0:
                for supplier in suppliers:
                    if supplier['item'] == i:
                        if not supplier in item_supplies:
                            item_supplies.append(supplier)
        return render_template('browse.html', a_list= item_supplies, result= "Suppliers")

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
    for i in range(3):
        i = i+1   # form numbers start at 1
        if request.form.get('item' + str(i)):
            items.append(request.form.get('item' + str(i)))

    #print "company {}".format( company)
    #print "contact {}".format( contact)
    #print "comptype {}".format( comptype)
    #print "item{}".format(item)
        
    #if person is a supplier, add person to suppliers list and
    #render the page of requesters who need the supplies
    if comptype == "supplier":
        item_requests = []
        for i in items:
            if i != 0:
                suppliers.append({'company': company, 'contact': contact, 'comptype': comptype, 'location': location, 'item': i})
                for requester in requesters:
                    if requester['item'] == i:
                        if not requester in item_requests:
                            item_requests.append(requester)
        return render_template('supplier.html', requesterlist= item_requests)

    #person must be a requester, so add person to requesters list and
    #render the page of suppliers who have the supplies
    else:
        item_supplies = []
        for i in items:
            if i != 0:
                requesters.append({'company': company, 'contact': contact, 'comptype': comptype, 'location': location, 'item': i})
                for supplier in suppliers:
                    if supplier['item'] == i:   #If the supplier has the item you desire
                        if not supplier in item_supplies: #If supplier isn't on the table, add him to it
                            item_supplies.append(supplier)
    return render_template('requester.html', supplierlist= item_supplies)
#return redirect("/", code=302)



    

port=os.getenv('PORT', '5000')
if __name__=="__main__":
    app.run(host='0.0.0.0',port=int(port))
