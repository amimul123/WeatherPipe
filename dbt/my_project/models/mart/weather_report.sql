{{
    config(
        materialized='table',
        unique_key='id'
    )
}}

select
        lat,
        long,
        insert_date as date,
        round(avg(temp)::numeric, 2) as avg_temp,
        count(temp) as tot_temp

from    {{ref('stg_weather_data')}}
group by    1, 2, 3
order by    date asc