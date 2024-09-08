select *
from article
left join  comment on article.id = comment.article_id
where article_id is null;
