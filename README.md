# CarHelper
## Project Description

CarHelper is a Django-based web application designed to help vehicle owners understand mechanical issues, share troubleshooting advice, and view information about their vehicles.

Many drivers experience problems with their vehicles but do not know whether the issue is common, serious, or easily repairable. Information is often scattered across forums, manufacturer documentation, and various automotive websites. CarHelper aims to centralize this knowledge by combining a community discussion platform with structured vehicle information and reliability ratings.

The application will allow users to register vehicles, post questions about issues they are experiencing, and interact with other users who may have encountered similar problems. In addition to the discussion forum, the platform will include a vehicle lookup system that displays important specifications such as engine type, transmission, drivetrain, fuel type, oil capacity, and wheel size.

CarHelper will also include a community-driven rating system that evaluates vehicles across multiple categories including reliability, repairability, fuel efficiency, parts availability, and overall ownership experience. These ratings will help users compare vehicles and identify common issues associated with specific makes and models.

The goal of the project is to create a platform that makes vehicle knowledge more accessible while allowing users to learn from the experiences of other vehicle owners.
## Minimum Viable Product (MVP)

The Minimum Viable Product (MVP) focuses on solving the core problem:

> Helping vehicle owners understand vehicle issues and access basic vehicle information.

The MVP version of the application will include the following core functionality:

- User authentication (account registration and login)
- Ability for users to add and manage their vehicles (year, make, model)
- A bulletin board where users can post vehicle-related issues
- Comment threads for community troubleshooting and discussion
- A basic rating system that allows users to rate vehicles based on reliability and cost of ownership

The MVP will provide a functional prototype that allows users to share knowledge and seek advice from other vehicle owners.
## Planned Features

### 1. Bulletin Board (Vehicle Issues Forum)

The platform will include a community bulletin board where users can post issues they are experiencing with their vehicles.

Features include:

- Posts filtered by vehicle make and model
- Display of the top 5 most discussed models with an additional "Other" category
- Tagging system for issues such as:
  - Engine
  - Transmission
  - Electrical
  - Suspension
- Upvote and downvote system to highlight helpful answers
- Comment threads for troubleshooting discussions
### 2. Vehicle Lookup Page

Users will be able to search for their vehicle using either:

- VIN number  
or  
- Make / Model / Year

The lookup page will display key vehicle specifications including:

- Engine type
- Horsepower
- Transmission type
- Drivetrain
- Fuel type
- Oil capacity
- OEM wheel size

Vehicle data will be retrieved using external automotive APIs.
### 3. Vehicle Rating System

Users will be able to rate vehicles using a 1–5 star rating system across multiple categories.

Rating categories include:

- Repairability
- Mechanical reliability
- Fuel efficiency
- Parts availability
- DIY capability
- Resale value
- Interior quality
- Rust resistance

The system will calculate an overall reliability score based on these ratings.

Additional planned features include:

- Vehicle comparison tools for vehicles with similar value or ratings
- Issue frequency tracking that highlights common problems for specific vehicles

Example:

> "2011 Nissan Versa has a higher than average number of reports related to transmission failures."
## Development Methodology (Agile)

This project will follow Agile development methodology with weekly sprints throughout the semester. Each sprint will focus on delivering a functional feature or improvement to the application.

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
- Implement vehicle lookup functionality

**Sprint 8**
- Add filtering and tagging system for posts

**Sprint 9**
- Expand vehicle rating categories

**Sprint 10**
- Implement issue frequency tracking

**Sprint 11**
- Testing, debugging, and final improvements
## Environment Setup

Clone the repository:

```bash
git clone https://github.com/roen-lerma/carhelper.git
cd carhelper
python -m venv venv
# using windows
venv\Scripts\activate
# using mac/linux
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


