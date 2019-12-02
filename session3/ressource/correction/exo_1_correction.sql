drop table if exists photos_hashtags;
drop table if exists hashtags;
drop table if exists likes;
drop table if exists comments;
drop table if exists photos;
drop table if exists users;

create table users
(
    -- primary key
    id                serial
        constraint user_pk
            primary key,

    -- detail columns
    username          varchar(255),
    email             varchar(255),
    salted_password   varchar(512),
    first_name        varchar(255),
    last_name         varchar(255),
    last_connected_ip varchar(15),
    registration_date timestamp,
    last_login_date   timestamp
);

create table photos
(
    -- primary key
    id               serial
        constraint photo_pk
            primary key,

    -- detail columns
    caption          varchar(255),
    latitude         numeric(9, 6),
    longitude        numeric(9, 6),
    image_path       varchar(1024),
    image_size       int,
    creation_date    timestamp,
    last_update_date timestamp,

    -- foreign key
    id_user          int
        constraint user_fk
            references users
            on delete cascade
);

create table comments
(
    -- primary key
    id       serial
        constraint comment_pk
            primary key,

    -- detail columns
    comment  text,

    -- foreign keys
    id_user  int
        constraint user_fk
            references users
            on delete cascade,
    id_photo int
        constraint photo_fk
            references photos
            on delete cascade
);

create table likes
(
    -- primary key
    id            serial
        constraint like_pk
            primary key,

    -- detail columns
    creation_date timestamp,

    -- foreign keys
    id_user       int
        constraint user_fk
            references users
            on delete cascade,
    id_photo      int
        constraint photo_fk
            references photos
            on delete cascade
);

create table hashtags
(
    -- primary key
    id      serial
        constraint hashtag_pk
            primary key,

    -- detail columns
    hashtag varchar(50)
);

create table photos_hashtags
(
    -- foreign keys
    id_hashtag int
        constraint hashtag_fk
            references hashtags
            on delete cascade,
    id_photo   int
        constraint photo_fk
            references photos
            on delete cascade,

    -- primary key
    primary key (id_hashtag, id_photo)
);