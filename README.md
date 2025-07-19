# Pawlio_drf_api

### Developer: Lewis Bull

[Live Link]()

This repository holds the API for the Pawlio front end social media application. It was set up using Django REST Framework
[LINK TO REPO HERE]() and [LINK TO FRONTEND WEBSITE)

## User Stories

The backend of the project has a focus on the admin side of the website allowing admins to audit content that has been posted by users. It covers the following user stories:

 - As an admin, I want to be able to create, edit and delete users posts
 - As an admin, I want to be able to create, edit and delete users comments
 - As an admin, I want to be able to create, edit and delete users likes
 - As an admin, I want to be able to create, edit and delete users accounts

## Database

The below models were created to represent the database model structure of the application:

DATABASE IMAGE HERE

### User Model

 - The User model contains information about the user. It is part of the Django allauth library.
 - One-to-one relation with the Profile model owner field
 - ForeignKey relation with the Follower model owner and followed fields
 - ForeignKey relation with the Post model owner field
 - ForeignKey relation with the Comment model owner field
 - ForeignKey relation with the Like model owner field

### Profile Model
The Profile model contains the following fields: owner, name, content, created_at, updated_at and image
One-to-one relation between the owner field and the User model id field

### Post Model
The Post model contains the following fields: owner, created_at, updated_at, title, content, category and image
ForeignKey relation with the Comment model post field
ForeignKey relation with the Like model post field

### Follower Model
The Follower model contains the following fields: owner, followed and created_at
ForeignKey relation between the owner field and the User model id field
ForeignKey relation between the followed field and the User model post field

### Comment Model
The Comment model contains the following fields: owner, post, created_at, updated_at and content
ForeignKey relation between the owner field and the User model id field
ForeignKey relation between the post field and the User model post field

### Like Model
The Like model contains the following fields: owner, post and created_at
ForeignKey relation between to the User model id field
ForeignKey relation between the owner field and the User model id field
ForeignKey relation between the post field and the Post model post field

## Technologies Used

 - Python
 - Django

## Libraries and Tools:

- Cloudinary - To store static files such as images
- Git - Used for version control via the Visual Studio Code terminal to push the code to Github
- Github - Used to store the project code into a remote repository
- Heroku - Used to deploy and host the website into live environment
- Django REST Framework - Used to build the API for the backend
- Djano AllAuth - Used for user authentication
- Pillow - Used for image processing and validation
- Psycopg2 - Used as a PostgreSQL database adapter for python
- PostgreSQL - The deployed project uses a PostgreSQL database
- Pycodestyle - Used to validate the code to PEP8 Standards

## Validation

### Pycodestyle/PEP8 Validation

The library Pycodestlye was used to validate all of the python code as the PEP8 Online validator no longer exists, All code passes with no errors or warnings:

## Testing 

The Following tests were carriewd out on the backend app:

 - Manual Testing of User Stories

### Manual Testing

- As an admin, I want to be able to create, edit and delete users posts

|Test|Action|Expected Result|Actual Result|
|---|---|---|---|
|Posts|Create a post on the admin portal|The admin can create a post|Works as expected|
|Posts|Edit a post on the admin portal|The admin can edit a users post|Works as expected|
|Posts|Delete a post on the admin portal|The admin can delete a users post|Works as expected|

 - As an admin, I want to be able to create, edit and delete users comments

|Test|Action|Expected Result|Actual Result|
|---|---|---|---|
|Comments|Create a comment on the admin portal|The admin can create a comment|Works as expected|
|Comments|Edit a comment on the admin portal|The admin can edit a users comment|Works as expected|
|Comments|Delete a Comment on the admin portal|The admin can delete a users comment|Works as expected|

 - As an admin, I want to be able to create, edit and delete users likes

|Test|Action|Expected Result|Actual Result|
|---|---|---|---|
|Likes|Like a post on the admin portal|The admin can like a post|Works as expected|
|Likes|Edit a users liked posts on the admin portal|The admin can edit a users likes|Works as expected|
|Likes|Delete a like for a post on the admin portal|The admin can delete a users likes|Works as expected|
  
 - As an admin, I want to be able to create, edit and delete users accounts

|Test|Action|Expected Result|Actual Result|
|---|---|---|---|
|Profiles|Create a Profile on the admin portal|The admin can create a Profile|Works as expected|
|Profiles|Edit a Profile on the admin portal|The admin can edit a users Profile|Works as expected|
|Profiles|Delete a Profile on the admin portal|The admin can delete a users Profile|Works as expected|



