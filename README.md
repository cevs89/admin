### Regiter User:

*/api/user/register/*

**Request**:
```
{
"username":"user",
"email":"valid email",
"password":"pass",
"first_name":"name",
"last_name":"last_name",
"academic_level":"Studies",
"address":"address",
"city":"city",
"country":"country"
}
```


**response sucess**:
```
{'success': True, 'msg': 'User has been created'}
```
======================================================

### Login:
*/authentication/login/*

**Request:**
```
{
"username":"valid user",
"email":"valid email",
"password":"valid password"
}
```

**Response Success:**
```
{
  "key": "TOKEN"
}
```

**Send Header in all request:**
Authorization: token YOUR_TOKEN

========================================================
### Logout:
*/authentication/logout/*

**request:**

**Send Header:**
Authorization: token YOUR_TOKEN


**Response:**
```
{
  "detail": "Successfully logged out."
}
```
=========================================================
### Get User Profile:
*/api/user/profile/*

**Header:**
Authorization: token YOUR_TOKEN


**Request:**

body:
```
{
"id_user":"2"
}
```
**Response success:**
```
{
  "address": "Calle Principal",
  "country": "Venezuela",
  "username": "carlos",
  "city": "Caracas",
  "academic_level": "Universitario
}
```
==========================================================

### Update Profile:
*/api/user/update/profile/*

**Header:**
Authorization: token YOUR_TOKEN

body:
```
{
"id_user":"2",
"academic_level":"primaria",
"address":"calle 1",
"city":"maracay",
"country":"Venezuela"
}
```
**Response success:**
```
{'success': True, 'msg': 'User has been modified'}
```
