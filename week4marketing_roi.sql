
 --Ühenda müük, kliendid ja veebilogi kanalitega:
SELECT
w.source AS turunduskanal,
COUNT(DISTINCT c.customer_id) AS kliente,
COUNT(DISTINCT o.sale_id) AS tellimusi,
SUM(o.total_price) AS kogukäive,
ROUND(AVG(o.total_price), 2) AS keskmine_tellimus
FROM sales o JOIN customers c ON o.customer_id = c.customer_id
LEFT JOIN web_logs w ON c.customer_id = w.customer_id
GROUP BY w.source
ORDER BY kogukäive DESC; 

Select sum(total_price) from sales --kogumüük 2909177.98
Select channel, sum(total_price) as kogumüük from sales group by channel order by kogumüük --Palju on reaalne müük  Online 1006747,68 Pood 1902430,30

--Iga müük vaid ühes kanalis (eemalda topelt kanded) et kogumüük klapiks tegeliku müügiga
WITH esimene_kanal AS (
    SELECT DISTINCT ON (customer_id)
        customer_id,
        source
    FROM web_logs
    ORDER BY customer_id, visit_date)
SELECT
    ek.source AS turunduskanal,
    COUNT(DISTINCT o.customer_id) AS kliente,
    COUNT(DISTINCT o.sale_id) AS tellimusi,
    SUM(o.total_price) AS kogukaive,
    ROUND(AVG(o.total_price), 2) AS keskmine_tellimus
FROM sales o
LEFT JOIN esimene_kanal ek
    ON o.customer_id = ek.customer_id
GROUP BY ek.source
ORDER BY kogukaive DESC;

--Kampaaniate kuised trendid
SELECT
w.source AS turunduskanal,
    DATE_TRUNC('month', o.sale_date) AS kuu,
    COUNT(DISTINCT o.sale_id) AS tellimusi,
    COUNT(DISTINCT o.customer_id) AS unikaalsed_kliendid,
    SUM(o.total_price) AS kogukäive
FROM sales o JOIN customers c
ON o.customer_id = c.customer_id
LEFT JOIN web_logs w ON c.customer_id = w.customer_id
GROUP BY
w.source,
DATE_TRUNC('month', o.sale_date)
HAVING COUNT(DISTINCT o.sale_id) > 50
ORDER BY
kuu, kogukäive asc;

-- Kampaaniate kuised trendid viimane aasta (Märts2024-Veeb2025)
SELECT
    w.source AS turunduskanal,
    DATE_TRUNC('month', o.sale_date) AS kuu,
    COUNT(DISTINCT o.sale_id) AS tellimusi,
    COUNT(DISTINCT o.customer_id) AS unikaalsed_kliendid,
    SUM(o.total_price) AS kogukäive
FROM sales o JOIN customers c
ON o.customer_id = c.customer_id
LEFT JOIN web_logs w ON c.customer_id = w.customer_id
WHERE o.sale_date >= '2024-03-01' AND o.sale_date < '2025-03-01'
GROUP BY
w.source,
DATE_TRUNC('month', o.sale_date)
HAVING COUNT(DISTINCT o.sale_id) > 30
ORDER BY
kuu,
kogukäive DESC;

--Kas Online liiklus/reklaamid on seotud tavapoe müükidega?  Jah = vigane
SELECT
    w.source AS turunduskanal,
    COUNT(DISTINCT o.sale_id) AS tavapoe_müügid,
    SUM(o.total_price) AS tavapoe_käive
FROM sales o LEFT JOIN web_logs w
    ON o.customer_id = w.customer_id
WHERE o.channel = 'pood'
GROUP BY w.source
ORDER BY tavapoe_käive DESC;
