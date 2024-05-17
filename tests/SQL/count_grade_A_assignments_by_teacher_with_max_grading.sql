SELECT COUNT(*) AS grade_A_count
FROM assignments
WHERE teacher_id = (
    SELECT teacher_id
    FROM (
        SELECT teacher_id, COUNT(*) AS num_graded_assignments
        FROM assignments
        WHERE state = 'GRADED'
        GROUP BY teacher_id
        ORDER BY num_graded_assignments DESC
        LIMIT 1
    ) AS max_grading
)
AND grade = 'A';
