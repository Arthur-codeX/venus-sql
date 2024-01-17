from flask import Flask,request,render_template,redirect,url_for,send_file,jsonify,session

import os

relative_path='templates'

absolute_path=os.path.abspath(relative_path)

app=Flask(__name__,template_folder=absolute_path)

# puppies=['Sam The Puppy',"Johann pupp","Puppito"]

puppies=[{'name':'Same','age':1,'pic':'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.NPzYJ3fFAKLETImjg09lNQHaFS%26pid%3DApi&f=1&ipt=e7ef6c09b22bbcf28084ef72a32347e24f2dfac49559e5f2954a4395403de5c0&ipo=images'},
         {'name':'Jojo','age':2,'pic':'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%3Fid%3DOIP.KigzMvp3i4nlP-EQJlvrJAHaE7%26pid%3DApi&f=1&ipt=a9d8ac3b75cf6167a1f2a8c541d955143adfb3c5de7332889d4a0a7729c71652&ipo=images'}]

@app.route("/")
def index():
    return render_template('index.html',title='Home',head='This is Home',puppies=puppies)

@app.route("/puppy/<int:id>")
def singlePuppy(id):
    print(id)
    puppy=puppies[id-1]
    return render_template('single.html',puppy=puppy)

@app.route('/inherit')
def inherit():
    return redirect(url_for('index'))

@app.route("/add",methods=['GET','POST'])
def add():

    print(request.method)

    if request.method=='POST':
        print(request.form)
        name=request.form['name']
        image_url=request.form['img']
        puppies.append({
            'name':name,
            'pic':image_url
        })
        return redirect(url_for('index'))

    return render_template('add.html')


if __name__=='__main__':
    app.run(debug=True,port=1234)


# @app.route("/")
# def index():

#     puppy_list=""

#     for index,puppy in enumerate(puppies):
#         puppy_list=puppy_list+f'<li><a href="adopt/{index}">{puppy}</a></li>'

#     print(puppy_list)

#     template='''<!DOCTYPE html>
#         <html lang="en">
#         <head>
#             <meta charset="UTF-8" />
#             <meta name="viewport" content="width=device-width, initial-scale=1.0" />
#             <title>Home</title>
#         </head>
#         <body>
#             <h1>We have many Puppies Adopt One</h1>
#             <ul>
#               {}
#             </ul>
#         </body>
#         </html>'''

#     return template.format(puppy_list)

# @app.route('/adopt/<int:puppy_id>')
# def adopt(puppy_id):

#     print(puppy_id)

#     length=len(puppies)
#     print(length)

#     if puppy_id<0 or puppy_id>length:
#         return f'<h1>Puppy doesnt exist</h1>  <div> <a href="/"><h1>To Home</h1></a></div>'

#     template='''<!DOCTYPE html>
#         <html lang="en">
#         <head>
#             <meta charset="UTF-8" />
#             <meta name="viewport" content="width=device-width, initial-scale=1.0" />
#             <title>Home</title>
#         </head>
#         <body>
#             <h1>Adopt the puppy</h1>
#             <div>{}</div>
#         </body>
#         </html>'''

#     return template.format(puppies[puppy_id])
    

    # @app.route('/user')
# def user():
#     data={
#         'name':"John",
#         'age':34,
#     }
#     return jsonify(data)

# @app.route('/image')
# def image():
#     absolute_path=os.path.abspath('static/bob.jpg')
#     print(absolute_path)
#     return send_file(absolute_path,mimetype='image/jpeg',as_attachment=True)

# # Entry point for our app

