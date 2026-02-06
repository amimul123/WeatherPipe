{{
    config(
        materialized = 'table',
        unique_key = 'id'
    )
}}

with source as (
    select *
    from    {{source('dev','raw_weather_data')}}
)

select
        *,
        inserted_at::date as insert_date,
        extract(HOUR from inserted_at) as hour,
        extract(MINUTE from inserted_at) as minute,
        extract(SECOND from inserted_at)::int as second

from    source
