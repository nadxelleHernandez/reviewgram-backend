**Summary of API EndPoint**

| **File** | **Description** | **Path** | **Request Body** | **Error Response** | **Response Body** | **Request Type** |
| ------ | --------------- | -------- | ---------------- | ------------------ | ----------------- | ----------------- |
| media_routes | Get images url | /media/image-url |    | {statuscode: 500,Message: “bad request”} | {"configuration": {"base_url": "http://image.tmdb.org/t/p/","poster_sizes": ["w92","w154","w185","w342","w500","w780","original"], "secure_base_url":  "https://image.tmdb.org/t/p/"},"message": "Images url configuration retrieved","statuscode": 200} | GET  |

| auth | Get | /     | {        | {stat   | {statuscode:     | POST |
| oriz | to  | token |          | uscode: | 201,             |      |
| atio | ken |       | u        | 403,    |                  |      |
| n_ro |     |       | sername: |         | message:         |      |
| utes |     |       | u        | M       | "generetaded     |      |
|      |     |       | sername, | essage: | used:            |      |
|      |     |       |          | "       |                  |      |
|      |     |       | p        | Unautho | token: token}    |      |
|      |     |       | assword: | rized"} |                  |      |
|      |     |       | password |         |                  |      |
|      |     |       |          |         |                  |      |
|      |     |       | }        |         |                  |      |
+------+-----+-------+----------+---------+------------------+------+
| use  | Cre | /     | {name:   | {stat   | {statuscode:     | POST |
| r_ro | ate | users | u        | uscode: | 201,             |      |
| utes | U   |       | serName, | 400,    |                  |      |
|      | ser |       | email:   |         | message: "User:  |      |
|      |     |       | us       | M       | {ne              |      |
|      |     |       | erEmail, | essage: | w_user.username} |      |
|      |     |       | u        | "bad    | created          |      |
|      |     |       | sername: | re      | successfully.",  |      |
|      |     |       | u        | quest"} |                  |      |
|      |     |       | sername, |         | user: {          |      |
|      |     |       |          |         |                  |      |
|      |     |       | p        |         | id: userId,      |      |
|      |     |       | assword: |         |                  |      |
|      |     |       | p        |         | name: userName,  |      |
|      |     |       | assword} |         |                  |      |
|      |     |       |          |         | email:           |      |
|      |     |       |          |         | userEmail,       |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | username: user,  |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | password:        |      |
|      |     |       |          |         | password         |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | }                |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | }                |      |
+------+-----+-------+----------+---------+------------------+------+
| use  | Get | /us   |          | {stat   | {statuscode:     | GET  |
| r_ro | U   | ers/\ |          | uscode: | 200,             |      |
| utes | ser | <id\> |          | 400,    |                  |      |
|      | by  |       |          |         | message:         |      |
|      | Id  |       |          | M       | "Successfully    |      |
|      |     |       |          | essage: | retrieved        |      |
|      |     |       |          | "bad    | {username}",     |      |
|      |     |       |          | re      |                  |      |
|      |     |       |          | quest"} | user: {          |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | id: userId,      |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | name: Name,      |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | email:           |      |
|      |     |       |          |         | userEmail,       |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | username: user   |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | }                |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | }                |      |
+------+-----+-------+----------+---------+------------------+------+
| use  | Upd | /us   | {name:   | {stat   | {statuscode:     | P    |
| r_ro | ate | ers/\ | u        | uscode: | 200,             | ATCH |
| utes | u   | <id\> | serName, | 400,    |                  |      |
|      | ser |       | email:   |         | message:         |      |
|      |     |       | us       | M       | "Successfully    |      |
|      |     |       | erEmail, | essage: | updated          |      |
|      |     |       |          | "bad    | {username}",     |      |
|      |     |       | }        | re      |                  |      |
|      |     |       |          | quest"} | user: {          |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | id: userId,      |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | name: userName,  |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | email:           |      |
|      |     |       |          |         | userEmail,       |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | username: user   |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | }                |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | }                |      |
+------+-----+-------+----------+---------+------------------+------+
| use  | Del | /us   |          | {stat   | { statuscode:    | DE   |
| r_ro | ete | ers/\ |          | uscode: | 200,             | LETE |
| utes | u   | <id\> |          | 400,    |                  |      |
|      | ser |       |          |         | message: "User   |      |
|      |     |       |          | M       | with id: \<id\>  |      |
|      |     |       |          | essage: | successfully     |      |
|      |     |       |          | "bad    | deleted"         |      |
|      |     |       |          | re      |                  |      |
|      |     |       |          | quest"} | }                |      |
+------+-----+-------+----------+---------+------------------+------+
| use  | Get | /     |          | {stat   | {statuscode:     | GET  |
| r_ro | u   | users |          | uscode: | 200,             |      |
| utes | ser | /\<id |          | 400,    |                  |      |
|      | r   | \>/re |          |         | message: "User   |      |
|      | evi | views |          | M       | \<username\>     |      |
|      | ews |       |          | essage: | reviews          |      |
|      |     |       |          | "bad    | retrieved        |      |
|      |     |       |          | re      | successfully.",  |      |
|      |     |       |          | quest"} |                  |      |
|      |     |       |          |         | data: {          |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | user: {          |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | userId: userId   |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | username:        |      |
|      |     |       |          |         | username} ,      |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | reviews: \[ {    |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | media: { id:     |      |
|      |     |       |          |         | TMDB_id, title:  |      |
|      |     |       |          |         | mediaTitle,      |      |
|      |     |       |          |         | isMovie:         |      |
|      |     |       |          |         | true/false}      |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | content:         |      |
|      |     |       |          |         | theReview,       |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | created:         |      |
|      |     |       |          |         | dateCreated,     |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | rating:          |      |
|      |     |       |          |         | 1.0-10.0,        |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | updated:         |      |
|      |     |       |          |         | dateUpdated,     |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | fromTMDB:false   |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | } { \<\<another  |      |
|      |     |       |          |         | review\>\>       |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | } \]             |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | } }              |      |
+------+-----+-------+----------+---------+------------------+------+
| use  | Add | /     | { media: | {       | {                | POST |
| r_ro | me  | users | {        |         |                  |      |
| utes | dia | /\<id | TMDB_id: | stat    | statuscode: 201, |      |
|      | rev | \>/re | TMDB_id  | uscode: |                  |      |
|      | iew | views | ,        | 400,    | message:         |      |
|      |     |       |          |         | "Success         |      |
|      |     |       | isMovie: | M       | creating review  |      |
|      |     |       | tru      | essage: | for user id:     |      |
|      |     |       | e/false, | "bad    | media id: ",     |      |
|      |     |       |          | r       |                  |      |
|      |     |       | title:   | equest" | data: {          |      |
|      |     |       | me       |         |                  |      |
|      |     |       | diaTitle | }       | user: { id:      |      |
|      |     |       | }        |         | userId           |      |
|      |     |       |          |         |                  |      |
|      |     |       | content: |         | username:        |      |
|      |     |       | th       |         | username },      |      |
|      |     |       | eReview, |         |                  |      |
|      |     |       |          |         | media: { id:     |      |
|      |     |       | rating:  |         | TMDB_id, title:  |      |
|      |     |       | 1        |         | mediaTitle,      |      |
|      |     |       | .0-10.0, |         | isMovie:         |      |
|      |     |       |          |         | true/false}      |      |
|      |     |       | }        |         |                  |      |
|      |     |       |          |         | content:         |      |
|      |     |       |          |         | theReview,       |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | created:         |      |
|      |     |       |          |         | dateCreated,     |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | rating:          |      |
|      |     |       |          |         | 1.0-10.0,        |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | updated:         |      |
|      |     |       |          |         | dateUpdated,     |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | fromTMDB: false  |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | }                |      |
+------+-----+-------+----------+---------+------------------+------+
| use  | Upd | /     | { media: | {       | {                | P    |
| r_ro | ate | users | { id:    |         |                  | ATCH |
| utes | me  | /\<id | TMDB_id  | stat    | statuscode: 201, |      |
|      | dia | \>/re | ,        | uscode: |                  |      |
|      | rev | views |          | 400,    | message:         |      |
|      | iew |       | isMovie: |         | "Success         |      |
|      |     |       | tru      | M       | creating review  |      |
|      |     |       | e/false, | essage: | for user id:     |      |
|      |     |       |          | "bad    | media id: ",     |      |
|      |     |       | title:   | r       |                  |      |
|      |     |       | me       | equest" | data: {          |      |
|      |     |       | diaTitle |         |                  |      |
|      |     |       | }        | }       | user: { id:      |      |
|      |     |       |          |         | userId           |      |
|      |     |       | content: |         |                  |      |
|      |     |       | th       |         | username:        |      |
|      |     |       | eReview, |         | username },      |      |
|      |     |       |          |         |                  |      |
|      |     |       | rating:  |         | media: { id:     |      |
|      |     |       | 1        |         | TMDB_id, title:  |      |
|      |     |       | .0-10.0, |         | mediaTitle,      |      |
|      |     |       |          |         | isMovie:         |      |
|      |     |       | }        |         | true/false}      |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | content:         |      |
|      |     |       |          |         | theReview,       |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | created:         |      |
|      |     |       |          |         | dateCreated,     |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | rating:          |      |
|      |     |       |          |         | 1.0-10.0,        |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | updated:         |      |
|      |     |       |          |         | dateUpdated,     |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | fromTMDB: false  |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | }                |      |
+------+-----+-------+----------+---------+------------------+------+
|      | *   |       |          |         |                  |      |
|      | *Mo |       |          |         |                  |      |
|      | vie |       |          |         |                  |      |
|      | s** |       |          |         |                  |      |
+------+-----+-------+----------+---------+------------------+------+
| medi | Get | medi  |          | {stat   | {statuscode:     | GET  |
| a_ro | a   | a/mov |          | uscode: | 200,             |      |
| utes | mo  | ies/\ |          | 500,    |                  |      |
|      | vie | <id\> |          | m       | message: "Movie  |      |
|      | by  |       |          | essage: | \<name\>         |      |
|      | id  |       |          | 'server | retrieved        |      |
|      |     |       |          | error'} | successfully.",  |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | movie: {         |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | id: MovieId,     |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | title:           |      |
|      |     |       |          |         | movieTitle,      |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | overview:        |      |
|      |     |       |          |         | briefsummary,    |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | rating:          |      |
|      |     |       |          |         | 1.0-10.0,        |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | genres: \[       |      |
|      |     |       |          |         | genre1, genre2,  |      |
|      |     |       |          |         | genre3\],        |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | posterUrl: (img  |      |
|      |     |       |          |         | url),            |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | Or               |      |
|      |     |       |          |         | iginal_language: |      |
|      |     |       |          |         | language,        |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | runtime: (num    |      |
|      |     |       |          |         | minutes),        |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | status:          |      |
|      |     |       |          |         | (Rumored,        |      |
|      |     |       |          |         | Planned, In      |      |
|      |     |       |          |         | Production, Post |      |
|      |     |       |          |         | Production,      |      |
|      |     |       |          |         | Released,        |      |
|      |     |       |          |         | Canceled)        |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | release_date:    |      |
|      |     |       |          |         | date             |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | }                |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | }                |      |
+------+-----+-------+----------+---------+------------------+------+
| medi | Get | me    |          | {stat   | {statuscode:     | GET  |
| a_ro | mo  | dia/m |          | uscode: | 200,             |      |
| utes | vie | ovies |          | 400,    |                  |      |
|      | r   | /\<id |          |         | message: "Movie  |      |
|      | evi | \>/re |          | M       | \<name\> reviews |      |
|      | ews | views |          | essage: | retrieved        |      |
|      |     |       |          | "bad    | successfully.",  |      |
|      |     |       |          | re      |                  |      |
|      |     |       |          | quest"} | media : { id:    |      |
|      |     |       |          |         | id,              |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | is_movie: false, |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | TMDB_id:         |      |
|      |     |       |          |         | tmdb_id,         |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | "Title": title   |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | }                |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | reviews: \[ {    |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | user: {id:       |      |
|      |     |       |          |         | userId           |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | username:        |      |
|      |     |       |          |         | username },      |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | content:         |      |
|      |     |       |          |         | theReview,       |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | created:         |      |
|      |     |       |          |         | dateCreated,     |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | rating:          |      |
|      |     |       |          |         | 1.0-10.0,        |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | updated:         |      |
|      |     |       |          |         | dateUpdated,     |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | fromTMDB:        |      |
|      |     |       |          |         | true/false       |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | } { \<\<another  |      |
|      |     |       |          |         | review\>\>       |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | } \]             |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | }                |      |
+------+-----+-------+----------+---------+------------------+------+
|      | **M |       |          |         |                  |      |
|      | edi |       |          |         |                  |      |
|      | a** |       |          |         |                  |      |
+------+-----+-------+----------+---------+------------------+------+
| medi | Sea | /me   | Qu       | {stat   | { statuscode:    | GET  |
| a_ro | rch | dia/s | eryparam | uscode: | 200,             |      |
| utes | me  | earch | qu       | 400,    |                  |      |
|      | dia |       | ery="sea |         | Message:         |      |
|      |     |       | rchdata" | M       | "Success",       |      |
|      |     |       |          | essage: |                  |      |
|      |     |       |          | "bad    | movies: \[ {     |      |
|      |     |       |          | re      |                  |      |
|      |     |       |          | quest"} | id: movieId,     |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | title:           |      |
|      |     |       |          |         | Movietitle,      |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | backdrop_path:   |      |
|      |     |       |          |         | imageUrl,        |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | release_date:    |      |
|      |     |       |          |         | date             |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | isMovie: true    |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | },               |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | {                |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \<\<another      |      |
|      |     |       |          |         | object\>\>       |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | }                |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \],              |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | Tvshows: \[ {    |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | id: tvshowId     |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | title: tvTitle,  |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | backdrop_path:   |      |
|      |     |       |          |         | imageUrl, },     |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | { \<\<another    |      |
|      |     |       |          |         | object \>\>}     |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \]               |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | }                |      |
+------+-----+-------+----------+---------+------------------+------+
|      |     |       |          |         |                  |      |
+------+-----+-------+----------+---------+------------------+------+
| medi | Get | /m    |          |         | {                | GET  |
| a_ro | top | edia/ |          |         |                  |      |
| utes | f   | top/m |          |         | \"message\":     |      |
|      | ive | ovies |          |         | \"Top movies     |      |
|      | mov |       |          |         | retrieved from   |      |
|      | ies |       |          |         | TMDB\",          |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"movies\": {    |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"0\": {         |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"TMDB_id\": id, |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"isMovie\":     |      |
|      |     |       |          |         | true,            |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"orig           |      |
|      |     |       |          |         | inal_language\": |      |
|      |     |       |          |         | \"en\",          |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"overview\":    |      |
|      |     |       |          |         | \"description\", |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"poster_url\":  |      |
|      |     |       |          |         | \"/ng            |      |
|      |     |       |          |         | l2FKBlU4fhbdsrtd |      |
|      |     |       |          |         | om9LVLBXw.jpg\", |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"rating\":      |      |
|      |     |       |          |         | 7.889,           |      |
|      |     |       |          |         | \                |      |
|      |     |       |          |         | "release_date\": |      |
|      |     |       |          |         | \"2023-02-10\",  |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"runtime\":     |      |
|      |     |       |          |         | \"unknown\",     |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"status\":      |      |
|      |     |       |          |         | \"unknown\",     |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"title\":       |      |
|      |     |       |          |         | \"Ant-Man and    |      |
|      |     |       |          |         | the Wasp:        |      |
|      |     |       |          |         | Quantumania\"    |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | },               |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"1\": {         |      |
|      |     |       |          |         | \<next\> }       |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | }                |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | }                |      |
+------+-----+-------+----------+---------+------------------+------+
| medi | Get | /me   |          |         | {                | GET  |
| a_ro | top | dia/t |          |         |                  |      |
| utes | f   | op/tv |          |         | \"message\":     |      |
|      | ive | shows |          |         | \"Top TV shows   |      |
|      | tv  |       |          |         | retrieved from   |      |
|      | sh  |       |          |         | TMDB\",          |      |
|      | ows |       |          |         |                  |      |
|      |     |       |          |         | \"statuscode\":  |      |
|      |     |       |          |         | 200,             |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"tvshows\": {   |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"0\": {         |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"TMDB_id\": id, |      |
|      |     |       |          |         | \"               |      |
|      |     |       |          |         | backdrop_path\": |      |
|      |     |       |          |         | path,            |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"isMovie\":     |      |
|      |     |       |          |         | false,           |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"name\":        |      |
|      |     |       |          |         | \"name\",        |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"overview\":    |      |
|      |     |       |          |         | \"brie           |      |
|      |     |       |          |         | f-description\", |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"poster_path\": |      |
|      |     |       |          |         | \"path\",        |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"rating\": 8.82 |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | },               |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"1\":           |      |
|      |     |       |          |         | {\<next_tvshow\> |      |
|      |     |       |          |         | } } }            |      |
+------+-----+-------+----------+---------+------------------+------+
| medi | Get | media |          |         | {statuscode:     | GET  |
| a_ro | TV  | /tv/\ |          |         | 200,             |      |
| utes | Sh  | <id\> |          |         |                  |      |
|      | ows |       |          |         | message: "TV     |      |
|      | by  |       |          |         | show \<name\>    |      |
|      | id  |       |          |         | retrieved        |      |
|      |     |       |          |         | successfully.",  |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | tvshow: {        |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | id: tvshowId,    |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | name:            |      |
|      |     |       |          |         | tvshowName,      |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | overview:        |      |
|      |     |       |          |         | briefsummary,    |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | rating:          |      |
|      |     |       |          |         | 1.0-10.0,        |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | genres: \[       |      |
|      |     |       |          |         | genre1, genre2,  |      |
|      |     |       |          |         | genre3\],        |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | poster_url: (img |      |
|      |     |       |          |         | url),            |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | or               |      |
|      |     |       |          |         | iginal_language: |      |
|      |     |       |          |         | language,        |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | episode_runtime: |      |
|      |     |       |          |         | \[ \]            |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | num              |      |
|      |     |       |          |         | ber_of_episodes: |      |
|      |     |       |          |         | \<number\>       |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | nu               |      |
|      |     |       |          |         | mber_of_seasons: |      |
|      |     |       |          |         | seasons          |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | status:          |      |
|      |     |       |          |         | (Rumored,        |      |
|      |     |       |          |         | Planned, In      |      |
|      |     |       |          |         | Production, Post |      |
|      |     |       |          |         | Production,      |      |
|      |     |       |          |         | Released,        |      |
|      |     |       |          |         | Canceled)        |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | first_air_date:  |      |
|      |     |       |          |         | date,            |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | last_air_date:   |      |
|      |     |       |          |         | date             |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | providers: \[    |      |
|      |     |       |          |         | netflix, appleTV |      |
|      |     |       |          |         | \]               |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | }                |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | }                |      |
+------+-----+-------+----------+---------+------------------+------+
| medi | Get | med   |          | {stat   | {statuscode:     | GET  |
| a_ro | TV  | ia/tv |          | uscode: | 200,             |      |
| utes | s   | /\<id |          | 400,    |                  |      |
|      | how | \>/re |          |         | message: "TV     |      |
|      | r   | views |          | M       | show \<name\>    |      |
|      | evi |       |          | essage: | reviews          |      |
|      | ews |       |          | "bad    | retrieved        |      |
|      |     |       |          | re      | successfully.",  |      |
|      |     |       |          | quest"} |                  |      |
|      |     |       |          |         | id : tv_id,      |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | reviews: \[ {    |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | user: {id:       |      |
|      |     |       |          |         | userId           |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | username:        |      |
|      |     |       |          |         | username },      |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | content:         |      |
|      |     |       |          |         | theReview,       |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | created:         |      |
|      |     |       |          |         | dateCreated,     |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | rating:          |      |
|      |     |       |          |         | 1.0-10.0,        |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | updated:         |      |
|      |     |       |          |         | dateUpdated,     |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | fromTMDB:        |      |
|      |     |       |          |         | true/false       |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | } { \<\<another  |      |
|      |     |       |          |         | review\>\>       |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | } \]             |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | }                |      |
+------+-----+-------+----------+---------+------------------+------+
|      | *   |       |          |         |                  |      |
|      | *Wa |       |          |         |                  |      |
|      | tch |       |          |         |                  |      |
|      | lis |       |          |         |                  |      |
|      | t** |       |          |         |                  |      |
+------+-----+-------+----------+---------+------------------+------+
|      | wat | /us   |          |         | {\"message\":    | GET  |
|      | chl | ers/\ |          |         | \"Successfully   |      |
|      | ist | <id\> |          |         | getting          |      |
|      | by  | /watc |          |         | \<username\>     |      |
|      | u   | hlist |          |         | watchlist.\",    |      |
|      | ser |       |          |         |                  |      |
|      |     |       |          |         | \"statuscode\":  |      |
|      |     |       |          |         | 200,             |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"watchlist\":   |      |
|      |     |       |          |         | \[{              |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"id\": 2,       |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"media\": {     |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"TMDB_id\": id, |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"id\": 4,       |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"is_movie\":    |      |
|      |     |       |          |         | false,           |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"title\": \"The |      |
|      |     |       |          |         | Last of Us\"     |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | },               |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"user\": {      |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"id\": 1,       |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"username\":    |      |
|      |     |       |          |         | \"user\"         |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | },               |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"watched\":     |      |
|      |     |       |          |         | false            |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | }, {\<another    |      |
|      |     |       |          |         | entry\>}         |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \]               |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | }                |      |
+------+-----+-------+----------+---------+------------------+------+
|      | W   | /     |          |         | {\"message\":    | GET  |
|      | atc | users |          |         | \"Successfully   |      |
|      | hed | /\<id |          |         | getting          |      |
|      | l   | \>/wa |          |         | \<username\>     |      |
|      | ist | tched |          |         | watchlist.\",    |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"statuscode\":  |      |
|      |     |       |          |         | 200,             |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"watched\": \[{ |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"id\": 2,       |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"media\": {     |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"TMDB_id\": id, |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"id\": 4,       |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"is_movie\":    |      |
|      |     |       |          |         | false,           |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"title\": \"The |      |
|      |     |       |          |         | Last of Us\"     |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | },               |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"user\": {      |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"id\": 1,       |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"username\":    |      |
|      |     |       |          |         | \"user\"         |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | },               |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"watched\":     |      |
|      |     |       |          |         | true             |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | }, {\<another    |      |
|      |     |       |          |         | entry\>}         |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \]               |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | }                |      |
+------+-----+-------+----------+---------+------------------+------+
|      | Add | /us   | {        |         | {\"entry\": {    | POST |
|      | me  | ers/\ | TMDB_id: |         |                  |      |
|      | dia | <id\> | tmdb_id, |         | \"id\": 5,       |      |
|      | wat | /watc |          |         |                  |      |
|      | chl | hlist | isMovie: |         | \"media\": {     |      |
|      | ist |       | tru      |         |                  |      |
|      |     |       | e/false, |         | \"TMDB_id\": id, |      |
|      |     |       |          |         |                  |      |
|      |     |       | title:   |         | \"id\": 5,       |      |
|      |     |       | title    |         |                  |      |
|      |     |       |          |         | \"is_movie\":    |      |
|      |     |       | }        |         | true,            |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"title\":       |      |
|      |     |       |          |         | "title"          |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | },               |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"user\": {      |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"id\": 1,       |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"username\":    |      |
|      |     |       |          |         | \"user\"         |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | },               |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"watched\":     |      |
|      |     |       |          |         | false            |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | },               |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"message\":     |      |
|      |     |       |          |         | \"Successfully   |      |
|      |     |       |          |         | adding November  |      |
|      |     |       |          |         | to \<username\>  |      |
|      |     |       |          |         | watchlist\",     |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"statuscode\":  |      |
|      |     |       |          |         | 201              |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | }                |      |
+------+-----+-------+----------+---------+------------------+------+
|      | Add | /     | {        |         | {\"entry\": {    | POST |
|      | me  | users | TMDB_id: |         |                  |      |
|      | dia | /\<id | tmdb_id, |         | \"id\": 5,       |      |
|      | w   | \>/wa |          |         |                  |      |
|      | atc | tched | isMovie: |         | \"media\": {     |      |
|      | hed |       | tru      |         |                  |      |
|      |     |       | e/false, |         | \"TMDB_id\": id, |      |
|      |     |       |          |         |                  |      |
|      |     |       | title:   |         | \"id\": 5,       |      |
|      |     |       | title    |         |                  |      |
|      |     |       |          |         | \"is_movie\":    |      |
|      |     |       | }        |         | true,            |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"title\":       |      |
|      |     |       |          |         | "title"          |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | },               |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"user\": {      |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"id\": 1,       |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"username\":    |      |
|      |     |       |          |         | \"user\"         |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | },               |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"watched\":     |      |
|      |     |       |          |         | true             |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | },               |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"message\":     |      |
|      |     |       |          |         | \"Successfully   |      |
|      |     |       |          |         | adding November  |      |
|      |     |       |          |         | to \<username\>  |      |
|      |     |       |          |         | watched list\",  |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | \"statuscode\":  |      |
|      |     |       |          |         | 201              |      |
|      |     |       |          |         |                  |      |
|      |     |       |          |         | }                |      |
+------+-----+-------+----------+---------+------------------+------+
|      | Del | /us   | {        |         |                  | DE   |
|      | ete | ers/\ | TMDB_id: |         |                  | LETE |
|      | me  | <id\> | tmdb_id, |         |                  |      |
|      | dia | /watc |          |         |                  |      |
|      | wat | hlist | isMovie: |         |                  |      |
|      | chl |       | tru      |         |                  |      |
|      | ist |       | e/false, |         |                  |      |
|      |     |       |          |         |                  |      |
|      |     |       | }        |         |                  |      |
+------+-----+-------+----------+---------+------------------+------+
|      | Del | /     | {        |         |                  | DE   |
|      | ete | users | TMDB_id: |         |                  | LETE |
|      | me  | /\<id | tmdb_id, |         |                  |      |
|      | dia | \>/wa |          |         |                  |      |
|      | w   | tched | isMovie: |         |                  |      |
|      | atc |       | tru      |         |                  |      |
|      | hed |       | e/false, |         |                  |      |
|      |     |       |          |         |                  |      |
|      |     |       | }        |         |                  |      |
+------+-----+-------+----------+---------+------------------+------+
|      | S   | /use  | {        |         |                  | P    |
|      | end | rs/\< | TMDB_id: |         |                  | ATCH |
|      | me  | id\>/ | tmdb_id, |         |                  |      |
|      | dia | to-wa |          |         |                  |      |
|      | f   | tched | isMovie: |         |                  |      |
|      | rom |       | tru      |         |                  |      |
|      | wat |       | e/false, |         |                  |      |
|      | chl |       |          |         |                  |      |
|      | ist |       | }        |         |                  |      |
|      | to  |       |          |         |                  |      |
|      | w   |       |          |         |                  |      |
|      | atc |       |          |         |                  |      |
|      | hed |       |          |         |                  |      |
+------+-----+-------+----------+---------+------------------+------+
|      | S   | /     | {        |         |                  | P    |
|      | end | users | TMDB_id: |         |                  | ATCH |
|      | me  | /\<id | tmdb_id, |         |                  |      |
|      | dia | \>/to |          |         |                  |      |
|      | f   | -watc | isMovie: |         |                  |      |
|      | rom | hlist | tru      |         |                  |      |
|      | w   |       | e/false, |         |                  |      |
|      | atc |       |          |         |                  |      |
|      | hed |       | }        |         |                  |      |
|      | to  |       |          |         |                  |      |
|      | wat |       |          |         |                  |      |
|      | chl |       |          |         |                  |      |
|      | ist |       |          |         |                  |      |
+------+-----+-------+----------+---------+------------------+------+
