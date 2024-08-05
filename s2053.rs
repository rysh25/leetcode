use std::collections::HashMap;

pub struct Solution;

impl Solution {
    /// - Time complexity: O(n)
    /// - Space complexity: O(n)
    ///
    /// #HashTable
    pub fn kth_distinct(arr: Vec<String>, k: i32) -> String {
        let mut count: HashMap<String, i32> = HashMap::new();

        for a in &arr {
            *count.entry(a.clone()).or_insert(0) += 1;
        }

        let mut c = 0;
        for a in arr {
            if count[&a] == 1 {
                c += 1;

                if c == k {
                    return a;
                }
            }
        }

        "".to_string()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert_eq!(
            Solution::kth_distinct(
                vec![
                    "d".to_string(),
                    "b".to_string(),
                    "c".to_string(),
                    "b".to_string(),
                    "c".to_string(),
                    "a".to_string()
                ],
                2
            ),
            "a"
        );
    }

    #[test]

    fn test_2() {
        assert_eq!(
            Solution::kth_distinct(
                vec!["aaa".to_string(), "aa".to_string(), "a".to_string()],
                1
            ),
            "aaa"
        );
    }

    #[test]

    fn test_3() {
        assert_eq!(
            Solution::kth_distinct(vec!["a".to_string(), "b".to_string(), "a".to_string()], 3),
            ""
        );
    }
}
