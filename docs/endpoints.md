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
| media_routes | Get a movie by id | /media/movies/\<TMDB_id\> |  | { statuscode: 500, message: ‘server error’ } | { statuscode: 200, message: "Movie with id: \<TMDB_id\> retrieved from TMDB",  movie: { TMDB_id: MovieId, title: movieTitle, overview: briefsummary, rating: 1.0-10.0, genres: \[ genre1, genre2, genre3\], posterUrl: (img url), original_language: language, runtime: (num minutes), status: (Rumored, Planned, In Production, Post Production, Released, Cancelled), release_date: date } } | GET |
| media_routes | Get movie reviews | /media/movies/\<TMDB_id\>/reviews |  | { statuscode: 400, Message: “bad request” } | {statuscode: 200, message: “Movie \<name\> reviews retrieved successfully.”,  media : { id: id,  is_movie: false,  TMDB_id: tmdb_id,  “Title”: title }, reviews: \[ { user: {id: userId, username: username }, content: theReview, created: dateCreated, rating: 1.0-10.0, updated: dateUpdated, fromTMDB: true/false}, { \<\<another review\>\> } \]} | GET |
| media_routes | Search Media | /media/search | { query: titleToSearch } | { statuscode: 400, Message: “bad request” } | { data: \[ {TMDB_id: id,  first_air_date: date,  isMovie: false,  name: tvshowName, origin_country: \[ country1, country2 \],  original_language: language,  overview: briefSummary,  poster_url: url, rating: 0-10.0 },  {TMDB_id: id,  release_date: date,  isMovie: true,  title: movieName,   original_language: language,  overview: briefSummary,  poster_url: url, rating: 0-10.0, vote_count: int }, { \<\<another media search result\>\> } \] } | POST |
| media_routes | Get top movies | /media/top/movies |  | { statuscode: 400, Message: “bad request” } | { "message": "Top movies retrieved from TMDB", "movies": \[ {"TMDB_id": id, "isMovie": true, "original_language": language, "overview": briefSummary, "poster_url": url, "rating": 0.0-10.0, "release_date": date, "title": movieTitle, "vote_count": int }, { \<\<another top movie\>\> } \] } | GET |
| media_routes | Get top TV shows | media/top/tvshows |  | { statuscode: 400, Message: “bad request” } | { "message": "Top TV shows retrieved from TMDB", "statuscode": 200, "tvshows": \[ {"TMDB_id": id, "first_air_date": date, "isMovie": false, "name": "Bodies", "origin_country": \[Country1, Country2\], "original_language": language, "overview": briefSummary, "poster_url":url, "rating": 0.0-10.0}, { \<\<another top tvshow \>\> } \] } | GET | 
| media_route | Get TV Show by Id | media/tv/\<TMDB_id\> |  | { statuscode: 400, Message: “bad request” } | {"message": "TV show with id: \<TMDB_id\> retrieved from TMDB", "statuscode": 200, "tvshow": {"TMDB_id": id, "episode_runtime": [], "first_air_date": date, "genres": \[Genre1,Genre2\], "isMovie": false, "last_air_date": date, "name": tvShowName, "number_of_episodes": int, "number_of_seasons": int, "origin_country": \[country1, country2\], "original_language": language, "overview": briefSummary, "poster_url": url, "providers": [], "rating": 0.0-10.0,  status:(Rumored, Planned, In Production, Post Production, Released, Cancelled), "vote_count": int} } | GET |
| media_routes | Get TV shows reviews | media/tv/\<TMDB_id\>/reviews | { statuscode: 400, Message: “bad request” } | { "media": {"TMDB_id": "100088", "id": null, "isMovie": false, "title": null},  reviews: \[ { user: {id: userId, username: username }, content: theReview, created: dateCreated, rating: 1.0-10.0, updated: dateUpdated, fromTMDB: true/false}, { <<another review>> } \], "message": "Reviews for tvshow with id: \<TMDB_id\>  retrieved Successfully",  "statuscode": 200 } | GET |
| user_routes | Get watchlist for user | /users/\<user_id\>/watchlist |  | { statuscode: 500, message: ‘server error’ } | {"message": "Successfully getting \<username\> watchlist.", "statuscode": 200, "watchlist": \[ { "id": int, "media": { "TMDB_id": id, "isMovie": true, "original_language": "en", "overview": BriefSummary, "poster_url": url, "rating": 8.425, "release_date": date, "title": Title, "vote_count": 4609 },  "user": {"id": int, "username": username }, "watched": false }, { \<\<Another entry \>\> } \] } | GET |
| user_routes | Get watched list for user | /users/\<user_id\>/watched |  | { statuscode: 500, message: ‘server error’ } | {"message": "Successfully getting \<username\> watchlist.", "statuscode": 200, "watched": \[ { "id": int, "media": { "TMDB_id": id, "isMovie": true, "original_language": "en", "overview": BriefSummary, "poster_url": url, "rating": 8.425, "release_date": date, "title": Title, "vote_count": 4609 },  "user": {"id": int, "username": username }, "watched": true }, { \<\<Another entry \>\> } \] } | GET |

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
