# Testing

## Full testing was performed on the following devices:

Desktop:
  * 4k resolution, 28-inch monitor
Mobile Devices:
  * OnePlus 9-Pro

Each device tested the site using the following browsers:
* Google Chrome
* Microsoft Edge
* Firefox
* Brave

## Home Page

| Feature        | Expected Outcome                                       | Testing Performed                                        | Result                      | Pass/Fail |
|----------------|--------------------------------------------------------|----------------------------------------------------------|-----------------------------|-----------|        
| About Sections | About section would be pulled from the database and displayed | Through views.py, pulled the data and displayed it on the frontend | All sections were displayed | Pass      |
| Hero Image     | Image would be connected properly and displayed on the index page | Tested with multiple different images                    | Images were displayed as they should be | Pass |

## Navigation

| Feature            | Expected Outcome                                 | Testing Performed                    | Result                          | Pass/Fail |
|--------------------|--------------------------------------------------|--------------------------------------|---------------------------------|-----------| 
| Logo link          | When clicked on the logo, it would take you to the home page | Clicked on the logo                   | Ended up on the Home Page       | Pass      |
| Navigation Links   | Each would take you to the corresponding site    | Clicked on each link                 | Ended where I should have       | Pass      |
| Burger Menu        | Small icon should appear when the screen gets too small | Shrank the window on desktop, tested on a phone | Small burger icon appears on smaller screens | Pass |

## Gallery

| Feature          | Expected Outcome                                  | Testing Performed                    | Result                          | Pass/Fail |
|------------------|---------------------------------------------------|--------------------------------------|---------------------------------|-----------| 
| Image slideshow  | Images could be replaced by clicking on the arrows next to them | Used the two buttons to see all of the images | Images would change when buttons were clicked | Pass |
| Review Section   | Reviews would be pulled randomly from the database and be displayed on the screen | Wrote multiple reviews to see them change | Reviews updated every 20 seconds as intended | Pass |
| Review Form      | User can leave reviews                            | Wrote a few reviews                  | Reviews would be entered in the database and later displayed in the review section | Pass |
| Login Message    | Users who were not logged in would see the message | Logged out of the account            | Message was displayed properly  | Pass      |

## Footer

| Feature             | Expected Outcome                        | Testing Performed             | Result               | Pass/Fail |
|---------------------|-----------------------------------------|-------------------------------|----------------------|-----------| 
| Social Media Links  | Links would take the user to the page   | Clicked on all of the links   | Links worked as intended | Pass      |

## Contact

| Feature        | Expected Outcome                                      | Testing Performed     | Result               | Pass/Fail |
|----------------|-------------------------------------------------------|-----------------------|----------------------|-----------| 
| Contact Form   | Filled out form would be sent to designated email     | Filled out the form   | Email arrived where it should | Pass | 

## Login/Register

| Feature       | Expected Outcome                                      | Testing Performed                    | Result                          | Pass/Fail |
|---------------|-------------------------------------------------------|--------------------------------------|---------------------------------|-----------|
| Forms         | Authentication system would be available for the user | Made an account and logged in with it | Account was created and I was able to use the credentials later to log in to it | Pass |

## Profile

| Feature               | Expected Outcome                                       | Testing Performed                    | Result                          | Pass/Fail |
|-----------------------|--------------------------------------------------------|--------------------------------------|---------------------------------|-----------|
| Information Section   | User would be able to see information they have inputted before | Made a few accounts with different information | All accounts had correct information displaying | Pass |
| Edit Information      | User would be able to edit information previously written | Used multiple accounts to change information | All accounts had their information changed and saved in the database | Pass |
| Review Section        | User can see reviews they have left in the past        | Written reviews                      | All reviews were shown          | Pass      |
| Edit/Delete Reviews   | User can manipulate the reviews they have              | Changed/deleted a few reviews        | Everything worked as intended   | Pass      |
| Delete Profile        | User can delete their profile if they wish to          | Deleted dummy profiles               | All were deleted along with all of the reviews | Pass |

## Other Features

| Feature          | Expected Outcome                                      | Testing Performed                    | Result                          | Pass/Fail |
|------------------|-------------------------------------------------------|--------------------------------------|---------------------------------|-----------|
| Success Message  | User would see messages when interacting with the site | Interacted with multiple things around the site | Every message popped up when it should | Pass |

#Validation

##Html

* index.html
![index](/docs/validation/index.png)

* gallery.html
![gallery](/docs/validation/gallery.png)

* contact.html
![contact](/docs/validation/contact.png)

* successs.html
![successs](/docs/validation/success.png)

* delete_profile.html
![delete_profile](/docs/validation/delete_profile.png)

* delete_review.html
![delete_review](/docs/validation/delete_review.png)

* edit_review.html
1[edit_review](/docs/validation/edit_review.png)

* login.html
![login](/docs/validation/login.png)

* profile.html
![profile](/docs/validation/profile.png)

* register.html
![register](/docs/validation/register.png)


##CSS

*style.css
![style](/docs/validation/style.png)

##JavaScript

* gallery.js
![gallery](/docs/validation/gallery.js.png)

* feedback.js
![feedback](/docs/validation/feedback.png)

* profile.js
![profile](/docs/validation/profile.js.png)



