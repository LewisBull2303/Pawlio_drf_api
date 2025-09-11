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
- [Credits](#Credits)

## User Stories

The backend of the project has a focus on the admin side of the website allowing admins to audit content that has been posted by users. It covers the following user stories:

 - As an admin, I want to be able to create, edit and delete users posts
 - As an admin, I want to be able to create, edit and delete users comments
 - As an admin, I want to be able to create, edit and delete users likes
 - As an admin, I want to be able to create, edit and delete users accounts

## Database

The below models were created to represent the database model structure of the application:

<img width="1760" height="655" alt="Database Diagram" src="https://github.com/user-attachments/assets/b9e0f733-31a4-41dc-8f8e-d5765fd0808b" />


### User Model

 - The User model contains information about the user. It is part of the Django allauth library.
 - One-to-one relation with the Profile model owner field
 - ForeignKey relation with the Follower model owner and followed fields
 - ForeignKey relation with the Post model owner field
 - ForeignKey relation with the Comment model owner field
 - ForeignKey relation with the Like model owner field

### Profile Model
- The Profile model contains the following fields: owner, name, content, created_at, updated_at and image
- One-to-one relation between the owner field and the User model id field

### Post Model
- The Post model contains the following fields: owner, created_at, updated_at, title, content, category and image
- ForeignKey relation with the Comment model post field
- ForeignKey relation with the Like model post field

### Follower Model
- The Follower model contains the following fields: owner, followed and created_at
- ForeignKey relation between the owner field and the User model id field
- ForeignKey relation between the followed field and the User model post field

### Comment Model
- The Comment model contains the following fields: owner, post, created_at, updated_at and content
- ForeignKey relation between the owner field and the User model id field
- ForeignKey relation between the post field and the User model post field

### Like Model
- The Like model contains the following fields: owner, post and created_at
- ForeignKey relation between to the User model id field
- ForeignKey relation between the owner field and the User model id field
- ForeignKey relation between the post field and the Post model post field

## Technologies Used

 - Python
 - Django

## Libraries and Tools:

- [APITestCase](https://www.django-rest-framework.org/api-guide/testing/) - Django Rest Framework APITestCase was used for automated testing
- [Cloudinary](https://cloudinary.com/) - To store static files such as images
- [Coverage](https://coverage.readthedocs.io/en/6.4.4/) - Used to create a report for automated tests
- [Dbdiagram.io](https://dbdiagram.io/home) used for the database diagram
- [Git](https://git-scm.com/) - Used for version control via the Visual Studio Code terminal to push the code to Github
- [Github](https://github.com/) - Used to store the project code into a remote repository
- [Heroku](https://www.heroku.com/) - Used to deploy and host the website into live environment
- [Django REST Framework](https://www.django-rest-framework.org/) - Used to build the API for the backend
- [Djano AllAuth](https://django-allauth.readthedocs.io/en/latest/index.html) - Used for user authentication
- [Pillow](https://pillow.readthedocs.io/en/stable/) - Used for image processing and validation
- [Psycopg2](https://www.psycopg.org/docs/) - Used as a PostgreSQL database adapter for python
- [PostgreSQL](https://www.postgresql.org/) - The deployed project uses a PostgreSQL database
- [Pycodestyle](https://pypi.org/project/pycodestyle/) - Used to validate the code to PEP8 Standards

## Validation

### Pycodestyle/PEP8 Validation

The library Pycodestlye was used to validate all of the python code as the PEP8 Online validator no longer exists, All code passes with no errors or warnings:

<details>
 <summary>Example Output</summary>

Example output if there are issues with a file:
<img width="798" height="241" alt="image" src="https://github.com/user-attachments/assets/4548cfb4-7f29-434a-a461-c077d5675f2e" />

</details>

<details>
 <summary>Comments</summary>

<img width="842" height="181" alt="image" src="https://github.com/user-attachments/assets/31717e8c-e5e7-4b03-9a70-18a3969dc9aa" />
<img width="879" height="125" alt="image" src="https://github.com/user-attachments/assets/1800d2d4-222b-4c1b-bea4-6f4a91929ce6" />
<img width="820" height="110" alt="image" src="https://github.com/user-attachments/assets/4747b87d-0428-4cb9-b30a-9347b203c023" />
<img width="876" height="101" alt="image" src="https://github.com/user-attachments/assets/ed3cbb93-8d12-4746-80e1-bd7ed8907ba3" />
<img width="804" height="44" alt="image" src="https://github.com/user-attachments/assets/fff42bde-b873-406d-a7fa-63e4e8932302" />
<img width="810" height="77" alt="image" src="https://github.com/user-attachments/assets/4cbb078b-eee0-463c-84de-8a5a52122965" />
<img width="816" height="78" alt="image" src="https://github.com/user-attachments/assets/b8247767-12f7-4cf7-a201-7d03d1e977d0" />

</details>

<details>
 <summary>Drf-API</summary>

<img width="849" height="85" alt="image" src="https://github.com/user-attachments/assets/6793d858-f798-41ed-a6bd-37aadac22c3f" />
<img width="864" height="85" alt="image" src="https://github.com/user-attachments/assets/5a33357c-d34a-4b78-ac57-28bb86590996" />

There is one error for the settings.py, however this is unfixable due to the name of the django variable being too long of a name natually, images below:

<img width="839" height="88" alt="image" src="https://github.com/user-attachments/assets/7e3b33d6-6703-437a-b364-75f6f3cf5b55" />
<img width="952" height="98" alt="image" src="https://github.com/user-attachments/assets/72887cb0-4736-402e-86a7-2a9b56402df7" />

<img width="808" height="59" alt="image" src="https://github.com/user-attachments/assets/176bc991-e95c-4089-8d8d-ad4cd3b931f0" />
<img width="825" height="51" alt="image" src="https://github.com/user-attachments/assets/b506d477-31d7-4745-97bb-f8f466536367" />
<img width="820" height="55" alt="image" src="https://github.com/user-attachments/assets/6aab49dc-c632-4c54-af54-6e7ad306c4e5" />

</details>

<details>
 <summary>Followers</summary>

<img width="816" height="44" alt="image" src="https://github.com/user-attachments/assets/982dc116-6ff4-4ea1-b20b-bf8ddc26d107" />
<img width="813" height="56" alt="image" src="https://github.com/user-attachments/assets/8ebd82e7-427d-4f77-a202-d5b4a91b8804" />
<img width="835" height="45" alt="image" src="https://github.com/user-attachments/assets/8288750e-36a9-47b3-8d8b-f0742ade53c7" />
<img width="872" height="48" alt="image" src="https://github.com/user-attachments/assets/0286cdc5-2def-43f8-b2a2-b192d3424561" />
<img width="853" height="47" alt="image" src="https://github.com/user-attachments/assets/acd0c697-56b0-4446-89dd-ec9c24ef9a2c" />
<img width="819" height="51" alt="image" src="https://github.com/user-attachments/assets/8d45aedd-87f5-4039-8419-3743250fbcf0" />
<img width="837" height="60" alt="image" src="https://github.com/user-attachments/assets/ce8371a7-19eb-42f8-bede-8ea763cc7e91" />

</details>

<details>
 <summary>Likes</summary>

<img width="783" height="48" alt="image" src="https://github.com/user-attachments/assets/615bc500-267d-40f7-9ff0-2e50c182f1ed" />
<img width="784" height="45" alt="image" src="https://github.com/user-attachments/assets/be671e95-8e51-46ad-af8d-9081af9e87bd" />
<img width="783" height="46" alt="image" src="https://github.com/user-attachments/assets/c68cc1dc-196d-43ff-85c5-fffcd5976aef" />
<img width="901" height="52" alt="image" src="https://github.com/user-attachments/assets/8aa6acfb-166a-416d-9548-59d9d2032dfa" />
<img width="787" height="48" alt="image" src="https://github.com/user-attachments/assets/fdfe791b-d38d-44cd-8f4b-13baa2fc3c2e" />
<img width="762" height="45" alt="image" src="https://github.com/user-attachments/assets/d4ce4410-47b1-4d24-b636-c9337b71a32c" />
<img width="782" height="57" alt="image" src="https://github.com/user-attachments/assets/25a2e522-dbdf-4914-90a7-55295876ea7d" />

</details>

<details>
 <summary>Posts</summary>

<img width="793" height="42" alt="image" src="https://github.com/user-attachments/assets/4a8ff2c1-a38c-406e-9dd1-96dbe15e2f9f" />
<img width="823" height="39" alt="image" src="https://github.com/user-attachments/assets/626feec7-fa06-4a6d-b520-e6fcf12f164f" />
<img width="804" height="48" alt="image" src="https://github.com/user-attachments/assets/35a53505-50c8-4bce-b2b2-5b1eaf369729" />
<img width="852" height="49" alt="image" src="https://github.com/user-attachments/assets/f9733b31-6f38-46df-80f4-da4c9299055e" />
<img width="793" height="49" alt="image" src="https://github.com/user-attachments/assets/ca627ef1-b05a-48bc-bf6e-a5f16f748422" />
<img width="798" height="56" alt="image" src="https://github.com/user-attachments/assets/8c8b8b34-0853-46a3-9482-3e34ad7b8451" />
<img width="814" height="45" alt="image" src="https://github.com/user-attachments/assets/8d9cd2b9-fc9e-4b0a-8baf-92e05a9c4728" />

</details>

<details>
 <summary>Profiles</summary>

<img width="881" height="48" alt="image" src="https://github.com/user-attachments/assets/9b9f87c5-e81e-4017-ac4e-538f229f50d5" />
<img width="831" height="59" alt="image" src="https://github.com/user-attachments/assets/30560f2f-fc95-466f-be77-96881e570556" />
<img width="816" height="47" alt="image" src="https://github.com/user-attachments/assets/5ed462ad-1838-4ce0-a704-fa744bf21c78" />
<img width="859" height="52" alt="image" src="https://github.com/user-attachments/assets/6535bd37-9e51-4913-b14c-8bbd1b0e7405" />
<img width="851" height="51" alt="image" src="https://github.com/user-attachments/assets/4bdc2b8d-5ad4-40dd-ba45-24b9a9a204bc" />
<img width="820" height="59" alt="image" src="https://github.com/user-attachments/assets/42be8250-50cb-40a7-ac89-7db224eba7da" />
<img width="812" height="49" alt="image" src="https://github.com/user-attachments/assets/9f7546be-54a2-41c4-9c94-4c7677097090" />

</details>

<details>
 <summary>Saves</summary>

<img width="792" height="53" alt="image" src="https://github.com/user-attachments/assets/e1fd6484-90b8-4af5-a9e5-a99cf68ca5d3" />
<img width="773" height="63" alt="image" src="https://github.com/user-attachments/assets/456718af-e8af-4d06-8891-81bcd422873f" />
<img width="787" height="52" alt="image" src="https://github.com/user-attachments/assets/689a9c39-4966-4fe6-acd0-7fc9a91fc895" />
<img width="824" height="51" alt="image" src="https://github.com/user-attachments/assets/486ba7eb-9ec3-4402-a53e-2fdfb17c2747" />
<img width="817" height="42" alt="image" src="https://github.com/user-attachments/assets/ef40cc1b-20ab-44d9-8896-2805ec3732d9" />
<img width="776" height="45" alt="image" src="https://github.com/user-attachments/assets/6b4a4554-1345-4472-906c-c2ad1582df97" />
<img width="798" height="46" alt="image" src="https://github.com/user-attachments/assets/dc428ddd-6a67-47c2-8f7b-de68b20179be" />

</details>

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

<details>
 <summary>Images - Posts</summary>

<img width="724" height="474" alt="image" src="https://github.com/user-attachments/assets/ca8db91a-5614-4027-9c5f-9480163451b9" />
<img width="797" height="662" alt="image" src="https://github.com/user-attachments/assets/ecffec5d-2ab1-49cd-8429-63a112cf3f2d" />
<img width="1237" height="525" alt="image" src="https://github.com/user-attachments/assets/7daab795-4ce5-491c-9f80-0a448c33a132" />
<img width="989" height="352" alt="image" src="https://github.com/user-attachments/assets/8274ae8e-07a5-4963-9466-8a00f5880c2b" />
<img width="311" height="81" alt="image" src="https://github.com/user-attachments/assets/e8f74f86-17b4-4e04-9329-2f96e6645d73" />


</details>

 - As an admin, I want to be able to create, edit and delete users comments

|Test|Action|Expected Result|Actual Result|
|---|---|---|---|
|Comments|Create a comment on the admin portal|The admin can create a comment|Works as expected|
|Comments|Edit a comment on the admin portal|The admin can edit a users comment|Works as expected|
|Comments|Delete a Comment on the admin portal|The admin can delete a users comment|Works as expected|

<details>
 <summary>Images - Comments</summary>

<img width="1222" height="599" alt="image" src="https://github.com/user-attachments/assets/031c6fd4-1a67-484a-80b4-69eabca06d75" />
<img width="1214" height="652" alt="image" src="https://github.com/user-attachments/assets/d293d148-6450-47a0-9aa7-539ea45e6fe5" />
<img width="1509" height="598" alt="image" src="https://github.com/user-attachments/assets/4da4ffa1-d1cd-4704-8ed3-1375257cb66f" />

</details>


 - As an admin, I want to be able to create, edit and delete users likes

|Test|Action|Expected Result|Actual Result|
|---|---|---|---|
|Likes|Like a post on the admin portal|The admin can like a post|Works as expected|
|Likes|Edit a users liked posts on the admin portal|The admin can edit a users likes|Works as expected|
|Likes|Delete a like for a post on the admin portal|The admin can delete a users likes|Works as expected|

<details>
 <summary>Images - Likes</summary>

<img width="948" height="418" alt="image" src="https://github.com/user-attachments/assets/c6a6ce5b-9938-4b4e-8965-4a95def36335" />
<img width="684" height="462" alt="image" src="https://github.com/user-attachments/assets/f0e90605-69f1-46c9-ad23-d803472f5a03" />
<img width="952" height="394" alt="image" src="https://github.com/user-attachments/assets/343e811e-53ae-4df2-a222-b2eedf05b8c7" />
<img width="1545" height="511" alt="image" src="https://github.com/user-attachments/assets/ce1f33fa-f132-466e-aaa6-be9cd0cda62d" />

</details>
  
 - As an admin, I want to be able to create, edit and delete users accounts

|Test|Action|Expected Result|Actual Result|
|---|---|---|---|
|Profiles|Create a Profile on the admin portal|The admin can create a Profile|Works as expected|
|Profiles|Edit a Profile on the admin portal|The admin can edit a users Profile|Works as expected|
|Profiles|Delete a Profile on the admin portal|The admin can delete a users Profile|Works as expected|

<details>
 <summary>Images - Profiles</summary>

<img width="1482" height="687" alt="image" src="https://github.com/user-attachments/assets/d191f30c-d04b-46b0-8519-0424d87b8c3a" />
<img width="1556" height="703" alt="image" src="https://github.com/user-attachments/assets/d280c02b-d405-41ba-9bc4-3fd05895945f" />
<img width="956" height="375" alt="image" src="https://github.com/user-attachments/assets/85d5c6d9-0aae-40d7-a746-2ff00ef90bcb" />
<img width="1293" height="446" alt="image" src="https://github.com/user-attachments/assets/e404de27-ad4b-4f7e-a69f-5fd8cf945098" />

</details>

## Automated Testing

Automated testing was done using the Django Rest Framework APITestCase. The report for the overall testing was created using the coverage tool:

<img width="869" height="482" alt="image" src="https://github.com/user-attachments/assets/1f7e3374-2573-4537-af4f-9c27741bbedb" />

<details>
 <summary>Detailed Coverage Report</summary>

<img width="1286" height="901" alt="image" src="https://github.com/user-attachments/assets/5a410176-670b-4330-a3a0-aff4b5d7cc1f" />

<img width="1240" height="877" alt="image" src="https://github.com/user-attachments/assets/0a2924c7-8565-43ab-9a5f-ede6208f2630" />

<img width="1194" height="877" alt="image" src="https://github.com/user-attachments/assets/e60837b8-cf8c-406c-a70e-e9868c373c0f" />

<img width="1367" height="849" alt="image" src="https://github.com/user-attachments/assets/4c4c5afd-e689-4742-be06-a14697fb9a70" />

</details>

## Deployment

### Heroku Deployment

This application has been deployed from Github using Heroku. Here's how:

1. Create an account at heroku.com
2. Create an app, give it a name for such as ci-pp4-the-wave, and select a region
3. Under resources search for postgres, and add a Postgres database to the app

### Heroku Postgres
1. Note the DATABASE_URL, this can be set as an environment variable in Heroku and your local deployment(env.py)
2. Install the plugins dj-database-url and psycopg2-binary.
3. Run pip3 freeze > requirements.txt so both are added to the requirements.txt file
4. Create a Procfile with the text: web: gunicorn the_wave.wsgi
5. In the settings.py ensure the connection is to the Heroku postgres database, no indentation if you are not using a separate test database. I store mine in env.py
6. Ensure debug is set to false in the settings.py file
7. Add localhost, and ci-pp4-the-wave.herokuapp.com to the ALLOWED_HOSTS variable in settings.py
8. Run "python3 manage.py showmigrations" to check the status of the migrations
9. Run "python3 manage.py migrate" to migrate the database
10. Run "python3 manage.py createsuperuser" to create a super/admin user
11. Run "python3 manage.py loaddata categories.json" on the categories file in products/fixtures to create the categories
12. Run "python3 manage.py loaddata products.json" on the products file in products/fixtures to create the products
13. Install gunicorn and add it to the requirements.txt file using the command pip3 freeze > requirements.txt
14. Ensure the following environment variables are set in Heroku
15. Connect the app to GitHub, and enable automatic deploys from main if you wish
16. Click deploy to deploy your application to Heroku for the first time
17. Click on the link provided to access the application
18. If you encounter any issues accessing the build logs is a good way to troubleshoot the issue

### Forking the Repository
To fork the repository by following these steps:

1. Go to the GitHub repository
2. Click on Fork button in upper right hand corner

### Clone Repository
You can clone the repository by following these steps:

1. Go to the GitHub repository
2. Locate the Code button above the list of files and click it
3. Select if you prefer to clone using HTTPS, SSH, or Github CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash
5. Change the current working directory to the one where you want the cloned directory
6. Type git clone and paste the URL from the clipboard ($ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY)
7. Press Enter to create your local clone.

## Credits:

### Images

- Images for the default post and default profile picture were taken from the Code Institute's Django REST API walkthrough project [Moments](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+RA101+3/courseware/70a8c55db0504bbdb5bcc3bfcf580080/953cd4e5015f483bb05263db3e740e19/)

### Code

This whole project was created based on the Code Institute's Django REST API walkthrough project [Moments](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+RA101+3/courseware/70a8c55db0504bbdb5bcc3bfcf580080/953cd4e5015f483bb05263db3e740e19/) which was an amazing learning experience for me and helped me a great deal to understanding many errors I faced and issues I had to overcome

### Acknowledgements

First and foremost, I would like to give a special thank you to my wonderful fiancée Jasmine, whose support has made managing a full-time job, Open University, and Code Institute submissions possible.
Another special thank you to my Friend Dylan who helped to test the final deployed project

Special thank you as well to my Mentor, Mo Shami, whos help and guidance has been a huge help
