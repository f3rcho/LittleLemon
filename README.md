# LittleLemon

Final Asignment

You could test the API with:

/restaurant/menu/
/restaurant/booking/

- login with this user test:
  curl --request POST \
   --url http://127.0.0.1:8000/auth/token/login \
   --header 'Content-Type: application/x-www-form-urlencoded' \
   --cookie csrftoken=Nj42H0XGXGkyDUEaWOFyXtDCDBHFeHYR \
   --data username=testuser \
   --data 'password=test@123!'

- get menu and menu items:
  curl --request GET \
   --url http://127.0.0.1:8000/restaurant/menu/3 \
   --header 'Authorization: Token aefe340674a5c6f064c3906580b75097e737e986' \
   --cookie csrftoken=Nj42H0XGXGkyDUEaWOFyXtDCDBHFeHYR

- get booking with:
  curl --request GET \
   --url http://127.0.0.1:8000/restaurant/booking/ \
   --cookie csrftoken=Nj42H0XGXGkyDUEaWOFyXtDCDBHFeHYR
