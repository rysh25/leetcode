use std::collections::HashMap;

pub struct Solution;

impl Solution {
    /// - Time complexity: O(n + k)
    /// - Space complexity: O(k)
    pub fn can_arrange(arr: Vec<i32>, k: i32) -> bool {
        let n = arr.len();
        let mut r: HashMap<i32, i32> = HashMap::new();

        for &num in &arr {
            *r.entry(((num % k) + k) % k).or_insert(0) += 1;
        }

        if *r.get(&0).unwrap_or(&0) % 2 != 0 {
            return false;
        }

        if k % 2 == 0 && *r.get(&(k / 2)).unwrap_or(&0) % 2 != 0 {
            return false;
        }

        let e = ((k + 1) / 2) as usize;

        for i in 1..e {
            if *r.get(&(i as i32)).unwrap_or(&0) != *r.get(&(k - i as i32)).unwrap_or(&0) {
                return false;
            }
        }

        true
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert!(Solution::can_arrange(
            vec![1, 2, 3, 4, 5, 10, 6, 7, 8, 9],
            5
        ));
    }

    #[test]

    fn test_2() {
        assert!(Solution::can_arrange(vec![1, 2, 3, 4, 5, 6], 7));
    }

    #[test]

    fn test_3() {
        assert!(!Solution::can_arrange(vec![1, 2, 3, 4, 5, 6], 10));
    }

    #[test]

    fn test_4() {
        assert!(!Solution::can_arrange(vec![5, 5, 1, 2, 3, 4], 10));
    }
}
