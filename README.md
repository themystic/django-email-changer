# Django Email Changer

Django app to securely change a user's email. This app will email your user at the new email with an activation URL. Once they click the link in the email, the new email will be put into their profile.


## Settings

### `EMAIL_CHANGE_NOTIFICATION_SUBJECT`

The subject of email change notifications.

### `EMAIL_CHANGE_NOTIFICATION_EMAIL_TEMPLATE`

The template for email change notifications.

### `EMAIL_CHANGE_NOTIFICATION_FROM`

Who is the email change notification from.

### `EMAIL_CHANGE_ACTIVATION_SUCCESS_URL`

When a user activates their email, we'll redirect to this URL.

### `EMAIL_CHANGE_SUCCESS_URL`

After a successfully submitting a new email, the user is forwarded to this URL.