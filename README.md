# MinMedia 🚀

A modern, responsive social media platform built with Django. Share your moments with beautiful posts, interact with likes and comments, and connect with others through personalized profiles.

![Django](https://img.shields.io/badge/Django-5.2.9-green.svg)
![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-4.6.2-purple.svg)

## ✨ Features

### 🔐 User Authentication
- **Sign Up**: Create your account with username, email, and password
- **Login/Logout**: Secure authentication system
- **User Profiles**: Customizable profiles with avatars and bio

### 📸 Post Management
- **Create Posts**: Share your thoughts with captions
- **Multiple Images**: Upload multiple images per post
- **Image Carousel**: Beautiful Bootstrap carousel for browsing multiple images
- **Feed View**: Scroll through all posts in a modern feed layout

### ❤️ Social Interactions
- **Like Posts**: Express your appreciation with likes
- **Comments**: Engage with others through comments
- **Real-time Updates**: AJAX-powered interactions without page refresh

### 🎨 Modern UI/UX
- **Dark Theme**: Sleek dark gradient background with glassmorphism effects
- **Responsive Design**: Fully responsive, works perfectly on mobile, tablet, and desktop
- **App-like Experience**: Non-zoomable viewport, optimized for mobile devices
- **Smooth Animations**: Beautiful transitions and hover effects
- **Modern Cards**: Glassmorphic card designs with gradient accents

## 🛠️ Tech Stack

- **Backend**: Django 5.2.9
- **Frontend**: HTML5, CSS3, JavaScript
- **UI Framework**: Bootstrap 4.6.2 (for carousel)
- **JavaScript Library**: jQuery 3.6.0
- **Database**: SQLite (default, can be changed to PostgreSQL/MySQL)
- **Font**: Inter (Google Fonts)

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd MinMed
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install django
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser** (optional, for admin access)
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Open your browser and navigate to `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

## 📁 Project Structure

```
MinMed/
├── MinMed/              # Main project directory
│   ├── settings.py      # Django settings
│   ├── urls.py          # URL configuration
│   ├── wsgi.py          # WSGI config
│   └── asgi.py          # ASGI config
├── users/               # Main app
│   ├── models.py        # Database models (Post, PostImage, Comments, ExtraUserInfo)
│   ├── views.py         # View functions
│   ├── admin.py         # Admin configuration
│   └── migrations/      # Database migrations
├── templates/           # HTML templates
│   ├── base.html        # Base template
│   ├── index.html       # Home feed page
│   ├── signin.html      # Login page
│   ├── signup.html      # Sign up page
│   ├── upload.html      # Create post page
│   ├── userpage.html    # User profile page
│   └── updateinfo.html  # Profile edit page
├── static/              # Static files
│   ├── css/
│   │   └── style.css    # Main stylesheet
│   └── js/
│       └── like.js      # Like functionality
├── media/               # User uploaded files
│   ├── avatars/         # Profile pictures
│   └── images/          # Post images
├── db.sqlite3           # SQLite database
└── manage.py            # Django management script
```

## 🎯 Key Features Explained

### Models
- **Post**: Stores post captions, creation time, and likes
- **PostImage**: Handles multiple images per post
- **Comments**: Stores user comments on posts
- **ExtraUserInfo**: Extended user information (bio, profile picture)

### Views
- `home_page`: Displays the main feed with all posts
- `signup_page`: User registration
- `login_page`: User authentication
- `upload_page`: Create new posts
- `profile`: View user profiles
- `like_post`: AJAX endpoint for liking posts
- `add_comment`: AJAX endpoint for adding comments
- `update_info`: Update user profile information

## 🎨 UI/UX Highlights

- **Dark Gradient Background**: Modern radial gradients with purple and pink accents
- **Glassmorphism**: Frosted glass effect on cards and navbar
- **Responsive Breakpoints**: Optimized for mobile (480px), tablet (768px), and desktop
- **Smooth Animations**: Hover effects, transitions, and micro-interactions
- **Full-Screen Layout**: Content stretches to fit screen perfectly
- **Touch Optimized**: Prevents zoom, optimized for mobile gestures

## 🔧 Configuration

### Media Files
Media files (images, avatars) are stored in the `media/` directory. Make sure `MEDIA_ROOT` and `MEDIA_URL` are properly configured in `settings.py`.

### Static Files
Static files (CSS, JS) are served from the `static/` directory. Run `python manage.py collectstatic` in production.

## 🚀 Deployment

For production deployment:

1. Set `DEBUG = False` in `settings.py`
2. Configure `ALLOWED_HOSTS`
3. Set up a production database (PostgreSQL recommended)
4. Configure static file serving
5. Set up proper media file storage (AWS S3, etc.)
6. Use environment variables for `SECRET_KEY`

## 📝 Usage

1. **Sign Up**: Create a new account at `/signup`
2. **Login**: Access your account at `/login`
3. **Create Post**: Click "Create" in navbar or go to `/upload`
4. **View Feed**: Browse all posts on the home page
5. **Like Posts**: Click the heart icon to like/unlike posts
6. **Comment**: Click "Comment" button and add your thoughts
7. **View Profile**: Click on usernames or go to `/profile/<username>`
8. **Edit Profile**: Update your bio and profile picture

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Built with ❤️ using Django

## 🙏 Acknowledgments

- Django Framework
- Bootstrap for carousel components
- Google Fonts (Inter)
- jQuery for AJAX functionality

---

**Note**: This is a development project. Make sure to configure proper security settings before deploying to production.
