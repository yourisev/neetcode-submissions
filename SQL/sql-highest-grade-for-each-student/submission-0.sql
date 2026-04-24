select exam_results.student_id as student_id, MIN(exam_id) as exam_id, exam_results.score as score from  exam_results
join (
    select student_id, max(score) as score from exam_results
group by student_id
order by score desc
) as max_score
on exam_results.student_id = max_score.student_id
and exam_results.score = max_score.score
group by exam_results.student_id, exam_results.score
order by exam_results.student_id
