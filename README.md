# Book Review System

## Description
The **Book Review System** is a **Flask-based web application** that allows users to **add, view, update, and delete book reviews**. It utilizes **MongoDB (PyMongo)** for data storage, ensuring efficient handling of book details and user-generated reviews. The system provides a user-friendly interface for managing book reviews while supporting multiple genres and authors.

## Features
- **Add Reviews**: Users can submit book reviews with details such as book name, author, rating, and review text.
- **View Reviews**: Search for books and display their reviews in an organized format.
- **Update Reviews**: Modify an existing review by replacing the old entry with an updated version.
- **Delete Reviews**: Remove specific reviews from the database.
- **MongoDB Integration**: Data is stored efficiently using PyMongo for seamless retrieval and updates.

## Technologies Used
- **Backend**: Flask (Python 3.12)
- **Database**: MongoDB (PyMongo)
- **Frontend**: HTML5, Jinja2

## Installation & Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/book-review-system.git
   cd book-review-system
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Start MongoDB (ensure it's running on `localhost:27017`).
5. Run the Flask application:
   ```sh
   python app.py
   ```
6. Open the application in your browser at `http://127.0.0.1:5000/`.

## Future Enhancements
- Implement **user authentication** for personalized review management.
- Add **pagination** for better navigation of book reviews.
- Develop **API endpoints** to enable third-party integration.


