import os
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

#list of all suppliers format [{'company': "company1",'contact': "company1@gmail.com" , 'comptype': "supplier", 'location':"USA", "item":"Water"}]
suppliers = [
        {'company': "Red Cross",'contact': "redcross@gmail.com" , 'comptype': "supplier", 'location':"USA", 'item':"Water"},
        {'company': "Red Cross",'contact': "redcross@gmail.com" , 'comptype': "supplier", 'location':"USA", 'item':"Food"},
        {'company': "Moving Company",'contact': "move@gmail.com" , 'comptype': "supplier", 'location':"Puerto Rico", 'item':"Transport"},
        {'company': "Relief Organization",'contact': "relief@gmail.com" , 'comptype': "supplier", 'location':"Dominican Republic", 'item':"Water"},
        {'company': "Relief Organization",'contact': "relief@gmail.com" , 'comptype': "supplier", 'location':"Dominican Republic", 'item':"Food"}
        
    ]
#list of all requesters format [{'company': "company2",'contact': "company2@gmail.com" , 'comptype': "requester" , 'location':"USA", "item":"Food"}]
requesters = [
    {'company': "Shelter",'contact': "shelter@gmail.com" , 'comptype': "requester", 'location':"Puerto Rico", 'item':"Water"},
        {'company': "Shelter",'contact': "shelter@gmail.com" , 'comptype': "requester", 'location':"Puerto Rico", 'item':"Food"}
    ]

#home page. Can go to register page or browse page
@app.route("/")
def home():
    return render_template('test_home.html')

#register page. Can go to supplier or requester page
@app.route("/index", methods = ['POST'])
def register():
    return render_template('test_index.html')

#
@app.route("/browse_index", methods = ['GET'])
def browse_index():
    return render_template('test_browse_index.html')

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
        return render_template('test_browse.html', a_list= item_requests, result= "Requesters")
    else:
        item_supplies = []
        for i in items:
            if i != 0:
                for supplier in suppliers:
                    if supplier['item'] == i:
                        if not supplier in item_supplies:
                            item_supplies.append(supplier)
        return render_template('test_browse.html', a_list= item_supplies, result= "Suppliers")

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
        return render_template('test_supplier.html', requesterlist= item_requests)

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
    return render_template('test_requester.html', supplierlist= item_supplies)

@app.route("/")
def returnHome():
    return redirect("/", code=302)



    

port=os.getenv('PORT', '5000')
if __name__=="__main__":
    app.run(host='0.0.0.0',port=int(port))
