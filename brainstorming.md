# What to build
    Fan fiction (fanfic) story website

# Goals

## User mgmt:
    Registration
    Login system
    Update personal and contact details
    Password recovery

## Data storage:
    Project details (title, summary, fandom, rating, co-authors, status, content )
    Inbox functionality
        Send messages
        Receive messages
        Archive messages
    Users can store and categorise their data (what would this be? User can see their own projects, edit and delete them, etc?)

## Security features:
    Data encryption methodologies to ensure sensitive data, passwords etc
    User roles (author, reader, admin)


# Personas
* Authors
* Readers

# User stories
As a .... I want to ... so that I ....

As an author, I want to write fan fiction stories online, so I can share them with friends.
As an author, I want to save a draft of my story, so I can publish it only when it is ready.
As an author, I want to split my story into chapters, so I can publish one chapter at a time.
As an author, I want to add additional authors to my stories, so I can show who my co-authors are.
As an author, I want to add images, so I can include covers for my stories.
As an author, I want to edit my published stories, so I can correct typos.
As an author, I want to receive messages from other users, so I can get feedback on my work.
As an author, I want to put my stories in cateogires, so readers can see what genre they are.
As an author, I want to archive messages, so I can hide unfavourable feedback.

As a reader, I want to search for stories by genre or fandom, so I can find stories I want to read.
As a reader, I want to send messages to authors, so I can give them feedback on their work.
As a reader, I want to mark stories as 'read', so I can keep track of what I've read.


# Tables
* User
* Profile
* Story
* Chapter
* Tag
* Coversation
* Message


# Relationships
User -> Profile         One to one
User -> Story           One to many
Story -> Chapter        One to many
Story -> Tag            Many to many
User -> Conversation    Many to many
Conversation -> Message One to many

