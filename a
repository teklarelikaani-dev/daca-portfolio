
--ALAÜLESANDE KAART C: Tooteandmete Puhastamine
CREATE TABLE products_test AS SELECT * FROM products; --Loo tabel
SELECT COUNT(*) AS ridade_arv FROM products_test;  --Kontolli ridade arv  362
SELECT product_name, COUNT(*) AS koopiate_arv   --Duplikaadid — kas on korduvaid tootenimesid  12 duplikaatset tootenime
FROM products_test
GROUP BY product_name
HAVING COUNT(*) > 1 ORDER BY koopiate_arv DESC;            

-- NULL väärtused kriitilistes väljades
SELECT
    COUNT(*) FILTER (WHERE product_name IS NULL OR product_name = '') AS null_nimi,   --null nimmi=0
    COUNT(*) FILTER (WHERE category IS NULL OR category = '') AS null_kategooria,     --null kategooria =0
    COUNT(*) FILTER (WHERE retail_price IS NULL) AS null_jaehind,                     -- null jaehind =0
    COUNT(*) FILTER (WHERE cost_price IS NULL) AS null_omahind                        --null omahind=0
FROM products_test;
-- Kas on negatiivseid hindu?   ei ole
SELECT COUNT(*) AS negatiivne_hind FROM products_test WHERE retail_price < 0;
-- Kas on äärmuslikke hindu (> 1000€)?  Ei ole tooteid, mille hind oleks suurem kui 1000€
SELECT product_name, retail_price FROM products_test WHERE retail_price > 1000 ORDER BY retail_price DESC;
--Katergooriate järjekindlus
SELECT category, COUNT(*) AS arv FROM products_test GROUP BY category ORDER BY category;

-- Ühtlusta kategooriate nimed
UPDATE products_test
SET category = INITCAP(TRIM(category))
WHERE category != INITCAP(TRIM(category));
