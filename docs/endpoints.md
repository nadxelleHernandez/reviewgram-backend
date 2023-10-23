**Summary of API EndPoint**

| **File** | **Description** | **Path** | **Request Body** | **Error Response** | **Response Body** | **Request Type** |
| ------ | --------------- | -------- | ---------------- | ------------------ | ----------------- | ----------------- |
| media_routes | Get images url | /media/image-url |    | {statuscode: 500,Message: “bad request”} | {"configuration": {"base_url": "http://image.tmdb.org/t/p/","poster_sizes": ["w92","w154","w185","w342","w500","w780","original"], "secure_base_url":  "https://image.tmdb.org/t/p/"},"message": "Images url configuration retrieved","statuscode": 200} | GET  |
| authorization_routes | Get token | /token | { username: username, password: password} | {statuscode: 403, Message: “Unauthorized”} | {statuscode: 201, message: “generated used: token: token}| POST |
| user_routes | Create User | /users | {name: userName, email: userEmail, username: username,password: password} | {statuscode: 400, Message: “bad request”} | {statuscode: 201, message: “User: {new_user.username} created successfully.”, user: { id: userId, name: userName, email: userEmail, username: user, password: password }} | POST |
| user_routes | Get User by Id | /users/\<id\> |  | {statuscode: 400, Message: “bad request”} | {statuscode: 200, message: “Successfully retrieved {username}”, user: { id: userId, name: Name, email: userEmail, username: user}} | GET |
| user_routes | Update User | /users/\<id\> | {name: userName, email: userEmail,} | {statuscode: 400, Message: “bad request”} | {statuscode: 200, message: “Successfully updated {username}”, user: { id: userId, name: userName, email: userEmail, username: user}} | PATCH |
| user_routes | Delete User | /users/\<id\> |  | {statuscode: 400, Message: “bad request”} | { statuscode: 200, message: “User with id: <id> successfully deleted”} | DELETE |
| user_routes | Get user reviews | /users/\<id\>/reviews |  | {statuscode: 400, Message: “bad request”} | { statuscode: 200, message: “User \<username\> reviews retrieved successfully.”, data: {  user: { userId: userId, username: username} , reviews: \[ { media: { id: TMDB_id, title: mediaTitle,    isMovie: true/false content: theReview, created: dateCreated, rating: 1.0-10.0, updated: dateUpdated, fromTMDB:false} { \<\<another review\>\> } \] } } | GET |
| user_routes | Add media review | /users/\<id\>/reviews |  { media: { TMDB_id: TMDB_id , isMovie: true/false, title: mediaTitle } content: theReview, rating: 1.0-10.0, } | {statuscode: 400, Message: “bad request”} | { statuscode: 201, message: “Success creating review for user id: media id: ”, data: { user: { id: userId, username: username }, media: { id: TMDB_id, title: mediaTitle,    isMovie: true/false}, content: theReview, created: dateCreated, rating: 1.0-10.0, updated: dateUpdated, fromTMDB: false } | POST |
| user_routes | Update media review | /users/\<id\>/reviews | { media: { TMDB_id: TMDB_id , isMovie: true/false, title: mediaTitle } content: theReview, rating: 1.0-10.0, } | {statuscode: 400, Message: “bad request”} | { statuscode: 201, message: “Success creating review for user id: media id: ”, data: { user: { id: userId, username: username }, media: { id: TMDB_id, title: mediaTitle, isMovie: true/false},  content: theReview, created: dateCreated, rating: 1.0-10.0, updated: dateUpdated, fromTMDB: false } | PATCH |
| media_routes | Get a movie by id | media/movies/\<TMDB_id\> |  | { statuscode: 500, message: ‘server error’ } | { statuscode: 200, message: “Movie \<name\> retrieved successfully.”,  movie: { TMDB_id: MovieId, title: movieTitle, overview: briefsummary, rating: 1.0-10.0, genres: \[ genre1, genre2, genre3\], posterUrl: (img url), original_language: language, runtime: (num minutes), status: (Rumored, Planned, In Production, Post Production, Released, Cancelled), release_date: date } } | GET |
| media_routes | Get movie reviews | media/movies/\<TMDB_id\>/reviews |  | { statuscode: 400, Message: “bad request” } | {statuscode: 200, message: “Movie \<name\> reviews retrieved successfully.”,  media : { id: id,  is_movie: false,  TMDB_id: tmdb_id,  “Title”: title }, reviews: \[ { user: {id: userId, username: username }, content: theReview, created: dateCreated, rating: 1.0-10.0, updated: dateUpdated, fromTMDB: true/false}, { \<\<another review\>\> } \]} | GET |




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
