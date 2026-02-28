# Library Management System

A full-stack Library Management System built with Django (REST API) and React.js.

## Features

### Backend (Django REST Framework)
- **Book Management**: Add, view, edit, and delete books
- **Member Management**: Student and Librarian roles
- **Borrow/Return System**: Track book borrowing and returns
- **Penalty Calculation**: Automatic penalty calculation for late returns
- **Token-based Authentication**: Secure API access

### Frontend (React.js)
- **User Authentication**: Login and Registration for students and librarians
- **Book Catalog**: Browse available books with cover images
- **Search & Filter**: Search books by title/author and filter by genre
- **Book Details**: View detailed book information
- **Borrow Books**: Borrow books with expected return date
- **Return Books**: Return borrowed books with penalty tracking
- **Responsive Design**: Modern, mobile-friendly UI

## Tech Stack

### Backend
- Django 4.x
- Django REST Framework
- SQLite Database
- Token Authentication

### Frontend
- React.js
- Axios for API calls
- CSS3 with custom styling

## Installation & Setup

### Prerequisites
- Python 3.8+
- Node.js 14+
- npm or yarn

### Backend Setup

1. Navigate to the project directory:
```
bash
cd library_system
```

2. Create a virtual environment:
```
bash
python -m venv venv
```

3. Activate the virtual environment:
```
bash
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

4. Install dependencies:
```
bash
pip install django djangorestframework django-cors-headers
```

5. Run migrations:
```
bash
python manage.py migrate
```

6. Create a superuser (optional):
```
bash
python manage.py createsuperuser
```

7. Run the development server:
```
bash
python manage.py runserver
```

The API will be available at `fetch(`${process.env.REACT_APP_API_URL}/api/books/`)`

### Frontend Setup

1. Navigate to the frontend directory:
```
bash
cd library-frontend
```

2. Install dependencies:
```
bash
npm install
```

3. Start the development server:
```
bash
npm start
```

The frontend will be available at `https://my-project-5fi1.onrender.com`

## API Endpoints

### Authentication
- `POST /api/register/` - Register a new student
- `POST /api/register/librarian/` - Register a new librarian
- `POST /api/login/` - Login and get auth token

### Books
- `GET /api/books/` - List all books
- `POST /api/books/` - Create a new book (requires auth)
- `GET /api/books/{id}/` - Get book details
- `PUT /api/books/{id}/` - Update book (requires auth)
- `DELETE /api/books/{id}/` - Delete book (requires auth)

### Members
- `GET /api/members/` - List all members (requires auth)
- `POST /api/members/` - Create a new member (requires auth)

### Borrow Records
- `GET /api/borrows/` - List user's borrow records
- `POST /api/borrows/` - Borrow a book
- `POST /api/borrows/{id}/return_book/` - Return a book

## Project Structure

```
library_system/
├── library/                 # Django app
│   ├── migrations/          # Database migrations
│   ├── admin.py            # Django admin configuration
│   ├── models.py           # Database models
│   ├── serializers.py      # DRF serializers
│   ├── urls.py             # URL routing
│   └── views.py            # API views
├── library_system/         # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── library-frontend/       # React frontend
│   └── src/
│       ├── App.js
│       ├── BookList.js
│       ├── BookDetail.js
│       ├── BorrowForm.js
│       ├── BorrowedBooks.js
│       ├── Login.js
│       └── Register.js
├── db.sqlite3             # SQLite database
└── manage.py              # Django management script
```

## Usage

1. Start the Django backend server
2. Start the React frontend server
3. Open your browser and navigate to `fetch(`${process.env.REACT_APP_API_URL}/api/books/`)`
4. Register a new student account or login
5. Browse the book catalog and borrow books
6. View your borrowed books and return them

## License

MIT License
