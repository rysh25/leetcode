use std::cmp::min;

pub struct Solution;

impl Solution {
    /// - Time complexity: O(n)
    /// - Space complexity: O(1)
    pub fn find_min_difference(mut time_points: Vec<String>) -> i32 {
        let n = time_points.len();
        time_points.sort();

        let mut ans = 1001001001;

        let mut prev_hour: i32 = (&time_points[0])[0..2].parse().unwrap();
        let mut prev_min: i32 = (&time_points[0])[3..5].parse().unwrap();

        for i in 0..n {
            let hour: i32 = (&time_points[(i + 1) % n])[0..2].parse().unwrap();
            let minute: i32 = (&time_points[(i + 1) % n])[3..5].parse().unwrap();

            let diff = (24 * 60 + hour * 60 + minute - prev_hour * 60 - prev_min) % (24 * 60);

            ans = min(ans, diff);

            prev_hour = hour;
            prev_min = minute;
        }

        ans
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert_eq!(
            Solution::find_min_difference(vec!["23:59".to_string(), "00:00".to_string()]),
            1
        );
    }

    #[test]

    fn test_2() {
        assert_eq!(
            Solution::find_min_difference(vec![
                "00:00".to_string(),
                "23:59".to_string(),
                "00:00".to_string()
            ]),
            0
        );
    }
    #[test]

    fn test_3() {
        assert_eq!(
            Solution::find_min_difference(vec!["12:12".to_string(), "12:13".to_string()]),
            1
        );
    }
}
