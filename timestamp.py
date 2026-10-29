select timestamp_seconds(0);
select current_time();
select current_date();
select current_timestamp();
select current_timezone();
select date_format(current_timestamp(), 'yyyy-MM-dd HH:mm:ss');

#adding months to timestamp
select add_months(current_timestamp, 1);
select add_months('2016-08-31', 1);
select add_months('2016-08-31', -6);

#getting day,hour,minute values
select month(current_timestamp());
select dayofmonth(current_timestamp());
select dayofweek(current_timestamp());
select dayofyear(current_timestamp());
select hour(current_timestamp());
select minute(current_timestamp());
select second(current_timestamp());

#getting unix timestamp
select unix_timestamp();
select unix_timestamp(current_timestamp());
select unix_timestamp(current_timestamp(), 'yyyy-MM-dd HH:mm:ss');
select unix_timestamp('2022-01-01 00:00:00', 'yyyy-MM-dd HH:mm:ss');

#extracting particular part of timestamp
select extract(year from current_timestamp());
select extract(month from current_timestamp());
select extract(day from current_timestamp());
select extract(hour from current_timestamp());
select extract(minute from current_timestamp());
select extract(second from current_timestamp());
select extract(dayofweek from current_timestamp());
select extract(dayofyear from current_timestamp());
select extract(dayofmonth from current_timestamp());
