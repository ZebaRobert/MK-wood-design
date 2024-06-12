# MKWoodDesign

## Introduction
MKWoodDesign is a website dedicated to showcasing the exquisite craftsmanship of the company that goes by the same name. This project aims to provide a seamless user experience while highlighting the artistry and versatility of custom furniture crafted from wood. MKWoodDesign offers a platform to explore past projects, connect with the artisan, and inquire about personalized collaborations.

## Table of Contents
1. [Introduction](#introduction)
2. [User Experience Design (UX)](#user-experience-design-ux)
    - [The Strategy Plane](#the-strategy-plane)
    - [Epics](#epics)
    - [User Stories](#user-stories)
    - [The Scope Plane](#the-scope-plane)
    - [The Skeleton Plane](#the-skeleton-plane)
        - [Wireframe mock-ups](#wireframe-mock-ups)
        - [Database Schema](#database-schema)
    - [The Surface Plane](#the-surface-plane)
        - [Design](#design)
        - [Typography](#typography)
        - [Images](#images)
4. [Future Enhancements](#future-enhancements)
5. [Testing](#testing)
    - [Testing Strategy](#testing-strategy)
    - [Validator Testing](#validator-testing)
    - [Notable Bugs](#notable-bugs)
6. [Technologies Used](#technologies-used)
    - [Packages Used](#packages-used)
    - [Resources Used](#resources-used)
7. [Deployment](#deployment)
    - [Project Deployment](#project-deployment)
8. [Credits](#credits)


## User Experience Design (UX)

[Screenshot of homepage](/docs/readme/home-page.jpg)

[View the live website on Heroku](https://mk-wood-design-0418729d9865.herokuapp.com/)

Please note: To open any links in this document in a new browser tab, please press CTRL + Left Click.

## UX
### The Strategy Plane

MKWoodDesign aims to offer users an immersive experience by providing comprehensive insights into the company's background and its owner. The primary objectives include:
- **Company Insight**: Users can learn more about the company's ethos, values, and the artisan behind the craftsmanship.
- **Portfolio Showcase**: Users can explore the diverse range of custom woodwork offered by the company.
- **Feedback Mechanism**: A platform is provided for users to leave comments and ratings based on their experiences with the company's services.
- **Collaboration Facilitation**: Users can easily initiate contact with the company for potential collaborations and bespoke projects.

This strategic approach ensures that MKWoodDesign serves as both an informative resource and a gateway for prospective clients to engage with the company's offerings effectively.

#### Epics

7 Epics were created which were then further developed into 24 User Stories. The details on each epic, along with the user stories linked to each one can be found in the project kanban board [here](https://github.com/users/ZebaRobert/projects/2/views/1)

1. Initial Setup [#17](https://github.com/ZebaRobert/MK-wood-design/issues/17)
2. User Profile Page [#21](https://github.com/ZebaRobert/MK-wood-design/issues/21)
3. User Experience Enhancements [#28](https://github.com/ZebaRobert/MK-wood-design/issues/28)
4. Contact Page [#31](https://github.com/ZebaRobert/MK-wood-design/issues/31)
5. Comment Section [#33](https://github.com/ZebaRobert/MK-wood-design/issues/33)
6. Basic Website Components [#38](https://github.com/ZebaRobert/MK-wood-design/issues/38)
7. Documentation[#45](https://github.com/ZebaRobert/MK-wood-design/issues/45)

### User Stories

From the Epics, 24 User stories were developed. Each story was assigned a classification of Must-Have, Should-Have, Could-Have or Won't Have. The full list of User Stories, seperated by those completed and those pushed to a future release is available on the project [kanban board](https://github.com/users/ZebaRobert/projects/2/views/1).

### The Scope Plane

**Features planned:**
* User Profile - Create, Read, Update and Delete
* Comment Section - Users can leave feedback for the company 
* Comments Editing - Users can edit/delete their comments on the Profile Page
* Comment Moderation - Admin can moderate the comment section to hide/block user comments that are inappropriate
* Gallery Section - Owner can display their past project and users can see them
* Home/About Page - User can learn about the company its motives and the owner from small but comprehensive text sections 
* Responsive Design - the site needs to be fully responsive to cover the wide variety of devices users may use to access a recipe site
* Alternative color themes and languages


### The Skeleton Plane
#### Wireframe mock-ups

* Home page:
    1. The home page provides the user with information about the company, its owner and goals.
    2. Users are gretted by a worm welcome message and a hero banner.

![Home Page Wireframe](/docs/wireframe/wireframe-home.jpg)

* Gallery Page:
  1. Users can see a gallery of images from companys previos projects.
  2. Under the gallery section useres will find the comment section
  3. Users can leave feedback about the company in the comment section
  4. Users can see feedback from other users in the comment section

![Gallery Page Wireframe](/docs/wireframe/wireframe-gallery.jpg)

* Contact Page:
  1. User can fill out the contact form to get in touch with the company
  2. Users can find all of the contact information as well as the location of the company under the contact form

![Contact Form Wireframe](/docs/wireframe/wireframe-contact.jpg)

* Login / Register Pages:
  1. User can Login with existing account via login form or create an account via register form

![Login Page Wireframe](/docs/wireframe/wireframe-login.jpg)

* Profile Page:
  1. User can see their information and preform full CRUD on their profile
  2. User can see the history of thair interactions with the web site and preform full CRUD functionaly on their comments

![Profile Page Wireframe](/docs/wireframe/wireframe-profile.jpg)

#### Database Schema

Several custom models were predicted to be required when building the site. With the intention to utilise AllAuth for the user authentication system, which utilises the built in Django User Model.

![Database Schema Diagram](/docs/readme/1)
![Database Schema Diagram](/docs/readme/2)
![Database Schema Diagram](/docs/readme/3)

### The Surface Plane

#### Design

The color pallet was chosen using [Coolors.co](https://coolors.co/) website to mix and match what suited best for the website. These 5 colors have been chosen :
    
    Rich Walnut Brown (#4A2C2A): This deep brown color mimics the natural tones of wood and conveys a sense of quality and sturdiness.
    Soft Cream (#F5F5DC): A light, creamy color that was used for backgrounds to keep the site feeling airy and open while complementing the darker tones.
    Forest Green (#228B22): A muted green that reflects nature and sustainability, ideal for accents and buttons.
    Warm Amber (#FFBF00): A warm, golden hue that was used to draw attention to key areas like calls-to-action and highlights.
    Slate Gray (#708090): A cool, neutral gray that balances the warmer tones and can be used for text and secondary elements.

#### Typography

The default font used throughout the site for paragraphs, sections, spans, and other text elements is **Noto Serif**. For headings, titles, and other prominent text, the **Play** font has been utilized to ensure a clear hierarchy and enhance readability.

#### Images

The images on the site come from two primary sources: the company owner’s personal collection and a selection from Unsplash, ensuring a blend of authentic and high-quality visuals.


## Future Enhancements

1. Dark / light toggle
2. Language toggle
3. Admin controle
4. Visual enhancements

## Testing

### Testing Strategy
I employed a manual testing strategy during the development of the site. A comprehensive breakdown of the testing procedures and methodology is available in the testing.md file, accessible [here](TESTING.md).

In addition to functionality testing and code testing, User Story tests were implemented to verify the fulfillment of acceptance criteria outlined in the user stories.

#### Validator Testing
All code files were validated using suitable validators for the specific language. The full details can be found in the testing.md file.

#### Notable Bugs

##### Unsloved Bugs

1. If the user is not logged in at the time he opens the gallery page a pop up message will show thanking the user for leaving feedback even thou non was left.
   
#### Technologies Used

* Python
    * The following python modules were used on this project:
        * asgiref==3.7.2
        * bleach==6.1.0
        * certifi==2023.11.17
        * cffi==1.16.0
        * charset-normalizer==3.3.2
        * cloudinary==1.38.0
        * crispy-bootstrap5==2023.10
        * cryptography==42.0.2
        * defusedxml==0.7.1
        * dj-database-url==2.1.0
        * dj3-cloudinary-storage==0.0.6
        * Django==5.0.1
        * django-allauth==0.60.1
        * django-crispy-forms==2.1
        * django-heroku==0.3.1
        * django-summernote==0.8.20.0
        * gunicorn==21.2.0
        * idna==3.6
        * oauthlib==3.2.2
        * packaging==23.2
        * psycopg2==2.9.9
        * pycparser==2.21
        * PyJWT==2.8.0
        * python3-openid==3.2.0
        * requests==2.31.0
        * requests-oauthlib==1.3.1
        * six==1.16.0
        * sqlparse==0.4.4
        * typing_extensions==4.9.0
        * tzdata==2023.4
        * urllib3==2.2.0
        * webencodings==0.5.1
        * whitenoise==6.6.0 

* Django
    * Django was used as the main python framework in the development of this project
    * Django AllAuth was utilised to provide enhanced user account management functionality.
* Heroku
    * Was used as the cloud based platform to deploy the site on
* Heroku PostgreSQL
    * Heroku PostgreSQL was used as the database for this project during development and in production.
* JavaScript
    * Custom JavaScript was utilised to enable the colour scheme functionality, the mobile menu, the enabling and disabling of buttons and forms .
* Bootstrap 5.13
    * Bootstrap was used for general layout and spacing requirements for the site.
* Font Awesome
    * Was used for access to several icons for different sections where icons were appropriate.
* CSS
    * Custom css was written for a large number of areas on the site to implement custom styling and escape a bootstrap look and feel to the site.
* Django Templating
    * Jinja/Django templating language was utilised to insert data from the database into the sites pages. It was also utilised to perform queries on different datasets.
* HTML
    * HTML was used as the base language for the templates created for the site.

#### Packages Used

* VS Code was used to develop the site
* Git was utilised for version control and transferring files between the code editor and the repository
* GitHub was utilised for storing the files for this project
* FIgma was utilised to develop wireframes for the site from which the design was based
* GIMP was used to adapt images for use within the site.
* DrawSQL.app was used to develop the database schema during development

#### Resources Used

* The Django documentation was used extensively during development of this project

## Deployment

The site was deployed via Heroku, and the live link can be found here - [MKWoodDesign]()

### Project Deployment

To deploy the project via Heroku, I followed these steps:

1. Sign up or log in to [Heroku](https://www.heroku.com/).
2. On the main Heroku Dashboard page, click on 'New' and then 'Create New App'.
3. Provide a name for the project (e.g., mk-wood-design) and select a suitable region, then click 'Create App'. Ensure the app name is unique.
4. This action creates the app within Heroku and directs you to the deploy tab. From there, navigate to the resources tab.
5. Add the database to the app by searching for 'Heroku Postgres' in the add-ons section. Select the appropriate package and add 'Heroku Postgres' as the database.
6. Go to the settings tab, then within the config vars section, copy the DATABASE_URL to the clipboard for later use in Django configuration.
7. Create a new file named env.py within the Django app repository. Inside this file, import the os library and set the environment variable for the DATABASE_URL by pasting the address copied from Heroku. The line should appear as `os.environ["DATABASE_URL"] = "Paste the link in here"`.
8. Add a secret key to the app using `os.environ["SECRET_KEY"] = "your secret key goes here"`.
9. Add the newly created secret key to the Heroku Config Vars as SECRET_KEY for the KEY value and the secret key value as the VALUE.
10. In the settings.py file within the Django app, import Path from pathlib, os, and dj_database_url.
11. Insert the line `if os.path.isfile("env.py"): import env`.
12. Remove the insecure secret key present by default in the Django settings file and replace it with `SECRET_KEY = os.environ.get('SECRET_KEY')`.
13. Replace the databases section with `DATABASES = {'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))}` and ensure correct Python indentation is used.
14. In the terminal, migrate the models to the new database connection.
15. In a browser, navigate to Cloudinary, log in or create an account if necessary. From the dashboard, copy the CLOUDINARY_URL to the clipboard.
16. In the env.py file created earlier, add `os.environ["CLOUDINARY_URL"] = "paste in the URL copied to the clipboard here"`.
17. In Heroku, add the CLOUDINARY_URL and its corresponding value to the config vars.
18. Also, add the KEY - DISABLE_COLLECTSTATIC with the Value - 1 to the config vars. This key-value pair must be removed before the final deployment.
19. Add the Cloudinary libraries to the list of installed apps, ensuring 'cloudinary_storage' is inserted above 'django.contrib.staticfiles' and 'cloudinary' below it.
20. In the Settings.py file, add the STATIC files settings including the URL, storage path, directory path, root path, media URL, and default file storage path.
21. Link the file to the templates directory in Heroku by setting TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates').
22. Change the templates directory to TEMPLATES_DIR - `DIRS': [TEMPLATES_DIR]`.
23. Add Heroku to the ALLOWED_HOSTS list in the format: app name given in Heroku followed by .herokuapp.com.
24. In your code editor, create two new top-level folders:static, and templates.
25. Create a new file in the top-level directory named Procfile.
26. Inside the Procfile, add the code: `web: gunicorn PROJECT_NAME.wsgi`.
27. In the terminal, add the changed files, commit, and push to GitHub.
28. In Heroku, navigate to the deployment tab and manually deploy the branch, monitoring the build logs for any errors.
29. Upon successful deployment, Heroku will provide a 'Your App Was Successfully Deployed' message and a link to visit the live site.


### Credits

I'd like to thank the following:    
* MattBCoding (Github Profile) and Gareth McGirr (Github Profile) for their incredible documentation, which I utilized to help shape my own readme.md and testing.md for this project. 
* My Code Institute Mentors Graeme Taylor and Mo Shami
