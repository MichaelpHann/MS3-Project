
# Commonplace | An Everyday Publishing Platform
 
Live application demo can be found [**here**](https://ms3-project-mph.herokuapp.com/)
 
## Table of Contents
 
* [UX](#UX)
  * [Application overview](#Application-overview)
  * [User stories](#User-stories)
  * [Design choices](#Design-choices)
  * [Wireframes](#Wireframes)
* [Features](#Features)
  * [Existing features](#Existing-features)
  * [Future features](#Future-features)
* [Technologies Used](#Technologies-Used)
* [Testing](#Testing)
  * [Implemented features](#Implemented-features)
  * [Functionality](#Functionality)
  * [Bugs](#Bugs)
* [Deployment](#Deployment)
* [Credits](#Credits)
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
 
### Wireframes
Wireframes for this website can be accessed in my wireframes folder within this github repository - [my wireframes](https://github.com/MichaelpHann/IFD-Milestone-Project/tree/master/Wireframes)
 
 
## Features
 
### Existing features


 
_____
 
## Technologies Used
 
#### Coding Languages
* [HTML5](https://en.wikipedia.org/wiki/HTML5) - used to build the structure of this application.
* [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) - used for styling of the application.
* [JavaScript](https://www.javascript.com/) - used to provide application interactivity.

#### Database Management System
* [MongoDB Atlas](https://www.javascript.com/) - used to

#### Integrations & Frameworks
* [Flask](https://www.javascript.com/) - used to 
* Jinja- used to provide
* [jQuery](https://www.javascript.com/) - used to provide application interactivity and simplify DOM manipulation.
* [Materialize CSS](https://materializecss.com/) - used to provide responsive frontend framework.
* [Google Fonts - Material Icons](https://fonts.google.com/icons) - used to style the application icons.
* [Font Awesome](https://fontawesome.com/) - used to style the application icons.

#### Version Control, Storage & Hosting
* [GIT](https://git-scm.com/) - used GitPod for version control.
* [GitHub](https://github.com/) - used for hosting the repository.
* [Heroku](https://heroku.com/) - used to deploy the live application.
 
 
### Testing tools
 
* [Google Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) to test the device responsiveness of the application.
* [JSHint](https://jshint.com/) to validate the JavaScript code.
* [JSLint](https://jshint.com/) to validate the JavaScript code.
* [W3C CSS validation](https://jigsaw.w3.org/css-validator/) to validate CSS. 
* [W3C Markup Validation](https://validator.w3.org/) to validate HTML code.
* [Auto-prefixer](https://autoprefixer.github.io/) to ensure the css includes all necessary browser prefixes it needs.
*Google Lighthouse
 
## Testing
 
### Implemented features
 
1. 
 
2. 
 
3. 
 
4. 
 
5. 
 
6. 
 
7. 
 
### Functionality
Google Chrome Developer was the principal tool used throughout the build to test functionality and device responsiveness. Additionally, in the latter stages, application responsiveness was tested via live user testing across a range of mobile, tablet and desktop devices. All feedback provided as part of this testing has been considered and, where necessary, incorporated into the application.
 
### Bugs
* 

## Creating the Database

This application is connected to MongoDB Atlas.

The following steps were taken to create the application’s database and database collections:

1. Create an account and login to [MongoDB Atlas](https://mongodb.com)
2. Select the option to create a **New Project** and complete required input fields
![New Project](https://github.com/MichaelpHann/MS3-Project/blob/master/static/README-imgs/1%20MDB-New-Project.png)
3. Select the option to **Build a Cluster** and then **Create a Cluster** (a Share Cluster (free) should be sufficient
![Build a Cluster](https://github.com/MichaelpHann/MS3-Project/blob/master/static/README-imgs/2%20MDB-Build-a-Cluster.png)
![Create a Cluster](https://github.com/MichaelpHann/MS3-Project/blob/master/static/README-imgs/3%20MDB-Create-a-Cluster.png)
4. Select a Cloud Provider (developer selected AWS for this project) and Region (nearest region to your location that is free)
![Cloud Provider & Region](https://github.com/MichaelpHann/MS3-Project/blob/master/static/README-imgs/4%20MDB-Cloud-Provider-Region.png)
5. Select Data Tier (developer selected M0 tier for this project)
![Data Tier](https://github.com/MichaelpHann/MS3-Project/blob/master/static/README-imgs/5%20MDB-Data-Tier.png)
6. Add Cluster Name
![Cluster Name](https://github.com/MichaelpHann/MS3-Project/blob/master/static/README-imgs/6%20MDB-Cluster-Name.png)
7. Click **Create Cluster**
8. Select **Database Access** under **SECURITY** on the left-hand-side ribbon
![Database Access](https://github.com/MichaelpHann/MS3-Project/blob/master/static/README-imgs/7%20MDB-DB-Access.png)
9. Add a **New Database User**, completing all required input fields
![New Database User](https://github.com/MichaelpHann/MS3-Project/blob/master/static/README-imgs/8%20MDB-New-DB-User.png)
![Add New Database User](https://github.com/MichaelpHann/MS3-Project/blob/master/static/README-imgs/9%20MDB-New-DB-User.png)
10. Select **Network Access** under **SECURITY** on the left-hand-side ribbon
11. Add or **whitelist** IP Address (you can Allow Access from Anywhere but this is not recommended for full production apps)
![Add IP Address](https://github.com/MichaelpHann/MS3-Project/blob/master/static/README-imgs/10%20MDB-IP-Address.png)
![Add IP Address Detail](https://github.com/MichaelpHann/MS3-Project/blob/master/static/README-imgs/11%20MDB-IP-Address.png)
12. Select **Clusters** under **DATA STORAGE** on the left-hand-side ribbon
![Clusters](https://github.com/MichaelpHann/MS3-Project/blob/master/static/README-imgs/12%20MDB-Clusters.png)
13. Select **COLLECTIONS** to add database and begin adding documents to your database collections
![Collections](https://github.com/MichaelpHann/MS3-Project/blob/master/static/README-imgs/14%20MDB-Cluster-Collections.png)
![Create Database](https://github.com/MichaelpHann/MS3-Project/blob/master/static/README-imgs/13%20MDB-Create-DB.png)
14. Please see indicative database schema structure depicted earlier in this file

 
## Deployment
 
This project was developed using Gitpod, with the repository stored on GitHub.

#### Creating a clone 
To clone this project from GitHub:
1. On GitHub, navigate to the project repository - https://github.com/MichaelpHann/MS3-Project.
2. Under the repository name, select the green **Code** dropdown button.
![GitHub Clone](https://github.com/MichaelpHann/MS3-Project/blob/master/static/README-imgs/1%20GH-Clone.png)
3. Highlight the URL provided or click the button to copy the URL.
4. Open your terminal.
5. Navigate to the working directory where the cloned repository will be placed.
6. In the command line type `git clone` and then paste the URL (copied in Step 3) immediately after.
  `git clone https://github.com/MichaelpHann/MS3-Project`
7. Press **Enter**. Your local clone will be created.
 
For more information or guidance, please see the relevant help section [Cloning a Repository](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).
 
The project was deployed using Heroku and the live application can be found [**here**](https://ms3-project-mph.herokuapp.com/)
 
#### Creating an app on Heroku
1. Sign-up or login to Heroku at heroku.com.
2. In the main body of the page, select the **New** dropdown button on the right-hand-side and select **Create new app**.
3. Insert the desired name of your app (the name must be unique and Heroku will confirm if the chosen name is available).
4. Select the most appropriate region based on your location.
![Create App](https://github.com/MichaelpHann/MS3-Project/blob/master/static/README-imgs/1%20H-Create-App.png)
5. Click the **Create app** button.

#### Deploying an app on Heroku
1. Upon creating an app, the user will be brought automatically to the **Deploy** tab in the app.
2. In the **Deployment Method** section, select **GitHub**, after which a **Connect to GitHub section will appear immediately below.
![Deployment Method](https://github.com/MichaelpHann/MS3-Project/blob/master/static/README-imgs/2%20H-Deploy-Method.png)
3. Search for the relevant GitHub repo using the **Search** functionality.
4. Click **Connect**
![Connect to GitHub](https://github.com/MichaelpHann/MS3-Project/blob/master/static/README-imgs/3%20H-Connect-GH.png)
5. The app uses configuration settings for MongoDB and secret keys for session cookies, both of which Heroku requires to enable the app to function correctly. For this, Configuration Variables or Config Vars need to be set in Heroku.
6. Within the **Settings** tab, under the Config Vars section, select **Reveal Config Vars**.
![Config Vars](https://github.com/MichaelpHann/MS3-Project/blob/master/static/README-imgs/4%20H-Config-Vars.png)
7. A form to input Key-Value pairs that are necessary to connect to the app will be displayed.

  KEY  |  VALUE  
-----|-------
   IP  | 0.0.0.0 
  PORT |  5000   
 SECRET KEY | Randomly Generated Fort Knox Key
 MONGO_URI | Unique MongoDB URI 
 MONGO_DBNAME | Unique Mongo DB name 
 
8. The **MONGO_URI** variable noted above can be located in the MongoDB Project, under **Cluster** and by clicking **Connect**
9. Select **Clusters**, then **Connect**, then select **Connect your application** and finally choose your Driver and Version.....
 
## Credits
 
### Technical sources
* Some application features, including the search functionality and the sign-up/security functionality, have been replicated from the Code Institute Python/Flask/Mongodb Mini Project.
 
### Acknowledgements
I would like to thank my mentor, [Sandeep Aggarwal](https://github.com/asandeep), for his constructive feedback and guidance throughout the project.
 
