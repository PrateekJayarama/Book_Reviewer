from flask import render_template,request,Flask, redirect
from pymongo import MongoClient

app=Flask(__name__)
client=MongoClient("mongodb://localhost:27017/")
db=client['Book_Reviews']
collect=db['Books']

@app.route('/')
def home():

	return render_template('index.html')

@app.route('/create', methods=['GET', 'POST'])
def add_review():
    if request.method == 'POST':
        b_name = request.form['book_name'].lower()
        b_result = collect.find_one({'book_name': b_name}, {'book_name': 1, '_id': 0})

        a_name = request.form['author_name'].lower()
        genre = request.form['genre'].lower()
        rating = request.form['rating']
        name = request.form['name'].lower()
        review = request.form['book_review'].lower()

        genre_list = genre.split(', ') if ',' in genre else [genre]

        if b_result and b_result.get('book_name', '').lower() == b_name:
            collect.update_one({'book_name': b_name}, {'$push': {'reviews': {'name': name, 'rating': rating, 'review': review}}})
        else:
            collect.insert_one({'book_name': b_name, 'author_name': a_name, 'genre': genre_list, 'reviews': [{'name': name, 'rating': rating, 'review': review}]})

    return render_template('add_review.html')


@app.route('/read',methods=['GET'])
def view_review():
	books=collect.find()
	if request.method=='GET':
		search_q=request.args.get("search")
		if search_q:
			b_result = collect.find_one({'book_name': search_q}, {'book_name': 1, '_id': 0})
			if b_result and b_result.get('book_name','') ==search_q:
				return render_template('book_details.html',book=search_q)
			return 'book not found' , 404
	return render_template('view_review.html',books=books)

@app.route('/update',methods=['GET','POST'])
def update_review():
	if request.method == 'POST':
		b_name = request.form['book_name'].lower()
		name=request.form['name'].lower()
		rating=request.form['rating']
		review=request.form['book_review'].lower()
		book=collect.find({'book_name': b_name, 'reviews.name': name})
		if book:
			result=collect.update_one({'book_name': b_name}, {'$pull': {'reviews':{'name': name}}})
			result=collect.update_one({'book_name': b_name}, {'$push': {'reviews':{'name':name,'rating': rating, 'review': review}}})
			if result.modified_count==0:
				return 'review not found or no updates made!'
		return redirect('/read')
	return render_template('update_review.html')

@app.route('/delete',methods=['GET','POST'])
def delete_review():
	if request.method == 'POST':
		b_name=request.form['book_name'].lower()
		name=request.form['name'].lower()
		result=collect.update_one({'book_name':b_name},{'$pull': {'reviews':{'name':name}}})
		if result.modified_count==0:
			return 'Your review has been deleted or not found', 404
	return render_template('delete_review.html')

if __name__=="__main__":
	app.run(debug=True)
