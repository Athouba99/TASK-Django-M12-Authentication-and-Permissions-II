Haven't seen a movie in a while?

## Steps

## Setup

1. Fork and clone [this repository](https://github.com/malthunayan/TASK-Django-M12-Authentication-and-Permissions-II).
2. Install the `requirements` using `pip install -r requirements/dev.lock`.

## Registration

1. Create a new app called `users` and create a `User` model that inherits from `django.contrib.auth.models.AbstractUser` and just `pass`es.
2. Go to `settings.py` and add `AUTH_USER_MODEL = "users.User"`, where `users` is that app name and `User` is the class name we chose for our custom `User` model.
3. Make migrations and migrate.
4. Add a `forms.py` file inside of your `users` app.
5. Add a `RegistrationForm` model form.
   - Make sure to set the model equal to `User`, but do not import your `User` model directly (use `Django`'s helper `get_user_model`, which you can read about [here](https://docs.djangoproject.com/en/4.0/topics/auth/customizing/#referencing-the-user-model)).
   - Add a widget for the password field to be hidden (you can read about widgets [here](https://docs.djangoproject.com/en/4.0/ref/forms/widgets/))
6. Add your `register_user` view in `users/views.py`.
   - Create a new instance of your `RegistrationForm`
   - Check if the `request method` is `POST` and then create a new instance of `RegistrationForm` with the first argument passed being `request.POST`
     - Check if the `form` is `valid` and then save the form, but do not commit (i.e., `commit=False`) and assign the return to a variable called `user`
     - Use `user.set_password` to set the password
     - Finally use `user.save` to commit your changes
     - Then use the `login` helper to login (read about it [here](https://docs.djangoproject.com/en/4.0/topics/auth/default/#how-to-log-a-user-in))
     - `Redirect` to `home`
   - Create your `context` and add your `form` instance to it
   - `Render` a template called `register.html`
7. Add your `register_user` view to `urls.py` and name it `register`.
8. Add the `register.html` template to `users/templates`.
9. We have no way right now to tell that we are registered and logged in other than trying to register again and failing. We will see how to make it visible to the user that they're logged in in the upcoming tasks.
10. Commit and push your changes.