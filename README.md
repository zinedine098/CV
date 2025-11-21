# Online Course Platform

Welcome to the Online Course Platform - a comprehensive Django-based web application designed to deliver online education with a focus on user experience and course management.

## Project Overview

This project is an online learning platform built with Django that allows students to browse courses, connect with instructors, and access educational content. The platform features a responsive design with modern UI elements and comprehensive course management capabilities.

## Current Progress & Features

### Core Structure
- **Django Project**: Built with Django 5.2.8
- **Database**: SQLite3 for development
- **Template System**: Django templating with base.html inheritance
- **Static Files**: Comprehensive asset management with Bootstrap-based design

### UI & Design
- **Responsive Layout**: Mobile-first design using Bootstrap 5.3.7
- **Modern Template**: "Learner" template with professional aesthetics
- **Static Assets**: CSS, JavaScript, images, and vendor libraries properly organized
- **Frontend Framework**: Bootstrap with custom CSS and JavaScript functionality

### Landing Page Features
- **Hero Section**: Engaging introduction with statistics and call-to-action buttons
- **Featured Courses**: Display of courses with details (level, duration, instructor, ratings)
- **Course Categories**: Comprehensive categorization with 18+ subject areas
- **Featured Instructors**: Professional profiles with ratings and course counts
- **Testimonials**: Student feedback system with rating display
- **Blog Section**: Recent posts with author information
- **Call-to-Action**: Enrollment section with key statistics

### Navigation & User Experience
- **Main Navigation**: Complete menu with Home, About, Courses, Instructors, Pricing, Blog
- **Dropdown Menus**: Extended navigation options for detailed content access
- **Responsive Design**: Mobile navigation toggle and responsive layouts
- **Social Media Integration**: Links to Twitter, Facebook, Instagram, LinkedIn

### Functionality Implemented
- **URL Routing**: Clean URL structure with Django URL patterns
- **View System**: Basic view implementation for landing page
- **Template Inheritance**: Base template with block structure for content
- **Static File Management**: Proper Django static file handling

### Technology Stack
- **Backend**: Django 5.2.8
- **Frontend**: HTML5, CSS3, JavaScript with Bootstrap 5
- **Database**: SQLite3
- **Template Engine**: Django Templates
- **CSS Framework**: Bootstrap with custom styling
- **JavaScript Libraries**: AOS, Swiper, PureCounter for interactive elements

### Course Management Features
- **Course Categories**: 18+ categories including Computer Science, Business, Design, Health, Languages, etc.
- **Course Display**: Detailed course cards with pricing, difficulty level, duration, and instructor information
- **Rating System**: Visual star ratings and numerical scores
- **Student Statistics**: Enrollment data and success metrics

### Instructor Management
- **Instructor Profiles**: Detailed profiles with specialties, ratings, and course counts
- **Social Media Integration**: Links to instructor professional networks
- **Performance Metrics**: Student counts and rating displays

## Application Structure

```
online_course/
├── config/                 # Django project settings
│   ├── settings.py         # Project configuration
│   ├── urls.py            # Main URL routing
│   └── wsgi.py            # WSGI application
├── landing/               # Main application
│   ├── views.py           # View functions
│   ├── urls.py            # App-specific URLs
│   ├── models.py          # Database models (empty for now)
│   └── admin.py           # Admin interface configuration
├── templates/             # HTML templates
│   ├── base.html          # Base template with layout
│   └── landing/           # Landing page templates
├── static/                # Static assets
│   └── assets/            # CSS, JS, images, vendors
└── db.sqlite3             # Database file
```

## Current Status

✅ **Completed Components:**
- Basic Django project structure
- Landing page with full UI implementation
- Responsive design and mobile compatibility
- Static file management
- URL routing configuration
- Template inheritance system

🔄 **In Progress:**
- Database model development
- User authentication system
- Course enrollment functionality
- Instructor portal
- Student dashboard

## Future Development

 Planned Features:
- User authentication and authorization
- Course enrollment system
- Payment integration
- Student progress tracking
- Instructor dashboard
- Content management system
- Interactive learning materials
- Video streaming capabilities
- Discussion forums
- Quiz and assessment tools

## Setup Instructions

1. Clone the repository
2. Create virtual environment: `python -m venv venv`
3. Activate virtual environment: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install django`
5. Run migrations: `python manage.py migrate`
6. Start development server: `python manage.py runserver`
7. Visit `http://127.0.0.1:8000/` to view the application

## Contributing

We welcome contributions to enhance the functionality and features of this online course platform. Please feel free to submit pull requests or create issues for bugs and feature requests.
