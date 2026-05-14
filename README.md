# CarHelper

## Project Description

CarHelper is a Django-based web app built for people who drive cars but don't always know what's wrong with them.

The idea came from a pretty common problem that everyone gets once in a while. When something feels off with your car, you have no idea if it's serious, and every answer you find online is either buried in reddit or its in a hard to find website with little information. CarHelper aims to fix that by putting all this data into one platform that combines a community discussion forum with structured vehicle information and reliability ratings.

Users can add their vehicles, post about issues they're having, and get input from other drivers who may have encountered the same problem. There's also a vehicle lookup tool that pulls real specs from the NHTSA database using a VIN, and a community-driven rating system that evaluates vehicles across multiple categories including reliability, repairability, fuel efficiency, and parts availability.


## Minimum Viable Product (MVP)

The Minimum Viable Product (MVP) focuses on solving the core problem:

> Helping vehicle owners understand vehicle issues and access basic vehicle information.

The MVP version of the application includes the following core functionality:

- User authentication (account registration and login)
- Ability for users to add, manage, and delete their vehicles (year, make, model, VIN, photo)
- A bulletin board where users can post vehicle-related issues with category tags
- Comment threads for community troubleshooting and discussion
- A rating system that allows users to rate vehicles across multiple categories
- A vehicle lookup tool powered by the NHTSA API
- An issue frequency tracker showing the most commonly reported problems by vehicle and category

## Features

### 1. Bulletin Board (Vehicle Issues Forum)

The platform includes a community bulletin board where users can post issues they are experiencing with their vehicles.

Features include:

- All community posts visible on the home page
- Tag filtering system for issues:
  - Engine
  - Transmission
  - Electrical
  - Suspension
  - Other
- Comment threads for troubleshooting discussions
- Post authors can delete their own posts

### 2. Vehicle Lookup Page

Users can search for their vehicle using a VIN number.

The lookup page displays key vehicle specifications retrieved from the NHTSA public API including:

- Make, Model, and Year
- Engine displacement (L) and cylinder count
- Fuel type
- Transmission style
- Drive type
- Vehicle type

### 3. Vehicle Rating System

Users can rate vehicles using a 1–5 scale across multiple categories.

Rating categories include:

- Mechanical reliability
- Cost of ownership
- Repairability
- Fuel efficiency
- Parts availability
- DIY capability
- Resale value

Each user can submit one rating per vehicle and update it at any time.

### 4. Issue Frequency Tracker

The issue tracker displays vehicles ranked by number of community reports, broken down by issue category. This helps users identify common problems associated with specific makes and models.

Example:

> "2011 Nissan Versa — Transmission — 4 reports"

### 5. Garage Management

Users can:

- Add vehicles with make, model, year, VIN, and an optional photo
- View all their registered vehicles on the home page
- Delete vehicles they no longer own

## Development Methodology (Agile)

This project followed Agile development methodology with weekly sprints. Each sprint focused on delivering a functional feature or improvement to the application.

### Sprint Plan

**Sprint 1**
- Project setup
- Repository creation
- Development environment configuration
- Initial README documentation

**Sprint 2**
- Implement user authentication (registration and login)

**Sprint 3**
- Create vehicle model and allow users to add and manage vehicles

**Sprint 4**
- Implement bulletin board post creation

**Sprint 5**
- Implement comment system for posts

**Sprint 6**
- Add basic vehicle rating system

**Sprint 7**
- Implement vehicle lookup functionality using the NHTSA API

**Sprint 8**
- Add filtering and tagging system for posts

**Sprint 9**
- Expand vehicle rating categories

**Sprint 10**
- Implement issue frequency tracking

**Sprint 11**
- Testing, debugging, UI cleanup, image upload support, delete functionality

## Environment Setup

Clone the repository:

```bash
git clone https://github.com/roen-lerma/carhelper.git
cd CarHelper
```

Create and activate a virtual environment:

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Apply migrations and run the server:

```bash
python manage.py migrate
python manage.py runserver
```

To access the admin panel, create a superuser:

```bash
python manage.py createsuperuser
```

Then go to `http://127.0.0.1:8000/admin/`
