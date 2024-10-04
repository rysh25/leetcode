use std::{cmp::min, collections::HashMap};

pub struct Solution;

impl Solution {
    pub fn min_subarray(nums: Vec<i32>, p: i32) -> i32 {
        let n = nums.len();
        let sum: i64 = nums.iter().map(|&x| x as i64).sum();

        let r: i64 = sum % p as i64;

        if r == 0 {
            return 0;
        }

        let mut prefix_sum: i64 = 0;
        let mut prefix_map: HashMap<i64, i32> = HashMap::new();
        prefix_map.insert(0, -1);
        let mut min_len = nums.len() as i32;

        for (i, num) in nums.iter().enumerate() {
            prefix_sum += *num as i64;
            let curr = prefix_sum.rem_euclid(p as i64);

            let target = (curr - r).rem_euclid(p as i64);
            if prefix_map.contains_key(&target) {
                min_len = min(min_len, i as i32 - *prefix_map.get(&target).unwrap());
            }

            prefix_map.insert(curr, i as i32);
        }

        if min_len < n as i32 {
            min_len as i32
        } else {
            -1
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert_eq!(Solution::min_subarray(vec![3, 1, 4, 2], 6), 1,);
    }

    #[test]

    fn test_2() {
        assert_eq!(Solution::min_subarray(vec![6, 3, 5, 2], 9), 2,);
    }

    #[test]

    fn test_3() {
        assert_eq!(Solution::min_subarray(vec![1, 2, 3], 3), 0,);
    }

    #[test]

    fn test_4() {
        assert_eq!(
            Solution::min_subarray(vec![1000000000, 1000000000, 1000000000], 3),
            0,
        );
    }
}
