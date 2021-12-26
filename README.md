# TestTask_Django-Celery
CSVFaker development flow


Commit id				    Description
------------------   24.12.2021   ------------------
[1.01] 				      -Created raw Django Project
					          -Installed packages & requirements.txt
                    -Created 2 apps (CSVFaker_main, base)
                    -Configured linters
                    -Created Git repo

[1.02]		          -Redefined default Django-User model 
                    -Created simple templates for login/logout
                    -Created model for Schema, Column with FK to Schema
                    -Defined path for storage .csv files for each Schema
                    -Designed templates: list of user's schemas, new scheme creation page
                    -Created inline formset for Schema+Column
                    -Implemented system to add columns dynamically on scheme creation page
                    -Added inline creation of Schema and multiple Columns for one
					          -Added urls for 'CRUD' of schemas
------------------   25.12.2021   ------------------
[1.03]		          -Installed Celery, and some other modules for development
					          -Created page for generating rows, for all available for user schemas
					          -Designed functions for generating rows on backend, and saving it to unique-named file
					          -Added possibility for downloading last created file for all schemas
					          -Added status bar for every scheme, which displays actual status of generating file on backend
					            There are 4 statuses : 	waiting (waiting for queue in celery)
												                      processing (backend processing data)
												                      ready (data generated, file can be downloaded)
												                      failed (something went wrong in the process of generation)
					          -All auth-logic classes moved to accounts app
					          -Added fields to Column model for setting range for some types of fields
					          -Rebuild big part of CSS for scheme-creation form
					          -Removed some redundant views
------------------   26.12.2021   ------------------
[1.04]              -Added remove button for additional columns on scheme creation page
                    -Configured Nginx
                    -Created Dockerfile and docker-compose files
                    -Made minor cosmetic changes
                    -Provided https connection to local server
                    -Designed volumes for Docker
                    -Reworked static files path's for deployment

[1.05]              -Project deployed on host-service
                    -Configured host machine for working with Django + Docker-compose
                    -Path's to media files reworked for normal downloading from the site
                    -Test task Done
