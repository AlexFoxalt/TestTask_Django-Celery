## CSVFaker development flow

# 24.12.2021
[1.01] 				
1. Created raw Django Project
2. Installed packages & requirements.txt
3. Created 2 apps (CSVFaker_main, base)
4. Configured linters
5. Created Git repo

[1.02]				
1. Redefined default Django-User model 
1. Created simple templates for login/logout
1. Created model for Schema, Column with FK to Schema
1. Defined path for storage .csv files for each Schema
1. Designed templates: list of user's schemas, new scheme creation page
1. Created inline formset for Schema+Column
1. Implemented system to add columns dynamically on scheme creation page
1. Added inline creation of Schema and multiple Columns for one
1. Added urls for 'CRUD' of schemas
## 25.12.2021
[1.03]				
1. Installed Celery, and some other modules for development
1. Created page for generating rows, for all available for user schemas
1. Designed functions for generating rows on backend, and saving it to unique-named file
1. Added possibility for downloading last created file for all schemas
1. Added status bar for every scheme, which displays actual status of generating file on backend.
    There are 4 statuses:
    1. waiting (waiting for queue in celery)
    1. processing (backend processing data)
    1. ready (data generated, file can be downloaded)
    1. failed (something went wrong in the process of generation)
1. All auth-logic classes moved to accounts app
1. Added fields to Column model for setting range for some types of fields
1. Rebuild big part of CSS for scheme-creation form
1. Removed some redundant views
## 26.12.2021
[1.04]              
1. Added remove button for additional columns on scheme creation page
1. Configured Nginx
1. Created Dockerfile and docker-compose files
1. Made minor cosmetic changes
1. Provided https connection to local server
1. Designed volumes for Docker
1. Reworked static files path's for deployment

[1.05]              
1. Project deployed on host-service
2. Configured host machine for working with Django + Docker-compose
3. Path's to media files reworked for normal downloading from the site
4. Test task Done

[1.06, 1.07, 1.08]
1. Made minor changes for correct work on the server

## Results

Tech tasks are in techtask.txt  
13/13 task done.  
11 tasks fully implemented   
2 tasks not fully implemented  

1. Issue 1 [task №5]: User can pick range only in 1st column. There is a problem with JavaScript on frontend, that should be fixed.
1. Issue 2 [task №12]: Https not provided, because of some problems with Docker Nginx and domain name registration.
