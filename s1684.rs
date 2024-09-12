use std::collections::HashSet;

pub struct Solution;

impl Solution {
    /// - Time complexity: O(l + n * m)
    /// - Space complexity: O(l)
    pub fn count_consistent_strings(allowed: String, words: Vec<String>) -> i32 {
        let s: HashSet<char> = HashSet::from_iter(allowed.chars());

        let mut ans = 0;

        for w in words {
            let mut is_consisting = true;

            for c in w.chars() {
                if !s.contains(&c) {
                    is_consisting = false;
                }
            }

            if is_consisting {
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
            Solution::count_consistent_strings(
                "ab".to_string(),
                vec![
                    "ad".to_string(),
                    "bd".to_string(),
                    "aaab".to_string(),
                    "baa".to_string(),
                    "badab".to_string()
                ]
            ),
            2
        );
    }

    #[test]

    fn test_2() {
        assert_eq!(
            Solution::count_consistent_strings(
                "abc".to_string(),
                vec![
                    "a".to_string(),
                    "b".to_string(),
                    "c".to_string(),
                    "ab".to_string(),
                    "ac".to_string(),
                    "bc".to_string(),
                    "abc".to_string()
                ]
            ),
            7
        );
    }

    #[test]

    fn test_3() {
        assert_eq!(
            Solution::count_consistent_strings(
                "cad".to_string(),
                vec![
                    "cc".to_string(),
                    "acd".to_string(),
                    "b".to_string(),
                    "ba".to_string(),
                    "bac".to_string(),
                    "bad".to_string(),
                    "ac".to_string(),
                    "d".to_string()
                ]
            ),
            4
        );
    }
}
