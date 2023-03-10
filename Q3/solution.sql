select owner_id, owner_name, count(category_id) as different_category_count
from (select article_id, owner_id, owner_name
from (select *
from owner a
inner join article b
on a.owner_id = b.owner_id) owner_article
inner join (select category_id
from category
inner join category_article_mapping
on category.category_id = category_article_mapping.category_id) mapping
on owner_article.article_id = mapping.article_id) table1
group by owner_id
order by different_category_count desc

