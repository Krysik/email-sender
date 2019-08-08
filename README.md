# Email sender

It's a basicly Flask server which handle POST request from an external website.

## Docker
To running my app with docker type just two commands.
```docker build -t email-sender .```
```docker run -e HOST=<serverSMTP> -e PORT=<portOfSMTPServer> -e EMAIL=<EMAIL> -e EMAIL_PASSWORD=<PASS_TO_YOUR_EMAIL_ACCOUNT> -p 5000:5000 email-sender```

**Server is running on port 5000**
**Remember to change the env variables.**
