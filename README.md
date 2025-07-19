# Pawlio_drf_api

### Developer: Lewis Bull

[Live Link](https://cl-pp5-pawlio-ba8f8e344581.herokuapp.com/)

This repository holds the API for the Pawlio front end social media application. It was set up using Django REST Framework
[Link to repository here](https://github.com/LewisBull2303/CL_PP5_Pawlio) and [Link to the website here](https://cl-pp5-pawlio-ba8f8e344581.herokuapp.com/)

## Table of Content

- [User Stories](#user-storeis)
- [Database](#database)
- [Technologies Used](#technologies-used)
- [Validation](#validation)
- [Testing](#testing)

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
- Coverage - Used to do automated tests and create a report for said tests
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


## Automated Testing

Automated testing was done using the Django Rest Framework APITestCase. The report for the overall testing was created using the coverage tool:

<img width="1314" height="188" alt="image" src="https://github.com/user-attachments/assets/bcc15b98-89e4-4ceb-9e05-41f513c516f8" />

Detailed Coverage Report:

Name                                                              Stmts   Miss  Cover
-------------------------------------------------------------------------------------
comments\__init__.py                                                  0      0   100%
comments\admin.py                                                     1      0   100%
comments\apps.py                                                      4      0   100%
comments\migrations\0001_initial.py                                   7      0   100%
comments\migrations\0002_alter_comment_content.py                     4      0   100%
comments\migrations\__init__.py                                       0      0   100%
comments\models.py                                                   13      1    92%
comments\serializers.py                                              20      2    90%
comments\tests.py                                                    52      0   100%
comments\urls.py                                                      3      0   100%
comments\views.py                                                    17      0   100%
drf_api\__init__.py                                                   0      0   100%
drf_api\permissions.py                                                6      0   100%
drf_api\serializers.py                                                7      0   100%
drf_api\settings.py                                                  37      1    97%
drf_api\urls.py                                                       4      0   100%
drf_api\views.py                                                     12      5    58%
env.py                                                                6      0   100%
followers\__init__.py                                                 0      0   100%
followers\admin.py                                                    1      0   100%
followers\apps.py                                                     4      0   100%
followers\migrations\0001_initial.py                                  7      0   100%
followers\migrations\__init__.py                                      0      0   100%
followers\models.py                                                  11      1    91%
followers\serializers.py                                             14      2    86%
followers\tests.py                                                   37      0   100%
followers\urls.py                                                     3      0   100%
followers\views.py                                                   14      0   100%
likes\__init__.py                                                     0      0   100%
likes\admin.py                                                        1      0   100%
likes\apps.py                                                         4      0   100%
likes\migrations\0001_initial.py                                      7      0   100%
likes\migrations\__init__.py                                          0      0   100%
likes\models.py                                                      12      1    92%
likes\serializer.py                                                  13      2    85%
likes\tests.py                                                       40      0   100%
likes\urls.py                                                         3      0   100%
likes\views.py                                                       14      0   100%
manage.py                                                            11      2    82%
posts\__init__.py                                                     0      0   100%
posts\admin.py                                                        3      0   100%
posts\apps.py                                                         4      0   100%
posts\migrations\0001_initial.py                                      7      0   100%
posts\migrations\0002_alter_post_content_alter_post_image.py          4      0   100%
posts\migrations\0003_alter_post_content.py                           4      0   100%
posts\migrations\0004_alter_post_category_alter_post_content.py       4      0   100%
posts\migrations\__init__.py                                          0      0   100%
posts\models.py                                                      15      1    93%
posts\serializers.py                                                 43     12    72%
posts\tests.py                                                       46      0   100%
posts\urls.py                                                         3      0   100%
posts\views.py                                                       20      0   100%
profiles\__init__.py                                                  0      0   100%
profiles\admin.py                                                     3      0   100%
profiles\apps.py                                                      4      0   100%
profiles\migrations\0001_initial.py                                   7      0   100%
profiles\migrations\0002_alter_profile_content.py                     4      0   100%
profiles\migrations\__init__.py                                       0      0   100%
profiles\models.py                                                   18      1    94%
profiles\serializers.py                                              22      1    95%
profiles\tests.py                                                    33      0   100%
profiles\urls.py                                                      3      0   100%
profiles\views.py                                                    16      0   100%
-------------------------------------------------------------------------------------
TOTAL                                                               652     32    95%

