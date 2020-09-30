# UdemyCourseEnrollBot
 A bot which scrapes coupon code & auto-enrolls you to that course.

# Video-link of the bot working

* **https://www.youtube.com/watch?v=u7dvwPBIMgI**

## Requirements

* Requires python, selenium, anti-captcha (pip install python-anticaptcha).

* Works in Latest version of chrome.

## How to use?

* On Line number 21 & 23, give your udemy login-email id & udemy password, and you are done.

* You need to install chromedriver & give its path in the PATH variable. 
### Note

* I made this so it can only scrape data from the first page of tutorial-bar, as from the second pages most of the coupon codes are already expired.

* If a course is already owned or there is a discount coupon it will throw an exception which is handled(it will print out a statement stating the problem).

* The google-recaptcha is commented because i don't have the minimum credits to use the captcha solving services, also the google-recaptcha comes if you try it repeatedly, so don't need to worry ^_^.

* You can use this bot once in a day.

#### Reminder

**Always pay for the course that you want to support your mentor. These are just free coupons available for a certain period of time and not based on quantity.**

