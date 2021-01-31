# API documentation
Documentation for the API server

# General
The used type of authorization is 
[BasicAuth](https://en.wikipedia.org/wiki/Basic_access_authentication),
so be sure to include a corresponding header if you are trying to reach endpoints that requires authorization.

There is 3 access levels (roles) defined for authorized users: admin, moderator and user.
Information about roles is stored in database and server uses it automatically.

All the endpoints have a `/api` prefix 

# Resources

## Table of Contents <a name="contents"></a>
| Endpoint         | Method   | Auth
| ---              | :------: | :--- |
|[`/items/<int:id>`](item) | [GET](item-get) |
|                          | [PUT](item-put) | moderator
|                          | [DELETE](item-delete) | admin
|[`/items`](items) | [GET](items-get) | 
|                  |[POST](items-post)| admin
|[`/picture/<int:id>`](picture)| [GET](picture-get) | 
|                              |[POST](picture-post)| admin


---
## Item <a name="item"></a>

### GET `/items/<int:id>` <a name="item-get"></a>
* Returns 200 and json of selected item
  ```javascript
  {
    "id": <int>,
    "title": <string>,
    "price": <float>,
    "description": <string>,
    "is_available": <bool>,
    "category_id": <int>,
    "pictures": [
        // links for the related pictures
    ]
  }
  ```
* or 404 if an item with this id does not exist

[↑ to table of contents](contents)

### PUT `/items/<int:id>` <a name="item-put"></a>
* _Moderator or admin role required_ 

* Modifies existing item. Request should have `multipart/form-data` Content-Type. Parts should have name of Item property and contain corresponding data or contain image with jpg or png extension.

* Returns 200 and json of modified item
* or 404 if an item with this id does not exist

[↑ to table of contents](contents)

### DELETE `/items/<int:id>` <a name="item-delete"></a>
* _Admin role required_
* Permanently deletes selected Item
* Returns 204 if successful
* or 404 if an item with this id does not exist

[↑ to table of contents](contents)


---
## Items <a name="items"></a>

### GET `/items?page=<int>&per_page=<int>` <a name="items-get"></a>

* Paginates the list of all items and returns 200 with an items page
  ```javascript
  {
      "items": [
          /* items (see GET /items/<int:id>) */
      ],
      "_meta": {
          "page": <int>,
          "per_page": <int>,
          "total_pages": <int>,
          "total_items": <int>
      },
      "_links": {
          "self": /* link for this page */,
          "next": /* link for the next page (or null) */,
          "prev": /* link for the previous page (or null) */
      }
    }
  ```
[↑ to table of contents](contents)

### POST `/items` <a name="items-post"></a>
* _Admin role required_ 
* Creates a new item. The request must be the same as for [PUT `/items/<int:id>`](item-put)
* Returns 201 if successful

[↑ to table of contents](contents)


---
## Picture <a name="picture"></a>

### GET `/picture/<int:id>` <a name="picture-get"></a>
* Returns 200 and corresponding image (in type of `image/*`)
* or 404 if a picture with this id does not exist

[↑ to table of contents](contents)

### DELETE `/picture/<int:id>` <a name="picture-delete"></a>
* _Admin role required_
* Permanently deletes selected picture
* Returns 204 if successful
* or 404 if a picture with this id does not exist

[↑ to table of contents](contents)
