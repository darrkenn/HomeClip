FROM golang:alpine as build

WORKDIR /build
COPY . .

ENV CGO_ENABLED=1
RUN apk add --no-cache build-base

RUN go mod tidy
RUN go mod vendor
RUN go build -o app .



FROM alpine



WORKDIR /app
RUN mkdir db

COPY --from=build /build/app ./app
COPY --from=build /build/templates ./templates/
COPY --from=build /build/static ./static/

RUN chmod +x ./app

RUN echo "DATABASE=/app/db/links.db" > .env

EXPOSE 3119
CMD ["./app"]