# My design decisions
## User stories

# Personas
* Authors
* Readers

<br>

### Reader user stories:

#### 1. Write stories
[MUST] As an author, I want to write fan fiction stories online, so I can share them with friends.

#### 2. Only publish when ready
[MUST] As an author, I want to save a draft of my story, so I can publish it only when it is ready.

#### 3. Multiple chapters per story
[MUST] As an author, I want to split my story into chapters, so I can publish one chapter at a time.

#### 4. Reorder chapters
[MUST] As an author, I want to be able to reorder my chapters, so I can change the order of chapters in my short story collections.

#### 5. Cover images
[MUST] As an author, I want to add images, so I can include covers for my stories.

#### 6. Editing
[MUST] As an author, I want to edit my published stories, so I can correct typos.

#### 7. Genres
[MUST] As an author, I want to put my stories in cateogires, so readers can see what genre they are.

#### 8. Sending and receiving messages
[MUST] As an author, I want to receive messages from other users, so I can get feedback on my work.

#### 9. Archiving messages
[MUST] As an author, I want to archive messages, so I can hide unfavourable feedback.

<br>

### Author user stories:

#### 1. Story metadata
[MUST] As a reader, I want to see a story summary and metadata, so I can judge whether the story would be interesting to read.

#### 2. List stories from an author
[MUST] As a reader, I want to see a list of all stories from a user, so I can read all works from my favourite authors.

#### 3. Message authors
[MUST] As a reader, I want to send messages to authors, so I can give them feedback on their work.

<br>

### Future stories:


#### 1. Add co-authors
[SHOULD] As an author, I want to add additional authors to my stories, so I can show who my co-authors are.

#### 2. Search functionality
[SHOULD] As a reader, I want to search for stories by genre or fandom, so I can find stories I want to read.

#### 3. Mark as read
[MUST] As a reader, I want to mark stories as 'read', so I can keep track of what I've read.

<br>
<br>

## Content

The site will include:
- Homepage showing published stories, links, and possible user actions
- Full authentication (register, login, logout, etc)
- Profile/account page
- Private messaging inbox and archive

For authors:
- A 'new story' page for creating new stories
- An editable detail page showing metadata for a story, as well as links to chapters
- 'Add a chapter' page, allowing the author to write more chapters
- A page for deleting stories

For readers:
- Story detail pages, featuring metadata about the story
- Chapter pages, with internal story navigation
- A page listing all of an author's stories

<br>
<br>

## Prioritised tasks:

?????????

<br>
<br>

## Wireframes

I created basic wireframes in Figma for mobile and desktop, with the mobile layout responsively catering for tablets too.

<br>
<br>

## Databases and tables

### ERD



#### 
[MUST] 

#### 
[MUST] 

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
- Fixed bug where not uploading a cover image crashed everything
- Set up Cloudinary and updated the Profile model, removing references to Pillow
- Changed Story model to work with Cloudinary and updated templates
- Wrote unit tests for the Story app
- Tidied up formatting, CSS etc, and cleared up the majority of 'Problems' from the Terminal
- Wrote docstrings for all model classes



Future tests:
With more time, I wanted to write tests for all models across all 3 apps (stories, user and mails). But, given that I was running out of time, I focused on the models for just the stories app. I also installed Coverage. With more time, I would ensure testing was set up for all apps, models, etc.

test_stories_list_view(self):
This didn't work. Then I realised that stories are created as draft by default, so wouldn't appear on the page. So, I researched and add an if statement to settings.py

test_create_post_view(self):
The genres field is a messy one. I had to figure out how to do dummy data here.
Used print(response.context['form'].errors)  to see what error messages the page was throwing.

test_update_story_view(self)
Again I had to add all required fields here.  The status was the new required field. I had to factor that into this test.