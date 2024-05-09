# BOARDGAMES

An exciting new place for board game fanatics to share their new finds and favourite classics with others! Log in to review a new game or look through the list of recommendations to find a new game to try! Mark games as favourites so you can easily find them again.

The ideal place for board game producers to advertise! Imagine your new game appearing just as a board game enthusiast has logged on to find some inspiration! And there is an easy place for them to come on, review and tell others all about it! We would also be happy to discuss adding links to purchase games that have been reviewed, to make it easier for players to purchase your game right away!

- Include a picture of site that shows it in responsive states and links to deployed code: https://ui.dev/amiresponsive

## Live Site
🚨**Required** 

- Include a link to deployed project (typically a Heroku Page)

## Repository
🚨**Required** 

- Include a Link to the GitHub repository

## Author

JENNIE WILLSON

# Table of Contents
🚀 **merit & beyond**

# Table of contents

- [OVERVIEW](#overview)
  - [Helpful tools](#helpful-tools)
    - [PDB Debugging](#pdb-debugging)
    - [Screenshots and Videos](#screenshots-and-videos)
    - [Cheatsheets and Auto Generation Tools](#cheatsheets-and-auto-generation-tools)
- [PROJECT_NAME](#project_name)
  - [Live Site](#live-site)
  - [Repository](#repository)
  - [Author](#author)
- [Table of Contents](#table-of-contents)
- [HOW TO USE](#how-to-use)
- [UX](#ux)
  - [Strategy](#strategy)
  - [Scope](#scope)
    - [Project Goals](#project-goals)
    - [User Goals](#user-goals)
    - [Developer Goals](#developer-goals)
    - [Website Owner Goals](#website-owner-goals)
    - [User Stories](#user-stories)
  - [Feasibility vs Importance](#feasibility-vs-importance)
  - [Target Audience](#target-audience)
  - [Design Choices](#design-choices)
    - [Colors](#colors)
    - [Typography](#typography)
    - [Images](#images)
    - [Design Elements](#design-elements)
    - [Animations and Transitions](#animations-and-transitions)
    - [Frameworks](#frameworks)
    - [Custom Styles](#custom-styles)
    - [Custom Javascript](#custom-javascript)
  - [Wireframes](#wireframes)
- [Information Architecture](#information-architecture)
  - [Entity Relationship Diagram](#entity-relationship-diagram)
  - [Database Choice](#database-choice)
  - [Data Models](#data-models)
  - [CRUD Flow Diagrams](#crud-flow-diagrams)
- [Features](#features)
  - [Implemented Features](#implemented-features)
  - [Future Features](#future-features)
- [Defensive Programming](#defensive-programming)
- [Testing](#testing)
  - [Validation Testing](#validation-testing)
    - [CSS Validation](#css-validation)
    - [HTML Validation](#html-validation)
    - [JavaScript Validation](#javascript-validation)
    - [Python Validation](#python-validation)
    - [JSON Validation](#json-validation)
  - [Accessibility Testing](#accessibility-testing)
    - [Accessibility Audits](#accessibility-audits)
    - [Keyboard Navigation](#keyboard-navigation)
    - [Chrome Vox Reader](#chrome-vox-reader)
  - [Core Web Vitals](#core-web-vitals)
    - [Cross Browser and Cross Device Testing](#cross-browser-and-cross-device-testing)
  - [Automated Testing](#automated-testing)
  - [Manual Testing](#manual-testing)
  - [Defects](#defects)
  - [Defects of Note](#defects-of-note)
  - [Outstanding Defects](#outstanding-defects)
- [Technologies Used](#technologies-used)
  - [Programming Languages](#programming-languages)
  - [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)
  - [Tools](#tools)
  - [APIs](#apis)
- [Deployment](#deployment)
  - [Prerequisites](#prerequisites)
  - [Fork and Clone the Repository](#fork-and-clone-the-repository)
  - [Deploy Locally](#deploy-locally)
  - [Production Deployment (Heroku)](#production-deployment-heroku)
- [Credits](#credits)
  - [Content](#content)
  - [Media](#media)
  - [Acknowledgments](#acknowledgments)

Generate after readme is complete by copying and pasting your readme from this point & below into this tool:
- [mardown table of contents generator](https://luciopaiva.com/markdown-toc/)
**NOTE:** It does have some bugs if you have dashes or trailing spaces in your headers, so make sure all these WORK!


# HOW TO USE
🚀 **merit & beyond**

This project requires DATA INTERACTION, if you set up user authentication, you should include example accounts to use in your heroku deployment so the assessors can use your site. 
Ideally you'd record yourself using the site in slack. Download it to your computer then drag and drop that into your README.md while editting it in github.

# UX
🚨**Required** 

## Strategy
🚨**Required** 
I LOVE playing board games and I play a lot online and in person. I am always interested in finding new games to play! I regularly get recommendations from friends but would love a way to access even more board game enthusiasts and their recommendations!

I know there are lots of people like me out there who would love this and love to share their board game finds with others!

This would also be the perfect place for board game producers to sell games, so people can have a one-click link from review to purchase site, as well as having the opportunity to advertise new games to people who really love them!

## Scope
🚨**Required** 
The MVP will introduce the concept and allow us to build up a user-base. It will be set up with some initial reviews, which I can easily add myself, as I have a lot of experience and knowledge of board games.

Once it starts to build up with users, I would then add a bit more functionality - things like ratings based on user ratings, ability for users to suggest edits to descriptions, to write their own reviews and to add hints and tips for the game or any add-ons or variations available.

Once there is a larger number of regular users I would get in touch with some board game producers and offer advertising on the site. To start with I might offer some of ths for free in exchange for advertising the site, for example adding flyers or QR codes in game boxes etc. Later I would hope this could move to profit making, potionally with a share in sales originating on my site, but I think a loss leader would be a better start long-term.

I would also like to look at allowing users to add suggestions for new games, which they could work on in collaboration with other users and potentially pitch to the game producers advertising on the site.

### Project Goals
🚨**Required** 
#### Board Game Enthusiasts
- Help to find new games
- Able to recommend games to others

#### Board game producers
- Targeted advertising to those most likely to be interested
- Increased sales
- Easy way to introduce new games to enthusiasts

#### Developer
- Initiate a website that will be enhanced and grown by the user base, so require reducing amounts of input
- Make money from advertising and sales of board games
- Enjoy using it myself!

### User goals

#### Guest

- View games
- See basic information about a game
- Filter games to find a specific genre
- Sort by name in alphabetical order
- Choose a game they would like to play
- Create an account to become a user

#### User with an account

As 'Guest' above, plus:
- Log in
- Sort by favourites
- Submit a board game
- Edit a board game I added
- Favourite a game
- Log out

#### Super-user

- Approve submitted board games
- Edit existing board games
- Delete board games

### User stories

#### Guest

##### US1
**As a** Guest to the website (or a logged in user)
**I want** to be able to see the list of games
**So that** I can learn about the games reviewed

##### US2
**As a** Guest to the website (or a logged in user)
**I want** to be able to filter the list of games
**So that** I can see only the games that fit my requirements

##### US3
**As a** Guest to the website (or a logged in user)
**I want** to be able to order the games by title or rating
**So that** it is easier to find a game or to see which are most highly recommended

##### US4
**As a** Guest to the website (or a logged in user)
**I want** to be able to contact the website owner
**So that** I can ask any questions or give any feedback on the site

#### New user

##### US5
**As a** New user
**I want** to be able to create an account
**So that** I can log in to add reviews or record my favourites

##### US6
**As a** New user
**I want** to be able to see what the terms of the website are and how my data will be stored and used as per GDPR
**So that** my legal rights are fulfilled and I can choose to sign up with full knowledge

#### Existing user

##### US7
**As an** existing user
**I want** to be able to log in to my account
**So that** I can access the features available to logged in users

##### US8
**As a** logged in user
**I want** to be able to submit a new board game review
**So that** I can share a new board game with others

##### US9
**As a** logged in user
**I want** to be able to edit my own board game reviews
**So that** I can correct mistakes or add new information

##### US10
**As a** logged in user
**I want** to be able to 'favourite' a game
**So that** I can mark a game as one I want to be able to easily access when I am logged in

##### US11
**As a** logged in user
**I want** to be able to sort the list of games by my favourites
**So that** I can easily access my favourite games whenever I am logged in

##### US12
**As a** logged in user
**I want** to be able to complete the contact form without adding my email
**So that** I am saved time, as I am already logged in

#### Super-user

##### US13
**As a** logged in Super-user
**I want** to be able to edit any game another user has added
**So that** I can correct any incorrect, in appropriate or out of date information

##### US14
**As a** logged in Super-user
**I want** to be able to view submitted reviews that have not yet been published
**So that** I can check a review submitted by a user to ensure it is appropriate for publishing

##### US15
**As a** logged in Super-user
**I want** to be able to mark a submitted review for publishing
**So that** I can check a review submitted by a user to ensure it is appropriate for publishing

### Future user goals

#### Board game producer

**As a** Board game producer
**I want** to be able to advertise my games clearly
**So that** I get the game recognised and more traffic to my website

**As a** Board game producer
**I want** to be able to advertise my games clearly
**So that** I can sell more of the game

### Developer Goals
🚀 **merit & beyond**

**As a** Developer
**I want** to pass my project
**So that** I can continue with the course and achieve the diploma

**As a** Developer
**I want** to improve my skills in coding, using databases, creating secure user accounts, management of data etc
**So that** I am able to use this in the future in work and outside

**As a** Developer
**I want** to create a website that I will enjoy and use myself
**So that** I can find more exciting board games to play and introduce others to the ones I love

**As a** Developer
**I want** to create a website that will be attractive to the target audience
**So that** I am able to gain users to make the website successful

**As a** Developer
**I want** to create a website that will eventually run itself
**So that** it is successful and potentially makes money with minimum effort from me

### Website Owner Goals
🚀 **merit & beyond**

**As a** Website owner
**I want** to attract a large number of regular users
**So that** I have good grounds for attracting advertising revenue

**As a** Website owner
**I want** the website to be run by users
**So that** it has minimal running costs

**As a** Website owner
**I want** to attract lots of relevant advertisers
**So that** I am able to make money from the adverts but also that users are not put off by irrelevant adverts

**As a** Website owner
**I want** users to buy board games through links from the site
**So that** I am able to make money and users benefit from a one-stop shop


## Feasibility vs Importance
🚀 **merit & beyond**

To scope the project for a MVP (minimally viable product) a feasibility analysis was done.

The features in the table below have been taken from the user stories above. Generic features found in most websites
will also be implemented such as nav-bar, footer, obvious website purpose etc.

| Opportunity/Feature | Current Feasibility/Viability (/5)     | PurposeLevel of Importance (score out of 5) | In Or Out |
|---------------------|----------------------------------------|---------------------------------------------|-----------|
| Create account      | 4                                      | 5                                           | In        |
| Log in              | 4                                      | 5                                           | In        |
| Log out             | 4                                      | 5                                           | In        |
| Filter              | 4                                      | 5                                           | In        |
| Sort                | 4                                      | 5                                           | In        |
| Advertising space   | 1                                      | 1                                           | Out       |
| Add board game      | 5                                      | 5                                           | In        |
| Edit board game     | 3                                      | 5                                           | In        |
| Delete board game   | 3                                      | 3                                           | In        |
| Link to buy game    | 2                                      | 1                                           | Out       |
| Report problem      | 2                                      | 2                                           | Out       |
| Contact us          | 4                                      | 5                                           | In        |

> You should discuss the outcome of what you will be dropping based on the outcome. Making a scatter plot of the scores and coloring the dot 


## Target Audience
🚀 **merit & beyond**

- Board game enthusiasts
- Occasional players
- All ages but more aimed at use by adults
- International potentially, mainly English speaking

## Design Choices
🚀 **merit & beyond**

### Simple

- The site is not specifically aimed at technical people or even those who necessarily use websites a lot. It might be an introduction to this sort of thing, so must be simple to navigate. 

### Minimal

- It should not have a large hierarchy of pages and menus should be simple and obvious
- The number of pages should be kept to a minimum and it should be possible to get to any of them from any other

### Easy navigation

- It should be very simple to perform all tasks for general users
- Users should not see what they are unable to access, to avoid confusion - or should be led to a login/sign-up page if relevant

### Colors

A colour scheme should fit with the theme of the site, so I considered the types of colours people might associate with board games.

Obviously that does include almost any colour, so I decided that the best option was to go with a classic board game approach.

Also board games are fun and the site should reflect that, so bright bold colours seemed appropriate.

I thought about games with a range of iconic colours and particularly thought about the standard colours for playing pieces across a lot of games. I decided the most appropriate one to base this on would be Cluedo. The colours are bright and recognisable and fun, there are six including white, which would work as a background colour as the focus of the site is a lot of pictures of games, so other background colours might detract from that. It would allow for a good range of five other colours to make different aspects of the site stand out, with some being used for smaller items, such as red for the 'favourite' heart and a smaller number, two or three, forming the basic colour scheme.

![alt text](<Boardgames colourscheme.png>)

### Typography
🚀 **merit & beyond**

Typography also needs to follow the plan of simple and easy - and also fun and bold! It should be easy to read but not take itself too seriously!

I decided to use ![Archivo black](https://fonts.google.com/specimen/Archivo+Black?preview.text=Boardgames!&stroke=Sans+Serif) for the titles as it is bold but simple.

For other text I will use ![Quicksand](https://fonts.google.com/specimen/Quicksand?preview.text=Boardgames!&query=Quic&stroke=Sans+Serif). I used suggestions from the website ![Design Your Way](https://www.designyourway.net/blog/best-fonts-for-reading/) and looked for something that was easy to read but was quite modern and not too business-like, as this should look fun! Quicksand looked like the perfect example.

### Images
🚀 **merit & beyond**

Explain why you used certain icons and images on your site

### Design Elements
🚀 **merit & beyond**

- list out the type of elements you want to use on your site, this will help you when choosing a framework and goes hand
  in hand when doing the wireframes. If you did something out of the ordinary, or think something was particularly
  clever, add a sentence and a screenshot or reference the file the code or css is in.

> - desktop navigation
> - mobile navigation
> - footer
> - containers/cards
> - buttons
> - text input
> - textarea inputs
> - dropdowns
> - modals/layers
> - check boxes
> - switches
> - accordions/drawers
> - pagination
> - date pickers
> - maps
> - images
> - tooltips
> - icons
> - tabbed content
> - file pickers
> - video players
> - audio players

### Animations and Transitions
🚀 **merit & beyond**

- discuss any special animations or transitions you've programmed
- special hover state effects

### Frameworks
🚨**Required** 

- If you use bootstrap, tailwind, bulma, materialize or some other JS/CSS framework, call it out here and why you made
  that choice. (Typically I look at the design elements I want and make sure the framework supports them)

### Custom Styles
🚨**Required**

- call out any overrides you did for bootstrap styles or the framework you used, even if they are fonts and colors, perhaps lead assessors to the file of interest in your repo

### Custom Javascript
🚨**Required** 

- call attention to any custom javascript you created to help your User Experience you can organize this by functions or files

## Wireframes
🚨**Required** 

![Home page](Home_List.png)
![alt text](Login_Register.png)
![alt text](<Add game.png>)
![alt text](<Contact us.png>)

- you need **mobile** & **desktop** views

- Capture Your Custom model's
  - CREATE/ADD
  - READ (LIST/DETAIL)
  - UPDATE/EDIT
  - DELETE
  - & triggers for such things
- call out differences for authentication levels:
  - not logged in
  - general user logged in
  - super user logged in
- HOW is the NAVIGATION different for admin users vs Logged-in users & unauthenticated users

🚀 **merit & beyond**
- tablet views
- Custom 404
- Profile Page
- Login
- Register
- Forgot Password

You can hand draw these, but CI posts a yearly license in the general channel for Balsamiq which is pretty easy to use.
Here is the [2023 announcement](https://code-institute-room.slack.com/archives/C0L316Z96/p1672656810467649)

# Information Architecture
🚨**Required** 

As part of the requirements for this project you need to have at least **1 original data model**.  It's this section that discusses your data and how each piece relates to another.

 - [draw.io](https://about.draw.io/features/) - is a free program that can be used to create Entity Relationship diagrams and CRUD flow diagrams.

## Entity Relationship Diagram
🚨**Required** 

Use some type of spreadsheet or even draw out one by hand, but you should show how your data models are related to each other  or what those tables are even if they are entirely separate from each other. 


## Database Choice
🚨**Required** 

Write out which database(s) you used and why sometimes you use a different one for local vs production.

## Data Models
🚨**Required** 

Show the accessors you know your data. If you end up using some data models from an example project, call that out and don't be as detailed about writing those up unless you added to them.  

Each data model that you created yourself should have its Fields, Field Type and any validation documented.  You should also cross-reference any code in your repository that relate to CREATE, READ, UPDATE, DELETE operations for these models.


You can try to use markdown, or just take a screenshot from a Google spreadsheet.

Below is an example of a write-up for an Activities Data Model
> **Activities Model**
> Activities is a table to hold a unique icon image and name values that users have associated with events and places. It helps with sorting events and prevents the need from carrying around two data objects in the larger Events and Places data structures. The purpose of an Activities object is to provide an imagery association to a category.
>
> | DB Key    | Data Type    |          Purpose            | Form Validation                            | DB processing        |
> |--------	|:---------:	|:-------------------------:	|----------------------------------------	|------------------	|
> | _id        | ObjectId    | unique identifier            | None                                    | n/a                |
> | name    | String        | Name of Activity            | Required<br>Min 1 char<br>Max 50 chars    | trim<br>to lower    |
> | icon    | String        | system path to image file    | Required                                |                  	|
>
> Activity entries are used by events, places and filtering.
>
> - [x] Create - An activity is potentially created when a user successfully creates a place, creates an event, updates an event, or updates a place.
> - [x] Read - The Activities table is read when a user is adding an event, updating an event, adding a place or updating a place, to determine if a new value should be created or not. The activities table is queried for using the name and icon pair, if it is found, the ObjectId is passed to the event and places. If no match is found, a new Activity is created and that ObjectID is passed to the place or event.
> - [ ] Update
> - [ ] Delete
    >
    >  This table has no deletion or updates associated with it. It's strictly create and read. Eventually, maintenance scripts should be written to delete unused/deprecated entries.
>
> The reading/writing of the activities table is housed in the [what2do2day/activities/views.py](what2do2day/activities/views.py) file.


## CRUD Flow Diagrams
🚀 **merit & beyond**

It might be overkill, but you could document the flow of how your CRUD operation logic works if its full of complex logic. Using a flow diagram or process diagram might make it easier for accessors to understand the inner workings of your program.


I used [draw.io](https://app.diagrams.net/) and hooked it up to my google drive to create the screenshot below

> ![image](https://user-images.githubusercontent.com/23039742/154406188-c9beb57a-2fd1-4f26-a8ed-bee320e46e3d.png)


# Features
🚨**Required** 

In this section, you should go over the different features of your project, and describe each in a sentence or so along with a screenshot. 

## Implemented Features

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

It's easiest to break this section down into by pages and common page components such as home page, products page, product detail page, product sort buttons, navigation, and footer. Call out differences between viewports as needed. 

Don't forget your 404 and 500 error pages.

Don't forget the 3 phases of navigation:
- unauthenticated
- general authenticated user
- superuser authenticated

And don't forget Defensive programming bits
- validation of form inputs
- not allowing users to create, read, update and delete information they shouldn't

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.


## Future Features
🚀 **merit & beyond**

Use this section to discuss plans for additional features to be implemented in the future:

If you end up not developing some features you hoped to implement, you can include those in this section.



# Defensive Programming
🚨**Required** 

Sites with admin rules and roles opens a site up to hacking especially if your users are savvy and notice url parameters correlate to database object manipulation.  If you did anything above the basics to defend your application against hacking write them out here. You want to make the accessor's job easy by stating what you did to keep the data safe.
   

# Testing
🚨**Required** 

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Validation Testing
🚨**Required** 

In this section you should write up any websites you used to validate your code and include screenshots.

**Validation issues are an automatic failure** You should run these about 3 times:
- when you first deploy your site
- just when you think you are done testing
- right before you submit because 😼, ⚽, 🐶 & 👼 can eliminate a closing tag or curly bracket without you noticing.

### CSS Validation
🚨**Required** 

The [Jigsaw validator](https://jigsaw.w3.org/css-validator/) was used to validate CSS.

> If you only have one CSS file, you can just run the validator through one deployed page URL, if you have custom CSS for different pages, make sure you hit those different URLS, or do direct input on each file.

Include a screenshot for each CSS file which includes the Green no ERRORS bar, two check marks:

**styles.css**
![img.png](documentation/images/css-validation.png)

### HTML Validation
🚨**Required** 

The **[W3 HTML Validator](https://validator.w3.org/)** was used to validate HTML by coping the page source as a direct input.

> For each view/route you wrote, you should validate the HTML and have a screenshot
> NOTE: You may need to right-click to view the source of each page and paste that into the validator if you need to go through authentication to get to the page. 
> The screenshot should have from blue to blue line. The [Go Full Page chrome extension](https://chrome.google.com/webstore/detail/gofullpage-full-page-scre/fdpohaocaechififmbbbbbknoalclacl) in is good if you have a long bit of output.

### JavaScript Validation
🚨**Required** 

The **[Jshint validator](https://jshint.com)** was used to validate each JS file.

> for each .js file, copy the code and paste it into this site, and have a test case for it linked to from here. You can have warnings, but no errors.
> if using ES6, add this before pasting in your file: `/*jshint esversion: 6 */ `, similarly you can update it to 7 if you see warnings about ES7 syntax `/*jshint esversion: 7 */ `

### Python Validation
🚨**Required** 

**[CI's pep8 tool](https://pep8ci.herokuapp.com/)** was used to validate each .py file created.

> for each .py file you created, copy the source code and paste it into this site, and have a test case for it linked to from here.
> include a screenshot of results in the test case showing NO ERRORS. (you should do this for all .py files in your repo

**run.py**

![image](https://user-images.githubusercontent.com/23039742/212106175-36b2f18a-7c75-458d-94dd-9886e81c71f3.png)

Ideally you would have no errors remaining outside of line too long which you can fix by 

adding
```$python 
# noqa
```
There is a space before the # and after it to skip the quality assurance for that line.

Note any errors or warnings you are ignoring and why.

### JSON Validation
🤷‍ **Required if you made some files** 
The **[JSONLINT validatior](https://jsonlint.com/)** was used to validate JSON files.

> for each .json file, you should copy the code and paste it into this site, and have a test case for it linked to from here.


## Accessibility Testing
🚨**Required** 

Accessibility testing is aimed to make sure that those with visual or physical disabilities can still browse your website. Some users have had strokes or accidents that make it difficult to use a mouse, so they use keyboard keys to tab through sites. Others use screen readers that rely on HTML tags to help the user navigate quickly through the site to find information they want, others have color blindness or contrast issues. It's the law to provide services 
Here's a [site](https://www.w3.org/WAI/fundamentals/accessibility-intro/#:~:text=Accessibility%20is%20Important%20for%20Individuals%2C%20Businesses%2C%20Society,-The%20Web%20is&text=That%20is%2C%20the%20accessibility%20barriers,older%20people) where you can learn more about accessibility and the internet.

### Accessibility Audits
🚨**Required** 

Accessibility audits run through the HTML and determine if the parts of the WCAG (web content accessibility guidelines ) that are implemented through HTML tags and attributes are present. They can do some checking for low vision/contrast stuff too.

You should run your deployed website pages through  at least on auditing tool. lighthouse's audit to check performance, accessibility, best practices and SEO scores. You should aim to get 85 or higher score on accessibility. 

**You should fix issues associated with:**
- contrast 
- aria labels
- alt text
- large images
- skewed images

**Lighthouse**
https://web.dev/measure/  If you have lower scores, read the report and follow the links to address the flagged issues. You can run this tool from Chrome Dev Tools too against your local machine, but chrome extensions can sometimes give you missing alt text on things like the grammarly plug in tracking pixel.

You want a score in the green for accessibility and should look at ways to get it to 100.


**[WAVE chrome](https://chrome.google.com/webstore/detail/wave-evaluation-tool/jbbplnpkjmmeebjpijfedlgcdilocofh?hl=en-US) extension**
Wave is developed by webaim.org and does a bit better at contrast issues and uses 2.1 guidelines

**Contrast Checkers**
- https://webaim.org/resources/contrastchecker/
- https://color.a11y.com/

### Keyboard Navigation
🚀 **merit & beyond**

Another way to accessibility test your site is to try to click on the browser URL and see what happens if you use the tab, arrow and enter keys. Does it work well or does the user get stuck? Check this in a couple browsers as the focus & active outlines are typically styled by the browser

The expected results for various keyboard entries and field types can be found [here](https://webaim.org/techniques/keyboard/#testing)

You can take a video of this testing if you want and convert it to a gif and paste that into your readme. Record something to yourself in a Slack direct message, then download it. Then you can use https://cloudconvert.com/mp4-to-gif to convert the mp4 to a gif and just paste it into the readme via GiHu, and it'll resolve itself.

### Chrome Vox Reader
🚀 **merit & beyond**

If you are really ambitious, you can use the [VoxReader](https://chrome.google.com/webstore/detail/screen-reader/kgejglhpjiefppelpmljglcjbhoiplfn?hl=en) extension in chrome to see what your site sounds like on a screen reader. It really drives home the need for good aria-labels & semantic HTML.

## Core Web Vitals
🚀 **merit & beyond**

SEO is greatly impacted by your core web vitals. The readout from https://web.dev/measure/ which is essentially a lighthouse audit gives your site scores in 4 categories. Ideally you want your site to be in the green for all 4 scores. web.dev has dedicated servers to test deployed sites without extensions that skew the results, so it's best to get results from this site.
 You should talk about the results for each section pay attention to 


### Cross Browser and Cross Device Testing
Create a table that lists out what devices, browsers, and operating system you tested your application on and a brief description of why you chose the mixture you did. The point is to prove that you looked at the site across various browsers, operating systems, and viewport breakpoints.

| TOOL / Device                 | BROWSER     | OS         | SCREEN WIDTH  |
|-------------------------------|-------------|------------|---------------|
| real phone: motog6            | chrome      | android    | XS 360 x 640  |
| browser stack: iPhone5s       | safari      | iOs        | XS 320 x 568  |
| dev tools emulator: pixel 2   | firefox     | android    | SM 411 x 731  |
| browserstack: iPhone 10x      | Chrome      | iOs        | SM 375 x 812  |
| browserstack: nexus 7 - vert  | Chrome      | android    | M 600 x 960   |
| real tablet: ipad mini - vert | safari      | iOs        | M 768 x 1024  |
| browserstack: nexus 7 - horiz | firefox     | android    | LG 960 x 600  |
| chrome emulator: ipad - horiz | safari      | iOs        | LG 1024 x 768 |
| browserstack                  | Chrome      | windows    | XL 1920 x 946 |
| real computer: mac book pro   | safari 12.1 | Mohave     | XL 1400 x 766 |
| browserstack                  | IE Edge 88  | windows 10 | XL 1920 x 964 |

## Automated Testing
🚀 **merit & beyond**

Whenever it is feasible, automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

If you did not run automating testing. State why you chose not to.

## Manual Testing
🚨**Required** 

You can track your test in various ways.  

But for any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. 

1. Markdown
>  A particularly useful form for describing your testing process is via scenarios, such as:
> 
>  **Register Page**
>  Go to the Register page: http://<YOUR APPP>.herokuapp.com/register
>    - [x] Try to submit the empty form and verify that an error message about the required fields appears
>    - [x] Try to submit the form with an invalid username format and verify that a relevant error message appears
>    - [x] Try to submit the form with an invalid password format and verify that a relevant error message appears
>    - [x] Try to submit the form with an existing username, should re-render page with relevant error message/warning
>    - [x] Try to submit the form with all inputs valid and verify that a success message appears and user is on profile page
>    - [x] Be logged in and go to register page url http://<YOUR APPP>.herokuapp.com/register, should have error saying you are already registered and be on profile page

2. Spreadsheet    
> Here is a [Manual Testing Template](https://docs.google.com/spreadsheets/d/189VpSeEG9oevSRhvb2WZl8zCk9L3s2iWQyrJ_1jjAGQ/edit?usp=sharing) that you can use as a starting point to keep track of your testing efforts. Make a copy of it in your own account and update as needed to reflect the browsers you are testing and features.  

3. GitHub Issues, Milestones & Boards
> You can also use agile tools in github to help track your testing and defects. Here's a document that I put together about that [process](https://docs.google.com/document/d/1nDS5tZeMO77Dfq85IZGMSV6C41XaPm9FwcpR3k-UTVc/edit?usp=sharing)

It's ok to spot check specific functionality across devices and browsers but each page should be viewed as a whole for each device/browser combo at least once.

A quick way to check if items are exceeding the screen width of a project is to run this javascript in the console for various screen emulations:

```
var docWidth = document.documentElement.offsetWidth;
[].forEach.call(document.querySelectorAll('*'),function(el){if(el.offsetWidth > docWidth){console.log(el);}});
```

## Defects
🚨**Required** 

You should mention  any  bugs or problems you discovered during your testing, even if you haven't addressed them yet.

Here is a [Defect Tracking Template](https://docs.google.com/spreadsheets/d/1tYB4X4wTCNEW_Y1no3hsGbclh2bLokl_I5Ev3s5EuJA/edit?usp=sharing) you use as a starting point to track defects. Make a copy of the sheet to your own account and update the Features sheet to match your project. 

Again, you could use [github issues](https://docs.google.com/document/d/1nDS5tZeMO77Dfq85IZGMSV6C41XaPm9FwcpR3k-UTVc/edit?usp=sharing) to track you defects. Or write them up with markdown.
 
## Defects of Note
🚀 **merit & beyond**

Some defects are more pesky than others. Highlight 3-5 of the bugs that drove you the most nuts and how you finally ended up resolving them.

## Outstanding Defects
🚨**Required** 

It's ok to not resolve all the defects you found as long as:
- it does not impact a user from completing a vital function on the website
- it only affects a very small subset of users
- is an extreme edge case that very few users would try
- there is an open issue against a framework, browser or technology used

If you know of something that isn't quite right, create an issue and link to it here and explain why you chose not to resolve it. 

Sometimes it's as simple, word wrapping issue that makes the site look odd at a certain screensize that you just didn't have time to fix due to the impending deadline it's best to mention it but note why you allowed it to go live: "Yes it looks odd, but it doesn't impact core functionality of the site." than to let the accessors think you didn't notice it. 


# Technologies Used
🚀 **merit & beyond**

In this section, you should mention the languages, frameworks, libraries, databases and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- If you included a js file that isn't your own, add it here.

- If you included a css file that isn't your own, add it here.

- Common 3rd party technologies to list:
  - wirefames
  - favicons
  - color palette images
  - fonts
  - CSS Frameworks
  - markdown tables
  - markdown table of contents
  
Please note, if this gets more than 5 items, you may want to break it down into logical subsections

## Programming Languages

- [CSS3](https://www.w3schools.com/w3css/default.asp) - used to style DOM appearance. 
- [HTML5](https://www.w3schools.com/html/default.asp) -  used to define DOM elements. 
- [JQuery](https://jquery.com) - used to initialize handlers for user interactive elements such as Bootstrap framework pieces like: check boxes, date pickers, menu toggles.
- [JavaScript](https://www.javascript.com/)  -  used to help handle challenge member entry.
- [Python](https://www.python.org/) the project back-end functions are written using Python. Django and Python is used to build route functions.
- [Flask](https://flask-doc.readthedocs.io/en/latest/) - python based templating language
- [mongodb](https://www.mongodb.com/cloud/atlas)- a fully-managed cloud database used to store manage and query data sets
- [Markdown](https://www.markdownguide.org/) Documentation within the readme was generated using markdown


## Frameworks, Libraries & Programs Used
🚀 **merit & beyond**

List out the tools you used with a link and a short description (this helps others figure out where to get the bonus points & reminds you what you used for your next project
- Balsamiq
- Coolors.co
- fontawesome
- gitpod
- github
- google fonts
- font awesome
- amiresponsive
- table of contents creator
- markdown table generator

## Tools
🚀 **merit & beyond**

In this section you should reference any 3rd party tools you used to make your project or readme. Wireframes, faviocon, github, color palette generators, heroku and any testing emulators are things that belong in this section.
[Back To Table of Contents](#table-of-contents)

## APIs
🚀 **merit & beyond**

List out the API's  you used for this project. 

# Deployment
🚨**Required** 

## Prerequisites
🚀 **merit & beyond**



If the user is required to have certain keys and credentials you should include this section with directions on how to get the necessary information. ex)

1. **Gmail Account:** In order to have verification and forgot password emails sent to registered users you need a
   google account. 
  - [create a gmail accoount](https://accounts.google.com/signup) 
  - [downgrade to less secure](https://myaccount.google.com/lesssecureapps?pli=1) after you are signed into the gmail account, downgrade to less secure
2. **Couldinary URL**
  - [create an account](https://cloudinary.com/)
  - go to the dashboard and copy your API environmental variable
   
    <img width="1230" alt="image" src="https://user-images.githubusercontent.com/23039742/213839829-b4f349b3-419d-4ea2-bbca-90cf3c663bba.png">     
 
## Fork and Clone the Repository
🚀 **merit & beyond**
To keep the main reposotory for this project clean, please fork the repostiory into your own account. GitHub has [forking directions](https://docs.github.com/en/get-started/quickstart/fork-a-repo#forking-a-repository) but here's what you might do:
1. login to your own gitHub account
2. navigate to [my repository](URL OF YOUR LIVE REPOSITORY)
3. In the top right corner of the page, click fork 

![image](https://user-images.githubusercontent.com/23039742/213840378-e785eaa0-712b-468c-bcda-64fde56eae44.png)

4. set yourself as the owner
5. change the name of the repo if you want
6. add a description if you want
7. choose what to copy, typicall the main branch only
8. click the snazy green button

![image](https://user-images.githubusercontent.com/23039742/213840549-5bef12ae-198e-412b-84b6-0cc718b6fa1d.png)

9. To get files to your local environment, you need to clone it: click the code button
10. Copy the url as needed (here's gitHub instructions)[https://docs.github.com/en/get-started/quickstart/fork-a-repo#cloning-your-forked-repository}


## Deploy Locally
🚨**Required** 

This section should describe the process someone would have to go through to get the local working in GitPod, or your preferred IDE. Start from installing the chrome extension then clicking the green gitpod button in THEIR FORKED repository, the enumerate the steps to walk them through the process as if they were brand new to this proccess. **Include screenshots** where applicable.

**Key points to cover** 
- Install required python packages: `pip3 install -r requirements.txt`
- Create env.py
- What to put in the env.py, don’t disclose real values
>  - EMAIL_HOST_PASSWORD=<YOUR_VALUE>
>  - DEFAULT_FROM_EMAIL=<YOUR_VALUE>
>  - EMAIL_USERNAME=<YOUR_VALUE>
>  - SECRET_KEY=<YOUR_VALUE>
>  - CLOUDINARY_URL=<YOUR_VALUE>
>  - DEV=True
- Apply Database Migrations so the database starts up `python3 manage.py migrate`
- Create a super user so you can add and inspect things via django admin  `python3 manage.py createsuperuser`
- Preload data: Sometimes you might want to include steps to create data in the admin or preload a data dump [coderwall blog](https://coderwall.com/p/mvsoyg/django-dumpdata-and-loaddata) has examples on how to dump data and load it which saves a bunch of time when deploying the application from a local database to a hosted database but you don’t  have to do this step
- Start the server `python3 run.py`


Write out the steps you take starting from cloning the repository in github or clicking a gitpod button to run your code locally. Test it out and make sure it works. This can be running from your IDE of choice like VSCode or PyCharm or GitPod.

You may want to re-watch the videos when writing up this section.

## Production Deployment (Heroku)
🚨**Required** 


This section should describe the process you went through to deploy the project to a server where anyone can access the url without your machine running. This is typically Heroku. **Include screenshots** if you think they would make the process easier. Start with getting an heroku account and then setting up databases and other packages.

If you have project settings required for Heroku, provide a table of the keys and values. Do not share your personal
keys but either cut them out of the screenshot or say <YOUR_VALUE> and include links on how the user would obtain such
values.

**Key points to cover** 
- creating new app
- setting app name
- setting region
- entering dreaded billing info
- subscribing to a plan
- setting up db
- adding environmental values- have a list or table so user has less chance of typos
>  - EMAIL_HOST_PASSWORD
>  - DEFAULT_FROM_EMAIL
>  - EMAIL_USERNAME
>  - SECRET_KEY
>  - CLOUDINARY_URL
>  - COLLECT_STATIC
- adding build packages
- deploy
- gitHub connection
- auto vs manual deploy
- monitor logs



# Credits
🚨**Required** 

To avoid plagiarism amd copyright infringement, you should mention any other projects, stackoverflow, videos, blogs, etc
that you used to gather imagery or ideas for your code even if you used it as a starting point and modified things.
Giving credit to other people's efforts and ideas that saved you time acknowledges the hard work others did.

- [Code Institute Template](https://github.com/Code-Institute-Org/python-essentials-template)
- The Template for the GUI for this project was provided by Code Institute. This allows for the Command line to be shown and used within the browser.

## Content

Use bullet points to list out sites you copied text from and cross-reference where those show up on your site

## Media

Make a list of sites you used images from. If you used several sites try to match up each image to the correct site. This includes attribution for icons if they came from font awesome or other sites, give them credit.

## Acknowledgments

This is the section where you refer to code examples, mentors, blogs, stack overflow answers and videos that helped you accomplish your end project. Even if it's an idea that you updated you should note the site and why it was important to your completed project.


![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for the mongo lessons. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Codeanywhere and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **April 3rd, 2023**

## Codeanywhere Reminders

# IDE

- **Connect to Mongo CLI on a IDE**
- navigate to your MongoDB Clusters Sandbox
- click **"Connect"** button
- select **"Connect with the MongoDB shell"**
- select **"I have the mongo shell installed"**
- choose option 4.4 for : **"Select your mongo shell version"**
- choose option: **"Run your connection string in your command line"**
- `mongo "mongodb+srv://<CLUSTER-NAME>.mongodb.net/<DBname>" --username <USERNAME>`
  - replace all `<angle-bracket>` keys with your own data
- enter password *(will not echo **\*\*\*\*** *on screen)\*

#### Clear screen in Mongo Shell:

- `cls`

#### Show all database collections:

- `show collections`

To run a frontend (HTML, CSS, Javascript only) application in Codeanywhere, in the terminal, type:

`python3 -m http.server`

A button should appear to click: _Open Preview_ or _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A button should appear to click: _Open Preview_ or _Open Browser_.

In Codeanywhere you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to _Account Settings_ in the menu under your avatar.
2. Scroll down to the _API Key_ and click _Reveal_
3. Copy the key
4. In Codeanywhere, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

---

Happy coding!
