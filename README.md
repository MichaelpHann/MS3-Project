
# Commonplace | An Everyday Publishing Platform
 
Live application demo can be found [**here**](https://ms3-project-mph.herokuapp.com/)
 
## Table of Contents
 
1. [UX](#UX)
   * [Application overview](#Application-overview)
   * [User stories](#User-stories)
   * [Design choices](#Design-choices)
   * [Database Schema](#Database-schema)
   * [Wireframes](#Wireframes)
2. [Features](#Features)
   * [Existing features](#Existing-features)
   * [Future features](#Future-features)
3. [Technologies Used](#Technologies-Used)
4. [Testing](#Testing)
   * [Implemented features](#Implemented-features)
   * [Functionality](#Functionality)
   * [Bugs](#Bugs)
5. [Deployment](#Deployment)
6. [Credits](#Credits)
   * [Content sources](#Content-sources)
   * [Acknowledgements](#Acknowledgements)
 
 
_____
 
## UX
 
### Application overview

The purpose of this application is to provide the user with an everyday, user-friendly publishing platform. Thee application enables users to create their own profile, publish free-form content, browse for topics of interest and curate their favourite posts.
 
### User stories
* As a new user I want to be able to quickly and intuitively understand how the application works, how to navigate throughout it, and what I need to do to get registered and begin using the site.
* As a user who wants to consume content, I want to be able to browse a stream of blog posts covering a variety of topics, where I am able to identify the broad category of topic about which the post is written.
* As a user who wants to consume content, I want to be able to filter the stream of posts, searching by key-words of interest.
* As a user who wants to consume content, I want to be able to like my favourite posts and view them in one location at any point.
* As a user who wants to publish content, I want to be able to post, edit and delete my posts in a straight-forward manner.
* As a published user, I want to be able to easily view all my posts in one place.
* As an admin user I want to be able to edit, delete and add categories to the app, depending on the popularity and trends of existing categories and/or requests from users.
 
### Design choices
* Contrasting header/footer vs main body colour scheme in order to frame the content on each page.
* A minimalist user interface on the navigation bar/ribbon, that collapses for mobile functionality.
* Subtle colour distinction between main body background colour and card-panel colours on each page. Sufficient to frame the content and direct the user’s attention without overwhelming the viewer.
* Compact, clear date/weather banner to provide a simple summary for the user.
* Use of instructive/complementary actions icons throughout. Consistent use of minimalist “chevron” icons used in buttons throughout.
* Descriptive button labelling throughout, and a distinctive theme for “positive action” actions, e.g. Submit, Create buttons, in Lime colour.

### Database schema
![Database Schema](https://github.com/MichaelpHann/MS3-Project/blob/master/static/README-imgs/Database%20Schema.PNG)

This project has been built using MongoDB Atlas. MongoDB is a non-relational database that enables the storage adn retrieval of user data sent to the database.

The database schema illustrated above is relatively simple, containing three collections, each of which contain two or more documents.

* **Categories Collection** - includes reference to the category name, only. The app includes a number of preset categories, and the "Admin" user has the ability to add additional categories via the "Create Category" function.

* **Posts Collection** - includes user inputs as well as data injected/retrieved from other collections. The user's form inputs when creating the blog post are strings and populate "post_title" and "post_content" documents. The "created_by" document is a string and is populated with the username from the *Users Collection**. The "poster" document is populated with the user's ObjectId from the **User's Category**. The "favourites" document is an integer that increments or decrements each time a user adds or removes a post from their favourites.

* **Users Collection** - also includes user inputs as well as data injected/retrieved from other collections. Inputs from the user sign-up form will be the first posting of the "first_name", "last_name", "username" and "password" string documents. These will be accessed/referred to each time the user signs into the app as well as if the user publishes a post. The "user_posts" document is an array and stores the ObjectId of each blog post that the user publishes. This array will be accessed and rendered to the user's profile page, displaying each of the user's posts. The "fav_posts" document is also an array and stores the ObjectId of each blog post that the user 'likes'. This array will be accessed and rendered to the user's profile page, displaying each of the user's "favourited" posts.
 
### Wireframes
Wireframes for this website can be accessed in my wireframes folder within this github repository - [my wireframes](https://github.com/MichaelpHann/MS3-Project)
 
_____

## Features
### Existing features

###### User status-dependent Navbar/Ribbon
Options that a user will see displayed in the navbar are dependant on the user’s status (logged in, logged out, logged in & Admin user status).

Users that are not logged in will see:
- Home
- Sign In
- Sign Up

Users that are logged in will see:
- Home
- Explore
- Profile
- New Post
- Sign Out

User with Admin status who is logged in will see:
- Home
- Explore
- Profile
- New Post
- Manage Categories
- Sign Out

###### Homepage
The landing page presents a simple narrative introduction/background to the application. Additionally, a user who is not logged in will be presented with **Sign In** and **Sign Up** buttons that the user can select depending on whether they are a new or existing user. A user who is already logged in will be presented with an **Explore** button that will direct them to the **Explore** page when pressed.

###### Create account
A new user can create their own profile by selecting the **Sign Up** button on the Navbar. The user must enter their first name, last name, a username and password to create an account. There is a check in place to ensure the proposed username does not already exist on the database. There are also checks in place to ensure the username and passwords are of appropriate min and max lengths, and only contain acceptable characters. The Werkzeug package takes the input from the password form and generates a hashed password. This provides far greater security than storing passwords in plain text. The users new profile will be added to the **Users Collection** on MongoDB. A flash message will welcome the user.

###### Sign In
Users who have created an account can log into their own profile by selecting the **Sign In** button on the Navbar. The user must enter their Username and Password as stored in the database to log in, otherwise they will be presented with a message indicating that one or both elements are incorrect. A flash message will welcome the user back.

###### Sign Out
Users that have signed into the site can end their session at any time by clicking the **Sign Out** button on the Navbar. Flask will end their session using the session.pop() method and will redirect the user to the **Sign In** page.

###### New Post
A registered user who is signed into the application can create a new blog post by selecting the **New Post** button on the Navbar.

The user must complete all elements of the **New Post** form including selecting a Category from the pre-populated dropdown menu, adding a blog post title and blog post content. The user will be prompted to complete all fields if they try to publish the post without them all having been completed. The published post will be stored in the **Posts Collection** in MongoDB, with the ObjectId also stored in the **user_posts** document of the specific user in the **Users Collection**. The post will be displayed on both the **Explore** page and the **USER POSTS** tab of the user’s **Profile** page (see detail below). A flash message will confirm the post was successfully published.

###### Edit Post
A registered user who is signed into their profile and who has published a post can edit their post by selecting the **Edit** button.

The user can click this button when viewing their posts on either the **Explore** or **Profile** page. The user will be taken to the **Edit Post** page where any/each of the three form elements - Category, Post Title, Post Content - can be changed. Once the user confirms the changes the edited post will be stored in the **Posts Collection** on MongoDB, and the changes will be displayed on both the Explore and Profile pages. A flash message will confirm the post was successfully updated. Access restrictions mean a user cannot edit another user’s post. 

###### Delete Post
A registered user who is signed into their profile and who has published a post can delete their post by selecting the **Delete** button.

The user can click this button when viewing their posts on either the **Explore** or **Profile** page. The post will be deleted from the **Posts Collection** in MongoDB and the ObjectId will be removed from the the **user_posts** document in the **Users Collection** also. Additionally, the post will no longer be displayed on either the **Explore** or **Profile** pages. A flash message will confirm the post has been deleted. Access restrictions mean a user cannot delete another user’s post. 

###### Like Post / Unlike Post
A user can “like” or “favourite” any post by clicking on the heart icon in the bottom-right of the post. Once clicked, the **favourites** document of the post in the **Posts Collection** in MongoDB is incremented by 1. Additionally, the ObjectId of the post is added to the “fav_posts” of the specific user in the **Users Collection** in MongoDB. Finally, the colour of the icon will change and the post will be added to the users **FAVOURITE POSTS** tab on their **Profile** page.

If the user clicks the same icon again, return it to its original colour, the exact reverse of events described above will occur.

###### New Category
The registered user with the **Admin** username, who is signed into the application can create a new category by selecting the **Manage Categories** button on the Navbar.

The user will be brought to the **Manage Categories** page where they can then select the **Create Category** button. They will be taken to the **New Category** page where they can add a new category name. A flash message will confirm the new post has been created. Once created, the category will be added to the **Categories Collection** on MongoDB and will be available to all users in the pre-populated dropdown menu in the **New Post** page. Access restrictions prevent a user who is not the “Admin” user from creating a new category.

###### Edit Category
The registered user with the **Admin** username, who is signed into the application can edit an existing category by selecting the **Manage Categories** button on the Navbar. 

The user will be brought to the **Manage Categories** page where each existing category will have a corresponding **Edit** button. When selected the user will be taken to the **Edit Category** page where they can amend the category name. A flash message will confirm the the category name has been updated. The amended category will be stored in the **Categories Collection** on MongoDB. Once updated, the revised category will be available to all users in the pre-populated dropdown menu in the **New Post** page. Access restrictions prevent a user who is not the **Admin** user from creating a new category.

###### Delete Category
The registered user with the **Admin** username, who is signed into the application can edit an existing category by selecting the **Manage Categories** button on the Navbar.

The user will be brought to the **Manage Categories** page where each existing category will have a corresponding **Delete** button. Once clicked the post will be deleted from the database, and its ObjectId is removed from their list of posts in their user record. The recipe is also removed from the favourites of all other users.

###### Profile - User Posts
All posts that a user has published will be displayed in the **USER POSTS** tab of their **Profile** page. The user can edit and delete these posts in the same manner as they can on the **Explore** page.

If the user has not published any posts they will be presented with a placeholder message of **View all your published posts here!**.

Profile - Favourite Posts
All posts that a user has “liked” or “favourited” will be displayed in the **FAVOURITE POSTS**  tab of their **Profile** page.

If the user has not “liked”/“favourited” any posts they will be presented with a placeholder message of **A place for you to curate your favourite posts!**.

###### Explore - Search
Any user that is logged in can conduct a keyword search based on the words contained with the Post Titles and Post Contents, as displayed at any point in time on the **Explore** page. A successful search will result in only those posts that contain a word matching that which was searched displayed on the **Explore** page.

###### Explore - Posts
Any user that is logged in can view all posts that have been published at any point in time on the **Explore** page.

### Future features

###### Enhanced search functionality
Current users can only conduct a search on Post Title and Post Content. It would be helpful if the user could search by Category also/instead. Or if the blog posts could first be filtered by category and then the user could conduct a keyword search on the posts that remain.

###### Delete confirmation modal
In order to avoid a user accidentally deleting a post or the Admin user accidentally deleting a category it would be helpful to have a confirmatory modal in place that asks the user whether they are sure they want to delete the post/category and requires them to select Yes or No.

###### The ability to comment on posts
It would be a nice enhancement if users could write comments beneath posts in a way to could create a conversation thread.
_____
 
## Technologies Used
#### Coding Languages
* [HTML5](https://en.wikipedia.org/wiki/HTML5) - used to build the structure of this application.
* [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) - used for styling of the application.
* [Python](https://www.python.org/) - an interpreted, high-level, general-purpose language, used for all backend functions of this project.
* [JavaScript](https://www.javascript.com/) - used to provide application interactivity.

#### Database Management System
* [MongoDB Atlas](https://www.javascript.com/) - MongoDB Atlas is the online host for remote MongoDB's NoSQL document-oriented databases.

#### Integrations & Frameworks
* [Flask](https://www.javascript.com/) - templating micro framework used to build web application.
* [PyMongo](https://pypi.org/project/pymongo/) - PyMongo is a Python distribution containing tools for working with MongoDB.
* Jinja - web templating engine for Python.
* [jQuery](https://www.javascript.com/) - used to provide application interactivity and simplify DOM manipulation.
* [Materialize CSS](https://materializecss.com/) - used to provide responsive frontend framework.
* [Google Fonts - Material Icons](https://fonts.google.com/icons) - used to style the application icons.
* [Font Awesome](https://fontawesome.com/) - used to style the application icons.

#### Version Control, Storage & Hosting
* [GIT](https://git-scm.com/) - used GitPod for version control.
* [GitHub](https://github.com/) - used for hosting the repository.
* [Heroku](https://heroku.com/) - used to deploy the live application.
 
#### Testing tools
* [Google Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) to test the device responsiveness of the application.
* [JSHint](https://jshint.com/) to validate the JavaScript code.
* [JSLint](https://jshint.com/) to validate the JavaScript code.
* [Esprima Syntax Validator](http://esprima.org/demo/validate.html) to validate the Javascript code.
* [W3C CSS validation](https://jigsaw.w3.org/css-validator/) to validate CSS. 
* [W3C Markup Validation](https://validator.w3.org/) to validate HTML code.
* [Auto-prefixer](https://autoprefixer.github.io/) to ensure the css includes all necessary browser prefixes it needs.
* [PEP8 Online Validator](http://pep8online.com/) to ensure the Python code is fully PEP8 compliant.
 
## Testing
#### Code Validation

###### HTML
The [W3C Markup Validator](https://validator.w3.org/) was used to check HTML from all templates. This generated a numerber of errores due to the inability of the validator to understand Jinja templating that builds most aspects of each page. For the HTML that does not involve Jinja, no errors were found.

###### CSS autoprefixer
The online [CSS autoprefixer](https://autoprefixer.github.io/) was used to ensure all appropriate prefixes were included. Output generated was used.

###### CSS
The [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) was used to check all CSS code, with no errors found.

###### Javascript
All Javascript was passes throught the [Esprima Syntax Validator](http://esprima.org/demo/validate.html) and was found to be syntactically valid.

###### Python
All Python code was passed through the [PEP8 Online Validator](http://pep8online.com/) and is fully PEP8 compliant.


#### Manual testing

 
#### Functionality
Google Chrome Developer was the principal tool used throughout the build to test functionality and device responsiveness. Additionally, in the latter stages, application responsiveness was tested via live user testing across a range of mobile, tablet and desktop devices. All feedback provided as part of this testing has been considered and, where necessary, incorporated into the application.

_____

## Creating the Database

This application is connected to MongoDB Atlas.

The following steps were taken to create the application’s database and database collections:

1. Create an account and login to [MongoDB Atlas](https://mongodb.com)
2. Select the option to create a **New Project** and complete required input fields
* View [New Project](https://github.com/MichaelpHann/MS3-Project/blob/master/static/README-imgs/1%20MDB-New-Project.png)
3. Select the option to **Build a Cluster** and then **Create a Cluster** (a Share Cluster (free) should be sufficient
* View [Build a Cluster](https://github.com/MichaelpHann/MS3-Project/blob/master/static/README-imgs/2%20MDB-Build-a-Cluster.png)
* View [Create a Cluster](https://github.com/MichaelpHann/MS3-Project/blob/master/static/README-imgs/3%20MDB-Create-a-Cluster.png)
4. Select a Cloud Provider (developer selected AWS for this project) and Region (nearest region to your location that is free)
* View [Cloud Provider & Region](https://github.com/MichaelpHann/MS3-Project/blob/master/static/README-imgs/4%20MDB-Cloud-Provider-Region.png)
5. Select Data Tier (developer selected M0 tier for this project)
* View [Data Tier](https://github.com/MichaelpHann/MS3-Project/blob/master/static/README-imgs/5%20MDB-Data-Tier.png)
6. Add Cluster Name
* View [Cluster Name](https://github.com/MichaelpHann/MS3-Project/blob/master/static/README-imgs/6%20MDB-Cluster-Name.png)
7. Click **Create Cluster**
8. Select **Database Access** under **SECURITY** on the left-hand-side ribbon
* View [Database Access](https://github.com/MichaelpHann/MS3-Project/blob/master/static/README-imgs/7%20MDB-DB-Access.png)
9. Add a **New Database User**, completing all required input fields
* View [New Database User](https://github.com/MichaelpHann/MS3-Project/blob/master/static/README-imgs/8%20MDB-New-DB-User.png)
* View [Add New Database User](https://github.com/MichaelpHann/MS3-Project/blob/master/static/README-imgs/9%20MDB-New-DB-User.png)
10. Select **Network Access** under **SECURITY** on the left-hand-side ribbon
11. Add or **whitelist** IP Address (you can Allow Access from Anywhere but this is not recommended for full production apps)
* View [Add IP Address](https://github.com/MichaelpHann/MS3-Project/blob/master/static/README-imgs/10%20MDB-IP-Address.png)
* View [Add IP Address Detail](https://github.com/MichaelpHann/MS3-Project/blob/master/static/README-imgs/11%20MDB-IP-Address.png)
12. Select **Clusters** under **DATA STORAGE** on the left-hand-side ribbon
* View [Clusters](https://github.com/MichaelpHann/MS3-Project/blob/master/static/README-imgs/12%20MDB-Clusters.png)
13. Select **COLLECTIONS** to add database and begin adding documents to your database collections
* View [Collections](https://github.com/MichaelpHann/MS3-Project/blob/master/static/README-imgs/14%20MDB-Cluster-Collections.png)
* View [Create Database](https://github.com/MichaelpHann/MS3-Project/blob/master/static/README-imgs/13%20MDB-Create-DB.png)
14. Please see indicative database schema structure depicted earlier in this file

_____

## Deployment
 
This project was developed using Gitpod, with the repository stored on GitHub.

#### Creating a clone 
To clone this project from GitHub:
1. On GitHub, navigate to the project repository - https://github.com/MichaelpHann/MS3-Project.
2. Under the repository name, select the green **Code** dropdown button.
* View [GitHub Clone](https://github.com/MichaelpHann/MS3-Project/blob/master/static/README-imgs/1%20GH-Clone.png)
3. Highlight the URL provided or click the button to copy the URL.
4. Open your terminal.
5. Navigate to the working directory where the cloned repository will be placed.
6. In the command line type `git clone` and then paste the URL (copied in Step 3) immediately after.
  `git clone https://github.com/MichaelpHann/MS3-Project`
7. Press **Enter**. Your local clone will be created.
 
For more information or guidance, please see the relevant help section [Cloning a Repository](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).
 
The project was deployed using Heroku and the live application can be found [**here**](https://ms3-project-mph.herokuapp.com/)
 
#### Deploying an app on Heroku

###### Create Application
1. Sign-up or login to Heroku at heroku.com.
2. In the main body of the page, select the **New** dropdown button on the right-hand-side and select **Create new app**.
3. Insert the desired name of your app (the name must be unique and Heroku will confirm if the chosen name is available).
4. Select the most appropriate region based on your location.
* View [Create App](https://github.com/MichaelpHann/MS3-Project/blob/master/static/README-imgs/1%20H-Create-App.png)
5. Click the **Create app** button.

###### Connect to GitHub Repository
1. Upon creating an app, the user will be brought automatically to the **Deploy** tab in the app.
2. In the **Deployment Method** section, select **GitHub**, after which a **Connect to GitHub section will appear immediately below.
* View [Deployment Method](https://github.com/MichaelpHann/MS3-Project/blob/master/static/README-imgs/2%20H-Deploy-Method.png)
3. Search for the relevant GitHub repo using the **Search** functionality.
4. Click **Connect**
* View [Connect to GitHub](https://github.com/MichaelpHann/MS3-Project/blob/master/static/README-imgs/3%20H-Connect-GH.png)

###### Setting Environment Variables
5. This project has been built with environment variable stored in a hidden env.py file. To enable Heroku to securely read these variables, Configuration Variables or Config Vars need to be set (in Heroku).
6. Within the **Settings** tab, under the Config Vars section, select **Reveal Config Vars**.
* View [Config Vars](https://github.com/MichaelpHann/MS3-Project/blob/master/static/README-imgs/4%20H-Config-Vars.png)
7. A form to input Key-Value pairs that are necessary to connect to the app will be displayed. The key value pairs, as stored in the env.py file and shown below should be added here.

KEY  |  VALUE  
-----|-------
   IP  | 0.0.0.0 
  PORT |  5000   
 SECRET KEY | Randomly Generated Fort Knox Key
 MONGO_URI | Unique MongoDB URI 
 MONGO_DBNAME | Unique Mongo DB name 

8. Ensure you include your onward DB Name and Password within the **MONGO_URI**. This can be found in the MONGO DB Project under **Cluster** and **Connect**

###### Enable Automatic Deployment

9. Click on the **Deploy** tab
10. Under the **Automatic Deploys** section, select the branch from GitHub that you want to deploy the app from and then click **Enable Automatic Deploys**
11. Finally, click **Deploy Branch** and once built the app will then be available by clicking the **View** button.

_____

## Credits
### Technical sources
* Some application features, including the search functionality and the sign-up/security functionality, have been replicated from the Code Institute Python/Flask/Mongodb Mini Project.

_____

### Acknowledgements
I would like to thank both [Sandeep Aggarwal](https://github.com/asandeep) and [Chris Quinn](https://github.com/10xOXR) for their guidance and constructvie feedback throughout the project.
 
