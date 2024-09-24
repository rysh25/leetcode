use std::{cmp::min, collections::HashSet};

pub struct Solution;

impl Solution {
    pub fn min_extra_char(s: String, dictionary: Vec<String>) -> i32 {
        let max_val = s.len() as i32 + 1;
        let mut dp = vec![max_val; s.len() + 1];
        dp[0] = 0;

        let dictionary_set: HashSet<String> = dictionary.into_iter().collect();

        for i in 1..=s.len() {
            dp[i] = dp[i - 1] + 1;
            for l in 1..=i {
                if dictionary_set.contains(&s[i - l..i]) {
                    dp[i] = min(dp[i], dp[i - l]);
                }
            }
        }
        dp[s.len()] as i32
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert_eq!(
            Solution::min_extra_char(
                "leetscode".to_string(),
                vec![
                    "leet".to_string(),
                    "code".to_string(),
                    "leetcode".to_string()
                ]
            ),
            1
        );
    }

    #[test]

    fn test_2() {
        assert_eq!(
            Solution::min_extra_char(
                "sayhelloworld".to_string(),
                vec!["hello".to_string(), "world".to_string()]
            ),
            3
        );
    }
}
