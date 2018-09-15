import os
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

database = [
        {'company': "company1",'contact': "company1@gmail.com" , 'comptype': "supplier" , "item":"Water"},
        {'company': "company2",'contact': "company2@gmail.com" , 'comptype': "requester" , "item":"Food"},
        ]

suppliers = [
        {'company': "company1",'contact': "company1@gmail.com" , 'comptype': "supplier" , "item":"Water"}
    ]
requesters = [
        {'company': "company2",'contact': "company2@gmail.com" , 'comptype': "requester" , "item":"Food"}
    ]


@app.route("/")
def hello():
    user = 'tommy'
    return render_template('index.html', data=database)


@app.route("/post", methods = ['POST', 'GET'])
def post():
    # get form data 

    # add posted data to database
    company = request.form.get('company')
    contact = request.form.get('contact')
    comptype = request.form.get('comptype')
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

    if comptype == "supplier":
        for i in items:
            if i != 0: 
                suppliers.append({'company': company, 'contact': contact, 'comptype': comptype, 'item': i})
        return render_template('supplier.html', requesterlist= requesters)
    
    for i in items:
        if i != 0: 
            requesters.append({'company': company, 'contact': contact, 'comptype': comptype, 'item': i})
        return render_template('requester.html', supplierlist= suppliers)
    #return redirect("/", code=302)



    

port=os.getenv('PORT', '5000')
if __name__=="__main__":
    app.run(host='0.0.0.0',port=int(port))
