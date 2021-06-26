with users as (
    select * 
    from transactions t1
),

exchange_rates as (
    select * 
    from exchange_rates er1
    where ts = (
        SELECT max(ts) 
        from exchange_rates er2
        where er1.from_currency = er2.from_currency
    )

),

joined_rates as (
    select 
        users.ts,
        users.user_id,
        users.currency,
        users.amount,
        coalesce(exchange_rates.rate,1) as exchange_rate
    from users
    left join exchange_rates
    on users.currency = exchange_rates.from_currency
    and exchange_rates.to_currency = 'GBP'
)

select 
    user_id,
    sum(exchange_rate * amount) as amount_GBP
from joined_rates
group by user_id
