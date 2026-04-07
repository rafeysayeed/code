/* Write your T-SQL query statement below */
WITH StartTime AS
(
    SELECT
        machine_id,
        process_id,
        timestamp AS TimeStart
    FROM
        Activity
    WHERE
        activity_type = 'start'
),
EndTime AS
(
    SELECT
        machine_id,
        process_id,
        timestamp AS TimeEnd
    FROM
        Activity
    WHERE
        activity_type = 'end'
),
TimeDifference AS
(
    SELECT
        S.machine_id,
        S.process_id,
        timeEnd - TimeStart AS DifferenceTime
    FROM
        StartTime S
    JOIN
        EndTime E
    ON
        S.machine_id = E.machine_id
    AND
        S.process_id = E.process_id
)

SELECT machine_id, ROUND(AVG(DifferenceTime),3) AS processing_time FROM TimeDifference GROUP BY machine_id