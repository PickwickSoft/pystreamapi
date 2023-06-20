# Date conditions

All date conditions can be used either with `datetime.datetime` or with `datetime.date`. All examples on this page are using `datetime`, but can be replaced by `date`.

### `before(date)`: Check if date is before another date

Check if a datetime/date is before a given datetime/date.

```python
Stream.of([datetime.now() - timedelta(days=1)])\
    .filter(before(datetime.now()))\
    .for_each(print)  # Output: 2023-06-01 17:03:54.386812
```

### `after(date)`: Check if date is after another date

Check if a datetime/date is after a given datetime/date.

```python
Stream.of([datetime.now() + timedelta(days=1)])\
    .filter(after(datetime.now()))\
    .for_each(print)  # Output: 2023-06-03 17:03:54.386812
```

### `before_or_equal(date)`: Check if date is before or equal to another date

Check if a datetime/date is before or equal to a given datetime/date.

```python
Stream.of([datetime.now() - timedelta(days=1)])\
    .filter(before_or_equal(datetime.now()))\
    .for_each(print)  # Output: 2023-06-01 17:03:54.386812
```

### `after_or_equal(date)`: Check if date is after or equal to another date

Check if a datetime/date is after or equal to a given datetime/date.

```python
Stream.of([datetime.now() + timedelta(days=1)])\
    .filter(after_or_equal(datetime.now()))\
    .for_each(print)  # Output: 2023-06-03 17:03:54.386812
```

### `between_or_equal(start_date, end_date)`: Check if date is between or equal to two dates

Check if a datetime/date is between or equal to two given datetimes/date.

```python
Stream.of([datetime.now() - timedelta(days=2)])\
    .filter(between_or_equal(datetime.now() - timedelta(days=3), datetime.now() - timedelta(days=1)))\
    .for_each(print)  # Output: 2023-06-01 17:03:54.386812
```

### `not_between_or_equal(start_date, end_date)`: Check if date is not between or equal to two dates

Check if a datetime/date is not between or equal to two given datetimes/dates.

```python
Stream.of([datetime.now() - timedelta(days=2)])\
    .filter(not_between_or_equal(datetime.now() - timedelta(days=3), datetime.now() - timedelta(days=1)))\
    .for_each(print)  # Output: (no output)
```

### `today()`: Check if date is today

Check if a datetime/date is today.

```python
Stream.of([datetime.now()])\
    .filter(today())\
    .for_each(print)  # Output: 2023-06-02 17:03:54.386812
```

### `today_utc()`: Check if date is today in UTC

Check if a datetime/date is today (in UTC).

```python
Stream.of([datetime.now(timezone.utc)])\
    .filter(today_utc())\
    .for_each(print)  # Output: 2023-06-02 17:03:54.386812
```

### `yesterday()`: Check if date is yesterday

Check if a datetime/date is yesterday.

```python
Stream.of([datetime.now() - timedelta(days=1)])\
    .filter(yesterday())\
    .for_each(print)  # Output: 2023-06-01 17:03:54.386812
```

### `yesterday_utc()`: Check if date is yesterday in UTC

Check if a datetime/date is yesterday (in UTC).

```python
Stream.of([datetime.now(timezone.utc) - timedelta(days=1)])\
    .filter(yesterday_utc())\
    .for_each(print)  # Output: 2023-06-01 17:03:54.386812
```

### `tomorrow()`: Check if date is tomorrow

Check if a datetime/date is tomorrow.

```python
Stream.of([datetime.now() + timedelta(days=1)])\
    .filter(tomorrow())\
    .for_each(print)  # Output: 2023-06-03 17:03:54.386812
```

### `tomorrow_utc()`: Check if date is tomorrow in UTC

Check if a datetime/date is tomorrow (in UTC).

```python
Stream.of([datetime.now(timezone.utc) + timedelta(days=1)])\
    .filter(tomorrow_utc())\
    .for_each(print)  # Output: 2023-06-03 17:03:54.386812
```

### `this_week()`: Check if date is within the current week

Check if a datetime/date is within the current week.

```python
Stream.of([datetime.now()])\
    .filter(this_week())\
    .for_each(print)  # Output: 2023-06-02 17:03:54.386812
```

### `this_week_utc()`: Check if date is within the current week in UTC

Check if a datetime/date is within the current week (in UTC).

```python
Stream.of([datetime.now(timezone.utc)])\
    .filter(this_week_utc())\
    .for_each(print)  # Output: 2023-06-02 17:03:54.386812
```

### `last_week()`: Check if date is within the previous week

Check if a datetime/date is within the previous week.

