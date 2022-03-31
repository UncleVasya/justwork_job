# justwork_job
Test task for JustWork company


# Installation:

```
git clone https://github.com/UncleVasya/justwork_job.git

cd justwork_job

docker-compose up runserver
```

------------------

# Usage

## Admin panel url:
```
http://localhost:8000/admin
```

credentials:
`admin:admin`

- page content sorting is done by dragging inline page elements;
- any page content can be added or edited from Page admin panel;
- added autocomplete for fast selection of page content pieces;


## API Web interface:
```
http://localhost:8000/api
```

## Celery Flower Dashboard (to see executed tasks)
```
http://localhost:5555
```

# API usage examples:

1. Pages list endpoint:

`curl -v http://localhost:8000/api/pages/`

Result:
```
*   Trying 127.0.0.1:8000...
* Connected to localhost (127.0.0.1) port 8000 (#0)
> GET /api/pages/ HTTP/1.1
> Host: localhost:8000
> User-Agent: curl/7.79.1
> Accept: */*
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Date: Thu, 31 Mar 2022 02:21:39 GMT
< Server: WSGIServer/0.2 CPython/3.8.13
< Content-Type: application/json
< Vary: Accept, Cookie
< Allow: GET, HEAD, OPTIONS
< X-Frame-Options: DENY
< Content-Length: 4437
< X-Content-Type-Options: nosniff
< Referrer-Policy: same-origin
{
	"count": 302,
	"next": "http://localhost:8000/api/pages/?page=2",
	"previous": null,
	"results": [{
			"id": 302,
			"title": "Interesting stuff 302",
			"url": "http://localhost:8000/api/pages/302/"
		}, {
			"id": 301,
			"title": "Content by Vasya 301",
			"url": "http://localhost:8000/api/pages/301/"
		}, {
			"id": 300,
			"title": "Stories by Vova 300",
			"url": "http://localhost:8000/api/pages/300/"
		}, {
			"id": 299,
			"title": "Interesting stuff 299",
			"url": "http://localhost:8000/api/pages/299/"
		}, 
		... 
	]
}
```

2. Page detail endpoint:

`curl -v http://localhost:8000/api/pages/202/`

Result:
```
* Trying 127.0.0.1: 8000...
 * TCP_NODELAY set
 * Connected to localhost(127.0.0.1)port 8000( # 0)
 > GET / api / pages / 202 / HTTP / 1.1
 > Host: localhost: 8000
 > User - Agent: curl / 7.68.0
 > Accept:  * /*
>
 * Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Date: Thu, 31 Mar 2022 03:20:09 GMT
< Server: WSGIServer/0.2 CPython/3.8.12
< Content-Type: application/json
< Vary: Accept, Cookie
< Allow: GET, HEAD, OPTIONS
< X-Frame-Options: DENY
< Content-Length: 852
< X-Content-Type-Options: nosniff
< Referrer-Policy: same-origin
{
	"url": "http://localhost:8000/api/pages/202/",
	"id": 202,
	"pieces": [{
			"id": 553,
			"title": "Funny cats 353",
			"counter": 2,
			"video_url": "https://justwork-tube.com/video/353",
			"subtitles_url": "https://justwork-tube.com/subtitles/353",
			"resourcetype": "VideoPiece"
		}, {
			"id": 589,
			"title": "Funny cats 389",
			"counter": 2,
			"video_url": "https://justwork-tube.com/video/389",
			"subtitles_url": "https://justwork-tube.com/subtitles/389",
			"resourcetype": "VideoPiece"
		}, {
			"id": 403,
			"title": "Movie review 403",
			"counter": 2,
			"text": "bla bla bla 403",
			"resourcetype": "TextPiece"
		}, {
			"id": 393,
			"title": "Movie review 393",
			"counter": 2,
			"text": "bla bla bla 393",
			"resourcetype": "TextPiece"
		}, {
			"id": 577,
			"title": "Funny cats 377",
			"counter": 2,
			"video_url": "https://justwork-tube.com/video/377",
			"subtitles_url": "https://justwork-tube.com/subtitles/377",
			"resourcetype": "VideoPiece"
		}
	],
	"title": "Stories by Vova 202"
}
```
# Running tests:
`docker-compose run autotests`

