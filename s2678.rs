pub struct Solution;

impl Solution {
    pub fn count_seniors(details: Vec<String>) -> i32 {
        let mut ans = 0;
        for detail in details {
            let age = &detail[11..13];
            if age.parse::<i32>().unwrap() > 60 {
                ans += 1;
            }
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
            Solution::count_seniors(vec![
                "7868190130M7522".to_string(),
                "5303914400F9211".to_string(),
                "9273338290F4010".to_string()
            ]),
            2
        );
    }

    #[test]

    fn test_2() {
        assert_eq!(
            Solution::count_seniors(vec![
                "1313579440F2036".to_string(),
                "2921522980M5644".to_string()
            ]),
            0
        );
    }
}
