#restfulapi
ubuntu:~/api/djangoresult/api/restfulapi$ curl --location --request POST 'http://127.0.0.1:8080/v1.0/music/' --header 'Content-Type: application/json' --data-raw '{"song":"中国龙","singer":"刘德华"}'
ubuntu:~/api/djangoresult/api/restfulapi$ curl --location --request GET 'http://127.0.0.1:8080/v1.0/music/'
{"code":200,"message":"success","data":[{"id":1,"song":"","singer":"","created":"2023-04-20T08:35:31.526294Z"},{"id":2,"song":"中国龙","singer":"刘德华","created":"2023-04-20T08:38:44.047311Z"},{"id":3,"song":"中国龙","singer":"刘德华","created":"2023-04-20T08:41:20.493172Z"}]}ubuntu:~/api/djangoresult/api/restfulapi$ 
