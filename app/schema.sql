drop table if exists entries;

create table entries (
    id integer primary key autoincrement,
    date_created datetime not null,
    date_modified datetime not null,
    title text not null,
    'text' text not null
);