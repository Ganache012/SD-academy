# 1. 웹의 동작 방식

## 1. Server - Client
- 네트워크 통신의 기본적인 구조
- 1:N
- 1:1 (Peer 2 peer)

### 1.1 protocol stack

1. OSI 7 Layer
    - 네트워크를 7개로 나눈 표준
    1. 물리계층(Physical): 통신에 필요한 모든 물리적인 표준
    2. 데이터 링크(Data-link): 하드웨어 주소(MAC)을 사용
    3. 인터넷 계층(Internet): IP주소를 사용
    4. 전송계층(Transfer): TCP, UDP
    5. 세션계층: 추상적인 계층
    6. Presentation: 추상적인 계층
    7. 응용계층(Application): HTTP, SSH, ...

2. 인터넷 5계층(비표준)
    - 실제 네트워크 구조를 반영함
    1. 물리계층(Physical)
    2. 링크 계층
    3. 네트워크 계층
    4. 전송계층(Transfer)
    5. 응용계층(Application)

## 2. 클라이언트 소캣 프로그램
    - 실습 사이트
    https://overthewire.org/wargames/vortex/vortex0.html

## 3. HTTP
    - 웹서버(web server)와 통신하기
    - Hyper Text Transfer Protocol
  웹 통신은 크게 두 가지로 나눠진다.
  4.1 요청(Request)
    - 요청 헤더(request header)
    ```
     start line(request-line)\r\n
      header-field\r\n
      \r\n
      body
    ```

    2.  request-line
    - 요청헤더의 start-line을 request-line이라고 한다.
    ```
        METHOD SP URL(URI) SP VERSION
    ```
    METHOD
        - GET(요청방식): 전달하려는 매개변수를 URL(URI)를 통해 전달하는 방식, 매개변수를 헤더를 통해서 전달.
        - POST(요청방식): 전달하려는 매개변수를 Body를 통해서 전달하는 방식
        - PUT
        - DELETE
        - OPTIONS
        - HEAD
    
    URL(URI)

    ```
        Protocol:// PATH ? 변수 = 값 & 변수 = 값 & ...

        구분자: '://', '?', '&'
    ```

    URL(Unified Resource Location)
    - 요청하는 자원의 위치를 사용

    URI(Unified Resource Identification)
    - 요청하는 자원의 식별자를 사용

  4.2 응답(Response)
    - 응답 헤더(response header)
    ```
     start line(respose-line)\r\n
      header-field\r\n
      \r\n
      body
    ```

    2. response-line
    ```
        VERSION SP STATUS-CODE SP STATUS-CHAR CRLF
    ```

# 2. 웹 프로그래밍

    - codepen.io
## 1. HTML

 - 블록 태그, 인라인 태그
 - 문서에 대한 구조를 표현, 미디어 태그
### 1.1 태그란?
    - Tag
    - "<",">"를 이용하여 표현
    - 1쌍을 이루어서 사용한다. (sample)
    ```
        <tag name>내용</tag name>
        <tag name/> self closing

        <tagName attribute1, attribute2, ....>
    ```
### 1.2 문서의 구조를 나타내는 태그
    1. 제목 태그
    ```
        <h1>제목</h1>
        <h2>제목</h2>
        <h3>제목</h3>
        <h4>제목</h4>
        <h5>제목</h5>
        <h6>제목</h6>
    ```
### 1.3 계층 구조
    - HTML 문서의 기본 구조
    ```
        <!Doctype>
        <html>
            <head></head>
            <body></body>
        </html>
    ```
    
## 2. CSS

## 3. Script