```python
Stream.of([datetime.now() - timedelta(weeks=1)])\
    .filter(last_week())\
    .for_each(print)  # Output: 2023-05-26 17:03:54.386812
```

### `last_week_utc()`: Check if date is within the previous week in UTC

Check if a datetime/date is within the previous week (in UTC).

```python
Stream.of([datetime.now(timezone.utc) - timedelta(weeks=1)])\
    .filter(last_week_utc())\
    .for_each(print)  # Output: 2023-05-26 17:03:54.386812
```

### `next_week()`: Check if date is within the next week

Check if a datetime/date is within the next week.

```python
Stream.of([datetime.now() + timedelta(weeks=1)])\
    .filter(next_week())\
    .for_each(print)  # Output: 2023-06-09 17:03:54.386812
```

### `next_week_utc()`: Check if date is within the next week in UTC

Check if a datetime/date is within the next week (in UTC).

```python
Stream.of([datetime.now(timezone.utc) + timedelta(weeks=1)])\
    .filter(next_week_utc())\
    .for_each(print)  # Output: 2023-06-09 17:03:54.386812
```

### `this_month()`: Check if date is within the current month

Check if a datetime/date is within the current month.

```python
Stream.of([datetime.now()])\
    .filter(this_month())\
    .for_each(print)  # Output: 2023-06-02 17:03:54.386812
```

### `this_month_utc()`: Check if date is within the current month in UTC

Check if a datetime/date is within the current month (in UTC).

```python
Stream.of([datetime.now(timezone.utc)])\
    .filter(this_month_utc())\
    .for_each(print)  # Output: 2023-06-02 17:03:54.386812
```

### `last_month()`: Check if date is within the previous month

Check if a datetime/date is within the previous month.

```python
Stream.of([datetime.now() - relativedelta(months=1)])\
    .filter(last_month())\
    .for_each(print)  # Output: 2023-05-02 17:03:54.386812
```

### `last_month_utc()`: Check if date is within the previous month in UTC

Check if a datetime/date is within the previous month (in UTC).

```python
Stream.of([datetime.now(timezone.utc) - relativedelta(months=1)])\
    .filter(last_month_utc())\
    .for_each(print)  # Output: 2023-05-02 17:03:54.386812
```

### `next_month()`: Check if date is within the next month

Check if a datetime/date is within the next month.

```python
Stream.of([datetime.now() + relativedelta(months=1)])\
    .filter(next_month())\
    .for_each(print)  # Output: 2023-07-02 17:03:54.386812
```

### `next_month_utc()`: Check if date is within the next month in UTC

Check if a datetime/date is within the next month (in UTC).

```python
Stream.of([datetime.now(timezone.utc) + relativedelta(months=1)])\
    .filter(next_month_utc())\
    .for_each(print)  # Output: 2023-07-02 17:03:54.386812
```

### `this_year()`: Check if date is within the current year

Check if a datetime/date is within the current year.

```python
Stream.of([datetime.now()])\
    .filter(this_year())\
    .for_each(print)  # Output: 2023-06-02 17:03:54.386812
```

### `this_year_utc()`: Check if date is within the current year in UTC

Check if a datetime/date is within the current year (in UTC).

```python
Stream.of([datetime.now(timezone.utc)])\
    .filter(this_year_utc())\
    .for_each(print)  # Output: 2023-06-02 17:03:54.386812
```

### `last_year()`: Check if date is within the previous year

Check if a datetime/date is within the previous year.

```python
Stream.of([datetime.now() - relativedelta(years=1)])\
    .filter(last_year())\
    .for_each(print)  # Output: 2022-06-02 17:03:54.386812
```

### `last_year_utc()`: Check if date is within the previous year in UTC

Check if a datetime/date is within the previous year (in UTC).

```python
Stream.of([datetime.now(timezone.utc) - relativedelta(years=1)])\
    .filter(last_year_utc())\
    .for_each(print)  # Output: 2022-06-02 17:03:54.386812
```

### `next_year()`: Check if date is within the next year

Check if a datetime/date is within the next year.

```python
Stream.of([datetime.now() + relativedelta(years=1)])\
    .filter(next_year())\
    .for_each(print)  # Output: 2024-06-02 17:03:54.386812
```

### `next_year_utc()`: Check if date is within the next year in UTC

Check if a datetime/date is within the next year (in UTC).

```python
Stream.of([datetime.now(timezone.utc) + relativedelta(years=1)])\
    .filter(next_year_utc())\
    .for_each(print)  # Output: 2024-06-02 17:03:54.386812
```
