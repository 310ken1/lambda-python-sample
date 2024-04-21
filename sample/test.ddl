-- Project Name : noname
-- Date/Time    : 2024/04/21 22:59:32
-- Author       : 
-- RDBMS Type   : PostgreSQL
-- Application  : A5:SQL Mk-2

/*
  << 注意！！ >>
  BackupToTempTable, RestoreFromTempTable疑似命令が付加されています。
  これにより、drop table, create table 後もデータが残ります。
  この機能は一時的に $$TableName のような一時テーブルを作成します。
  この機能は A5:SQL Mk-2でのみ有効であることに注意してください。
*/

-- data
-- * RestoreFromTempTable
create table data (
  id serial not null
  , name text
  , age integer
  , constraint data_PKC primary key (id)
) ;

comment on table data is 'data';
comment on column data.id is 'id';
comment on column data.name is 'name';
comment on column data.age is 'age';

