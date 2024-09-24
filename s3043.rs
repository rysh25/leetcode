use std::{cmp::max, collections::HashSet};

pub struct Solution;

impl Solution {
    /// - Time complexty: O(n+m)
    /// - Space complexity: O(n)
    pub fn longest_common_prefix(arr1: Vec<i32>, arr2: Vec<i32>) -> i32 {
        let mut prefix: HashSet<i32> = HashSet::new();

        for i in arr1 {
            let mut x = i;
            while x > 0 {
                prefix.insert(x);

                x /= 10;
            }
        }

        let mut ans: i32 = 0;

        for i in arr2 {
            let mut x = i;
            while x > 0 {
                // println!("x={:?}", x);
                if prefix.contains(&x) {
                    let l = x.to_string().len() as i32;
                    // println!("l={:?}", l);
                    ans = max(ans, l);
                    break;
                }

                x /= 10;
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
            Solution::longest_common_prefix(vec![1, 10, 100], vec![1000]),
            3
        );
    }

    #[test]

    fn test_2() {
        assert_eq!(
            Solution::longest_common_prefix(vec![1, 2, 3], vec![4, 4, 4]),
            0
        );
    }

    #[test]

    fn test_3() {
        assert_eq!(Solution::longest_common_prefix(vec![10], vec![17, 11]), 1);
    }
}
