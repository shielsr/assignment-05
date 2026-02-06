# Assignment 5 - "Fanfictastic"

## Website URL
https://assignment-05-5qp8.onrender.com/

## Github Repo
https://github.com/shielsr/assignment-05/

## Documentation
1. [View setup instructions](setup.md)

2. [View Documentation](documentation.md)

## Project goal
The goal of the project is to allow writers to post 'fan fiction' stories about their favourite TV shows, films, books, etc.

## Features
### As a writer, the user can:
- Register, log in and out
- Write and edit stories
- Add chapters to their stories
- Publish and unpublish their stories
- Receive direct messages from other users

### As a reader, the user can:
- Register, log in and out
- Read stories from other users
- Send direct messages to authors

<br>
<br>



# Instructions on how to use the site

<br>

## Navbar

The navbar is responsive on desktop and mobile.

The buttons change based on logged-in status.

The buttons also change based on the user's role. Admins (i.e. 'staff' users in the `auth_user` table) can access the Django Admin dashboard.


<br>

## Register

Users can register via the form on /register.

Their passwords are hashed in the database. 

Once they fill out the form, they are directed to /login, where they can enter their new credentials.

<br>

## Logging into admin

To access the admin dashboard, use the username rob and password XXXXXXXX (see the version of readme.md in the .zip submission for the actual password)


<br>

## Homepage story list

The homepage shows a list of all the published stories.

<br>

## Writing stories

Logged-in users click 'New story' in the nav bar or 'Write a new story' in the Actions sidebar to open the form.

They fill out the form and submit it. This inserts a new row in the `order`table and a new row in the `pumpkin_design` table.

On the following /order page, the user can add another pumpkin to their order, which takes them to the /add page where they can create another design.

<br>

## Cancelling an order

Cancelling an order deletes that row from the `order` table and 'cascade-deletes' all related rows from the `pumpkin_design` table. 

Customers can cancel an order in two places:

1. On the /order page before they've submitted

2. On the /my-account page, where they can cancel an order as long as it hasn't been marked as 'Delivered' (at which point the Cancel button is not shown)

<br>

##  View my account

Only customers can see links to the /my-account page

Customers can view their previous orders here, along with in-progress ones. As mentioned above, they can cancel orders as long as their status is not `Delivered`.

<br>

## Admin

If a user logs in as an admin (see 'Logging in' above) they can see all orders that can be read from the `order` database table, along with the customer details and pumpkins connected to the order.

Admins can edit the status of orders. This updates the relevant entry in the database.

They can also see statistics.

NOTE: If an admin sets an order to `Delivered`, then the 'Cancel order' button no longer appears for the customer.

