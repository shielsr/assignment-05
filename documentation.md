# My development process
## How I went about it

The following is a step-by-step account of how I did the project, which closely corresponds with the series of commits I made to the repo.

- Set up new Git in GitHub and cloned into VSCode
- Brainstormed initial ideas for the assignment
- Wrote user stories
- Designed the database schema
- Set up the Django environment as per the tutorials
- Created superuser
- Created the first model, Story, and added some stories via a shell
- Updated the homepage to loop through stories
- Set up Registration page and successfully registered new users
- Installed Crispy Forms with Bootstrap styling
- Created login and logout pages and completed user authentication setup
- Added editable profile pages and resizable profile picture upload
- Set up class-based views for CRUD operations
- Pagination added
- New page showing all of a user's stories
- Set up a burner email account and created the Password Reset infrastructure
- Swapped Bootstrap 5 for Bootstrap 4 to catch some legacy style classes
- Created a new form for adding chapters, and allowed authors to add chapters to their stories
- Added publish/unpublish functionality
- Set it up so that if a book was published once & then unpublished, the original publish date would persist
- Created a new app called Mails to handle user-to-user messaging (as per the assignment requirements)
- Continued updating the UI
- Added a word count using javascript to the Add chapter section
- On the story detail page, I used SortableJS to set up a drag-and-drop reordering of chapters
- Went through the process of deploying to Render.com